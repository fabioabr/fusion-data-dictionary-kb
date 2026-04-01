---
id: DOC-HCM-PVO-FndNodeTLVO
doc_type: system-doc
title: "FndNodeTLVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - FndNodeTLVO
  - fndnodetlvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndNodeTLVO

## 📌 Visão Geral

Disponibiliza traduções de nós de árvore hierárquica Foundation. Utilizado para exibição multilíngue de estruturas organizacionais e financeiras.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AnalyticsServiceAM.FndNodeTLVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 3 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_node_tl|FND_NODE_TL]] — 11 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[fnd_node_tl|FND_NODE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | NodeId | NODE_ID | 🔑 | ✅ |
| 9 | NodeName | NODE_NAME | — | ✅ |
| 10 | SourceLang | SOURCE_LANG | — | ✅ |
| 11 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
