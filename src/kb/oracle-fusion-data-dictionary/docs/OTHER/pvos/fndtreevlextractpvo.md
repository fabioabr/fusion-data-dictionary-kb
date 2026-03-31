---
id: DOC-OTHER-PVO-FndTreeVLExtractPVO
doc_type: system-doc
title: "FndTreeVLExtractPVO — PVO Cross-Module"
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
  - FndTreeVLExtractPVO
  - fndtreevlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndTreeVLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Tree VLExtract. Acessa as tabelas: FND_TREE_VL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.FndTreeVLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_tree_vl|FND_TREE_VL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[fnd_tree_vl|FND_TREE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | IconName | ICON_NAME | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | SetId | SET_ID | — | ✅ |
| 9 | TreeCode | TREE_CODE | 🔑 | ✅ |
| 10 | TreeName | TREE_NAME | — | ✅ |
| 11 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
