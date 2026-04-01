---
id: DOC-OTHER-PVO-PersonEthinicityPVO
doc_type: system-doc
title: "PersonEthinicityPVO — PVO Cross-Module"
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
  - PersonEthinicityPVO
  - personethinicitypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonEthinicityPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Ethinicity. Acessa as tabelas: PER_ETHNICITIES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.PersonEthinicityPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_ethnicities|PER_ETHNICITIES]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[per_ethnicities|PER_ETHNICITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EthnicityId | ETHNICITY_ID | 🔑 | ✅ |
| 2 | EthnicityPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | EthnicityPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | EthnicityPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | EthnicityPEODeclarerId | DECLARER_ID | — | ✅ |
| 6 | EthnicityPEOEthnicity | ETHNICITY | — | ✅ |
| 7 | EthnicityPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | EthnicityPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | EthnicityPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | EthnicityPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 11 | EthnicityPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | EthnicityPEOPersonId | PERSON_ID | — | ✅ |
| 13 | EthnicityPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
