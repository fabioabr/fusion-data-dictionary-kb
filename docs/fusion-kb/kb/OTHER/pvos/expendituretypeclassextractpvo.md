---
id: DOC-OTHER-PVO-ExpenditureTypeClassExtractPVO
doc_type: system-doc
title: "ExpenditureTypeClassExtractPVO — PVO Cross-Module"
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
  - ExpenditureTypeClassExtractPVO
  - expendituretypeclassextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenditureTypeClassExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expenditure Type Class Extract. Acessa as tabelas: PJF_SYSTEM_LINKAGES_B, PJF_SYSTEM_LINKAGES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ExpenditureTypeClassExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 2 | 1 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_system_linkages_b|PJF_SYSTEM_LINKAGES_B]] — 12 atributos (1 PKs, 12 BICC)
- [[pjf_system_linkages_tl|PJF_SYSTEM_LINKAGES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_system_linkages_b|PJF_SYSTEM_LINKAGES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeClassBasePEOCcFunctionTransactionCode | CC_FUNCTION_TRANSACTION_CODE | — | ✅ |
| 2 | ExpenditureTypeClassBasePEOCostCreditFunctionCode | COST_CREDIT_FUNCTION_CODE | — | ✅ |
| 3 | ExpenditureTypeClassBasePEOCostDebitFunctionCode | COST_DEBIT_FUNCTION_CODE | — | ✅ |
| 4 | ExpenditureTypeClassBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | ExpenditureTypeClassBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | ExpenditureTypeClassBasePEOFunction1 | FUNCTION | 🔑 | ✅ |
| 7 | ExpenditureTypeClassBasePEOLaborNonLaborFlag | LABOR_NON_LABOR_FLAG | — | ✅ |
| 8 | ExpenditureTypeClassBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ExpenditureTypeClassBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | ExpenditureTypeClassBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ExpenditureTypeClassBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ExpenditureTypeClassBasePEOProjectManufacturingFlag | PROJECT_MANUFACTURING_FLAG | — | ✅ |

### [[pjf_system_linkages_tl|PJF_SYSTEM_LINKAGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeClassTransPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ExpenditureTypeClassTransPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ExpenditureTypeClassTransPEODescription | DESCRIPTION | — | ✅ |
| 4 | ExpenditureTypeClassTransPEOFunction1 | FUNCTION | — | ✅ |
| 5 | ExpenditureTypeClassTransPEOLanguage | LANGUAGE | — | ✅ |
| 6 | ExpenditureTypeClassTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ExpenditureTypeClassTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ExpenditureTypeClassTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ExpenditureTypeClassTransPEOMeaning | MEANING | — | ✅ |
| 10 | ExpenditureTypeClassTransPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ExpenditureTypeClassTransPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
