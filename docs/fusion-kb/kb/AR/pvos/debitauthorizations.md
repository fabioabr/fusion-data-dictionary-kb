---
id: DOC-AR-PVO-DebitAuthorizations
doc_type: system-doc
title: "DebitAuthorizations — PVO Accounts Receivable"
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
  - DebitAuthorizations
  - debitauthorizations
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DebitAuthorizations

## 📌 Visão Geral

Extrai as autorizações de débito direto concedidas por clientes, incluindo validade, banco autorizado e entidade legal. Permite controlar as autorizações vigentes para cobranças por débito automático e garantir compliance regulatório.

**Caminho:** `FscmTopModelAM.FinArCustomersPublicModelAM.DebitAuthorizations`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 3 | 3 | 14 | 70% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 2 atributos (1 BICC)
- [[iby_debit_authorizations_f|IBY_DEBIT_AUTHORIZATIONS_F]] — 14 atributos (3 PKs, 12 BICC)
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 4 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyId | PARTY_ID | — | — |
| 2 | PartyName | PARTY_NAME | — | ✅ |

### [[iby_debit_authorizations_f|IBY_DEBIT_AUTHORIZATIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DebitAuthorizeAmendmentReasonCode | AMENDMENT_REASON_CODE | — | ✅ |
| 2 | DebitAuthorizeAuthCancelDate | AUTH_CANCEL_DATE | — | ✅ |
| 3 | DebitAuthorizeAuthSignDate | AUTH_SIGN_DATE | — | ✅ |
| 4 | DebitAuthorizeAuthorizationReferenceNumber | AUTHORIZATION_REFERENCE_NUMBER | — | ✅ |
| 5 | DebitAuthorizeAuthorizationRevisionNumber | AUTHORIZATION_REVISION_NUMBER | — | ✅ |
| 6 | DebitAuthorizeCreditorIdentifier | CREDITOR_IDENTIFIER | — | ✅ |
| 7 | DebitAuthorizeDebitAuthMethod | DEBIT_AUTH_METHOD | — | ✅ |
| 8 | DebitAuthorizeDebitAuthorizationId | DEBIT_AUTHORIZATION_ID | 🔑 | ✅ |
| 9 | DebitAuthorizeDebtorPartyId | DEBTOR_PARTY_ID | — | — |
| 10 | DebitAuthorizeEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 11 | DebitAuthorizeEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 12 | DebitAuthorizeExternalBankAccountId | EXTERNAL_BANK_ACCOUNT_ID | — | — |
| 13 | DebitAuthorizePaymentTypeCode | PAYMENT_TYPE_CODE | — | ✅ |
| 14 | DebitAuthorizePrimaryFlag | PRIMARY_FLAG | — | ✅ |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 2 | LegalEntityIdentifier | LEGAL_ENTITY_IDENTIFIER | — | — |
| 3 | LegalEntityName | NAME | — | ✅ |
| 4 | LegalEntityObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
