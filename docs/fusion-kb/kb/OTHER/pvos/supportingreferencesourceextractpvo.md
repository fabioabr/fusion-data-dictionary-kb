---
id: DOC-OTHER-PVO-SupportingReferenceSourceExtractPVO
doc_type: system-doc
title: "SupportingReferenceSourceExtractPVO — PVO Cross-Module"
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
  - SupportingReferenceSourceExtractPVO
  - supportingreferencesourceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupportingReferenceSourceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supporting Reference Source Extract. Acessa as tabelas: XLA_ANALYTICAL_SOURCES.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SupportingReferenceSourceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 7 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_analytical_sources|XLA_ANALYTICAL_SOURCES]] — 17 atributos (7 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[xla_analytical_sources|XLA_ANALYTICAL_SOURCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupportingReferenceSourceAmbContextCode | AMB_CONTEXT_CODE | — | ✅ |
| 2 | SupportingReferenceSourceAnalyticalDetailCode | ANALYTICAL_DETAIL_CODE | — | ✅ |
| 3 | SupportingReferenceSourceApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 4 | SupportingReferenceSourceCreatedBy | CREATED_BY | — | ✅ |
| 5 | SupportingReferenceSourceCreationDate | CREATION_DATE | — | ✅ |
| 6 | SupportingReferenceSourceEntityCode | ENTITY_CODE | 🔑 | ✅ |
| 7 | SupportingReferenceSourceEventClassCode | EVENT_CLASS_CODE | 🔑 | ✅ |
| 8 | SupportingReferenceSourceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | SupportingReferenceSourceLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | SupportingReferenceSourceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | SupportingReferenceSourceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | SupportingReferenceSourceSourceApplicationId | SOURCE_APPLICATION_ID | 🔑 | ✅ |
| 13 | SupportingReferenceSourceSourceCode | SOURCE_CODE | 🔑 | ✅ |
| 14 | SupportingReferenceSourceSourceOriginCode | SOURCE_ORIGIN_CODE | — | ✅ |
| 15 | SupportingReferenceSourceSourceTypeCode | SOURCE_TYPE_CODE | 🔑 | ✅ |
| 16 | SupportingReferenceSourceSupportingReferenceCode | ANALYTICAL_CRITERION_CODE | 🔑 | ✅ |
| 17 | SupportingReferenceSourceSupportingReferenceTypeCode | ANALYTICAL_CRITERION_TYPE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
