---
id: DOC-OTHER-PVO-AccrualPlanTranslationPVO
doc_type: system-doc
title: "AccrualPlanTranslationPVO — PVO Cross-Module"
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
  - AccrualPlanTranslationPVO
  - accrualplantranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AccrualPlanTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Accrual Plan Translation. Acessa as tabelas: PER_ACCRUAL_PLANS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AccrualAM.AccrualPlanTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 3 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[per_accrual_plans_tl|PER_ACCRUAL_PLANS_TL]] — 11 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[per_accrual_plans_tl|PER_ACCRUAL_PLANS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrualPlanId | ACCRUAL_PLAN_ID | 🔑 | ✅ |
| 2 | AccrualPlanTranslationPEOAccrualPlanName | ACCRUAL_PLAN_NAME | — | — |
| 3 | AccrualPlanTranslationPEOCreatedBy | CREATED_BY | — | — |
| 4 | AccrualPlanTranslationPEOCreationDate | CREATION_DATE | — | — |
| 5 | AccrualPlanTranslationPEODescription | DESCRIPTION | — | — |
| 6 | AccrualPlanTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AccrualPlanTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AccrualPlanTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AccrualPlanTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | AccrualPlanTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 11 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
