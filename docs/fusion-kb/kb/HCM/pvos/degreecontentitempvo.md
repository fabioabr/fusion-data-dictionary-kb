---
id: DOC-HCM-PVO-DegreeContentItemPVO
doc_type: system-doc
title: "DegreeContentItemPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - DegreeContentItemPVO
  - degreecontentitempvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DegreeContentItemPVO

## 📌 Visão Geral

Cataloga graus academicos na biblioteca de conteudo de perfis com traducoes. Referencia para qualificacoes educacionais no modelo de talent management.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileContentLibraryAM.DegreeContentItemPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 92 | 3 | 3 | 8 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]] — 65 atributos (2 PKs, 4 BICC)
- [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]] — 23 atributos (1 PKs, 3 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 4 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | ContentItemBPEOContentItemCode | CONTENT_ITEM_CODE | — | — |
| 3 | ContentItemBPEOContentItemId | CONTENT_ITEM_ID | 🔑 | ✅ |
| 4 | ContentItemBPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 5 | ContentItemBPEODateFrom | DATE_FROM | — | — |
| 6 | ContentItemBPEODateTo | DATE_TO | — | — |
| 7 | ContentItemBPEORatingModelId | RATING_MODEL_ID | — | — |
| 8 | ContentKeyflexId | CONTENT_KEYFLEX_ID | — | — |
| 9 | ContentSupplierCode | CONTENT_SUPPLIER_CODE | — | — |
| 10 | CreatedBy | CREATED_BY | — | — |
| 11 | CreationDate | CREATION_DATE | — | — |
| 12 | ItemDate1 | ITEM_DATE_1 | — | — |
| 13 | ItemDate10 | ITEM_DATE_10 | — | — |
| 14 | ItemDate2 | ITEM_DATE_2 | — | — |
| 15 | ItemDate3 | ITEM_DATE_3 | — | — |
| 16 | ItemDate4 | ITEM_DATE_4 | — | — |
| 17 | ItemDate5 | ITEM_DATE_5 | — | — |
| 18 | ItemDate6 | ITEM_DATE_6 | — | — |
| 19 | ItemDate7 | ITEM_DATE_7 | — | — |
| 20 | ItemDate8 | ITEM_DATE_8 | — | — |
| 21 | ItemDate9 | ITEM_DATE_9 | — | — |
| 22 | ItemNumber1 | ITEM_NUMBER_1 | — | — |
| 23 | ItemNumber10 | ITEM_NUMBER_10 | — | — |
| 24 | ItemNumber2 | ITEM_NUMBER_2 | — | — |
| 25 | ItemNumber3 | ITEM_NUMBER_3 | — | — |
| 26 | ItemNumber4 | ITEM_NUMBER_4 | — | — |
| 27 | ItemNumber5 | ITEM_NUMBER_5 | — | — |
| 28 | ItemNumber6 | ITEM_NUMBER_6 | — | — |
| 29 | ItemNumber7 | ITEM_NUMBER_7 | — | — |
| 30 | ItemNumber8 | ITEM_NUMBER_8 | — | — |
| 31 | ItemNumber9 | ITEM_NUMBER_9 | — | — |
| 32 | ItemText1 | ITEM_TEXT_1 | — | — |
| 33 | ItemText10 | ITEM_TEXT_10 | — | — |
| 34 | ItemText11 | ITEM_TEXT_11 | — | — |
| 35 | ItemText12 | ITEM_TEXT_12 | — | — |
| 36 | ItemText13 | ITEM_TEXT_13 | — | — |
| 37 | ItemText14 | ITEM_TEXT_14 | — | — |
| 38 | ItemText15 | ITEM_TEXT_15 | — | — |
| 39 | ItemText16 | ITEM_TEXT_16 | — | — |
| 40 | ItemText17 | ITEM_TEXT_17 | — | — |
| 41 | ItemText18 | ITEM_TEXT_18 | — | — |
| 42 | ItemText19 | ITEM_TEXT_19 | — | — |
| 43 | ItemText2 | ITEM_TEXT_2 | — | — |
| 44 | ItemText20 | ITEM_TEXT_20 | — | — |
| 45 | ItemText21 | ITEM_TEXT_21 | — | — |
| 46 | ItemText22 | ITEM_TEXT_22 | — | — |
| 47 | ItemText23 | ITEM_TEXT_23 | — | — |
| 48 | ItemText24 | ITEM_TEXT_24 | — | — |
| 49 | ItemText25 | ITEM_TEXT_25 | — | — |
| 50 | ItemText26 | ITEM_TEXT_26 | — | — |
| 51 | ItemText27 | ITEM_TEXT_27 | — | — |
| 52 | ItemText28 | ITEM_TEXT_28 | — | — |
| 53 | ItemText29 | ITEM_TEXT_29 | — | — |
| 54 | ItemText3 | ITEM_TEXT_3 | — | — |
| 55 | ItemText30 | ITEM_TEXT_30 | — | — |
| 56 | ItemText4 | ITEM_TEXT_4 | — | — |
| 57 | ItemText5 | ITEM_TEXT_5 | — | — |
| 58 | ItemText6 | ITEM_TEXT_6 | — | — |
| 59 | ItemText7 | ITEM_TEXT_7 | — | — |
| 60 | ItemText8 | ITEM_TEXT_8 | — | — |
| 61 | ItemText9 | ITEM_TEXT_9 | — | — |
| 62 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 63 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 64 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 65 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentItemTranslationPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 3 | ContentItemTranslationPEOItemDescription | ITEM_DESCRIPTION | — | — |
| 4 | ContentItemTranslationPEOItemDescrlong | ITEM_DESCRLONG | — | — |
| 5 | ContentItemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ContentItemTranslationPEOName | NAME | — | ✅ |
| 7 | ItemTextTl1 | ITEM_TEXT_TL_1 | — | — |
| 8 | ItemTextTl10 | ITEM_TEXT_TL_10 | — | — |
| 9 | ItemTextTl11 | ITEM_TEXT_TL_11 | — | — |
| 10 | ItemTextTl12 | ITEM_TEXT_TL_12 | — | — |
| 11 | ItemTextTl13 | ITEM_TEXT_TL_13 | — | — |
| 12 | ItemTextTl14 | ITEM_TEXT_TL_14 | — | — |
| 13 | ItemTextTl15 | ITEM_TEXT_TL_15 | — | — |
| 14 | ItemTextTl2 | ITEM_TEXT_TL_2 | — | — |
| 15 | ItemTextTl3 | ITEM_TEXT_TL_3 | — | — |
| 16 | ItemTextTl4 | ITEM_TEXT_TL_4 | — | — |
| 17 | ItemTextTl5 | ITEM_TEXT_TL_5 | — | — |
| 18 | ItemTextTl6 | ITEM_TEXT_TL_6 | — | — |
| 19 | ItemTextTl7 | ITEM_TEXT_TL_7 | — | — |
| 20 | ItemTextTl8 | ITEM_TEXT_TL_8 | — | — |
| 21 | ItemTextTl9 | ITEM_TEXT_TL_9 | — | — |
| 22 | Language | LANGUAGE | 🔑 | ✅ |
| 23 | SourceLang | SOURCE_LANG | — | — |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | ContentTypeId | CONTENT_TYPE_ID | — | — |
| 4 | ContextName | CONTEXT_NAME | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
