---
id: DOC-OTHER-PVO-ContentItemTranslationPVO
doc_type: system-doc
title: "ContentItemTranslationPVO — PVO Cross-Module"
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
  - ContentItemTranslationPVO
  - contentitemtranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContentItemTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Content Item Translation. Acessa as tabelas: HRT_CONTENT_ITEMS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmProfileContentLibraryAM.ContentItemTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 1 | 3 | 28 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]] — 28 atributos (3 PKs, 28 BICC)

---

## ⚙️ Atributos

### [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | ContentItemId | CONTENT_ITEM_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | ItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 6 | ItemDescrlong | ITEM_DESCRLONG | — | ✅ |
| 7 | ItemTextTl1 | ITEM_TEXT_TL_1 | — | ✅ |
| 8 | ItemTextTl10 | ITEM_TEXT_TL_10 | — | ✅ |
| 9 | ItemTextTl11 | ITEM_TEXT_TL_11 | — | ✅ |
| 10 | ItemTextTl12 | ITEM_TEXT_TL_12 | — | ✅ |
| 11 | ItemTextTl13 | ITEM_TEXT_TL_13 | — | ✅ |
| 12 | ItemTextTl14 | ITEM_TEXT_TL_14 | — | ✅ |
| 13 | ItemTextTl15 | ITEM_TEXT_TL_15 | — | ✅ |
| 14 | ItemTextTl2 | ITEM_TEXT_TL_2 | — | ✅ |
| 15 | ItemTextTl3 | ITEM_TEXT_TL_3 | — | ✅ |
| 16 | ItemTextTl4 | ITEM_TEXT_TL_4 | — | ✅ |
| 17 | ItemTextTl5 | ITEM_TEXT_TL_5 | — | ✅ |
| 18 | ItemTextTl6 | ITEM_TEXT_TL_6 | — | ✅ |
| 19 | ItemTextTl7 | ITEM_TEXT_TL_7 | — | ✅ |
| 20 | ItemTextTl8 | ITEM_TEXT_TL_8 | — | ✅ |
| 21 | ItemTextTl9 | ITEM_TEXT_TL_9 | — | ✅ |
| 22 | Language | LANGUAGE | 🔑 | ✅ |
| 23 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 25 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | Name | NAME | — | ✅ |
| 27 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 28 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
