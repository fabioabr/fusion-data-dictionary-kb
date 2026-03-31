---
id: DOC-OTHER-PVO-ProjectAccountingPeriodExtractPVO
doc_type: system-doc
title: "ProjectAccountingPeriodExtractPVO — PVO Cross-Module"
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
  - ProjectAccountingPeriodExtractPVO
  - projectaccountingperiodextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectAccountingPeriodExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Accounting Period Extract. Acessa as tabelas: PJF_PERIODS_ALL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectAccountingPeriodExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_periods_all|PJF_PERIODS_ALL]] — 13 atributos (2 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[pjf_periods_all|PJF_PERIODS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectAccountingPeriodPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectAccountingPeriodPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectAccountingPeriodPEOEndDate | END_DATE | — | ✅ |
| 4 | ProjectAccountingPeriodPEOGlPeriodName | GL_PERIOD_NAME | — | ✅ |
| 5 | ProjectAccountingPeriodPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectAccountingPeriodPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectAccountingPeriodPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectAccountingPeriodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ProjectAccountingPeriodPEOOrgId | ORG_ID | 🔑 | ✅ |
| 10 | ProjectAccountingPeriodPEOPeriodName | PERIOD_NAME | 🔑 | ✅ |
| 11 | ProjectAccountingPeriodPEOPeriodNum | PERIOD_NUM | — | ✅ |
| 12 | ProjectAccountingPeriodPEOStartDate | START_DATE | — | ✅ |
| 13 | ProjectAccountingPeriodPEOStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
