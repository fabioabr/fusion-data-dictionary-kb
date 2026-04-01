---
id: DOC-OTHER-PVO-WarrantyClaimExtractPVO
doc_type: system-doc
title: "WarrantyClaimExtractPVO — PVO Cross-Module"
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
  - WarrantyClaimExtractPVO
  - warrantyclaimextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WarrantyClaimExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Warranty Claim Extract. Acessa as tabelas: CSE_W_CLAIMS_B, CSE_W_CLAIMS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.WarrantyClaimExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 93 | 2 | 3 | 93 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_w_claims_b|CSE_W_CLAIMS_B]] — 83 atributos (1 PKs, 83 BICC)
- [[cse_w_claims_tl|CSE_W_CLAIMS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[cse_w_claims_b|CSE_W_CLAIMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | AssignedToPersonId | ASSIGNED_TO_PERSON_ID | — | ✅ |
| 3 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 4 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 5 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 6 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 7 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 8 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 9 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 10 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 11 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 12 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 13 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 14 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 15 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 16 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 17 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 18 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 19 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 20 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 21 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 22 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 23 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 24 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 25 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 26 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 27 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 28 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 29 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 30 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 31 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 32 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 33 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 34 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 35 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 36 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 37 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 38 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 39 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 40 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 41 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 42 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 43 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 44 | ClaimAdjustmentAmount | CLAIM_ADJUSTMENT_AMOUNT | — | ✅ |
| 45 | ClaimAmount | CLAIM_AMOUNT | — | ✅ |
| 46 | ClaimAmountCurrencyCode | CLAIM_AMOUNT_CURRENCY_CODE | — | ✅ |
| 47 | ClaimDate | CLAIM_DATE | — | ✅ |
| 48 | ClaimId | CLAIM_ID | 🔑 | ✅ |
| 49 | ClaimNotes | CLAIM_NOTES | — | ✅ |
| 50 | ClaimNumber | CLAIM_NUMBER | — | ✅ |
| 51 | ClaimStatusCode | CLAIM_STATUS_CODE | — | ✅ |
| 52 | ClaimTypeCode | CLAIM_TYPE_CODE | — | ✅ |
| 53 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | ✅ |
| 54 | CreatedBy | CREATED_BY | — | ✅ |
| 55 | CreationDate | CREATION_DATE | — | ✅ |
| 56 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | ✅ |
| 57 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 58 | CurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 59 | CurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 60 | EquipmentAmountTotal | EQUIPMENT_AMOUNT_TOTAL | — | ✅ |
| 61 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 62 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 63 | LaborAmountTotal | LABOR_AMOUNT_TOTAL | — | ✅ |
| 64 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 65 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 66 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 67 | ManuallyCreatedFlag | MANUALLY_CREATED_FLAG | — | ✅ |
| 68 | MatchToTxnCodeFlag | MATCH_TO_TXN_CODE_FLAG | — | ✅ |
| 69 | MaterialAmountTotal | MATERIAL_AMOUNT_TOTAL | — | ✅ |
| 70 | ObjectId | OBJECT_ID | — | ✅ |
| 71 | ObjectTypeCode | OBJECT_TYPE_CODE | — | ✅ |
| 72 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 73 | OtherAmount | OTHER_AMOUNT | — | ✅ |
| 74 | ProviderLaborRate | PROVIDER_LABOR_RATE | — | ✅ |
| 75 | ReasonForRepairCodeId | REASON_FOR_REPAIR_CODE_ID | — | ✅ |
| 76 | ReimbursementAmount | REIMBURSEMENT_AMOUNT | — | ✅ |
| 77 | ReimbursementReference | REIMBURSEMENT_REFERENCE | — | ✅ |
| 78 | ReimbursementTypeCode | REIMBURSEMENT_TYPE_CODE | — | ✅ |
| 79 | RequestId | REQUEST_ID | — | ✅ |
| 80 | ResolutionDate | RESOLUTION_DATE | — | ✅ |
| 81 | StandardLaborAmount | STANDARD_LABOR_AMOUNT | — | ✅ |
| 82 | SubmitByDate | SUBMIT_BY_DATE | — | ✅ |
| 83 | WarrantyProviderId | WARRANTY_PROVIDER_ID | — | ✅ |

### [[cse_w_claims_tl|CSE_W_CLAIMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WarrantyClaimsAnalyticsTLPEOClaimDescription | CLAIM_DESCRIPTION | — | ✅ |
| 2 | WarrantyClaimsAnalyticsTLPEOClaimId | CLAIM_ID | 🔑 | ✅ |
| 3 | WarrantyClaimsAnalyticsTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | WarrantyClaimsAnalyticsTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | WarrantyClaimsAnalyticsTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | WarrantyClaimsAnalyticsTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | WarrantyClaimsAnalyticsTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | WarrantyClaimsAnalyticsTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | WarrantyClaimsAnalyticsTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | WarrantyClaimsAnalyticsTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
