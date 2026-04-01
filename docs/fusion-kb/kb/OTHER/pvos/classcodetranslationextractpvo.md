---
id: DOC-OTHER-PVO-ClassCodeTranslationExtractPVO
doc_type: system-doc
title: "ClassCodeTranslationExtractPVO — PVO Cross-Module"
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
  - ClassCodeTranslationExtractPVO
  - classcodetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClassCodeTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Class Code Translation Extract. Acessa as tabelas: PJF_CLASS_CODES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ClassCodeTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_class_codes_tl|PJF_CLASS_CODES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_class_codes_tl|PJF_CLASS_CODES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassCodeTranslationPEOClassCode | CLASS_CODE | — | ✅ |
| 2 | ClassCodeTranslationPEOClassCodeId | CLASS_CODE_ID | 🔑 | ✅ |
| 3 | ClassCodeTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ClassCodeTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ClassCodeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 6 | ClassCodeTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | ClassCodeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ClassCodeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ClassCodeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ClassCodeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ClassCodeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
