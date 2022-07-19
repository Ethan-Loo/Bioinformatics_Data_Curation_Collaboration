# Auto generated from curated_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-07-07T14:02:08
# Schema: CMD
#
# id: https://w3id.org/CMD
# description: Curated Metagenomic Data Curation Schema
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CMD = CurieNamespace('CMD', 'https://w3id.org/CMD/')
NCIT = CurieNamespace('NCIT', 'http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CMD


# Types

# Class references



@dataclass
class Sample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CMD.Sample
    class_class_curie: ClassVar[str] = "CMD:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = CMD.Sample

    age: str = None
    body_site: str = None
    country: str = None
    curator: Union[str, List[str]] = None
    gender: str = None
    median_read_length: int = None
    minimum_read_length: int = None
    number_bases: int = None
    number_reads: int = None
    sample_id: str = None
    sequencing_platform: str = None
    subject_id: str = None
    ALT: Optional[float] = None
    ASO: Optional[float] = None
    BASDAI: Optional[float] = None
    BASFI: Optional[float] = None
    BMI: Optional[float] = None
    DNA_extraction_kit: Optional[str] = None
    ESR: Optional[float] = None
    HBI: Optional[float] = None
    HLA: Optional[Union[str, List[str]]] = empty_list()
    NCBI_accession: Optional[Union[str, List[str]]] = empty_list()
    ORR: Optional[str] = None
    PFS12: Optional[str] = None
    PMID: Optional[str] = None
    PPD_B: Optional[float] = None
    PPD_D: Optional[float] = None
    PPD_L: Optional[float] = None
    PPD_M: Optional[float] = None
    RECIST: Optional[str] = None
    SCCAI: Optional[float] = None
    adiponectin: Optional[float] = None
    age_T1D_diagnosis: Optional[float] = None
    age_category: Optional[str] = None
    age_seroconversion: Optional[float] = None
    age_twins_started_to_live_apart: Optional[int] = None
    ajcc: Optional[str] = None
    albumine: Optional[float] = None
    alcohol: Optional[str] = None
    alcohol_numeric: Optional[float] = None
    anti_PD_1: Optional[str] = None
    anti_ccp_antibody: Optional[float] = None
    antibiotics_current_use: Optional[str] = None
    antibiotics_family: Optional[Union[str, List[str]]] = empty_list()
    ast: Optional[float] = None
    autoantibody_positive: Optional[Union[str, List[str]]] = empty_list()
    bilubirin: Optional[float] = None
    birth_control_pil: Optional[str] = None
    birth_order: Optional[int] = None
    birth_weight: Optional[float] = None
    blood_platelet: Optional[float] = None
    body_subsite: Optional[str] = None
    born_method: Optional[str] = None
    breastfeeding_duration: Optional[int] = None
    brinkman_index: Optional[float] = None
    c_peptide: Optional[float] = None
    c_section_type: Optional[str] = None
    calprotectin: Optional[float] = None
    cd163: Optional[float] = None
    change_in_tumor_size: Optional[str] = None
    cholesterol: Optional[float] = None
    creatine: Optional[float] = None
    creatinine: Optional[float] = None
    ctp: Optional[int] = None
    days_after_onset: Optional[int] = None
    days_from_first_collection: Optional[int] = None
    dental_sample_type: Optional[str] = None
    diet: Optional[str] = None
    disease: Optional[Union[str, List[str]]] = empty_list()
    disease_location: Optional[Union[str, List[str]]] = empty_list()
    disease_stage: Optional[str] = None
    disease_subtype: Optional[Union[str, List[str]]] = empty_list()
    dyastolic_p: Optional[float] = None
    eGFR: Optional[float] = None
    ever_smoker: Optional[str] = None
    family: Optional[str] = None
    family_role: Optional[str] = None
    fasting_glucose: Optional[float] = None
    fasting_insulin: Optional[float] = None
    feeding_practice: Optional[str] = None
    ferm_milk_prod_consumer: Optional[str] = None
    fgf_19: Optional[float] = None
    flg_genotype: Optional[str] = None
    fobt: Optional[str] = None
    formula_first_day: Optional[int] = None
    gestational_age: Optional[float] = None
    globulin: Optional[float] = None
    glp_1: Optional[float] = None
    glucose: Optional[float] = None
    glutamate_decarboxylase_2_antibody: Optional[float] = None
    hba1c: Optional[float] = None
    hdl: Optional[float] = None
    hemoglobinometry: Optional[float] = None
    history_of_periodontitis: Optional[str] = None
    hitchip_probe_class: Optional[str] = None
    hla_dqa11: Optional[int] = None
    hla_dqa12: Optional[int] = None
    hla_drb11: Optional[int] = None
    hla_drb12: Optional[int] = None
    hscrp: Optional[float] = None
    il_1: Optional[float] = None
    infant_age: Optional[int] = None
    inr: Optional[float] = None
    insulin_cat: Optional[str] = None
    lactating: Optional[str] = None
    ldl: Optional[float] = None
    leptin: Optional[float] = None
    lifestyle: Optional[str] = None
    location: Optional[str] = None
    menopausal_status: Optional[str] = None
    mgs_richness: Optional[float] = None
    mumps: Optional[str] = None
    non_westernized: Optional[str] = None
    performance_status: Optional[float] = None
    population: Optional[str] = None
    pregnant: Optional[str] = None
    premature: Optional[str] = None
    previous_therapy: Optional[str] = None
    protein_intake: Optional[float] = None
    prothrombin_time: Optional[float] = None
    rbc: Optional[float] = None
    remission: Optional[str] = None
    rheumatoid_factor: Optional[float] = None
    shigatoxin_2_elisa: Optional[str] = None
    smoker: Optional[str] = None
    stec_count: Optional[str] = None
    stool_texture: Optional[str] = None
    study_condition: Optional[str] = None
    study_name: Optional[str] = None
    subcohort: Optional[str] = None
    systolic_p: Optional[float] = None
    tnm: Optional[str] = None
    toxicity_above_zero: Optional[str] = None
    travel_destination: Optional[str] = None
    treatment: Optional[Union[str, List[str]]] = empty_list()
    triglycerides: Optional[float] = None
    uncurated_metadata: Optional[str] = None
    urea_nitrogen: Optional[float] = None
    visit_number: Optional[int] = None
    wbc: Optional[float] = None
    zigosity: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.age):
            self.MissingRequiredField("age")
        if not isinstance(self.age, str):
            self.age = str(self.age)

        if self._is_empty(self.body_site):
            self.MissingRequiredField("body_site")
        if not isinstance(self.body_site, str):
            self.body_site = str(self.body_site)

        if self._is_empty(self.country):
            self.MissingRequiredField("country")
        if not isinstance(self.country, str):
            self.country = str(self.country)

        if self._is_empty(self.curator):
            self.MissingRequiredField("curator")
        if not isinstance(self.curator, list):
            self.curator = [self.curator] if self.curator is not None else []
        self.curator = [v if isinstance(v, str) else str(v) for v in self.curator]

        if self._is_empty(self.gender):
            self.MissingRequiredField("gender")
        if not isinstance(self.gender, str):
            self.gender = str(self.gender)

        if self._is_empty(self.median_read_length):
            self.MissingRequiredField("median_read_length")
        if not isinstance(self.median_read_length, int):
            self.median_read_length = int(self.median_read_length)

        if self._is_empty(self.minimum_read_length):
            self.MissingRequiredField("minimum_read_length")
        if not isinstance(self.minimum_read_length, int):
            self.minimum_read_length = int(self.minimum_read_length)

        if self._is_empty(self.number_bases):
            self.MissingRequiredField("number_bases")
        if not isinstance(self.number_bases, int):
            self.number_bases = int(self.number_bases)

        if self._is_empty(self.number_reads):
            self.MissingRequiredField("number_reads")
        if not isinstance(self.number_reads, int):
            self.number_reads = int(self.number_reads)

        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, str):
            self.sample_id = str(self.sample_id)

        if self._is_empty(self.sequencing_platform):
            self.MissingRequiredField("sequencing_platform")
        if not isinstance(self.sequencing_platform, str):
            self.sequencing_platform = str(self.sequencing_platform)

        if self._is_empty(self.subject_id):
            self.MissingRequiredField("subject_id")
        if not isinstance(self.subject_id, str):
            self.subject_id = str(self.subject_id)

        if self.ALT is not None and not isinstance(self.ALT, float):
            self.ALT = float(self.ALT)

        if self.ASO is not None and not isinstance(self.ASO, float):
            self.ASO = float(self.ASO)

        if self.BASDAI is not None and not isinstance(self.BASDAI, float):
            self.BASDAI = float(self.BASDAI)

        if self.BASFI is not None and not isinstance(self.BASFI, float):
            self.BASFI = float(self.BASFI)

        if self.BMI is not None and not isinstance(self.BMI, float):
            self.BMI = float(self.BMI)

        if self.DNA_extraction_kit is not None and not isinstance(self.DNA_extraction_kit, str):
            self.DNA_extraction_kit = str(self.DNA_extraction_kit)

        if self.ESR is not None and not isinstance(self.ESR, float):
            self.ESR = float(self.ESR)

        if self.HBI is not None and not isinstance(self.HBI, float):
            self.HBI = float(self.HBI)

        if not isinstance(self.HLA, list):
            self.HLA = [self.HLA] if self.HLA is not None else []
        self.HLA = [v if isinstance(v, str) else str(v) for v in self.HLA]

        if not isinstance(self.NCBI_accession, list):
            self.NCBI_accession = [self.NCBI_accession] if self.NCBI_accession is not None else []
        self.NCBI_accession = [v if isinstance(v, str) else str(v) for v in self.NCBI_accession]

        if self.ORR is not None and not isinstance(self.ORR, str):
            self.ORR = str(self.ORR)

        if self.PFS12 is not None and not isinstance(self.PFS12, str):
            self.PFS12 = str(self.PFS12)

        if self.PMID is not None and not isinstance(self.PMID, str):
            self.PMID = str(self.PMID)

        if self.PPD_B is not None and not isinstance(self.PPD_B, float):
            self.PPD_B = float(self.PPD_B)

        if self.PPD_D is not None and not isinstance(self.PPD_D, float):
            self.PPD_D = float(self.PPD_D)

        if self.PPD_L is not None and not isinstance(self.PPD_L, float):
            self.PPD_L = float(self.PPD_L)

        if self.PPD_M is not None and not isinstance(self.PPD_M, float):
            self.PPD_M = float(self.PPD_M)

        if self.RECIST is not None and not isinstance(self.RECIST, str):
            self.RECIST = str(self.RECIST)

        if self.SCCAI is not None and not isinstance(self.SCCAI, float):
            self.SCCAI = float(self.SCCAI)

        if self.adiponectin is not None and not isinstance(self.adiponectin, float):
            self.adiponectin = float(self.adiponectin)

        if self.age_T1D_diagnosis is not None and not isinstance(self.age_T1D_diagnosis, float):
            self.age_T1D_diagnosis = float(self.age_T1D_diagnosis)

        if self.age_category is not None and not isinstance(self.age_category, str):
            self.age_category = str(self.age_category)

        if self.age_seroconversion is not None and not isinstance(self.age_seroconversion, float):
            self.age_seroconversion = float(self.age_seroconversion)

        if self.age_twins_started_to_live_apart is not None and not isinstance(self.age_twins_started_to_live_apart, int):
            self.age_twins_started_to_live_apart = int(self.age_twins_started_to_live_apart)

        if self.ajcc is not None and not isinstance(self.ajcc, str):
            self.ajcc = str(self.ajcc)

        if self.albumine is not None and not isinstance(self.albumine, float):
            self.albumine = float(self.albumine)

        if self.alcohol is not None and not isinstance(self.alcohol, str):
            self.alcohol = str(self.alcohol)

        if self.alcohol_numeric is not None and not isinstance(self.alcohol_numeric, float):
            self.alcohol_numeric = float(self.alcohol_numeric)

        if self.anti_PD_1 is not None and not isinstance(self.anti_PD_1, str):
            self.anti_PD_1 = str(self.anti_PD_1)

        if self.anti_ccp_antibody is not None and not isinstance(self.anti_ccp_antibody, float):
            self.anti_ccp_antibody = float(self.anti_ccp_antibody)

        if self.antibiotics_current_use is not None and not isinstance(self.antibiotics_current_use, str):
            self.antibiotics_current_use = str(self.antibiotics_current_use)

        if not isinstance(self.antibiotics_family, list):
            self.antibiotics_family = [self.antibiotics_family] if self.antibiotics_family is not None else []
        self.antibiotics_family = [v if isinstance(v, str) else str(v) for v in self.antibiotics_family]

        if self.ast is not None and not isinstance(self.ast, float):
            self.ast = float(self.ast)

        if not isinstance(self.autoantibody_positive, list):
            self.autoantibody_positive = [self.autoantibody_positive] if self.autoantibody_positive is not None else []
        self.autoantibody_positive = [v if isinstance(v, str) else str(v) for v in self.autoantibody_positive]

        if self.bilubirin is not None and not isinstance(self.bilubirin, float):
            self.bilubirin = float(self.bilubirin)

        if self.birth_control_pil is not None and not isinstance(self.birth_control_pil, str):
            self.birth_control_pil = str(self.birth_control_pil)

        if self.birth_order is not None and not isinstance(self.birth_order, int):
            self.birth_order = int(self.birth_order)

        if self.birth_weight is not None and not isinstance(self.birth_weight, float):
            self.birth_weight = float(self.birth_weight)

        if self.blood_platelet is not None and not isinstance(self.blood_platelet, float):
            self.blood_platelet = float(self.blood_platelet)

        if self.body_subsite is not None and not isinstance(self.body_subsite, str):
            self.body_subsite = str(self.body_subsite)

        if self.born_method is not None and not isinstance(self.born_method, str):
            self.born_method = str(self.born_method)

        if self.breastfeeding_duration is not None and not isinstance(self.breastfeeding_duration, int):
            self.breastfeeding_duration = int(self.breastfeeding_duration)

        if self.brinkman_index is not None and not isinstance(self.brinkman_index, float):
            self.brinkman_index = float(self.brinkman_index)

        if self.c_peptide is not None and not isinstance(self.c_peptide, float):
            self.c_peptide = float(self.c_peptide)

        if self.c_section_type is not None and not isinstance(self.c_section_type, str):
            self.c_section_type = str(self.c_section_type)

        if self.calprotectin is not None and not isinstance(self.calprotectin, float):
            self.calprotectin = float(self.calprotectin)

        if self.cd163 is not None and not isinstance(self.cd163, float):
            self.cd163 = float(self.cd163)

        if self.change_in_tumor_size is not None and not isinstance(self.change_in_tumor_size, str):
            self.change_in_tumor_size = str(self.change_in_tumor_size)

        if self.cholesterol is not None and not isinstance(self.cholesterol, float):
            self.cholesterol = float(self.cholesterol)

        if self.creatine is not None and not isinstance(self.creatine, float):
            self.creatine = float(self.creatine)

        if self.creatinine is not None and not isinstance(self.creatinine, float):
            self.creatinine = float(self.creatinine)

        if self.ctp is not None and not isinstance(self.ctp, int):
            self.ctp = int(self.ctp)

        if self.days_after_onset is not None and not isinstance(self.days_after_onset, int):
            self.days_after_onset = int(self.days_after_onset)

        if self.days_from_first_collection is not None and not isinstance(self.days_from_first_collection, int):
            self.days_from_first_collection = int(self.days_from_first_collection)

        if self.dental_sample_type is not None and not isinstance(self.dental_sample_type, str):
            self.dental_sample_type = str(self.dental_sample_type)

        if self.diet is not None and not isinstance(self.diet, str):
            self.diet = str(self.diet)

        if not isinstance(self.disease, list):
            self.disease = [self.disease] if self.disease is not None else []
        self.disease = [v if isinstance(v, str) else str(v) for v in self.disease]

        if not isinstance(self.disease_location, list):
            self.disease_location = [self.disease_location] if self.disease_location is not None else []
        self.disease_location = [v if isinstance(v, str) else str(v) for v in self.disease_location]

        if self.disease_stage is not None and not isinstance(self.disease_stage, str):
            self.disease_stage = str(self.disease_stage)

        if not isinstance(self.disease_subtype, list):
            self.disease_subtype = [self.disease_subtype] if self.disease_subtype is not None else []
        self.disease_subtype = [v if isinstance(v, str) else str(v) for v in self.disease_subtype]

        if self.dyastolic_p is not None and not isinstance(self.dyastolic_p, float):
            self.dyastolic_p = float(self.dyastolic_p)

        if self.eGFR is not None and not isinstance(self.eGFR, float):
            self.eGFR = float(self.eGFR)

        if self.ever_smoker is not None and not isinstance(self.ever_smoker, str):
            self.ever_smoker = str(self.ever_smoker)

        if self.family is not None and not isinstance(self.family, str):
            self.family = str(self.family)

        if self.family_role is not None and not isinstance(self.family_role, str):
            self.family_role = str(self.family_role)

        if self.fasting_glucose is not None and not isinstance(self.fasting_glucose, float):
            self.fasting_glucose = float(self.fasting_glucose)

        if self.fasting_insulin is not None and not isinstance(self.fasting_insulin, float):
            self.fasting_insulin = float(self.fasting_insulin)

        if self.feeding_practice is not None and not isinstance(self.feeding_practice, str):
            self.feeding_practice = str(self.feeding_practice)

        if self.ferm_milk_prod_consumer is not None and not isinstance(self.ferm_milk_prod_consumer, str):
            self.ferm_milk_prod_consumer = str(self.ferm_milk_prod_consumer)

        if self.fgf_19 is not None and not isinstance(self.fgf_19, float):
            self.fgf_19 = float(self.fgf_19)

        if self.flg_genotype is not None and not isinstance(self.flg_genotype, str):
            self.flg_genotype = str(self.flg_genotype)

        if self.fobt is not None and not isinstance(self.fobt, str):
            self.fobt = str(self.fobt)

        if self.formula_first_day is not None and not isinstance(self.formula_first_day, int):
            self.formula_first_day = int(self.formula_first_day)

        if self.gestational_age is not None and not isinstance(self.gestational_age, float):
            self.gestational_age = float(self.gestational_age)

        if self.globulin is not None and not isinstance(self.globulin, float):
            self.globulin = float(self.globulin)

        if self.glp_1 is not None and not isinstance(self.glp_1, float):
            self.glp_1 = float(self.glp_1)

        if self.glucose is not None and not isinstance(self.glucose, float):
            self.glucose = float(self.glucose)

        if self.glutamate_decarboxylase_2_antibody is not None and not isinstance(self.glutamate_decarboxylase_2_antibody, float):
            self.glutamate_decarboxylase_2_antibody = float(self.glutamate_decarboxylase_2_antibody)

        if self.hba1c is not None and not isinstance(self.hba1c, float):
            self.hba1c = float(self.hba1c)

        if self.hdl is not None and not isinstance(self.hdl, float):
            self.hdl = float(self.hdl)

        if self.hemoglobinometry is not None and not isinstance(self.hemoglobinometry, float):
            self.hemoglobinometry = float(self.hemoglobinometry)

        if self.history_of_periodontitis is not None and not isinstance(self.history_of_periodontitis, str):
            self.history_of_periodontitis = str(self.history_of_periodontitis)

        if self.hitchip_probe_class is not None and not isinstance(self.hitchip_probe_class, str):
            self.hitchip_probe_class = str(self.hitchip_probe_class)

        if self.hla_dqa11 is not None and not isinstance(self.hla_dqa11, int):
            self.hla_dqa11 = int(self.hla_dqa11)

        if self.hla_dqa12 is not None and not isinstance(self.hla_dqa12, int):
            self.hla_dqa12 = int(self.hla_dqa12)

        if self.hla_drb11 is not None and not isinstance(self.hla_drb11, int):
            self.hla_drb11 = int(self.hla_drb11)

        if self.hla_drb12 is not None and not isinstance(self.hla_drb12, int):
            self.hla_drb12 = int(self.hla_drb12)

        if self.hscrp is not None and not isinstance(self.hscrp, float):
            self.hscrp = float(self.hscrp)

        if self.il_1 is not None and not isinstance(self.il_1, float):
            self.il_1 = float(self.il_1)

        if self.infant_age is not None and not isinstance(self.infant_age, int):
            self.infant_age = int(self.infant_age)

        if self.inr is not None and not isinstance(self.inr, float):
            self.inr = float(self.inr)

        if self.insulin_cat is not None and not isinstance(self.insulin_cat, str):
            self.insulin_cat = str(self.insulin_cat)

        if self.lactating is not None and not isinstance(self.lactating, str):
            self.lactating = str(self.lactating)

        if self.ldl is not None and not isinstance(self.ldl, float):
            self.ldl = float(self.ldl)

        if self.leptin is not None and not isinstance(self.leptin, float):
            self.leptin = float(self.leptin)

        if self.lifestyle is not None and not isinstance(self.lifestyle, str):
            self.lifestyle = str(self.lifestyle)

        if self.location is not None and not isinstance(self.location, str):
            self.location = str(self.location)

        if self.menopausal_status is not None and not isinstance(self.menopausal_status, str):
            self.menopausal_status = str(self.menopausal_status)

        if self.mgs_richness is not None and not isinstance(self.mgs_richness, float):
            self.mgs_richness = float(self.mgs_richness)

        if self.mumps is not None and not isinstance(self.mumps, str):
            self.mumps = str(self.mumps)

        if self.non_westernized is not None and not isinstance(self.non_westernized, str):
            self.non_westernized = str(self.non_westernized)

        if self.performance_status is not None and not isinstance(self.performance_status, float):
            self.performance_status = float(self.performance_status)

        if self.population is not None and not isinstance(self.population, str):
            self.population = str(self.population)

        if self.pregnant is not None and not isinstance(self.pregnant, str):
            self.pregnant = str(self.pregnant)

        if self.premature is not None and not isinstance(self.premature, str):
            self.premature = str(self.premature)

        if self.previous_therapy is not None and not isinstance(self.previous_therapy, str):
            self.previous_therapy = str(self.previous_therapy)

        if self.protein_intake is not None and not isinstance(self.protein_intake, float):
            self.protein_intake = float(self.protein_intake)

        if self.prothrombin_time is not None and not isinstance(self.prothrombin_time, float):
            self.prothrombin_time = float(self.prothrombin_time)

        if self.rbc is not None and not isinstance(self.rbc, float):
            self.rbc = float(self.rbc)

        if self.remission is not None and not isinstance(self.remission, str):
            self.remission = str(self.remission)

        if self.rheumatoid_factor is not None and not isinstance(self.rheumatoid_factor, float):
            self.rheumatoid_factor = float(self.rheumatoid_factor)

        if self.shigatoxin_2_elisa is not None and not isinstance(self.shigatoxin_2_elisa, str):
            self.shigatoxin_2_elisa = str(self.shigatoxin_2_elisa)

        if self.smoker is not None and not isinstance(self.smoker, str):
            self.smoker = str(self.smoker)

        if self.stec_count is not None and not isinstance(self.stec_count, str):
            self.stec_count = str(self.stec_count)

        if self.stool_texture is not None and not isinstance(self.stool_texture, str):
            self.stool_texture = str(self.stool_texture)

        if self.study_condition is not None and not isinstance(self.study_condition, str):
            self.study_condition = str(self.study_condition)

        if self.study_name is not None and not isinstance(self.study_name, str):
            self.study_name = str(self.study_name)

        if self.subcohort is not None and not isinstance(self.subcohort, str):
            self.subcohort = str(self.subcohort)

        if self.systolic_p is not None and not isinstance(self.systolic_p, float):
            self.systolic_p = float(self.systolic_p)

        if self.tnm is not None and not isinstance(self.tnm, str):
            self.tnm = str(self.tnm)

        if self.toxicity_above_zero is not None and not isinstance(self.toxicity_above_zero, str):
            self.toxicity_above_zero = str(self.toxicity_above_zero)

        if self.travel_destination is not None and not isinstance(self.travel_destination, str):
            self.travel_destination = str(self.travel_destination)

        if not isinstance(self.treatment, list):
            self.treatment = [self.treatment] if self.treatment is not None else []
        self.treatment = [v if isinstance(v, str) else str(v) for v in self.treatment]

        if self.triglycerides is not None and not isinstance(self.triglycerides, float):
            self.triglycerides = float(self.triglycerides)

        if self.uncurated_metadata is not None and not isinstance(self.uncurated_metadata, str):
            self.uncurated_metadata = str(self.uncurated_metadata)

        if self.urea_nitrogen is not None and not isinstance(self.urea_nitrogen, float):
            self.urea_nitrogen = float(self.urea_nitrogen)

        if self.visit_number is not None and not isinstance(self.visit_number, int):
            self.visit_number = int(self.visit_number)

        if self.wbc is not None and not isinstance(self.wbc, float):
            self.wbc = float(self.wbc)

        if self.zigosity is not None and not isinstance(self.zigosity, str):
            self.zigosity = str(self.zigosity)

        super().__post_init__(**kwargs)


@dataclass
class Study(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CMD.Study
    class_class_curie: ClassVar[str] = "CMD:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = CMD.Study

    samples: Optional[Union[Union[dict, Sample], List[Union[dict, Sample]]]] = empty_list()
    study_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.samples, list):
            self.samples = [self.samples] if self.samples is not None else []
        self.samples = [v if isinstance(v, Sample) else Sample(**as_dict(v)) for v in self.samples]

        if self.study_name is not None and not isinstance(self.study_name, str):
            self.study_name = str(self.study_name)

        super().__post_init__(**kwargs)


@dataclass
class Project(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CMD.Project
    class_class_curie: ClassVar[str] = "CMD:Project"
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = CMD.Project

    project_name: Optional[str] = None
    studies: Optional[Union[Union[dict, Study], List[Union[dict, Study]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.project_name is not None and not isinstance(self.project_name, str):
            self.project_name = str(self.project_name)

        if not isinstance(self.studies, list):
            self.studies = [self.studies] if self.studies is not None else []
        self.studies = [v if isinstance(v, Study) else Study(**as_dict(v)) for v in self.studies]

        super().__post_init__(**kwargs)


# Enumerations
class StatusEnum(EnumDefinitionImpl):

    NA = PermissibleValue(text="NA")

    _defn = EnumDefinition(
        name="StatusEnum",
    )

class DNAExtractionKitEnum(EnumDefinitionImpl):

    Chemagen = PermissibleValue(text="Chemagen",
                                       description="Chemagen")
    Gnome = PermissibleValue(text="Gnome",
                                 description="Gnome")
    Illuminakit = PermissibleValue(text="Illuminakit",
                                             description="Illuminakit")
    KAMA_Hyper_Prep = PermissibleValue(text="KAMA_Hyper_Prep",
                                                     description="KAMA_Hyper_Prep")
    MPBio = PermissibleValue(text="MPBio",
                                 description="MPBio")
    Maxwell_LEV = PermissibleValue(text="Maxwell_LEV",
                                             description="Maxwell_LEV")
    MoBio = PermissibleValue(text="MoBio",
                                 description="MoBio")
    NorgenBiotek = PermissibleValue(text="NorgenBiotek",
                                               description="NorgenBiotek")
    PSP_Spin_Stool = PermissibleValue(text="PSP_Spin_Stool",
                                                   description="PSP_Spin_Stool")
    PowerSoil = PermissibleValue(text="PowerSoil",
                                         description="PowerSoil")
    PowerSoilPro = PermissibleValue(text="PowerSoilPro",
                                               description="PowerSoilPro")
    Qiagen = PermissibleValue(text="Qiagen",
                                   description="Qiagen")
    Tiangen = PermissibleValue(text="Tiangen",
                                     description="Tiangen")
    ZR_Fecal_DNA_MiniPrep = PermissibleValue(text="ZR_Fecal_DNA_MiniPrep",
                                                                 description="ZR_Fecal_DNA_MiniPrep")
    other = PermissibleValue(text="other",
                                 description="other")
    thermo_fisher = PermissibleValue(text="thermo_fisher",
                                                 description="thermo_fisher")

    _defn = EnumDefinition(
        name="DNAExtractionKitEnum",
    )

class RECISTEnum(EnumDefinitionImpl):

    CR = PermissibleValue(text="CR",
                           description="CR")
    PD = PermissibleValue(text="PD",
                           description="PD")
    PR = PermissibleValue(text="PR",
                           description="PR")
    SD = PermissibleValue(text="SD",
                           description="SD")

    _defn = EnumDefinition(
        name="RECISTEnum",
    )

class CatAge(EnumDefinitionImpl):

    adult = PermissibleValue(text="adult")
    child = PermissibleValue(text="child")
    newborn = PermissibleValue(text="newborn")
    schoolage = PermissibleValue(text="schoolage")
    senior = PermissibleValue(text="senior")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="CatAge",
    )

class AntiPD1Enum(EnumDefinitionImpl):

    non_responder = PermissibleValue(text="non_responder",
                                                 description="non_responder")
    responder = PermissibleValue(text="responder",
                                         description="responder")

    _defn = EnumDefinition(
        name="AntiPD1Enum",
    )

class BornMethodEnum(EnumDefinitionImpl):

    c_section = PermissibleValue(text="c_section",
                                         description="c_section")
    vaginal = PermissibleValue(text="vaginal",
                                     description="vaginal")

    _defn = EnumDefinition(
        name="BornMethodEnum",
    )

class CSectionTypeEnum(EnumDefinitionImpl):

    Elective_CS = PermissibleValue(text="Elective_CS",
                                             description="Elective_CS")
    Emergency_CS = PermissibleValue(text="Emergency_CS",
                                               description="Emergency_CS")

    _defn = EnumDefinition(
        name="CSectionTypeEnum",
    )

class CountryEnum(EnumDefinitionImpl):

    AUT = PermissibleValue(text="AUT",
                             description="AUT")
    BGD = PermissibleValue(text="BGD",
                             description="BGD")
    BRA = PermissibleValue(text="BRA",
                             description="BRA")
    BRN = PermissibleValue(text="BRN",
                             description="BRN")
    CAN = PermissibleValue(text="CAN",
                             description="CAN")
    CHN = PermissibleValue(text="CHN",
                             description="CHN")
    CMR = PermissibleValue(text="CMR",
                             description="CMR")
    DEU = PermissibleValue(text="DEU",
                             description="DEU")
    DNK = PermissibleValue(text="DNK",
                             description="DNK")
    ESP = PermissibleValue(text="ESP",
                             description="ESP")
    EST = PermissibleValue(text="EST",
                             description="EST")
    ETH = PermissibleValue(text="ETH",
                             description="ETH")
    FIN = PermissibleValue(text="FIN",
                             description="FIN")
    FJI = PermissibleValue(text="FJI",
                             description="FJI")
    FRA = PermissibleValue(text="FRA",
                             description="FRA")
    GBR = PermissibleValue(text="GBR",
                             description="GBR")
    GHA = PermissibleValue(text="GHA",
                             description="GHA")
    HUN = PermissibleValue(text="HUN",
                             description="HUN")
    IDN = PermissibleValue(text="IDN",
                             description="IDN")
    IND = PermissibleValue(text="IND",
                             description="IND")
    IRL = PermissibleValue(text="IRL",
                             description="IRL")
    ISL = PermissibleValue(text="ISL",
                             description="ISL")
    ISR = PermissibleValue(text="ISR",
                             description="ISR")
    ITA = PermissibleValue(text="ITA",
                             description="ITA")
    JPN = PermissibleValue(text="JPN",
                             description="JPN")
    KAZ = PermissibleValue(text="KAZ",
                             description="KAZ")
    KOR = PermissibleValue(text="KOR",
                             description="KOR")
    LBR = PermissibleValue(text="LBR",
                             description="LBR")
    LUX = PermissibleValue(text="LUX",
                             description="LUX")
    MDG = PermissibleValue(text="MDG",
                             description="MDG")
    MNG = PermissibleValue(text="MNG",
                             description="MNG")
    MYS = PermissibleValue(text="MYS",
                             description="MYS")
    NLD = PermissibleValue(text="NLD",
                             description="NLD")
    NOR = PermissibleValue(text="NOR",
                             description="NOR")
    PER = PermissibleValue(text="PER",
                             description="PER")
    PHL = PermissibleValue(text="PHL",
                             description="PHL")
    RUS = PermissibleValue(text="RUS",
                             description="RUS")
    SGP = PermissibleValue(text="SGP",
                             description="SGP")
    SLV = PermissibleValue(text="SLV",
                             description="SLV")
    SVK = PermissibleValue(text="SVK",
                             description="SVK")
    SWE = PermissibleValue(text="SWE",
                             description="SWE")
    TZA = PermissibleValue(text="TZA",
                             description="TZA")
    USA = PermissibleValue(text="USA",
                             description="USA")

    _defn = EnumDefinition(
        name="CountryEnum",
    )

class DentalSampleTypeEnum(EnumDefinitionImpl):

    implant = PermissibleValue(text="implant",
                                     description="implant")
    teeth = PermissibleValue(text="teeth",
                                 description="teeth")

    _defn = EnumDefinition(
        name="DentalSampleTypeEnum",
    )

class DietEnum(EnumDefinitionImpl):

    omnivore = PermissibleValue(text="omnivore",
                                       description="omnivore")
    vegan = PermissibleValue(text="vegan",
                                 description="vegan")
    vegetarian = PermissibleValue(text="vegetarian",
                                           description="vegetarian")

    _defn = EnumDefinition(
        name="DietEnum",
    )

class FamilyRoleEnum(EnumDefinitionImpl):

    child = PermissibleValue(text="child",
                                 description="child")
    father = PermissibleValue(text="father",
                                   description="father")
    mother = PermissibleValue(text="mother",
                                   description="mother")

    _defn = EnumDefinition(
        name="FamilyRoleEnum",
    )

class FeedingPracticeEnum(EnumDefinitionImpl):

    any_breastfeeding = PermissibleValue(text="any_breastfeeding",
                                                         description="any_breastfeeding")
    exclusively_breastfeeding = PermissibleValue(text="exclusively_breastfeeding",
                                                                         description="exclusively_breastfeeding")
    exclusively_formula_feeding = PermissibleValue(text="exclusively_formula_feeding",
                                                                             description="exclusively_formula_feeding")
    mixed_feeding = PermissibleValue(text="mixed_feeding",
                                                 description="mixed_feeding")
    no_breastfeeding = PermissibleValue(text="no_breastfeeding",
                                                       description="no_breastfeeding")

    _defn = EnumDefinition(
        name="FeedingPracticeEnum",
    )

class FermMilkProdConsumerEnum(EnumDefinitionImpl):

    dfmp = PermissibleValue(text="dfmp",
                               description="dfmp")

    _defn = EnumDefinition(
        name="FermMilkProdConsumerEnum",
    )

class FlgGenotypeEnum(EnumDefinitionImpl):

    e2422x = PermissibleValue(text="e2422x",
                                   description="e2422x")
    s1515x = PermissibleValue(text="s1515x",
                                   description="s1515x")
    wt = PermissibleValue(text="wt",
                           description="wt")

    _defn = EnumDefinition(
        name="FlgGenotypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "e2422x/3321dela",
                PermissibleValue(text="e2422x/3321dela",
                                 description="e2422x/3321dela") )

class HitchipProbeClassEnum(EnumDefinitionImpl):

    hpc = PermissibleValue(text="hpc",
                             description="hpc")
    lpc = PermissibleValue(text="lpc",
                             description="lpc")

    _defn = EnumDefinition(
        name="HitchipProbeClassEnum",
    )

class LifestyleEnum(EnumDefinitionImpl):

    Agriculturalist = PermissibleValue(text="Agriculturalist",
                                                     description="Agriculturalist")
    Agropastoralist = PermissibleValue(text="Agropastoralist",
                                                     description="Agropastoralist")
    Fisher = PermissibleValue(text="Fisher",
                                   description="Fisher")
    Pastoralist = PermissibleValue(text="Pastoralist",
                                             description="Pastoralist")

    _defn = EnumDefinition(
        name="LifestyleEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Hunter-gatherer",
                PermissibleValue(text="Hunter-gatherer",
                                 description="Hunter-gatherer") )

class MenopausalStatusEnum(EnumDefinitionImpl):

    going_through = PermissibleValue(text="going_through",
                                                 description="going_through")
    post = PermissibleValue(text="post",
                               description="post")
    pre = PermissibleValue(text="pre",
                             description="pre")

    _defn = EnumDefinition(
        name="MenopausalStatusEnum",
    )

class SequencingPlatformEnum(EnumDefinitionImpl):

    IlluminaHiSeq = PermissibleValue(text="IlluminaHiSeq",
                                                 description="IlluminaHiSeq")
    IlluminaMiSeq = PermissibleValue(text="IlluminaMiSeq",
                                                 description="IlluminaMiSeq")
    IlluminaNextSeq = PermissibleValue(text="IlluminaNextSeq",
                                                     description="IlluminaNextSeq")
    IlluminaNovaSeq = PermissibleValue(text="IlluminaNovaSeq",
                                                     description="IlluminaNovaSeq")

    _defn = EnumDefinition(
        name="SequencingPlatformEnum",
    )

class Shigatoxin2ElisaEnum(EnumDefinitionImpl):

    negative = PermissibleValue(text="negative",
                                       description="negative")
    positive = PermissibleValue(text="positive",
                                       description="positive")

    _defn = EnumDefinition(
        name="Shigatoxin2ElisaEnum",
    )

class StecCountEnum(EnumDefinitionImpl):

    high = PermissibleValue(text="high",
                               description="high")
    low = PermissibleValue(text="low",
                             description="low")
    moderate = PermissibleValue(text="moderate",
                                       description="moderate")

    _defn = EnumDefinition(
        name="StecCountEnum",
    )

class StoolTextureEnum(EnumDefinitionImpl):

    bloody = PermissibleValue(text="bloody",
                                   description="bloody")
    smooth = PermissibleValue(text="smooth",
                                   description="smooth")
    watery = PermissibleValue(text="watery",
                                   description="watery")

    _defn = EnumDefinition(
        name="StoolTextureEnum",
    )

class TnmEnum(EnumDefinitionImpl):

    ptis = PermissibleValue(text="ptis",
                               description="ptis")
    t1n0m0 = PermissibleValue(text="t1n0m0",
                                   description="t1n0m0")
    t1n0m1 = PermissibleValue(text="t1n0m1",
                                   description="t1n0m1")
    t2m0n0 = PermissibleValue(text="t2m0n0",
                                   description="t2m0n0")
    t2n0m0 = PermissibleValue(text="t2n0m0",
                                   description="t2n0m0")
    t2n0m1 = PermissibleValue(text="t2n0m1",
                                   description="t2n0m1")
    t2n1m0 = PermissibleValue(text="t2n1m0",
                                   description="t2n1m0")
    t2n1m1 = PermissibleValue(text="t2n1m1",
                                   description="t2n1m1")
    t2n2m0 = PermissibleValue(text="t2n2m0",
                                   description="t2n2m0")
    t3n0m0 = PermissibleValue(text="t3n0m0",
                                   description="t3n0m0")
    t3n0m1 = PermissibleValue(text="t3n0m1",
                                   description="t3n0m1")
    t3n1m0 = PermissibleValue(text="t3n1m0",
                                   description="t3n1m0")
    t3n1m1 = PermissibleValue(text="t3n1m1",
                                   description="t3n1m1")
    t3n2m0 = PermissibleValue(text="t3n2m0",
                                   description="t3n2m0")
    t3n2m1 = PermissibleValue(text="t3n2m1",
                                   description="t3n2m1")
    t3n3m1 = PermissibleValue(text="t3n3m1",
                                   description="t3n3m1")
    t3nxm1 = PermissibleValue(text="t3nxm1",
                                   description="t3nxm1")
    t4n0m0 = PermissibleValue(text="t4n0m0",
                                   description="t4n0m0")
    t4n0m1 = PermissibleValue(text="t4n0m1",
                                   description="t4n0m1")
    t4n1m0 = PermissibleValue(text="t4n1m0",
                                   description="t4n1m0")
    t4n1m1 = PermissibleValue(text="t4n1m1",
                                   description="t4n1m1")
    t4n2m0 = PermissibleValue(text="t4n2m0",
                                   description="t4n2m0")
    t4n2m1 = PermissibleValue(text="t4n2m1",
                                   description="t4n2m1")
    tisn0m0 = PermissibleValue(text="tisn0m0",
                                     description="tisn0m0")

    _defn = EnumDefinition(
        name="TnmEnum",
    )

class TravelDestinationEnum(EnumDefinitionImpl):

    CMR = PermissibleValue(text="CMR",
                             description="CMR")
    ETH = PermissibleValue(text="ETH",
                             description="ETH")
    IND = PermissibleValue(text="IND",
                             description="IND")
    KEN = PermissibleValue(text="KEN",
                             description="KEN")
    LKA = PermissibleValue(text="LKA",
                             description="LKA")
    NPL = PermissibleValue(text="NPL",
                             description="NPL")
    RWA = PermissibleValue(text="RWA",
                             description="RWA")
    TZA = PermissibleValue(text="TZA",
                             description="TZA")

    _defn = EnumDefinition(
        name="TravelDestinationEnum",
    )

class ZigosityEnum(EnumDefinitionImpl):

    dizygotic = PermissibleValue(text="dizygotic",
                                         description="dizygotic")
    monozygotic = PermissibleValue(text="monozygotic",
                                             description="monozygotic")

    _defn = EnumDefinition(
        name="ZigosityEnum",
    )

class Gender(EnumDefinitionImpl):

    female = PermissibleValue(text="female")
    male = PermissibleValue(text="male")
    other = PermissibleValue(text="other")
    NA = PermissibleValue(text="NA")

    _defn = EnumDefinition(
        name="Gender",
    )

class YesNo(EnumDefinitionImpl):

    no = PermissibleValue(text="no")
    yes = PermissibleValue(text="yes")

    _defn = EnumDefinition(
        name="YesNo",
    )

class BodySite(EnumDefinitionImpl):

    lung = PermissibleValue(text="lung",
                               description="lung",
                               meaning=UBERON["0002048"])
    milk = PermissibleValue(text="milk",
                               description="milk",
                               meaning=UBERON["0001913"])
    nasalcavity = PermissibleValue(text="nasalcavity",
                                             description="nasal cavity",
                                             meaning=UBERON["0001707"])
    oralcavity = PermissibleValue(text="oralcavity",
                                           description="oral cavity",
                                           meaning=UBERON["0000167"])
    skin = PermissibleValue(text="skin",
                               description="skin of body",
                               meaning=UBERON["0002097"])
    stool = PermissibleValue(text="stool",
                                 description="feces",
                                 meaning=UBERON["0001988"])
    vagina = PermissibleValue(text="vagina",
                                   description="vagina",
                                   meaning=UBERON["0000996"])

    _defn = EnumDefinition(
        name="BodySite",
    )

class BodySubsite(EnumDefinitionImpl):

    anterior_nares = PermissibleValue(text="anterior_nares",
                                                   description="anterior naris",
                                                   meaning=UBERON["2001427"])
    buccal_mucosa = PermissibleValue(text="buccal_mucosa",
                                                 description="buccal mucosa",
                                                 meaning=UBERON["0006956"])
    chest = PermissibleValue(text="chest",
                                 description="chest",
                                 meaning=UBERON["0001443"])
    hard_palate = PermissibleValue(text="hard_palate",
                                             description="hard palate",
                                             meaning=UBERON["0003216"])
    keratinized_gingiva = PermissibleValue(text="keratinized_gingiva",
                                                             description="gingival epithelium",
                                                             meaning=UBERON["0001949"])
    l_retroauricular_crease = PermissibleValue(text="l_retroauricular_crease",
                                                                     description="skin crease",
                                                                     meaning=UBERON["0019243"])
    left_ear = PermissibleValue(text="left_ear",
                                       description="left ear",
                                       meaning=UBERON["0035295"])
    left_elbow = PermissibleValue(text="left_elbow",
                                           description="elbow",
                                           meaning=UBERON["0001461"])
    mid_vagina = PermissibleValue(text="mid_vagina",
                                           description="median vaginal canal",
                                           meaning=UBERON["0013524"])
    palatine_tonsils = PermissibleValue(text="palatine_tonsils",
                                                       description="palatine tonsil",
                                                       meaning=UBERON["0002373"])
    posterior_fornix = PermissibleValue(text="posterior_fornix",
                                                       description="posterior fornix of vagina",
                                                       meaning=UBERON["0016486"])
    r_retroauricular_crease = PermissibleValue(text="r_retroauricular_crease",
                                                                     description="skin crease",
                                                                     meaning=UBERON["0019243"])
    rectal_swab = PermissibleValue(text="rectal_swab",
                                             description="rectal swab specimen",
                                             meaning=NCIT.C173641)
    right_ear = PermissibleValue(text="right_ear",
                                         description="right ear",
                                         meaning=UBERON["0035174"])
    right_elbow = PermissibleValue(text="right_elbow",
                                             description="elbow",
                                             meaning=UBERON["0001461"])
    saliva = PermissibleValue(text="saliva",
                                   description="saliva",
                                   meaning=UBERON["0001836"])
    sputum = PermissibleValue(text="sputum",
                                   description="sputum",
                                   meaning=UBERON["0007311"])
    subgingival_plaque = PermissibleValue(text="subgingival_plaque",
                                                           description="subgingival dental plaque",
                                                           meaning=UBERON["0016484"])
    supragingival_plaque = PermissibleValue(text="supragingival_plaque",
                                                               description="supragingival dental plaque",
                                                               meaning=UBERON["0016485"])
    throat = PermissibleValue(text="throat",
                                   description="throat",
                                   meaning=UBERON["0000341"])
    tongue_dorsum = PermissibleValue(text="tongue_dorsum",
                                                 description="dorsum of tongue",
                                                 meaning=UBERON["0009471"])
    vaginal_introitus = PermissibleValue(text="vaginal_introitus",
                                                         description="vaginal oriface",
                                                         meaning=UBERON["0012317"])
    stool = PermissibleValue(text="stool",
                                 description="feces",
                                 meaning=UBERON["0001988"])

    _defn = EnumDefinition(
        name="BodySubsite",
    )

class TreatmentEnum(EnumDefinitionImpl):

    albendazole = PermissibleValue(text="albendazole")
    anthelmintics = PermissibleValue(text="anthelmintics")
    aza = PermissibleValue(text="aza")
    CTLA4 = PermissibleValue(text="CTLA4")
    EEN = PermissibleValue(text="EEN")
    folate = PermissibleValue(text="folate")
    forceval = PermissibleValue(text="forceval")
    ipilumumab = PermissibleValue(text="ipilumumab")
    iron = PermissibleValue(text="iron")
    Lactulose = PermissibleValue(text="Lactulose")
    lantus = PermissibleValue(text="lantus")
    metformin = PermissibleValue(text="metformin")
    methotrexate = PermissibleValue(text="methotrexate")
    modulen_suppl = PermissibleValue(text="modulen_suppl")
    nivolmab = PermissibleValue(text="nivolmab")
    no = PermissibleValue(text="no")
    novorapid = PermissibleValue(text="novorapid")
    NSAID = PermissibleValue(text="NSAID")
    PD1 = PermissibleValue(text="PD1")
    pembrolizumab = PermissibleValue(text="pembrolizumab")
    PPI = PermissibleValue(text="PPI")
    probiotic = PermissibleValue(text="probiotic")
    sitagliptin = PermissibleValue(text="sitagliptin")
    solostar = PermissibleValue(text="solostar")
    steroids = PermissibleValue(text="steroids")
    sulphonylurea = PermissibleValue(text="sulphonylurea")

    _defn = EnumDefinition(
        name="TreatmentEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "5-ASA",
                PermissibleValue(text="5-ASA") )

class AntibioticsFamilyEnum(EnumDefinitionImpl):

    aminoglycosides = PermissibleValue(text="aminoglycosides")
    anti_retrovirals = PermissibleValue(text="anti_retrovirals")
    anti_virals = PermissibleValue(text="anti_virals")
    beta_blockers = PermissibleValue(text="beta_blockers")
    beta_lactamase_inhibitors = PermissibleValue(text="beta_lactamase_inhibitors")
    blood_pressure_medication = PermissibleValue(text="blood_pressure_medication")
    carbapenems = PermissibleValue(text="carbapenems")
    cephalosporins = PermissibleValue(text="cephalosporins")
    diabetes_oral_medication = PermissibleValue(text="diabetes_oral_medication")
    dopamine_antagonists = PermissibleValue(text="dopamine_antagonists")
    fluoroquinolones = PermissibleValue(text="fluoroquinolones")
    laxatives = PermissibleValue(text="laxatives")
    macrolides = PermissibleValue(text="macrolides")
    nitrofurans = PermissibleValue(text="nitrofurans")
    none = PermissibleValue(text="none")
    penicillins = PermissibleValue(text="penicillins")
    phenylpiperidines = PermissibleValue(text="phenylpiperidines")
    reverse_transcriptase_inhibitors = PermissibleValue(text="reverse_transcriptase_inhibitors")
    sulphonamides = PermissibleValue(text="sulphonamides")
    thienobenzodiazepines = PermissibleValue(text="thienobenzodiazepines")

    _defn = EnumDefinition(
        name="AntibioticsFamilyEnum",
    )

class DiseaseSubtypeEnum(EnumDefinitionImpl):

    adenocarcinoma = PermissibleValue(text="adenocarcinoma")
    adenoma = PermissibleValue(text="adenoma")
    advancedadenoma = PermissibleValue(text="advancedadenoma")
    AS = PermissibleValue(text="AS")
    ascaris_lumbricoides = PermissibleValue(text="ascaris_lumbricoides")
    carcinoma = PermissibleValue(text="carcinoma")
    CD = PermissibleValue(text="CD")
    cholera = PermissibleValue(text="cholera")
    cirrhosis = PermissibleValue(text="cirrhosis")
    entamoeba_histolytica = PermissibleValue(text="entamoeba_histolytica")
    first_episode_schizofrenia = PermissibleValue(text="first_episode_schizofrenia")
    HBV = PermissibleValue(text="HBV")
    HDV = PermissibleValue(text="HDV")
    healthy = PermissibleValue(text="healthy")
    HEV = PermissibleValue(text="HEV")
    hookworm = PermissibleValue(text="hookworm")
    largeadenoma = PermissibleValue(text="largeadenoma")
    mansonella_perstans = PermissibleValue(text="mansonella_perstans")
    microfilaria_loa_loa = PermissibleValue(text="microfilaria_loa_loa")
    microfilaria_spp = PermissibleValue(text="microfilaria_spp")
    NAFLD = PermissibleValue(text="NAFLD")
    necator_americanus = PermissibleValue(text="necator_americanus")
    plasmodium_falciparum = PermissibleValue(text="plasmodium_falciparum")
    repeated_episodes_shizofrenia = PermissibleValue(text="repeated_episodes_shizofrenia")
    smalladenoma = PermissibleValue(text="smalladenoma")
    T1D_nonconverter = PermissibleValue(text="T1D_nonconverter")
    T1D_seroconverter = PermissibleValue(text="T1D_seroconverter")
    trichuris_trichiura = PermissibleValue(text="trichuris_trichiura")
    UC = PermissibleValue(text="UC")
    Ulcerative_colitis = PermissibleValue(text="Ulcerative_colitis")
    undetermined_colitis = PermissibleValue(text="undetermined_colitis")

    _defn = EnumDefinition(
        name="DiseaseSubtypeEnum",
    )

class DiseaseEnum(EnumDefinitionImpl):

    abdominalhernia = PermissibleValue(text="abdominalhernia")
    acute_diarrhoea = PermissibleValue(text="acute_diarrhoea")
    ACVD = PermissibleValue(text="ACVD")
    AD = PermissibleValue(text="AD")
    adenoma = PermissibleValue(text="adenoma")
    AR = PermissibleValue(text="AR")
    arthritis = PermissibleValue(text="arthritis")
    ascites = PermissibleValue(text="ascites")
    asthma = PermissibleValue(text="asthma")
    BD = PermissibleValue(text="BD")
    bronchitis = PermissibleValue(text="bronchitis")
    carcinoma_surgery_history = PermissibleValue(text="carcinoma_surgery_history")
    CDI = PermissibleValue(text="CDI")
    cellulitis = PermissibleValue(text="cellulitis")
    chorioamnionitis = PermissibleValue(text="chorioamnionitis")
    cirrhosis = PermissibleValue(text="cirrhosis")
    CMV = PermissibleValue(text="CMV")
    coeliac = PermissibleValue(text="coeliac")
    cough = PermissibleValue(text="cough")
    CRC = PermissibleValue(text="CRC")
    cystitis = PermissibleValue(text="cystitis")
    fatty_liver = PermissibleValue(text="fatty_liver")
    fever = PermissibleValue(text="fever")
    few_polyps = PermissibleValue(text="few_polyps")
    gangrene = PermissibleValue(text="gangrene")
    generic_diabetes = PermissibleValue(text="generic_diabetes")
    gestational_diabetes = PermissibleValue(text="gestational_diabetes")
    healthy = PermissibleValue(text="healthy")
    hepatitis = PermissibleValue(text="hepatitis")
    hypercholesterolemia = PermissibleValue(text="hypercholesterolemia")
    hypertension = PermissibleValue(text="hypertension")
    IBD = PermissibleValue(text="IBD")
    IGT = PermissibleValue(text="IGT")
    infectiousgastroenteritis = PermissibleValue(text="infectiousgastroenteritis")
    melanoma = PermissibleValue(text="melanoma")
    metabolic_syndrome = PermissibleValue(text="metabolic_syndrome")
    metastases = PermissibleValue(text="metastases")
    migraine = PermissibleValue(text="migraine")
    mucositis = PermissibleValue(text="mucositis")
    NK = PermissibleValue(text="NK")
    osteoarthritis = PermissibleValue(text="osteoarthritis")
    otitis = PermissibleValue(text="otitis")
    periodontitis = PermissibleValue(text="periodontitis")
    pneumonia = PermissibleValue(text="pneumonia")
    premature_born = PermissibleValue(text="premature_born")
    psoriasis = PermissibleValue(text="psoriasis")
    pyelonefritis = PermissibleValue(text="pyelonefritis")
    pyelonephritis = PermissibleValue(text="pyelonephritis")
    RA = PermissibleValue(text="RA")
    respiratoryinf = PermissibleValue(text="respiratoryinf")
    salmonellosis = PermissibleValue(text="salmonellosis")
    schizofrenia = PermissibleValue(text="schizofrenia")
    sepsis = PermissibleValue(text="sepsis")
    skininf = PermissibleValue(text="skininf")
    STEC = PermissibleValue(text="STEC")
    STH = PermissibleValue(text="STH")
    stomatitis = PermissibleValue(text="stomatitis")
    suspinf = PermissibleValue(text="suspinf")
    T1D = PermissibleValue(text="T1D")
    T2D = PermissibleValue(text="T2D")
    tonsillitis = PermissibleValue(text="tonsillitis")
    wilson = PermissibleValue(text="wilson")

    _defn = EnumDefinition(
        name="DiseaseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ME/CFS",
                PermissibleValue(text="ME/CFS") )
        setattr(cls, "peri-implantitis",
                PermissibleValue(text="peri-implantitis") )
        setattr(cls, "pre-eclampsia",
                PermissibleValue(text="pre-eclampsia") )

class StudyConditionEnum(EnumDefinitionImpl):

    abdominalhernia = PermissibleValue(text="abdominalhernia")
    acute_diarrhoea = PermissibleValue(text="acute_diarrhoea")
    ACVD = PermissibleValue(text="ACVD")
    AD = PermissibleValue(text="AD")
    adenoma = PermissibleValue(text="adenoma")
    AR = PermissibleValue(text="AR")
    arthritis = PermissibleValue(text="arthritis")
    AS = PermissibleValue(text="AS")
    ascites = PermissibleValue(text="ascites")
    asthma = PermissibleValue(text="asthma")
    BD = PermissibleValue(text="BD")
    bronchitis = PermissibleValue(text="bronchitis")
    carcinoma_surgery_history = PermissibleValue(text="carcinoma_surgery_history")
    CDI = PermissibleValue(text="CDI")
    cellulitis = PermissibleValue(text="cellulitis")
    cephalosporins = PermissibleValue(text="cephalosporins")
    chorioamnionitis = PermissibleValue(text="chorioamnionitis")
    cirrhosis = PermissibleValue(text="cirrhosis")
    CMV = PermissibleValue(text="CMV")
    coeliac = PermissibleValue(text="coeliac")
    control = PermissibleValue(text="control")
    cough = PermissibleValue(text="cough")
    CRC = PermissibleValue(text="CRC")
    cystitis = PermissibleValue(text="cystitis")
    fatty_liver = PermissibleValue(text="fatty_liver")
    fever = PermissibleValue(text="fever")
    FMT = PermissibleValue(text="FMT")
    gangrene = PermissibleValue(text="gangrene")
    generic_diabetes = PermissibleValue(text="generic_diabetes")
    gestational_diabetes = PermissibleValue(text="gestational_diabetes")
    hypertension = PermissibleValue(text="hypertension")
    IBD = PermissibleValue(text="IBD")
    IGT = PermissibleValue(text="IGT")
    infectiousgastroenteritis = PermissibleValue(text="infectiousgastroenteritis")
    melanoma = PermissibleValue(text="melanoma")
    metabolic_syndrome = PermissibleValue(text="metabolic_syndrome")
    migraine = PermissibleValue(text="migraine")
    mucositis = PermissibleValue(text="mucositis")
    NK = PermissibleValue(text="NK")
    osteoarthritis = PermissibleValue(text="osteoarthritis")
    otitis = PermissibleValue(text="otitis")
    periodontitis = PermissibleValue(text="periodontitis")
    pneumonia = PermissibleValue(text="pneumonia")
    premature_born = PermissibleValue(text="premature_born")
    psoriasis = PermissibleValue(text="psoriasis")
    pyelonefritis = PermissibleValue(text="pyelonefritis")
    pyelonephritis = PermissibleValue(text="pyelonephritis")
    RA = PermissibleValue(text="RA")
    respiratoryinf = PermissibleValue(text="respiratoryinf")
    salmonellosis = PermissibleValue(text="salmonellosis")
    schizofrenia = PermissibleValue(text="schizofrenia")
    sepsis = PermissibleValue(text="sepsis")
    skininf = PermissibleValue(text="skininf")
    SRP = PermissibleValue(text="SRP")
    STEC = PermissibleValue(text="STEC")
    STH = PermissibleValue(text="STH")
    stomatitis = PermissibleValue(text="stomatitis")
    suspinf = PermissibleValue(text="suspinf")
    T1D = PermissibleValue(text="T1D")
    T2D = PermissibleValue(text="T2D")
    tonsillitis = PermissibleValue(text="tonsillitis")
    wilson = PermissibleValue(text="wilson")

    _defn = EnumDefinition(
        name="StudyConditionEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ME/CFS",
                PermissibleValue(text="ME/CFS") )
        setattr(cls, "peri-implantitis",
                PermissibleValue(text="peri-implantitis") )
        setattr(cls, "pre-eclampsia",
                PermissibleValue(text="pre-eclampsia") )
        setattr(cls, "pre-hypertension",
                PermissibleValue(text="pre-hypertension") )

class AutoantibodyPositiveEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AutoantibodyPositiveEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "IAA;GADA",
                PermissibleValue(text="IAA;GADA",
                                 description="IAA;GADA") )
        setattr(cls, "IAA;GADA;IA-2A;ICA",
                PermissibleValue(text="IAA;GADA;IA-2A;ICA",
                                 description="IAA;GADA;IA-2A;ICA") )
        setattr(cls, "IAA;GADA;IA-2A;ZNT8A;ICA",
                PermissibleValue(text="IAA;GADA;IA-2A;ZNT8A;ICA",
                                 description="IAA;GADA;IA-2A;ZNT8A;ICA") )
        setattr(cls, "IAA;GADA;ZNT8A;ICA",
                PermissibleValue(text="IAA;GADA;ZNT8A;ICA",
                                 description="IAA;GADA;ZNT8A;ICA") )
        setattr(cls, "IAA;IA-2A;ZNT8A;ICA",
                PermissibleValue(text="IAA;IA-2A;ZNT8A;ICA",
                                 description="IAA;IA-2A;ZNT8A;ICA") )
        setattr(cls, "IAA;ICA",
                PermissibleValue(text="IAA;ICA",
                                 description="IAA;ICA") )

class PopulationEnum(EnumDefinitionImpl):

    Aeta = PermissibleValue(text="Aeta",
                               description="Aeta")
    African_American = PermissibleValue(text="African_American",
                                                       description="African_American")
    Agta = PermissibleValue(text="Agta",
                               description="Agta")
    Asian = PermissibleValue(text="Asian",
                                 description="Asian")
    Australoid = PermissibleValue(text="Australoid",
                                           description="Australoid")
    Bagyeli = PermissibleValue(text="Bagyeli",
                                     description="Bagyeli")
    Bantu = PermissibleValue(text="Bantu",
                                 description="Bantu")
    Batak = PermissibleValue(text="Batak",
                                 description="Batak")
    Bhopal = PermissibleValue(text="Bhopal",
                                   description="Bhopal")
    Casigurani = PermissibleValue(text="Casigurani",
                                           description="Casigurani")
    Caucasian = PermissibleValue(text="Caucasian",
                                         description="Caucasian")
    Caucasoid = PermissibleValue(text="Caucasoid",
                                         description="Caucasoid")
    Dutch = PermissibleValue(text="Dutch",
                                 description="Dutch")
    Hispanic_Latino = PermissibleValue(text="Hispanic_Latino",
                                                     description="Hispanic_Latino")
    Kerala = PermissibleValue(text="Kerala",
                                   description="Kerala")
    MDG_1FE = PermissibleValue(text="MDG_1FE",
                                     description="MDG_1FE")
    MDG_2FE = PermissibleValue(text="MDG_2FE",
                                     description="MDG_2FE")
    Mongoloid = PermissibleValue(text="Mongoloid",
                                         description="Mongoloid")
    Tagbanua = PermissibleValue(text="Tagbanua",
                                       description="Tagbanua")
    Zambal = PermissibleValue(text="Zambal",
                                   description="Zambal")
    asian = PermissibleValue(text="asian",
                                 description="asian")
    hispanic = PermissibleValue(text="hispanic",
                                       description="hispanic")

    _defn = EnumDefinition(
        name="PopulationEnum",
    )

class SubcohortEnum(EnumDefinitionImpl):

    Barcelona = PermissibleValue(text="Barcelona",
                                         description="Barcelona")
    Leeds = PermissibleValue(text="Leeds",
                                 description="Leeds")

    _defn = EnumDefinition(
        name="SubcohortEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "PRIMM-NL",
                PermissibleValue(text="PRIMM-NL",
                                 description="PRIMM-NL") )
        setattr(cls, "PRIMM-UK",
                PermissibleValue(text="PRIMM-UK",
                                 description="PRIMM-UK") )

# Slots
class slots:
    pass

slots.ALT = Slot(uri=CMD.ALT, name="ALT", curie=CMD.curie('ALT'),
                   model_uri=CMD.ALT, domain=None, range=Optional[float])

slots.ASO = Slot(uri=CMD.ASO, name="ASO", curie=CMD.curie('ASO'),
                   model_uri=CMD.ASO, domain=None, range=Optional[float])

slots.BASDAI = Slot(uri=CMD.BASDAI, name="BASDAI", curie=CMD.curie('BASDAI'),
                   model_uri=CMD.BASDAI, domain=None, range=Optional[float])

slots.BASFI = Slot(uri=CMD.BASFI, name="BASFI", curie=CMD.curie('BASFI'),
                   model_uri=CMD.BASFI, domain=None, range=Optional[float])

slots.BMI = Slot(uri=CMD.BMI, name="BMI", curie=CMD.curie('BMI'),
                   model_uri=CMD.BMI, domain=None, range=Optional[float])

slots.DNA_extraction_kit = Slot(uri=CMD.DNA_extraction_kit, name="DNA_extraction_kit", curie=CMD.curie('DNA_extraction_kit'),
                   model_uri=CMD.DNA_extraction_kit, domain=None, range=Optional[str])

slots.ESR = Slot(uri=CMD.ESR, name="ESR", curie=CMD.curie('ESR'),
                   model_uri=CMD.ESR, domain=None, range=Optional[float])

slots.HBI = Slot(uri=CMD.HBI, name="HBI", curie=CMD.curie('HBI'),
                   model_uri=CMD.HBI, domain=None, range=Optional[float])

slots.HLA = Slot(uri=CMD.HLA, name="HLA", curie=CMD.curie('HLA'),
                   model_uri=CMD.HLA, domain=None, range=Optional[Union[str, List[str]]])

slots.NCBI_accession = Slot(uri=CMD.NCBI_accession, name="NCBI_accession", curie=CMD.curie('NCBI_accession'),
                   model_uri=CMD.NCBI_accession, domain=None, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'[ES]R[SR][0-9]+'))

slots.ORR = Slot(uri=CMD.ORR, name="ORR", curie=CMD.curie('ORR'),
                   model_uri=CMD.ORR, domain=None, range=Optional[str])

slots.PFS12 = Slot(uri=CMD.PFS12, name="PFS12", curie=CMD.curie('PFS12'),
                   model_uri=CMD.PFS12, domain=None, range=Optional[str])

slots.PMID = Slot(uri=CMD.PMID, name="PMID", curie=CMD.curie('PMID'),
                   model_uri=CMD.PMID, domain=None, range=Optional[str],
                   pattern=re.compile(r'[0-9]{8}'))

slots.PPD_B = Slot(uri=CMD.PPD_B, name="PPD_B", curie=CMD.curie('PPD_B'),
                   model_uri=CMD.PPD_B, domain=None, range=Optional[float])

slots.PPD_D = Slot(uri=CMD.PPD_D, name="PPD_D", curie=CMD.curie('PPD_D'),
                   model_uri=CMD.PPD_D, domain=None, range=Optional[float])

slots.PPD_L = Slot(uri=CMD.PPD_L, name="PPD_L", curie=CMD.curie('PPD_L'),
                   model_uri=CMD.PPD_L, domain=None, range=Optional[float])

slots.PPD_M = Slot(uri=CMD.PPD_M, name="PPD_M", curie=CMD.curie('PPD_M'),
                   model_uri=CMD.PPD_M, domain=None, range=Optional[float])

slots.RECIST = Slot(uri=CMD.RECIST, name="RECIST", curie=CMD.curie('RECIST'),
                   model_uri=CMD.RECIST, domain=None, range=Optional[str])

slots.SCCAI = Slot(uri=CMD.SCCAI, name="SCCAI", curie=CMD.curie('SCCAI'),
                   model_uri=CMD.SCCAI, domain=None, range=Optional[float])

slots.adiponectin = Slot(uri=CMD.adiponectin, name="adiponectin", curie=CMD.curie('adiponectin'),
                   model_uri=CMD.adiponectin, domain=None, range=Optional[float])

slots.age = Slot(uri=CMD.age, name="age", curie=CMD.curie('age'),
                   model_uri=CMD.age, domain=None, range=str)

slots.age_T1D_diagnosis = Slot(uri=CMD.age_T1D_diagnosis, name="age_T1D_diagnosis", curie=CMD.curie('age_T1D_diagnosis'),
                   model_uri=CMD.age_T1D_diagnosis, domain=None, range=Optional[float])

slots.age_category = Slot(uri=CMD.age_category, name="age_category", curie=CMD.curie('age_category'),
                   model_uri=CMD.age_category, domain=None, range=Optional[str])

slots.age_seroconversion = Slot(uri=CMD.age_seroconversion, name="age_seroconversion", curie=CMD.curie('age_seroconversion'),
                   model_uri=CMD.age_seroconversion, domain=None, range=Optional[float])

slots.age_twins_started_to_live_apart = Slot(uri=CMD.age_twins_started_to_live_apart, name="age_twins_started_to_live_apart", curie=CMD.curie('age_twins_started_to_live_apart'),
                   model_uri=CMD.age_twins_started_to_live_apart, domain=None, range=Optional[int])

slots.ajcc = Slot(uri=CMD.ajcc, name="ajcc", curie=CMD.curie('ajcc'),
                   model_uri=CMD.ajcc, domain=None, range=Optional[str],
                   pattern=re.compile(r'0|i|ii|iii|iv|iii/iv'))

slots.albumine = Slot(uri=CMD.albumine, name="albumine", curie=CMD.curie('albumine'),
                   model_uri=CMD.albumine, domain=None, range=Optional[float])

slots.alcohol = Slot(uri=CMD.alcohol, name="alcohol", curie=CMD.curie('alcohol'),
                   model_uri=CMD.alcohol, domain=None, range=Optional[str])

slots.alcohol_numeric = Slot(uri=CMD.alcohol_numeric, name="alcohol_numeric", curie=CMD.curie('alcohol_numeric'),
                   model_uri=CMD.alcohol_numeric, domain=None, range=Optional[float])

slots.anti_PD_1 = Slot(uri=CMD.anti_PD_1, name="anti_PD_1", curie=CMD.curie('anti_PD_1'),
                   model_uri=CMD.anti_PD_1, domain=None, range=Optional[str])

slots.anti_ccp_antibody = Slot(uri=CMD.anti_ccp_antibody, name="anti_ccp_antibody", curie=CMD.curie('anti_ccp_antibody'),
                   model_uri=CMD.anti_ccp_antibody, domain=None, range=Optional[float])

slots.antibiotics_current_use = Slot(uri=CMD.antibiotics_current_use, name="antibiotics_current_use", curie=CMD.curie('antibiotics_current_use'),
                   model_uri=CMD.antibiotics_current_use, domain=None, range=Optional[str])

slots.antibiotics_family = Slot(uri=CMD.antibiotics_family, name="antibiotics_family", curie=CMD.curie('antibiotics_family'),
                   model_uri=CMD.antibiotics_family, domain=None, range=Optional[Union[str, List[str]]])

slots.ast = Slot(uri=CMD.ast, name="ast", curie=CMD.curie('ast'),
                   model_uri=CMD.ast, domain=None, range=Optional[float])

slots.autoantibody_positive = Slot(uri=CMD.autoantibody_positive, name="autoantibody_positive", curie=CMD.curie('autoantibody_positive'),
                   model_uri=CMD.autoantibody_positive, domain=None, range=Optional[Union[str, List[str]]])

slots.bilubirin = Slot(uri=CMD.bilubirin, name="bilubirin", curie=CMD.curie('bilubirin'),
                   model_uri=CMD.bilubirin, domain=None, range=Optional[float])

slots.birth_control_pil = Slot(uri=CMD.birth_control_pil, name="birth_control_pil", curie=CMD.curie('birth_control_pil'),
                   model_uri=CMD.birth_control_pil, domain=None, range=Optional[str])

slots.birth_order = Slot(uri=CMD.birth_order, name="birth_order", curie=CMD.curie('birth_order'),
                   model_uri=CMD.birth_order, domain=None, range=Optional[int])

slots.birth_weight = Slot(uri=CMD.birth_weight, name="birth_weight", curie=CMD.curie('birth_weight'),
                   model_uri=CMD.birth_weight, domain=None, range=Optional[float])

slots.blood_platelet = Slot(uri=CMD.blood_platelet, name="blood_platelet", curie=CMD.curie('blood_platelet'),
                   model_uri=CMD.blood_platelet, domain=None, range=Optional[float])

slots.body_site = Slot(uri=CMD.body_site, name="body_site", curie=CMD.curie('body_site'),
                   model_uri=CMD.body_site, domain=None, range=str)

slots.body_subsite = Slot(uri=CMD.body_subsite, name="body_subsite", curie=CMD.curie('body_subsite'),
                   model_uri=CMD.body_subsite, domain=None, range=Optional[str])

slots.born_method = Slot(uri=CMD.born_method, name="born_method", curie=CMD.curie('born_method'),
                   model_uri=CMD.born_method, domain=None, range=Optional[str])

slots.breastfeeding_duration = Slot(uri=CMD.breastfeeding_duration, name="breastfeeding_duration", curie=CMD.curie('breastfeeding_duration'),
                   model_uri=CMD.breastfeeding_duration, domain=None, range=Optional[int])

slots.brinkman_index = Slot(uri=CMD.brinkman_index, name="brinkman_index", curie=CMD.curie('brinkman_index'),
                   model_uri=CMD.brinkman_index, domain=None, range=Optional[float])

slots.c_peptide = Slot(uri=CMD.c_peptide, name="c_peptide", curie=CMD.curie('c_peptide'),
                   model_uri=CMD.c_peptide, domain=None, range=Optional[float])

slots.c_section_type = Slot(uri=CMD.c_section_type, name="c_section_type", curie=CMD.curie('c_section_type'),
                   model_uri=CMD.c_section_type, domain=None, range=Optional[str])

slots.calprotectin = Slot(uri=CMD.calprotectin, name="calprotectin", curie=CMD.curie('calprotectin'),
                   model_uri=CMD.calprotectin, domain=None, range=Optional[float])

slots.cd163 = Slot(uri=CMD.cd163, name="cd163", curie=CMD.curie('cd163'),
                   model_uri=CMD.cd163, domain=None, range=Optional[float])

slots.change_in_tumor_size = Slot(uri=CMD.change_in_tumor_size, name="change_in_tumor_size", curie=CMD.curie('change_in_tumor_size'),
                   model_uri=CMD.change_in_tumor_size, domain=None, range=Optional[str])

slots.cholesterol = Slot(uri=CMD.cholesterol, name="cholesterol", curie=CMD.curie('cholesterol'),
                   model_uri=CMD.cholesterol, domain=None, range=Optional[float])

slots.country = Slot(uri=CMD.country, name="country", curie=CMD.curie('country'),
                   model_uri=CMD.country, domain=None, range=str)

slots.creatine = Slot(uri=CMD.creatine, name="creatine", curie=CMD.curie('creatine'),
                   model_uri=CMD.creatine, domain=None, range=Optional[float])

slots.creatinine = Slot(uri=CMD.creatinine, name="creatinine", curie=CMD.curie('creatinine'),
                   model_uri=CMD.creatinine, domain=None, range=Optional[float])

slots.ctp = Slot(uri=CMD.ctp, name="ctp", curie=CMD.curie('ctp'),
                   model_uri=CMD.ctp, domain=None, range=Optional[int])

slots.curator = Slot(uri=CMD.curator, name="curator", curie=CMD.curie('curator'),
                   model_uri=CMD.curator, domain=None, range=Union[str, List[str]])

slots.days_after_onset = Slot(uri=CMD.days_after_onset, name="days_after_onset", curie=CMD.curie('days_after_onset'),
                   model_uri=CMD.days_after_onset, domain=None, range=Optional[int])

slots.days_from_first_collection = Slot(uri=CMD.days_from_first_collection, name="days_from_first_collection", curie=CMD.curie('days_from_first_collection'),
                   model_uri=CMD.days_from_first_collection, domain=None, range=Optional[int])

slots.dental_sample_type = Slot(uri=CMD.dental_sample_type, name="dental_sample_type", curie=CMD.curie('dental_sample_type'),
                   model_uri=CMD.dental_sample_type, domain=None, range=Optional[str])

slots.diet = Slot(uri=CMD.diet, name="diet", curie=CMD.curie('diet'),
                   model_uri=CMD.diet, domain=None, range=Optional[str])

slots.disease = Slot(uri=CMD.disease, name="disease", curie=CMD.curie('disease'),
                   model_uri=CMD.disease, domain=None, range=Optional[Union[str, List[str]]])

slots.disease_location = Slot(uri=CMD.disease_location, name="disease_location", curie=CMD.curie('disease_location'),
                   model_uri=CMD.disease_location, domain=None, range=Optional[Union[str, List[str]]])

slots.disease_stage = Slot(uri=CMD.disease_stage, name="disease_stage", curie=CMD.curie('disease_stage'),
                   model_uri=CMD.disease_stage, domain=None, range=Optional[str])

slots.disease_subtype = Slot(uri=CMD.disease_subtype, name="disease_subtype", curie=CMD.curie('disease_subtype'),
                   model_uri=CMD.disease_subtype, domain=None, range=Optional[Union[str, List[str]]])

slots.dyastolic_p = Slot(uri=CMD.dyastolic_p, name="dyastolic_p", curie=CMD.curie('dyastolic_p'),
                   model_uri=CMD.dyastolic_p, domain=None, range=Optional[float])

slots.eGFR = Slot(uri=CMD.eGFR, name="eGFR", curie=CMD.curie('eGFR'),
                   model_uri=CMD.eGFR, domain=None, range=Optional[float])

slots.ever_smoker = Slot(uri=CMD.ever_smoker, name="ever_smoker", curie=CMD.curie('ever_smoker'),
                   model_uri=CMD.ever_smoker, domain=None, range=Optional[str])

slots.family = Slot(uri=CMD.family, name="family", curie=CMD.curie('family'),
                   model_uri=CMD.family, domain=None, range=Optional[str])

slots.family_role = Slot(uri=CMD.family_role, name="family_role", curie=CMD.curie('family_role'),
                   model_uri=CMD.family_role, domain=None, range=Optional[str])

slots.fasting_glucose = Slot(uri=CMD.fasting_glucose, name="fasting_glucose", curie=CMD.curie('fasting_glucose'),
                   model_uri=CMD.fasting_glucose, domain=None, range=Optional[float])

slots.fasting_insulin = Slot(uri=CMD.fasting_insulin, name="fasting_insulin", curie=CMD.curie('fasting_insulin'),
                   model_uri=CMD.fasting_insulin, domain=None, range=Optional[float])

slots.feeding_practice = Slot(uri=CMD.feeding_practice, name="feeding_practice", curie=CMD.curie('feeding_practice'),
                   model_uri=CMD.feeding_practice, domain=None, range=Optional[str])

slots.ferm_milk_prod_consumer = Slot(uri=CMD.ferm_milk_prod_consumer, name="ferm_milk_prod_consumer", curie=CMD.curie('ferm_milk_prod_consumer'),
                   model_uri=CMD.ferm_milk_prod_consumer, domain=None, range=Optional[str])

slots.fgf_19 = Slot(uri=CMD.fgf_19, name="fgf_19", curie=CMD.curie('fgf_19'),
                   model_uri=CMD.fgf_19, domain=None, range=Optional[float])

slots.flg_genotype = Slot(uri=CMD.flg_genotype, name="flg_genotype", curie=CMD.curie('flg_genotype'),
                   model_uri=CMD.flg_genotype, domain=None, range=Optional[str])

slots.fobt = Slot(uri=CMD.fobt, name="fobt", curie=CMD.curie('fobt'),
                   model_uri=CMD.fobt, domain=None, range=Optional[str])

slots.formula_first_day = Slot(uri=CMD.formula_first_day, name="formula_first_day", curie=CMD.curie('formula_first_day'),
                   model_uri=CMD.formula_first_day, domain=None, range=Optional[int])

slots.gender = Slot(uri=CMD.gender, name="gender", curie=CMD.curie('gender'),
                   model_uri=CMD.gender, domain=None, range=str)

slots.gestational_age = Slot(uri=CMD.gestational_age, name="gestational_age", curie=CMD.curie('gestational_age'),
                   model_uri=CMD.gestational_age, domain=None, range=Optional[float])

slots.globulin = Slot(uri=CMD.globulin, name="globulin", curie=CMD.curie('globulin'),
                   model_uri=CMD.globulin, domain=None, range=Optional[float])

slots.glp_1 = Slot(uri=CMD.glp_1, name="glp_1", curie=CMD.curie('glp_1'),
                   model_uri=CMD.glp_1, domain=None, range=Optional[float])

slots.glucose = Slot(uri=CMD.glucose, name="glucose", curie=CMD.curie('glucose'),
                   model_uri=CMD.glucose, domain=None, range=Optional[float])

slots.glutamate_decarboxylase_2_antibody = Slot(uri=CMD.glutamate_decarboxylase_2_antibody, name="glutamate_decarboxylase_2_antibody", curie=CMD.curie('glutamate_decarboxylase_2_antibody'),
                   model_uri=CMD.glutamate_decarboxylase_2_antibody, domain=None, range=Optional[float])

slots.hba1c = Slot(uri=CMD.hba1c, name="hba1c", curie=CMD.curie('hba1c'),
                   model_uri=CMD.hba1c, domain=None, range=Optional[float])

slots.hdl = Slot(uri=CMD.hdl, name="hdl", curie=CMD.curie('hdl'),
                   model_uri=CMD.hdl, domain=None, range=Optional[float])

slots.hemoglobinometry = Slot(uri=CMD.hemoglobinometry, name="hemoglobinometry", curie=CMD.curie('hemoglobinometry'),
                   model_uri=CMD.hemoglobinometry, domain=None, range=Optional[float])

slots.history_of_periodontitis = Slot(uri=CMD.history_of_periodontitis, name="history_of_periodontitis", curie=CMD.curie('history_of_periodontitis'),
                   model_uri=CMD.history_of_periodontitis, domain=None, range=Optional[str])

slots.hitchip_probe_class = Slot(uri=CMD.hitchip_probe_class, name="hitchip_probe_class", curie=CMD.curie('hitchip_probe_class'),
                   model_uri=CMD.hitchip_probe_class, domain=None, range=Optional[str])

slots.hla_dqa11 = Slot(uri=CMD.hla_dqa11, name="hla_dqa11", curie=CMD.curie('hla_dqa11'),
                   model_uri=CMD.hla_dqa11, domain=None, range=Optional[int])

slots.hla_dqa12 = Slot(uri=CMD.hla_dqa12, name="hla_dqa12", curie=CMD.curie('hla_dqa12'),
                   model_uri=CMD.hla_dqa12, domain=None, range=Optional[int])

slots.hla_drb11 = Slot(uri=CMD.hla_drb11, name="hla_drb11", curie=CMD.curie('hla_drb11'),
                   model_uri=CMD.hla_drb11, domain=None, range=Optional[int])

slots.hla_drb12 = Slot(uri=CMD.hla_drb12, name="hla_drb12", curie=CMD.curie('hla_drb12'),
                   model_uri=CMD.hla_drb12, domain=None, range=Optional[int])

slots.hscrp = Slot(uri=CMD.hscrp, name="hscrp", curie=CMD.curie('hscrp'),
                   model_uri=CMD.hscrp, domain=None, range=Optional[float])

slots.il_1 = Slot(uri=CMD.il_1, name="il_1", curie=CMD.curie('il_1'),
                   model_uri=CMD.il_1, domain=None, range=Optional[float])

slots.infant_age = Slot(uri=CMD.infant_age, name="infant_age", curie=CMD.curie('infant_age'),
                   model_uri=CMD.infant_age, domain=None, range=Optional[int])

slots.inr = Slot(uri=CMD.inr, name="inr", curie=CMD.curie('inr'),
                   model_uri=CMD.inr, domain=None, range=Optional[float])

slots.insulin_cat = Slot(uri=CMD.insulin_cat, name="insulin_cat", curie=CMD.curie('insulin_cat'),
                   model_uri=CMD.insulin_cat, domain=None, range=Optional[str])

slots.lactating = Slot(uri=CMD.lactating, name="lactating", curie=CMD.curie('lactating'),
                   model_uri=CMD.lactating, domain=None, range=Optional[str])

slots.ldl = Slot(uri=CMD.ldl, name="ldl", curie=CMD.curie('ldl'),
                   model_uri=CMD.ldl, domain=None, range=Optional[float])

slots.leptin = Slot(uri=CMD.leptin, name="leptin", curie=CMD.curie('leptin'),
                   model_uri=CMD.leptin, domain=None, range=Optional[float])

slots.lifestyle = Slot(uri=CMD.lifestyle, name="lifestyle", curie=CMD.curie('lifestyle'),
                   model_uri=CMD.lifestyle, domain=None, range=Optional[str])

slots.location = Slot(uri=CMD.location, name="location", curie=CMD.curie('location'),
                   model_uri=CMD.location, domain=None, range=Optional[str])

slots.median_read_length = Slot(uri=CMD.median_read_length, name="median_read_length", curie=CMD.curie('median_read_length'),
                   model_uri=CMD.median_read_length, domain=None, range=int)

slots.menopausal_status = Slot(uri=CMD.menopausal_status, name="menopausal_status", curie=CMD.curie('menopausal_status'),
                   model_uri=CMD.menopausal_status, domain=None, range=Optional[str])

slots.mgs_richness = Slot(uri=CMD.mgs_richness, name="mgs_richness", curie=CMD.curie('mgs_richness'),
                   model_uri=CMD.mgs_richness, domain=None, range=Optional[float])

slots.minimum_read_length = Slot(uri=CMD.minimum_read_length, name="minimum_read_length", curie=CMD.curie('minimum_read_length'),
                   model_uri=CMD.minimum_read_length, domain=None, range=int)

slots.mumps = Slot(uri=CMD.mumps, name="mumps", curie=CMD.curie('mumps'),
                   model_uri=CMD.mumps, domain=None, range=Optional[str])

slots.non_westernized = Slot(uri=CMD.non_westernized, name="non_westernized", curie=CMD.curie('non_westernized'),
                   model_uri=CMD.non_westernized, domain=None, range=Optional[str])

slots.number_bases = Slot(uri=CMD.number_bases, name="number_bases", curie=CMD.curie('number_bases'),
                   model_uri=CMD.number_bases, domain=None, range=int)

slots.number_reads = Slot(uri=CMD.number_reads, name="number_reads", curie=CMD.curie('number_reads'),
                   model_uri=CMD.number_reads, domain=None, range=int)

slots.performance_status = Slot(uri=CMD.performance_status, name="performance_status", curie=CMD.curie('performance_status'),
                   model_uri=CMD.performance_status, domain=None, range=Optional[float])

slots.population = Slot(uri=CMD.population, name="population", curie=CMD.curie('population'),
                   model_uri=CMD.population, domain=None, range=Optional[str],
                   pattern=re.compile(r'[a-zA-Z]\S+'))

slots.pregnant = Slot(uri=CMD.pregnant, name="pregnant", curie=CMD.curie('pregnant'),
                   model_uri=CMD.pregnant, domain=None, range=Optional[str])

slots.premature = Slot(uri=CMD.premature, name="premature", curie=CMD.curie('premature'),
                   model_uri=CMD.premature, domain=None, range=Optional[str])

slots.previous_therapy = Slot(uri=CMD.previous_therapy, name="previous_therapy", curie=CMD.curie('previous_therapy'),
                   model_uri=CMD.previous_therapy, domain=None, range=Optional[str])

slots.protein_intake = Slot(uri=CMD.protein_intake, name="protein_intake", curie=CMD.curie('protein_intake'),
                   model_uri=CMD.protein_intake, domain=None, range=Optional[float])

slots.prothrombin_time = Slot(uri=CMD.prothrombin_time, name="prothrombin_time", curie=CMD.curie('prothrombin_time'),
                   model_uri=CMD.prothrombin_time, domain=None, range=Optional[float])

slots.rbc = Slot(uri=CMD.rbc, name="rbc", curie=CMD.curie('rbc'),
                   model_uri=CMD.rbc, domain=None, range=Optional[float])

slots.remission = Slot(uri=CMD.remission, name="remission", curie=CMD.curie('remission'),
                   model_uri=CMD.remission, domain=None, range=Optional[str])

slots.rheumatoid_factor = Slot(uri=CMD.rheumatoid_factor, name="rheumatoid_factor", curie=CMD.curie('rheumatoid_factor'),
                   model_uri=CMD.rheumatoid_factor, domain=None, range=Optional[float])

slots.sample_id = Slot(uri=CMD.sample_id, name="sample_id", curie=CMD.curie('sample_id'),
                   model_uri=CMD.sample_id, domain=None, range=str,
                   pattern=re.compile(r'[0-9a-zA-Z_]'))

slots.sequencing_platform = Slot(uri=CMD.sequencing_platform, name="sequencing_platform", curie=CMD.curie('sequencing_platform'),
                   model_uri=CMD.sequencing_platform, domain=None, range=str)

slots.shigatoxin_2_elisa = Slot(uri=CMD.shigatoxin_2_elisa, name="shigatoxin_2_elisa", curie=CMD.curie('shigatoxin_2_elisa'),
                   model_uri=CMD.shigatoxin_2_elisa, domain=None, range=Optional[str])

slots.smoker = Slot(uri=CMD.smoker, name="smoker", curie=CMD.curie('smoker'),
                   model_uri=CMD.smoker, domain=None, range=Optional[str])

slots.stec_count = Slot(uri=CMD.stec_count, name="stec_count", curie=CMD.curie('stec_count'),
                   model_uri=CMD.stec_count, domain=None, range=Optional[str])

slots.stool_texture = Slot(uri=CMD.stool_texture, name="stool_texture", curie=CMD.curie('stool_texture'),
                   model_uri=CMD.stool_texture, domain=None, range=Optional[str])

slots.study_condition = Slot(uri=CMD.study_condition, name="study_condition", curie=CMD.curie('study_condition'),
                   model_uri=CMD.study_condition, domain=None, range=Optional[str])

slots.study_name = Slot(uri=CMD.study_name, name="study_name", curie=CMD.curie('study_name'),
                   model_uri=CMD.study_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'[a-zA-Z-]+_[0-9]{4}|[a-zA-Z-]+_[0-9]{4}[a-zA-Z-]+|[a-zA-Z-]+_[0-9]{4}_[a-zA-Z-]+|[a-zA-Z-]+_[0-9]{4}_[a-zA-Z0-9]+'))

slots.subcohort = Slot(uri=CMD.subcohort, name="subcohort", curie=CMD.curie('subcohort'),
                   model_uri=CMD.subcohort, domain=None, range=Optional[str],
                   pattern=re.compile(r'[a-zA-Z]\S+'))

slots.subject_id = Slot(uri=CMD.subject_id, name="subject_id", curie=CMD.curie('subject_id'),
                   model_uri=CMD.subject_id, domain=None, range=str,
                   pattern=re.compile(r'[0-9a-zA-Z_]'))

slots.systolic_p = Slot(uri=CMD.systolic_p, name="systolic_p", curie=CMD.curie('systolic_p'),
                   model_uri=CMD.systolic_p, domain=None, range=Optional[float])

slots.tnm = Slot(uri=CMD.tnm, name="tnm", curie=CMD.curie('tnm'),
                   model_uri=CMD.tnm, domain=None, range=Optional[str])

slots.toxicity_above_zero = Slot(uri=CMD.toxicity_above_zero, name="toxicity_above_zero", curie=CMD.curie('toxicity_above_zero'),
                   model_uri=CMD.toxicity_above_zero, domain=None, range=Optional[str])

slots.travel_destination = Slot(uri=CMD.travel_destination, name="travel_destination", curie=CMD.curie('travel_destination'),
                   model_uri=CMD.travel_destination, domain=None, range=Optional[str])

slots.treatment = Slot(uri=CMD.treatment, name="treatment", curie=CMD.curie('treatment'),
                   model_uri=CMD.treatment, domain=None, range=Optional[Union[str, List[str]]])

slots.triglycerides = Slot(uri=CMD.triglycerides, name="triglycerides", curie=CMD.curie('triglycerides'),
                   model_uri=CMD.triglycerides, domain=None, range=Optional[float])

slots.uncurated_metadata = Slot(uri=CMD.uncurated_metadata, name="uncurated_metadata", curie=CMD.curie('uncurated_metadata'),
                   model_uri=CMD.uncurated_metadata, domain=None, range=Optional[str])

slots.urea_nitrogen = Slot(uri=CMD.urea_nitrogen, name="urea_nitrogen", curie=CMD.curie('urea_nitrogen'),
                   model_uri=CMD.urea_nitrogen, domain=None, range=Optional[float])

slots.visit_number = Slot(uri=CMD.visit_number, name="visit_number", curie=CMD.curie('visit_number'),
                   model_uri=CMD.visit_number, domain=None, range=Optional[int])

slots.wbc = Slot(uri=CMD.wbc, name="wbc", curie=CMD.curie('wbc'),
                   model_uri=CMD.wbc, domain=None, range=Optional[float])

slots.zigosity = Slot(uri=CMD.zigosity, name="zigosity", curie=CMD.curie('zigosity'),
                   model_uri=CMD.zigosity, domain=None, range=Optional[str])

slots.samples = Slot(uri=CMD.samples, name="samples", curie=CMD.curie('samples'),
                   model_uri=CMD.samples, domain=None, range=Optional[Union[Union[dict, Sample], List[Union[dict, Sample]]]])

slots.studies = Slot(uri=CMD.studies, name="studies", curie=CMD.curie('studies'),
                   model_uri=CMD.studies, domain=None, range=Optional[Union[Union[dict, Study], List[Union[dict, Study]]]])

slots.project_name = Slot(uri=CMD.project_name, name="project_name", curie=CMD.curie('project_name'),
                   model_uri=CMD.project_name, domain=None, range=Optional[str])