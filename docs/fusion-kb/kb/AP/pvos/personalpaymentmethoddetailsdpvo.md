---
id: DOC-AP-PVO-PersonalPaymentMethodDetailsDPVO
doc_type: system-doc
title: "PersonalPaymentMethodDetailsDPVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PersonalPaymentMethodDetailsDPVO
  - personalpaymentmethoddetailsdpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonalPaymentMethodDetailsDPVO

## 📌 Visão Geral

Extrai os detalhes dos métodos de pagamento pessoais dos colaboradores na folha de pagamento, incluindo método organizacional vinculado e relacionamento trabalhista. Essencial para garantir que cada colaborador receba o pagamento na conta e método corretos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayPaymentSetupAM.PersonalPaymentMethodDetailsDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 4 | 3 | 8 | 22% |

---

## 🔗 Tabelas Relacionadas

- [[pay_org_pay_methods_vl|PAY_ORG_PAY_METHODS_VL]] — 10 atributos (2 BICC)
- [[pay_org_pay_method_usages_f|PAY_ORG_PAY_METHOD_USAGES_F]] — 4 atributos (1 BICC)
- [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]] — 4 atributos
- [[pay_person_pay_methods_f|PAY_PERSON_PAY_METHODS_F]] — 19 atributos (3 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[pay_org_pay_methods_vl|PAY_ORG_PAY_METHODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationPaymentMethodDPECurrencyCode | CURRENCY_CODE | — | — |
| 2 | OrganizationPaymentMethodDPEEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrganizationPaymentMethodDPEEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | OrganizationPaymentMethodDPEObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | OrganizationPaymentMethodDPEOrgPaymentMethodId | ORG_PAYMENT_METHOD_ID | — | — |
| 6 | PaymentSourceDPEOBankAccountId | BANK_ACCOUNT_ID | — | — |
| 7 | PaymentSourceDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PaymentSourceDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | PaymentSourceDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PaymentSourceDPEOOrgPaymentMethodId | ORG_PAYMENT_METHOD_ID | — | — |

### [[pay_org_pay_method_usages_f|PAY_ORG_PAY_METHOD_USAGES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgPaymentMethodUsageDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrgPaymentMethodUsageDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OrgPaymentMethodUsageDPEOOrgPayMethodUsageId | ORG_PAY_METHOD_USAGE_ID | — | — |
| 4 | OrgPaymentMethodUsageDPEOPayrollId | PAYROLL_ID | — | — |

### [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollRelationshipPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | PayrollRelationshipPEOPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | — |
| 3 | PayrollRelationshipPEOPayrollStatUnitId | PAYROLL_STAT_UNIT_ID | — | — |
| 4 | PayrollRelationshipPEOPersonId | PERSON_ID | — | — |

### [[pay_person_pay_methods_f|PAY_PERSON_PAY_METHODS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | PersonalPaymentMethodDPEOAmount | AMOUNT | — | ✅ |
| 4 | PersonalPaymentMethodDPEOBankAccountId | BANK_ACCOUNT_ID | — | — |
| 5 | PersonalPaymentMethodDPEOCreatedBy | CREATED_BY | — | — |
| 6 | PersonalPaymentMethodDPEOCreationDate | CREATION_DATE | — | — |
| 7 | PersonalPaymentMethodDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PersonalPaymentMethodDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PersonalPaymentMethodDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PersonalPaymentMethodDPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 11 | PersonalPaymentMethodDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PersonalPaymentMethodDPEOOrgPaymentMethodId | ORG_PAYMENT_METHOD_ID | — | — |
| 13 | PersonalPaymentMethodDPEOPaymentAmountType | PAYMENT_AMOUNT_TYPE | — | — |
| 14 | PersonalPaymentMethodDPEOPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | — |
| 15 | PersonalPaymentMethodDPEOPercentage | PERCENTAGE | — | — |
| 16 | PersonalPaymentMethodDPEOPriority | PRIORITY | — | — |
| 17 | PersonalPaymentMethodDPEORunTypeId | RUN_TYPE_ID | — | — |
| 18 | PersonalPaymentMethodDPEOThirdPartyPayeeId | THIRD_PARTY_PAYEE_ID | — | — |
| 19 | PersonalPaymentMethodId | PERSONAL_PAYMENT_METHOD_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
