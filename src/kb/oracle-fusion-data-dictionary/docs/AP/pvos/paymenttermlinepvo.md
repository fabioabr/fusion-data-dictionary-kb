---
id: DOC-AP-PVO-PaymentTermLinePVO
doc_type: system-doc
title: "PaymentTermLinePVO — PVO Accounts Payable"
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

Extrai as linhas das condições de pagamento, incluindo percentual por parcela, dias de vencimento e tipo de desconto. Permite detalhar a composição de cada condição de pagamento (ex: 50% em 30 dias + 50% em 60 dias).

**Caminho:** `FscmTopModelAM.FinApInvSetupPmtTermsAM.PaymentTermLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 41 | 2 | 3 | 14 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[ap_terms_lines|AP_TERMS_LINES]] — 27 atributos (3 PKs, 8 BICC)
- [[ap_terms_vl|AP_TERMS_VL]] — 14 atributos (6 BICC)

---

## ⚙️ Atributos

### [[ap_terms_lines|AP_TERMS_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentTermLineCalendar | CALENDAR | — | — |
| 2 | PaymentTermLineCreatedBy | CREATED_BY | — | — |
| 3 | PaymentTermLineCreationDate | CREATION_DATE | — | — |
| 4 | PaymentTermLineDiscountDayOfMonth | DISCOUNT_DAY_OF_MONTH | — | — |
| 5 | PaymentTermLineDiscountDayOfMonth2 | DISCOUNT_DAY_OF_MONTH_2 | — | — |
| 6 | PaymentTermLineDiscountDayOfMonth3 | DISCOUNT_DAY_OF_MONTH_3 | — | — |
| 7 | PaymentTermLineDiscountDays | DISCOUNT_DAYS | — | — |
| 8 | PaymentTermLineDiscountDays2 | DISCOUNT_DAYS_2 | — | — |
| 9 | PaymentTermLineDiscountDays3 | DISCOUNT_DAYS_3 | — | — |
| 10 | PaymentTermLineDiscountMonthsForward | DISCOUNT_MONTHS_FORWARD | — | — |
| 11 | PaymentTermLineDiscountMonthsForward2 | DISCOUNT_MONTHS_FORWARD_2 | — | — |
| 12 | PaymentTermLineDiscountMonthsForward3 | DISCOUNT_MONTHS_FORWARD_3 | — | — |
| 13 | PaymentTermLineDiscountPercent | DISCOUNT_PERCENT | — | — |
| 14 | PaymentTermLineDiscountPercent2 | DISCOUNT_PERCENT_2 | — | — |
| 15 | PaymentTermLineDiscountPercent3 | DISCOUNT_PERCENT_3 | — | — |
| 16 | PaymentTermLineDueAmount | DUE_AMOUNT | — | ✅ |
| 17 | PaymentTermLineDueDayOfMonth | DUE_DAY_OF_MONTH | — | ✅ |
| 18 | PaymentTermLineDueDays | DUE_DAYS | — | ✅ |
| 19 | PaymentTermLineDueMonthsForward | DUE_MONTHS_FORWARD | — | ✅ |
| 20 | PaymentTermLineDuePercent | DUE_PERCENT | — | ✅ |
| 21 | PaymentTermLineFixedDate | FIXED_DATE | — | — |
| 22 | PaymentTermLineLastUpdateDate | LAST_UPDATE_DATE | 🔑 | ✅ |
| 23 | PaymentTermLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | PaymentTermLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | PaymentTermLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | SequenceNum | SEQUENCE_NUM | 🔑 | ✅ |
| 27 | TermId | TERM_ID | 🔑 | ✅ |

### [[ap_terms_vl|AP_TERMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentTermHeaderCreatedBy | CREATED_BY | — | ✅ |
| 2 | PaymentTermHeaderCreationDate | CREATION_DATE | — | ✅ |
| 3 | PaymentTermHeaderDescription | DESCRIPTION | — | — |
| 4 | PaymentTermHeaderDueCutoffDay | DUE_CUTOFF_DAY | — | — |
| 5 | PaymentTermHeaderEnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | PaymentTermHeaderEndDateActive | END_DATE_ACTIVE | — | — |
| 7 | PaymentTermHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PaymentTermHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PaymentTermHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PaymentTermHeaderName | NAME | — | — |
| 11 | PaymentTermHeaderRank | RANK | — | — |
| 12 | PaymentTermHeaderStartDateActive | START_DATE_ACTIVE | — | — |
| 13 | PaymentTermHeaderTermId | TERM_ID | — | ✅ |
| 14 | PaymentTermHeaderType | TYPE | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
