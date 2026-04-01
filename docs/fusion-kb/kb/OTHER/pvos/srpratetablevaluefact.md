---
id: DOC-OTHER-PVO-SrpRateTableValueFact
doc_type: system-doc
title: "SrpRateTableValueFact — PVO Cross-Module"
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
  - SrpRateTableValueFact
  - srpratetablevaluefact
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SrpRateTableValueFact

## 📌 Visão Geral

View Object para extração BICC de dados de Srp Rate Table Value Fact. Acessa as tabelas: CN_RATE_TABLE_VALUES_ALL, CN_SRP_FORM_RATE_TABLES_ALL, CN_SRP_PARTICIPANTS_ALL (+1).

**Caminho:** `FscmTopModelAM.SrpCompPlanAM.SrpRateTableValueFact`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 53 | 4 | 2 | 19 | 36% |

---

## 🔗 Tabelas Relacionadas

- [[cn_rate_table_values_all|CN_RATE_TABLE_VALUES_ALL]] — 13 atributos (1 PKs, 9 BICC)
- [[cn_srp_form_rate_tables_all|CN_SRP_FORM_RATE_TABLES_ALL]] — 33 atributos (1 PKs, 9 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 4 atributos
- [[cn_srp_plan_components_all|CN_SRP_PLAN_COMPONENTS_ALL]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cn_rate_table_values_all|CN_RATE_TABLE_VALUES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RateTableValueId | RATE_TABLE_VALUE_ID | 🔑 | ✅ |
| 2 | RateValPEOCommissionValue | COMMISSION_VALUE | — | ✅ |
| 3 | RateValPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | RateValPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | RateValPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RateValPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | RateValPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | RateValPEOObjVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | RateValPEOOrgId | ORG_ID | — | — |
| 10 | RateValPEOParRateTabValId | PARENT_RATE_TABLE_VALUE_ID | — | ✅ |
| 11 | RateValPEORateSequence | RATE_SEQUENCE | — | ✅ |
| 12 | RateValPEORateTableId | RATE_TABLE_ID | — | — |
| 13 | RateValPEOSrpFormRateTableId | SRP_FORM_RATE_TABLE_ID | — | — |

### [[cn_srp_form_rate_tables_all|CN_SRP_FORM_RATE_TABLES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute2 | ATTRIBUTE2 | — | — |
| 9 | Attribute3 | ATTRIBUTE3 | — | — |
| 10 | Attribute4 | ATTRIBUTE4 | — | — |
| 11 | Attribute5 | ATTRIBUTE5 | — | — |
| 12 | Attribute6 | ATTRIBUTE6 | — | — |
| 13 | Attribute7 | ATTRIBUTE7 | — | — |
| 14 | Attribute8 | ATTRIBUTE8 | — | — |
| 15 | Attribute9 | ATTRIBUTE9 | — | — |
| 16 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | CompPlanId | COMP_PLAN_ID | — | — |
| 18 | CreatedBy | CREATED_BY | — | ✅ |
| 19 | CreationDate | CREATION_DATE | — | ✅ |
| 20 | FormulaId | FORMULA_ID | — | — |
| 21 | FormulaRateTableId | FORMULA_RATE_TABLE_ID | — | ✅ |
| 22 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | OrgId | ORG_ID | — | — |
| 27 | ParticipantId | PARTICIPANT_ID | — | ✅ |
| 28 | PlanComponentId | PLAN_COMPONENT_ID | — | — |
| 29 | RateTableId | RATE_TABLE_ID | — | ✅ |
| 30 | SrpCompPlanId | SRP_COMP_PLAN_ID | — | — |
| 31 | SrpFormMetricId | SRP_FORM_METRIC_ID | — | — |
| 32 | SrpFormRateTableId | SRP_FORM_RATE_TABLE_ID | 🔑 | ✅ |
| 33 | SrpPlanComponentId | SRP_PLAN_COMPONENT_ID | — | — |

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParticipantPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 2 | ParticipantPEOParticipantId | PARTICIPANT_ID | — | — |
| 3 | ParticipantPEOPartyId | PARTY_ID | — | — |
| 4 | ParticipantPEOSourceSystemId | SOURCE_SYSTEM_ID | — | — |

### [[cn_srp_plan_components_all|CN_SRP_PLAN_COMPONENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IndividualizedFlag | CUSTOMIZED_FLAG | — | ✅ |
| 2 | PcPEOPlanComponentId | PLAN_COMPONENT_ID | — | — |
| 3 | PcPEOSrpPlanComponentId | SRP_PLAN_COMPONENT_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
