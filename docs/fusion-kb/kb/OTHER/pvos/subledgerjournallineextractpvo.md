---
id: DOC-OTHER-PVO-SubledgerJournalLineExtractPVO
doc_type: system-doc
title: "SubledgerJournalLineExtractPVO — PVO Cross-Module"
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
  - SubledgerJournalLineExtractPVO
  - subledgerjournallineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerJournalLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Journal Line Extract. Acessa as tabelas: XLA_AE_LINES.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SubledgerJournalLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 133 | 1 | 3 | 116 | 87% |

---

## 🔗 Tabelas Relacionadas

- [[xla_ae_lines|XLA_AE_LINES]] — 133 atributos (3 PKs, 116 BICC)

---

## ⚙️ Atributos

### [[xla_ae_lines|XLA_AE_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalEntryLineAccountedCr | ACCOUNTED_CR | — | ✅ |
| 2 | JournalEntryLineAccountedDr | ACCOUNTED_DR | — | ✅ |
| 3 | JournalEntryLineAccountingClassCode | ACCOUNTING_CLASS_CODE | — | ✅ |
| 4 | JournalEntryLineAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 5 | JournalEntryLineAeHeaderId | AE_HEADER_ID | 🔑 | ✅ |
| 6 | JournalEntryLineAeLineNum | AE_LINE_NUM | 🔑 | ✅ |
| 7 | JournalEntryLineAnalyticalBalanceFlag | ANALYTICAL_BALANCE_FLAG | — | ✅ |
| 8 | JournalEntryLineAnchorLineFlag | ANCHOR_LINE_FLAG | — | — |
| 9 | JournalEntryLineApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 10 | JournalEntryLineAttribute1 | ATTRIBUTE1 | — | — |
| 11 | JournalEntryLineAttribute10 | ATTRIBUTE10 | — | — |
| 12 | JournalEntryLineAttribute11 | ATTRIBUTE11 | — | — |
| 13 | JournalEntryLineAttribute12 | ATTRIBUTE12 | — | — |
| 14 | JournalEntryLineAttribute13 | ATTRIBUTE13 | — | — |
| 15 | JournalEntryLineAttribute14 | ATTRIBUTE14 | — | — |
| 16 | JournalEntryLineAttribute15 | ATTRIBUTE15 | — | — |
| 17 | JournalEntryLineAttribute2 | ATTRIBUTE2 | — | — |
| 18 | JournalEntryLineAttribute3 | ATTRIBUTE3 | — | — |
| 19 | JournalEntryLineAttribute4 | ATTRIBUTE4 | — | — |
| 20 | JournalEntryLineAttribute5 | ATTRIBUTE5 | — | — |
| 21 | JournalEntryLineAttribute6 | ATTRIBUTE6 | — | — |
| 22 | JournalEntryLineAttribute7 | ATTRIBUTE7 | — | — |
| 23 | JournalEntryLineAttribute8 | ATTRIBUTE8 | — | — |
| 24 | JournalEntryLineAttribute9 | ATTRIBUTE9 | — | — |
| 25 | JournalEntryLineAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 26 | JournalEntryLineBusinessClassCode | BUSINESS_CLASS_CODE | — | ✅ |
| 27 | JournalEntryLineCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 28 | JournalEntryLineControlBalanceFlag | CONTROL_BALANCE_FLAG | — | ✅ |
| 29 | JournalEntryLineCreatedBy | CREATED_BY | — | ✅ |
| 30 | JournalEntryLineCreationDate | CREATION_DATE | — | ✅ |
| 31 | JournalEntryLineCurrencyCode | CURRENCY_CODE | — | ✅ |
| 32 | JournalEntryLineCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 33 | JournalEntryLineCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 34 | JournalEntryLineCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 35 | JournalEntryLineDescription | DESCRIPTION | — | ✅ |
| 36 | JournalEntryLineDisplayedLineNumber | DISPLAYED_LINE_NUMBER | — | ✅ |
| 37 | JournalEntryLineEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | ✅ |
| 38 | JournalEntryLineEnteredCr | ENTERED_CR | — | ✅ |
| 39 | JournalEntryLineEnteredDr | ENTERED_DR | — | ✅ |
| 40 | JournalEntryLineFundsStatusCode | FUNDS_STATUS_CODE | — | ✅ |
| 41 | JournalEntryLineGainOrLossFlag | GAIN_OR_LOSS_FLAG | — | ✅ |
| 42 | JournalEntryLineGlSlLinkId | GL_SL_LINK_ID | — | ✅ |
| 43 | JournalEntryLineGlSlLinkTable | GL_SL_LINK_TABLE | — | ✅ |
| 44 | JournalEntryLineIntercompanyReversalFlag | INTERCOMPANY_REVERSAL_FLAG | — | ✅ |
| 45 | JournalEntryLineJgzzReconRef | JGZZ_RECON_REF | — | ✅ |
| 46 | JournalEntryLineJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 47 | JournalEntryLineJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 48 | JournalEntryLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | JournalEntryLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 50 | JournalEntryLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 51 | JournalEntryLineLedgerId | LEDGER_ID | — | ✅ |
| 52 | JournalEntryLineMergeCodeCombinationId | MERGE_CODE_COMBINATION_ID | — | ✅ |
| 53 | JournalEntryLineMergePartyId | MERGE_PARTY_ID | — | ✅ |
| 54 | JournalEntryLineMergePartySiteId | MERGE_PARTY_SITE_ID | — | ✅ |
| 55 | JournalEntryLineMpaAccrualEntryFlag | MPA_ACCRUAL_ENTRY_FLAG | — | ✅ |
| 56 | JournalEntryLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 57 | JournalEntryLineOverriddenCodeCombinationId | OVERRIDDEN_CODE_COMBINATION_ID | — | ✅ |
| 58 | JournalEntryLineOverrideReason | OVERRIDE_REASON | — | ✅ |
| 59 | JournalEntryLinePartyId | PARTY_ID | — | ✅ |
| 60 | JournalEntryLinePartySiteId | PARTY_SITE_ID | — | ✅ |
| 61 | JournalEntryLinePartyTypeCode | PARTY_TYPE_CODE | — | ✅ |
| 62 | JournalEntryLinePeriodName | PERIOD_NAME | — | ✅ |
| 63 | JournalEntryLineRequestId | REQUEST_ID | — | ✅ |
| 64 | JournalEntryLineSourceId | SOURCE_ID | — | ✅ |
| 65 | JournalEntryLineSr1 | SR1 | — | ✅ |
| 66 | JournalEntryLineSr10 | SR10 | — | ✅ |
| 67 | JournalEntryLineSr11 | SR11 | — | ✅ |
| 68 | JournalEntryLineSr12 | SR12 | — | ✅ |
| 69 | JournalEntryLineSr13 | SR13 | — | ✅ |
| 70 | JournalEntryLineSr14 | SR14 | — | ✅ |
| 71 | JournalEntryLineSr15 | SR15 | — | ✅ |
| 72 | JournalEntryLineSr16 | SR16 | — | ✅ |
| 73 | JournalEntryLineSr17 | SR17 | — | ✅ |
| 74 | JournalEntryLineSr18 | SR18 | — | ✅ |
| 75 | JournalEntryLineSr19 | SR19 | — | ✅ |
| 76 | JournalEntryLineSr2 | SR2 | — | ✅ |
| 77 | JournalEntryLineSr20 | SR20 | — | ✅ |
| 78 | JournalEntryLineSr21 | SR21 | — | ✅ |
| 79 | JournalEntryLineSr22 | SR22 | — | ✅ |
| 80 | JournalEntryLineSr23 | SR23 | — | ✅ |
| 81 | JournalEntryLineSr24 | SR24 | — | ✅ |
| 82 | JournalEntryLineSr25 | SR25 | — | ✅ |
| 83 | JournalEntryLineSr26 | SR26 | — | ✅ |
| 84 | JournalEntryLineSr27 | SR27 | — | ✅ |
| 85 | JournalEntryLineSr28 | SR28 | — | ✅ |
| 86 | JournalEntryLineSr29 | SR29 | — | ✅ |
| 87 | JournalEntryLineSr3 | SR3 | — | ✅ |
| 88 | JournalEntryLineSr30 | SR30 | — | ✅ |
| 89 | JournalEntryLineSr31 | SR31 | — | ✅ |
| 90 | JournalEntryLineSr32 | SR32 | — | ✅ |
| 91 | JournalEntryLineSr33 | SR33 | — | ✅ |
| 92 | JournalEntryLineSr34 | SR34 | — | ✅ |
| 93 | JournalEntryLineSr35 | SR35 | — | ✅ |
| 94 | JournalEntryLineSr36 | SR36 | — | ✅ |
| 95 | JournalEntryLineSr37 | SR37 | — | ✅ |
| 96 | JournalEntryLineSr38 | SR38 | — | ✅ |
| 97 | JournalEntryLineSr39 | SR39 | — | ✅ |
| 98 | JournalEntryLineSr4 | SR4 | — | ✅ |
| 99 | JournalEntryLineSr40 | SR40 | — | ✅ |
| 100 | JournalEntryLineSr41 | SR41 | — | ✅ |
| 101 | JournalEntryLineSr42 | SR42 | — | ✅ |
| 102 | JournalEntryLineSr43 | SR43 | — | ✅ |
| 103 | JournalEntryLineSr44 | SR44 | — | ✅ |
| 104 | JournalEntryLineSr45 | SR45 | — | ✅ |
| 105 | JournalEntryLineSr46 | SR46 | — | ✅ |
| 106 | JournalEntryLineSr47 | SR47 | — | ✅ |
| 107 | JournalEntryLineSr48 | SR48 | — | ✅ |
| 108 | JournalEntryLineSr49 | SR49 | — | ✅ |
| 109 | JournalEntryLineSr5 | SR5 | — | ✅ |
| 110 | JournalEntryLineSr50 | SR50 | — | ✅ |
| 111 | JournalEntryLineSr51 | SR51 | — | ✅ |
| 112 | JournalEntryLineSr52 | SR52 | — | ✅ |
| 113 | JournalEntryLineSr53 | SR53 | — | ✅ |
| 114 | JournalEntryLineSr54 | SR54 | — | ✅ |
| 115 | JournalEntryLineSr55 | SR55 | — | ✅ |
| 116 | JournalEntryLineSr56 | SR56 | — | ✅ |
| 117 | JournalEntryLineSr57 | SR57 | — | ✅ |
| 118 | JournalEntryLineSr58 | SR58 | — | ✅ |
| 119 | JournalEntryLineSr59 | SR59 | — | ✅ |
| 120 | JournalEntryLineSr6 | SR6 | — | ✅ |
| 121 | JournalEntryLineSr60 | SR60 | — | ✅ |
| 122 | JournalEntryLineSr7 | SR7 | — | ✅ |
| 123 | JournalEntryLineSr8 | SR8 | — | ✅ |
| 124 | JournalEntryLineSr9 | SR9 | — | ✅ |
| 125 | JournalEntryLineStatisticalAmount | STATISTICAL_AMOUNT | — | ✅ |
| 126 | JournalEntryLineSubledgerXccCompleteStatus | SUBLEDGER_XCC_COMPLETE_STATUS | — | ✅ |
| 127 | JournalEntryLineSubstitutedCcid | SUBSTITUTED_CCID | — | ✅ |
| 128 | JournalEntryLineSuppRefCombinationId | SUPP_REF_COMBINATION_ID | — | ✅ |
| 129 | JournalEntryLineSuppRefValues | SUPP_REF_VALUES | — | ✅ |
| 130 | JournalEntryLineUnroundedAccountedCr | UNROUNDED_ACCOUNTED_CR | — | ✅ |
| 131 | JournalEntryLineUnroundedAccountedDr | UNROUNDED_ACCOUNTED_DR | — | ✅ |
| 132 | JournalEntryLineUnroundedEnteredCr | UNROUNDED_ENTERED_CR | — | ✅ |
| 133 | JournalEntryLineUnroundedEnteredDr | UNROUNDED_ENTERED_DR | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
