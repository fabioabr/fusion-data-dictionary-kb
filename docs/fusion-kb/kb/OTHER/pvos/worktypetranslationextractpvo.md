---
id: DOC-OTHER-PVO-WorkTypeTranslationExtractPVO
doc_type: system-doc
title: "WorkTypeTranslationExtractPVO — PVO Cross-Module"
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
  - WorkTypeTranslationExtractPVO
  - worktypetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkTypeTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Type Translation Extract. Acessa as tabelas: PJF_WORK_TYPES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.WorkTypeTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_work_types_tl|PJF_WORK_TYPES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_work_types_tl|PJF_WORK_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkTypeTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | WorkTypeTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WorkTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | WorkTypeTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | WorkTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | WorkTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | WorkTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | WorkTypeTranslationPEOName | NAME | — | ✅ |
| 9 | WorkTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | WorkTypeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 11 | WorkTypeTranslationPEOWorkTypeId | WORK_TYPE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
