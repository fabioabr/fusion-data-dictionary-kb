---
id: DOC-OTHER-PVO-PaymentBatch
doc_type: system-doc
title: "PaymentBatch — PVO Cross-Module"
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
  - PaymentBatch
  - paymentbatch
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentBatch

## 📌 Visão Geral

View Object para extração BICC de dados de Payment Batch. Acessa as tabelas: CN_PAY_GROUPS_ALL_TL, CN_PERIODS_TL, CN_PRD_STATUSES_ALL (+2).

**Caminho:** `FscmTopModelAM.PayrunAM.PaymentBatch`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 5 | 1 | 13 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[cn_pay_groups_all_tl|CN_PAY_GROUPS_ALL_TL]] — 4 atributos (1 BICC)
- [[cn_periods_tl|CN_PERIODS_TL]] — 4 atributos (2 BICC)
- [[cn_prd_statuses_all|CN_PRD_STATUSES_ALL]] — 2 atributos
- [[cn_tp_payruns_all|CN_TP_PAYRUNS_ALL]] — 17 atributos (1 PKs, 9 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cn_pay_groups_all_tl|CN_PAY_GROUPS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language1 | LANGUAGE | — | — |
| 2 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 3 | PayGroupId1 | PAY_GROUP_ID | — | — |
| 4 | PayGroupName | PAY_GROUP_NAME | — | ✅ |

### [[cn_periods_tl|CN_PERIODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalendarId | CALENDAR_ID | — | — |
| 2 | Language | LANGUAGE | — | ✅ |
| 3 | PeriodId | PERIOD_ID | — | — |
| 4 | PeriodName | PERIOD_NAME | — | ✅ |

### [[cn_prd_statuses_all|CN_PRD_STATUSES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PeriodStatusPEOOrgId | ORG_ID | — | — |
| 2 | PeriodStatusPEOPeriodId | PERIOD_ID | — | — |

### [[cn_tp_payruns_all|CN_TP_PAYRUNS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustComments | ADJUST_COMMENTS | — | ✅ |
| 2 | AdjustStatus | ADJUST_STATUS | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | — |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | IncentiveTypeCode | INCENTIVE_TYPE_CODE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ObjectStatus | OBJECT_STATUS | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | OrgId | ORG_ID | — | — |
| 12 | PayDate | PAY_DATE | — | ✅ |
| 13 | PayGroupId | PAY_GROUP_ID | — | — |
| 14 | PayPeriodId | PAY_PERIOD_ID | — | — |
| 15 | PayrunId | PAYRUN_ID | 🔑 | ✅ |
| 16 | PayrunMode | PAYRUN_MODE | — | ✅ |
| 17 | PayrunName | PAYRUN_NAME | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |
| 2 | Name | BU_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
