---
id: DOC-OTHER-PVO-TagPVO
doc_type: system-doc
title: "TagPVO — PVO Cross-Module"
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
  - TagPVO
  - tagpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TagPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Tag. Acessa as tabelas: PJL_TAGS.

**Caminho:** `FscmTopModelAM.PjlTaskManagementAM.TagPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 1 | 3 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[pjl_tags|PJL_TAGS]] — 8 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[pjl_tags|PJL_TAGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TagId | TAG_ID | 🔑 | ✅ |
| 2 | TagPEOCreatedBy | CREATED_BY | — | — |
| 3 | TagPEOCreationDate | CREATION_DATE | — | — |
| 4 | TagPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TagPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | TagPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | TagPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | TagPEOTag | TAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
