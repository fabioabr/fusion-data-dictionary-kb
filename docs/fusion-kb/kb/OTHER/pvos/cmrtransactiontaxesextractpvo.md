---
id: DOC-OTHER-PVO-CmrTransactionTaxesExtractPVO
doc_type: system-doc
title: "CmrTransactionTaxesExtractPVO — PVO Cross-Module"
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
  - CmrTransactionTaxesExtractPVO
  - cmrtransactiontaxesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrTransactionTaxesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Transaction Taxes Extract. Acessa as tabelas: CMR_TRANSACTION_TAXES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrTransactionTaxesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 1 | 1 | 40 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_transaction_taxes|CMR_TRANSACTION_TAXES]] — 40 atributos (1 PKs, 40 BICC)

---

## ⚙️ Atributos

### [[cmr_transaction_taxes|CMR_TRANSACTION_TAXES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrTransactionTaxesPEOAccountCcid | ACCOUNT_CCID | — | ✅ |
| 2 | CmrTransactionTaxesPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 3 | CmrTransactionTaxesPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CmrTransactionTaxesPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CmrTransactionTaxesPEOEffectiveDate | EFFECTIVE_DATE | — | ✅ |
| 6 | CmrTransactionTaxesPEOEventDate | EVENT_DATE | — | ✅ |
| 7 | CmrTransactionTaxesPEOFiscalProcessOptionCode | FISCAL_PROCESS_OPTION_CODE | — | ✅ |
| 8 | CmrTransactionTaxesPEOInclusiveFlag | INCLUSIVE_FLAG | — | ✅ |
| 9 | CmrTransactionTaxesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | CmrTransactionTaxesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | CmrTransactionTaxesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | CmrTransactionTaxesPEOLatestCorrectTxnId | LATEST_CORRECT_TXN_ID | — | ✅ |
| 13 | CmrTransactionTaxesPEOParentTransactionId | PARENT_TRANSACTION_ID | — | ✅ |
| 14 | CmrTransactionTaxesPEOPerUnitTaxAmt | PER_UNIT_TAX_AMT | — | ✅ |
| 15 | CmrTransactionTaxesPEOPoTaxFlag | PO_TAX_FLAG | — | ✅ |
| 16 | CmrTransactionTaxesPEOProcessedByCaFlag | PROCESSED_BY_CA_FLAG | — | ✅ |
| 17 | CmrTransactionTaxesPEOProcessedByRaFlag | PROCESSED_BY_RA_FLAG | — | ✅ |
| 18 | CmrTransactionTaxesPEORecNrecTaxAmt | REC_NREC_TAX_AMT | — | ✅ |
| 19 | CmrTransactionTaxesPEORecoverableFlag | RECOVERABLE_FLAG | — | ✅ |
| 20 | CmrTransactionTaxesPEORecoveryRateCode | RECOVERY_RATE_CODE | — | ✅ |
| 21 | CmrTransactionTaxesPEORecoveryTypeCode | RECOVERY_TYPE_CODE | — | ✅ |
| 22 | CmrTransactionTaxesPEOSelfAssessedFlag | SELF_ASSESSED_FLAG | — | ✅ |
| 23 | CmrTransactionTaxesPEOTax | TAX | — | ✅ |
| 24 | CmrTransactionTaxesPEOTaxApportionmentLineNumber | TAX_APPORTIONMENT_LINE_NUMBER | — | ✅ |
| 25 | CmrTransactionTaxesPEOTaxJurisdictionId | TAX_JURISDICTION_ID | — | ✅ |
| 26 | CmrTransactionTaxesPEOTaxLiabilityAccountId | TAX_LIABILITY_ACCOUNT_ID | — | ✅ |
| 27 | CmrTransactionTaxesPEOTaxLineNumber | TAX_LINE_NUMBER | — | ✅ |
| 28 | CmrTransactionTaxesPEOTaxOnlyLineFlag | TAX_ONLY_LINE_FLAG | — | ✅ |
| 29 | CmrTransactionTaxesPEOTaxPointBasis | TAX_POINT_BASIS | — | ✅ |
| 30 | CmrTransactionTaxesPEOTaxPointDate | TAX_POINT_DATE | — | ✅ |
| 31 | CmrTransactionTaxesPEOTaxRate | TAX_RATE | — | ✅ |
| 32 | CmrTransactionTaxesPEOTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 33 | CmrTransactionTaxesPEOTaxRateId | TAX_RATE_ID | — | ✅ |
| 34 | CmrTransactionTaxesPEOTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 35 | CmrTransactionTaxesPEOTaxStatusCode | TAX_STATUS_CODE | — | ✅ |
| 36 | CmrTransactionTaxesPEOTaxableAmt | TAXABLE_AMT | — | ✅ |
| 37 | CmrTransactionTaxesPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 38 | CmrTransactionTaxesPEOTransactionTaxId | TRANSACTION_TAX_ID | 🔑 | ✅ |
| 39 | CmrTransactionTaxesPEOTrxId | TRX_ID | — | ✅ |
| 40 | CmrTransactionTaxesPEOTrxQuantity | TRX_QUANTITY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
