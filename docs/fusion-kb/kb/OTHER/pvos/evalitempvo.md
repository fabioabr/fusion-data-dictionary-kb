---
id: DOC-OTHER-PVO-EvalItemPVO
doc_type: system-doc
title: "EvalItemPVO — PVO Cross-Module"
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
  - EvalItemPVO
  - evalitempvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EvalItemPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Eval Item. Acessa as tabelas: HRA_EVAL_ITEMS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.EvalItemPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 12 | 55% |

---

## 🔗 Tabelas Relacionadas

- [[hra_eval_items|HRA_EVAL_ITEMS]] — 22 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hra_eval_items|HRA_EVAL_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | EvalItemId | EVAL_ITEM_ID | 🔑 | ✅ |
| 5 | EvalItemPEOAchievementDate | ACHIEVEMENT_DATE | — | ✅ |
| 6 | EvalItemPEODescription | DESCRIPTION | — | — |
| 7 | EvalItemPEODueDate | DUE_DATE | — | ✅ |
| 8 | EvalItemPEOItemName | ITEM_NAME | — | — |
| 9 | EvalItemPEOMandatoryFlag | MANDATORY_FLAG | — | — |
| 10 | EvalItemPEOMeasurement | MEASUREMENT | — | ✅ |
| 11 | EvalItemPEOMinWeight | MIN_WEIGHT | — | ✅ |
| 12 | EvalItemPEOOwnedBy | OWNED_BY | — | ✅ |
| 13 | EvalItemPEOPercentCompleted | PERCENT_COMPLETED | — | ✅ |
| 14 | EvalItemPEORatingOverideFlag | RATING_OVERIDE_FLAG | — | — |
| 15 | EvalItemPEOReminderDate | REMINDER_DATE | — | ✅ |
| 16 | EvalItemPEOStartDate | START_DATE | — | ✅ |
| 17 | EvalItemPEOTargetDate | TARGET_DATE | — | ✅ |
| 18 | EvalItemPEOWeight | WEIGHT | — | ✅ |
| 19 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
