---
id: DOC-OTHER-PVO-SupportingReferencePVO
doc_type: system-doc
title: "SupportingReferencePVO — PVO Cross-Module"
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
  - SupportingReferencePVO
  - supportingreferencepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupportingReferencePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supporting Reference. Acessa as tabelas: XLA_ANALYTICAL_HDRS_B, XLA_ANALYTICAL_HDRS_TL, XLA_SUBLEDGERS_VL.

**Caminho:** `FscmTopModelAM.FinXlaAmsSuppRefAM.SupportingReferencePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 3 | 3 | 3 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[xla_analytical_hdrs_b|XLA_ANALYTICAL_HDRS_B]] — 17 atributos (3 PKs, 3 BICC)
- [[xla_analytical_hdrs_tl|XLA_ANALYTICAL_HDRS_TL]] — 13 atributos
- [[xla_subledgers_vl|XLA_SUBLEDGERS_VL]] — 7 atributos

---

## ⚙️ Atributos

### [[xla_analytical_hdrs_b|XLA_ANALYTICAL_HDRS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AmbContextCode | AMB_CONTEXT_CODE | 🔑 | ✅ |
| 2 | AnalyticalCriterionCode | ANALYTICAL_CRITERION_CODE | 🔑 | ✅ |
| 3 | AnalyticalCriterionTypeCode | ANALYTICAL_CRITERION_TYPE_CODE | 🔑 | ✅ |
| 4 | SupportingRefApplicationId | APPLICATION_ID | — | — |
| 5 | SupportingRefBalancingFlag | BALANCING_FLAG | — | — |
| 6 | SupportingRefCreatedBy | CREATED_BY | — | — |
| 7 | SupportingRefCreationDate | CREATION_DATE | — | — |
| 8 | SupportingRefDisplayOrder | DISPLAY_ORDER | — | — |
| 9 | SupportingRefEnabledFlag | ENABLED_FLAG | — | — |
| 10 | SupportingRefLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 11 | SupportingRefLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | SupportingRefLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | SupportingRefObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | SupportingRefSuppRefOrder | SUPP_REF_ORDER | — | — |
| 15 | SupportingRefUpdatedFlag | UPDATED_FLAG | — | — |
| 16 | SupportingRefVersionNum | VERSION_NUM | — | — |
| 17 | SupportingRefYearEndCarryForwardCode | YEAR_END_CARRY_FORWARD_CODE | — | — |

### [[xla_analytical_hdrs_tl|XLA_ANALYTICAL_HDRS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupportingRefTranslatedAmbContextCode | AMB_CONTEXT_CODE | — | — |
| 2 | SupportingRefTranslatedAnalyticalCriterionCode | ANALYTICAL_CRITERION_CODE | — | — |
| 3 | SupportingRefTranslatedAnalyticalCriterionTypeCode | ANALYTICAL_CRITERION_TYPE_CODE | — | — |
| 4 | SupportingRefTranslatedCreatedBy | CREATED_BY | — | — |
| 5 | SupportingRefTranslatedCreationDate | CREATION_DATE | — | — |
| 6 | SupportingRefTranslatedDescription | DESCRIPTION | — | — |
| 7 | SupportingRefTranslatedLanguage | LANGUAGE | — | — |
| 8 | SupportingRefTranslatedLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | SupportingRefTranslatedLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | SupportingRefTranslatedLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | SupportingRefTranslatedName | NAME | — | — |
| 12 | SupportingRefTranslatedObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | SupportingRefTranslatedSourceLang | SOURCE_LANG | — | — |

### [[xla_subledgers_vl|XLA_SUBLEDGERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | XlaApplnVLApplicationId | APPLICATION_ID | — | — |
| 2 | XlaApplnVLApplicationName | APPLICATION_NAME | — | — |
| 3 | XlaApplnVLApplicationShortName | APPLICATION_SHORT_NAME | — | — |
| 4 | XlaApplnVLDescription | DESCRIPTION | — | — |
| 5 | XlaApplnVLDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | — |
| 6 | XlaApplnVLJeSourceName | JE_SOURCE_NAME | — | — |
| 7 | XlaApplnVLSecurityFunctionName | SECURITY_FUNCTION_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
