---
id: DOC-OTHER-PVO-ReligionPVOViewAll
doc_type: system-doc
title: "ReligionPVOViewAll — PVO Cross-Module"
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
  - ReligionPVOViewAll
  - religionpvoviewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReligionPVOViewAll

## 📌 Visão Geral

View Object para extração BICC de dados de Religion View All. Acessa as tabelas: PER_RELIGIONS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.ReligionPVOViewAll`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 9 | 75% |

---

## 🔗 Tabelas Relacionadas

- [[per_religions|PER_RELIGIONS]] — 12 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[per_religions|PER_RELIGIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReligionId | RELIGION_ID | 🔑 | ✅ |
| 2 | ReligionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ReligionPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ReligionPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ReligionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ReligionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ReligionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ReligionPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 9 | ReligionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ReligionPEOPersonId | PERSON_ID | — | ✅ |
| 11 | ReligionPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 12 | ReligionPEOReligion | RELIGION | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
