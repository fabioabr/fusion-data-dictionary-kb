---
id: DOC-AR-PVO-TransactionTypePVO
doc_type: system-doc
title: "TransactionTypePVO — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - TransactionTypePVO
  - transactiontypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionTypePVO

## 📌 Visão Geral

Extrai os tipos de transação configurados em Contas a Receber (fatura, nota de crédito, nota de débito, depósito), com regras de contabilização e comportamento. Define a parametrização que controla o fluxo contábil e operacional de cada classe de transação.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.TransactionTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 53 | 2 | 1 | 23 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[ar_lookups|AR_LOOKUPS]] — 13 atributos (4 BICC)
- [[ra_cust_trx_types_all|RA_CUST_TRX_TYPES_ALL]] — 40 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[ar_lookups|AR_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArLookupCreatedBy | CREATED_BY | — | — |
| 2 | ArLookupCreationDate | CREATION_DATE | — | ✅ |
| 3 | ArLookupDescription | DESCRIPTION | — | ✅ |
| 4 | ArLookupEnabledFlag | ENABLED_FLAG | — | — |
| 5 | ArLookupEndDateActive | END_DATE_ACTIVE | — | — |
| 6 | ArLookupLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ArLookupLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ArLookupLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ArLookupLookupCode | LOOKUP_CODE | — | — |
| 10 | ArLookupLookupType | LOOKUP_TYPE | — | — |
| 11 | ArLookupMeaning | MEANING | — | ✅ |
| 12 | ArLookupStartDateActive | START_DATE_ACTIVE | — | — |
| 13 | ArLookupTag | TAG | — | — |

### [[ra_cust_trx_types_all|RA_CUST_TRX_TYPES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | 🔑 | ✅ |
| 2 | TransactionTypeAccountingAffectFlag | ACCOUNTING_AFFECT_FLAG | — | ✅ |
| 3 | TransactionTypeAllocateTaxFreight | ALLOCATE_TAX_FREIGHT | — | ✅ |
| 4 | TransactionTypeAllowFreightFlag | ALLOW_FREIGHT_FLAG | — | — |
| 5 | TransactionTypeAllowOverapplicationFlag | ALLOW_OVERAPPLICATION_FLAG | — | ✅ |
| 6 | TransactionTypeControlCompletionLevelCode | CONTROL_COMPLETION_LEVEL_CODE | — | — |
| 7 | TransactionTypeCreatedBy | CREATED_BY | — | ✅ |
| 8 | TransactionTypeCreationDate | CREATION_DATE | — | ✅ |
| 9 | TransactionTypeCreationSign | CREATION_SIGN | — | ✅ |
| 10 | TransactionTypeCreditMemoTypeId | CREDIT_MEMO_TYPE_ID | — | — |
| 11 | TransactionTypeCreditMemoTypeSeqId | CREDIT_MEMO_TYPE_SEQ_ID | — | — |
| 12 | TransactionTypeCustTrxTypeId | CUST_TRX_TYPE_ID | — | ✅ |
| 13 | TransactionTypeDefaultPrintingOption | DEFAULT_PRINTING_OPTION | — | — |
| 14 | TransactionTypeDefaultStatus | DEFAULT_STATUS | — | — |
| 15 | TransactionTypeDefaultTerm | DEFAULT_TERM | — | — |
| 16 | TransactionTypeDescription | DESCRIPTION | — | ✅ |
| 17 | TransactionTypeDocumentType | DOCUMENT_TYPE | — | — |
| 18 | TransactionTypeDraweeIssuedFlag | DRAWEE_ISSUED_FLAG | — | ✅ |
| 19 | TransactionTypeEndDate | END_DATE | — | — |
| 20 | TransactionTypeExcludeFromLateCharges | EXCLUDE_FROM_LATE_CHARGES | — | — |
| 21 | TransactionTypeFormatProgramId | FORMAT_PROGRAM_ID | — | — |
| 22 | TransactionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | TransactionTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | TransactionTypeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | TransactionTypeLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 26 | TransactionTypeMagneticFormatCode | MAGNETIC_FORMAT_CODE | — | — |
| 27 | TransactionTypeName | NAME | — | ✅ |
| 28 | TransactionTypeNaturalApplicationOnlyFlag | NATURAL_APPLICATION_ONLY_FLAG | — | ✅ |
| 29 | TransactionTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 30 | TransactionTypePostToGl | POST_TO_GL | — | ✅ |
| 31 | TransactionTypeRuleSetId | RULE_SET_ID | — | — |
| 32 | TransactionTypeSetId | SET_ID | — | — |
| 33 | TransactionTypeSignedFlag | SIGNED_FLAG | — | ✅ |
| 34 | TransactionTypeStartDate | START_DATE | — | — |
| 35 | TransactionTypeStatus | STATUS | — | — |
| 36 | TransactionTypeSubsequentTrxTypeId | SUBSEQUENT_TRX_TYPE_ID | — | ✅ |
| 37 | TransactionTypeSubsequentTrxTypeSeqId | SUBSEQUENT_TRX_TYPE_SEQ_ID | — | — |
| 38 | TransactionTypeTaxCalculationFlag | TAX_CALCULATION_FLAG | — | ✅ |
| 39 | TransactionTypeType | TYPE | — | ✅ |
| 40 | TransactionTypeUsageCategoryCode | USAGE_CATEGORY_CODE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
