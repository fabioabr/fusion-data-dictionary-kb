---
id: DOC-HCM-PVO-OrganizationPerWorkDayInfoPVO
doc_type: system-doc
title: "OrganizationPerWorkDayInfoPVO — PVO Human Capital Management"
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
  - OrganizationPerWorkDayInfoPVO
  - organizationperworkdayinfopvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrganizationPerWorkDayInfoPVO

## 📌 Visão Geral

Extrai informações de dia útil por organização com vigência temporal. Utilizado para configuração de calendários de trabalho e cálculos de jornada por unidade organizacional.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.OrganizationAM.OrganizationPerWorkDayInfoPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 79 | 1 | 3 | 4 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 79 atributos (3 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | OrgInformationId | ORG_INFORMATION_ID | 🔑 | ✅ |
| 4 | OrganizationInformationPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 5 | OrganizationInformationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | OrganizationInformationPEOCreatedBy | CREATED_BY | — | — |
| 7 | OrganizationInformationPEOCreationDate | CREATION_DATE | — | — |
| 8 | OrganizationInformationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | OrganizationInformationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | OrganizationInformationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | OrganizationInformationPEOLegislationCode | LEGISLATION_CODE | — | — |
| 12 | OrganizationInformationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | OrganizationInformationPEOOrgInformation1 | ORG_INFORMATION1 | — | — |
| 14 | OrganizationInformationPEOOrgInformation10 | ORG_INFORMATION10 | — | — |
| 15 | OrganizationInformationPEOOrgInformation11 | ORG_INFORMATION11 | — | — |
| 16 | OrganizationInformationPEOOrgInformation12 | ORG_INFORMATION12 | — | — |
| 17 | OrganizationInformationPEOOrgInformation13 | ORG_INFORMATION13 | — | — |
| 18 | OrganizationInformationPEOOrgInformation14 | ORG_INFORMATION14 | — | — |
| 19 | OrganizationInformationPEOOrgInformation15 | ORG_INFORMATION15 | — | — |
| 20 | OrganizationInformationPEOOrgInformation16 | ORG_INFORMATION16 | — | — |
| 21 | OrganizationInformationPEOOrgInformation17 | ORG_INFORMATION17 | — | — |
| 22 | OrganizationInformationPEOOrgInformation18 | ORG_INFORMATION18 | — | — |
| 23 | OrganizationInformationPEOOrgInformation19 | ORG_INFORMATION19 | — | — |
| 24 | OrganizationInformationPEOOrgInformation2 | ORG_INFORMATION2 | — | — |
| 25 | OrganizationInformationPEOOrgInformation20 | ORG_INFORMATION20 | — | — |
| 26 | OrganizationInformationPEOOrgInformation21 | ORG_INFORMATION21 | — | — |
| 27 | OrganizationInformationPEOOrgInformation22 | ORG_INFORMATION22 | — | — |
| 28 | OrganizationInformationPEOOrgInformation23 | ORG_INFORMATION23 | — | — |
| 29 | OrganizationInformationPEOOrgInformation24 | ORG_INFORMATION24 | — | — |
| 30 | OrganizationInformationPEOOrgInformation25 | ORG_INFORMATION25 | — | — |
| 31 | OrganizationInformationPEOOrgInformation26 | ORG_INFORMATION26 | — | — |
| 32 | OrganizationInformationPEOOrgInformation27 | ORG_INFORMATION27 | — | — |
| 33 | OrganizationInformationPEOOrgInformation28 | ORG_INFORMATION28 | — | — |
| 34 | OrganizationInformationPEOOrgInformation29 | ORG_INFORMATION29 | — | — |
| 35 | OrganizationInformationPEOOrgInformation3 | ORG_INFORMATION3 | — | — |
| 36 | OrganizationInformationPEOOrgInformation30 | ORG_INFORMATION30 | — | — |
| 37 | OrganizationInformationPEOOrgInformation4 | ORG_INFORMATION4 | — | — |
| 38 | OrganizationInformationPEOOrgInformation5 | ORG_INFORMATION5 | — | — |
| 39 | OrganizationInformationPEOOrgInformation6 | ORG_INFORMATION6 | — | — |
| 40 | OrganizationInformationPEOOrgInformation7 | ORG_INFORMATION7 | — | — |
| 41 | OrganizationInformationPEOOrgInformation8 | ORG_INFORMATION8 | — | — |
| 42 | OrganizationInformationPEOOrgInformation9 | ORG_INFORMATION9 | — | — |
| 43 | OrganizationInformationPEOOrgInformationContext | ORG_INFORMATION_CONTEXT | — | — |
| 44 | OrganizationInformationPEOOrgInformationDate1 | ORG_INFORMATION_DATE1 | — | — |
| 45 | OrganizationInformationPEOOrgInformationDate10 | ORG_INFORMATION_DATE10 | — | — |
| 46 | OrganizationInformationPEOOrgInformationDate11 | ORG_INFORMATION_DATE11 | — | — |
| 47 | OrganizationInformationPEOOrgInformationDate12 | ORG_INFORMATION_DATE12 | — | — |
| 48 | OrganizationInformationPEOOrgInformationDate13 | ORG_INFORMATION_DATE13 | — | — |
| 49 | OrganizationInformationPEOOrgInformationDate14 | ORG_INFORMATION_DATE14 | — | — |
| 50 | OrganizationInformationPEOOrgInformationDate15 | ORG_INFORMATION_DATE15 | — | — |
| 51 | OrganizationInformationPEOOrgInformationDate2 | ORG_INFORMATION_DATE2 | — | — |
| 52 | OrganizationInformationPEOOrgInformationDate3 | ORG_INFORMATION_DATE3 | — | — |
| 53 | OrganizationInformationPEOOrgInformationDate4 | ORG_INFORMATION_DATE4 | — | — |
| 54 | OrganizationInformationPEOOrgInformationDate5 | ORG_INFORMATION_DATE5 | — | — |
| 55 | OrganizationInformationPEOOrgInformationDate6 | ORG_INFORMATION_DATE6 | — | — |
| 56 | OrganizationInformationPEOOrgInformationDate7 | ORG_INFORMATION_DATE7 | — | — |
| 57 | OrganizationInformationPEOOrgInformationDate8 | ORG_INFORMATION_DATE8 | — | — |
| 58 | OrganizationInformationPEOOrgInformationDate9 | ORG_INFORMATION_DATE9 | — | — |
| 59 | OrganizationInformationPEOOrgInformationNumber1 | ORG_INFORMATION_NUMBER1 | — | — |
| 60 | OrganizationInformationPEOOrgInformationNumber10 | ORG_INFORMATION_NUMBER10 | — | — |
| 61 | OrganizationInformationPEOOrgInformationNumber11 | ORG_INFORMATION_NUMBER11 | — | — |
| 62 | OrganizationInformationPEOOrgInformationNumber12 | ORG_INFORMATION_NUMBER12 | — | — |
| 63 | OrganizationInformationPEOOrgInformationNumber13 | ORG_INFORMATION_NUMBER13 | — | — |
| 64 | OrganizationInformationPEOOrgInformationNumber14 | ORG_INFORMATION_NUMBER14 | — | — |
| 65 | OrganizationInformationPEOOrgInformationNumber15 | ORG_INFORMATION_NUMBER15 | — | — |
| 66 | OrganizationInformationPEOOrgInformationNumber16 | ORG_INFORMATION_NUMBER16 | — | — |
| 67 | OrganizationInformationPEOOrgInformationNumber17 | ORG_INFORMATION_NUMBER17 | — | — |
| 68 | OrganizationInformationPEOOrgInformationNumber18 | ORG_INFORMATION_NUMBER18 | — | — |
| 69 | OrganizationInformationPEOOrgInformationNumber19 | ORG_INFORMATION_NUMBER19 | — | — |
| 70 | OrganizationInformationPEOOrgInformationNumber2 | ORG_INFORMATION_NUMBER2 | — | — |
| 71 | OrganizationInformationPEOOrgInformationNumber20 | ORG_INFORMATION_NUMBER20 | — | — |
| 72 | OrganizationInformationPEOOrgInformationNumber3 | ORG_INFORMATION_NUMBER3 | — | — |
| 73 | OrganizationInformationPEOOrgInformationNumber4 | ORG_INFORMATION_NUMBER4 | — | — |
| 74 | OrganizationInformationPEOOrgInformationNumber5 | ORG_INFORMATION_NUMBER5 | — | — |
| 75 | OrganizationInformationPEOOrgInformationNumber6 | ORG_INFORMATION_NUMBER6 | — | — |
| 76 | OrganizationInformationPEOOrgInformationNumber7 | ORG_INFORMATION_NUMBER7 | — | — |
| 77 | OrganizationInformationPEOOrgInformationNumber8 | ORG_INFORMATION_NUMBER8 | — | — |
| 78 | OrganizationInformationPEOOrgInformationNumber9 | ORG_INFORMATION_NUMBER9 | — | — |
| 79 | OrganizationInformationPEOOrganizationId | ORGANIZATION_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
