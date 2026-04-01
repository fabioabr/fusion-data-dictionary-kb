---
id: DOC-HCM-PVO-CourtOrderPVO
doc_type: system-doc
title: "CourtOrderPVO — PVO Human Capital Management"
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
  - CourtOrderPVO
  - courtorderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CourtOrderPVO

## 📌 Visão Geral

Extrai ordens judiciais relacionadas a beneficios com dependentes e planos. Suporta compliance legal e gestao de pensao alimenticia via folha.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.CourtOrderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 263 | 3 | 2 | 46 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[ben_crt_ordr_f|BEN_CRT_ORDR_F]] — 138 atributos (31 BICC)
- [[ben_crt_ordr_pl_dpnt|BEN_CRT_ORDR_PL_DPNT]] — 122 atributos (2 PKs, 15 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos

---

## ⚙️ Atributos

### [[ben_crt_ordr_f|BEN_CRT_ORDR_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressLine1 | ADDRESS_LINE_1 | — | ✅ |
| 2 | AddressLine2 | ADDRESS_LINE_2 | — | ✅ |
| 3 | AddressLine3 | ADDRESS_LINE_3 | — | ✅ |
| 4 | AddressLine4 | ADDRESS_LINE_4 | — | ✅ |
| 5 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | ✅ |
| 6 | City | CITY | — | ✅ |
| 7 | ConfigChar101 | CONFIG_CHAR_10 | — | — |
| 8 | ConfigChar11 | CONFIG_CHAR_1 | — | — |
| 9 | ConfigChar21 | CONFIG_CHAR_2 | — | — |
| 10 | ConfigChar31 | CONFIG_CHAR_3 | — | — |
| 11 | ConfigChar41 | CONFIG_CHAR_4 | — | — |
| 12 | ConfigChar51 | CONFIG_CHAR_5 | — | — |
| 13 | ConfigChar61 | CONFIG_CHAR_6 | — | — |
| 14 | ConfigChar71 | CONFIG_CHAR_7 | — | — |
| 15 | ConfigChar81 | CONFIG_CHAR_8 | — | — |
| 16 | ConfigChar91 | CONFIG_CHAR_9 | — | — |
| 17 | ConfigDate101 | CONFIG_DATE_10 | — | — |
| 18 | ConfigDate11 | CONFIG_DATE_1 | — | — |
| 19 | ConfigDate21 | CONFIG_DATE_2 | — | — |
| 20 | ConfigDate31 | CONFIG_DATE_3 | — | — |
| 21 | ConfigDate41 | CONFIG_DATE_4 | — | — |
| 22 | ConfigDate51 | CONFIG_DATE_5 | — | — |
| 23 | ConfigDate61 | CONFIG_DATE_6 | — | — |
| 24 | ConfigDate71 | CONFIG_DATE_7 | — | — |
| 25 | ConfigDate81 | CONFIG_DATE_8 | — | — |
| 26 | ConfigDate91 | CONFIG_DATE_9 | — | — |
| 27 | ConfigId101 | CONFIG_ID_10 | — | — |
| 28 | ConfigId11 | CONFIG_ID_1 | — | — |
| 29 | ConfigId21 | CONFIG_ID_2 | — | — |
| 30 | ConfigId31 | CONFIG_ID_3 | — | — |
| 31 | ConfigId41 | CONFIG_ID_4 | — | — |
| 32 | ConfigId51 | CONFIG_ID_5 | — | — |
| 33 | ConfigId61 | CONFIG_ID_6 | — | — |
| 34 | ConfigId71 | CONFIG_ID_7 | — | — |
| 35 | ConfigId81 | CONFIG_ID_8 | — | — |
| 36 | ConfigId91 | CONFIG_ID_9 | — | — |
| 37 | ConfigNum101 | CONFIG_NUM_10 | — | — |
| 38 | ConfigNum11 | CONFIG_NUM_1 | — | — |
| 39 | ConfigNum21 | CONFIG_NUM_2 | — | — |
| 40 | ConfigNum31 | CONFIG_NUM_3 | — | — |
| 41 | ConfigNum41 | CONFIG_NUM_4 | — | — |
| 42 | ConfigNum51 | CONFIG_NUM_5 | — | — |
| 43 | ConfigNum61 | CONFIG_NUM_6 | — | — |
| 44 | ConfigNum71 | CONFIG_NUM_7 | — | — |
| 45 | ConfigNum81 | CONFIG_NUM_8 | — | — |
| 46 | ConfigNum91 | CONFIG_NUM_9 | — | — |
| 47 | Country | COUNTRY | — | ✅ |
| 48 | CreatedBy1 | CREATED_BY | — | ✅ |
| 49 | CreationDate1 | CREATION_DATE | — | ✅ |
| 50 | CrtAttribute1 | CRT_ATTRIBUTE1 | — | — |
| 51 | CrtAttribute10 | CRT_ATTRIBUTE10 | — | — |
| 52 | CrtAttribute11 | CRT_ATTRIBUTE11 | — | — |
| 53 | CrtAttribute12 | CRT_ATTRIBUTE12 | — | — |
| 54 | CrtAttribute13 | CRT_ATTRIBUTE13 | — | — |
| 55 | CrtAttribute14 | CRT_ATTRIBUTE14 | — | — |
| 56 | CrtAttribute15 | CRT_ATTRIBUTE15 | — | — |
| 57 | CrtAttribute16 | CRT_ATTRIBUTE16 | — | — |
| 58 | CrtAttribute17 | CRT_ATTRIBUTE17 | — | — |
| 59 | CrtAttribute18 | CRT_ATTRIBUTE18 | — | — |
| 60 | CrtAttribute19 | CRT_ATTRIBUTE19 | — | — |
| 61 | CrtAttribute2 | CRT_ATTRIBUTE2 | — | — |
| 62 | CrtAttribute20 | CRT_ATTRIBUTE20 | — | — |
| 63 | CrtAttribute21 | CRT_ATTRIBUTE21 | — | — |
| 64 | CrtAttribute22 | CRT_ATTRIBUTE22 | — | — |
| 65 | CrtAttribute23 | CRT_ATTRIBUTE23 | — | — |
| 66 | CrtAttribute24 | CRT_ATTRIBUTE24 | — | — |
| 67 | CrtAttribute25 | CRT_ATTRIBUTE25 | — | — |
| 68 | CrtAttribute26 | CRT_ATTRIBUTE26 | — | — |
| 69 | CrtAttribute27 | CRT_ATTRIBUTE27 | — | — |
| 70 | CrtAttribute28 | CRT_ATTRIBUTE28 | — | — |
| 71 | CrtAttribute29 | CRT_ATTRIBUTE29 | — | — |
| 72 | CrtAttribute3 | CRT_ATTRIBUTE3 | — | — |
| 73 | CrtAttribute30 | CRT_ATTRIBUTE30 | — | — |
| 74 | CrtAttribute4 | CRT_ATTRIBUTE4 | — | — |
| 75 | CrtAttribute5 | CRT_ATTRIBUTE5 | — | — |
| 76 | CrtAttribute6 | CRT_ATTRIBUTE6 | — | — |
| 77 | CrtAttribute7 | CRT_ATTRIBUTE7 | — | — |
| 78 | CrtAttribute8 | CRT_ATTRIBUTE8 | — | — |
| 79 | CrtAttribute9 | CRT_ATTRIBUTE9 | — | — |
| 80 | CrtAttributeCategory | CRT_ATTRIBUTE_CATEGORY | — | — |
| 81 | CrtAttributeDate1 | CRT_ATTRIBUTE_DATE1 | — | — |
| 82 | CrtAttributeDate10 | CRT_ATTRIBUTE_DATE10 | — | — |
| 83 | CrtAttributeDate11 | CRT_ATTRIBUTE_DATE11 | — | — |
| 84 | CrtAttributeDate12 | CRT_ATTRIBUTE_DATE12 | — | — |
| 85 | CrtAttributeDate13 | CRT_ATTRIBUTE_DATE13 | — | — |
| 86 | CrtAttributeDate14 | CRT_ATTRIBUTE_DATE14 | — | — |
| 87 | CrtAttributeDate15 | CRT_ATTRIBUTE_DATE15 | — | — |
| 88 | CrtAttributeDate2 | CRT_ATTRIBUTE_DATE2 | — | — |
| 89 | CrtAttributeDate3 | CRT_ATTRIBUTE_DATE3 | — | — |
| 90 | CrtAttributeDate4 | CRT_ATTRIBUTE_DATE4 | — | — |
| 91 | CrtAttributeDate5 | CRT_ATTRIBUTE_DATE5 | — | — |
| 92 | CrtAttributeDate6 | CRT_ATTRIBUTE_DATE6 | — | — |
| 93 | CrtAttributeDate7 | CRT_ATTRIBUTE_DATE7 | — | — |
| 94 | CrtAttributeDate8 | CRT_ATTRIBUTE_DATE8 | — | — |
| 95 | CrtAttributeDate9 | CRT_ATTRIBUTE_DATE9 | — | — |
| 96 | CrtAttributeNumber1 | CRT_ATTRIBUTE_NUMBER1 | — | — |
| 97 | CrtAttributeNumber10 | CRT_ATTRIBUTE_NUMBER10 | — | — |
| 98 | CrtAttributeNumber11 | CRT_ATTRIBUTE_NUMBER11 | — | — |
| 99 | CrtAttributeNumber12 | CRT_ATTRIBUTE_NUMBER12 | — | — |
| 100 | CrtAttributeNumber13 | CRT_ATTRIBUTE_NUMBER13 | — | — |
| 101 | CrtAttributeNumber14 | CRT_ATTRIBUTE_NUMBER14 | — | — |
| 102 | CrtAttributeNumber15 | CRT_ATTRIBUTE_NUMBER15 | — | — |
| 103 | CrtAttributeNumber16 | CRT_ATTRIBUTE_NUMBER16 | — | — |
| 104 | CrtAttributeNumber17 | CRT_ATTRIBUTE_NUMBER17 | — | — |
| 105 | CrtAttributeNumber18 | CRT_ATTRIBUTE_NUMBER18 | — | — |
| 106 | CrtAttributeNumber19 | CRT_ATTRIBUTE_NUMBER19 | — | — |
| 107 | CrtAttributeNumber2 | CRT_ATTRIBUTE_NUMBER2 | — | — |
| 108 | CrtAttributeNumber20 | CRT_ATTRIBUTE_NUMBER20 | — | — |
| 109 | CrtAttributeNumber3 | CRT_ATTRIBUTE_NUMBER3 | — | — |
| 110 | CrtAttributeNumber4 | CRT_ATTRIBUTE_NUMBER4 | — | — |
| 111 | CrtAttributeNumber5 | CRT_ATTRIBUTE_NUMBER5 | — | — |
| 112 | CrtAttributeNumber6 | CRT_ATTRIBUTE_NUMBER6 | — | — |
| 113 | CrtAttributeNumber7 | CRT_ATTRIBUTE_NUMBER7 | — | — |
| 114 | CrtAttributeNumber8 | CRT_ATTRIBUTE_NUMBER8 | — | — |
| 115 | CrtAttributeNumber9 | CRT_ATTRIBUTE_NUMBER9 | — | — |
| 116 | CrtIdent | CRT_IDENT | — | ✅ |
| 117 | CrtIssng | CRT_ISSNG | — | ✅ |
| 118 | CrtOrdrId1 | CRT_ORDR_ID | — | ✅ |
| 119 | CrtOrdrStatCd | CRT_ORDR_STAT_CD | — | ✅ |
| 120 | CrtOrdrTypCd | CRT_ORDR_TYP_CD | — | ✅ |
| 121 | Description | DESCRIPTION | — | ✅ |
| 122 | DetdQlfdOrdrDt | DETD_QLFD_ORDR_DT | — | ✅ |
| 123 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 124 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 125 | EligibleDt | ELIGIBLE_DT | — | ✅ |
| 126 | IssueDt | ISSUE_DT | — | ✅ |
| 127 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 128 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 129 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 130 | Notes | NOTES | — | ✅ |
| 131 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 132 | OrdrEndDate1 | ORDR_END_DATE | — | ✅ |
| 133 | OrdrStartDate1 | ORDR_START_DATE | — | ✅ |
| 134 | PassdFinAssmnt | PASSD_FIN_ASSMNT | — | ✅ |
| 135 | PersonId | PERSON_ID | — | ✅ |
| 136 | PostalCode | POSTAL_CODE | — | ✅ |
| 137 | RcvdDt | RCVD_DT | — | ✅ |
| 138 | State | STATE | — | ✅ |

### [[ben_crt_ordr_pl_dpnt|BEN_CRT_ORDR_PL_DPNT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
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
| 22 | ConfigId1 | CONFIG_ID_1 | — | — |
| 23 | ConfigId10 | CONFIG_ID_10 | — | — |
| 24 | ConfigId2 | CONFIG_ID_2 | — | — |
| 25 | ConfigId3 | CONFIG_ID_3 | — | — |
| 26 | ConfigId4 | CONFIG_ID_4 | — | — |
| 27 | ConfigId5 | CONFIG_ID_5 | — | — |
| 28 | ConfigId6 | CONFIG_ID_6 | — | — |
| 29 | ConfigId7 | CONFIG_ID_7 | — | — |
| 30 | ConfigId8 | CONFIG_ID_8 | — | — |
| 31 | ConfigId9 | CONFIG_ID_9 | — | — |
| 32 | ConfigNum1 | CONFIG_NUM_1 | — | — |
| 33 | ConfigNum10 | CONFIG_NUM_10 | — | — |
| 34 | ConfigNum2 | CONFIG_NUM_2 | — | — |
| 35 | ConfigNum3 | CONFIG_NUM_3 | — | — |
| 36 | ConfigNum4 | CONFIG_NUM_4 | — | — |
| 37 | ConfigNum5 | CONFIG_NUM_5 | — | — |
| 38 | ConfigNum6 | CONFIG_NUM_6 | — | — |
| 39 | ConfigNum7 | CONFIG_NUM_7 | — | — |
| 40 | ConfigNum8 | CONFIG_NUM_8 | — | — |
| 41 | ConfigNum9 | CONFIG_NUM_9 | — | — |
| 42 | ContactPersonId | CONTACT_PERSON_ID | — | ✅ |
| 43 | CrdAttribute1 | CRD_ATTRIBUTE1 | — | — |
| 44 | CrdAttribute10 | CRD_ATTRIBUTE10 | — | — |
| 45 | CrdAttribute11 | CRD_ATTRIBUTE11 | — | — |
| 46 | CrdAttribute12 | CRD_ATTRIBUTE12 | — | — |
| 47 | CrdAttribute13 | CRD_ATTRIBUTE13 | — | — |
| 48 | CrdAttribute14 | CRD_ATTRIBUTE14 | — | — |
| 49 | CrdAttribute15 | CRD_ATTRIBUTE15 | — | — |
| 50 | CrdAttribute16 | CRD_ATTRIBUTE16 | — | — |
| 51 | CrdAttribute17 | CRD_ATTRIBUTE17 | — | — |
| 52 | CrdAttribute18 | CRD_ATTRIBUTE18 | — | — |
| 53 | CrdAttribute19 | CRD_ATTRIBUTE19 | — | — |
| 54 | CrdAttribute2 | CRD_ATTRIBUTE2 | — | — |
| 55 | CrdAttribute20 | CRD_ATTRIBUTE20 | — | — |
| 56 | CrdAttribute21 | CRD_ATTRIBUTE21 | — | — |
| 57 | CrdAttribute22 | CRD_ATTRIBUTE22 | — | — |
| 58 | CrdAttribute23 | CRD_ATTRIBUTE23 | — | — |
| 59 | CrdAttribute24 | CRD_ATTRIBUTE24 | — | — |
| 60 | CrdAttribute25 | CRD_ATTRIBUTE25 | — | — |
| 61 | CrdAttribute26 | CRD_ATTRIBUTE26 | — | — |
| 62 | CrdAttribute27 | CRD_ATTRIBUTE27 | — | — |
| 63 | CrdAttribute28 | CRD_ATTRIBUTE28 | — | — |
| 64 | CrdAttribute29 | CRD_ATTRIBUTE29 | — | — |
| 65 | CrdAttribute3 | CRD_ATTRIBUTE3 | — | — |
| 66 | CrdAttribute30 | CRD_ATTRIBUTE30 | — | — |
| 67 | CrdAttribute4 | CRD_ATTRIBUTE4 | — | — |
| 68 | CrdAttribute5 | CRD_ATTRIBUTE5 | — | — |
| 69 | CrdAttribute6 | CRD_ATTRIBUTE6 | — | — |
| 70 | CrdAttribute7 | CRD_ATTRIBUTE7 | — | — |
| 71 | CrdAttribute8 | CRD_ATTRIBUTE8 | — | — |
| 72 | CrdAttribute9 | CRD_ATTRIBUTE9 | — | — |
| 73 | CrdAttributeCategory | CRD_ATTRIBUTE_CATEGORY | — | — |
| 74 | CrdAttributeDate1 | CRD_ATTRIBUTE_DATE1 | — | — |
| 75 | CrdAttributeDate10 | CRD_ATTRIBUTE_DATE10 | — | — |
| 76 | CrdAttributeDate11 | CRD_ATTRIBUTE_DATE11 | — | — |
| 77 | CrdAttributeDate12 | CRD_ATTRIBUTE_DATE12 | — | — |
| 78 | CrdAttributeDate13 | CRD_ATTRIBUTE_DATE13 | — | — |
| 79 | CrdAttributeDate14 | CRD_ATTRIBUTE_DATE14 | — | — |
| 80 | CrdAttributeDate15 | CRD_ATTRIBUTE_DATE15 | — | — |
| 81 | CrdAttributeDate2 | CRD_ATTRIBUTE_DATE2 | — | — |
| 82 | CrdAttributeDate3 | CRD_ATTRIBUTE_DATE3 | — | — |
| 83 | CrdAttributeDate4 | CRD_ATTRIBUTE_DATE4 | — | — |
| 84 | CrdAttributeDate5 | CRD_ATTRIBUTE_DATE5 | — | — |
| 85 | CrdAttributeDate6 | CRD_ATTRIBUTE_DATE6 | — | — |
| 86 | CrdAttributeDate7 | CRD_ATTRIBUTE_DATE7 | — | — |
| 87 | CrdAttributeDate8 | CRD_ATTRIBUTE_DATE8 | — | — |
| 88 | CrdAttributeDate9 | CRD_ATTRIBUTE_DATE9 | — | — |
| 89 | CrdAttributeNumber1 | CRD_ATTRIBUTE_NUMBER1 | — | — |
| 90 | CrdAttributeNumber10 | CRD_ATTRIBUTE_NUMBER10 | — | — |
| 91 | CrdAttributeNumber11 | CRD_ATTRIBUTE_NUMBER11 | — | — |
| 92 | CrdAttributeNumber12 | CRD_ATTRIBUTE_NUMBER12 | — | — |
| 93 | CrdAttributeNumber13 | CRD_ATTRIBUTE_NUMBER13 | — | — |
| 94 | CrdAttributeNumber14 | CRD_ATTRIBUTE_NUMBER14 | — | — |
| 95 | CrdAttributeNumber15 | CRD_ATTRIBUTE_NUMBER15 | — | — |
| 96 | CrdAttributeNumber16 | CRD_ATTRIBUTE_NUMBER16 | — | — |
| 97 | CrdAttributeNumber17 | CRD_ATTRIBUTE_NUMBER17 | — | — |
| 98 | CrdAttributeNumber18 | CRD_ATTRIBUTE_NUMBER18 | — | — |
| 99 | CrdAttributeNumber19 | CRD_ATTRIBUTE_NUMBER19 | — | — |
| 100 | CrdAttributeNumber2 | CRD_ATTRIBUTE_NUMBER2 | — | — |
| 101 | CrdAttributeNumber20 | CRD_ATTRIBUTE_NUMBER20 | — | — |
| 102 | CrdAttributeNumber3 | CRD_ATTRIBUTE_NUMBER3 | — | — |
| 103 | CrdAttributeNumber4 | CRD_ATTRIBUTE_NUMBER4 | — | — |
| 104 | CrdAttributeNumber5 | CRD_ATTRIBUTE_NUMBER5 | — | — |
| 105 | CrdAttributeNumber6 | CRD_ATTRIBUTE_NUMBER6 | — | — |
| 106 | CrdAttributeNumber7 | CRD_ATTRIBUTE_NUMBER7 | — | — |
| 107 | CrdAttributeNumber8 | CRD_ATTRIBUTE_NUMBER8 | — | — |
| 108 | CrdAttributeNumber9 | CRD_ATTRIBUTE_NUMBER9 | — | — |
| 109 | CreatedBy | CREATED_BY | — | ✅ |
| 110 | CreationDate | CREATION_DATE | — | ✅ |
| 111 | CrtOrdrId | CRT_ORDR_ID | 🔑 | ✅ |
| 112 | CrtOrdrPlDpntId | CRT_ORDR_PL_DPNT_ID | 🔑 | ✅ |
| 113 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 114 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 115 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 116 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 117 | OrdrEndDate | ORDR_END_DATE | — | ✅ |
| 118 | OrdrStartDate | ORDR_START_DATE | — | ✅ |
| 119 | PlId | PL_ID | — | ✅ |
| 120 | PlTypId | PL_TYP_ID | — | ✅ |
| 121 | PrvntDeenrtFlag | PRVNT_DEENRT_FLAG | — | ✅ |
| 122 | RlshpTypCd | RLSHP_TYP_CD | — | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 3 | PersonId1 | PERSON_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
