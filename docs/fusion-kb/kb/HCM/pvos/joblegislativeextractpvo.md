---
id: DOC-HCM-PVO-JobLegislativeExtractPVO
doc_type: system-doc
title: "JobLegislativeExtractPVO — PVO Human Capital Management"
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
  - JobLegislativeExtractPVO
  - joblegislativeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobLegislativeExtractPVO

## 📌 Visão Geral

Extrai dados legislativos de cargos com atributos flexíveis por jurisdição. Fundamental para compliance trabalhista e classificação legal de funções.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.JobBiccExtractAM.JobLegislativeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 146 | 1 | 3 | 16 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[per_job_leg_f|PER_JOB_LEG_F]] — 146 atributos (3 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[per_job_leg_f|PER_JOB_LEG_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 2 | Attribute1 | ATTRIBUTE1 | — | — |
| 3 | Attribute10 | ATTRIBUTE10 | — | — |
| 4 | Attribute11 | ATTRIBUTE11 | — | — |
| 5 | Attribute12 | ATTRIBUTE12 | — | — |
| 6 | Attribute13 | ATTRIBUTE13 | — | — |
| 7 | Attribute14 | ATTRIBUTE14 | — | — |
| 8 | Attribute15 | ATTRIBUTE15 | — | — |
| 9 | Attribute16 | ATTRIBUTE16 | — | — |
| 10 | Attribute17 | ATTRIBUTE17 | — | — |
| 11 | Attribute18 | ATTRIBUTE18 | — | — |
| 12 | Attribute19 | ATTRIBUTE19 | — | — |
| 13 | Attribute2 | ATTRIBUTE2 | — | — |
| 14 | Attribute20 | ATTRIBUTE20 | — | — |
| 15 | Attribute21 | ATTRIBUTE21 | — | — |
| 16 | Attribute22 | ATTRIBUTE22 | — | — |
| 17 | Attribute23 | ATTRIBUTE23 | — | — |
| 18 | Attribute24 | ATTRIBUTE24 | — | — |
| 19 | Attribute25 | ATTRIBUTE25 | — | — |
| 20 | Attribute26 | ATTRIBUTE26 | — | — |
| 21 | Attribute27 | ATTRIBUTE27 | — | — |
| 22 | Attribute28 | ATTRIBUTE28 | — | — |
| 23 | Attribute29 | ATTRIBUTE29 | — | — |
| 24 | Attribute3 | ATTRIBUTE3 | — | — |
| 25 | Attribute30 | ATTRIBUTE30 | — | — |
| 26 | Attribute4 | ATTRIBUTE4 | — | — |
| 27 | Attribute5 | ATTRIBUTE5 | — | — |
| 28 | Attribute6 | ATTRIBUTE6 | — | — |
| 29 | Attribute7 | ATTRIBUTE7 | — | — |
| 30 | Attribute8 | ATTRIBUTE8 | — | — |
| 31 | Attribute9 | ATTRIBUTE9 | — | — |
| 32 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 33 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 34 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 35 | AttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 36 | AttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 37 | AttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 38 | AttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 39 | AttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 40 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 41 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 42 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 43 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 44 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 45 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 46 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 47 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 48 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 49 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 50 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 51 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 52 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 53 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 54 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 55 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 56 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 57 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 58 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 59 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 60 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 61 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 62 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 63 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 64 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 65 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 66 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 67 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 68 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 69 | CreatedBy | CREATED_BY | — | ✅ |
| 70 | CreationDate | CREATION_DATE | — | ✅ |
| 71 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 72 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 73 | Information1 | INFORMATION1 | — | — |
| 74 | Information10 | INFORMATION10 | — | — |
| 75 | Information11 | INFORMATION11 | — | — |
| 76 | Information12 | INFORMATION12 | — | — |
| 77 | Information13 | INFORMATION13 | — | — |
| 78 | Information14 | INFORMATION14 | — | — |
| 79 | Information15 | INFORMATION15 | — | — |
| 80 | Information16 | INFORMATION16 | — | — |
| 81 | Information17 | INFORMATION17 | — | — |
| 82 | Information18 | INFORMATION18 | — | — |
| 83 | Information19 | INFORMATION19 | — | — |
| 84 | Information2 | INFORMATION2 | — | — |
| 85 | Information20 | INFORMATION20 | — | — |
| 86 | Information21 | INFORMATION21 | — | — |
| 87 | Information22 | INFORMATION22 | — | — |
| 88 | Information23 | INFORMATION23 | — | — |
| 89 | Information24 | INFORMATION24 | — | — |
| 90 | Information25 | INFORMATION25 | — | — |
| 91 | Information26 | INFORMATION26 | — | — |
| 92 | Information27 | INFORMATION27 | — | — |
| 93 | Information28 | INFORMATION28 | — | — |
| 94 | Information29 | INFORMATION29 | — | — |
| 95 | Information3 | INFORMATION3 | — | — |
| 96 | Information30 | INFORMATION30 | — | — |
| 97 | Information4 | INFORMATION4 | — | — |
| 98 | Information5 | INFORMATION5 | — | — |
| 99 | Information6 | INFORMATION6 | — | — |
| 100 | Information7 | INFORMATION7 | — | — |
| 101 | Information8 | INFORMATION8 | — | — |
| 102 | Information9 | INFORMATION9 | — | — |
| 103 | InformationCategory | INFORMATION_CATEGORY | — | ✅ |
| 104 | InformationDate1 | INFORMATION_DATE1 | — | — |
| 105 | InformationDate10 | INFORMATION_DATE10 | — | — |
| 106 | InformationDate11 | INFORMATION_DATE11 | — | — |
| 107 | InformationDate12 | INFORMATION_DATE12 | — | — |
| 108 | InformationDate13 | INFORMATION_DATE13 | — | — |
| 109 | InformationDate14 | INFORMATION_DATE14 | — | — |
| 110 | InformationDate15 | INFORMATION_DATE15 | — | — |
| 111 | InformationDate2 | INFORMATION_DATE2 | — | — |
| 112 | InformationDate3 | INFORMATION_DATE3 | — | — |
| 113 | InformationDate4 | INFORMATION_DATE4 | — | — |
| 114 | InformationDate5 | INFORMATION_DATE5 | — | — |
| 115 | InformationDate6 | INFORMATION_DATE6 | — | — |
| 116 | InformationDate7 | INFORMATION_DATE7 | — | — |
| 117 | InformationDate8 | INFORMATION_DATE8 | — | — |
| 118 | InformationDate9 | INFORMATION_DATE9 | — | — |
| 119 | InformationNumber1 | INFORMATION_NUMBER1 | — | — |
| 120 | InformationNumber10 | INFORMATION_NUMBER10 | — | — |
| 121 | InformationNumber11 | INFORMATION_NUMBER11 | — | — |
| 122 | InformationNumber12 | INFORMATION_NUMBER12 | — | — |
| 123 | InformationNumber13 | INFORMATION_NUMBER13 | — | — |
| 124 | InformationNumber14 | INFORMATION_NUMBER14 | — | — |
| 125 | InformationNumber15 | INFORMATION_NUMBER15 | — | — |
| 126 | InformationNumber16 | INFORMATION_NUMBER16 | — | — |
| 127 | InformationNumber17 | INFORMATION_NUMBER17 | — | — |
| 128 | InformationNumber18 | INFORMATION_NUMBER18 | — | — |
| 129 | InformationNumber19 | INFORMATION_NUMBER19 | — | — |
| 130 | InformationNumber2 | INFORMATION_NUMBER2 | — | — |
| 131 | InformationNumber20 | INFORMATION_NUMBER20 | — | — |
| 132 | InformationNumber3 | INFORMATION_NUMBER3 | — | — |
| 133 | InformationNumber4 | INFORMATION_NUMBER4 | — | — |
| 134 | InformationNumber5 | INFORMATION_NUMBER5 | — | — |
| 135 | InformationNumber6 | INFORMATION_NUMBER6 | — | — |
| 136 | InformationNumber7 | INFORMATION_NUMBER7 | — | — |
| 137 | InformationNumber8 | INFORMATION_NUMBER8 | — | — |
| 138 | InformationNumber9 | INFORMATION_NUMBER9 | — | — |
| 139 | JobId | JOB_ID | — | ✅ |
| 140 | JobLegId | JOB_LEG_ID | 🔑 | ✅ |
| 141 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 142 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 143 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 144 | LegislationCode | LEGISLATION_CODE | — | ✅ |
| 145 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 146 | SequenceNumber | SEQUENCE_NUMBER | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
