---
id: DOC-OTHER-PVO-BillingPlanExtractPVO
doc_type: system-doc
title: "BillingPlanExtractPVO — PVO Cross-Module"
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
  - BillingPlanExtractPVO
  - billingplanextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillingPlanExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Billing Plan Extract. Acessa as tabelas: DOO_BILLING_PLANS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.BillingPlanExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_billing_plans|DOO_BILLING_PLANS]] — 21 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[doo_billing_plans|DOO_BILLING_PLANS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillingPlanBillingNumOfPeriods | BILLING_NUM_OF_PERIODS | — | ✅ |
| 2 | BillingPlanBillingPeriodEndDate | BILLING_PERIOD_END_DATE | — | ✅ |
| 3 | BillingPlanBillingPeriodNumber | BILLING_PERIOD_NUMBER | — | ✅ |
| 4 | BillingPlanBillingPeriodStartDate | BILLING_PERIOD_START_DATE | — | ✅ |
| 5 | BillingPlanBillingTrxDate | BILLING_TRX_DATE | — | ✅ |
| 6 | BillingPlanCancellationEffectiveDate | CANCELLATION_EFFECTIVE_DATE | — | ✅ |
| 7 | BillingPlanCreatedBy | CREATED_BY | — | ✅ |
| 8 | BillingPlanCreationDate | CREATION_DATE | — | ✅ |
| 9 | BillingPlanFulfillLineId | FULFILL_LINE_ID | — | ✅ |
| 10 | BillingPlanId | BILLING_PLAN_ID | 🔑 | ✅ |
| 11 | BillingPlanLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | BillingPlanLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | BillingPlanLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | BillingPlanNetBillingAmtPerPeriod | NET_BILLING_AMT_PER_PERIOD | — | ✅ |
| 15 | BillingPlanObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | BillingPlanOverridePeriod | OVERRIDE_PERIOD | — | ✅ |
| 17 | BillingPlanOverridePeriodAmount | OVERRIDE_PERIOD_AMOUNT | — | ✅ |
| 18 | BillingPlanOverridePeriodQuantity | OVERRIDE_PERIOD_QUANTITY | — | ✅ |
| 19 | BillingPlanPeriodicityCode | PERIODICITY_CODE | — | ✅ |
| 20 | BillingPlanSourceBillingPlanId | SOURCE_BILLING_PLAN_ID | — | ✅ |
| 21 | BillingPlanTypeCode | BILLING_PLAN_TYPE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
