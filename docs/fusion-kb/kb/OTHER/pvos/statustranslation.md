---
id: DOC-OTHER-PVO-StatusTranslation
doc_type: system-doc
title: "StatusTranslation — PVO Cross-Module"
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
  - StatusTranslation
  - statustranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StatusTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Status Translation. Acessa as tabelas: DOO_STATUSES_TL.

**Caminho:** `FscmTopModelAM.DooTopAM.StatusTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 4 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[doo_statuses_tl|DOO_STATUSES_TL]] — 10 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[doo_statuses_tl|DOO_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DisplayName | DISPLAY_NAME | — | — |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SourceLang | SOURCE_LANG | — | — |
| 10 | StatusId | STATUS_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
