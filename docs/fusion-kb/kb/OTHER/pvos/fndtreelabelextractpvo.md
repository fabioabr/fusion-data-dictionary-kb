---
id: DOC-OTHER-PVO-FndTreeLabelExtractPVO
doc_type: system-doc
title: "FndTreeLabelExtractPVO — PVO Cross-Module"
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
  - FndTreeLabelExtractPVO
  - fndtreelabelextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndTreeLabelExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Tree Label Extract. Acessa as tabelas: FND_TREE_LABEL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.FndTreeLabelExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 4 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_tree_label|FND_TREE_LABEL]] — 15 atributos (4 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[fnd_tree_label|FND_TREE_LABEL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DataSourceId | DATA_SOURCE_ID | 🔑 | ✅ |
| 4 | LabelPk1Value | LABEL_PK1_VALUE | — | ✅ |
| 5 | LabelPk2Value | LABEL_PK2_VALUE | — | ✅ |
| 6 | LabelPk3Value | LABEL_PK3_VALUE | — | ✅ |
| 7 | LabelPk4Value | LABEL_PK4_VALUE | — | ✅ |
| 8 | LabelPk5Value | LABEL_PK5_VALUE | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | SortOrder | SORT_ORDER | — | ✅ |
| 13 | TreeCode | TREE_CODE | 🔑 | ✅ |
| 14 | TreeLabelId | TREE_LABEL_ID | 🔑 | ✅ |
| 15 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
