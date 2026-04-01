---
id: DOC-HCM-PVO-JobExtraInfoExtractPVO
doc_type: system-doc
title: "JobExtraInfoExtractPVO — PVO Human Capital Management"
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
  - JobExtraInfoExtractPVO
  - jobextrainfoextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobExtraInfoExtractPVO

## 📌 Visão Geral

Extrai informações extras de cargos com atributos flexíveis por período de vigência. Suporta customizações e dados legislativos complementares de cargos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.JobBiccExtractAM.JobExtraInfoExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 75 | 1 | 3 | 15 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[per_job_extra_info_f|PER_JOB_EXTRA_INFO_F]] — 75 atributos (3 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[per_job_extra_info_f|PER_JOB_EXTRA_INFO_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 5 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 6 | InformationType | INFORMATION_TYPE | — | ✅ |
| 7 | JeiAttribute1 | JEI_ATTRIBUTE1 | — | — |
| 8 | JeiAttribute10 | JEI_ATTRIBUTE10 | — | — |
| 9 | JeiAttribute11 | JEI_ATTRIBUTE11 | — | — |
| 10 | JeiAttribute12 | JEI_ATTRIBUTE12 | — | — |
| 11 | JeiAttribute13 | JEI_ATTRIBUTE13 | — | — |
| 12 | JeiAttribute14 | JEI_ATTRIBUTE14 | — | — |
| 13 | JeiAttribute15 | JEI_ATTRIBUTE15 | — | — |
| 14 | JeiAttribute16 | JEI_ATTRIBUTE16 | — | — |
| 15 | JeiAttribute17 | JEI_ATTRIBUTE17 | — | — |
| 16 | JeiAttribute18 | JEI_ATTRIBUTE18 | — | — |
| 17 | JeiAttribute19 | JEI_ATTRIBUTE19 | — | — |
| 18 | JeiAttribute2 | JEI_ATTRIBUTE2 | — | — |
| 19 | JeiAttribute20 | JEI_ATTRIBUTE20 | — | — |
| 20 | JeiAttribute21 | JEI_ATTRIBUTE21 | — | — |
| 21 | JeiAttribute22 | JEI_ATTRIBUTE22 | — | — |
| 22 | JeiAttribute23 | JEI_ATTRIBUTE23 | — | — |
| 23 | JeiAttribute24 | JEI_ATTRIBUTE24 | — | — |
| 24 | JeiAttribute25 | JEI_ATTRIBUTE25 | — | — |
| 25 | JeiAttribute26 | JEI_ATTRIBUTE26 | — | — |
| 26 | JeiAttribute27 | JEI_ATTRIBUTE27 | — | — |
| 27 | JeiAttribute28 | JEI_ATTRIBUTE28 | — | — |
| 28 | JeiAttribute29 | JEI_ATTRIBUTE29 | — | — |
| 29 | JeiAttribute3 | JEI_ATTRIBUTE3 | — | — |
| 30 | JeiAttribute30 | JEI_ATTRIBUTE30 | — | — |
| 31 | JeiAttribute4 | JEI_ATTRIBUTE4 | — | — |
| 32 | JeiAttribute5 | JEI_ATTRIBUTE5 | — | — |
| 33 | JeiAttribute6 | JEI_ATTRIBUTE6 | — | — |
| 34 | JeiAttribute7 | JEI_ATTRIBUTE7 | — | — |
| 35 | JeiAttribute8 | JEI_ATTRIBUTE8 | — | — |
| 36 | JeiAttribute9 | JEI_ATTRIBUTE9 | — | — |
| 37 | JeiAttributeCategory | JEI_ATTRIBUTE_CATEGORY | — | ✅ |
| 38 | JeiInformation1 | JEI_INFORMATION1 | — | — |
| 39 | JeiInformation10 | JEI_INFORMATION10 | — | — |
| 40 | JeiInformation11 | JEI_INFORMATION11 | — | — |
| 41 | JeiInformation12 | JEI_INFORMATION12 | — | — |
| 42 | JeiInformation13 | JEI_INFORMATION13 | — | — |
| 43 | JeiInformation14 | JEI_INFORMATION14 | — | — |
| 44 | JeiInformation15 | JEI_INFORMATION15 | — | — |
| 45 | JeiInformation16 | JEI_INFORMATION16 | — | — |
| 46 | JeiInformation17 | JEI_INFORMATION17 | — | — |
| 47 | JeiInformation18 | JEI_INFORMATION18 | — | — |
| 48 | JeiInformation19 | JEI_INFORMATION19 | — | — |
| 49 | JeiInformation2 | JEI_INFORMATION2 | — | — |
| 50 | JeiInformation20 | JEI_INFORMATION20 | — | — |
| 51 | JeiInformation21 | JEI_INFORMATION21 | — | — |
| 52 | JeiInformation22 | JEI_INFORMATION22 | — | — |
| 53 | JeiInformation23 | JEI_INFORMATION23 | — | — |
| 54 | JeiInformation24 | JEI_INFORMATION24 | — | — |
| 55 | JeiInformation25 | JEI_INFORMATION25 | — | — |
| 56 | JeiInformation26 | JEI_INFORMATION26 | — | — |
| 57 | JeiInformation27 | JEI_INFORMATION27 | — | — |
| 58 | JeiInformation28 | JEI_INFORMATION28 | — | — |
| 59 | JeiInformation29 | JEI_INFORMATION29 | — | — |
| 60 | JeiInformation3 | JEI_INFORMATION3 | — | — |
| 61 | JeiInformation30 | JEI_INFORMATION30 | — | — |
| 62 | JeiInformation4 | JEI_INFORMATION4 | — | — |
| 63 | JeiInformation5 | JEI_INFORMATION5 | — | — |
| 64 | JeiInformation6 | JEI_INFORMATION6 | — | — |
| 65 | JeiInformation7 | JEI_INFORMATION7 | — | — |
| 66 | JeiInformation8 | JEI_INFORMATION8 | — | — |
| 67 | JeiInformation9 | JEI_INFORMATION9 | — | — |
| 68 | JeiInformationCategory | JEI_INFORMATION_CATEGORY | — | ✅ |
| 69 | JobExtraInfoId | JOB_EXTRA_INFO_ID | 🔑 | ✅ |
| 70 | JobId | JOB_ID | — | ✅ |
| 71 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 72 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 73 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 74 | LegislationCode | LEGISLATION_CODE | — | ✅ |
| 75 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
