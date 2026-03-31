---
id: DOC-OTHER-PVO-AwardBudgetPeriodPVO
doc_type: system-doc
title: "AwardBudgetPeriodPVO — PVO Cross-Module"
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
  - AwardBudgetPeriodPVO
  - awardbudgetperiodpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardBudgetPeriodPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Budget Period. Acessa as tabelas: GMS_AWARD_BUDGET_PERIODS.

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardBudgetPeriodPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_budget_periods|GMS_AWARD_BUDGET_PERIODS]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[gms_award_budget_periods|GMS_AWARD_BUDGET_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardBudgetPeriodPEOAwardId | AWARD_ID | — | ✅ |
| 2 | AwardBudgetPeriodPEOBudgetPeriod | BUDGET_PERIOD | — | ✅ |
| 3 | AwardBudgetPeriodPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AwardBudgetPeriodPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AwardBudgetPeriodPEOEndDate | END_DATE | — | ✅ |
| 6 | AwardBudgetPeriodPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AwardBudgetPeriodPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AwardBudgetPeriodPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AwardBudgetPeriodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | AwardBudgetPeriodPEOSeqNum | SEQ_NUM | — | ✅ |
| 11 | AwardBudgetPeriodPEOStartDate | START_DATE | — | ✅ |
| 12 | Id | ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
