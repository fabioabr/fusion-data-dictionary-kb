---
id: DOC-HCM-PVO-ParticipantEnrollmentPVO
doc_type: system-doc
title: "ParticipantEnrollmentPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ParticipantEnrollmentPVO
  - participantenrollmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ParticipantEnrollmentPVO

## 📌 Visão Geral

Consolida inscrições de participantes em planos de benefícios com valores de taxas, grupos e relações. Visão central do enrollment para análise de adesão e custos de benefícios.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.ParticipantEnrollmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 227 | 5 | 11 | 79 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[ben_benefit_relations_f|BEN_BENEFIT_RELATIONS_F]] — 9 atributos (3 PKs, 5 BICC)
- [[ben_per_benefit_group_f|BEN_PER_BENEFIT_GROUP_F]] — 6 atributos (3 PKs, 4 BICC)
- [[ben_prtt_enrt_rslt|BEN_PRTT_ENRT_RSLT]] — 111 atributos (1 PKs, 39 BICC)
- [[ben_prtt_rt_val|BEN_PRTT_RT_VAL]] — 98 atributos (1 PKs, 28 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos (3 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[ben_benefit_relations_f|BEN_BENEFIT_RELATIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BenefitRelSystemCd | BENEFIT_REL_SYSTEM_CD | — | — |
| 2 | BenefitRelationId1 | BENEFIT_RELATION_ID | 🔑 | ✅ |
| 3 | BenefitRelationName | BENEFIT_RELATION_NAME | — | ✅ |
| 4 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 5 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | PrimaryRel | PRIMARY_REL | — | ✅ |
| 8 | RelPrmryAsgId | REL_PRMRY_ASG_ID | — | — |
| 9 | Status | STATUS | — | — |

### [[ben_per_benefit_group_f|BEN_PER_BENEFIT_GROUP_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BenefitGroupId | BENEFIT_GROUP_ID | — | — |
| 2 | EffectiveEndDate2 | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 3 | EffectiveEndDate3 | EFFECTIVE_END_DATE | — | — |
| 4 | EffectiveStartDate1 | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 5 | EffectiveStartDate2 | EFFECTIVE_START_DATE | — | ✅ |
| 6 | LeBenefitGroupId | LE_BENEFIT_GROUP_ID | 🔑 | ✅ |

### [[ben_prtt_enrt_rslt|BEN_PRTT_ENRT_RSLT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdminCategoryCd | ADMIN_CATEGORY_CD | — | — |
| 2 | AssignmentId | ASSIGNMENT_ID | — | — |
| 3 | BenefitRelationId | BENEFIT_RELATION_ID | — | — |
| 4 | BnftAmt | BNFT_AMT | — | ✅ |
| 5 | BnftNnmntryUom | BNFT_NNMNTRY_UOM | — | ✅ |
| 6 | BnftOrdrNum | BNFT_ORDR_NUM | — | ✅ |
| 7 | BnftTypCd | BNFT_TYP_CD | — | ✅ |
| 8 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 9 | CirBenefitId | CIR_BENEFIT_ID | — | — |
| 10 | CompLvlCd | COMP_LVL_CD | — | ✅ |
| 11 | ConfigChar1 | CONFIG_CHAR_1 | — | ✅ |
| 12 | ConfigChar10 | CONFIG_CHAR_10 | — | — |
| 13 | ConfigChar6 | CONFIG_CHAR_6 | — | — |
| 14 | ConfigChar7 | CONFIG_CHAR_7 | — | — |
| 15 | ConfigChar8 | CONFIG_CHAR_8 | — | — |
| 16 | ConfigChar9 | CONFIG_CHAR_9 | — | — |
| 17 | ConfigId1 | CONFIG_ID_1 | — | — |
| 18 | ConfigId2 | CONFIG_ID_2 | — | — |
| 19 | ConfigId3 | CONFIG_ID_3 | — | — |
| 20 | ConfigId4 | CONFIG_ID_4 | — | — |
| 21 | ConfigId5 | CONFIG_ID_5 | — | — |
| 22 | ConfigNum1 | CONFIG_NUM_1 | — | — |
| 23 | ConfigNum10 | CONFIG_NUM_10 | — | — |
| 24 | ConfigNum6 | CONFIG_NUM_6 | — | — |
| 25 | ConfigNum7 | CONFIG_NUM_7 | — | — |
| 26 | ConfigNum8 | CONFIG_NUM_8 | — | — |
| 27 | ConfigNum9 | CONFIG_NUM_9 | — | — |
| 28 | CreatedBy | CREATED_BY | — | ✅ |
| 29 | CreationDate | CREATION_DATE | — | ✅ |
| 30 | ElectionDate | ELECTION_DATE | — | ✅ |
| 31 | EndedCvgThruDt | ENDED_CVG_THRU_DT | — | — |
| 32 | EndedPerInLerId | ENDED_PER_IN_LER_ID | — | — |
| 33 | EnrtCvgStrtDt | ENRT_CVG_STRT_DT | — | ✅ |
| 34 | EnrtCvgThruDt | ENRT_CVG_THRU_DT | — | ✅ |
| 35 | EnrtMthdCd | ENRT_MTHD_CD | — | ✅ |
| 36 | EnrtOvridRsnCd | ENRT_OVRID_RSN_CD | — | ✅ |
| 37 | EnrtOvridThruDt | ENRT_OVRID_THRU_DT | — | ✅ |
| 38 | EnrtOvridnFlag | ENRT_OVRIDN_FLAG | — | ✅ |
| 39 | ErlstDeenrtDt | ERLST_DEENRT_DT | — | ✅ |
| 40 | ImptdIncmCalcCd | IMPTD_INCM_CALC_CD | — | — |
| 41 | InterimFlag | INTERIM_FLAG | — | ✅ |
| 42 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 43 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 44 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 45 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 46 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 47 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 48 | LerId | LER_ID | — | — |
| 49 | MiscPlnFlag | MISC_PLN_FLAG | — | ✅ |
| 50 | NoLngrEligFlag | NO_LNGR_ELIG_FLAG | — | ✅ |
| 51 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 52 | OiplId | OIPL_ID | — | — |
| 53 | OiplOrdrNum | OIPL_ORDR_NUM | — | ✅ |
| 54 | OptId | OPT_ID | — | — |
| 55 | OrgnlEnrtDt | ORGNL_ENRT_DT | — | ✅ |
| 56 | PenAttribute1 | PEN_ATTRIBUTE1 | — | — |
| 57 | PenAttribute10 | PEN_ATTRIBUTE10 | — | — |
| 58 | PenAttribute11 | PEN_ATTRIBUTE11 | — | — |
| 59 | PenAttribute12 | PEN_ATTRIBUTE12 | — | — |
| 60 | PenAttribute13 | PEN_ATTRIBUTE13 | — | — |
| 61 | PenAttribute14 | PEN_ATTRIBUTE14 | — | — |
| 62 | PenAttribute15 | PEN_ATTRIBUTE15 | — | — |
| 63 | PenAttribute16 | PEN_ATTRIBUTE16 | — | — |
| 64 | PenAttribute17 | PEN_ATTRIBUTE17 | — | — |
| 65 | PenAttribute18 | PEN_ATTRIBUTE18 | — | — |
| 66 | PenAttribute19 | PEN_ATTRIBUTE19 | — | — |
| 67 | PenAttribute2 | PEN_ATTRIBUTE2 | — | — |
| 68 | PenAttribute20 | PEN_ATTRIBUTE20 | — | — |
| 69 | PenAttribute21 | PEN_ATTRIBUTE21 | — | — |
| 70 | PenAttribute22 | PEN_ATTRIBUTE22 | — | — |
| 71 | PenAttribute23 | PEN_ATTRIBUTE23 | — | — |
| 72 | PenAttribute24 | PEN_ATTRIBUTE24 | — | — |
| 73 | PenAttribute25 | PEN_ATTRIBUTE25 | — | — |
| 74 | PenAttribute26 | PEN_ATTRIBUTE26 | — | — |
| 75 | PenAttribute27 | PEN_ATTRIBUTE27 | — | — |
| 76 | PenAttribute28 | PEN_ATTRIBUTE28 | — | — |
| 77 | PenAttribute29 | PEN_ATTRIBUTE29 | — | — |
| 78 | PenAttribute3 | PEN_ATTRIBUTE3 | — | — |
| 79 | PenAttribute30 | PEN_ATTRIBUTE30 | — | — |
| 80 | PenAttribute4 | PEN_ATTRIBUTE4 | — | — |
| 81 | PenAttribute5 | PEN_ATTRIBUTE5 | — | — |
| 82 | PenAttribute6 | PEN_ATTRIBUTE6 | — | — |
| 83 | PenAttribute7 | PEN_ATTRIBUTE7 | — | — |
| 84 | PenAttribute8 | PEN_ATTRIBUTE8 | — | — |
| 85 | PenAttribute9 | PEN_ATTRIBUTE9 | — | — |
| 86 | PenAttributeCategory | PEN_ATTRIBUTE_CATEGORY | — | — |
| 87 | PerInLerId | PER_IN_LER_ID | — | — |
| 88 | PersonId | PERSON_ID | — | ✅ |
| 89 | PgmId | PGM_ID | — | — |
| 90 | PlId | PL_ID | — | — |
| 91 | PlOrdrNum | PL_ORDR_NUM | — | ✅ |
| 92 | PlTypId | PL_TYP_ID | — | — |
| 93 | PlipOrdrNum | PLIP_ORDR_NUM | — | ✅ |
| 94 | ProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 95 | ProgramName | PROGRAM_NAME | — | ✅ |
| 96 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 97 | PrttEnrtRsltId | PRTT_ENRT_RSLT_ID | 🔑 | ✅ |
| 98 | PrttEnrtRsltStatCd | PRTT_ENRT_RSLT_STAT_CD | — | ✅ |
| 99 | PrttIsCvrdFlag | PRTT_IS_CVRD_FLAG | — | ✅ |
| 100 | PrvsCvgStrtDt | PRVS_CVG_STRT_DT | — | ✅ |
| 101 | PrvsCvgThruDt | PRVS_CVG_THRU_DT | — | ✅ |
| 102 | PrvsSspnddFlag | PRVS_SSPNDD_FLAG | — | ✅ |
| 103 | PtipId | PTIP_ID | — | — |
| 104 | PtipOrdrNum | PTIP_ORDR_NUM | — | — |
| 105 | RequestId | REQUEST_ID | — | — |
| 106 | RplcsSspnddRsltId | RPLCS_SSPNDD_RSLT_ID | — | — |
| 107 | SsCategoryCd | SS_CATEGORY_CD | — | — |
| 108 | SspnddFlag | SSPNDD_FLAG | — | ✅ |
| 109 | SvngsPlnFlag | SVNGS_PLN_FLAG | — | ✅ |
| 110 | TypeId | TYPE_ID | — | ✅ |
| 111 | Uom | UOM | — | ✅ |

### [[ben_prtt_rt_val|BEN_PRTT_RT_VAL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActlPremId | ACTL_PREM_ID | — | — |
| 2 | ActyBaseRtId | ACTY_BASE_RT_ID | — | — |
| 3 | ActyRefPerdCd | ACTY_REF_PERD_CD | — | ✅ |
| 4 | ActyTypCd | ACTY_TYP_CD | — | ✅ |
| 5 | AnnRtVal | ANN_RT_VAL | — | ✅ |
| 6 | BnftRtTypCd | BNFT_RT_TYP_CD | — | ✅ |
| 7 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 8 | CmcdRefPerdCd | CMCD_REF_PERD_CD | — | ✅ |
| 9 | CmcdRtVal | CMCD_RT_VAL | — | ✅ |
| 10 | CompLvlFctrId | COMP_LVL_FCTR_ID | — | — |
| 11 | CreatedBy1 | CREATED_BY | — | — |
| 12 | CreationDate1 | CREATION_DATE | — | — |
| 13 | CvgAmtCalcMthdId | CVG_AMT_CALC_MTHD_ID | — | — |
| 14 | DirCardCompDefId | DIR_CARD_COMP_DEF_ID | — | — |
| 15 | DirCardDefinitionId | DIR_CARD_DEFINITION_ID | — | — |
| 16 | DsplyOnEnrtFlag | DSPLY_ON_ENRT_FLAG | — | ✅ |
| 17 | ElctnsMadeDt | ELCTNS_MADE_DT | — | ✅ |
| 18 | ElementEntryValueId | ELEMENT_ENTRY_VALUE_ID | — | — |
| 19 | EndedPerInLerId1 | ENDED_PER_IN_LER_ID | — | — |
| 20 | EndedRateThruDt | ENDED_RATE_THRU_DT | — | ✅ |
| 21 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 22 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 23 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 24 | MappingId | MAPPING_ID | — | — |
| 25 | MltCd | MLT_CD | — | ✅ |
| 26 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 27 | OrdrNum | ORDR_NUM | — | ✅ |
| 28 | ParticipantEnrollmentRatePEOConfigChar1 | CONFIG_CHAR_1 | — | ✅ |
| 29 | ParticipantEnrollmentRatePEOTypeId | TYPE_ID | — | ✅ |
| 30 | PerInLerId1 | PER_IN_LER_ID | — | — |
| 31 | PkId | PK_ID | — | — |
| 32 | PkIdTableName | PK_ID_TABLE_NAME | — | — |
| 33 | PpInYrUsedNum | PP_IN_YR_USED_NUM | — | ✅ |
| 34 | PrttEnrtRsltId1 | PRTT_ENRT_RSLT_ID | — | — |
| 35 | PrttReimbmtRqstId | PRTT_REIMBMT_RQST_ID | — | — |
| 36 | PrttRmtAprvdFrPymtId | PRTT_RMT_APRVD_FR_PYMT_ID | — | — |
| 37 | PrttRtValId | PRTT_RT_VAL_ID | 🔑 | ✅ |
| 38 | PrttRtValStatCd | PRTT_RT_VAL_STAT_CD | — | ✅ |
| 39 | PrvAttribute1 | PRV_ATTRIBUTE1 | — | — |
| 40 | PrvAttribute10 | PRV_ATTRIBUTE10 | — | — |
| 41 | PrvAttribute11 | PRV_ATTRIBUTE11 | — | — |
| 42 | PrvAttribute12 | PRV_ATTRIBUTE12 | — | — |
| 43 | PrvAttribute13 | PRV_ATTRIBUTE13 | — | — |
| 44 | PrvAttribute14 | PRV_ATTRIBUTE14 | — | — |
| 45 | PrvAttribute15 | PRV_ATTRIBUTE15 | — | — |
| 46 | PrvAttribute16 | PRV_ATTRIBUTE16 | — | — |
| 47 | PrvAttribute17 | PRV_ATTRIBUTE17 | — | — |
| 48 | PrvAttribute18 | PRV_ATTRIBUTE18 | — | — |
| 49 | PrvAttribute19 | PRV_ATTRIBUTE19 | — | — |
| 50 | PrvAttribute2 | PRV_ATTRIBUTE2 | — | — |
| 51 | PrvAttribute20 | PRV_ATTRIBUTE20 | — | — |
| 52 | PrvAttribute21 | PRV_ATTRIBUTE21 | — | — |
| 53 | PrvAttribute22 | PRV_ATTRIBUTE22 | — | — |
| 54 | PrvAttribute23 | PRV_ATTRIBUTE23 | — | — |
| 55 | PrvAttribute24 | PRV_ATTRIBUTE24 | — | — |
| 56 | PrvAttribute25 | PRV_ATTRIBUTE25 | — | — |
| 57 | PrvAttribute26 | PRV_ATTRIBUTE26 | — | — |
| 58 | PrvAttribute27 | PRV_ATTRIBUTE27 | — | — |
| 59 | PrvAttribute28 | PRV_ATTRIBUTE28 | — | — |
| 60 | PrvAttribute29 | PRV_ATTRIBUTE29 | — | — |
| 61 | PrvAttribute3 | PRV_ATTRIBUTE3 | — | — |
| 62 | PrvAttribute30 | PRV_ATTRIBUTE30 | — | — |
| 63 | PrvAttribute4 | PRV_ATTRIBUTE4 | — | — |
| 64 | PrvAttribute5 | PRV_ATTRIBUTE5 | — | — |
| 65 | PrvAttribute6 | PRV_ATTRIBUTE6 | — | — |
| 66 | PrvAttribute7 | PRV_ATTRIBUTE7 | — | — |
| 67 | PrvAttribute8 | PRV_ATTRIBUTE8 | — | — |
| 68 | PrvAttribute9 | PRV_ATTRIBUTE9 | — | — |
| 69 | PrvAttributeCategory | PRV_ATTRIBUTE_CATEGORY | — | — |
| 70 | PrvConfigChar10 | CONFIG_CHAR_10 | — | — |
| 71 | PrvConfigChar6 | CONFIG_CHAR_6 | — | — |
| 72 | PrvConfigChar7 | CONFIG_CHAR_7 | — | — |
| 73 | PrvConfigChar8 | CONFIG_CHAR_8 | — | — |
| 74 | PrvConfigChar9 | CONFIG_CHAR_9 | — | — |
| 75 | PrvConfigId1 | CONFIG_ID_1 | — | — |
| 76 | PrvConfigId2 | CONFIG_ID_2 | — | — |
| 77 | PrvConfigId3 | CONFIG_ID_3 | — | — |
| 78 | PrvConfigId4 | CONFIG_ID_4 | — | — |
| 79 | PrvConfigId5 | CONFIG_ID_5 | — | — |
| 80 | PrvConfigNum10 | CONFIG_NUM_10 | — | — |
| 81 | PrvConfigNum6 | CONFIG_NUM_6 | — | — |
| 82 | PrvConfigNum7 | CONFIG_NUM_7 | — | — |
| 83 | PrvConfigNum8 | CONFIG_NUM_8 | — | — |
| 84 | PrvConfigNum9 | CONFIG_NUM_9 | — | — |
| 85 | PrvsRateStrtDt | PRVS_RATE_STRT_DT | — | ✅ |
| 86 | PrvsRateThruDt | PRVS_RATE_THRU_DT | — | ✅ |
| 87 | RateDisplayCd | RATE_DISPLAY_CD | — | ✅ |
| 88 | RcrrgFlag | RCRRG_FLAG | — | ✅ |
| 89 | RtEndDt | RT_END_DT | — | ✅ |
| 90 | RtOvridnFlag | RT_OVRIDN_FLAG | — | ✅ |
| 91 | RtOvridnThruDt | RT_OVRIDN_THRU_DT | — | ✅ |
| 92 | RtStrtDt | RT_STRT_DT | — | ✅ |
| 93 | RtTypCd | RT_TYP_CD | — | ✅ |
| 94 | RtVal | RT_VAL | — | ✅ |
| 95 | TxTypCd | TX_TYP_CD | — | ✅ |
| 96 | ValueDefinitionBaseName | VALUE_DEFINITION_BASE_NAME | — | — |
| 97 | VdefnDirCardCompDefId | VDEFN_DIR_CARD_COMP_DEF_ID | — | — |
| 98 | VdefnElementTypeId | VDEFN_ELEMENT_TYPE_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate4 | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate3 | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | PersonId1 | PERSON_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
