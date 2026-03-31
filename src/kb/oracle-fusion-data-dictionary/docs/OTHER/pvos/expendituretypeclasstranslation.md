---
id: DOC-OTHER-PVO-ExpenditureTypeClassTranslation
doc_type: system-doc
title: "ExpenditureTypeClassTranslation — PVO Cross-Module"
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
  - ExpenditureTypeClassTranslation
  - expendituretypeclasstranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenditureTypeClassTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Expenditure Type Class Translation. Acessa as tabelas: PJF_SYSTEM_LINKAGES_TL.

**Caminho:** `FscmTopModelAM.PjfSetupSystemAM.ExpenditureTypeClassTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 9 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_system_linkages_tl|PJF_SYSTEM_LINKAGES_TL]] — 11 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[pjf_system_linkages_tl|PJF_SYSTEM_LINKAGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Function1 | FUNCTION | 🔑 | ✅ |
| 5 | Language | LANGUAGE | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | Meaning | MEANING | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
