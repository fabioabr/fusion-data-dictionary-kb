---
id: DOC-OTHER-PVO-FndNodeVO
doc_type: system-doc
title: "FndNodeVO — PVO Cross-Module"
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
  - FndNodeVO
  - fndnodevo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndNodeVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Node VO. Acessa as tabelas: FND_NODE_VL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.FndNodeVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 0 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_node_vl|FND_NODE_VL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[fnd_node_vl|FND_NODE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 5 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | NodeId | NODE_ID | — | ✅ |
| 10 | NodeName | NODE_NAME | — | ✅ |
| 11 | SetId | SET_ID | — | ✅ |
| 12 | TreeStructureCode | TREE_STRUCTURE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
