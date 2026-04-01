---
id: DOC-OTHER-PVO-FiscalDocAssoctnsP
doc_type: system-doc
title: "FiscalDocAssoctnsP — PVO Cross-Module"
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
  - FiscalDocAssoctnsP
  - fiscaldocassoctnsp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FiscalDocAssoctnsP

## 📌 Visão Geral

View Object para extração BICC de dados de Fiscal Doc Assoctns P. Acessa as tabelas: CMF_FISCAL_DOC_ASSOCTNS_VL, CMF_FISCAL_PROC_OPTIONS.

**Caminho:** `FscmTopModelAM.FiscalDocumentAM.FiscalDocAssoctnsP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 70 | 2 | 1 | 70 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmf_fiscal_doc_assoctns_vl|CMF_FISCAL_DOC_ASSOCTNS_VL]] — 16 atributos (1 PKs, 16 BICC)
- [[cmf_fiscal_proc_options|CMF_FISCAL_PROC_OPTIONS]] — 54 atributos (54 BICC)

---

## ⚙️ Atributos

### [[cmf_fiscal_doc_assoctns_vl|CMF_FISCAL_DOC_ASSOCTNS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocAssoctnsId | FISCAL_DOC_ASSOCTNS_ID | 🔑 | ✅ |
| 2 | FiscalDocAssoctnsPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 3 | FiscalDocAssoctnsPEOAssociationCode | ASSOCIATION_CODE | — | ✅ |
| 4 | FiscalDocAssoctnsPEOCountryCode | COUNTRY_CODE | — | ✅ |
| 5 | FiscalDocAssoctnsPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | FiscalDocAssoctnsPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | FiscalDocAssoctnsPEODescription | DESCRIPTION | — | ✅ |
| 8 | FiscalDocAssoctnsPEOEndDate | END_DATE | — | ✅ |
| 9 | FiscalDocAssoctnsPEOFiscalProcOptionsId | FISCAL_PROC_OPTIONS_ID | — | ✅ |
| 10 | FiscalDocAssoctnsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | FiscalDocAssoctnsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | FiscalDocAssoctnsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | FiscalDocAssoctnsPEOName | NAME | — | ✅ |
| 14 | FiscalDocAssoctnsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | FiscalDocAssoctnsPEOSeedFlag | SEED_FLAG | — | ✅ |
| 16 | FiscalDocAssoctnsPEOStartDate | START_DATE | — | ✅ |

### [[cmf_fiscal_proc_options|CMF_FISCAL_PROC_OPTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalProcOptionsPEOAdditionalMatchRule | ADDITIONAL_MATCH_RULE | — | ✅ |
| 2 | FiscalProcOptionsPEOChangeDocStatusFlag | CHANGE_DOC_STATUS_FLAG | — | ✅ |
| 3 | FiscalProcOptionsPEOChargeAllocation1Flag | CHARGE_ALLOCATION_1_FLAG | — | ✅ |
| 4 | FiscalProcOptionsPEOChargeAllocationFlag | CHARGE_ALLOCATION_FLAG | — | ✅ |
| 5 | FiscalProcOptionsPEOChargesDistributionFlag | CHARGES_DISTRIBUTION_FLAG | — | ✅ |
| 6 | FiscalProcOptionsPEOComplementaryFlag | COMPLEMENTARY_FLAG | — | ✅ |
| 7 | FiscalProcOptionsPEOComplementaryLineType | COMPLEMENTARY_LINE_TYPE | — | ✅ |
| 8 | FiscalProcOptionsPEOCostDistribution | COST_DISTRIBUTION | — | ✅ |
| 9 | FiscalProcOptionsPEOCountryCode | COUNTRY_CODE | — | ✅ |
| 10 | FiscalProcOptionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | FiscalProcOptionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | FiscalProcOptionsPEODeleteAllowedFlag | DELETE_ALLOWED_FLAG | — | ✅ |
| 13 | FiscalProcOptionsPEODocumentTypeCode | DOCUMENT_TYPE_CODE | — | ✅ |
| 14 | FiscalProcOptionsPEOElectronicModel | ELECTRONIC_MODEL | — | ✅ |
| 15 | FiscalProcOptionsPEOEndDate | END_DATE | — | ✅ |
| 16 | FiscalProcOptionsPEOFdCurrencyCode | FD_CURRENCY_CODE | — | ✅ |
| 17 | FiscalProcOptionsPEOFdHeaderLineRelationship | FD_HEADER_LINE_RELATIONSHIP | — | ✅ |
| 18 | FiscalProcOptionsPEOFdUsage | FD_USAGE | — | ✅ |
| 19 | FiscalProcOptionsPEOFiscalAttributesFlag | FISCAL_ATTRIBUTES_FLAG | — | ✅ |
| 20 | FiscalProcOptionsPEOFiscalProcOptionsId | FISCAL_PROC_OPTIONS_ID | — | ✅ |
| 21 | FiscalProcOptionsPEOHoldMgmtFlag | HOLD_MGMT_FLAG | — | ✅ |
| 22 | FiscalProcOptionsPEOIfaceApFlag | IFACE_AP_FLAG | — | ✅ |
| 23 | FiscalProcOptionsPEOIfaceCstFlag | IFACE_CST_FLAG | — | ✅ |
| 24 | FiscalProcOptionsPEOIfaceRcvFlag | IFACE_RCV_FLAG | — | ✅ |
| 25 | FiscalProcOptionsPEOInformativeCharges | INFORMATIVE_CHARGES | — | ✅ |
| 26 | FiscalProcOptionsPEOIssuerType | ISSUER_TYPE | — | ✅ |
| 27 | FiscalProcOptionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | FiscalProcOptionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 29 | FiscalProcOptionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | FiscalProcOptionsPEOLegalProcessesFlag | LEGAL_PROCESSES_FLAG | — | ✅ |
| 31 | FiscalProcOptionsPEOLineSrcDocTypeCode | LINE_SRC_DOC_TYPE_CODE | — | ✅ |
| 32 | FiscalProcOptionsPEOManualPrQttyEntryFlag | MANUAL_PR_QTTY_ENTRY_FLAG | — | ✅ |
| 33 | FiscalProcOptionsPEOMatchRefPrepaymentFlag | MATCH_REF_PREPAYMENT_FLAG | — | ✅ |
| 34 | FiscalProcOptionsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 35 | FiscalProcOptionsPEOOperationType | OPERATION_TYPE | — | ✅ |
| 36 | FiscalProcOptionsPEOParentProcessOptId | PARENT_PROCESS_OPT_ID | — | ✅ |
| 37 | FiscalProcOptionsPEOPayablesDocTypeCode | PAYABLES_DOC_TYPE_CODE | — | ✅ |
| 38 | FiscalProcOptionsPEOPhysicalRecptByOrderFd | PHYSICAL_RECPT_BY_ORDER_FD | — | ✅ |
| 39 | FiscalProcOptionsPEOProcessCode | PROCESS_CODE | — | ✅ |
| 40 | FiscalProcOptionsPEOProcessOptionCode | PROCESS_OPTION_CODE | — | ✅ |
| 41 | FiscalProcOptionsPEOReceiverType | RECEIVER_TYPE | — | ✅ |
| 42 | FiscalProcOptionsPEOReferenceAllowedFlag | REFERENCE_ALLOWED_FLAG | — | ✅ |
| 43 | FiscalProcOptionsPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 44 | FiscalProcOptionsPEOSeriesReq | SERIES_REQ | — | ✅ |
| 45 | FiscalProcOptionsPEOShipFromType | SHIP_FROM_TYPE | — | ✅ |
| 46 | FiscalProcOptionsPEOShipToType | SHIP_TO_TYPE | — | ✅ |
| 47 | FiscalProcOptionsPEOSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | ✅ |
| 48 | FiscalProcOptionsPEOSrcDocCurrencyCode | SRC_DOC_CURRENCY_CODE | — | ✅ |
| 49 | FiscalProcOptionsPEOStartDate | START_DATE | — | ✅ |
| 50 | FiscalProcOptionsPEOSubSeriesReq | SUB_SERIES_REQ | — | ✅ |
| 51 | FiscalProcOptionsPEOTaxCalculationFlag | TAX_CALCULATION_FLAG | — | ✅ |
| 52 | FiscalProcOptionsPEOUpdateRefPhysicalReceipt | UPDATE_REF_PHYSICAL_RECEIPT | — | ✅ |
| 53 | FiscalProcOptionsPEOValidateRefDocFlag | VALIDATE_REF_DOC_FLAG | — | ✅ |
| 54 | FiscalProcOptionsPEOValidationFlag | VALIDATION_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
