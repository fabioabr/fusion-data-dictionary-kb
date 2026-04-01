---
id: DOC-OTHER-PVO-ProjectPeriodPVO
doc_type: system-doc
title: "ProjectPeriodPVO — PVO Cross-Module"
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
  - ProjectPeriodPVO
  - projectperiodpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectPeriodPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Period. Acessa as tabelas: GL_PERIODS, HR_ORGANIZATION_INFORMATION_F, PJF_BU_IMPL_ALL.

**Caminho:** `FscmTopModelAM.PjfSetupPeriodsAM.ProjectPeriodPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 3 | 4 | 12 | 63% |

---

## 🔗 Tabelas Relacionadas

- [[gl_periods|GL_PERIODS]] — 12 atributos (4 PKs, 11 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 5 atributos (1 BICC)
- [[pjf_bu_impl_all|PJF_BU_IMPL_ALL]] — 2 atributos

---

## ⚙️ Atributos

### [[gl_periods|GL_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlPeriodsAdjustmentPeriodFlag | ADJUSTMENT_PERIOD_FLAG | — | — |
| 2 | GlPeriodsObjectVersionNumber | OBJECT_VERSION_NUMBER | 🔑 | ✅ |
| 3 | PaPeriodName | PERIOD_NAME | 🔑 | ✅ |
| 4 | PaPeriodSetName | PERIOD_SET_NAME | 🔑 | ✅ |
| 5 | PaPeriodType | PERIOD_TYPE | 🔑 | ✅ |
| 6 | ProjectPeriodsDatePEOPaPeriodEndDate | END_DATE | — | ✅ |
| 7 | ProjectPeriodsDatePEOPaPeriodNumber | PERIOD_NUM | — | ✅ |
| 8 | ProjectPeriodsDatePEOPaPeriodStartDate | START_DATE | — | ✅ |
| 9 | ProjectPeriodsDatePEOPaPeriodYear | PERIOD_YEAR | — | ✅ |
| 10 | ProjectPeriodsDatePEOPaQuarterNumber | QUARTER_NUM | — | ✅ |
| 11 | ProjectPeriodsDatePEOPaQuarterStartDate | QUARTER_START_DATE | — | ✅ |
| 12 | ProjectPeriodsDatePEOPaYearStartDate | YEAR_START_DATE | — | ✅ |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgInfoPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrgInfoPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OrgInfoPEOOrgInformationContext | ORG_INFORMATION_CONTEXT | — | — |
| 4 | OrgInfoPEOOrgInformationId | ORG_INFORMATION_ID | — | — |
| 5 | PrimaryLedgerId | ORG_INFORMATION3 | — | — |

### [[pjf_bu_impl_all|PJF_BU_IMPL_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjfBuImplAllObjVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ProjectPeriodsDatePEOOrgId | ORG_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
