---
id: DOC-OTHER-PVO-PayrollDPVO
doc_type: system-doc
title: "PayrollDPVO — PVO Cross-Module"
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
  - PayrollDPVO
  - payrolldpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PayrollDPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Payroll D. Acessa as tabelas: PAY_ALL_PAYROLLS_F, PAY_CONSOLIDATION_SETS, PAY_ORG_PAY_METHODS_VL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayCoreAM.PayrollDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 3 | 2 | 22 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[pay_all_payrolls_f|PAY_ALL_PAYROLLS_F]] — 26 atributos (2 PKs, 20 BICC)
- [[pay_consolidation_sets|PAY_CONSOLIDATION_SETS]] — 2 atributos (1 BICC)
- [[pay_org_pay_methods_vl|PAY_ORG_PAY_METHODS_VL]] — 5 atributos (1 BICC)

---

## ⚙️ Atributos

### [[pay_all_payrolls_f|PAY_ALL_PAYROLLS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | FixedDate | FIXED_DATE | — | ✅ |
| 4 | PayrollDPEOConsolidationSetId | CONSOLIDATION_SET_ID | — | — |
| 5 | PayrollDPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | PayrollDPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | PayrollDPEOCutOffDateOffset | CUT_OFF_DATE_OFFSET | — | ✅ |
| 8 | PayrollDPEODefaultPaydateOffset | DEFAULT_PAYDATE_OFFSET | — | ✅ |
| 9 | PayrollDPEODefaultPaymentMethodId | DEFAULT_PAYMENT_METHOD_ID | — | — |
| 10 | PayrollDPEOFirstPeriodEndDate | FIRST_PERIOD_END_DATE | — | ✅ |
| 11 | PayrollDPEOGlSetOfBooksId | GL_SET_OF_BOOKS_ID | — | — |
| 12 | PayrollDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PayrollDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | PayrollDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | PayrollDPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 16 | PayrollDPEONegativePayAllowedFlag | NEGATIVE_PAY_ALLOWED_FLAG | — | ✅ |
| 17 | PayrollDPEONumberOfYears | NUMBER_OF_YEARS | — | ✅ |
| 18 | PayrollDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | PayrollDPEOPayrollName | PAYROLL_NAME | — | ✅ |
| 20 | PayrollDPEOPayslipViewDateOffset | PAYSLIP_VIEW_DATE_OFFSET | — | ✅ |
| 21 | PayrollDPEOPeriodResetYears | PERIOD_RESET_YEARS | — | ✅ |
| 22 | PayrollDPEOPeriodType | PERIOD_TYPE | — | ✅ |
| 23 | PayrollDPEORegularEarnDateOffset | REGULAR_EARN_DATE_OFFSET | — | ✅ |
| 24 | PayrollDPEORegularProcessDateOffset | REGULAR_PROCESS_DATE_OFFSET | — | ✅ |
| 25 | PayrollDPEOTimeDefinitionId | TIME_DEFINITION_ID | — | — |
| 26 | PayrollId | PAYROLL_ID | 🔑 | ✅ |

### [[pay_consolidation_sets|PAY_CONSOLIDATION_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConsolidationSetId | CONSOLIDATION_SET_ID | — | — |
| 2 | ConsolidationSetName | CONSOLIDATION_SET_NAME | — | ✅ |

### [[pay_org_pay_methods_vl|PAY_ORG_PAY_METHODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BaseOrgPayMethodName | BASE_ORG_PAY_METHOD_NAME | — | ✅ |
| 2 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 3 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 4 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | OrgPaymentMethodId | ORG_PAYMENT_METHOD_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
