---
id: DOC-OTHER-PVO-ReferableProduct
doc_type: system-doc
title: "ReferableProduct — PVO Cross-Module"
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
  - ReferableProduct
  - referableproduct
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReferableProduct

## 📌 Visão Geral

View Object para extração BICC de dados de Referable Product. Acessa as tabelas: ZBS_REFERABLE_PRODUCTS.

**Caminho:** `FscmTopModelAM.ReferenceAM.ReferableProduct`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 1 | 1 | 6 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[zbs_referable_products|ZBS_REFERABLE_PRODUCTS]] — 25 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[zbs_referable_products|ZBS_REFERABLE_PRODUCTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Comments | COMMENTS | — | — |
| 2 | ConflictId | CONFLICT_ID | — | — |
| 3 | CreatedBy | CREATED_BY | — | — |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | HideFlag | HIDE_FLAG | — | — |
| 6 | InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 7 | InventoryOrgId | INVENTORY_ORG_ID | — | — |
| 8 | KeyContactId | KEY_CONTACT_ID | — | — |
| 9 | LastOrderDate | LAST_ORDER_DATE | — | — |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | LevelCode | LEVEL_CODE | — | — |
| 14 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | PartyId | PARTY_ID | — | ✅ |
| 16 | ProdGroupId | PROD_GROUP_ID | — | ✅ |
| 17 | QuantityNum | QUANTITY_NUM | — | — |
| 18 | ReferableCode | REFERABLE_CODE | — | — |
| 19 | ReferableProductId | REFERABLE_PRODUCT_ID | 🔑 | ✅ |
| 20 | RevnAmt | REVN_AMT | — | — |
| 21 | RevnCurrencyCode | REVN_CURRENCY_CODE | — | — |
| 22 | RowTypeCode | ROW_TYPE_CODE | — | — |
| 23 | SourceCode | SOURCE_CODE | — | — |
| 24 | UomCode | UOM_CODE | — | — |
| 25 | UserLastUpdateDate | USER_LAST_UPDATE_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
