---
id: DOC-HCM-879
doc_type: system-doc
title: "ZX_EXEMPTIONS — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - ZX_EXEMPTIONS
  - zx_exemptions
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_EXEMPTIONS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTENT_OWNER_ID | — | — | — | — | — | — |
| 2 | CREATED_BY | — | — | — | — | — | — |
| 3 | CREATION_DATE | — | — | — | — | — | — |
| 4 | CUST_ACCOUNT_ID | — | — | — | — | — | — |
| 5 | DET_FACTOR_TEMPL_CODE | — | — | — | — | — | — |
| 6 | DUPLICATE_EXEMPTION | — | — | — | — | — | — |
| 7 | EFFECTIVE_FROM | — | — | — | — | — | — |
| 8 | EFFECTIVE_TO | — | — | — | — | — | — |
| 9 | EXEMPTION_STATUS_CODE | — | — | — | — | — | — |
| 10 | EXEMPTION_TYPE_CODE | — | — | — | — | — | — |
| 11 | EXEMPTION_USAGE_CODE | — | — | — | — | — | — |
| 12 | EXEMPT_CERTIFICATE_NUMBER | — | — | — | — | — | — |
| 13 | EXEMPT_REASON_CODE | — | — | — | — | — | — |
| 14 | INVENTORY_ORG_ID | — | — | — | — | — | — |
| 15 | ISSUE_FLAG | — | — | — | — | — | — |
| 16 | ISSUING_TAX_AUTHORITY_ID | — | — | — | — | — | — |
| 17 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 18 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 19 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 20 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 21 | PARTY_TAX_PROFILE_ID | — | — | — | — | — | — |
| 22 | PRINT_FLAG | — | — | — | — | — | — |
| 23 | PRODUCT_ID | — | — | — | — | — | — |
| 24 | PROGRAM_APP_NAME | — | — | — | — | — | — |
| 25 | PROGRAM_LOGIN_ID | — | — | — | — | — | — |
| 26 | PROGRAM_NAME | — | — | — | — | — | — |
| 27 | PROTOCOL_NUMBER_SEQ | — | — | — | — | — | — |
| 28 | RATE_MODIFIER | — | — | — | — | — | — |
| 29 | RECORD_TYPE_CODE | — | — | — | — | — | — |
| 30 | REQUEST_ID | — | — | — | — | — | — |
| 31 | SITE_USE_ID | — | — | — | — | — | — |
| 32 | TAX | — | — | — | — | — | — |
| 33 | TAX_EXEMPTION_ID | — | — | — | — | — | — |
| 34 | TAX_JURISDICTION_ID | — | — | — | — | — | — |
| 35 | TAX_RATE_CODE | — | — | — | — | — | — |
| 36 | TAX_REGIME_CODE | — | — | — | — | — | — |
| 37 | TAX_STATUS_CODE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[sitetaxexemption|SiteTaxExemption]] (AR · BICC: 12/37)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTENT_OWNER_ID | TaxExemptionContentOwnerId | — |
| CREATED_BY | TaxExemptionCreatedBy | — |
| CREATION_DATE | TaxExemptionCreationDate | ✅ |
| CUST_ACCOUNT_ID | TaxExemptionCustAccountId | — |
| DET_FACTOR_TEMPL_CODE | TaxExemptionDetFactorTemplCode | — |
| DUPLICATE_EXEMPTION | TaxExemptionDuplicateExemption | — |
| EFFECTIVE_FROM | TaxExemptionEffectiveFrom | ✅ |
| EFFECTIVE_TO | TaxExemptionEffectiveTo | ✅ |
| EXEMPT_CERTIFICATE_NUMBER | TaxExemptionExemptCertificateNumber | ✅ |
| EXEMPT_REASON_CODE | TaxExemptionExemptReasonCode | ✅ |
| EXEMPTION_STATUS_CODE | TaxExemptionExemptionStatusCode | — |
| EXEMPTION_TYPE_CODE | TaxExemptionExemptionTypeCode | ✅ |
| EXEMPTION_USAGE_CODE | TaxExemptionExemptionUsageCode | — |
| INVENTORY_ORG_ID | TaxExemptionInventoryOrgId | — |
| ISSUE_FLAG | TaxExemptionIssueFlag | — |
| ISSUING_TAX_AUTHORITY_ID | TaxExemptionIssuingTaxAuthorityId | — |
| LAST_UPDATE_DATE | TaxExemptionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaxExemptionLastUpdateLogin | — |
| LAST_UPDATED_BY | TaxExemptionLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | TaxExemptionObjectVersionNumber | — |
| PARTY_TAX_PROFILE_ID | TaxExemptionPartyTaxProfileId | — |
| PRINT_FLAG | TaxExemptionPrintFlag | — |
| PRODUCT_ID | TaxExemptionProductId | — |
| PROGRAM_APP_NAME | TaxExemptionProgramAppName | — |
| PROGRAM_LOGIN_ID | TaxExemptionProgramLoginId | — |
| PROGRAM_NAME | TaxExemptionProgramName | — |
| PROTOCOL_NUMBER_SEQ | TaxExemptionProtocolNumberSeq | — |
| RATE_MODIFIER | TaxExemptionRateModifier | ✅ |
| RECORD_TYPE_CODE | TaxExemptionRecordTypeCode | — |
| REQUEST_ID | TaxExemptionRequestId | — |
| SITE_USE_ID | TaxExemptionSiteUseId | — |
| TAX | TaxExemptionTax | ✅ |
| TAX_EXEMPTION_ID | TaxExemptionId | — |
| TAX_JURISDICTION_ID | TaxExemptionTaxJurisdictionId | — |
| TAX_RATE_CODE | TaxExemptionTaxRateCode | ✅ |
| TAX_REGIME_CODE | TaxExemptionTaxRegimeCode | ✅ |
| TAX_STATUS_CODE | TaxExemptionTaxStatusCode | ✅ |

### [[taxexemption|TaxExemption]] (AR · BICC: 13/37)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTENT_OWNER_ID | TaxExemptionContentOwnerId | — |
| CREATED_BY | TaxExemptionCreatedBy | — |
| CREATION_DATE | TaxExemptionCreationDate | ✅ |
| CUST_ACCOUNT_ID | TaxExemptionCustAccountId | — |
| DET_FACTOR_TEMPL_CODE | TaxExemptionDetFactorTemplCode | — |
| DUPLICATE_EXEMPTION | TaxExemptionDuplicateExemption | — |
| EFFECTIVE_FROM | TaxExemptionEffectiveFrom | ✅ |
| EFFECTIVE_TO | TaxExemptionEffectiveTo | ✅ |
| EXEMPT_CERTIFICATE_NUMBER | TaxExemptionExemptCertificateNumber | ✅ |
| EXEMPT_REASON_CODE | TaxExemptionExemptReasonCode | ✅ |
| EXEMPTION_STATUS_CODE | TaxExemptionExemptionStatusCode | ✅ |
| EXEMPTION_TYPE_CODE | TaxExemptionExemptionTypeCode | ✅ |
| EXEMPTION_USAGE_CODE | TaxExemptionExemptionUsageCode | — |
| INVENTORY_ORG_ID | TaxExemptionInventoryOrgId | — |
| ISSUE_FLAG | TaxExemptionIssueFlag | — |
| ISSUING_TAX_AUTHORITY_ID | TaxExemptionIssuingTaxAuthorityId | — |
| LAST_UPDATE_DATE | TaxExemptionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaxExemptionLastUpdateLogin | — |
| LAST_UPDATED_BY | TaxExemptionLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | TaxExemptionObjectVersionNumber | — |
| PARTY_TAX_PROFILE_ID | TaxExemptionPartyTaxProfileId | — |
| PRINT_FLAG | TaxExemptionPrintFlag | — |
| PRODUCT_ID | TaxExemptionProductId | — |
| PROGRAM_APP_NAME | TaxExemptionProgramAppName | — |
| PROGRAM_LOGIN_ID | TaxExemptionProgramLoginId | — |
| PROGRAM_NAME | TaxExemptionProgramName | — |
| PROTOCOL_NUMBER_SEQ | TaxExemptionProtocolNumberSeq | — |
| RATE_MODIFIER | TaxExemptionRateModifier | ✅ |
| RECORD_TYPE_CODE | TaxExemptionRecordTypeCode | — |
| REQUEST_ID | TaxExemptionRequestId | — |
| SITE_USE_ID | TaxExemptionSiteUseId | — |
| TAX | TaxExemptionTax | ✅ |
| TAX_EXEMPTION_ID | TaxExemptionId | — |
| TAX_JURISDICTION_ID | TaxExemptionTaxJurisdictionId | — |
| TAX_RATE_CODE | TaxExemptionTaxRateCode | ✅ |
| TAX_REGIME_CODE | TaxExemptionTaxRegimeCode | ✅ |
| TAX_STATUS_CODE | TaxExemptionTaxStatusCode | ✅ |
