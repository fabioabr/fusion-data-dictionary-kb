---
id: DOC-GL-PVO-JournalLineExtractPVO
doc_type: system-doc
title: "JournalLineExtractPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - JournalLineExtractPVO
  - journallineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Line Extract. Acessa as tabelas: GL_JE_LINES, GL_PERIOD_STATUSES.

**Caminho:** `FscmTopModelAM.FinGlJrnlEntriesAM.JournalLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 146 | 2 | 2 | 2 | 1% |

---

## 🔗 Tabelas Relacionadas

- [[gl_je_lines|GL_JE_LINES]] — 115 atributos (2 PKs, 2 BICC)
- [[gl_period_statuses|GL_PERIOD_STATUSES]] — 31 atributos

---

## ⚙️ Atributos

### [[gl_je_lines|GL_JE_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlJeLinesAccountedCr | ACCOUNTED_CR | — | — |
| 2 | GlJeLinesAccountedDr | ACCOUNTED_DR | — | — |
| 3 | GlJeLinesAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 4 | GlJeLinesAttribute1 | ATTRIBUTE1 | — | — |
| 5 | GlJeLinesAttribute10 | ATTRIBUTE10 | — | — |
| 6 | GlJeLinesAttribute11 | ATTRIBUTE11 | — | — |
| 7 | GlJeLinesAttribute12 | ATTRIBUTE12 | — | — |
| 8 | GlJeLinesAttribute13 | ATTRIBUTE13 | — | — |
| 9 | GlJeLinesAttribute14 | ATTRIBUTE14 | — | — |
| 10 | GlJeLinesAttribute15 | ATTRIBUTE15 | — | — |
| 11 | GlJeLinesAttribute16 | ATTRIBUTE16 | — | — |
| 12 | GlJeLinesAttribute17 | ATTRIBUTE17 | — | — |
| 13 | GlJeLinesAttribute18 | ATTRIBUTE18 | — | — |
| 14 | GlJeLinesAttribute19 | ATTRIBUTE19 | — | — |
| 15 | GlJeLinesAttribute2 | ATTRIBUTE2 | — | — |
| 16 | GlJeLinesAttribute20 | ATTRIBUTE20 | — | — |
| 17 | GlJeLinesAttribute3 | ATTRIBUTE3 | — | — |
| 18 | GlJeLinesAttribute4 | ATTRIBUTE4 | — | — |
| 19 | GlJeLinesAttribute5 | ATTRIBUTE5 | — | — |
| 20 | GlJeLinesAttribute6 | ATTRIBUTE6 | — | — |
| 21 | GlJeLinesAttribute7 | ATTRIBUTE7 | — | — |
| 22 | GlJeLinesAttribute8 | ATTRIBUTE8 | — | — |
| 23 | GlJeLinesAttribute9 | ATTRIBUTE9 | — | — |
| 24 | GlJeLinesAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 25 | GlJeLinesAttributeCategory2 | ATTRIBUTE_CATEGORY2 | — | — |
| 26 | GlJeLinesAttributeCategory3 | ATTRIBUTE_CATEGORY3 | — | — |
| 27 | GlJeLinesAttributeCategory4 | ATTRIBUTE_CATEGORY4 | — | — |
| 28 | GlJeLinesCoProcessedFlag | CO_PROCESSED_FLAG | — | — |
| 29 | GlJeLinesCoThirdParty | CO_THIRD_PARTY | — | — |
| 30 | GlJeLinesCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 31 | GlJeLinesCreatedBy | CREATED_BY | — | — |
| 32 | GlJeLinesCreationDate | CREATION_DATE | — | — |
| 33 | GlJeLinesCurrencyCode | CURRENCY_CODE | — | — |
| 34 | GlJeLinesCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | — |
| 35 | GlJeLinesCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 36 | GlJeLinesCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | — |
| 37 | GlJeLinesDescription | DESCRIPTION | — | — |
| 38 | GlJeLinesEffectiveDate | EFFECTIVE_DATE | — | — |
| 39 | GlJeLinesEnteredCr | ENTERED_CR | — | — |
| 40 | GlJeLinesEnteredDr | ENTERED_DR | — | — |
| 41 | GlJeLinesGlSlLinkId | GL_SL_LINK_ID | — | — |
| 42 | GlJeLinesGlSlLinkTable | GL_SL_LINK_TABLE | — | — |
| 43 | GlJeLinesGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 44 | GlJeLinesGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 45 | GlJeLinesGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 46 | GlJeLinesGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 47 | GlJeLinesGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 48 | GlJeLinesGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 49 | GlJeLinesGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 50 | GlJeLinesGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 51 | GlJeLinesGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 52 | GlJeLinesGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 53 | GlJeLinesGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 54 | GlJeLinesGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 55 | GlJeLinesGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 56 | GlJeLinesGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 57 | GlJeLinesGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 58 | GlJeLinesGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 59 | GlJeLinesGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 60 | GlJeLinesGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 61 | GlJeLinesGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 62 | GlJeLinesGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 63 | GlJeLinesGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 64 | GlJeLinesGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 65 | GlJeLinesGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 66 | GlJeLinesGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 67 | GlJeLinesGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 68 | GlJeLinesGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 69 | GlJeLinesGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 70 | GlJeLinesGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 71 | GlJeLinesGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 72 | GlJeLinesGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 73 | GlJeLinesGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 74 | GlJeLinesIgnoreRateFlag | IGNORE_RATE_FLAG | — | — |
| 75 | GlJeLinesInvoiceAmount | INVOICE_AMOUNT | — | — |
| 76 | GlJeLinesInvoiceDate | INVOICE_DATE | — | — |
| 77 | GlJeLinesInvoiceIdentifier | INVOICE_IDENTIFIER | — | — |
| 78 | GlJeLinesJgzzReconRef | JGZZ_RECON_REF | — | — |
| 79 | GlJeLinesLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 80 | GlJeLinesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 81 | GlJeLinesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 82 | GlJeLinesLedgerId | LEDGER_ID | — | — |
| 83 | GlJeLinesLineTypeCode | LINE_TYPE_CODE | — | — |
| 84 | GlJeLinesNo1 | NO1 | — | — |
| 85 | GlJeLinesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 86 | GlJeLinesPeriodName | PERIOD_NAME | — | — |
| 87 | GlJeLinesReference1 | REFERENCE_1 | — | — |
| 88 | GlJeLinesReference10 | REFERENCE_10 | — | — |
| 89 | GlJeLinesReference2 | REFERENCE_2 | — | — |
| 90 | GlJeLinesReference3 | REFERENCE_3 | — | — |
| 91 | GlJeLinesReference4 | REFERENCE_4 | — | — |
| 92 | GlJeLinesReference5 | REFERENCE_5 | — | — |
| 93 | GlJeLinesReference6 | REFERENCE_6 | — | — |
| 94 | GlJeLinesReference7 | REFERENCE_7 | — | — |
| 95 | GlJeLinesReference8 | REFERENCE_8 | — | — |
| 96 | GlJeLinesReference9 | REFERENCE_9 | — | — |
| 97 | GlJeLinesStatAmount | STAT_AMOUNT | — | — |
| 98 | GlJeLinesStatus | STATUS | — | — |
| 99 | GlJeLinesSubledgerDocSequenceId | SUBLEDGER_DOC_SEQUENCE_ID | — | — |
| 100 | GlJeLinesSubledgerDocSequenceValue | SUBLEDGER_DOC_SEQUENCE_VALUE | — | — |
| 101 | GlJeLinesTaxCode | TAX_CODE | — | — |
| 102 | GlJeLinesTaxCodeId | TAX_CODE_ID | — | — |
| 103 | GlJeLinesTaxCustomerName | TAX_CUSTOMER_NAME | — | — |
| 104 | GlJeLinesTaxCustomerReference | TAX_CUSTOMER_REFERENCE | — | — |
| 105 | GlJeLinesTaxDocumentDate | TAX_DOCUMENT_DATE | — | — |
| 106 | GlJeLinesTaxDocumentIdentifier | TAX_DOCUMENT_IDENTIFIER | — | — |
| 107 | GlJeLinesTaxGroupId | TAX_GROUP_ID | — | — |
| 108 | GlJeLinesTaxLineFlag | TAX_LINE_FLAG | — | — |
| 109 | GlJeLinesTaxRegistrationNumber | TAX_REGISTRATION_NUMBER | — | — |
| 110 | GlJeLinesTaxRoundingRuleCode | TAX_ROUNDING_RULE_CODE | — | — |
| 111 | GlJeLinesTaxTypeCode | TAX_TYPE_CODE | — | — |
| 112 | GlJeLinesTaxableLineFlag | TAXABLE_LINE_FLAG | — | — |
| 113 | GlJeLinesUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 114 | JeHeaderId | JE_HEADER_ID | 🔑 | ✅ |
| 115 | JeLineNum | JE_LINE_NUM | 🔑 | ✅ |

### [[gl_period_statuses|GL_PERIOD_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlPeriodStatusesAdjustmentPeriodFlag | ADJUSTMENT_PERIOD_FLAG | — | — |
| 2 | GlPeriodStatusesApplicationId | APPLICATION_ID | — | — |
| 3 | GlPeriodStatusesAttribute110 | ATTRIBUTE1 | — | — |
| 4 | GlPeriodStatusesAttribute21 | ATTRIBUTE2 | — | — |
| 5 | GlPeriodStatusesAttribute31 | ATTRIBUTE3 | — | — |
| 6 | GlPeriodStatusesAttribute41 | ATTRIBUTE4 | — | — |
| 7 | GlPeriodStatusesAttribute51 | ATTRIBUTE5 | — | — |
| 8 | GlPeriodStatusesAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 9 | GlPeriodStatusesChronologicalSeqStatusCode | CHRONOLOGICAL_SEQ_STATUS_CODE | — | — |
| 10 | GlPeriodStatusesClosingStatus | CLOSING_STATUS | — | — |
| 11 | GlPeriodStatusesCreatedBy | CREATED_BY | — | — |
| 12 | GlPeriodStatusesCreationDate | CREATION_DATE | — | — |
| 13 | GlPeriodStatusesEffectivePeriodNum | EFFECTIVE_PERIOD_NUM | — | — |
| 14 | GlPeriodStatusesEliminationConfirmedFlag | ELIMINATION_CONFIRMED_FLAG | — | — |
| 15 | GlPeriodStatusesEndDate | END_DATE | — | — |
| 16 | GlPeriodStatusesLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 17 | GlPeriodStatusesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | GlPeriodStatusesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | GlPeriodStatusesLedgerId | LEDGER_ID | — | — |
| 20 | GlPeriodStatusesMigrationStatusCode | MIGRATION_STATUS_CODE | — | — |
| 21 | GlPeriodStatusesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | GlPeriodStatusesPeriodName | PERIOD_NAME | — | — |
| 23 | GlPeriodStatusesPeriodNum | PERIOD_NUM | — | — |
| 24 | GlPeriodStatusesPeriodType | PERIOD_TYPE | — | — |
| 25 | GlPeriodStatusesPeriodYear | PERIOD_YEAR | — | — |
| 26 | GlPeriodStatusesQuarterNum | QUARTER_NUM | — | — |
| 27 | GlPeriodStatusesQuarterStartDate | QUARTER_START_DATE | — | — |
| 28 | GlPeriodStatusesSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 29 | GlPeriodStatusesStartDate | START_DATE | — | — |
| 30 | GlPeriodStatusesTrackBcYtdFlag | TRACK_BC_YTD_FLAG | — | — |
| 31 | GlPeriodStatusesYearStartDate | YEAR_START_DATE | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
