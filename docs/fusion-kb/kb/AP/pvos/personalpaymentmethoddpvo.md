---
id: DOC-AP-PVO-PersonalPaymentMethodDPVO
doc_type: system-doc
title: "PersonalPaymentMethodDPVO — PVO Accounts Payable"
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
  - PersonalPaymentMethodDPVO
  - personalpaymentmethoddpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonalPaymentMethodDPVO

## 📌 Visão Geral

Extrai os métodos de pagamento pessoais cadastrados para colaboradores na folha de pagamento, incluindo tipo, prioridade e vigência. Permite gerenciar e auditar as preferências de recebimento de salário de cada colaborador.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayPaymentSetupAM.PersonalPaymentMethodDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 3 | 17 | 85% |

---

## 🔗 Tabelas Relacionadas

- [[pay_person_pay_methods_f|PAY_PERSON_PAY_METHODS_F]] — 20 atributos (3 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[pay_person_pay_methods_f|PAY_PERSON_PAY_METHODS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | PersonalPaymentMethodDPEOAmount | AMOUNT | — | ✅ |
| 4 | PersonalPaymentMethodDPEOBankAccountId | BANK_ACCOUNT_ID | — | ✅ |
| 5 | PersonalPaymentMethodDPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | PersonalPaymentMethodDPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | PersonalPaymentMethodDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PersonalPaymentMethodDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PersonalPaymentMethodDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PersonalPaymentMethodDPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 11 | PersonalPaymentMethodDPEOName | NAME | — | ✅ |
| 12 | PersonalPaymentMethodDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | PersonalPaymentMethodDPEOOrgPaymentMethodId | ORG_PAYMENT_METHOD_ID | — | ✅ |
| 14 | PersonalPaymentMethodDPEOPaymentAmountType | PAYMENT_AMOUNT_TYPE | — | ✅ |
| 15 | PersonalPaymentMethodDPEOPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | ✅ |
| 16 | PersonalPaymentMethodDPEOPercentage | PERCENTAGE | — | ✅ |
| 17 | PersonalPaymentMethodDPEOPriority | PRIORITY | — | ✅ |
| 18 | PersonalPaymentMethodDPEORunTypeId | RUN_TYPE_ID | — | ✅ |
| 19 | PersonalPaymentMethodDPEOThirdPartyPayeeId | THIRD_PARTY_PAYEE_ID | — | — |
| 20 | PersonalPaymentMethodId | PERSONAL_PAYMENT_METHOD_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
