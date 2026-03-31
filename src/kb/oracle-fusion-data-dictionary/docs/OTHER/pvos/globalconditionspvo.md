---
id: DOC-OTHER-PVO-GlobalConditionsPVO
doc_type: system-doc
title: "GlobalConditionsPVO — PVO Cross-Module"
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
  - GlobalConditionsPVO
  - globalconditionspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GlobalConditionsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Global Conditions. Acessa as tabelas: GRC_OTBI_CND_RPT_FLTR, GRC_OTBI_COND_REPORT, PER_PERSON_NAMES_F_V (+1).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.GlobalConditionsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 49 | 4 | 1 | 17 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[grc_otbi_cnd_rpt_fltr|GRC_OTBI_CND_RPT_FLTR]] — 14 atributos (7 BICC)
- [[grc_otbi_cond_report|GRC_OTBI_COND_REPORT]] — 15 atributos (1 PKs, 8 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[grc_otbi_cnd_rpt_fltr|GRC_OTBI_CND_RPT_FLTR]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlobalCondFilterPEOCondition | CONDITION | — | ✅ |
| 2 | GlobalCondFilterPEOCreatedBy | CREATED_BY | — | — |
| 3 | GlobalCondFilterPEOCreationDate | CREATION_DATE | — | — |
| 4 | GlobalCondFilterPEOExcluded | EXCLUDED | — | — |
| 5 | GlobalCondFilterPEOFilterName | FILTER_NAME | — | ✅ |
| 6 | GlobalCondFilterPEOId | ID | — | ✅ |
| 7 | GlobalCondFilterPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | GlobalCondFilterPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | GlobalCondFilterPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | GlobalCondFilterPEOObject | OBJECT | — | ✅ |
| 11 | GlobalCondFilterPEORowNum | ROW_NUM | — | — |
| 12 | GlobalCondFilterPEOType | TYPE | — | — |
| 13 | GlobalCondFilterPEOValue | VALUE | — | ✅ |
| 14 | GlobalCondFiltersPEOAttribute | ATTRIBUTE | — | ✅ |

### [[grc_otbi_cond_report|GRC_OTBI_COND_REPORT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlobalConditionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | GlobalConditionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | GlobalConditionsPEODescription | DESCRIPTION | — | ✅ |
| 4 | GlobalConditionsPEOId | ID | 🔑 | ✅ |
| 5 | GlobalConditionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | GlobalConditionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | GlobalConditionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | GlobalConditionsPEOName | NAME | — | ✅ |
| 9 | GlobalConditionsPEOPriority | PRIORITY | — | — |
| 10 | GlobalConditionsPEORowNum | ROW_NUM | — | — |
| 11 | GlobalConditionsPEOStateCode | STATE_CODE | — | — |
| 12 | GlobalConditionsPEOStatus | STATUS | — | ✅ |
| 13 | GlobalConditionsPEOStatusId | STATUS_ID | — | — |
| 14 | GlobalConditionsPEOType | TYPE | — | — |
| 15 | GlobalConditionsPEOTypeName | TYPE_NAME | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GCPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | GCPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | GCPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | GCPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | GCPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | GCPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | GCPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | GCPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | GCPersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | GCPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GCCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | GCCreatedByPersonId | PERSON_ID | — | — |
| 3 | GCCreatedByUserGuid | USER_GUID | — | — |
| 4 | GCCreatedByUserId | USER_ID | — | — |
| 5 | GCCreatedByUsername | USERNAME | — | — |
| 6 | GCUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | GCUpdatedByPersonId | PERSON_ID | — | — |
| 8 | GCUpdatedByUserGuid | USER_GUID | — | — |
| 9 | GCUpdatedByUserId | USER_ID | — | — |
| 10 | GCUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
