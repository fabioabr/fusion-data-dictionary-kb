---
id: DOC-OTHER-PVO-ChangeOrderTranslatePVO
doc_type: system-doc
title: "ChangeOrderTranslatePVO — PVO Cross-Module"
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
  - ChangeOrderTranslatePVO
  - changeordertranslatepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeOrderTranslatePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Order Translate. Acessa as tabelas: EGO_ENGINEERING_CHANGES_TL.

**Caminho:** `FscmTopModelAM.CommonAnalyticsAM.ChangeOrderTranslatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 11 | 85% |

---

## 🔗 Tabelas Relacionadas

- [[ego_engineering_changes_tl|EGO_ENGINEERING_CHANGES_TL]] — 13 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[ego_engineering_changes_tl|EGO_ENGINEERING_CHANGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CancellationComments | CANCELLATION_COMMENTS | — | — |
| 2 | ChangeId | CHANGE_ID | 🔑 | ✅ |
| 3 | ChangeName | CHANGE_NAME | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | Description | DESCRIPTION | — | ✅ |
| 7 | Language | LANGUAGE | 🔑 | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | Resolution | RESOLUTION | — | — |
| 13 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
