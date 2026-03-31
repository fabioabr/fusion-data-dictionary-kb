---
id: DOC-HCM-510
doc_type: system-doc
title: "IBY_DEBIT_AUTHORIZATIONS_F — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - IBY_DEBIT_AUTHORIZATIONS_F
  - iby_debit_authorizations_f
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# IBY_DEBIT_AUTHORIZATIONS_F

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | AMENDMENT_REASON_CODE | — | — | — | — | — | — |
| 2 | AUTHORIZATION_REFERENCE_NUMBER | — | — | — | — | — | — |
| 3 | AUTHORIZATION_REVISION_NUMBER | — | — | — | — | — | — |
| 4 | AUTH_CANCEL_DATE | — | — | — | — | — | — |
| 5 | AUTH_SIGN_DATE | — | — | — | — | — | — |
| 6 | CREDITOR_IDENTIFIER | — | — | — | — | — | — |
| 7 | DEBIT_AUTHORIZATION_ID | — | — | — | — | — | — |
| 8 | DEBIT_AUTH_METHOD | — | — | — | — | — | — |
| 9 | DEBTOR_PARTY_ID | — | — | — | — | — | — |
| 10 | EFFECTIVE_END_DATE | — | — | — | — | — | — |
| 11 | EFFECTIVE_START_DATE | — | — | — | — | — | — |
| 12 | EXTERNAL_BANK_ACCOUNT_ID | — | — | — | — | — | — |
| 13 | PAYMENT_TYPE_CODE | — | — | — | — | — | — |
| 14 | PRIMARY_FLAG | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[debitauthorizations|DebitAuthorizations]] (AR · BICC: 12/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMENDMENT_REASON_CODE | DebitAuthorizeAmendmentReasonCode | ✅ |
| AUTH_CANCEL_DATE | DebitAuthorizeAuthCancelDate | ✅ |
| AUTH_SIGN_DATE | DebitAuthorizeAuthSignDate | ✅ |
| AUTHORIZATION_REFERENCE_NUMBER | DebitAuthorizeAuthorizationReferenceNumber | ✅ |
| AUTHORIZATION_REVISION_NUMBER | DebitAuthorizeAuthorizationRevisionNumber | ✅ |
| CREDITOR_IDENTIFIER | DebitAuthorizeCreditorIdentifier | ✅ |
| DEBIT_AUTH_METHOD | DebitAuthorizeDebitAuthMethod | ✅ |
| DEBIT_AUTHORIZATION_ID | DebitAuthorizeDebitAuthorizationId | ✅ |
| DEBTOR_PARTY_ID | DebitAuthorizeDebtorPartyId | — |
| EFFECTIVE_END_DATE | DebitAuthorizeEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | DebitAuthorizeEffectiveStartDate | ✅ |
| EXTERNAL_BANK_ACCOUNT_ID | DebitAuthorizeExternalBankAccountId | — |
| PAYMENT_TYPE_CODE | DebitAuthorizePaymentTypeCode | ✅ |
| PRIMARY_FLAG | DebitAuthorizePrimaryFlag | ✅ |
