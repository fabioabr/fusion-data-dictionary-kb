---
id: DOC-OTHER-PVO-CitizenshipPVO
doc_type: system-doc
title: "CitizenshipPVO — PVO Cross-Module"
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
  - CitizenshipPVO
  - citizenshippvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CitizenshipPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Citizenship. Acessa as tabelas: PER_CITIZENSHIPS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.CitizenshipPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_citizenships|PER_CITIZENSHIPS]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[per_citizenships|PER_CITIZENSHIPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CitizenshipId | CITIZENSHIP_ID | 🔑 | ✅ |
| 2 | CitizenshipPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | CitizenshipPEOCitizenshipStatus | CITIZENSHIP_STATUS | — | ✅ |
| 4 | CitizenshipPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | CitizenshipPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | CitizenshipPEODateFrom | DATE_FROM | — | ✅ |
| 7 | CitizenshipPEODateTo | DATE_TO | — | ✅ |
| 8 | CitizenshipPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | CitizenshipPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | CitizenshipPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | CitizenshipPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 12 | CitizenshipPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | CitizenshipPEOPersonId | PERSON_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
