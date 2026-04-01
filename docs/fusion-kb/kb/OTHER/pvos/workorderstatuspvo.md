---
id: DOC-OTHER-PVO-WorkOrderStatusPVO
doc_type: system-doc
title: "WorkOrderStatusPVO — PVO Cross-Module"
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
  - WorkOrderStatusPVO
  - workorderstatuspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkOrderStatusPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Order Status. Acessa as tabelas: WIE_WO_STATUSES_B, WIE_WO_STATUSES_TL.

**Caminho:** `FscmTopModelAM.WorkOrderAM.WorkOrderStatusPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 1 | 14 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[wie_wo_statuses_b|WIE_WO_STATUSES_B]] — 11 atributos (1 PKs, 7 BICC)
- [[wie_wo_statuses_tl|WIE_WO_STATUSES_TL]] — 11 atributos (7 BICC)

---

## ⚙️ Atributos

### [[wie_wo_statuses_b|WIE_WO_STATUSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderStatusPEOCreatedBy | CREATED_BY | — | — |
| 2 | WorkOrderStatusPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WorkOrderStatusPEOInactiveDate | INACTIVE_DATE | — | ✅ |
| 4 | WorkOrderStatusPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | WorkOrderStatusPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | WorkOrderStatusPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | WorkOrderStatusPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | WorkOrderStatusPEOSeededFlag | SEEDED_FLAG | — | ✅ |
| 9 | WorkOrderStatusPEOWoStatusCode | WO_STATUS_CODE | — | ✅ |
| 10 | WorkOrderStatusPEOWoStatusId | WO_STATUS_ID | 🔑 | ✅ |
| 11 | WorkOrderStatusPEOWoSystemStatusCode | WO_SYSTEM_STATUS_CODE | — | ✅ |

### [[wie_wo_statuses_tl|WIE_WO_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderStatusTranslationPEOCreatedBy1 | CREATED_BY | — | — |
| 2 | WorkOrderStatusTranslationPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 3 | WorkOrderStatusTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 4 | WorkOrderStatusTranslationPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 5 | WorkOrderStatusTranslationPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 6 | WorkOrderStatusTranslationPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 7 | WorkOrderStatusTranslationPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 8 | WorkOrderStatusTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 9 | WorkOrderStatusTranslationPEOWoStatusDescription | WO_STATUS_DESCRIPTION | — | ✅ |
| 10 | WorkOrderStatusTranslationPEOWoStatusId1 | WO_STATUS_ID | — | ✅ |
| 11 | WorkOrderStatusTranslationPEOWoStatusName | WO_STATUS_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
