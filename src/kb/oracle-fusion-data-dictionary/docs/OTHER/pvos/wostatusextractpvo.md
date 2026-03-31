---
id: DOC-OTHER-PVO-WOStatusExtractPVO
doc_type: system-doc
title: "WOStatusExtractPVO — PVO Cross-Module"
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
  - WOStatusExtractPVO
  - wostatusextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOStatusExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOStatus Extract. Acessa as tabelas: WIE_WO_STATUSES_B, WIE_WO_STATUSES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WieBiccExtractAM.WOStatusExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 63 | 2 | 1 | 63 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wie_wo_statuses_b|WIE_WO_STATUSES_B]] — 52 atributos (1 PKs, 52 BICC)
- [[wie_wo_statuses_tl|WIE_WO_STATUSES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[wie_wo_statuses_b|WIE_WO_STATUSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOStatusPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | WOStatusPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | WOStatusPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | WOStatusPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | WOStatusPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | WOStatusPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | WOStatusPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | WOStatusPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | WOStatusPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 10 | WOStatusPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 11 | WOStatusPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 12 | WOStatusPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 13 | WOStatusPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 14 | WOStatusPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 15 | WOStatusPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 16 | WOStatusPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 17 | WOStatusPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 18 | WOStatusPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 19 | WOStatusPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 20 | WOStatusPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 21 | WOStatusPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 22 | WOStatusPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 23 | WOStatusPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 24 | WOStatusPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 25 | WOStatusPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 26 | WOStatusPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 27 | WOStatusPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 28 | WOStatusPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 29 | WOStatusPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 30 | WOStatusPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | WOStatusPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 32 | WOStatusPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 33 | WOStatusPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 34 | WOStatusPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 35 | WOStatusPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 36 | WOStatusPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 37 | WOStatusPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 38 | WOStatusPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 39 | WOStatusPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 40 | WOStatusPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 41 | WOStatusPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 42 | WOStatusPEOCreatedBy | CREATED_BY | — | ✅ |
| 43 | WOStatusPEOCreationDate | CREATION_DATE | — | ✅ |
| 44 | WOStatusPEOInactiveDate | INACTIVE_DATE | — | ✅ |
| 45 | WOStatusPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | WOStatusPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 47 | WOStatusPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 48 | WOStatusPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 49 | WOStatusPEOSeededFlag | SEEDED_FLAG | — | ✅ |
| 50 | WOStatusPEOWoStatusCode | WO_STATUS_CODE | — | ✅ |
| 51 | WOStatusPEOWoStatusId | WO_STATUS_ID | 🔑 | ✅ |
| 52 | WOStatusPEOWoSystemStatusCode | WO_SYSTEM_STATUS_CODE | — | ✅ |

### [[wie_wo_statuses_tl|WIE_WO_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOStatusTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | WOStatusTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WOStatusTLPEOLanguage | LANGUAGE | — | ✅ |
| 4 | WOStatusTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | WOStatusTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | WOStatusTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | WOStatusTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | WOStatusTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 9 | WOStatusTLPEOWoStatusDescription | WO_STATUS_DESCRIPTION | — | ✅ |
| 10 | WOStatusTLPEOWoStatusId | WO_STATUS_ID | — | ✅ |
| 11 | WOStatusTLPEOWoStatusName | WO_STATUS_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
