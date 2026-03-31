---
id: DOC-PO-PVO-PurchasingLineTypeBExtractPVO
doc_type: system-doc
title: "PurchasingLineTypeBExtractPVO — PVO Purchasing"
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
  - PurchasingLineTypeBExtractPVO
  - purchasinglinetypebextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingLineTypeBExtractPVO

## 📌 Visão Geral

Extrai os tipos de linha de compra configurados (bens, serviços, taxa fixa) para carga BICC, com regras de recebimento e faturamento. Define como cada tipo de aquisição é processado.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingLineTypeBExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 69 | 1 | 1 | 18 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[po_line_types_b|PO_LINE_TYPES_B]] — 69 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[po_line_types_b|PO_LINE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute16 | ATTRIBUTE16 | — | — |
| 9 | Attribute17 | ATTRIBUTE17 | — | — |
| 10 | Attribute18 | ATTRIBUTE18 | — | — |
| 11 | Attribute19 | ATTRIBUTE19 | — | — |
| 12 | Attribute2 | ATTRIBUTE2 | — | — |
| 13 | Attribute20 | ATTRIBUTE20 | — | — |
| 14 | Attribute3 | ATTRIBUTE3 | — | — |
| 15 | Attribute4 | ATTRIBUTE4 | — | — |
| 16 | Attribute5 | ATTRIBUTE5 | — | — |
| 17 | Attribute6 | ATTRIBUTE6 | — | — |
| 18 | Attribute7 | ATTRIBUTE7 | — | — |
| 19 | Attribute8 | ATTRIBUTE8 | — | — |
| 20 | Attribute9 | ATTRIBUTE9 | — | — |
| 21 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | CategoryId | CATEGORY_ID | — | ✅ |
| 53 | CreatedBy | CREATED_BY | — | ✅ |
| 54 | CreationDate | CREATION_DATE | — | ✅ |
| 55 | InactiveDate | INACTIVE_DATE | — | ✅ |
| 56 | InspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | ✅ |
| 57 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 58 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 59 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 60 | LineTypeCode | LINE_TYPE_CODE | — | ✅ |
| 61 | LineTypeId | LINE_TYPE_ID | 🔑 | ✅ |
| 62 | MatchOption | MATCH_OPTION | — | ✅ |
| 63 | MatchingBasis | MATCHING_BASIS | — | ✅ |
| 64 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 65 | PurchaseBasis | PURCHASE_BASIS | — | ✅ |
| 66 | ReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | ✅ |
| 67 | ReceivingFlag | RECEIVING_FLAG | — | ✅ |
| 68 | UnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 69 | UomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
