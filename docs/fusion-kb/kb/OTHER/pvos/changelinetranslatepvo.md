---
id: DOC-OTHER-PVO-ChangeLineTranslatePVO
doc_type: system-doc
title: "ChangeLineTranslatePVO — PVO Cross-Module"
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
  - ChangeLineTranslatePVO
  - changelinetranslatepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeLineTranslatePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Line Translate. Acessa as tabelas: EGO_CHANGE_LINES_TL.

**Caminho:** `FscmTopModelAM.CommonAnalyticsAM.ChangeLineTranslatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 10 | 83% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_lines_tl|EGO_CHANGE_LINES_TL]] — 12 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[ego_change_lines_tl|EGO_CHANGE_LINES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CancelComments | CANCEL_COMMENTS | — | — |
| 2 | ChangeLineId | CHANGE_LINE_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | Description | DESCRIPTION | — | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | Name | NAME | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
