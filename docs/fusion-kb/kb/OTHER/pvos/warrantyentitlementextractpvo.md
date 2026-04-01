---
id: DOC-OTHER-PVO-WarrantyEntitlementExtractPVO
doc_type: system-doc
title: "WarrantyEntitlementExtractPVO — PVO Cross-Module"
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
  - WarrantyEntitlementExtractPVO
  - warrantyentitlementextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WarrantyEntitlementExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Warranty Entitlement Extract. Acessa as tabelas: CSE_W_ENTITLEMENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.WarrantyEntitlementExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 79 | 1 | 1 | 79 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_w_entitlements|CSE_W_ENTITLEMENTS]] — 79 atributos (1 PKs, 79 BICC)

---

## ⚙️ Atributos

### [[cse_w_entitlements|CSE_W_ENTITLEMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetId | ASSET_ID | — | ✅ |
| 2 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 3 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 4 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 5 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 6 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 7 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 8 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 9 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 10 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 11 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 12 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 13 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 14 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 15 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 16 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 17 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 18 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 19 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 20 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 21 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 22 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 23 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 24 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 25 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 26 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 27 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 28 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 29 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 30 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 31 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 32 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 33 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 34 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 35 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 36 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 37 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 38 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 39 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 40 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 41 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 42 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 43 | ClaimId | CLAIM_ID | — | ✅ |
| 44 | ContractId | CONTRACT_ID | — | ✅ |
| 45 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | ✅ |
| 46 | CostTransactionId | COST_TRANSACTION_ID | — | ✅ |
| 47 | CreatedBy | CREATED_BY | — | ✅ |
| 48 | CreationDate | CREATION_DATE | — | ✅ |
| 49 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | ✅ |
| 50 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 51 | EntitlementDate | ENTITLEMENT_DATE | — | ✅ |
| 52 | EntitlementDescription | ENTITLEMENT_DESCRIPTION | — | ✅ |
| 53 | EntitlementId | ENTITLEMENT_ID | 🔑 | ✅ |
| 54 | EntitlementNotes | ENTITLEMENT_NOTES | — | ✅ |
| 55 | EntitlementNumber | ENTITLEMENT_NUMBER | — | ✅ |
| 56 | EntitlementTypeCode | ENTITLEMENT_TYPE_CODE | — | ✅ |
| 57 | ExternalReferenceNumber | EXTERNAL_REFERENCE_NUMBER | — | ✅ |
| 58 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 59 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 60 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 62 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 63 | ManuallyCreatedFlag | MANUALLY_CREATED_FLAG | — | ✅ |
| 64 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 65 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 66 | ReasonForRepairCodeId | REASON_FOR_REPAIR_CODE_ID | — | ✅ |
| 67 | ReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | ✅ |
| 68 | ReimbursementQty | REIMBURSEMENT_QTY | — | ✅ |
| 69 | ReimbursementQtyUomCode | REIMBURSEMENT_QTY_UOM_CODE | — | ✅ |
| 70 | ReimbursementTotalCost | REIMBURSEMENT_TOTAL_COST | — | ✅ |
| 71 | ReimbursementUnitCost | REIMBURSEMENT_UNIT_COST | — | ✅ |
| 72 | RequestId | REQUEST_ID | — | ✅ |
| 73 | TransactionCodeId | TRANSACTION_CODE_ID | — | ✅ |
| 74 | WarrantyEntitledFlag | WARRANTY_ENTITLED_FLAG | — | ✅ |
| 75 | WoOperationId | WO_OPERATION_ID | — | ✅ |
| 76 | WoOperationMaterialId | WO_OPERATION_MATERIAL_ID | — | ✅ |
| 77 | WoOperationResourceId | WO_OPERATION_RESOURCE_ID | — | ✅ |
| 78 | WorkAccomplishedCodeId | WORK_ACCOMPLISHED_CODE_ID | — | ✅ |
| 79 | WorkOrderId | WORK_ORDER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
