---
id: DOC-HCM-PVO-CoveredBeneficiariesPVO
doc_type: system-doc
title: "CoveredBeneficiariesPVO — PVO Human Capital Management"
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
  - CoveredBeneficiariesPVO
  - coveredbeneficiariespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CoveredBeneficiariesPVO

## 📌 Visão Geral

Disponibiliza beneficiarios cobertos com life events e detalhes de plano. Essencial para gestao de cobertura e designacao de beneficiarios.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.CoveredBeneficiariesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 206 | 2 | 1 | 30 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[ben_per_in_ler|BEN_PER_IN_LER]] — 65 atributos (1 BICC)
- [[ben_pl_bnf|BEN_PL_BNF]] — 141 atributos (1 PKs, 29 BICC)

---

## ⚙️ Atributos

### [[ben_per_in_ler|BEN_PER_IN_LER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonLifeEventPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | PersonLifeEventPEOBcktDt | BCKT_DT | — | — |
| 3 | PersonLifeEventPEOBcktPerInLerId | BCKT_PER_IN_LER_ID | — | — |
| 4 | PersonLifeEventPEOBenefitRelationId | BENEFIT_RELATION_ID | — | — |
| 5 | PersonLifeEventPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | PersonLifeEventPEOClsdDt | CLSD_DT | — | — |
| 7 | PersonLifeEventPEOCreatedBy | CREATED_BY | — | — |
| 8 | PersonLifeEventPEOCreationDate | CREATION_DATE | — | — |
| 9 | PersonLifeEventPEOGroupPlId | GROUP_PL_ID | — | — |
| 10 | PersonLifeEventPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | PersonLifeEventPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | PersonLifeEventPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PersonLifeEventPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | PersonLifeEventPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | PersonLifeEventPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 16 | PersonLifeEventPEOLerId | LER_ID | — | — |
| 17 | PersonLifeEventPEOLerTypeCd | LER_TYPE_CD | — | — |
| 18 | PersonLifeEventPEOLfEvtOcrdDt | LF_EVT_OCRD_DT | — | — |
| 19 | PersonLifeEventPEONtfnDt | NTFN_DT | — | — |
| 20 | PersonLifeEventPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | PersonLifeEventPEOPerInLerId | PER_IN_LER_ID | — | — |
| 22 | PersonLifeEventPEOPerInLerStatCd | PER_IN_LER_STAT_CD | — | — |
| 23 | PersonLifeEventPEOPersonId | PERSON_ID | — | — |
| 24 | PersonLifeEventPEOPilAttribute1 | PIL_ATTRIBUTE1 | — | — |
| 25 | PersonLifeEventPEOPilAttribute10 | PIL_ATTRIBUTE10 | — | — |
| 26 | PersonLifeEventPEOPilAttribute11 | PIL_ATTRIBUTE11 | — | — |
| 27 | PersonLifeEventPEOPilAttribute12 | PIL_ATTRIBUTE12 | — | — |
| 28 | PersonLifeEventPEOPilAttribute13 | PIL_ATTRIBUTE13 | — | — |
| 29 | PersonLifeEventPEOPilAttribute14 | PIL_ATTRIBUTE14 | — | — |
| 30 | PersonLifeEventPEOPilAttribute15 | PIL_ATTRIBUTE15 | — | — |
| 31 | PersonLifeEventPEOPilAttribute16 | PIL_ATTRIBUTE16 | — | — |
| 32 | PersonLifeEventPEOPilAttribute17 | PIL_ATTRIBUTE17 | — | — |
| 33 | PersonLifeEventPEOPilAttribute18 | PIL_ATTRIBUTE18 | — | — |
| 34 | PersonLifeEventPEOPilAttribute19 | PIL_ATTRIBUTE19 | — | — |
| 35 | PersonLifeEventPEOPilAttribute2 | PIL_ATTRIBUTE2 | — | — |
| 36 | PersonLifeEventPEOPilAttribute20 | PIL_ATTRIBUTE20 | — | — |
| 37 | PersonLifeEventPEOPilAttribute21 | PIL_ATTRIBUTE21 | — | — |
| 38 | PersonLifeEventPEOPilAttribute22 | PIL_ATTRIBUTE22 | — | — |
| 39 | PersonLifeEventPEOPilAttribute23 | PIL_ATTRIBUTE23 | — | — |
| 40 | PersonLifeEventPEOPilAttribute24 | PIL_ATTRIBUTE24 | — | — |
| 41 | PersonLifeEventPEOPilAttribute25 | PIL_ATTRIBUTE25 | — | — |
| 42 | PersonLifeEventPEOPilAttribute26 | PIL_ATTRIBUTE26 | — | — |
| 43 | PersonLifeEventPEOPilAttribute27 | PIL_ATTRIBUTE27 | — | — |
| 44 | PersonLifeEventPEOPilAttribute28 | PIL_ATTRIBUTE28 | — | — |
| 45 | PersonLifeEventPEOPilAttribute29 | PIL_ATTRIBUTE29 | — | — |
| 46 | PersonLifeEventPEOPilAttribute3 | PIL_ATTRIBUTE3 | — | — |
| 47 | PersonLifeEventPEOPilAttribute30 | PIL_ATTRIBUTE30 | — | — |
| 48 | PersonLifeEventPEOPilAttribute4 | PIL_ATTRIBUTE4 | — | — |
| 49 | PersonLifeEventPEOPilAttribute5 | PIL_ATTRIBUTE5 | — | — |
| 50 | PersonLifeEventPEOPilAttribute6 | PIL_ATTRIBUTE6 | — | — |
| 51 | PersonLifeEventPEOPilAttribute7 | PIL_ATTRIBUTE7 | — | — |
| 52 | PersonLifeEventPEOPilAttribute8 | PIL_ATTRIBUTE8 | — | — |
| 53 | PersonLifeEventPEOPilAttribute9 | PIL_ATTRIBUTE9 | — | — |
| 54 | PersonLifeEventPEOPilAttributeCategory | PIL_ATTRIBUTE_CATEGORY | — | — |
| 55 | PersonLifeEventPEOProcdDt | PROCD_DT | — | — |
| 56 | PersonLifeEventPEOProdCd | PROD_CD | — | — |
| 57 | PersonLifeEventPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 58 | PersonLifeEventPEOProgramName | PROGRAM_NAME | — | — |
| 59 | PersonLifeEventPEOProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 60 | PersonLifeEventPEOPrvsStatCd | PRVS_STAT_CD | — | — |
| 61 | PersonLifeEventPEOPtnlLerForPerId | PTNL_LER_FOR_PER_ID | — | — |
| 62 | PersonLifeEventPEORequestId | REQUEST_ID | — | — |
| 63 | PersonLifeEventPEOStrtdDt | STRTD_DT | — | — |
| 64 | PersonLifeEventPEOTrgrTablePkId | TRGR_TABLE_PK_ID | — | — |
| 65 | PersonLifeEventPEOVoiddDt | VOIDD_DT | — | — |

### [[ben_pl_bnf|BEN_PL_BNF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BnfOvrd | BNF_OVRD | — | — |
| 2 | ConfigChar1 | CONFIG_CHAR_1 | — | — |
| 3 | ConfigChar10 | CONFIG_CHAR_10 | — | — |
| 4 | ConfigChar2 | CONFIG_CHAR_2 | — | — |
| 5 | ConfigChar3 | CONFIG_CHAR_3 | — | — |
| 6 | ConfigChar4 | CONFIG_CHAR_4 | — | — |
| 7 | ConfigChar5 | CONFIG_CHAR_5 | — | — |
| 8 | ConfigChar6 | CONFIG_CHAR_6 | — | — |
| 9 | ConfigChar7 | CONFIG_CHAR_7 | — | — |
| 10 | ConfigChar8 | CONFIG_CHAR_8 | — | — |
| 11 | ConfigChar9 | CONFIG_CHAR_9 | — | — |
| 12 | ConfigDate1 | CONFIG_DATE_1 | — | — |
| 13 | ConfigDate10 | CONFIG_DATE_10 | — | — |
| 14 | ConfigDate2 | CONFIG_DATE_2 | — | — |
| 15 | ConfigDate3 | CONFIG_DATE_3 | — | — |
| 16 | ConfigDate4 | CONFIG_DATE_4 | — | — |
| 17 | ConfigDate5 | CONFIG_DATE_5 | — | — |
| 18 | ConfigDate6 | CONFIG_DATE_6 | — | — |
| 19 | ConfigDate7 | CONFIG_DATE_7 | — | — |
| 20 | ConfigDate8 | CONFIG_DATE_8 | — | — |
| 21 | ConfigDate9 | CONFIG_DATE_9 | — | — |
| 22 | ConfigNum1 | CONFIG_NUM_1 | — | — |
| 23 | ConfigNum10 | CONFIG_NUM_10 | — | — |
| 24 | ConfigNum2 | CONFIG_NUM_2 | — | — |
| 25 | ConfigNum3 | CONFIG_NUM_3 | — | — |
| 26 | ConfigNum4 | CONFIG_NUM_4 | — | — |
| 27 | ConfigNum5 | CONFIG_NUM_5 | — | — |
| 28 | ConfigNum6 | CONFIG_NUM_6 | — | — |
| 29 | ConfigNum7 | CONFIG_NUM_7 | — | — |
| 30 | ConfigNum8 | CONFIG_NUM_8 | — | — |
| 31 | ConfigNum9 | CONFIG_NUM_9 | — | — |
| 32 | CoveredBeneficiariesPEOAddlInstrnTxt | ADDL_INSTRN_TXT | — | ✅ |
| 33 | CoveredBeneficiariesPEOAmtDsgdUom | AMT_DSGD_UOM | — | ✅ |
| 34 | CoveredBeneficiariesPEOAmtDsgdVal | AMT_DSGD_VAL | — | ✅ |
| 35 | CoveredBeneficiariesPEOBnfPersonId | BNF_PERSON_ID | — | ✅ |
| 36 | CoveredBeneficiariesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 37 | CoveredBeneficiariesPEOCntngtBnfsAlwdFlag | CNTNGT_BNFS_ALWD_FLAG | — | ✅ |
| 38 | CoveredBeneficiariesPEOCreatedBy | CREATED_BY | — | ✅ |
| 39 | CoveredBeneficiariesPEOCreationDate | CREATION_DATE | — | ✅ |
| 40 | CoveredBeneficiariesPEOCtfnReqdFlag | CTFN_REQD_FLAG | — | — |
| 41 | CoveredBeneficiariesPEOCvrdAmt | CVRD_AMT | — | ✅ |
| 42 | CoveredBeneficiariesPEOCvrdCntngtAmt | CVRD_CNTNGT_AMT | — | ✅ |
| 43 | CoveredBeneficiariesPEOCvrdCntngtPercentage | CVRD_CNTNGT_PERCENTAGE | — | ✅ |
| 44 | CoveredBeneficiariesPEOCvrdFlag | CVRD_FLAG | — | ✅ |
| 45 | CoveredBeneficiariesPEOCvrdPercentage | CVRD_PERCENTAGE | — | ✅ |
| 46 | CoveredBeneficiariesPEOCvrdPrmryCntngntCd | CVRD_PRMRY_CNTNGNT_CD | — | ✅ |
| 47 | CoveredBeneficiariesPEODsgnStrtDt | DSGN_STRT_DT | — | ✅ |
| 48 | CoveredBeneficiariesPEODsgnThruDt | DSGN_THRU_DT | — | ✅ |
| 49 | CoveredBeneficiariesPEOEligPerElctblChcId | ELIG_PER_ELCTBL_CHC_ID | — | — |
| 50 | CoveredBeneficiariesPEOEndedCvgThruDt | ENDED_CVG_THRU_DT | — | ✅ |
| 51 | CoveredBeneficiariesPEOEndedPerInLerId | ENDED_PER_IN_LER_ID | — | — |
| 52 | CoveredBeneficiariesPEOEnrtBnftId | ENRT_BNFT_ID | — | — |
| 53 | CoveredBeneficiariesPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 54 | CoveredBeneficiariesPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 55 | CoveredBeneficiariesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 56 | CoveredBeneficiariesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 57 | CoveredBeneficiariesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 58 | CoveredBeneficiariesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 59 | CoveredBeneficiariesPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 60 | CoveredBeneficiariesPEOOrgnlOiplDsgnStrtDt | ORGNL_OIPL_DSGN_STRT_DT | — | — |
| 61 | CoveredBeneficiariesPEOOrgnlPlanDsgnStrtDt | ORGNL_PLAN_DSGN_STRT_DT | — | — |
| 62 | CoveredBeneficiariesPEOPbnAttribute1 | PBN_ATTRIBUTE1 | — | — |
| 63 | CoveredBeneficiariesPEOPbnAttribute10 | PBN_ATTRIBUTE10 | — | — |
| 64 | CoveredBeneficiariesPEOPbnAttribute11 | PBN_ATTRIBUTE11 | — | — |
| 65 | CoveredBeneficiariesPEOPbnAttribute12 | PBN_ATTRIBUTE12 | — | — |
| 66 | CoveredBeneficiariesPEOPbnAttribute13 | PBN_ATTRIBUTE13 | — | — |
| 67 | CoveredBeneficiariesPEOPbnAttribute14 | PBN_ATTRIBUTE14 | — | — |
| 68 | CoveredBeneficiariesPEOPbnAttribute15 | PBN_ATTRIBUTE15 | — | — |
| 69 | CoveredBeneficiariesPEOPbnAttribute16 | PBN_ATTRIBUTE16 | — | — |
| 70 | CoveredBeneficiariesPEOPbnAttribute17 | PBN_ATTRIBUTE17 | — | — |
| 71 | CoveredBeneficiariesPEOPbnAttribute18 | PBN_ATTRIBUTE18 | — | — |
| 72 | CoveredBeneficiariesPEOPbnAttribute19 | PBN_ATTRIBUTE19 | — | — |
| 73 | CoveredBeneficiariesPEOPbnAttribute2 | PBN_ATTRIBUTE2 | — | — |
| 74 | CoveredBeneficiariesPEOPbnAttribute20 | PBN_ATTRIBUTE20 | — | — |
| 75 | CoveredBeneficiariesPEOPbnAttribute21 | PBN_ATTRIBUTE21 | — | — |
| 76 | CoveredBeneficiariesPEOPbnAttribute22 | PBN_ATTRIBUTE22 | — | — |
| 77 | CoveredBeneficiariesPEOPbnAttribute23 | PBN_ATTRIBUTE23 | — | — |
| 78 | CoveredBeneficiariesPEOPbnAttribute24 | PBN_ATTRIBUTE24 | — | — |
| 79 | CoveredBeneficiariesPEOPbnAttribute25 | PBN_ATTRIBUTE25 | — | — |
| 80 | CoveredBeneficiariesPEOPbnAttribute26 | PBN_ATTRIBUTE26 | — | — |
| 81 | CoveredBeneficiariesPEOPbnAttribute27 | PBN_ATTRIBUTE27 | — | — |
| 82 | CoveredBeneficiariesPEOPbnAttribute28 | PBN_ATTRIBUTE28 | — | — |
| 83 | CoveredBeneficiariesPEOPbnAttribute29 | PBN_ATTRIBUTE29 | — | — |
| 84 | CoveredBeneficiariesPEOPbnAttribute3 | PBN_ATTRIBUTE3 | — | — |
| 85 | CoveredBeneficiariesPEOPbnAttribute30 | PBN_ATTRIBUTE30 | — | — |
| 86 | CoveredBeneficiariesPEOPbnAttribute4 | PBN_ATTRIBUTE4 | — | — |
| 87 | CoveredBeneficiariesPEOPbnAttribute5 | PBN_ATTRIBUTE5 | — | — |
| 88 | CoveredBeneficiariesPEOPbnAttribute6 | PBN_ATTRIBUTE6 | — | — |
| 89 | CoveredBeneficiariesPEOPbnAttribute7 | PBN_ATTRIBUTE7 | — | — |
| 90 | CoveredBeneficiariesPEOPbnAttribute8 | PBN_ATTRIBUTE8 | — | — |
| 91 | CoveredBeneficiariesPEOPbnAttribute9 | PBN_ATTRIBUTE9 | — | — |
| 92 | CoveredBeneficiariesPEOPbnAttributeCategory | PBN_ATTRIBUTE_CATEGORY | — | — |
| 93 | CoveredBeneficiariesPEOPbnAttributeDate1 | PBN_ATTRIBUTE_DATE1 | — | — |
| 94 | CoveredBeneficiariesPEOPbnAttributeDate10 | PBN_ATTRIBUTE_DATE10 | — | — |
| 95 | CoveredBeneficiariesPEOPbnAttributeDate11 | PBN_ATTRIBUTE_DATE11 | — | — |
| 96 | CoveredBeneficiariesPEOPbnAttributeDate12 | PBN_ATTRIBUTE_DATE12 | — | — |
| 97 | CoveredBeneficiariesPEOPbnAttributeDate13 | PBN_ATTRIBUTE_DATE13 | — | — |
| 98 | CoveredBeneficiariesPEOPbnAttributeDate14 | PBN_ATTRIBUTE_DATE14 | — | — |
| 99 | CoveredBeneficiariesPEOPbnAttributeDate15 | PBN_ATTRIBUTE_DATE15 | — | — |
| 100 | CoveredBeneficiariesPEOPbnAttributeDate2 | PBN_ATTRIBUTE_DATE2 | — | — |
| 101 | CoveredBeneficiariesPEOPbnAttributeDate3 | PBN_ATTRIBUTE_DATE3 | — | — |
| 102 | CoveredBeneficiariesPEOPbnAttributeDate4 | PBN_ATTRIBUTE_DATE4 | — | — |
| 103 | CoveredBeneficiariesPEOPbnAttributeDate5 | PBN_ATTRIBUTE_DATE5 | — | — |
| 104 | CoveredBeneficiariesPEOPbnAttributeDate6 | PBN_ATTRIBUTE_DATE6 | — | — |
| 105 | CoveredBeneficiariesPEOPbnAttributeDate7 | PBN_ATTRIBUTE_DATE7 | — | — |
| 106 | CoveredBeneficiariesPEOPbnAttributeDate8 | PBN_ATTRIBUTE_DATE8 | — | — |
| 107 | CoveredBeneficiariesPEOPbnAttributeDate9 | PBN_ATTRIBUTE_DATE9 | — | — |
| 108 | CoveredBeneficiariesPEOPbnAttributeNumber1 | PBN_ATTRIBUTE_NUMBER1 | — | — |
| 109 | CoveredBeneficiariesPEOPbnAttributeNumber10 | PBN_ATTRIBUTE_NUMBER10 | — | — |
| 110 | CoveredBeneficiariesPEOPbnAttributeNumber11 | PBN_ATTRIBUTE_NUMBER11 | — | — |
| 111 | CoveredBeneficiariesPEOPbnAttributeNumber12 | PBN_ATTRIBUTE_NUMBER12 | — | — |
| 112 | CoveredBeneficiariesPEOPbnAttributeNumber13 | PBN_ATTRIBUTE_NUMBER13 | — | — |
| 113 | CoveredBeneficiariesPEOPbnAttributeNumber14 | PBN_ATTRIBUTE_NUMBER14 | — | — |
| 114 | CoveredBeneficiariesPEOPbnAttributeNumber15 | PBN_ATTRIBUTE_NUMBER15 | — | — |
| 115 | CoveredBeneficiariesPEOPbnAttributeNumber16 | PBN_ATTRIBUTE_NUMBER16 | — | — |
| 116 | CoveredBeneficiariesPEOPbnAttributeNumber17 | PBN_ATTRIBUTE_NUMBER17 | — | — |
| 117 | CoveredBeneficiariesPEOPbnAttributeNumber18 | PBN_ATTRIBUTE_NUMBER18 | — | — |
| 118 | CoveredBeneficiariesPEOPbnAttributeNumber19 | PBN_ATTRIBUTE_NUMBER19 | — | — |
| 119 | CoveredBeneficiariesPEOPbnAttributeNumber2 | PBN_ATTRIBUTE_NUMBER2 | — | — |
| 120 | CoveredBeneficiariesPEOPbnAttributeNumber20 | PBN_ATTRIBUTE_NUMBER20 | — | — |
| 121 | CoveredBeneficiariesPEOPbnAttributeNumber3 | PBN_ATTRIBUTE_NUMBER3 | — | — |
| 122 | CoveredBeneficiariesPEOPbnAttributeNumber4 | PBN_ATTRIBUTE_NUMBER4 | — | — |
| 123 | CoveredBeneficiariesPEOPbnAttributeNumber5 | PBN_ATTRIBUTE_NUMBER5 | — | — |
| 124 | CoveredBeneficiariesPEOPbnAttributeNumber6 | PBN_ATTRIBUTE_NUMBER6 | — | — |
| 125 | CoveredBeneficiariesPEOPbnAttributeNumber7 | PBN_ATTRIBUTE_NUMBER7 | — | — |
| 126 | CoveredBeneficiariesPEOPbnAttributeNumber8 | PBN_ATTRIBUTE_NUMBER8 | — | — |
| 127 | CoveredBeneficiariesPEOPbnAttributeNumber9 | PBN_ATTRIBUTE_NUMBER9 | — | — |
| 128 | CoveredBeneficiariesPEOPctDsgdNum | PCT_DSGD_NUM | — | ✅ |
| 129 | CoveredBeneficiariesPEOPerInLerId | PER_IN_LER_ID | — | — |
| 130 | CoveredBeneficiariesPEOPlBnfId | PL_BNF_ID | 🔑 | ✅ |
| 131 | CoveredBeneficiariesPEOPrmryCntngntCd | PRMRY_CNTNGNT_CD | — | ✅ |
| 132 | CoveredBeneficiariesPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 133 | CoveredBeneficiariesPEOProgramName | PROGRAM_NAME | — | — |
| 134 | CoveredBeneficiariesPEOProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 135 | CoveredBeneficiariesPEOPrttEnrtRsltId | PRTT_ENRT_RSLT_ID | — | ✅ |
| 136 | CoveredBeneficiariesPEOPrvsCvgStrtDt | PRVS_CVG_STRT_DT | — | ✅ |
| 137 | CoveredBeneficiariesPEOPrvsCvgThruDt | PRVS_CVG_THRU_DT | — | ✅ |
| 138 | CoveredBeneficiariesPEORequestId | REQUEST_ID | — | — |
| 139 | CoveredBeneficiariesPEORlnshpCd | RLNSHP_CD | — | ✅ |
| 140 | CoveredBeneficiariesPEOSuspendFlag | SUSPEND_FLAG | — | ✅ |
| 141 | CoveredBeneficiariesPEOTteePersonId | TTEE_PERSON_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
