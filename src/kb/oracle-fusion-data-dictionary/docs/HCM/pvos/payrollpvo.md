---
id: DOC-HCM-PVO-PayrollPVO
doc_type: system-doc
title: "PayrollPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PayrollPVO
  - payrollpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PayrollPVO

## 📌 Visão Geral

Extrai o cadastro de folhas de pagamento com método de pagamento base e conjunto de consolidação. Base dimensional para vinculação de colaboradores a ciclos de processamento de payroll.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayCoreAM.PayrollPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 3 | 1 | 21 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[pay_all_payrolls_f|PAY_ALL_PAYROLLS_F]] — 26 atributos (1 PKs, 19 BICC)
- [[pay_consolidation_sets|PAY_CONSOLIDATION_SETS]] — 2 atributos (1 BICC)
- [[pay_org_pay_methods_vl|PAY_ORG_PAY_METHODS_VL]] — 5 atributos (1 BICC)

---

## ⚙️ Atributos

### [[pay_all_payrolls_f|PAY_ALL_PAYROLLS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollId | PAYROLL_ID | 🔑 | ✅ |
| 2 | PayrollPEOConsolidationSetId | CONSOLIDATION_SET_ID | — | — |
| 3 | PayrollPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | PayrollPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | PayrollPEOCutOffDateOffset | CUT_OFF_DATE_OFFSET | — | ✅ |
| 6 | PayrollPEODefaultPaydateOffset | DEFAULT_PAYDATE_OFFSET | — | ✅ |
| 7 | PayrollPEODefaultPaymentMethodId | DEFAULT_PAYMENT_METHOD_ID | — | — |
| 8 | PayrollPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 9 | PayrollPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 10 | PayrollPEOFirstPeriodEndDate | FIRST_PERIOD_END_DATE | — | ✅ |
| 11 | PayrollPEOFixedDate | FIXED_DATE | — | ✅ |
| 12 | PayrollPEOGlSetOfBooksId | GL_SET_OF_BOOKS_ID | — | — |
| 13 | PayrollPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | PayrollPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | PayrollPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | PayrollPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 17 | PayrollPEONegativePayAllowedFlag | NEGATIVE_PAY_ALLOWED_FLAG | — | ✅ |
| 18 | PayrollPEONumberOfYears | NUMBER_OF_YEARS | — | ✅ |
| 19 | PayrollPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | PayrollPEOPayrollName | PAYROLL_NAME | — | ✅ |
| 21 | PayrollPEOPayslipViewDateOffset | PAYSLIP_VIEW_DATE_OFFSET | — | ✅ |
| 22 | PayrollPEOPeriodResetYears | PERIOD_RESET_YEARS | — | ✅ |
| 23 | PayrollPEOPeriodType | PERIOD_TYPE | — | ✅ |
| 24 | PayrollPEORegularEarnDateOffset | REGULAR_EARN_DATE_OFFSET | — | ✅ |
| 25 | PayrollPEORegularProcessDateOffset | REGULAR_PROCESS_DATE_OFFSET | — | ✅ |
| 26 | PayrollPEOTimeDefinitionId | TIME_DEFINITION_ID | — | — |

### [[pay_consolidation_sets|PAY_CONSOLIDATION_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConsolidationSetId | CONSOLIDATION_SET_ID | — | — |
| 2 | ConsolidationSetName | CONSOLIDATION_SET_NAME | — | ✅ |

### [[pay_org_pay_methods_vl|PAY_ORG_PAY_METHODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BaseOrgPayMethodName | BASE_ORG_PAY_METHOD_NAME | — | ✅ |
| 2 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | OrgPaymentMethodId | ORG_PAYMENT_METHOD_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
