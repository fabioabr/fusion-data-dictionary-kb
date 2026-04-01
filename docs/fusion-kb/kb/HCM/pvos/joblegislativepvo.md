---
id: DOC-HCM-PVO-JobLegislativePVO
doc_type: system-doc
title: "JobLegislativePVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - JobLegislativePVO
  - joblegislativepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobLegislativePVO

## 📌 Visão Geral

Disponibiliza dados legislativos de cargos com vigência por jurisdição. Utilizado para atender requisitos regulatórios de classificação de funções.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.JobAM.JobLegislativePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 1 | 2 | 14 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[per_job_leg_f|PER_JOB_LEG_F]] — 44 atributos (2 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[per_job_leg_f|PER_JOB_LEG_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | JobLegId | JOB_LEG_ID | 🔑 | ✅ |
| 4 | JobLegislativePEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 5 | JobLegislativePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | JobLegislativePEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | JobLegislativePEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | JobLegislativePEOInformation1 | INFORMATION1 | — | ✅ |
| 9 | JobLegislativePEOInformation10 | INFORMATION10 | — | — |
| 10 | JobLegislativePEOInformation11 | INFORMATION11 | — | — |
| 11 | JobLegislativePEOInformation12 | INFORMATION12 | — | — |
| 12 | JobLegislativePEOInformation13 | INFORMATION13 | — | — |
| 13 | JobLegislativePEOInformation14 | INFORMATION14 | — | — |
| 14 | JobLegislativePEOInformation15 | INFORMATION15 | — | — |
| 15 | JobLegislativePEOInformation16 | INFORMATION16 | — | — |
| 16 | JobLegislativePEOInformation17 | INFORMATION17 | — | — |
| 17 | JobLegislativePEOInformation18 | INFORMATION18 | — | — |
| 18 | JobLegislativePEOInformation19 | INFORMATION19 | — | — |
| 19 | JobLegislativePEOInformation2 | INFORMATION2 | — | ✅ |
| 20 | JobLegislativePEOInformation20 | INFORMATION20 | — | — |
| 21 | JobLegislativePEOInformation21 | INFORMATION21 | — | — |
| 22 | JobLegislativePEOInformation22 | INFORMATION22 | — | — |
| 23 | JobLegislativePEOInformation23 | INFORMATION23 | — | — |
| 24 | JobLegislativePEOInformation24 | INFORMATION24 | — | — |
| 25 | JobLegislativePEOInformation25 | INFORMATION25 | — | — |
| 26 | JobLegislativePEOInformation26 | INFORMATION26 | — | — |
| 27 | JobLegislativePEOInformation27 | INFORMATION27 | — | — |
| 28 | JobLegislativePEOInformation28 | INFORMATION28 | — | — |
| 29 | JobLegislativePEOInformation29 | INFORMATION29 | — | — |
| 30 | JobLegislativePEOInformation3 | INFORMATION3 | — | ✅ |
| 31 | JobLegislativePEOInformation30 | INFORMATION30 | — | — |
| 32 | JobLegislativePEOInformation4 | INFORMATION4 | — | — |
| 33 | JobLegislativePEOInformation5 | INFORMATION5 | — | — |
| 34 | JobLegislativePEOInformation6 | INFORMATION6 | — | — |
| 35 | JobLegislativePEOInformation7 | INFORMATION7 | — | — |
| 36 | JobLegislativePEOInformation8 | INFORMATION8 | — | — |
| 37 | JobLegislativePEOInformation9 | INFORMATION9 | — | — |
| 38 | JobLegislativePEOInformationCategory | INFORMATION_CATEGORY | — | ✅ |
| 39 | JobLegislativePEOJobId | JOB_ID | — | ✅ |
| 40 | JobLegislativePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | JobLegislativePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 42 | JobLegislativePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 43 | JobLegislativePEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 44 | JobLegislativePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
