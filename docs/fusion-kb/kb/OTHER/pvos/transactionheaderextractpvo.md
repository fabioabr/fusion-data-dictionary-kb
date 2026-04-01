---
id: DOC-OTHER-PVO-TransactionHeaderExtractPVO
doc_type: system-doc
title: "TransactionHeaderExtractPVO — PVO Cross-Module"
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
  - TransactionHeaderExtractPVO
  - transactionheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Header Extract. Acessa as tabelas: XCC_TR_HEADERS.

**Caminho:** `FscmTopModelAM.FinExtractAM.XccBiccExtractAM.TransactionHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 1 | 1 | 26 | 87% |

---

## 🔗 Tabelas Relacionadas

- [[xcc_tr_headers|XCC_TR_HEADERS]] — 30 atributos (1 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[xcc_tr_headers|XCC_TR_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArrivalOrder | ARRIVAL_ORDER | — | ✅ |
| 2 | BudgetFlag | BUDGET_FLAG | — | ✅ |
| 3 | BusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | DataPurgedFlag | DATA_PURGED_FLAG | — | — |
| 7 | DataSetId | DATA_SET_ID | — | ✅ |
| 8 | DestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 9 | DocumentTypeCode | DOCUMENT_TYPE_CODE | — | ✅ |
| 10 | DraftFlag | DRAFT_FLAG | — | ✅ |
| 11 | FailureReasonCode | FAILURE_REASON_CODE | — | — |
| 12 | HeaderGroupCode | HEADER_GROUP_CODE | — | — |
| 13 | HeaderNum | HEADER_NUM | 🔑 | ✅ |
| 14 | JeSourceCode | JE_SOURCE_CODE | — | ✅ |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | LedgerId | LEDGER_ID | — | ✅ |
| 19 | LiquidationDateCode | LIQUIDATION_DATE_CODE | — | ✅ |
| 20 | OverridableCode | OVERRIDABLE_CODE | — | ✅ |
| 21 | OverrideFlag | OVERRIDE_FLAG | — | ✅ |
| 22 | PartialReservationFlag | PARTIAL_RESERVATION_FLAG | — | ✅ |
| 23 | ResultCode | RESULT_CODE | — | ✅ |
| 24 | SourceActionCode | SOURCE_ACTION_CODE | — | ✅ |
| 25 | SourceHeaderId1 | SOURCE_HEADER_ID_1 | — | ✅ |
| 26 | SourceHeaderId2 | SOURCE_HEADER_ID_2 | — | ✅ |
| 27 | SuccessReasonCode | SUCCESS_REASON_CODE | — | — |
| 28 | TransactionNumber | TRANSACTION_NUMBER | — | ✅ |
| 29 | TransactionSourceCode | TRANSACTION_SOURCE_CODE | — | ✅ |
| 30 | TransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
