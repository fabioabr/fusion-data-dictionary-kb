---
id: DOC-OTHER-PVO-FndLabelExtractPVO
doc_type: system-doc
title: "FndLabelExtractPVO — PVO Cross-Module"
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
  - FndLabelExtractPVO
  - fndlabelextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndLabelExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Label Extract. Acessa as tabelas: FND_LABEL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.FndLabelExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 3 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_label|FND_LABEL]] — 13 atributos (3 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[fnd_label|FND_LABEL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DataSourceId | DATA_SOURCE_ID | 🔑 | ✅ |
| 4 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 5 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | IconName | ICON_NAME | — | ✅ |
| 7 | LabelId | LABEL_ID | 🔑 | ✅ |
| 8 | LabelShortName | LABEL_SHORT_NAME | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | SetId | SET_ID | — | ✅ |
| 13 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
