---
id: DOC-OTHER-PVO-SubledgerJournalDistributionExtractPVO
doc_type: system-doc
title: "SubledgerJournalDistributionExtractPVO — PVO Cross-Module"
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
  - SubledgerJournalDistributionExtractPVO
  - subledgerjournaldistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerJournalDistributionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Journal Distribution Extract. Acessa as tabelas: XLA_DISTRIBUTION_LINKS.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SubledgerJournalDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 92 | 1 | 4 | 92 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_distribution_links|XLA_DISTRIBUTION_LINKS]] — 92 atributos (4 PKs, 92 BICC)

---

## ⚙️ Atributos

### [[xla_distribution_links|XLA_DISTRIBUTION_LINKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalEntryDistributionAccountingLineCode | ACCOUNTING_LINE_CODE | — | ✅ |
| 2 | JournalEntryDistributionAccountingLineTypeCode | ACCOUNTING_LINE_TYPE_CODE | — | ✅ |
| 3 | JournalEntryDistributionAeHeaderId | AE_HEADER_ID | 🔑 | ✅ |
| 4 | JournalEntryDistributionAeLineNum | AE_LINE_NUM | — | ✅ |
| 5 | JournalEntryDistributionAllocToApplicationId | ALLOC_TO_APPLICATION_ID | — | ✅ |
| 6 | JournalEntryDistributionAllocToDistIdChar1 | ALLOC_TO_DIST_ID_CHAR_1 | — | ✅ |
| 7 | JournalEntryDistributionAllocToDistIdChar2 | ALLOC_TO_DIST_ID_CHAR_2 | — | ✅ |
| 8 | JournalEntryDistributionAllocToDistIdChar3 | ALLOC_TO_DIST_ID_CHAR_3 | — | ✅ |
| 9 | JournalEntryDistributionAllocToDistIdChar4 | ALLOC_TO_DIST_ID_CHAR_4 | — | ✅ |
| 10 | JournalEntryDistributionAllocToDistIdChar5 | ALLOC_TO_DIST_ID_CHAR_5 | — | ✅ |
| 11 | JournalEntryDistributionAllocToDistIdNum1 | ALLOC_TO_DIST_ID_NUM_1 | — | ✅ |
| 12 | JournalEntryDistributionAllocToDistIdNum2 | ALLOC_TO_DIST_ID_NUM_2 | — | ✅ |
| 13 | JournalEntryDistributionAllocToDistIdNum3 | ALLOC_TO_DIST_ID_NUM_3 | — | ✅ |
| 14 | JournalEntryDistributionAllocToDistIdNum4 | ALLOC_TO_DIST_ID_NUM_4 | — | ✅ |
| 15 | JournalEntryDistributionAllocToDistIdNum5 | ALLOC_TO_DIST_ID_NUM_5 | — | ✅ |
| 16 | JournalEntryDistributionAllocToDistributionType | ALLOC_TO_DISTRIBUTION_TYPE | — | ✅ |
| 17 | JournalEntryDistributionAllocToEntityCode | ALLOC_TO_ENTITY_CODE | — | ✅ |
| 18 | JournalEntryDistributionAllocToSourceIdChar1 | ALLOC_TO_SOURCE_ID_CHAR_1 | — | ✅ |
| 19 | JournalEntryDistributionAllocToSourceIdChar2 | ALLOC_TO_SOURCE_ID_CHAR_2 | — | ✅ |
| 20 | JournalEntryDistributionAllocToSourceIdChar3 | ALLOC_TO_SOURCE_ID_CHAR_3 | — | ✅ |
| 21 | JournalEntryDistributionAllocToSourceIdChar4 | ALLOC_TO_SOURCE_ID_CHAR_4 | — | ✅ |
| 22 | JournalEntryDistributionAllocToSourceIdNum1 | ALLOC_TO_SOURCE_ID_NUM_1 | — | ✅ |
| 23 | JournalEntryDistributionAllocToSourceIdNum2 | ALLOC_TO_SOURCE_ID_NUM_2 | — | ✅ |
| 24 | JournalEntryDistributionAllocToSourceIdNum3 | ALLOC_TO_SOURCE_ID_NUM_3 | — | ✅ |
| 25 | JournalEntryDistributionAllocToSourceIdNum4 | ALLOC_TO_SOURCE_ID_NUM_4 | — | ✅ |
| 26 | JournalEntryDistributionApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 27 | JournalEntryDistributionAppliedToApplicationId | APPLIED_TO_APPLICATION_ID | — | ✅ |
| 28 | JournalEntryDistributionAppliedToDistIdChar1 | APPLIED_TO_DIST_ID_CHAR_1 | — | ✅ |
| 29 | JournalEntryDistributionAppliedToDistIdChar2 | APPLIED_TO_DIST_ID_CHAR_2 | — | ✅ |
| 30 | JournalEntryDistributionAppliedToDistIdChar3 | APPLIED_TO_DIST_ID_CHAR_3 | — | ✅ |
| 31 | JournalEntryDistributionAppliedToDistIdChar4 | APPLIED_TO_DIST_ID_CHAR_4 | — | ✅ |
| 32 | JournalEntryDistributionAppliedToDistIdChar5 | APPLIED_TO_DIST_ID_CHAR_5 | — | ✅ |
| 33 | JournalEntryDistributionAppliedToDistIdNum1 | APPLIED_TO_DIST_ID_NUM_1 | — | ✅ |
| 34 | JournalEntryDistributionAppliedToDistIdNum2 | APPLIED_TO_DIST_ID_NUM_2 | — | ✅ |
| 35 | JournalEntryDistributionAppliedToDistIdNum3 | APPLIED_TO_DIST_ID_NUM_3 | — | ✅ |
| 36 | JournalEntryDistributionAppliedToDistIdNum4 | APPLIED_TO_DIST_ID_NUM_4 | — | ✅ |
| 37 | JournalEntryDistributionAppliedToDistIdNum5 | APPLIED_TO_DIST_ID_NUM_5 | — | ✅ |
| 38 | JournalEntryDistributionAppliedToDistributionType | APPLIED_TO_DISTRIBUTION_TYPE | — | ✅ |
| 39 | JournalEntryDistributionAppliedToEntityCode | APPLIED_TO_ENTITY_CODE | — | ✅ |
| 40 | JournalEntryDistributionAppliedToEntityId | APPLIED_TO_ENTITY_ID | — | ✅ |
| 41 | JournalEntryDistributionAppliedToSourceIdChar1 | APPLIED_TO_SOURCE_ID_CHAR_1 | — | ✅ |
| 42 | JournalEntryDistributionAppliedToSourceIdChar2 | APPLIED_TO_SOURCE_ID_CHAR_2 | — | ✅ |
| 43 | JournalEntryDistributionAppliedToSourceIdChar3 | APPLIED_TO_SOURCE_ID_CHAR_3 | — | ✅ |
| 44 | JournalEntryDistributionAppliedToSourceIdChar4 | APPLIED_TO_SOURCE_ID_CHAR_4 | — | ✅ |
| 45 | JournalEntryDistributionAppliedToSourceIdNum1 | APPLIED_TO_SOURCE_ID_NUM_1 | — | ✅ |
| 46 | JournalEntryDistributionAppliedToSourceIdNum2 | APPLIED_TO_SOURCE_ID_NUM_2 | — | ✅ |
| 47 | JournalEntryDistributionAppliedToSourceIdNum3 | APPLIED_TO_SOURCE_ID_NUM_3 | — | ✅ |
| 48 | JournalEntryDistributionAppliedToSourceIdNum4 | APPLIED_TO_SOURCE_ID_NUM_4 | — | ✅ |
| 49 | JournalEntryDistributionCalculateAcctdAmtsFlag | CALCULATE_ACCTD_AMTS_FLAG | — | ✅ |
| 50 | JournalEntryDistributionCalculateGLAmtsFlag | CALCULATE_G_L_AMTS_FLAG | — | ✅ |
| 51 | JournalEntryDistributionCreatedBy | CREATED_BY | — | ✅ |
| 52 | JournalEntryDistributionCreationDate | CREATION_DATE | — | ✅ |
| 53 | JournalEntryDistributionDocRoundingAcctdAmt | DOC_ROUNDING_ACCTD_AMT | — | ✅ |
| 54 | JournalEntryDistributionDocRoundingEnteredAmt | DOC_ROUNDING_ENTERED_AMT | — | ✅ |
| 55 | JournalEntryDistributionDocumentRoundingLevel | DOCUMENT_ROUNDING_LEVEL | — | ✅ |
| 56 | JournalEntryDistributionEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 57 | JournalEntryDistributionEventId | EVENT_ID | — | ✅ |
| 58 | JournalEntryDistributionEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 59 | JournalEntryDistributionGainOrLossRef | GAIN_OR_LOSS_REF | — | ✅ |
| 60 | JournalEntryDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | JournalEntryDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 62 | JournalEntryDistributionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 63 | JournalEntryDistributionLineDefinitionCode | LINE_DEFINITION_CODE | — | ✅ |
| 64 | JournalEntryDistributionLineDefinitionOwnerCode | LINE_DEFINITION_OWNER_CODE | — | ✅ |
| 65 | JournalEntryDistributionMergeDuplicateCode | MERGE_DUPLICATE_CODE | — | ✅ |
| 66 | JournalEntryDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 67 | JournalEntryDistributionRefAeHeaderId | REF_AE_HEADER_ID | 🔑 | ✅ |
| 68 | JournalEntryDistributionRefAeLineNum | REF_AE_LINE_NUM | — | ✅ |
| 69 | JournalEntryDistributionRefEventId | REF_EVENT_ID | — | ✅ |
| 70 | JournalEntryDistributionRefTempLineNum | REF_TEMP_LINE_NUM | — | ✅ |
| 71 | JournalEntryDistributionRoundingClassCode | ROUNDING_CLASS_CODE | — | ✅ |
| 72 | JournalEntryDistributionSourceDistributionIdChar1 | SOURCE_DISTRIBUTION_ID_CHAR_1 | — | ✅ |
| 73 | JournalEntryDistributionSourceDistributionIdChar2 | SOURCE_DISTRIBUTION_ID_CHAR_2 | — | ✅ |
| 74 | JournalEntryDistributionSourceDistributionIdChar3 | SOURCE_DISTRIBUTION_ID_CHAR_3 | — | ✅ |
| 75 | JournalEntryDistributionSourceDistributionIdChar4 | SOURCE_DISTRIBUTION_ID_CHAR_4 | — | ✅ |
| 76 | JournalEntryDistributionSourceDistributionIdChar5 | SOURCE_DISTRIBUTION_ID_CHAR_5 | — | ✅ |
| 77 | JournalEntryDistributionSourceDistributionIdNum1 | SOURCE_DISTRIBUTION_ID_NUM_1 | — | ✅ |
| 78 | JournalEntryDistributionSourceDistributionIdNum2 | SOURCE_DISTRIBUTION_ID_NUM_2 | — | ✅ |
| 79 | JournalEntryDistributionSourceDistributionIdNum3 | SOURCE_DISTRIBUTION_ID_NUM_3 | — | ✅ |
| 80 | JournalEntryDistributionSourceDistributionIdNum4 | SOURCE_DISTRIBUTION_ID_NUM_4 | — | ✅ |
| 81 | JournalEntryDistributionSourceDistributionIdNum5 | SOURCE_DISTRIBUTION_ID_NUM_5 | — | ✅ |
| 82 | JournalEntryDistributionSourceDistributionType | SOURCE_DISTRIBUTION_TYPE | — | ✅ |
| 83 | JournalEntryDistributionStatisticalAmount | STATISTICAL_AMOUNT | — | ✅ |
| 84 | JournalEntryDistributionTaxLineRefId | TAX_LINE_REF_ID | — | ✅ |
| 85 | JournalEntryDistributionTaxRecNrecDistRefId | TAX_REC_NREC_DIST_REF_ID | — | ✅ |
| 86 | JournalEntryDistributionTaxSummaryLineRefId | TAX_SUMMARY_LINE_REF_ID | — | ✅ |
| 87 | JournalEntryDistributionTempLineNum | TEMP_LINE_NUM | 🔑 | ✅ |
| 88 | JournalEntryDistributionUnroundedAccountedCr | UNROUNDED_ACCOUNTED_CR | — | ✅ |
| 89 | JournalEntryDistributionUnroundedAccountedDr | UNROUNDED_ACCOUNTED_DR | — | ✅ |
| 90 | JournalEntryDistributionUnroundedEnteredCr | UNROUNDED_ENTERED_CR | — | ✅ |
| 91 | JournalEntryDistributionUnroundedEnteredDr | UNROUNDED_ENTERED_DR | — | ✅ |
| 92 | JournalEntryDistributionUpgBatchId | UPG_BATCH_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
