---
id: DOC-PO-PVO-PurchasingDocumentStyleLineBP
doc_type: system-doc
title: "PurchasingDocumentStyleLineBP — PVO Purchasing"
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
  - PurchasingDocumentStyleLineBP
  - purchasingdocumentstylelinebp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingDocumentStyleLineBP

## 📌 Visão Geral

Disponibiliza estilos de documento de compra por linha para consulta, controlando a experiência do usuário nos formulários e garantindo padronização conforme política corporativa.

**Caminho:** `FscmTopModelAM.PrcPoPublicViewAM.PurchasingDocumentStyleLineBP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 3 | 2 | 13 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[po_doc_style_headers|PO_DOC_STYLE_HEADERS]] — 15 atributos (8 BICC)
- [[po_doc_style_lines_b|PO_DOC_STYLE_LINES_B]] — 9 atributos (2 PKs, 4 BICC)
- [[po_doc_style_lines_tl|PO_DOC_STYLE_LINES_TL]] — 5 atributos (1 BICC)

---

## ⚙️ Atributos

### [[po_doc_style_headers|PO_DOC_STYLE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PODocumentStyleHeaderAdvancesFlag | ADVANCES_FLAG | — | — |
| 2 | PODocumentStyleHeaderConsignedItemsFlag | CONSIGNED_ITEMS_FLAG | — | ✅ |
| 3 | PODocumentStyleHeaderContractFinancingFlag | CONTRACT_FINANCING_FLAG | — | — |
| 4 | PODocumentStyleHeaderCreationDate | CREATION_DATE | — | — |
| 5 | PODocumentStyleHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PODocumentStyleHeaderLineTypeAllowed | LINE_TYPE_ALLOWED | — | ✅ |
| 7 | PODocumentStyleHeaderPriceBreaksFlag | PRICE_BREAKS_FLAG | — | — |
| 8 | PODocumentStyleHeaderPriceDifferentialsFlag | PRICE_DIFFERENTIALS_FLAG | — | — |
| 9 | PODocumentStyleHeaderProgressPaymentFlag | PROGRESS_PAYMENT_FLAG | — | ✅ |
| 10 | PODocumentStyleHeaderRetainageFlag | RETAINAGE_FLAG | — | — |
| 11 | PODocumentStyleHeaderStatus | STATUS | — | ✅ |
| 12 | PODocumentStyleHeaderStyleDescription | STYLE_DESCRIPTION | — | ✅ |
| 13 | PODocumentStyleHeaderStyleId | STYLE_ID | — | — |
| 14 | PODocumentStyleHeaderStyleName | STYLE_NAME | — | ✅ |
| 15 | PODocumentStyleHeaderStyleType | STYLE_TYPE | — | ✅ |

### [[po_doc_style_lines_b|PO_DOC_STYLE_LINES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentSubtype | DOCUMENT_SUBTYPE | 🔑 | ✅ |
| 2 | PODocumentStyleLineBCreatedBy | CREATED_BY | — | — |
| 3 | PODocumentStyleLineBCreationDate | CREATION_DATE | — | ✅ |
| 4 | PODocumentStyleLineBEnabledFlag | ENABLED_FLAG | — | — |
| 5 | PODocumentStyleLineBLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PODocumentStyleLineBLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | PODocumentStyleLineBLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | PODocumentStyleLineBObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | StyleId | STYLE_ID | 🔑 | ✅ |

### [[po_doc_style_lines_tl|PO_DOC_STYLE_LINES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PODocumentStyleLineTransDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PODocumentStyleLineTransDocumentSubtype | DOCUMENT_SUBTYPE | — | — |
| 3 | PODocumentStyleLineTransLanguage | LANGUAGE | — | — |
| 4 | PODocumentStyleLineTransSourceLang | SOURCE_LANG | — | — |
| 5 | PODocumentStyleLineTransStyleId | STYLE_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
