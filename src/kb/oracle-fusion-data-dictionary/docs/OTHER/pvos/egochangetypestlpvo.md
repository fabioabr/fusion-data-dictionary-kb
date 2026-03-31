---
id: DOC-OTHER-PVO-EgoChangeTypesTLPVO
doc_type: system-doc
title: "EgoChangeTypesTLPVO — PVO Cross-Module"
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
  - EgoChangeTypesTLPVO
  - egochangetypestlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EgoChangeTypesTLPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ego Change Types TL. Acessa as tabelas: EGO_CHANGE_TYPES_TL.

**Caminho:** `FscmTopModelAM.ChangeTypesAM.EgoChangeTypesTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 4 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_types_tl|EGO_CHANGE_TYPES_TL]] — 12 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[ego_change_types_tl|EGO_CHANGE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeTypeId | CHANGE_TYPE_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | Description | DESCRIPTION | — | — |
| 5 | Language | LANGUAGE | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | SourceLang | SOURCE_LANG | — | — |
| 11 | TabText | TAB_TEXT | — | — |
| 12 | TypeName | TYPE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
