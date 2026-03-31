---
id: DOC-PO-PVO-NegotiationRequistionReferenceExtractPVO
doc_type: system-doc
title: "NegotiationRequistionReferenceExtractPVO — PVO Purchasing"
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
  - NegotiationRequistionReferenceExtractPVO
  - negotiationrequistionreferenceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationRequistionReferenceExtractPVO

## 📌 Visão Geral

Extrai as referências entre negociações e requisições de compra originais, rastreando quais demandas internas deram origem a cada processo de sourcing.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationRequistionReferenceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_backing_requisitions|PON_BACKING_REQUISITIONS]] — 12 atributos (3 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pon_backing_requisitions|PON_BACKING_REQUISITIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | RequisitionHeaderId | REQUISITION_HEADER_ID | — | ✅ |
| 10 | RequisitionLineId | REQUISITION_LINE_ID | 🔑 | ✅ |
| 11 | RequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 12 | RequisitionQuantity | REQUISITION_QUANTITY | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
