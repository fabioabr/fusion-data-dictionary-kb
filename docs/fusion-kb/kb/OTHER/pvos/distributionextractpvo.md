---
id: DOC-OTHER-PVO-DistributionExtractPVO
doc_type: system-doc
title: "DistributionExtractPVO — PVO Cross-Module"
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
  - DistributionExtractPVO
  - distributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DistributionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Distribution Extract. Acessa as tabelas: AR_DISTRIBUTIONS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.DistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 1 | 1 | 48 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ar_distributions_all|AR_DISTRIBUTIONS_ALL]] — 48 atributos (1 PKs, 48 BICC)

---

## ⚙️ Atributos

### [[ar_distributions_all|AR_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArDistributionAcctdAmountCr | ACCTD_AMOUNT_CR | — | ✅ |
| 2 | ArDistributionAcctdAmountDr | ACCTD_AMOUNT_DR | — | ✅ |
| 3 | ArDistributionActivityBucket | ACTIVITY_BUCKET | — | ✅ |
| 4 | ArDistributionAmountCr | AMOUNT_CR | — | ✅ |
| 5 | ArDistributionAmountDr | AMOUNT_DR | — | ✅ |
| 6 | ArDistributionCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 7 | ArDistributionCreatedBy | CREATED_BY | — | ✅ |
| 8 | ArDistributionCreationDate | CREATION_DATE | — | ✅ |
| 9 | ArDistributionCurrencyCode | CURRENCY_CODE | — | ✅ |
| 10 | ArDistributionCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 11 | ArDistributionCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 12 | ArDistributionCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 13 | ArDistributionFromAcctdAmountCr | FROM_ACCTD_AMOUNT_CR | — | ✅ |
| 14 | ArDistributionFromAcctdAmountDr | FROM_ACCTD_AMOUNT_DR | — | ✅ |
| 15 | ArDistributionFromAmountCr | FROM_AMOUNT_CR | — | ✅ |
| 16 | ArDistributionFromAmountDr | FROM_AMOUNT_DR | — | ✅ |
| 17 | ArDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | ArDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | ArDistributionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | ArDistributionLineId | LINE_ID | 🔑 | ✅ |
| 21 | ArDistributionLocationSegmentId | LOCATION_SEGMENT_ID | — | ✅ |
| 22 | ArDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | ArDistributionOrgId | ORG_ID | — | ✅ |
| 24 | ArDistributionRefAccountClass | REF_ACCOUNT_CLASS | — | ✅ |
| 25 | ArDistributionRefCustTrxLineGlDistId | REF_CUST_TRX_LINE_GL_DIST_ID | — | ✅ |
| 26 | ArDistributionRefCustomerTrxLineId | REF_CUSTOMER_TRX_LINE_ID | — | ✅ |
| 27 | ArDistributionRefDistCcid | REF_DIST_CCID | — | ✅ |
| 28 | ArDistributionRefLineId | REF_LINE_ID | — | ✅ |
| 29 | ArDistributionRefMfDistFlag | REF_MF_DIST_FLAG | — | ✅ |
| 30 | ArDistributionRefPrevCustTrxLineId | REF_PREV_CUST_TRX_LINE_ID | — | ✅ |
| 31 | ArDistributionReversalFlag | REVERSAL_FLAG | — | ✅ |
| 32 | ArDistributionReversedSourceId | REVERSED_SOURCE_ID | — | ✅ |
| 33 | ArDistributionSourceId | SOURCE_ID | — | ✅ |
| 34 | ArDistributionSourceIdSecondary | SOURCE_ID_SECONDARY | — | ✅ |
| 35 | ArDistributionSourceTable | SOURCE_TABLE | — | ✅ |
| 36 | ArDistributionSourceTableSecondary | SOURCE_TABLE_SECONDARY | — | ✅ |
| 37 | ArDistributionSourceType | SOURCE_TYPE | — | ✅ |
| 38 | ArDistributionSourceTypeSecondary | SOURCE_TYPE_SECONDARY | — | ✅ |
| 39 | ArDistributionTaxCodeId | TAX_CODE_ID | — | ✅ |
| 40 | ArDistributionTaxGroupCodeId | TAX_GROUP_CODE_ID | — | ✅ |
| 41 | ArDistributionTaxId | TAX_ID | — | ✅ |
| 42 | ArDistributionTaxLinkId | TAX_LINK_ID | — | ✅ |
| 43 | ArDistributionTaxableAccountedCr | TAXABLE_ACCOUNTED_CR | — | ✅ |
| 44 | ArDistributionTaxableAccountedDr | TAXABLE_ACCOUNTED_DR | — | ✅ |
| 45 | ArDistributionTaxableEnteredCr | TAXABLE_ENTERED_CR | — | ✅ |
| 46 | ArDistributionTaxableEnteredDr | TAXABLE_ENTERED_DR | — | ✅ |
| 47 | ArDistributionThirdPartyId | THIRD_PARTY_ID | — | ✅ |
| 48 | ArDistributionThirdPartySubId | THIRD_PARTY_SUB_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
