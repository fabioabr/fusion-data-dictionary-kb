---
id: DOC-OTHER-PVO-RaRuleSchedulesPVO
doc_type: system-doc
title: "RaRuleSchedulesPVO — PVO Cross-Module"
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
  - RaRuleSchedulesPVO
  - raruleschedulespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RaRuleSchedulesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ra Rule Schedules. Acessa as tabelas: RA_RULES, RA_RULE_SCHEDULES.

**Caminho:** `FscmTopModelAM.FinVrmRRSharedPublicModelAM.RaRuleSchedulesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 45 | 2 | 2 | 12 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[ra_rules|RA_RULES]] — 18 atributos (7 BICC)
- [[ra_rule_schedules|RA_RULE_SCHEDULES]] — 27 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[ra_rules|RA_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaRulesAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | RaRulesCalendarId | CALENDAR_ID | — | — |
| 3 | RaRulesCreatedBy | CREATED_BY | — | — |
| 4 | RaRulesCreationDate | CREATION_DATE | — | — |
| 5 | RaRulesDeferredRevenueFlag | DEFERRED_REVENUE_FLAG | — | — |
| 6 | RaRulesDescription | DESCRIPTION | — | ✅ |
| 7 | RaRulesFrequency | FREQUENCY | — | ✅ |
| 8 | RaRulesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | RaRulesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | RaRulesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | RaRulesModuleId | MODULE_ID | — | — |
| 12 | RaRulesName | NAME | — | ✅ |
| 13 | RaRulesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | RaRulesOccurrences | OCCURRENCES | — | ✅ |
| 15 | RaRulesRuleId | RULE_ID | — | — |
| 16 | RaRulesSetId | SET_ID | — | — |
| 17 | RaRulesStatus | STATUS | — | ✅ |
| 18 | RaRulesType | TYPE | — | ✅ |

### [[ra_rule_schedules|RA_RULE_SCHEDULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PeriodNumber | PERIOD_NUMBER | 🔑 | ✅ |
| 2 | RaRuleSchedulesAttribute1 | ATTRIBUTE1 | — | — |
| 3 | RaRuleSchedulesAttribute10 | ATTRIBUTE10 | — | — |
| 4 | RaRuleSchedulesAttribute11 | ATTRIBUTE11 | — | — |
| 5 | RaRuleSchedulesAttribute12 | ATTRIBUTE12 | — | — |
| 6 | RaRuleSchedulesAttribute13 | ATTRIBUTE13 | — | — |
| 7 | RaRuleSchedulesAttribute14 | ATTRIBUTE14 | — | — |
| 8 | RaRuleSchedulesAttribute15 | ATTRIBUTE15 | — | — |
| 9 | RaRuleSchedulesAttribute2 | ATTRIBUTE2 | — | — |
| 10 | RaRuleSchedulesAttribute3 | ATTRIBUTE3 | — | — |
| 11 | RaRuleSchedulesAttribute4 | ATTRIBUTE4 | — | — |
| 12 | RaRuleSchedulesAttribute5 | ATTRIBUTE5 | — | — |
| 13 | RaRuleSchedulesAttribute6 | ATTRIBUTE6 | — | — |
| 14 | RaRuleSchedulesAttribute7 | ATTRIBUTE7 | — | — |
| 15 | RaRuleSchedulesAttribute8 | ATTRIBUTE8 | — | — |
| 16 | RaRuleSchedulesAttribute9 | ATTRIBUTE9 | — | — |
| 17 | RaRuleSchedulesAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 18 | RaRuleSchedulesCreatedBy | CREATED_BY | — | — |
| 19 | RaRuleSchedulesCreationDate | CREATION_DATE | — | — |
| 20 | RaRuleSchedulesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | RaRuleSchedulesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | RaRuleSchedulesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | RaRuleSchedulesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | RaRuleSchedulesPercent | PERCENT | — | ✅ |
| 25 | RaRuleSchedulesRuleDate | RULE_DATE | — | ✅ |
| 26 | RaRuleSchedulesSetId | SET_ID | — | — |
| 27 | RuleId | RULE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
