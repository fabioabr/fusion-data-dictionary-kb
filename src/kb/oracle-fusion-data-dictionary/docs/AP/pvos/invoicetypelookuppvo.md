---
id: DOC-AP-PVO-InvoiceTypeLookupPVO
doc_type: system-doc
title: "InvoiceTypeLookupPVO — PVO Accounts Payable"
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
  - InvoiceTypeLookupPVO
  - invoicetypelookuppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvoiceTypeLookupPVO

## 📌 Visão Geral

Extrai a tabela de lookup de tipos de fatura no módulo de contas a pagar (standard, crédito, débito, prepayment). Serve como referência para classificar e filtrar faturas por natureza da transação.

**Caminho:** `FscmTopModelAM.FinApSharedCoreAM.InvoiceTypeLookupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 7 | 1 | 2 | 5 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[ap_lookup_codes|AP_LOOKUP_CODES]] — 7 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[ap_lookup_codes|AP_LOOKUP_CODES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | DisplayedField | DISPLAYED_FIELD | — | ✅ |
| 3 | EnabledFlag | ENABLED_FLAG | — | — |
| 4 | EndDateActive | END_DATE_ACTIVE | — | — |
| 5 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 6 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 7 | StartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
