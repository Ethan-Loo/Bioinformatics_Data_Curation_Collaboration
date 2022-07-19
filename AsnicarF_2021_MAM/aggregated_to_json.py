# import pprint
# from pathlib import Path
# yaml_dumper from linkml_runtime.dumpers
# import math
import re
from typing import Dict

import click
import pandas as pd
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import json_dumper
from linkml_runtime.linkml_model import EnumDefinition

import curated_schema as cs

import logging
import click_log

multivalued_delimiter = ";"

col_mappings = {"alt": "ALT"}

# todo: verbosity/logging level stuck on debug?

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--tsv_in_file", type=click.Path(exists=True), required=True)
@click.option("--schema_file", type=click.Path(exists=True), required=True)
@click.option("--json_out_file", type=click.Path(), required=True)
@click.option("--project_name", required=True)
def cli(tsv_in_file: str, schema_file: str, project_name: str, json_out_file: str):
    """
    Break the aggregated TSV into samples, studies and a project
    Write back out as schema-compliant JSON.
    """

    agg_data = pd.read_csv(tsv_in_file, sep="\t", low_memory=False)

    schema = SchemaView(schema_file)

    studies = agg_data["study_name"].unique().tolist()
    studies.sort()

    obj_list = []
    # "ChengpingW_2017"
    for i in studies:
        logger.warning(i)
        current_study = make_study(i, agg_data, schema)
        obj_list.append(current_study)

    logger.warning("\nPlease wait, assembling project...")

    current_project = make_project(project_name)
    current_project.studies = obj_list

    # don't want these alpha-sorted
    # when does that happen?

    json_dumper.dump(current_project, json_out_file)


def make_sample(sample_dict: Dict, schema: SchemaView) -> cs.Sample:
    """
    Make a sample from one row of data.
    """
    # todo: refactor this schema extraction out of the function and pass it TO the function
    all_slots = schema.class_induced_slots("Sample")
    all_slot_names = [slot.alias for slot in all_slots]
    all_slots_dict = dict(zip(all_slot_names, all_slots))

    inferred_requireds = [i.alias for i in all_slots if i.required]
    remaining_slots = [i.alias for i in all_slots if i.alias not in inferred_requireds]

    ir_data = {i: sample_dict[i] for i in inferred_requireds}

    curator_hotfix = ir_data["curator"]
    # curator_hotfix = curator_hotfix.split(multivalued_delimiter)
    curator_hotfix = re.split("[;,]", curator_hotfix)

    # todo generalize this
    curator_hotfix = list(
        map(lambda x: x.replace("Giacomo_Damato", "Giacomo_DAmato"), curator_hotfix)
    )
    curator_hotfix = list(
        map(
            lambda x: x.replace("Mireia_VallesColomer", "Mireia_Valles-Colomer"),
            curator_hotfix,
        )
    )
    curator_hotfix = list(set(curator_hotfix))
    curator_hotfix.sort()

    ir_data["curator"] = curator_hotfix

    gender_hotfix = ir_data["gender"]
    gender_enum = schema.get_enum("Gender")
    # gender_pvs = list(gender_enum.permissible_values.keys())
    # if gender_hotfix not in gender_pvs:
    #     # logger.warning(f"provided gender: {gender_hotfix}; expected: {gender_pvs}")
    #     gender_hotfix = "NA"
    #
    # ir_data["gender"] = gender_hotfix

    age_hotfix = ir_data["age"]

    try:
        ir_data["age"] = int(age_hotfix)
    except ValueError:
        # logger.warning(f"    age value {age_hotfix} is not an integer")
        ir_data["age"] = "NA"

    current_sample = cs.Sample(**ir_data)

    for i in remaining_slots:

        current_range = all_slots_dict[i]["range"]

        current_range_element = schema.get_element(current_range)
        current_range_type = type(current_range_element).class_name

        current_value = sample_dict[i]
        multivalued = all_slots_dict[i]["multivalued"]

        if current_range == "string":
            # todo extremely short-sighted check for any-of boolean/status_enum
            if len(all_slots_dict[i]["any_of"]) > 0:
                # print(f"{i} {current_value}")
                if current_value == "yes":
                    current_sample[i] = True
                elif current_value == "no":
                    current_sample[i] = False
                else:
                    current_sample[i] = "NA"
            elif current_value and str(current_value) == current_value:
                if multivalued:
                    # todo parameterize this
                    val_list = current_value.split(";")
                    val_list = list(set(val_list))
                    val_list.sort()
                    for current_split in val_list:
                        current_sample[i].append(current_split)
                else:
                    current_sample[i] = current_value
        elif current_range == "float":
            nan_bool = pd.isna(float(current_value))
            # todo any multivalued float slots?
            if not nan_bool:
                try:
                    current_float = float(current_value)
                    current_sample[i] = current_float
                except ValueError:
                    pass
                    # logger.warning(f"    {i} value {current_value} is not a float")
            # else:
            #     logger.warning(f"    blank {i} value")

        elif current_range == "integer":
            # todo any multivalued integer slots?
            if current_value and current_value != "":
                nan_bool = pd.isna(current_value)
                if not nan_bool:
                    try:
                        current_int = int(current_value)
                        current_sample[i] = current_int
                    except ValueError:
                        pass
                        # logger.warning(f"    {i} value {current_value} is not an integer")
            # else:
            #     logger.warning(f"    blank {i} value")

        elif current_range_type == EnumDefinition.class_name:
            if str(current_value) == current_value:
                if multivalued:
                    logger.warning(
                        f"MULTIVALUED ENUM: {i}; current_value: {current_value}; multivalued: {multivalued}"
                    )
                else:
                    if ":" in current_value:
                        logger.warning(
                            f"ERRONEOUS SINGLE-VALUED ENUM: {i}; current_value: {current_value}; multivalued: {multivalued}"
                        )
                    else:
                        current_sample[i] = current_value

        # elif current_range == "boolean":
        #     if current_value and current_value != "":
        #         current_sample[i] = current_value in ["yes"]

        # OTHER slot: premature; current_range: boolean; current range type:type_definition; current_value: nan; multivalued: None

        else:
            logger.warning(
                f"OTHER slot: {i}; current_range: {current_range}; current range type:{current_range_type}; current_value: {current_value}; multivalued: {multivalued}"
            )

    return current_sample


def make_study(
        study_name: str, agg_frame: pd.DataFrame, schema: SchemaView
) -> cs.Study:
    """
    Make a collection of all samples with a shared study name.
    """
    current_data = agg_frame[agg_frame["study_name"] == study_name]
    # logger.info(current_data.head())
    current_study = cs.Study(study_name=study_name)
    sample_list = current_data.to_dict("records")
    object_list = []
    for i in sample_list:
        current_sample = make_sample(i, schema)
        object_list.append(current_sample)

    current_study.samples = object_list

    return current_study


def make_project(project_name: str) -> cs.Project:
    """
    Make a collection of all studies in the curatedMetagenomicDataCuration directory.
    """
    current_project = cs.Project(project_name=project_name)
    return current_project


if __name__ == "__main__":
    cli()
