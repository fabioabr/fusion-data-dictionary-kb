---
id: DOC-HCM-PVO-AdminIndicatorPVO
doc_type: system-doc
title: "AdminIndicatorPVO — PVO Human Capital Management"
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
  - AdminIndicatorPVO
  - adminindicatorpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdminIndicatorPVO

## 📌 Visão Geral

Extrai indicadores administrativos do modulo Higher Education com codigo, nome e descricao. Utilizado para classificacao e monitoramento institucional.

**Caminho:** `FscmTopModelAM.HedHeyIndicatorAssignmentAM.AdminIndicatorPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 68 | 1 | 1 | 7 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[hey_admin_indicators_vl|HEY_ADMIN_INDICATORS_VL]] — 68 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[hey_admin_indicators_vl|HEY_ADMIN_INDICATORS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdminIndicatorPEOAcademicOrgId | ACADEMIC_ORG_ID | — | — |
| 2 | AdminIndicatorPEOActiveFlag | ACTIVE_FLAG | — | — |
| 3 | AdminIndicatorPEOAdminIndicatorCode | ADMIN_INDICATOR_CODE | — | ✅ |
| 4 | AdminIndicatorPEOAdminIndicatorId | ADMIN_INDICATOR_ID | 🔑 | ✅ |
| 5 | AdminIndicatorPEOAttribute1 | ATTRIBUTE1 | — | — |
| 6 | AdminIndicatorPEOAttribute10 | ATTRIBUTE10 | — | — |
| 7 | AdminIndicatorPEOAttribute11 | ATTRIBUTE11 | — | — |
| 8 | AdminIndicatorPEOAttribute12 | ATTRIBUTE12 | — | — |
| 9 | AdminIndicatorPEOAttribute13 | ATTRIBUTE13 | — | — |
| 10 | AdminIndicatorPEOAttribute14 | ATTRIBUTE14 | — | — |
| 11 | AdminIndicatorPEOAttribute15 | ATTRIBUTE15 | — | — |
| 12 | AdminIndicatorPEOAttribute16 | ATTRIBUTE16 | — | — |
| 13 | AdminIndicatorPEOAttribute17 | ATTRIBUTE17 | — | — |
| 14 | AdminIndicatorPEOAttribute18 | ATTRIBUTE18 | — | — |
| 15 | AdminIndicatorPEOAttribute19 | ATTRIBUTE19 | — | — |
| 16 | AdminIndicatorPEOAttribute2 | ATTRIBUTE2 | — | — |
| 17 | AdminIndicatorPEOAttribute20 | ATTRIBUTE20 | — | — |
| 18 | AdminIndicatorPEOAttribute3 | ATTRIBUTE3 | — | — |
| 19 | AdminIndicatorPEOAttribute4 | ATTRIBUTE4 | — | — |
| 20 | AdminIndicatorPEOAttribute5 | ATTRIBUTE5 | — | — |
| 21 | AdminIndicatorPEOAttribute6 | ATTRIBUTE6 | — | — |
| 22 | AdminIndicatorPEOAttribute7 | ATTRIBUTE7 | — | — |
| 23 | AdminIndicatorPEOAttribute8 | ATTRIBUTE8 | — | — |
| 24 | AdminIndicatorPEOAttribute9 | ATTRIBUTE9 | — | — |
| 25 | AdminIndicatorPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 26 | AdminIndicatorPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 27 | AdminIndicatorPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 28 | AdminIndicatorPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 29 | AdminIndicatorPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 30 | AdminIndicatorPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 31 | AdminIndicatorPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 32 | AdminIndicatorPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 33 | AdminIndicatorPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 34 | AdminIndicatorPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 35 | AdminIndicatorPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 36 | AdminIndicatorPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 37 | AdminIndicatorPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 38 | AdminIndicatorPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 39 | AdminIndicatorPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 40 | AdminIndicatorPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 41 | AdminIndicatorPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 42 | AdminIndicatorPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 43 | AdminIndicatorPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 44 | AdminIndicatorPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 45 | AdminIndicatorPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 46 | AdminIndicatorPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 47 | AdminIndicatorPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 48 | AdminIndicatorPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 49 | AdminIndicatorPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 50 | AdminIndicatorPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 51 | AdminIndicatorPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 52 | AdminIndicatorPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 53 | AdminIndicatorPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 54 | AdminIndicatorPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 55 | AdminIndicatorPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 56 | AdminIndicatorPEOCreatedBy | CREATED_BY | — | — |
| 57 | AdminIndicatorPEOCreationDate | CREATION_DATE | — | — |
| 58 | AdminIndicatorPEOEndDate | END_DATE | — | — |
| 59 | AdminIndicatorPEOIndicatorDescription | INDICATOR_DESCRIPTION | — | ✅ |
| 60 | AdminIndicatorPEOIndicatorName | INDICATOR_NAME | — | ✅ |
| 61 | AdminIndicatorPEOIndicatorTypeCode | INDICATOR_TYPE_CODE | — | ✅ |
| 62 | AdminIndicatorPEOInstitutionId | INSTITUTION_ID | — | — |
| 63 | AdminIndicatorPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 64 | AdminIndicatorPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 65 | AdminIndicatorPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 66 | AdminIndicatorPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 67 | AdminIndicatorPEOShowToRecipientFlag | SHOW_TO_RECIPIENT_FLAG | — | ✅ |
| 68 | AdminIndicatorPEOStartDate | START_DATE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
