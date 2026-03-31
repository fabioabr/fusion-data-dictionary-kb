---
id: DOC-OTHER-PVO-AccountingPeriodTypeExtractPVO
doc_type: system-doc
title: "AccountingPeriodTypeExtractPVO — PVO Cross-Module"
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
  - AccountingPeriodTypeExtractPVO
  - accountingperiodtypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AccountingPeriodTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Accounting Period Type Extract. Acessa as tabelas: GL_PERIOD_TYPES.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.AccountingPeriodTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gl_period_types|GL_PERIOD_TYPES]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[gl_period_types|GL_PERIOD_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlPeriodTypesCreatedBy | CREATED_BY | — | ✅ |
| 2 | GlPeriodTypesCreationDate | CREATION_DATE | — | ✅ |
| 3 | GlPeriodTypesDescription | DESCRIPTION | — | ✅ |
| 4 | GlPeriodTypesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | GlPeriodTypesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | GlPeriodTypesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | GlPeriodTypesNumberPerFiscalYear | NUMBER_PER_FISCAL_YEAR | — | ✅ |
| 8 | GlPeriodTypesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | GlPeriodTypesPeriodType | PERIOD_TYPE | 🔑 | ✅ |
| 10 | GlPeriodTypesPeriodTypeId | PERIOD_TYPE_ID | 🔑 | ✅ |
| 11 | GlPeriodTypesUserPeriodType | USER_PERIOD_TYPE | — | ✅ |
| 12 | GlPeriodTypesYearTypeInName | YEAR_TYPE_IN_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
