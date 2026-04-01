---
id: DOC-OTHER-PVO-ItemClassTranslationExtractPVO
doc_type: system-doc
title: "ItemClassTranslationExtractPVO — PVO Cross-Module"
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
  - ItemClassTranslationExtractPVO
  - itemclasstranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemClassTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Class Translation Extract. Acessa as tabelas: EGP_ITEM_CLASSES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.ItemClassTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_classes_tl|EGP_ITEM_CLASSES_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[egp_item_classes_tl|EGP_ITEM_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemClassTranPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ItemClassTranPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ItemClassTranPEODescription | DESCRIPTION | — | ✅ |
| 4 | ItemClassTranPEOItemClassId | ITEM_CLASS_ID | 🔑 | ✅ |
| 5 | ItemClassTranPEOItemClassName | ITEM_CLASS_NAME | — | ✅ |
| 6 | ItemClassTranPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | ItemClassTranPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ItemClassTranPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ItemClassTranPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ItemClassTranPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
