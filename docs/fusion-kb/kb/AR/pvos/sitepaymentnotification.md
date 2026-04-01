---
id: DOC-AR-PVO-SitePaymentNotification
doc_type: system-doc
title: "SitePaymentNotification — PVO Accounts Receivable"
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
  - SitePaymentNotification
  - sitepaymentnotification
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SitePaymentNotification

## 📌 Visão Geral

Extrai as configurações de notificação de pagamento por site de cliente. Controla as preferências de comunicação sobre cobranças e confirmações de recebimento em cada localidade do cliente.

**Caminho:** `FscmTopModelAM.FinArCustomersPublicModelAM.SitePaymentNotification`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 5 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[iby_external_payers_all|IBY_EXTERNAL_PAYERS_ALL]] — 18 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[iby_external_payers_all|IBY_EXTERNAL_PAYERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExtPayerId | EXT_PAYER_ID | 🔑 | ✅ |
| 2 | PayersAcctSiteUseId | ACCT_SITE_USE_ID | — | — |
| 3 | PayersBankChargeBearerCode | BANK_CHARGE_BEARER_CODE | — | — |
| 4 | PayersCreatedBy | CREATED_BY | — | — |
| 5 | PayersCreationDate | CREATION_DATE | — | — |
| 6 | PayersCustAccountId | CUST_ACCOUNT_ID | — | — |
| 7 | PayersDebitAdviceDeliveryMethod | DEBIT_ADVICE_DELIVERY_METHOD | — | ✅ |
| 8 | PayersDebitAdviceEmail | DEBIT_ADVICE_EMAIL | — | ✅ |
| 9 | PayersDebitAdviceFax | DEBIT_ADVICE_FAX | — | ✅ |
| 10 | PayersDirdebInstructionCode | DIRDEB_INSTRUCTION_CODE | — | — |
| 11 | PayersLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | PayersLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | PayersLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | PayersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | PayersOrgId | ORG_ID | — | — |
| 16 | PayersOrgType | ORG_TYPE | — | — |
| 17 | PayersPartyId | PARTY_ID | — | — |
| 18 | PayersPaymentFunction | PAYMENT_FUNCTION | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
