---
id: DOC-OTHER-PVO-GrantsBusinessUnitExtractPVO
doc_type: system-doc
title: "GrantsBusinessUnitExtractPVO — PVO Cross-Module"
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
  - GrantsBusinessUnitExtractPVO
  - grantsbusinessunitextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GrantsBusinessUnitExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Grants Business Unit Extract. Acessa as tabelas: GMS_BUSINESS_UNITS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.GrantsBusinessUnitExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 1 | 1 | 25 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_business_units|GMS_BUSINESS_UNITS]] — 25 atributos (1 PKs, 25 BICC)

---

## ⚙️ Atributos

### [[gms_business_units|GMS_BUSINESS_UNITS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GrantsBusinessUnitPEOAutoReleaseInvoice | AUTO_RELEASE_INVOICE | — | ✅ |
| 2 | GrantsBusinessUnitPEOBillingCycleId | BILLING_CYCLE_ID | — | ✅ |
| 3 | GrantsBusinessUnitPEOBuId | BU_ID | 🔑 | ✅ |
| 4 | GrantsBusinessUnitPEOContractTypeId | CONTRACT_TYPE_ID | — | ✅ |
| 5 | GrantsBusinessUnitPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | GrantsBusinessUnitPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | GrantsBusinessUnitPEODayToClose | DAY_TO_CLOSE | — | ✅ |
| 8 | GrantsBusinessUnitPEOEventFormatId | EVENT_FORMAT_ID | — | ✅ |
| 9 | GrantsBusinessUnitPEOIndRateSchId | IND_RATE_SCH_ID | — | ✅ |
| 10 | GrantsBusinessUnitPEOInstitutionId | INSTITUTION_ID | — | ✅ |
| 11 | GrantsBusinessUnitPEOInvHdrGroupingOptions | INV_HDR_GROUPING_OPTIONS | — | ✅ |
| 12 | GrantsBusinessUnitPEOInvTrxTypeId | INV_TRX_TYPE_ID | — | ✅ |
| 13 | GrantsBusinessUnitPEOInvoiceMethodId | INVOICE_METHOD_ID | — | ✅ |
| 14 | GrantsBusinessUnitPEOLaborFormatId | LABOR_FORMAT_ID | — | ✅ |
| 15 | GrantsBusinessUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | GrantsBusinessUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | GrantsBusinessUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | GrantsBusinessUnitPEONetInvoiceFlag | NET_INVOICE_FLAG | — | ✅ |
| 19 | GrantsBusinessUnitPEONonLaborFormatId | NON_LABOR_FORMAT_ID | — | ✅ |
| 20 | GrantsBusinessUnitPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | GrantsBusinessUnitPEOOnTrackPctTo | ON_TRACK_PCT_TO | — | ✅ |
| 22 | GrantsBusinessUnitPEOOtValueUsedInGraph | OT_VALUE_USED_IN_GRAPH | — | ✅ |
| 23 | GrantsBusinessUnitPEORevenueMethodId | REVENUE_METHOD_ID | — | ✅ |
| 24 | GrantsBusinessUnitPEOUnderSpendPctTo | UNDER_SPEND_PCT_TO | — | ✅ |
| 25 | GrantsBusinessUnitPEOUsValueUsedInGraph | US_VALUE_USED_IN_GRAPH | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
