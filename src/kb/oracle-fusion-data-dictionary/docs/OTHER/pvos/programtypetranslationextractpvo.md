---
id: DOC-OTHER-PVO-ProgramTypeTranslationExtractPVO
doc_type: system-doc
title: "ProgramTypeTranslationExtractPVO — PVO Cross-Module"
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
  - ProgramTypeTranslationExtractPVO
  - programtypetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProgramTypeTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Program Type Translation Extract. Acessa as tabelas: CJM_PROGRAM_TYPES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ProgramTypeTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_program_types_tl|CJM_PROGRAM_TYPES_TL]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[cjm_program_types_tl|CJM_PROGRAM_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ProgramTypeId | PROGRAM_TYPE_ID | 🔑 | ✅ |
| 8 | ProgramTypeName | PROGRAM_TYPE_NAME | — | ✅ |
| 9 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
