---
id: DOC-OTHER-PVO-FndTreeVersionTLP1
doc_type: system-doc
title: "FndTreeVersionTLP1 — PVO Cross-Module"
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
  - FndTreeVersionTLP1
  - fndtreeversiontlp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndTreeVersionTLP1

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Tree Version TLP1. Acessa as tabelas: FND_TREE_VERSION_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AnalyticsServiceAM.FndTreeVersionTLP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 5 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_tree_version_tl|FND_TREE_VERSION_TL]] — 14 atributos (5 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[fnd_tree_version_tl|FND_TREE_VERSION_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 5 | Language | LANGUAGE | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | SourceLang | SOURCE_LANG | — | ✅ |
| 10 | TreeCode | TREE_CODE | 🔑 | ✅ |
| 11 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |
| 12 | TreeVersionId | TREE_VERSION_ID | 🔑 | ✅ |
| 13 | TreeVersionName | TREE_VERSION_NAME | — | ✅ |
| 14 | VersionComment | VERSION_COMMENT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
