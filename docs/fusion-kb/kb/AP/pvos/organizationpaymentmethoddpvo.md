---
id: DOC-AP-PVO-OrganizationPaymentMethodDPVO
doc_type: system-doc
title: "OrganizationPaymentMethodDPVO — PVO Accounts Payable"
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
  - OrganizationPaymentMethodDPVO
  - organizationpaymentmethoddpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrganizationPaymentMethodDPVO

## 📌 Visão Geral

Extrai os métodos de pagamento configurados por organização na folha de pagamento, incluindo tipo de pagamento e tradução. Permite mapear as formas de pagamento habilitadas para cada unidade organizacional no processo de folha.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayPaymentSetupAM.OrganizationPaymentMethodDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 4 | 3 | 23 | 68% |

---

## 🔗 Tabelas Relacionadas

- [[pay_org_pay_methods_f|PAY_ORG_PAY_METHODS_F]] — 19 atributos (3 PKs, 13 BICC)
- [[pay_org_pay_methods_tl|PAY_ORG_PAY_METHODS_TL]] — 4 atributos (2 BICC)
- [[pay_payment_types|PAY_PAYMENT_TYPES]] — 6 atributos (5 BICC)
- [[pay_payment_types_tl|PAY_PAYMENT_TYPES_TL]] — 5 atributos (3 BICC)

---

## ⚙️ Atributos

### [[pay_org_pay_methods_f|PAY_ORG_PAY_METHODS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | OrgPaymentMethodId | ORG_PAYMENT_METHOD_ID | 🔑 | ✅ |
| 4 | OrgnPaymentMethodBaseDPEOBankAccountId | BANK_ACCOUNT_ID | — | ✅ |
| 5 | OrgnPaymentMethodBaseDPEOBaseOrgPayMethodName | BASE_ORG_PAY_METHOD_NAME | — | ✅ |
| 6 | OrgnPaymentMethodBaseDPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | OrgnPaymentMethodBaseDPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | OrgnPaymentMethodBaseDPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 9 | OrgnPaymentMethodBaseDPEODefinedBalanceId | DEFINED_BALANCE_ID | — | — |
| 10 | OrgnPaymentMethodBaseDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | OrgnPaymentMethodBaseDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | OrgnPaymentMethodBaseDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | OrgnPaymentMethodBaseDPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 14 | OrgnPaymentMethodBaseDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | OrgnPaymentMethodBaseDPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 16 | OrgnPaymentMethodBaseDPEOParentOrgPayMethodId | PARENT_ORG_PAY_METHOD_ID | — | — |
| 17 | OrgnPaymentMethodBaseDPEOPaymentTypeId | PAYMENT_TYPE_ID | — | — |
| 18 | OrgnPaymentMethodBaseDPEOTimeDefinitionId | TIME_DEFINITION_ID | — | — |
| 19 | OrgnPaymentMethodBaseDPEOType | TYPE | — | ✅ |

### [[pay_org_pay_methods_tl|PAY_ORG_PAY_METHODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgnPaymentMethodTrasltnPEOLanguage | LANGUAGE | — | ✅ |
| 2 | OrgnPaymentMethodTrasltnPEOOrgPaymentMethodId | ORG_PAYMENT_METHOD_ID | — | — |
| 3 | OrgnPaymentMethodTrasltnPEOOrgPaymentMethodName | ORG_PAYMENT_METHOD_NAME | — | ✅ |
| 4 | OrgnPaymentMethodTrasltnPEOSourceLang | SOURCE_LANG | — | — |

### [[pay_payment_types|PAY_PAYMENT_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentTypeBasePEOAllowAsDefault | ALLOW_AS_DEFAULT | — | ✅ |
| 2 | PaymentTypeBasePEOBasePaymentTypeName | BASE_PAYMENT_TYPE_NAME | — | ✅ |
| 3 | PaymentTypeBasePEOCategory | CATEGORY | — | ✅ |
| 4 | PaymentTypeBasePEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 5 | PaymentTypeBasePEOModuleId | MODULE_ID | — | — |
| 6 | PaymentTypeBasePEOPaymentTypeId | PAYMENT_TYPE_ID | — | ✅ |

### [[pay_payment_types_tl|PAY_PAYMENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 2 | PaymentTypeTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 3 | PaymentTypeTranslationPEOPaymentTypeId | PAYMENT_TYPE_ID | — | — |
| 4 | PaymentTypeTranslationPEOPaymentTypeName | PAYMENT_TYPE_NAME | — | ✅ |
| 5 | PaymentTypeTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
