---
id: DOC-HCM-PVO-PersonAccrualEntryExtractPVO
doc_type: system-doc
title: "PersonAccrualEntryExtractPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PersonAccrualEntryExtractPVO
  - personaccrualentryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAccrualEntryExtractPVO

## 📌 Visão Geral

Extrai os lançamentos de accrual de ausências por período, com saldo inicial e valor provisionado. Permite acompanhar a evolução do saldo de férias e licenças dos colaboradores.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmGblAbsencesBiccExtractAM.PersonAccrualEntryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 19 | 86% |

---

## 🔗 Tabelas Relacionadas

- [[anc_per_accrual_entries|ANC_PER_ACCRUAL_ENTRIES]] — 22 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[anc_per_accrual_entries|ANC_PER_ACCRUAL_ENTRIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrualPeriod | ACCRUAL_PERIOD | — | ✅ |
| 2 | Accrued | ACCRUED | — | ✅ |
| 3 | BeginBal | BEGIN_BAL | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | EndBal | END_BAL | — | ✅ |
| 7 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | PerAccrualEntryId | PER_ACCRUAL_ENTRY_ID | 🔑 | ✅ |
| 13 | PerPlanEnrtId | PER_PLAN_ENRT_ID | — | ✅ |
| 14 | PersonEventId | PERSON_EVENT_ID | — | ✅ |
| 15 | PersonId | PERSON_ID | — | ✅ |
| 16 | PlanId | PLAN_ID | — | ✅ |
| 17 | PrdOfSvcId | PRD_OF_SVC_ID | — | ✅ |
| 18 | RateDefinitionId | RATE_DEFINITION_ID | — | — |
| 19 | RptPeriodId | RPT_PERIOD_ID | — | — |
| 20 | Status | STATUS | — | — |
| 21 | Used | USED | — | ✅ |
| 22 | WorkTermAsgId | WORK_TERM_ASG_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
