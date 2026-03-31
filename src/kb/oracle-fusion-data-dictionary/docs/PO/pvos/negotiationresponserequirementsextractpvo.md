---
id: DOC-PO-PVO-NegotiationResponseRequirementsExtractPVO
doc_type: system-doc
title: "NegotiationResponseRequirementsExtractPVO — PVO Purchasing"
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
  - NegotiationResponseRequirementsExtractPVO
  - negotiationresponserequirementsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationResponseRequirementsExtractPVO

## 📌 Visão Geral

Extrai as respostas dos fornecedores aos requisitos de negociação para carga BICC. Alimenta análises de conformidade de propostas com critérios técnicos e comerciais.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationResponseRequirementsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 2 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_bid_requirements|PON_BID_REQUIREMENTS]] — 20 atributos (2 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[pon_bid_requirements|PON_BID_REQUIREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 2 | BidNumber | BID_NUMBER | 🔑 | ✅ |
| 3 | Comments | COMMENTS | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | HasBidFlag | HAS_BID_FLAG | — | ✅ |
| 7 | InterfaceLineId | INTERFACE_LINE_ID | — | ✅ |
| 8 | InternalNote | INTERNAL_NOTE | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | OldComments | OLD_COMMENTS | — | ✅ |
| 14 | RequirementId | REQUIREMENT_ID | 🔑 | ✅ |
| 15 | Score | SCORE | — | ✅ |
| 16 | SectionId | SECTION_ID | — | ✅ |
| 17 | SequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 18 | WeightedScore | WEIGHTED_SCORE | — | ✅ |
| 19 | WorksheetName | WORKSHEET_NAME | — | ✅ |
| 20 | WorksheetSequenceNumber | WORKSHEET_SEQUENCE_NUMBER | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
