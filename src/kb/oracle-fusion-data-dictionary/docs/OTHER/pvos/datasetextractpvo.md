---
id: DOC-OTHER-PVO-DataSetExtractPVO
doc_type: system-doc
title: "DataSetExtractPVO — PVO Cross-Module"
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
  - DataSetExtractPVO
  - datasetextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DataSetExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Data Set Extract. Acessa as tabelas: XCC_DATA_SETS.

**Caminho:** `FscmTopModelAM.FinExtractAM.XccBiccExtractAM.DataSetExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 18 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[xcc_data_sets|XCC_DATA_SETS]] — 19 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[xcc_data_sets|XCC_DATA_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionCode | ACTION_CODE | — | ✅ |
| 2 | CallingMethodCode | CALLING_METHOD_CODE | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | DataSetId | DATA_SET_ID | 🔑 | ✅ |
| 6 | FatalErrorMessage | FATAL_ERROR_MESSAGE | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | LedgerId | LEDGER_ID | — | ✅ |
| 11 | OverrideAvailableFlag | OVERRIDE_AVAILABLE_FLAG | — | ✅ |
| 12 | OverrideFlag | OVERRIDE_FLAG | — | ✅ |
| 13 | OverrideModeCode | OVERRIDE_MODE_CODE | — | ✅ |
| 14 | OverrideReason | OVERRIDE_REASON | — | ✅ |
| 15 | OverrideUserGuid | OVERRIDE_USER_GUID | — | ✅ |
| 16 | ReprocessFlag | REPROCESS_FLAG | — | — |
| 17 | ReservationModeCode | RESERVATION_MODE_CODE | — | ✅ |
| 18 | ResultCode | RESULT_CODE | — | ✅ |
| 19 | TransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
