---
id: DOC-OTHER-PVO-PersonTypesPVO
doc_type: system-doc
title: "PersonTypesPVO — PVO Cross-Module"
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
  - PersonTypesPVO
  - persontypespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonTypesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Types. Acessa as tabelas: PER_PERSON_TYPES, PER_PERSON_TYPE_USAGES_M.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.PersonTypesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 2 | 5 | 14 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_types|PER_PERSON_TYPES]] — 11 atributos (1 PKs, 8 BICC)
- [[per_person_type_usages_m|PER_PERSON_TYPE_USAGES_M]] — 13 atributos (4 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[per_person_types|PER_PERSON_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonTypeId | PERSON_TYPE_ID | 🔑 | ✅ |
| 2 | PersonTypesPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 3 | PersonTypesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | PersonTypesPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | PersonTypesPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | PersonTypesPEODefaultFlag | DEFAULT_FLAG | — | ✅ |
| 7 | PersonTypesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PersonTypesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PersonTypesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PersonTypesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PersonTypesPEOSystemPersonType | SYSTEM_PERSON_TYPE | — | ✅ |

### [[per_person_type_usages_m|PER_PERSON_TYPE_USAGES_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonTypeUsagesPEOCreatedBy | CREATED_BY | — | — |
| 2 | PersonTypeUsagesPEOCreationDate | CREATION_DATE | — | — |
| 3 | PersonTypeUsagesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | PersonTypeUsagesPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | 🔑 | ✅ |
| 5 | PersonTypeUsagesPEOEffectiveSequence | EFFECTIVE_SEQUENCE | 🔑 | ✅ |
| 6 | PersonTypeUsagesPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | PersonTypeUsagesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PersonTypeUsagesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PersonTypeUsagesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PersonTypeUsagesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PersonTypeUsagesPEOPersonId | PERSON_ID | — | ✅ |
| 12 | PersonTypeUsagesPEOPersonTypeUsageId | PERSON_TYPE_USAGE_ID | 🔑 | ✅ |
| 13 | PersonTypeUsagesPEOSystemPersonType | SYSTEM_PERSON_TYPE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
