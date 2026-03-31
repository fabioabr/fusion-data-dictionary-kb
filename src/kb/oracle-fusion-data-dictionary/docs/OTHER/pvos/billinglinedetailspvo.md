---
id: DOC-OTHER-PVO-BillingLineDetailsPVO
doc_type: system-doc
title: "BillingLineDetailsPVO — PVO Cross-Module"
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
  - BillingLineDetailsPVO
  - billinglinedetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillingLineDetailsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Billing Line Details. Acessa as tabelas: PER_PERSON_NAMES_F_V, PER_USERS, VRM_BILLING_LINE_DETAILS.

**Caminho:** `FscmTopModelAM.FinVrmRRSharedPublicModelAM.BillingLineDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 3 | 1 | 18 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 10 atributos
- [[vrm_billing_line_details|VRM_BILLING_LINE_DETAILS]] — 38 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByPersonId | PERSON_ID | — | — |
| 3 | UserCreatedByUserGuid | USER_GUID | — | — |
| 4 | UserCreatedByUserId | USER_ID | — | — |
| 5 | UserCreatedByUsername | USERNAME | — | — |
| 6 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

### [[vrm_billing_line_details|VRM_BILLING_LINE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillingLineDetailId | BILLING_LINE_DETAIL_ID | 🔑 | ✅ |
| 2 | BillingLineDetailsBillAccountingDate | BILL_ACCOUNTING_DATE | — | ✅ |
| 3 | BillingLineDetailsBillAcctdAmount | BILL_ACCTD_AMOUNT | — | — |
| 4 | BillingLineDetailsBillAmount | BILL_AMOUNT | — | — |
| 5 | BillingLineDetailsBillDate | BILL_DATE | — | ✅ |
| 6 | BillingLineDetailsBillId | BILL_ID | — | — |
| 7 | BillingLineDetailsBillLineId | BILL_LINE_ID | — | — |
| 8 | BillingLineDetailsBillLineNumber | BILL_LINE_NUMBER | — | ✅ |
| 9 | BillingLineDetailsBillNumber | BILL_NUMBER | — | ✅ |
| 10 | BillingLineDetailsBillQuantity | BILL_QUANTITY | — | — |
| 11 | BillingLineDetailsBillSubLineId | BILL_SUB_LINE_ID | — | — |
| 12 | BillingLineDetailsBillingApplication | BILLING_APPLICATION | — | ✅ |
| 13 | BillingLineDetailsBillingDataProcessedStatus | BILLING_DATA_PROCESSED_STATUS | — | ✅ |
| 14 | BillingLineDetailsCreatedBy1 | CREATED_BY | — | ✅ |
| 15 | BillingLineDetailsCreationDate | CREATION_DATE | — | ✅ |
| 16 | BillingLineDetailsDocLineIdChar1 | DOC_LINE_ID_CHAR_1 | — | — |
| 17 | BillingLineDetailsDocLineIdChar2 | DOC_LINE_ID_CHAR_2 | — | — |
| 18 | BillingLineDetailsDocLineIdChar3 | DOC_LINE_ID_CHAR_3 | — | — |
| 19 | BillingLineDetailsDocLineIdChar4 | DOC_LINE_ID_CHAR_4 | — | — |
| 20 | BillingLineDetailsDocLineIdChar5 | DOC_LINE_ID_CHAR_5 | — | — |
| 21 | BillingLineDetailsDocLineIdInt1 | DOC_LINE_ID_INT_1 | — | — |
| 22 | BillingLineDetailsDocLineIdInt2 | DOC_LINE_ID_INT_2 | — | — |
| 23 | BillingLineDetailsDocLineIdInt3 | DOC_LINE_ID_INT_3 | — | — |
| 24 | BillingLineDetailsDocLineIdInt4 | DOC_LINE_ID_INT_4 | — | — |
| 25 | BillingLineDetailsDocLineIdInt5 | DOC_LINE_ID_INT_5 | — | — |
| 26 | BillingLineDetailsDocumentLineId | DOCUMENT_LINE_ID | — | — |
| 27 | BillingLineDetailsDocumentTypeId | DOCUMENT_TYPE_ID | — | — |
| 28 | BillingLineDetailsExchangeRate | EXCHANGE_RATE | — | ✅ |
| 29 | BillingLineDetailsExchangeRateDate | EXCHANGE_RATE_DATE | — | ✅ |
| 30 | BillingLineDetailsExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 31 | BillingLineDetailsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | BillingLineDetailsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | BillingLineDetailsLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 34 | BillingLineDetailsLoadRequestId | LOAD_REQUEST_ID | — | — |
| 35 | BillingLineDetailsSourceDocumentDate | SOURCE_DOCUMENT_DATE | — | ✅ |
| 36 | BillingLineDetailsSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | ✅ |
| 37 | BillingLineDetailsSourceDocumentNumber | SOURCE_DOCUMENT_NUMBER | — | ✅ |
| 38 | BillingLineDetailsSourceSystem | SOURCE_SYSTEM | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
