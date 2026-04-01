---
id: DOC-AP-PVO-PaymentMethodLookupPVO
doc_type: system-doc
title: "PaymentMethodLookupPVO — PVO Accounts Payable"
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
  - PaymentMethodLookupPVO
  - paymentmethodlookuppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentMethodLookupPVO

## 📌 Visão Geral

Extrai a tabela de lookup de métodos de pagamento no módulo de contas a pagar (cheque, transferência, boleto). Serve como referência para decodificar os códigos de método de pagamento utilizados nos desembolsos.

**Caminho:** `FscmTopModelAM.FinApSharedCoreAM.PaymentMethodLookupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 7 | 1 | 2 | 3 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[ap_lookup_codes|AP_LOOKUP_CODES]] — 7 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[ap_lookup_codes|AP_LOOKUP_CODES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | — |
| 2 | DisplayedField | DISPLAYED_FIELD | — | — |
| 3 | EnabledFlag | ENABLED_FLAG | — | — |
| 4 | EndDateActive | END_DATE_ACTIVE | — | — |
| 5 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 6 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 7 | StartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
