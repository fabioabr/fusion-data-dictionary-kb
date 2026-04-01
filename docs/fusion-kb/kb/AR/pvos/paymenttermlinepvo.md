---
id: DOC-AR-PVO-PaymentTermLinePVO
doc_type: system-doc
title: "PaymentTermLinePVO — PVO Accounts Receivable"
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
  - PaymentTermLinePVO
  - paymenttermlinepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentTermLinePVO

## 📌 Visão Geral

Extrai as linhas de condições de pagamento, detalhando cada parcela da condição (percentual, dias de vencimento, desconto por antecipação). Permite configurar esquemas complexos de parcelamento e incentivos de pagamento antecipado.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.PaymentTermLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 2 | 2 | 16 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[ra_terms_b|RA_TERMS_B]] — 23 atributos (8 BICC)
- [[ra_terms_lines|RA_TERMS_LINES]] — 14 atributos (2 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[ra_terms_b|RA_TERMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentTermBaseAmount | BASE_AMOUNT | — | ✅ |
| 2 | PaymentTermBillingCycleId | BILLING_CYCLE_ID | — | — |
| 3 | PaymentTermCalcDiscountOnLinesFlag | CALC_DISCOUNT_ON_LINES_FLAG | — | — |
| 4 | PaymentTermCreatedBy | CREATED_BY | — | ✅ |
| 5 | PaymentTermCreationDate | CREATION_DATE | — | ✅ |
| 6 | PaymentTermCreditCheckFlag | CREDIT_CHECK_FLAG | — | — |
| 7 | PaymentTermDescription | DESCRIPTION | — | — |
| 8 | PaymentTermDueCutoffDay | DUE_CUTOFF_DAY | — | — |
| 9 | PaymentTermEndDateActive | END_DATE_ACTIVE | — | — |
| 10 | PaymentTermFirstInstallmentCode | FIRST_INSTALLMENT_CODE | — | — |
| 11 | PaymentTermInUse | IN_USE | — | — |
| 12 | PaymentTermLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PaymentTermLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | PaymentTermLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | PaymentTermModuleId | MODULE_ID | — | — |
| 16 | PaymentTermName | NAME | — | — |
| 17 | PaymentTermObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | PaymentTermPartialDiscountFlag | PARTIAL_DISCOUNT_FLAG | — | — |
| 19 | PaymentTermPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 20 | PaymentTermPrintingLeadDays | PRINTING_LEAD_DAYS | — | ✅ |
| 21 | PaymentTermSetId | SET_ID | — | ✅ |
| 22 | PaymentTermStartDateActive | START_DATE_ACTIVE | — | — |
| 23 | PaymentTermTermId | TERM_ID | — | ✅ |

### [[ra_terms_lines|RA_TERMS_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentTermLineCreatedBy | CREATED_BY | — | — |
| 2 | PaymentTermLineCreationDate | CREATION_DATE | — | — |
| 3 | PaymentTermLineDueDate | DUE_DATE | — | — |
| 4 | PaymentTermLineDueDayOfMonth | DUE_DAY_OF_MONTH | — | ✅ |
| 5 | PaymentTermLineDueDays | DUE_DAYS | — | ✅ |
| 6 | PaymentTermLineDueMonthsForward | DUE_MONTHS_FORWARD | — | ✅ |
| 7 | PaymentTermLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PaymentTermLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PaymentTermLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PaymentTermLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PaymentTermLineRelativeAmount | RELATIVE_AMOUNT | — | ✅ |
| 12 | PaymentTermLineSetId | SET_ID | — | ✅ |
| 13 | SequenceNum | SEQUENCE_NUM | 🔑 | ✅ |
| 14 | TermId | TERM_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
