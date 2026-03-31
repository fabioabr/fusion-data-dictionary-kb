---
id: DOC-OTHER-PVO-TransactionDistributionExtractPVO
doc_type: system-doc
title: "TransactionDistributionExtractPVO — PVO Cross-Module"
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
  - TransactionDistributionExtractPVO
  - transactiondistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionDistributionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Distribution Extract. Acessa as tabelas: RA_CUST_TRX_LINE_GL_DIST_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.TransactionDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 55 | 1 | 1 | 39 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[ra_cust_trx_line_gl_dist_all|RA_CUST_TRX_LINE_GL_DIST_ALL]] — 55 atributos (1 PKs, 39 BICC)

---

## ⚙️ Atributos

### [[ra_cust_trx_line_gl_dist_all|RA_CUST_TRX_LINE_GL_DIST_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaCustTrxLineGlDistAccountClass | ACCOUNT_CLASS | — | ✅ |
| 2 | RaCustTrxLineGlDistAccountSetFlag | ACCOUNT_SET_FLAG | — | ✅ |
| 3 | RaCustTrxLineGlDistAcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 4 | RaCustTrxLineGlDistAmount | AMOUNT | — | ✅ |
| 5 | RaCustTrxLineGlDistAttribute1 | ATTRIBUTE1 | — | — |
| 6 | RaCustTrxLineGlDistAttribute10 | ATTRIBUTE10 | — | — |
| 7 | RaCustTrxLineGlDistAttribute11 | ATTRIBUTE11 | — | — |
| 8 | RaCustTrxLineGlDistAttribute12 | ATTRIBUTE12 | — | — |
| 9 | RaCustTrxLineGlDistAttribute13 | ATTRIBUTE13 | — | — |
| 10 | RaCustTrxLineGlDistAttribute14 | ATTRIBUTE14 | — | — |
| 11 | RaCustTrxLineGlDistAttribute15 | ATTRIBUTE15 | — | — |
| 12 | RaCustTrxLineGlDistAttribute2 | ATTRIBUTE2 | — | — |
| 13 | RaCustTrxLineGlDistAttribute3 | ATTRIBUTE3 | — | — |
| 14 | RaCustTrxLineGlDistAttribute4 | ATTRIBUTE4 | — | — |
| 15 | RaCustTrxLineGlDistAttribute5 | ATTRIBUTE5 | — | — |
| 16 | RaCustTrxLineGlDistAttribute6 | ATTRIBUTE6 | — | — |
| 17 | RaCustTrxLineGlDistAttribute7 | ATTRIBUTE7 | — | — |
| 18 | RaCustTrxLineGlDistAttribute8 | ATTRIBUTE8 | — | — |
| 19 | RaCustTrxLineGlDistAttribute9 | ATTRIBUTE9 | — | — |
| 20 | RaCustTrxLineGlDistAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 21 | RaCustTrxLineGlDistCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 22 | RaCustTrxLineGlDistCollectedTaxCcid | COLLECTED_TAX_CCID | — | ✅ |
| 23 | RaCustTrxLineGlDistCollectedTaxConcatSeg | COLLECTED_TAX_CONCAT_SEG | — | ✅ |
| 24 | RaCustTrxLineGlDistComments | COMMENTS | — | ✅ |
| 25 | RaCustTrxLineGlDistConcatenatedSegments | CONCATENATED_SEGMENTS | — | ✅ |
| 26 | RaCustTrxLineGlDistCreatedBy | CREATED_BY | — | ✅ |
| 27 | RaCustTrxLineGlDistCreationDate | CREATION_DATE | — | ✅ |
| 28 | RaCustTrxLineGlDistCustTrxLineGlDistId | CUST_TRX_LINE_GL_DIST_ID | 🔑 | ✅ |
| 29 | RaCustTrxLineGlDistCustTrxLineSalesrepId | CUST_TRX_LINE_SALESREP_ID | — | ✅ |
| 30 | RaCustTrxLineGlDistCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 31 | RaCustTrxLineGlDistCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | ✅ |
| 32 | RaCustTrxLineGlDistEventId | EVENT_ID | — | ✅ |
| 33 | RaCustTrxLineGlDistGlDate | GL_DATE | — | ✅ |
| 34 | RaCustTrxLineGlDistGlPostedDate | GL_POSTED_DATE | — | ✅ |
| 35 | RaCustTrxLineGlDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | RaCustTrxLineGlDistLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 37 | RaCustTrxLineGlDistLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 38 | RaCustTrxLineGlDistLatestRecFlag | LATEST_REC_FLAG | — | ✅ |
| 39 | RaCustTrxLineGlDistObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | RaCustTrxLineGlDistOrgId | ORG_ID | — | ✅ |
| 41 | RaCustTrxLineGlDistOriginalGlDate | ORIGINAL_GL_DATE | — | ✅ |
| 42 | RaCustTrxLineGlDistPercent | PERCENT | — | ✅ |
| 43 | RaCustTrxLineGlDistPostRequestId | POST_REQUEST_ID | — | ✅ |
| 44 | RaCustTrxLineGlDistPostingControlId | POSTING_CONTROL_ID | — | ✅ |
| 45 | RaCustTrxLineGlDistProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 46 | RaCustTrxLineGlDistProgramId | PROGRAM_ID | — | ✅ |
| 47 | RaCustTrxLineGlDistProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 48 | RaCustTrxLineGlDistRecOffsetFlag | REC_OFFSET_FLAG | — | ✅ |
| 49 | RaCustTrxLineGlDistRequestId | REQUEST_ID | — | ✅ |
| 50 | RaCustTrxLineGlDistRevAdjClassTemp | REV_ADJ_CLASS_TEMP | — | ✅ |
| 51 | RaCustTrxLineGlDistRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | — | ✅ |
| 52 | RaCustTrxLineGlDistRoundingCorrectionFlag | ROUNDING_CORRECTION_FLAG | — | ✅ |
| 53 | RaCustTrxLineGlDistSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 54 | RaCustTrxLineGlDistTransferToCosting | TRANSFER_TO_COSTING | — | ✅ |
| 55 | RaCustTrxLineGlDistUserGeneratedFlag | USER_GENERATED_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
