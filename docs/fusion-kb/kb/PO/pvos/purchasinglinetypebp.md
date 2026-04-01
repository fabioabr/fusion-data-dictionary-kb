---
id: DOC-PO-PVO-PurchasingLineTypeBP
doc_type: system-doc
title: "PurchasingLineTypeBP — PVO Purchasing"
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
  - PurchasingLineTypeBP
  - purchasinglinetypebp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingLineTypeBP

## 📌 Visão Geral

Disponibiliza os tipos de linha de compra para consulta, incluindo nome, regras de processamento e categorização. Suporta padronização e validação de configurações de procurement.

**Caminho:** `FscmTopModelAM.PrcPoPublicViewAM.PurchasingLineTypeBP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 2 | 1 | 14 | 54% |

---

## 🔗 Tabelas Relacionadas

- [[po_line_types_b|PO_LINE_TYPES_B]] — 21 atributos (1 PKs, 12 BICC)
- [[po_line_types_tl|PO_LINE_TYPES_TL]] — 5 atributos (2 BICC)

---

## ⚙️ Atributos

### [[po_line_types_b|PO_LINE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineTypeId | LINE_TYPE_ID | 🔑 | ✅ |
| 2 | POLineTypeBCategoryId | CATEGORY_ID | — | — |
| 3 | POLineTypeBCreatedBy | CREATED_BY | — | ✅ |
| 4 | POLineTypeBCreationDate | CREATION_DATE | — | ✅ |
| 5 | POLineTypeBInactiveDate | INACTIVE_DATE | — | ✅ |
| 6 | POLineTypeBInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | ✅ |
| 7 | POLineTypeBLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | POLineTypeBLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | POLineTypeBLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | POLineTypeBLineTypeCode | LINE_TYPE_CODE | — | ✅ |
| 11 | POLineTypeBMatchOption | MATCH_OPTION | — | — |
| 12 | POLineTypeBMatchingBasis | MATCHING_BASIS | — | ✅ |
| 13 | POLineTypeBObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | POLineTypeBOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | ✅ |
| 15 | POLineTypeBOutsideOperationFlag | OUTSIDE_OPERATION_FLAG | — | — |
| 16 | POLineTypeBPurchaseBasis | PURCHASE_BASIS | — | ✅ |
| 17 | POLineTypeBReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | ✅ |
| 18 | POLineTypeBReceivingFlag | RECEIVING_FLAG | — | — |
| 19 | POLineTypeBUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 20 | POLineTypeBUnitPrice | UNIT_PRICE | — | — |
| 21 | POLineTypeBUomCode | UOM_CODE | — | — |

### [[po_line_types_tl|PO_LINE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | POLineTypeTransDescription | DESCRIPTION | — | ✅ |
| 2 | POLineTypeTransLanguage | LANGUAGE | — | — |
| 3 | POLineTypeTransLineType | LINE_TYPE | — | ✅ |
| 4 | POLineTypeTransLineTypeId | LINE_TYPE_ID | — | — |
| 5 | POLineTypeTransSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
