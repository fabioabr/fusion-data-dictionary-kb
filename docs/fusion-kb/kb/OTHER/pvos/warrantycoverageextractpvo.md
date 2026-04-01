---
id: DOC-OTHER-PVO-WarrantyCoverageExtractPVO
doc_type: system-doc
title: "WarrantyCoverageExtractPVO — PVO Cross-Module"
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
  - WarrantyCoverageExtractPVO
  - warrantycoverageextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WarrantyCoverageExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Warranty Coverage Extract. Acessa as tabelas: CSE_W_COVERAGES_B, CSE_W_COVERAGES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.WarrantyCoverageExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 85 | 2 | 3 | 85 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_w_coverages_b|CSE_W_COVERAGES_B]] — 74 atributos (1 PKs, 74 BICC)
- [[cse_w_coverages_tl|CSE_W_COVERAGES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cse_w_coverages_b|CSE_W_COVERAGES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 10 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 11 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 12 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 13 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 14 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 15 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 16 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 17 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 18 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 19 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 20 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 21 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 22 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 23 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 24 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 25 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 26 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 27 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 28 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 29 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 30 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 32 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 33 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 34 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 35 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 36 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 37 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 38 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 39 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 40 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 41 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 42 | AuthorizationRequiredFlag | AUTHORIZATION_REQUIRED_FLAG | — | ✅ |
| 43 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | ✅ |
| 44 | CoverageCode | COVERAGE_CODE | — | ✅ |
| 45 | CoverageEndDate | COVERAGE_END_DATE | — | ✅ |
| 46 | CoverageId | COVERAGE_ID | 🔑 | ✅ |
| 47 | CoverageStartDate | COVERAGE_START_DATE | — | ✅ |
| 48 | CoverageStatusCode | COVERAGE_STATUS_CODE | — | ✅ |
| 49 | CoverageTypeCode | COVERAGE_TYPE_CODE | — | ✅ |
| 50 | CreatedBy | CREATED_BY | — | ✅ |
| 51 | CreationDate | CREATION_DATE | — | ✅ |
| 52 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | ✅ |
| 53 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 54 | FilterByTxnCodeFlag | FILTER_BY_TXN_CODE_FLAG | — | ✅ |
| 55 | InternalRepairAllowedFlag | INTERNAL_REPAIR_ALLOWED_FLAG | — | ✅ |
| 56 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 57 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 58 | LaborReimbursementFlag | LABOR_REIMBURSEMENT_FLAG | — | ✅ |
| 59 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 60 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 61 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 62 | ManufacturerId | MANUFACTURER_ID | — | ✅ |
| 63 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 64 | PartsReimbursementFlag | PARTS_REIMBURSEMENT_FLAG | — | ✅ |
| 65 | PartsReturnRequiredFlag | PARTS_RETURN_REQUIRED_FLAG | — | ✅ |
| 66 | ReactionsAndResolutions | REACTIONS_AND_RESOLUTIONS | — | ✅ |
| 67 | RequestId | REQUEST_ID | — | ✅ |
| 68 | ServiceLevelAgreements | SERVICE_LEVEL_AGREEMENTS | — | ✅ |
| 69 | SupplierId | SUPPLIER_ID | — | ✅ |
| 70 | TermsAndConditions | TERMS_AND_CONDITIONS | — | ✅ |
| 71 | WarrantyDuration | WARRANTY_DURATION | — | ✅ |
| 72 | WarrantyDurationUomCode | WARRANTY_DURATION_UOM_CODE | — | ✅ |
| 73 | WarrantyProviderId | WARRANTY_PROVIDER_ID | — | ✅ |
| 74 | WarrantyProviderTypeCode | WARRANTY_PROVIDER_TYPE_CODE | — | ✅ |

### [[cse_w_coverages_tl|CSE_W_COVERAGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CoverageDescription | COVERAGE_DESCRIPTION | — | ✅ |
| 2 | WarrantyCoverageAnalyticsTLPEOCoverageId | COVERAGE_ID | 🔑 | ✅ |
| 3 | WarrantyCoverageAnalyticsTLPEOCoverageName | COVERAGE_NAME | — | ✅ |
| 4 | WarrantyCoverageAnalyticsTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | WarrantyCoverageAnalyticsTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | WarrantyCoverageAnalyticsTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | WarrantyCoverageAnalyticsTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | WarrantyCoverageAnalyticsTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | WarrantyCoverageAnalyticsTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | WarrantyCoverageAnalyticsTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | WarrantyCoverageAnalyticsTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
