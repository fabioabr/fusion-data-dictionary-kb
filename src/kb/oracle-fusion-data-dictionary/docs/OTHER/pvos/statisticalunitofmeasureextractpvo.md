---
id: DOC-OTHER-PVO-StatisticalUnitOfMeasureExtractPVO
doc_type: system-doc
title: "StatisticalUnitOfMeasureExtractPVO — PVO Cross-Module"
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
  - StatisticalUnitOfMeasureExtractPVO
  - statisticalunitofmeasureextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StatisticalUnitOfMeasureExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Statistical Unit Of Measure Extract. Acessa as tabelas: GL_STAT_ACCOUNT_UOM.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.StatisticalUnitOfMeasureExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gl_stat_account_uom|GL_STAT_ACCOUNT_UOM]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[gl_stat_account_uom|GL_STAT_ACCOUNT_UOM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StatisticalUnitOfMeasureAccountSegmentValue | ACCOUNT_SEGMENT_VALUE | 🔑 | ✅ |
| 2 | StatisticalUnitOfMeasureChartOfAccountsId | CHART_OF_ACCOUNTS_ID | 🔑 | ✅ |
| 3 | StatisticalUnitOfMeasureCreatedBy | CREATED_BY | — | ✅ |
| 4 | StatisticalUnitOfMeasureCreationDate | CREATION_DATE | — | ✅ |
| 5 | StatisticalUnitOfMeasureDescription | DESCRIPTION | — | ✅ |
| 6 | StatisticalUnitOfMeasureLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | StatisticalUnitOfMeasureLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | StatisticalUnitOfMeasureLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | StatisticalUnitOfMeasureObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | StatisticalUnitOfMeasureUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
