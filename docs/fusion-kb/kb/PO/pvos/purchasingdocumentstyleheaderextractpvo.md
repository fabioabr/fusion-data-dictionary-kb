---
id: DOC-PO-PVO-PurchasingDocumentStyleHeaderExtractPVO
doc_type: system-doc
title: "PurchasingDocumentStyleHeaderExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PurchasingDocumentStyleHeaderExtractPVO
  - purchasingdocumentstyleheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingDocumentStyleHeaderExtractPVO

## 📌 Visão Geral

Extrai os estilos de documento de compra no nível de cabeçalho para carga BICC, definindo regras de layout, campos obrigatórios e comportamento do formulário por tipo de pedido.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingDocumentStyleHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 1 | 17 | 81% |

---

## 🔗 Tabelas Relacionadas

- [[po_doc_style_headers|PO_DOC_STYLE_HEADERS]] — 21 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[po_doc_style_headers|PO_DOC_STYLE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdvancesFlag | ADVANCES_FLAG | — | — |
| 2 | ConfiguredItemFlag | CONFIGURED_ITEM_FLAG | — | ✅ |
| 3 | ConsignedItemsFlag | CONSIGNED_ITEMS_FLAG | — | ✅ |
| 4 | ContractFinancingFlag | CONTRACT_FINANCING_FLAG | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | LineTypeAllowed | LINE_TYPE_ALLOWED | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | OutsideProcessingFlag | OUTSIDE_PROCESSING_FLAG | — | ✅ |
| 13 | PriceBreaksFlag | PRICE_BREAKS_FLAG | — | ✅ |
| 14 | PriceDifferentialsFlag | PRICE_DIFFERENTIALS_FLAG | — | — |
| 15 | ProgressPaymentFlag | PROGRESS_PAYMENT_FLAG | — | — |
| 16 | RetainageFlag | RETAINAGE_FLAG | — | — |
| 17 | Status | STATUS | — | ✅ |
| 18 | StyleDescription | STYLE_DESCRIPTION | — | ✅ |
| 19 | StyleId | STYLE_ID | 🔑 | ✅ |
| 20 | StyleName | STYLE_NAME | — | ✅ |
| 21 | StyleType | STYLE_TYPE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
