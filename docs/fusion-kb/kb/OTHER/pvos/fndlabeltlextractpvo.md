---
id: DOC-OTHER-PVO-FndLabelTLExtractPVO
doc_type: system-doc
title: "FndLabelTLExtractPVO — PVO Cross-Module"
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
  - FndLabelTLExtractPVO
  - fndlabeltlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndLabelTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Label TLExtract. Acessa as tabelas: FND_LABEL_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.FndLabelTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 4 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_label_tl|FND_LABEL_TL]] — 12 atributos (4 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[fnd_label_tl|FND_LABEL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DataSourceId | DATA_SOURCE_ID | 🔑 | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | LabelId | LABEL_ID | 🔑 | ✅ |
| 6 | LabelName | LABEL_NAME | — | ✅ |
| 7 | Language | LANGUAGE | 🔑 | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |
| 12 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
