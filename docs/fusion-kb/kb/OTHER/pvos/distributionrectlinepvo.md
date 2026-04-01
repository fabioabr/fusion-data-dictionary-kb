---
id: DOC-OTHER-PVO-DistributionRectLinePVO
doc_type: system-doc
title: "DistributionRectLinePVO — PVO Cross-Module"
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
  - DistributionRectLinePVO
  - distributionrectlinepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DistributionRectLinePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Distribution Rect Line. Acessa as tabelas: FUN_BATCH_DISTS, FUN_DIST_LINES, FUN_INTERCO_ORGANIZATIONS (+7).

**Caminho:** `FscmTopModelAM.FinFunIntercoTransactionsAM.DistributionRectLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 324 | 10 | 1 | 45 | 14% |

---

## 🔗 Tabelas Relacionadas

- [[fun_batch_dists|FUN_BATCH_DISTS]] — 12 atributos (1 BICC)
- [[fun_dist_lines|FUN_DIST_LINES]] — 19 atributos (1 PKs, 7 BICC)
- [[fun_interco_organizations|FUN_INTERCO_ORGANIZATIONS]] — 43 atributos (4 BICC)
- [[fun_lookups|FUN_LOOKUPS]] — 14 atributos (3 BICC)
- [[fun_trx_batches|FUN_TRX_BATCHES]] — 87 atributos (12 BICC)
- [[fun_trx_headers|FUN_TRX_HEADERS]] — 96 atributos (14 BICC)
- [[fun_trx_lines|FUN_TRX_LINES]] — 15 atributos (1 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 18 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[fun_batch_dists|FUN_BATCH_DISTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BatchDistributionBatchDistId | BATCH_DIST_ID | — | — |
| 2 | BatchDistributionBatchId | BATCH_ID | — | — |
| 3 | BatchDistributionCcid | CCID | — | — |
| 4 | BatchDistributionCreatedBy | CREATED_BY | — | — |
| 5 | BatchDistributionCreationDate | CREATION_DATE | — | — |
| 6 | BatchDistributionDescription | DESCRIPTION | — | — |
| 7 | BatchDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | BatchDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | BatchDistributionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | BatchDistributionLineNumber | LINE_NUMBER | — | — |
| 11 | BatchDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | BatchDistributionPercentage | PERCENTAGE | — | — |

### [[fun_dist_lines|FUN_DIST_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistId | DIST_ID | 🔑 | ✅ |
| 2 | DistributionLineAmountCr | AMOUNT_CR | — | ✅ |
| 3 | DistributionLineAmountDr | AMOUNT_DR | — | ✅ |
| 4 | DistributionLineAutoGenerateFlag | AUTO_GENERATE_FLAG | — | — |
| 5 | DistributionLineBatchDistId | BATCH_DIST_ID | — | — |
| 6 | DistributionLineCcid | CCID | — | — |
| 7 | DistributionLineCreatedBy | CREATED_BY | — | — |
| 8 | DistributionLineCreationDate | CREATION_DATE | — | — |
| 9 | DistributionLineDescription | DESCRIPTION | — | ✅ |
| 10 | DistributionLineDistNumber | DIST_NUMBER | — | ✅ |
| 11 | DistributionLineDistTypeFlag | DIST_TYPE_FLAG | — | — |
| 12 | DistributionLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | DistributionLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | DistributionLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | DistributionLineLineId | LINE_ID | — | — |
| 16 | DistributionLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | DistributionLinePartyId | PARTY_ID | — | — |
| 18 | DistributionLinePartyTypeFlag | PARTY_TYPE_FLAG | — | ✅ |
| 19 | DistributionLineTrxId | TRX_ID | — | — |

### [[fun_interco_organizations|FUN_INTERCO_ORGANIZATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IntercoOrgBatchInitIdContactPersonId | CONTACT_PERSON_ID | — | — |
| 2 | IntercoOrgBatchInitIdCreatedBy | CREATED_BY | — | — |
| 3 | IntercoOrgBatchInitIdCreationDate | CREATION_DATE | — | — |
| 4 | IntercoOrgBatchInitIdDescription | DESCRIPTION | — | — |
| 5 | IntercoOrgBatchInitIdEnabledFlag | ENABLED_FLAG | — | — |
| 6 | IntercoOrgBatchInitIdIntercoOrgId | INTERCO_ORG_ID | — | — |
| 7 | IntercoOrgBatchInitIdIntercoOrgName | INTERCO_ORG_NAME | — | ✅ |
| 8 | IntercoOrgBatchInitIdLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | IntercoOrgBatchInitIdLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | IntercoOrgBatchInitIdLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | IntercoOrgBatchInitIdLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 12 | IntercoOrgBatchInitIdObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | IntercoOrgBatchInitIdPayBuId | PAY_BU_ID | — | — |
| 14 | IntercoOrgBatchInitIdRecBuId | REC_BU_ID | — | — |
| 15 | IntercoOrgBatchInitIdRemoteInstanceFlag | REMOTE_INSTANCE_FLAG | — | — |
| 16 | IntercoOrgBatchInitIdRemoteInstanceIdentifier | REMOTE_INSTANCE_IDENTIFIER | — | — |
| 17 | IntercoOrgContactPersonId | CONTACT_PERSON_ID | — | — |
| 18 | IntercoOrgDescription | DESCRIPTION | — | — |
| 19 | IntercoOrgEnabledFlag | ENABLED_FLAG | — | — |
| 20 | IntercoOrgIntercoOrgId | INTERCO_ORG_ID | — | — |
| 21 | IntercoOrgIntercoOrgName | INTERCO_ORG_NAME | — | — |
| 22 | IntercoOrgLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 23 | IntercoOrgObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | IntercoOrgPayBuId | PAY_BU_ID | — | — |
| 25 | IntercoOrgRcptIdContactPersonId | CONTACT_PERSON_ID | — | — |
| 26 | IntercoOrgRcptIdCreatedBy | CREATED_BY | — | — |
| 27 | IntercoOrgRcptIdCreationDate | CREATION_DATE | — | — |
| 28 | IntercoOrgRcptIdDescription | DESCRIPTION | — | — |
| 29 | IntercoOrgRcptIdEnabledFlag | ENABLED_FLAG | — | — |
| 30 | IntercoOrgRcptIdIntercoOrgId | INTERCO_ORG_ID | — | — |
| 31 | IntercoOrgRcptIdIntercoOrgName | INTERCO_ORG_NAME | — | ✅ |
| 32 | IntercoOrgRcptIdLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | IntercoOrgRcptIdLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | IntercoOrgRcptIdLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 35 | IntercoOrgRcptIdLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 36 | IntercoOrgRcptIdObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 37 | IntercoOrgRcptIdPayBuId | PAY_BU_ID | — | — |
| 38 | IntercoOrgRcptIdRecBuId | REC_BU_ID | — | — |
| 39 | IntercoOrgRcptIdRemoteInstanceFlag | REMOTE_INSTANCE_FLAG | — | — |
| 40 | IntercoOrgRcptIdRemoteInstanceIdentifier | REMOTE_INSTANCE_IDENTIFIER | — | — |
| 41 | IntercoOrgRecBuId | REC_BU_ID | — | — |
| 42 | IntercoOrgRemoteInstanceFlag | REMOTE_INSTANCE_FLAG | — | — |
| 43 | IntercoOrgRemoteInstanceIdentifier | REMOTE_INSTANCE_IDENTIFIER | — | — |

### [[fun_lookups|FUN_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BatchLookupDescription | DESCRIPTION | — | — |
| 2 | BatchLookupEnabledFlag | ENABLED_FLAG | — | — |
| 3 | BatchLookupEndDateActive | END_DATE_ACTIVE | — | — |
| 4 | BatchLookupLookupCode | LOOKUP_CODE | — | — |
| 5 | BatchLookupLookupType | LOOKUP_TYPE | — | — |
| 6 | BatchLookupMeaning | MEANING | — | ✅ |
| 7 | BatchLookupStartDateActive | START_DATE_ACTIVE | — | — |
| 8 | HeaderLookupDescription | DESCRIPTION | — | ✅ |
| 9 | HeaderLookupEnabledFlag | ENABLED_FLAG | — | — |
| 10 | HeaderLookupEndDateActive | END_DATE_ACTIVE | — | — |
| 11 | HeaderLookupLookupCode | LOOKUP_CODE | — | — |
| 12 | HeaderLookupLookupType | LOOKUP_TYPE | — | — |
| 13 | HeaderLookupMeaning | MEANING | — | ✅ |
| 14 | HeaderLookupStartDateActive | START_DATE_ACTIVE | — | — |

### [[fun_trx_batches|FUN_TRX_BATCHES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionBatchAutoProrationFlag | AUTO_PRORATION_FLAG | — | — |
| 2 | TransactionBatchBatchDate | BATCH_DATE | — | ✅ |
| 3 | TransactionBatchBatchId | BATCH_ID | — | ✅ |
| 4 | TransactionBatchBatchNumber | BATCH_NUMBER | — | ✅ |
| 5 | TransactionBatchControlTotal | CONTROL_TOTAL | — | — |
| 6 | TransactionBatchCreatedBy | CREATED_BY | — | — |
| 7 | TransactionBatchCreationDate | CREATION_DATE | — | — |
| 8 | TransactionBatchCurrencyCode | CURRENCY_CODE | — | ✅ |
| 9 | TransactionBatchDescription | DESCRIPTION | — | ✅ |
| 10 | TransactionBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 11 | TransactionBatchFromLeId | FROM_LE_ID | — | — |
| 12 | TransactionBatchFromLedgerId | FROM_LEDGER_ID | — | — |
| 13 | TransactionBatchFromRecurringBatchId | FROM_RECURRING_BATCH_ID | — | — |
| 14 | TransactionBatchGlDate | GL_DATE | — | ✅ |
| 15 | TransactionBatchInitiatorId | INITIATOR_ID | — | — |
| 16 | TransactionBatchInitiatorSource | INITIATOR_SOURCE | — | — |
| 17 | TransactionBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | TransactionBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | TransactionBatchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | TransactionBatchNote | NOTE | — | ✅ |
| 21 | TransactionBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | TransactionBatchOrigAutoProrationFlag | AUTO_PRORATION_FLAG | — | — |
| 23 | TransactionBatchOrigBatchDate | BATCH_DATE | — | — |
| 24 | TransactionBatchOrigBatchId | BATCH_ID | — | — |
| 25 | TransactionBatchOrigBatchNumber | BATCH_NUMBER | — | — |
| 26 | TransactionBatchOrigControlTotal | CONTROL_TOTAL | — | — |
| 27 | TransactionBatchOrigCreatedBy | CREATED_BY | — | — |
| 28 | TransactionBatchOrigCreationDate | CREATION_DATE | — | — |
| 29 | TransactionBatchOrigCurrencyCode | CURRENCY_CODE | — | — |
| 30 | TransactionBatchOrigDescription | DESCRIPTION | — | — |
| 31 | TransactionBatchOrigExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 32 | TransactionBatchOrigFromLeId | FROM_LE_ID | — | — |
| 33 | TransactionBatchOrigFromLedgerId | FROM_LEDGER_ID | — | — |
| 34 | TransactionBatchOrigFromRecurringBatchId | FROM_RECURRING_BATCH_ID | — | — |
| 35 | TransactionBatchOrigGlDate | GL_DATE | — | — |
| 36 | TransactionBatchOrigInitiatorId | INITIATOR_ID | — | — |
| 37 | TransactionBatchOrigInitiatorSource | INITIATOR_SOURCE | — | — |
| 38 | TransactionBatchOrigLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | TransactionBatchOrigLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 40 | TransactionBatchOrigLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 41 | TransactionBatchOrigNote | NOTE | — | — |
| 42 | TransactionBatchOrigObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | TransactionBatchOrigOriginalBatchId | ORIGINAL_BATCH_ID | — | — |
| 44 | TransactionBatchOrigRejectAllowFlag | REJECT_ALLOW_FLAG | — | — |
| 45 | TransactionBatchOrigReversedBatchId | REVERSED_BATCH_ID | — | — |
| 46 | TransactionBatchOrigRunningTotalCr | RUNNING_TOTAL_CR | — | — |
| 47 | TransactionBatchOrigRunningTotalDr | RUNNING_TOTAL_DR | — | — |
| 48 | TransactionBatchOrigStatus | STATUS | — | — |
| 49 | TransactionBatchOrigTrxTypeCode | TRX_TYPE_CODE | — | — |
| 50 | TransactionBatchOrigTrxTypeId | TRX_TYPE_ID | — | — |
| 51 | TransactionBatchOriginalBatchId | ORIGINAL_BATCH_ID | — | — |
| 52 | TransactionBatchRejectAllowFlag | REJECT_ALLOW_FLAG | — | — |
| 53 | TransactionBatchReverseAutoProrationFlag | AUTO_PRORATION_FLAG | — | — |
| 54 | TransactionBatchReverseBatchDate | BATCH_DATE | — | — |
| 55 | TransactionBatchReverseBatchId | BATCH_ID | — | — |
| 56 | TransactionBatchReverseBatchNumber | BATCH_NUMBER | — | — |
| 57 | TransactionBatchReverseControlTotal | CONTROL_TOTAL | — | — |
| 58 | TransactionBatchReverseCreatedBy | CREATED_BY | — | — |
| 59 | TransactionBatchReverseCreationDate | CREATION_DATE | — | — |
| 60 | TransactionBatchReverseCurrencyCode | CURRENCY_CODE | — | — |
| 61 | TransactionBatchReverseDescription | DESCRIPTION | — | — |
| 62 | TransactionBatchReverseExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 63 | TransactionBatchReverseFromLeId | FROM_LE_ID | — | — |
| 64 | TransactionBatchReverseFromLedgerId | FROM_LEDGER_ID | — | — |
| 65 | TransactionBatchReverseFromRecurringBatchId | FROM_RECURRING_BATCH_ID | — | — |
| 66 | TransactionBatchReverseGlDate | GL_DATE | — | — |
| 67 | TransactionBatchReverseInitiatorId | INITIATOR_ID | — | — |
| 68 | TransactionBatchReverseInitiatorSource | INITIATOR_SOURCE | — | — |
| 69 | TransactionBatchReverseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 70 | TransactionBatchReverseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 71 | TransactionBatchReverseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 72 | TransactionBatchReverseNote | NOTE | — | — |
| 73 | TransactionBatchReverseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 74 | TransactionBatchReverseOriginalBatchId | ORIGINAL_BATCH_ID | — | — |
| 75 | TransactionBatchReverseRejectAllowFlag | REJECT_ALLOW_FLAG | — | — |
| 76 | TransactionBatchReverseReversedBatchId | REVERSED_BATCH_ID | — | — |
| 77 | TransactionBatchReverseRunningTotalCr | RUNNING_TOTAL_CR | — | — |
| 78 | TransactionBatchReverseRunningTotalDr | RUNNING_TOTAL_DR | — | — |
| 79 | TransactionBatchReverseStatus | STATUS | — | — |
| 80 | TransactionBatchReverseTrxTypeCode | TRX_TYPE_CODE | — | — |
| 81 | TransactionBatchReverseTrxTypeId | TRX_TYPE_ID | — | — |
| 82 | TransactionBatchReversedBatchId | REVERSED_BATCH_ID | — | — |
| 83 | TransactionBatchRunningTotalCr | RUNNING_TOTAL_CR | — | — |
| 84 | TransactionBatchRunningTotalDr | RUNNING_TOTAL_DR | — | — |
| 85 | TransactionBatchStatus | STATUS | — | — |
| 86 | TransactionBatchTrxTypeCode | TRX_TYPE_CODE | — | ✅ |
| 87 | TransactionBatchTrxTypeId | TRX_TYPE_ID | — | — |

### [[fun_trx_headers|FUN_TRX_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionHeaderApprovalDate | APPROVAL_DATE | — | ✅ |
| 2 | TransactionHeaderApproverId | APPROVER_ID | — | — |
| 3 | TransactionHeaderArInvoiceNumber | AR_INVOICE_NUMBER | — | ✅ |
| 4 | TransactionHeaderBatchId | BATCH_ID | — | — |
| 5 | TransactionHeaderCreatedBy | CREATED_BY | — | ✅ |
| 6 | TransactionHeaderCreationDate | CREATION_DATE | — | ✅ |
| 7 | TransactionHeaderDescription | DESCRIPTION | — | ✅ |
| 8 | TransactionHeaderErrorReason | ERROR_REASON | — | ✅ |
| 9 | TransactionHeaderFromRecurringTrxId | FROM_RECURRING_TRX_ID | — | — |
| 10 | TransactionHeaderInitAmountCr | INIT_AMOUNT_CR | — | — |
| 11 | TransactionHeaderInitAmountDr | INIT_AMOUNT_DR | — | — |
| 12 | TransactionHeaderInitWfKey | INIT_WF_KEY | — | — |
| 13 | TransactionHeaderInitiatorId | INITIATOR_ID | — | — |
| 14 | TransactionHeaderInitiatorInstanceFlag | INITIATOR_INSTANCE_FLAG | — | — |
| 15 | TransactionHeaderInvoiceFlag | INVOICE_FLAG | — | ✅ |
| 16 | TransactionHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | TransactionHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | TransactionHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | TransactionHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | TransactionHeaderOrigApprovalDate | APPROVAL_DATE | — | — |
| 21 | TransactionHeaderOrigApproverId | APPROVER_ID | — | — |
| 22 | TransactionHeaderOrigArInvoiceNumber | AR_INVOICE_NUMBER | — | — |
| 23 | TransactionHeaderOrigBatchId | BATCH_ID | — | — |
| 24 | TransactionHeaderOrigCreatedBy | CREATED_BY | — | — |
| 25 | TransactionHeaderOrigCreationDate | CREATION_DATE | — | — |
| 26 | TransactionHeaderOrigDescription | DESCRIPTION | — | — |
| 27 | TransactionHeaderOrigErrorReason | ERROR_REASON | — | — |
| 28 | TransactionHeaderOrigFromRecurringTrxId | FROM_RECURRING_TRX_ID | — | — |
| 29 | TransactionHeaderOrigInitAmountCr | INIT_AMOUNT_CR | — | — |
| 30 | TransactionHeaderOrigInitAmountDr | INIT_AMOUNT_DR | — | — |
| 31 | TransactionHeaderOrigInitWfKey | INIT_WF_KEY | — | — |
| 32 | TransactionHeaderOrigInitiatorId | INITIATOR_ID | — | — |
| 33 | TransactionHeaderOrigInitiatorInstanceFlag | INITIATOR_INSTANCE_FLAG | — | — |
| 34 | TransactionHeaderOrigInvoiceFlag | INVOICE_FLAG | — | — |
| 35 | TransactionHeaderOrigLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | TransactionHeaderOrigLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 37 | TransactionHeaderOrigLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 38 | TransactionHeaderOrigObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 39 | TransactionHeaderOrigOriginalTrxId | ORIGINAL_TRX_ID | — | — |
| 40 | TransactionHeaderOrigReciAmountCr | RECI_AMOUNT_CR | — | — |
| 41 | TransactionHeaderOrigReciAmountDr | RECI_AMOUNT_DR | — | — |
| 42 | TransactionHeaderOrigReciWfKey | RECI_WF_KEY | — | — |
| 43 | TransactionHeaderOrigRecipientId | RECIPIENT_ID | — | — |
| 44 | TransactionHeaderOrigRecipientInstanceFlag | RECIPIENT_INSTANCE_FLAG | — | — |
| 45 | TransactionHeaderOrigRejectReason | REJECT_REASON | — | — |
| 46 | TransactionHeaderOrigReversedTrxId | REVERSED_TRX_ID | — | — |
| 47 | TransactionHeaderOrigStatus | STATUS | — | — |
| 48 | TransactionHeaderOrigToLeId | TO_LE_ID | — | — |
| 49 | TransactionHeaderOrigToLedgerId | TO_LEDGER_ID | — | — |
| 50 | TransactionHeaderOrigTrxId | TRX_ID | — | — |
| 51 | TransactionHeaderOrigTrxNumber | TRX_NUMBER | — | — |
| 52 | TransactionHeaderOriginalTrxId | ORIGINAL_TRX_ID | — | — |
| 53 | TransactionHeaderReciAmountCr | RECI_AMOUNT_CR | — | — |
| 54 | TransactionHeaderReciAmountDr | RECI_AMOUNT_DR | — | — |
| 55 | TransactionHeaderReciWfKey | RECI_WF_KEY | — | — |
| 56 | TransactionHeaderRecipientId | RECIPIENT_ID | — | — |
| 57 | TransactionHeaderRecipientInstanceFlag | RECIPIENT_INSTANCE_FLAG | — | — |
| 58 | TransactionHeaderRejectReason | REJECT_REASON | — | ✅ |
| 59 | TransactionHeaderReverseApprovalDate | APPROVAL_DATE | — | — |
| 60 | TransactionHeaderReverseApproverId | APPROVER_ID | — | — |
| 61 | TransactionHeaderReverseArInvoiceNumber | AR_INVOICE_NUMBER | — | — |
| 62 | TransactionHeaderReverseBatchId | BATCH_ID | — | — |
| 63 | TransactionHeaderReverseCreatedBy | CREATED_BY | — | — |
| 64 | TransactionHeaderReverseCreationDate | CREATION_DATE | — | — |
| 65 | TransactionHeaderReverseDescription | DESCRIPTION | — | — |
| 66 | TransactionHeaderReverseErrorReason | ERROR_REASON | — | — |
| 67 | TransactionHeaderReverseFromRecurringTrxId | FROM_RECURRING_TRX_ID | — | — |
| 68 | TransactionHeaderReverseInitAmountCr | INIT_AMOUNT_CR | — | — |
| 69 | TransactionHeaderReverseInitAmountDr | INIT_AMOUNT_DR | — | — |
| 70 | TransactionHeaderReverseInitWfKey | INIT_WF_KEY | — | — |
| 71 | TransactionHeaderReverseInitiatorId | INITIATOR_ID | — | — |
| 72 | TransactionHeaderReverseInitiatorInstanceFlag | INITIATOR_INSTANCE_FLAG | — | — |
| 73 | TransactionHeaderReverseInvoiceFlag | INVOICE_FLAG | — | — |
| 74 | TransactionHeaderReverseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 75 | TransactionHeaderReverseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 76 | TransactionHeaderReverseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 77 | TransactionHeaderReverseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 78 | TransactionHeaderReverseOriginalTrxId | ORIGINAL_TRX_ID | — | — |
| 79 | TransactionHeaderReverseReciAmountCr | RECI_AMOUNT_CR | — | — |
| 80 | TransactionHeaderReverseReciAmountDr | RECI_AMOUNT_DR | — | — |
| 81 | TransactionHeaderReverseReciWfKey | RECI_WF_KEY | — | — |
| 82 | TransactionHeaderReverseRecipientId | RECIPIENT_ID | — | — |
| 83 | TransactionHeaderReverseRecipientInstanceFlag | RECIPIENT_INSTANCE_FLAG | — | — |
| 84 | TransactionHeaderReverseRejectReason | REJECT_REASON | — | — |
| 85 | TransactionHeaderReverseReversedTrxId | REVERSED_TRX_ID | — | — |
| 86 | TransactionHeaderReverseStatus | STATUS | — | — |
| 87 | TransactionHeaderReverseToLeId | TO_LE_ID | — | — |
| 88 | TransactionHeaderReverseToLedgerId | TO_LEDGER_ID | — | — |
| 89 | TransactionHeaderReverseTrxId | TRX_ID | — | — |
| 90 | TransactionHeaderReverseTrxNumber | TRX_NUMBER | — | — |
| 91 | TransactionHeaderReversedTrxId | REVERSED_TRX_ID | — | — |
| 92 | TransactionHeaderStatus | STATUS | — | — |
| 93 | TransactionHeaderToLeId | TO_LE_ID | — | — |
| 94 | TransactionHeaderToLedgerId | TO_LEDGER_ID | — | — |
| 95 | TransactionHeaderTrxId | TRX_ID | — | ✅ |
| 96 | TransactionHeaderTrxNumber | TRX_NUMBER | — | ✅ |

### [[fun_trx_lines|FUN_TRX_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionLineCreatedBy | CREATED_BY | — | — |
| 2 | TransactionLineCreationDate | CREATION_DATE | — | — |
| 3 | TransactionLineDescription | DESCRIPTION | — | — |
| 4 | TransactionLineInitAmountCr | INIT_AMOUNT_CR | — | — |
| 5 | TransactionLineInitAmountDr | INIT_AMOUNT_DR | — | — |
| 6 | TransactionLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TransactionLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | TransactionLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | TransactionLineLineId | LINE_ID | — | — |
| 10 | TransactionLineLineNumber | LINE_NUMBER | — | — |
| 11 | TransactionLineLineTypeFlag | LINE_TYPE_FLAG | — | — |
| 12 | TransactionLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | TransactionLineReciAmountCr | RECI_AMOUNT_CR | — | — |
| 14 | TransactionLineReciAmountDr | RECI_AMOUNT_DR | — | — |
| 15 | TransactionLineTrxId | TRX_ID | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DailyConversionTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | DailyConversionTypeCreatedBy | CREATED_BY | — | — |
| 3 | DailyConversionTypeCreationDate | CREATION_DATE | — | — |
| 4 | DailyConversionTypeDescription | DESCRIPTION | — | — |
| 5 | DailyConversionTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 6 | DailyConversionTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 7 | DailyConversionTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 8 | DailyConversionTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 9 | DailyConversionTypeFemScenario | FEM_SCENARIO | — | — |
| 10 | DailyConversionTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 11 | DailyConversionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | DailyConversionTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | DailyConversionTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | DailyConversionTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | DailyConversionTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 16 | DailyConversionTypeSecurityFlag | SECURITY_FLAG | — | — |
| 17 | DailyConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | — |
| 18 | DailyConversionTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 3 | UserCreatedByPersonId | PERSON_ID | — | — |
| 4 | UserCreatedByUserGuid | USER_GUID | — | — |
| 5 | UserCreatedByUserId | USER_ID | — | — |
| 6 | UserCreatedByUsername | USERNAME | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
