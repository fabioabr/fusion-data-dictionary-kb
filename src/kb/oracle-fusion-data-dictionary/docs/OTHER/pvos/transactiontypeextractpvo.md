---
id: DOC-OTHER-PVO-TransactionTypeExtractPVO
doc_type: system-doc
title: "TransactionTypeExtractPVO — PVO Cross-Module"
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
  - TransactionTypeExtractPVO
  - transactiontypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Type Extract. Acessa as tabelas: RA_CUST_TRX_TYPES_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.TransactionTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 88 | 1 | 1 | 41 | 47% |

---

## 🔗 Tabelas Relacionadas

- [[ra_cust_trx_types_all|RA_CUST_TRX_TYPES_ALL]] — 88 atributos (1 PKs, 41 BICC)

---

## ⚙️ Atributos

### [[ra_cust_trx_types_all|RA_CUST_TRX_TYPES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaCustTrxTypeAccountingAffectFlag | ACCOUNTING_AFFECT_FLAG | — | ✅ |
| 2 | RaCustTrxTypeAllocateTaxFreight | ALLOCATE_TAX_FREIGHT | — | ✅ |
| 3 | RaCustTrxTypeAllowFreightFlag | ALLOW_FREIGHT_FLAG | — | ✅ |
| 4 | RaCustTrxTypeAllowFutureAcctDateFlag | ALLOW_FUTURE_ACCT_DATE_FLAG | — | ✅ |
| 5 | RaCustTrxTypeAllowOverapplicationFlag | ALLOW_OVERAPPLICATION_FLAG | — | ✅ |
| 6 | RaCustTrxTypeAttribute1 | ATTRIBUTE1 | — | — |
| 7 | RaCustTrxTypeAttribute10 | ATTRIBUTE10 | — | — |
| 8 | RaCustTrxTypeAttribute11 | ATTRIBUTE11 | — | — |
| 9 | RaCustTrxTypeAttribute12 | ATTRIBUTE12 | — | — |
| 10 | RaCustTrxTypeAttribute13 | ATTRIBUTE13 | — | — |
| 11 | RaCustTrxTypeAttribute14 | ATTRIBUTE14 | — | — |
| 12 | RaCustTrxTypeAttribute15 | ATTRIBUTE15 | — | — |
| 13 | RaCustTrxTypeAttribute2 | ATTRIBUTE2 | — | — |
| 14 | RaCustTrxTypeAttribute3 | ATTRIBUTE3 | — | — |
| 15 | RaCustTrxTypeAttribute4 | ATTRIBUTE4 | — | — |
| 16 | RaCustTrxTypeAttribute5 | ATTRIBUTE5 | — | — |
| 17 | RaCustTrxTypeAttribute6 | ATTRIBUTE6 | — | — |
| 18 | RaCustTrxTypeAttribute7 | ATTRIBUTE7 | — | — |
| 19 | RaCustTrxTypeAttribute8 | ATTRIBUTE8 | — | — |
| 20 | RaCustTrxTypeAttribute9 | ATTRIBUTE9 | — | — |
| 21 | RaCustTrxTypeAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | RaCustTrxTypeControlCompletionLevelCode | CONTROL_COMPLETION_LEVEL_CODE | — | ✅ |
| 23 | RaCustTrxTypeCreatedBy | CREATED_BY | — | ✅ |
| 24 | RaCustTrxTypeCreationDate | CREATION_DATE | — | ✅ |
| 25 | RaCustTrxTypeCreationSign | CREATION_SIGN | — | ✅ |
| 26 | RaCustTrxTypeCreditMemoTypeId | CREDIT_MEMO_TYPE_ID | — | ✅ |
| 27 | RaCustTrxTypeCreditMemoTypeSeqId | CREDIT_MEMO_TYPE_SEQ_ID | — | ✅ |
| 28 | RaCustTrxTypeCustTrxTypeId | CUST_TRX_TYPE_ID | — | ✅ |
| 29 | RaCustTrxTypeCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | 🔑 | ✅ |
| 30 | RaCustTrxTypeDefaultPrintingOption | DEFAULT_PRINTING_OPTION | — | ✅ |
| 31 | RaCustTrxTypeDefaultStatus | DEFAULT_STATUS | — | ✅ |
| 32 | RaCustTrxTypeDefaultTerm | DEFAULT_TERM | — | ✅ |
| 33 | RaCustTrxTypeDescription | DESCRIPTION | — | ✅ |
| 34 | RaCustTrxTypeDocumentType | DOCUMENT_TYPE | — | ✅ |
| 35 | RaCustTrxTypeDraweeIssuedFlag | DRAWEE_ISSUED_FLAG | — | ✅ |
| 36 | RaCustTrxTypeEndDate | END_DATE | — | ✅ |
| 37 | RaCustTrxTypeExcludeFromLateCharges | EXCLUDE_FROM_LATE_CHARGES | — | ✅ |
| 38 | RaCustTrxTypeFormatProgramId | FORMAT_PROGRAM_ID | — | ✅ |
| 39 | RaCustTrxTypeGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 40 | RaCustTrxTypeGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 41 | RaCustTrxTypeGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 42 | RaCustTrxTypeGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 43 | RaCustTrxTypeGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 44 | RaCustTrxTypeGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 45 | RaCustTrxTypeGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 46 | RaCustTrxTypeGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 47 | RaCustTrxTypeGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 48 | RaCustTrxTypeGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 49 | RaCustTrxTypeGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 50 | RaCustTrxTypeGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 51 | RaCustTrxTypeGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 52 | RaCustTrxTypeGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 53 | RaCustTrxTypeGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 54 | RaCustTrxTypeGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 55 | RaCustTrxTypeGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 56 | RaCustTrxTypeGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 57 | RaCustTrxTypeGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 58 | RaCustTrxTypeGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 59 | RaCustTrxTypeGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 60 | RaCustTrxTypeGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 61 | RaCustTrxTypeGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 62 | RaCustTrxTypeGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 63 | RaCustTrxTypeGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 64 | RaCustTrxTypeGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 65 | RaCustTrxTypeGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 66 | RaCustTrxTypeGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 67 | RaCustTrxTypeGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 68 | RaCustTrxTypeGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 69 | RaCustTrxTypeGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 70 | RaCustTrxTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 71 | RaCustTrxTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 72 | RaCustTrxTypeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 73 | RaCustTrxTypeLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 74 | RaCustTrxTypeMagneticFormatCode | MAGNETIC_FORMAT_CODE | — | ✅ |
| 75 | RaCustTrxTypeName | NAME | — | ✅ |
| 76 | RaCustTrxTypeNaturalApplicationOnlyFlag | NATURAL_APPLICATION_ONLY_FLAG | — | ✅ |
| 77 | RaCustTrxTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 78 | RaCustTrxTypePostToGl | POST_TO_GL | — | ✅ |
| 79 | RaCustTrxTypeRuleSetId | RULE_SET_ID | — | ✅ |
| 80 | RaCustTrxTypeSetId | SET_ID | — | ✅ |
| 81 | RaCustTrxTypeSignedFlag | SIGNED_FLAG | — | ✅ |
| 82 | RaCustTrxTypeStartDate | START_DATE | — | ✅ |
| 83 | RaCustTrxTypeStatus | STATUS | — | ✅ |
| 84 | RaCustTrxTypeSubsequentTrxTypeId | SUBSEQUENT_TRX_TYPE_ID | — | ✅ |
| 85 | RaCustTrxTypeSubsequentTrxTypeSeqId | SUBSEQUENT_TRX_TYPE_SEQ_ID | — | ✅ |
| 86 | RaCustTrxTypeTaxCalculationFlag | TAX_CALCULATION_FLAG | — | ✅ |
| 87 | RaCustTrxTypeType | TYPE | — | ✅ |
| 88 | RaCustTrxTypeUsageCategoryCode | USAGE_CATEGORY_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
