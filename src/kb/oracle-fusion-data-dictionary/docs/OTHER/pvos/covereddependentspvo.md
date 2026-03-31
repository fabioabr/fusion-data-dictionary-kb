---
id: DOC-OTHER-PVO-CoveredDependentsPVO
doc_type: system-doc
title: "CoveredDependentsPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CoveredDependentsPVO
  - covereddependentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CoveredDependentsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Covered Dependents. Acessa as tabelas: BEN_ELIG_CVRD_DPNT, BEN_PER_IN_LER.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.CoveredDependentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 161 | 2 | 1 | 17 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[ben_elig_cvrd_dpnt|BEN_ELIG_CVRD_DPNT]] — 96 atributos (1 PKs, 15 BICC)
- [[ben_per_in_ler|BEN_PER_IN_LER]] — 65 atributos (2 BICC)

---

## ⚙️ Atributos

### [[ben_elig_cvrd_dpnt|BEN_ELIG_CVRD_DPNT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CoveredDependentsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CoveredDependentsPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | CoveredDependentsPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | CoveredDependentsPEOCvgPndgFlag | CVG_PNDG_FLAG | — | ✅ |
| 5 | CoveredDependentsPEOCvgStrtDt | CVG_STRT_DT | — | ✅ |
| 6 | CoveredDependentsPEOCvgThruDt | CVG_THRU_DT | — | ✅ |
| 7 | CoveredDependentsPEODpntPersonId | DPNT_PERSON_ID | — | — |
| 8 | CoveredDependentsPEOEligCvrdDpntId | ELIG_CVRD_DPNT_ID | 🔑 | ✅ |
| 9 | CoveredDependentsPEOEligPerElctblChcId | ELIG_PER_ELCTBL_CHC_ID | — | — |
| 10 | CoveredDependentsPEOEndedCvgThruDt | ENDED_CVG_THRU_DT | — | ✅ |
| 11 | CoveredDependentsPEOEndedPerInLerId | ENDED_PER_IN_LER_ID | — | — |
| 12 | CoveredDependentsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 13 | CoveredDependentsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 14 | CoveredDependentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | CoveredDependentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | CoveredDependentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | CoveredDependentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | CoveredDependentsPEOOrgnlOiplCvgStrtDt | ORGNL_OIPL_CVG_STRT_DT | — | ✅ |
| 19 | CoveredDependentsPEOOrgnlPlanCvgStrtDt | ORGNL_PLAN_CVG_STRT_DT | — | ✅ |
| 20 | CoveredDependentsPEOOvrdnFlag | OVRDN_FLAG | — | ✅ |
| 21 | CoveredDependentsPEOOvrdnThruDt | OVRDN_THRU_DT | — | ✅ |
| 22 | CoveredDependentsPEOPdpAttribute1 | PDP_ATTRIBUTE1 | — | — |
| 23 | CoveredDependentsPEOPdpAttribute10 | PDP_ATTRIBUTE10 | — | — |
| 24 | CoveredDependentsPEOPdpAttribute11 | PDP_ATTRIBUTE11 | — | — |
| 25 | CoveredDependentsPEOPdpAttribute12 | PDP_ATTRIBUTE12 | — | — |
| 26 | CoveredDependentsPEOPdpAttribute13 | PDP_ATTRIBUTE13 | — | — |
| 27 | CoveredDependentsPEOPdpAttribute14 | PDP_ATTRIBUTE14 | — | — |
| 28 | CoveredDependentsPEOPdpAttribute15 | PDP_ATTRIBUTE15 | — | — |
| 29 | CoveredDependentsPEOPdpAttribute16 | PDP_ATTRIBUTE16 | — | — |
| 30 | CoveredDependentsPEOPdpAttribute17 | PDP_ATTRIBUTE17 | — | — |
| 31 | CoveredDependentsPEOPdpAttribute18 | PDP_ATTRIBUTE18 | — | — |
| 32 | CoveredDependentsPEOPdpAttribute19 | PDP_ATTRIBUTE19 | — | — |
| 33 | CoveredDependentsPEOPdpAttribute2 | PDP_ATTRIBUTE2 | — | — |
| 34 | CoveredDependentsPEOPdpAttribute20 | PDP_ATTRIBUTE20 | — | — |
| 35 | CoveredDependentsPEOPdpAttribute21 | PDP_ATTRIBUTE21 | — | — |
| 36 | CoveredDependentsPEOPdpAttribute22 | PDP_ATTRIBUTE22 | — | — |
| 37 | CoveredDependentsPEOPdpAttribute23 | PDP_ATTRIBUTE23 | — | — |
| 38 | CoveredDependentsPEOPdpAttribute24 | PDP_ATTRIBUTE24 | — | — |
| 39 | CoveredDependentsPEOPdpAttribute25 | PDP_ATTRIBUTE25 | — | — |
| 40 | CoveredDependentsPEOPdpAttribute26 | PDP_ATTRIBUTE26 | — | — |
| 41 | CoveredDependentsPEOPdpAttribute27 | PDP_ATTRIBUTE27 | — | — |
| 42 | CoveredDependentsPEOPdpAttribute28 | PDP_ATTRIBUTE28 | — | — |
| 43 | CoveredDependentsPEOPdpAttribute29 | PDP_ATTRIBUTE29 | — | — |
| 44 | CoveredDependentsPEOPdpAttribute3 | PDP_ATTRIBUTE3 | — | — |
| 45 | CoveredDependentsPEOPdpAttribute30 | PDP_ATTRIBUTE30 | — | — |
| 46 | CoveredDependentsPEOPdpAttribute4 | PDP_ATTRIBUTE4 | — | — |
| 47 | CoveredDependentsPEOPdpAttribute5 | PDP_ATTRIBUTE5 | — | — |
| 48 | CoveredDependentsPEOPdpAttribute6 | PDP_ATTRIBUTE6 | — | — |
| 49 | CoveredDependentsPEOPdpAttribute7 | PDP_ATTRIBUTE7 | — | — |
| 50 | CoveredDependentsPEOPdpAttribute8 | PDP_ATTRIBUTE8 | — | — |
| 51 | CoveredDependentsPEOPdpAttribute9 | PDP_ATTRIBUTE9 | — | — |
| 52 | CoveredDependentsPEOPdpAttributeCategory | PDP_ATTRIBUTE_CATEGORY | — | — |
| 53 | CoveredDependentsPEOPdpAttributeDate1 | PDP_ATTRIBUTE_DATE1 | — | — |
| 54 | CoveredDependentsPEOPdpAttributeDate10 | PDP_ATTRIBUTE_DATE10 | — | — |
| 55 | CoveredDependentsPEOPdpAttributeDate11 | PDP_ATTRIBUTE_DATE11 | — | — |
| 56 | CoveredDependentsPEOPdpAttributeDate12 | PDP_ATTRIBUTE_DATE12 | — | — |
| 57 | CoveredDependentsPEOPdpAttributeDate13 | PDP_ATTRIBUTE_DATE13 | — | — |
| 58 | CoveredDependentsPEOPdpAttributeDate14 | PDP_ATTRIBUTE_DATE14 | — | — |
| 59 | CoveredDependentsPEOPdpAttributeDate15 | PDP_ATTRIBUTE_DATE15 | — | — |
| 60 | CoveredDependentsPEOPdpAttributeDate2 | PDP_ATTRIBUTE_DATE2 | — | — |
| 61 | CoveredDependentsPEOPdpAttributeDate3 | PDP_ATTRIBUTE_DATE3 | — | — |
| 62 | CoveredDependentsPEOPdpAttributeDate4 | PDP_ATTRIBUTE_DATE4 | — | — |
| 63 | CoveredDependentsPEOPdpAttributeDate5 | PDP_ATTRIBUTE_DATE5 | — | — |
| 64 | CoveredDependentsPEOPdpAttributeDate6 | PDP_ATTRIBUTE_DATE6 | — | — |
| 65 | CoveredDependentsPEOPdpAttributeDate7 | PDP_ATTRIBUTE_DATE7 | — | — |
| 66 | CoveredDependentsPEOPdpAttributeDate8 | PDP_ATTRIBUTE_DATE8 | — | — |
| 67 | CoveredDependentsPEOPdpAttributeDate9 | PDP_ATTRIBUTE_DATE9 | — | — |
| 68 | CoveredDependentsPEOPdpAttributeNumber1 | PDP_ATTRIBUTE_NUMBER1 | — | — |
| 69 | CoveredDependentsPEOPdpAttributeNumber10 | PDP_ATTRIBUTE_NUMBER10 | — | — |
| 70 | CoveredDependentsPEOPdpAttributeNumber11 | PDP_ATTRIBUTE_NUMBER11 | — | — |
| 71 | CoveredDependentsPEOPdpAttributeNumber12 | PDP_ATTRIBUTE_NUMBER12 | — | — |
| 72 | CoveredDependentsPEOPdpAttributeNumber13 | PDP_ATTRIBUTE_NUMBER13 | — | — |
| 73 | CoveredDependentsPEOPdpAttributeNumber14 | PDP_ATTRIBUTE_NUMBER14 | — | — |
| 74 | CoveredDependentsPEOPdpAttributeNumber15 | PDP_ATTRIBUTE_NUMBER15 | — | — |
| 75 | CoveredDependentsPEOPdpAttributeNumber16 | PDP_ATTRIBUTE_NUMBER16 | — | — |
| 76 | CoveredDependentsPEOPdpAttributeNumber17 | PDP_ATTRIBUTE_NUMBER17 | — | — |
| 77 | CoveredDependentsPEOPdpAttributeNumber18 | PDP_ATTRIBUTE_NUMBER18 | — | — |
| 78 | CoveredDependentsPEOPdpAttributeNumber19 | PDP_ATTRIBUTE_NUMBER19 | — | — |
| 79 | CoveredDependentsPEOPdpAttributeNumber2 | PDP_ATTRIBUTE_NUMBER2 | — | — |
| 80 | CoveredDependentsPEOPdpAttributeNumber20 | PDP_ATTRIBUTE_NUMBER20 | — | — |
| 81 | CoveredDependentsPEOPdpAttributeNumber3 | PDP_ATTRIBUTE_NUMBER3 | — | — |
| 82 | CoveredDependentsPEOPdpAttributeNumber4 | PDP_ATTRIBUTE_NUMBER4 | — | — |
| 83 | CoveredDependentsPEOPdpAttributeNumber5 | PDP_ATTRIBUTE_NUMBER5 | — | — |
| 84 | CoveredDependentsPEOPdpAttributeNumber6 | PDP_ATTRIBUTE_NUMBER6 | — | — |
| 85 | CoveredDependentsPEOPdpAttributeNumber7 | PDP_ATTRIBUTE_NUMBER7 | — | — |
| 86 | CoveredDependentsPEOPdpAttributeNumber8 | PDP_ATTRIBUTE_NUMBER8 | — | — |
| 87 | CoveredDependentsPEOPdpAttributeNumber9 | PDP_ATTRIBUTE_NUMBER9 | — | — |
| 88 | CoveredDependentsPEOPerInLerId | PER_IN_LER_ID | — | — |
| 89 | CoveredDependentsPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 90 | CoveredDependentsPEOProgramName | PROGRAM_NAME | — | — |
| 91 | CoveredDependentsPEOProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 92 | CoveredDependentsPEOPrttEnrtRsltId | PRTT_ENRT_RSLT_ID | — | — |
| 93 | CoveredDependentsPEOPrvsCvgStrtDt | PRVS_CVG_STRT_DT | — | — |
| 94 | CoveredDependentsPEOPrvsCvgThruDt | PRVS_CVG_THRU_DT | — | — |
| 95 | CoveredDependentsPEORequestId | REQUEST_ID | — | — |
| 96 | CoveredDependentsPEORlnshpCd | RLNSHP_CD | — | ✅ |

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
| 8 | PersonLifeEventPEOCreationDate1 | CREATION_DATE | — | — |
| 9 | PersonLifeEventPEOGroupPlId | GROUP_PL_ID | — | — |
| 10 | PersonLifeEventPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | PersonLifeEventPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | PersonLifeEventPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 13 | PersonLifeEventPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | PersonLifeEventPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 15 | PersonLifeEventPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 16 | PersonLifeEventPEOLerId | LER_ID | — | ✅ |
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

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
