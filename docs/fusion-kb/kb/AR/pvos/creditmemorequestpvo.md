---
id: DOC-AR-PVO-CreditMemoRequestPVO
doc_type: system-doc
title: "CreditMemoRequestPVO — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CreditMemoRequestPVO
  - creditmemorequestpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CreditMemoRequestPVO

## 📌 Visão Geral

Extrai as solicitações de notas de crédito (credit memo requests), com motivo, valor, status de aprovação e transação de origem. Viabiliza o controle do fluxo de aprovação de créditos e análise de motivos de concessão (devoluções, bonificações, correções).

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.CreditMemoRequestPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 62 | 5 | 2 | 15 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 2 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 8 atributos
- [[ra_cm_requests_all|RA_CM_REQUESTS_ALL]] — 40 atributos (2 PKs, 15 BICC)
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 2 atributos

---

## ⚙️ Atributos

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitName | BU_NAME | — | — |

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
| 1 | UserCreatedByPersonId | PERSON_ID | — | — |
| 2 | UserCreatedByUserGuid | USER_GUID | — | — |
| 3 | UserCreatedByUserId | USER_ID | — | — |
| 4 | UserCreatedByUsername | USERNAME | — | — |
| 5 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 6 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 7 | UserUpdatedByUserId | USER_ID | — | — |
| 8 | UserUpdatedByUsername | USERNAME | — | — |

### [[ra_cm_requests_all|RA_CM_REQUESTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivitiesUrl | ACTIVITIES_URL | — | — |
| 2 | ApprovalDate | APPROVAL_DATE | — | ✅ |
| 3 | CmCustomerTrxId | CM_CUSTOMER_TRX_ID | — | — |
| 4 | CmReasonCode | CM_REASON_CODE | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | CustomerTrxId | CUSTOMER_TRX_ID | 🔑 | ✅ |
| 8 | FreightAmount | FREIGHT_AMOUNT | — | ✅ |
| 9 | InterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 10 | InterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 11 | InterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 12 | InterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 13 | InterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 14 | InterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 15 | InterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 16 | InterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 17 | InterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 18 | InterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 19 | InterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 20 | InterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 21 | InterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 22 | InterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 23 | InterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 24 | InterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 25 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | LineAmount | LINE_AMOUNT | — | ✅ |
| 29 | LineCreditsFlag | LINE_CREDITS_FLAG | — | ✅ |
| 30 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 31 | OrgId | ORG_ID | — | — |
| 32 | OrigTrxNumber | ORIG_TRX_NUMBER | — | ✅ |
| 33 | RequestId | REQUEST_ID | 🔑 | ✅ |
| 34 | Status | STATUS | — | — |
| 35 | TaxAmount | TAX_AMOUNT | — | ✅ |
| 36 | TaxExCertNum | TAX_EX_CERT_NUM | — | ✅ |
| 37 | TermsSequenceNumber | TERMS_SEQUENCE_NUMBER | — | — |
| 38 | TotalAmount | TOTAL_AMOUNT | — | ✅ |
| 39 | TransactionUrl | TRANSACTION_URL | — | — |
| 40 | Url | URL | — | — |

### [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionHeaderCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 2 | TransactionHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
