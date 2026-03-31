---
id: DOC-PO-PVO-NegotiationRespRequirementValuesExtractPVO
doc_type: system-doc
title: "NegotiationRespRequirementValuesExtractPVO — PVO Purchasing"
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
  - NegotiationRespRequirementValuesExtractPVO
  - negotiationresprequirementvaluesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationRespRequirementValuesExtractPVO

## 📌 Visão Geral

Extrai os valores específicos informados pelos fornecedores para cada requisito em negociações. Permite análise quantitativa granular de conformidade e scoring automatizado.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationRespRequirementValuesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_bid_requirement_values|PON_BID_REQUIREMENT_VALUES]] — 21 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[pon_bid_requirement_values|PON_BID_REQUIREMENT_VALUES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 2 | BidNumber | BID_NUMBER | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | DateValue | DATE_VALUE | — | ✅ |
| 6 | DatetimeValue | DATETIME_VALUE | — | ✅ |
| 7 | IsSelectedFlag | IS_SELECTED_FLAG | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | NumberValue | NUMBER_VALUE | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | OldDateValue | OLD_DATE_VALUE | — | ✅ |
| 14 | OldDatetimeValue | OLD_DATETIME_VALUE | — | ✅ |
| 15 | OldIsSelectedFlag | OLD_IS_SELECTED_FLAG | — | ✅ |
| 16 | OldNumberValue | OLD_NUMBER_VALUE | — | ✅ |
| 17 | OldTextValue | OLD_TEXT_VALUE | — | ✅ |
| 18 | RequirementId | REQUIREMENT_ID | — | ✅ |
| 19 | RequirementValueId | REQUIREMENT_VALUE_ID | 🔑 | ✅ |
| 20 | ScoreId | SCORE_ID | — | ✅ |
| 21 | TextValue | TEXT_VALUE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
