---
id: DOC-OTHER-PVO-JournalHeaderExtractPVO
doc_type: system-doc
title: "JournalHeaderExtractPVO — PVO Cross-Module"
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
  - JournalHeaderExtractPVO
  - journalheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Header Extract. Acessa as tabelas: FUN_SEQ_VERSIONS, GL_ENCUMBRANCE_TYPES_TL, GL_JE_BATCHES (+1).

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.JournalHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 123 | 4 | 1 | 54 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[fun_seq_versions|FUN_SEQ_VERSIONS]] — 6 atributos
- [[gl_encumbrance_types_tl|GL_ENCUMBRANCE_TYPES_TL]] — 4 atributos
- [[gl_je_batches|GL_JE_BATCHES]] — 3 atributos
- [[gl_je_headers|GL_JE_HEADERS]] — 110 atributos (1 PKs, 54 BICC)

---

## ⚙️ Atributos

### [[fun_seq_versions|FUN_SEQ_VERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CloseAcctSeqVersionsHeaderName | HEADER_NAME | — | — |
| 2 | CloseAcctSeqVersionsSeqVersionId | SEQ_VERSION_ID | — | — |
| 3 | CloseAcctSeqVersionsVersionName | VERSION_NAME | — | — |
| 4 | PostAcctSeqVersionsHeaderName | HEADER_NAME | — | — |
| 5 | PostAcctSeqVersionsSeqVersionId | SEQ_VERSION_ID | — | — |
| 6 | PostAcctSeqVersionsVersionName | VERSION_NAME | — | — |

### [[gl_encumbrance_types_tl|GL_ENCUMBRANCE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalEncumbranceTLDescription | DESCRIPTION | — | — |
| 2 | JournalEncumbranceTLEncumbranceType | ENCUMBRANCE_TYPE | — | — |
| 3 | JournalEncumbranceTLEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | — |
| 4 | JournalEncumbranceTLLanguage | LANGUAGE | — | — |

### [[gl_je_batches|GL_JE_BATCHES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlJeBatchesDescription | DESCRIPTION | — | — |
| 2 | GlJeBatchesJeBatchId | JE_BATCH_ID | — | — |
| 3 | GlJeBatchesName | NAME | — | — |

### [[gl_je_headers|GL_JE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlJeHeadersAccrualRevChangeSignFlag | ACCRUAL_REV_CHANGE_SIGN_FLAG | — | ✅ |
| 2 | GlJeHeadersAccrualRevEffectiveDate | ACCRUAL_REV_EFFECTIVE_DATE | — | ✅ |
| 3 | GlJeHeadersAccrualRevFlag | ACCRUAL_REV_FLAG | — | — |
| 4 | GlJeHeadersAccrualRevJeHeaderId | ACCRUAL_REV_JE_HEADER_ID | — | ✅ |
| 5 | GlJeHeadersAccrualRevPeriodName | ACCRUAL_REV_PERIOD_NAME | — | ✅ |
| 6 | GlJeHeadersAccrualRevStatus | ACCRUAL_REV_STATUS | — | ✅ |
| 7 | GlJeHeadersActualFlag | ACTUAL_FLAG | — | ✅ |
| 8 | GlJeHeadersAttribute1 | ATTRIBUTE1 | — | — |
| 9 | GlJeHeadersAttribute10 | ATTRIBUTE10 | — | — |
| 10 | GlJeHeadersAttribute2 | ATTRIBUTE2 | — | — |
| 11 | GlJeHeadersAttribute3 | ATTRIBUTE3 | — | — |
| 12 | GlJeHeadersAttribute4 | ATTRIBUTE4 | — | — |
| 13 | GlJeHeadersAttribute5 | ATTRIBUTE5 | — | — |
| 14 | GlJeHeadersAttribute6 | ATTRIBUTE6 | — | — |
| 15 | GlJeHeadersAttribute7 | ATTRIBUTE7 | — | — |
| 16 | GlJeHeadersAttribute8 | ATTRIBUTE8 | — | — |
| 17 | GlJeHeadersAttribute9 | ATTRIBUTE9 | — | — |
| 18 | GlJeHeadersAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | GlJeHeadersAttributeCategory2 | ATTRIBUTE_CATEGORY2 | — | — |
| 20 | GlJeHeadersAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 21 | GlJeHeadersAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 22 | GlJeHeadersAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 23 | GlJeHeadersAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 24 | GlJeHeadersAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 25 | GlJeHeadersAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 26 | GlJeHeadersAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 27 | GlJeHeadersAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 28 | GlJeHeadersAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 29 | GlJeHeadersAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 30 | GlJeHeadersBalancedJeFlag | BALANCED_JE_FLAG | — | ✅ |
| 31 | GlJeHeadersCloseAcctSeqAssignId | CLOSE_ACCT_SEQ_ASSIGN_ID | — | ✅ |
| 32 | GlJeHeadersCloseAcctSeqValue | CLOSE_ACCT_SEQ_VALUE | — | ✅ |
| 33 | GlJeHeadersCloseAcctSeqVersionId | CLOSE_ACCT_SEQ_VERSION_ID | — | ✅ |
| 34 | GlJeHeadersControlTotal | CONTROL_TOTAL | — | ✅ |
| 35 | GlJeHeadersCreatedBy | CREATED_BY | — | ✅ |
| 36 | GlJeHeadersCreationDate | CREATION_DATE | — | ✅ |
| 37 | GlJeHeadersCurrencyCode | CURRENCY_CODE | — | ✅ |
| 38 | GlJeHeadersCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 39 | GlJeHeadersCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 40 | GlJeHeadersCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 41 | GlJeHeadersDateCreated | DATE_CREATED | — | ✅ |
| 42 | GlJeHeadersDefaultEffectiveDate | DEFAULT_EFFECTIVE_DATE | — | ✅ |
| 43 | GlJeHeadersDescription | DESCRIPTION | — | ✅ |
| 44 | GlJeHeadersDisplayAlcJournalFlag | DISPLAY_ALC_JOURNAL_FLAG | — | ✅ |
| 45 | GlJeHeadersEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | ✅ |
| 46 | GlJeHeadersExternalReference | EXTERNAL_REFERENCE | — | ✅ |
| 47 | GlJeHeadersGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 48 | GlJeHeadersGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 49 | GlJeHeadersGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 50 | GlJeHeadersGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 51 | GlJeHeadersGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 52 | GlJeHeadersGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 53 | GlJeHeadersGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 54 | GlJeHeadersGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 55 | GlJeHeadersGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 56 | GlJeHeadersGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 57 | GlJeHeadersGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 58 | GlJeHeadersGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 59 | GlJeHeadersGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 60 | GlJeHeadersGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 61 | GlJeHeadersGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 62 | GlJeHeadersGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 63 | GlJeHeadersGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 64 | GlJeHeadersGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 65 | GlJeHeadersGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 66 | GlJeHeadersGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 67 | GlJeHeadersGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 68 | GlJeHeadersGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 69 | GlJeHeadersGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 70 | GlJeHeadersGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 71 | GlJeHeadersGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 72 | GlJeHeadersGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 73 | GlJeHeadersGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 74 | GlJeHeadersGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 75 | GlJeHeadersGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 76 | GlJeHeadersGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 77 | GlJeHeadersGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 78 | GlJeHeadersIntercompanyMode | INTERCOMPANY_MODE | — | ✅ |
| 79 | GlJeHeadersJeBatchId | JE_BATCH_ID | — | ✅ |
| 80 | GlJeHeadersJeCategory | JE_CATEGORY | — | ✅ |
| 81 | GlJeHeadersJeFromSlaFlag | JE_FROM_SLA_FLAG | — | ✅ |
| 82 | GlJeHeadersJeSource | JE_SOURCE | — | ✅ |
| 83 | GlJeHeadersLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 84 | GlJeHeadersLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 85 | GlJeHeadersLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 86 | GlJeHeadersLedgerId | LEDGER_ID | — | ✅ |
| 87 | GlJeHeadersLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 88 | GlJeHeadersMultiBalSegFlag | MULTI_BAL_SEG_FLAG | — | ✅ |
| 89 | GlJeHeadersMultiCurrencyFlag | MULTI_CURRENCY_FLAG | — | ✅ |
| 90 | GlJeHeadersName | NAME | — | ✅ |
| 91 | GlJeHeadersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 92 | GlJeHeadersOriginatingBalSegValue | ORIGINATING_BAL_SEG_VALUE | — | ✅ |
| 93 | GlJeHeadersParentJeHeaderId | PARENT_JE_HEADER_ID | — | ✅ |
| 94 | GlJeHeadersPeriodName | PERIOD_NAME | — | ✅ |
| 95 | GlJeHeadersPostCurrencyCode | POST_CURRENCY_CODE | — | ✅ |
| 96 | GlJeHeadersPostMultiCurrencyFlag | POST_MULTI_CURRENCY_FLAG | — | ✅ |
| 97 | GlJeHeadersPostedDate | POSTED_DATE | — | ✅ |
| 98 | GlJeHeadersPostingAcctSeqAssignId | POSTING_ACCT_SEQ_ASSIGN_ID | — | ✅ |
| 99 | GlJeHeadersPostingAcctSeqValue | POSTING_ACCT_SEQ_VALUE | — | ✅ |
| 100 | GlJeHeadersPostingAcctSeqVersionId | POSTING_ACCT_SEQ_VERSION_ID | — | ✅ |
| 101 | GlJeHeadersReferenceDate | REFERENCE_DATE | — | ✅ |
| 102 | GlJeHeadersReversedJeHeaderId | REVERSED_JE_HEADER_ID | — | ✅ |
| 103 | GlJeHeadersRunningTotalAccountedCr | RUNNING_TOTAL_ACCOUNTED_CR | — | ✅ |
| 104 | GlJeHeadersRunningTotalAccountedDr | RUNNING_TOTAL_ACCOUNTED_DR | — | ✅ |
| 105 | GlJeHeadersRunningTotalCr | RUNNING_TOTAL_CR | — | ✅ |
| 106 | GlJeHeadersRunningTotalDr | RUNNING_TOTAL_DR | — | ✅ |
| 107 | GlJeHeadersStatus | STATUS | — | ✅ |
| 108 | JeHeaderId | JE_HEADER_ID | 🔑 | ✅ |
| 109 | ReversalJournalHeaderJeHeaderId | JE_HEADER_ID | — | — |
| 110 | ReversalJournalHeaderName | NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
