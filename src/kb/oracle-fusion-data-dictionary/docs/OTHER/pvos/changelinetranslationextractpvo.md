---
id: DOC-OTHER-PVO-ChangeLineTranslationExtractPVO
doc_type: system-doc
title: "ChangeLineTranslationExtractPVO — PVO Cross-Module"
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
  - ChangeLineTranslationExtractPVO
  - changelinetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeLineTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Line Translation Extract. Acessa as tabelas: EGO_CHANGE_LINES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.ChangeLineTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_lines_tl|EGO_CHANGE_LINES_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[ego_change_lines_tl|EGO_CHANGE_LINES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeLineTLPEOCancelComments | CANCEL_COMMENTS | — | ✅ |
| 2 | ChangeLineTLPEOChangeLineId | CHANGE_LINE_ID | 🔑 | ✅ |
| 3 | ChangeLineTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ChangeLineTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ChangeLineTLPEODescription | DESCRIPTION | — | ✅ |
| 6 | ChangeLineTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | ChangeLineTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ChangeLineTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ChangeLineTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ChangeLineTLPEOName | NAME | — | ✅ |
| 11 | ChangeLineTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ChangeLineTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
