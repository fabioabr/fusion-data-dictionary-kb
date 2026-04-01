---
id: DOC-OTHER-PVO-ProjectCostAllocExceptionsExtractPVO
doc_type: system-doc
title: "ProjectCostAllocExceptionsExtractPVO — PVO Cross-Module"
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
  - ProjectCostAllocExceptionsExtractPVO
  - projectcostallocexceptionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectCostAllocExceptionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Cost Alloc Exceptions Extract. Acessa as tabelas: PJC_ALLOC_EXCEPTIONS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.ProjectCostAllocExceptionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_alloc_exceptions|PJC_ALLOC_EXCEPTIONS]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[pjc_alloc_exceptions|PJC_ALLOC_EXCEPTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LaborScheduleCostDistErrorsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | LaborScheduleCostDistErrorsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | LaborScheduleCostDistErrorsPEOExceptionCode | EXCEPTION_CODE | — | ✅ |
| 4 | LaborScheduleCostDistErrorsPEOExceptionId | EXCEPTION_ID | 🔑 | ✅ |
| 5 | LaborScheduleCostDistErrorsPEOExceptionType | EXCEPTION_TYPE | — | ✅ |
| 6 | LaborScheduleCostDistErrorsPEOExpenditureItemId | EXPENDITURE_ITEM_ID | — | ✅ |
| 7 | LaborScheduleCostDistErrorsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LaborScheduleCostDistErrorsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LaborScheduleCostDistErrorsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | LaborScheduleCostDistErrorsPEOLevelCode | LEVEL_CODE | — | ✅ |
| 11 | LaborScheduleCostDistErrorsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | LaborScheduleCostDistErrorsPEOProjectId | PROJECT_ID | — | ✅ |
| 13 | LaborScheduleCostDistErrorsPEORuleId | RULE_ID | — | ✅ |
| 14 | LaborScheduleCostDistErrorsPEORunId | RUN_ID | — | ✅ |
| 15 | LaborScheduleCostDistErrorsPEORunTargetId | RUN_TARGET_ID | — | ✅ |
| 16 | LaborScheduleCostDistErrorsPEOTaskId | TASK_ID | — | ✅ |
| 17 | LaborScheduleCostDistErrorsPEOTokenName1 | TOKEN_NAME1 | — | ✅ |
| 18 | LaborScheduleCostDistErrorsPEOTokenName2 | TOKEN_NAME2 | — | ✅ |
| 19 | LaborScheduleCostDistErrorsPEOTokenName3 | TOKEN_NAME3 | — | ✅ |
| 20 | LaborScheduleCostDistErrorsPEOTokenValue1 | TOKEN_VALUE1 | — | ✅ |
| 21 | LaborScheduleCostDistErrorsPEOTokenValue2 | TOKEN_VALUE2 | — | ✅ |
| 22 | LaborScheduleCostDistErrorsPEOTokenValue3 | TOKEN_VALUE3 | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
