---
id: DOC-AR-PVO-PaymentTermBPVO
doc_type: system-doc
title: "PaymentTermBPVO — PVO Accounts Receivable"
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
  - PaymentTermBPVO
  - paymenttermbpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentTermBPVO

## 📌 Visão Geral

Extrai as condições de pagamento (payment terms) cadastradas no sistema, com datas-base, percentuais de desconto e prazos. Define as regras de parcelamento e descontos aplicáveis às transações de recebíveis.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.PaymentTermBPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 1 | 1 | 5 | 22% |

---

## 🔗 Tabelas Relacionadas

- [[ra_terms_b|RA_TERMS_B]] — 23 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[ra_terms_b|RA_TERMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BaseAmount | BASE_AMOUNT | — | ✅ |
| 2 | BillingCycleId | BILLING_CYCLE_ID | — | — |
| 3 | CalcDiscountOnLinesFlag | CALC_DISCOUNT_ON_LINES_FLAG | — | — |
| 4 | CreatedBy | CREATED_BY | — | — |
| 5 | CreationDate | CREATION_DATE | — | — |
| 6 | CreditCheckFlag | CREDIT_CHECK_FLAG | — | — |
| 7 | Description | DESCRIPTION | — | — |
| 8 | DueCutoffDay | DUE_CUTOFF_DAY | — | — |
| 9 | EndDateActive | END_DATE_ACTIVE | — | — |
| 10 | FirstInstallmentCode | FIRST_INSTALLMENT_CODE | — | — |
| 11 | InUse | IN_USE | — | — |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | ModuleId | MODULE_ID | — | — |
| 16 | Name | NAME | — | — |
| 17 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | PartialDiscountFlag | PARTIAL_DISCOUNT_FLAG | — | — |
| 19 | PrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 20 | PrintingLeadDays | PRINTING_LEAD_DAYS | — | ✅ |
| 21 | SetId | SET_ID | — | ✅ |
| 22 | StartDateActive | START_DATE_ACTIVE | — | — |
| 23 | TermId | TERM_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
