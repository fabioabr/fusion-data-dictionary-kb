---
id: DOC-OTHER-PVO-PrimaryCareProviderPVO
doc_type: system-doc
title: "PrimaryCareProviderPVO — PVO Cross-Module"
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
  - PrimaryCareProviderPVO
  - primarycareproviderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PrimaryCareProviderPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Primary Care Provider. Acessa as tabelas: BEN_PRMRY_CARE_PRVDR.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.PrimaryCareProviderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 92 | 1 | 1 | 19 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[ben_prmry_care_prvdr|BEN_PRMRY_CARE_PRVDR]] — 92 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[ben_prmry_care_prvdr|BEN_PRMRY_CARE_PRVDR]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | CvgStrtDt | CVG_STRT_DT | — | ✅ |
| 5 | CvgThruDt | CVG_THRU_DT | — | ✅ |
| 6 | CvrdFlag | CVRD_FLAG | — | ✅ |
| 7 | EligCvrdDpntId | ELIG_CVRD_DPNT_ID | — | ✅ |
| 8 | EligDpntId | ELIG_DPNT_ID | — | ✅ |
| 9 | EligPerElctblChcId | ELIG_PER_ELCTBL_CHC_ID | — | ✅ |
| 10 | EndedCvgThruDt | ENDED_CVG_THRU_DT | — | ✅ |
| 11 | EndedPerInLerId | ENDED_PER_IN_LER_ID | — | ✅ |
| 12 | ExtIdent | EXT_IDENT | — | ✅ |
| 13 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 14 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | Name | NAME | — | ✅ |
| 19 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | PprAttribute1 | PPR_ATTRIBUTE1 | — | — |
| 21 | PprAttribute10 | PPR_ATTRIBUTE10 | — | — |
| 22 | PprAttribute11 | PPR_ATTRIBUTE11 | — | — |
| 23 | PprAttribute12 | PPR_ATTRIBUTE12 | — | — |
| 24 | PprAttribute13 | PPR_ATTRIBUTE13 | — | — |
| 25 | PprAttribute14 | PPR_ATTRIBUTE14 | — | — |
| 26 | PprAttribute15 | PPR_ATTRIBUTE15 | — | — |
| 27 | PprAttribute16 | PPR_ATTRIBUTE16 | — | — |
| 28 | PprAttribute17 | PPR_ATTRIBUTE17 | — | — |
| 29 | PprAttribute18 | PPR_ATTRIBUTE18 | — | — |
| 30 | PprAttribute19 | PPR_ATTRIBUTE19 | — | — |
| 31 | PprAttribute2 | PPR_ATTRIBUTE2 | — | — |
| 32 | PprAttribute20 | PPR_ATTRIBUTE20 | — | — |
| 33 | PprAttribute21 | PPR_ATTRIBUTE21 | — | — |
| 34 | PprAttribute22 | PPR_ATTRIBUTE22 | — | — |
| 35 | PprAttribute23 | PPR_ATTRIBUTE23 | — | — |
| 36 | PprAttribute24 | PPR_ATTRIBUTE24 | — | — |
| 37 | PprAttribute25 | PPR_ATTRIBUTE25 | — | — |
| 38 | PprAttribute26 | PPR_ATTRIBUTE26 | — | — |
| 39 | PprAttribute27 | PPR_ATTRIBUTE27 | — | — |
| 40 | PprAttribute28 | PPR_ATTRIBUTE28 | — | — |
| 41 | PprAttribute29 | PPR_ATTRIBUTE29 | — | — |
| 42 | PprAttribute3 | PPR_ATTRIBUTE3 | — | — |
| 43 | PprAttribute30 | PPR_ATTRIBUTE30 | — | — |
| 44 | PprAttribute4 | PPR_ATTRIBUTE4 | — | — |
| 45 | PprAttribute5 | PPR_ATTRIBUTE5 | — | — |
| 46 | PprAttribute6 | PPR_ATTRIBUTE6 | — | — |
| 47 | PprAttribute7 | PPR_ATTRIBUTE7 | — | — |
| 48 | PprAttribute8 | PPR_ATTRIBUTE8 | — | — |
| 49 | PprAttribute9 | PPR_ATTRIBUTE9 | — | — |
| 50 | PprAttributeCategory | PPR_ATTRIBUTE_CATEGORY | — | — |
| 51 | PprAttributeDate1 | PPR_ATTRIBUTE_DATE1 | — | — |
| 52 | PprAttributeDate10 | PPR_ATTRIBUTE_DATE10 | — | — |
| 53 | PprAttributeDate11 | PPR_ATTRIBUTE_DATE11 | — | — |
| 54 | PprAttributeDate12 | PPR_ATTRIBUTE_DATE12 | — | — |
| 55 | PprAttributeDate13 | PPR_ATTRIBUTE_DATE13 | — | — |
| 56 | PprAttributeDate14 | PPR_ATTRIBUTE_DATE14 | — | — |
| 57 | PprAttributeDate15 | PPR_ATTRIBUTE_DATE15 | — | — |
| 58 | PprAttributeDate2 | PPR_ATTRIBUTE_DATE2 | — | — |
| 59 | PprAttributeDate3 | PPR_ATTRIBUTE_DATE3 | — | — |
| 60 | PprAttributeDate4 | PPR_ATTRIBUTE_DATE4 | — | — |
| 61 | PprAttributeDate5 | PPR_ATTRIBUTE_DATE5 | — | — |
| 62 | PprAttributeDate6 | PPR_ATTRIBUTE_DATE6 | — | — |
| 63 | PprAttributeDate7 | PPR_ATTRIBUTE_DATE7 | — | — |
| 64 | PprAttributeDate8 | PPR_ATTRIBUTE_DATE8 | — | — |
| 65 | PprAttributeDate9 | PPR_ATTRIBUTE_DATE9 | — | — |
| 66 | PprAttributeNumber1 | PPR_ATTRIBUTE_NUMBER1 | — | — |
| 67 | PprAttributeNumber10 | PPR_ATTRIBUTE_NUMBER10 | — | — |
| 68 | PprAttributeNumber11 | PPR_ATTRIBUTE_NUMBER11 | — | — |
| 69 | PprAttributeNumber12 | PPR_ATTRIBUTE_NUMBER12 | — | — |
| 70 | PprAttributeNumber13 | PPR_ATTRIBUTE_NUMBER13 | — | — |
| 71 | PprAttributeNumber14 | PPR_ATTRIBUTE_NUMBER14 | — | — |
| 72 | PprAttributeNumber15 | PPR_ATTRIBUTE_NUMBER15 | — | — |
| 73 | PprAttributeNumber16 | PPR_ATTRIBUTE_NUMBER16 | — | — |
| 74 | PprAttributeNumber17 | PPR_ATTRIBUTE_NUMBER17 | — | — |
| 75 | PprAttributeNumber18 | PPR_ATTRIBUTE_NUMBER18 | — | — |
| 76 | PprAttributeNumber19 | PPR_ATTRIBUTE_NUMBER19 | — | — |
| 77 | PprAttributeNumber2 | PPR_ATTRIBUTE_NUMBER2 | — | — |
| 78 | PprAttributeNumber20 | PPR_ATTRIBUTE_NUMBER20 | — | — |
| 79 | PprAttributeNumber3 | PPR_ATTRIBUTE_NUMBER3 | — | — |
| 80 | PprAttributeNumber4 | PPR_ATTRIBUTE_NUMBER4 | — | — |
| 81 | PprAttributeNumber5 | PPR_ATTRIBUTE_NUMBER5 | — | — |
| 82 | PprAttributeNumber6 | PPR_ATTRIBUTE_NUMBER6 | — | — |
| 83 | PprAttributeNumber7 | PPR_ATTRIBUTE_NUMBER7 | — | — |
| 84 | PprAttributeNumber8 | PPR_ATTRIBUTE_NUMBER8 | — | — |
| 85 | PprAttributeNumber9 | PPR_ATTRIBUTE_NUMBER9 | — | — |
| 86 | PrmryCarePrvdrId | PRMRY_CARE_PRVDR_ID | 🔑 | ✅ |
| 87 | PrmryCarePrvdrTypCd | PRMRY_CARE_PRVDR_TYP_CD | — | ✅ |
| 88 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 89 | PrttEnrtRsltId | PRTT_ENRT_RSLT_ID | — | ✅ |
| 90 | PrvsCvgStrtDt | PRVS_CVG_STRT_DT | — | — |
| 91 | PrvsCvgThruDt | PRVS_CVG_THRU_DT | — | — |
| 92 | RequestId | REQUEST_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
