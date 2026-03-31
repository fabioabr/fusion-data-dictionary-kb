---
id: DOC-OTHER-PVO-BillingMethodExtractPVO
doc_type: system-doc
title: "BillingMethodExtractPVO — PVO Cross-Module"
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
  - BillingMethodExtractPVO
  - billingmethodextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillingMethodExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Billing Method Extract. Acessa as tabelas: PJB_BILLING_METHODS_B, PJB_BILLING_METHODS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.BillingMethodExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 2 | 3 | 28 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_billing_methods_b|PJB_BILLING_METHODS_B]] — 16 atributos (1 PKs, 16 BICC)
- [[pjb_billing_methods_tl|PJB_BILLING_METHODS_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjb_billing_methods_b|PJB_BILLING_METHODS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillingMethodBasePEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | BillingMethodBasePEOBillMethodFlag | BILL_METHOD_FLAG | — | ✅ |
| 3 | BillingMethodBasePEOBillMethodId | BILL_METHOD_ID | 🔑 | ✅ |
| 4 | BillingMethodBasePEOBillTypeClassCode | BILL_TYPE_CLASS_CODE | — | ✅ |
| 5 | BillingMethodBasePEOCalculationLevelCode | CALCULATION_LEVEL_CODE | — | ✅ |
| 6 | BillingMethodBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | BillingMethodBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | BillingMethodBasePEOIntercompanyMethod | INTERCOMPANY_METHOD | — | ✅ |
| 9 | BillingMethodBasePEOLaborRateTypeCode | LABOR_RATE_TYPE_CODE | — | ✅ |
| 10 | BillingMethodBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | BillingMethodBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | BillingMethodBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | BillingMethodBasePEOMethodCfgType | METHOD_CFG_TYPE | — | ✅ |
| 14 | BillingMethodBasePEONlRateTypeCode | NL_RATE_TYPE_CODE | — | ✅ |
| 15 | BillingMethodBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | BillingMethodBasePEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |

### [[pjb_billing_methods_tl|PJB_BILLING_METHODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillingMethodTransLangPEOBillMethodDesc | BILL_METHOD_DESC | — | ✅ |
| 2 | BillingMethodTransLangPEOBillMethodId | BILL_METHOD_ID | 🔑 | ✅ |
| 3 | BillingMethodTransLangPEOBillMethodName | BILL_METHOD_NAME | — | ✅ |
| 4 | BillingMethodTransLangPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | BillingMethodTransLangPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | BillingMethodTransLangPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | BillingMethodTransLangPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | BillingMethodTransLangPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | BillingMethodTransLangPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | BillingMethodTransLangPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | BillingMethodTransLangPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | BillingMethodTransLangPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
