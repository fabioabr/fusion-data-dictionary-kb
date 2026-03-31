---
id: DOC-PO-PVO-AllBuyerPVO
doc_type: system-doc
title: "AllBuyerPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - AllBuyerPVO
  - allbuyerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AllBuyerPVO

## 📌 Visão Geral

Extrai o cadastro completo de compradores (buyers) da organização, incluindo nome, unidade de negócio, endereço e dados de contato. Permite análise de distribuição de compras por comprador, carga de trabalho e cobertura organizacional.

**Caminho:** `FscmTopModelAM.PrcPoPublicViewAM.AllBuyerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 632 | 15 | 1 | 32 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[fun_bu_usages_v|FUN_BU_USAGES_V]] — 8 atributos
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 18 atributos (2 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 5 atributos (2 BICC)
- [[per_addresses_f|PER_ADDRESSES_F]] — 55 atributos (2 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 279 atributos (4 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 19 atributos (2 BICC)
- [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]] — 102 atributos (4 BICC)
- [[per_email_addresses|PER_EMAIL_ADDRESSES]] — 13 atributos (2 BICC)
- [[per_jobs_f|PER_JOBS_F]] — 23 atributos (2 BICC)
- [[per_jobs_f_tl|PER_JOBS_F_TL]] — 5 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 71 atributos (5 BICC)
- [[per_phones|PER_PHONES]] — 20 atributos (2 BICC)
- [[per_users|PER_USERS]] — 2 atributos (1 BICC)
- [[po_agents_v|PO_AGENTS_V]] — 1 atributos (1 PKs, 1 BICC)
- [[po_agent_assignments|PO_AGENT_ASSIGNMENTS]] — 11 atributos (1 BICC)

---

## ⚙️ Atributos

### [[fun_bu_usages_v|FUN_BU_USAGES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitUsageBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 2 | BusinessUnitUsageConfigurationStatus | CONFIGURATION_STATUS | — | — |
| 3 | BusinessUnitUsageModuleId | MODULE_ID | — | — |
| 4 | BusinessUnitUsageModuleKey | MODULE_KEY | — | — |
| 5 | BusinessUnitUsageModuleName | MODULE_NAME | — | — |
| 6 | BusinessUnitUsageName | BU_NAME | — | — |
| 7 | BusinessUnitUsageShortCode | SHORT_CODE | — | — |
| 8 | BusinessUnitUsageStatus | STATUS | — | — |

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | OrganizationBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | OrganizationCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 4 | OrganizationCreatedBy | CREATED_BY | — | — |
| 5 | OrganizationCreationDate | CREATION_DATE | — | — |
| 6 | OrganizationEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | OrganizationEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | OrganizationEstablishmentId | ESTABLISHMENT_ID | — | — |
| 9 | OrganizationInternalAddressLine | INTERNAL_ADDRESS_LINE | — | — |
| 10 | OrganizationInternalExternalFlag | INTERNAL_EXTERNAL_FLAG | — | — |
| 11 | OrganizationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | OrganizationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | OrganizationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | OrganizationLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | OrganizationLocationId | LOCATION_ID | — | — |
| 16 | OrganizationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | OrganizationOrganizationId | ORGANIZATION_ID | — | — |
| 18 | OrganizationType | TYPE | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgUnitTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrgUnitTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OrgUnitTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | OrgUnitTranslationPEOName | NAME | — | ✅ |
| 5 | OrgUnitTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[per_addresses_f|PER_ADDRESSES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressAddlAddressAttribute1 | ADDL_ADDRESS_ATTRIBUTE1 | — | — |
| 2 | AddressAddlAddressAttribute2 | ADDL_ADDRESS_ATTRIBUTE2 | — | — |
| 3 | AddressAddlAddressAttribute3 | ADDL_ADDRESS_ATTRIBUTE3 | — | — |
| 4 | AddressAddlAddressAttribute4 | ADDL_ADDRESS_ATTRIBUTE4 | — | — |
| 5 | AddressAddlAddressAttribute5 | ADDL_ADDRESS_ATTRIBUTE5 | — | — |
| 6 | AddressAddrAttribute1 | ADDR_ATTRIBUTE1 | — | — |
| 7 | AddressAddrAttribute10 | ADDR_ATTRIBUTE10 | — | — |
| 8 | AddressAddrAttribute11 | ADDR_ATTRIBUTE11 | — | — |
| 9 | AddressAddrAttribute12 | ADDR_ATTRIBUTE12 | — | — |
| 10 | AddressAddrAttribute13 | ADDR_ATTRIBUTE13 | — | — |
| 11 | AddressAddrAttribute14 | ADDR_ATTRIBUTE14 | — | — |
| 12 | AddressAddrAttribute15 | ADDR_ATTRIBUTE15 | — | — |
| 13 | AddressAddrAttribute16 | ADDR_ATTRIBUTE16 | — | — |
| 14 | AddressAddrAttribute17 | ADDR_ATTRIBUTE17 | — | — |
| 15 | AddressAddrAttribute18 | ADDR_ATTRIBUTE18 | — | — |
| 16 | AddressAddrAttribute19 | ADDR_ATTRIBUTE19 | — | — |
| 17 | AddressAddrAttribute2 | ADDR_ATTRIBUTE2 | — | — |
| 18 | AddressAddrAttribute20 | ADDR_ATTRIBUTE20 | — | — |
| 19 | AddressAddrAttribute21 | ADDR_ATTRIBUTE21 | — | — |
| 20 | AddressAddrAttribute22 | ADDR_ATTRIBUTE22 | — | — |
| 21 | AddressAddrAttribute23 | ADDR_ATTRIBUTE23 | — | — |
| 22 | AddressAddrAttribute24 | ADDR_ATTRIBUTE24 | — | — |
| 23 | AddressAddrAttribute25 | ADDR_ATTRIBUTE25 | — | — |
| 24 | AddressAddrAttribute26 | ADDR_ATTRIBUTE26 | — | — |
| 25 | AddressAddrAttribute27 | ADDR_ATTRIBUTE27 | — | — |
| 26 | AddressAddrAttribute28 | ADDR_ATTRIBUTE28 | — | — |
| 27 | AddressAddrAttribute29 | ADDR_ATTRIBUTE29 | — | — |
| 28 | AddressAddrAttribute3 | ADDR_ATTRIBUTE3 | — | — |
| 29 | AddressAddrAttribute30 | ADDR_ATTRIBUTE30 | — | — |
| 30 | AddressAddrAttribute4 | ADDR_ATTRIBUTE4 | — | — |
| 31 | AddressAddrAttribute5 | ADDR_ATTRIBUTE5 | — | — |
| 32 | AddressAddrAttribute6 | ADDR_ATTRIBUTE6 | — | — |
| 33 | AddressAddrAttribute7 | ADDR_ATTRIBUTE7 | — | — |
| 34 | AddressAddrAttribute8 | ADDR_ATTRIBUTE8 | — | — |
| 35 | AddressAddrAttribute9 | ADDR_ATTRIBUTE9 | — | — |
| 36 | AddressAddrAttributeCategory | ADDR_ATTRIBUTE_CATEGORY | — | — |
| 37 | AddressAddressId | ADDRESS_ID | — | — |
| 38 | AddressBuilding | BUILDING | — | — |
| 39 | AddressBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 40 | AddressCreatedBy | CREATED_BY | — | — |
| 41 | AddressCreationDate | CREATION_DATE | — | — |
| 42 | AddressDerivedLocale | DERIVED_LOCALE | — | — |
| 43 | AddressDqValidationLevel | DQ_VALIDATION_LEVEL | — | — |
| 44 | AddressEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 45 | AddressEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 46 | AddressFloorNumber | FLOOR_NUMBER | — | — |
| 47 | AddressLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 48 | AddressLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 49 | AddressLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 50 | AddressLongPostalCode | LONG_POSTAL_CODE | — | — |
| 51 | AddressObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 52 | AddressRegion1 | REGION_1 | — | — |
| 53 | AddressRegion2 | REGION_2 | — | — |
| 54 | AddressRegion3 | REGION_3 | — | — |
| 55 | AddressTimezoneCode | TIMEZONE_CODE | — | — |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentActionCode | ACTION_CODE | — | — |
| 2 | AssignmentActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 3 | AssignmentAllowAsgOverrideFlag | ALLOW_ASG_OVERRIDE_FLAG | — | — |
| 4 | AssignmentApplicantRank | APPLICANT_RANK | — | — |
| 5 | AssignmentAsgInformation1 | ASG_INFORMATION1 | — | — |
| 6 | AssignmentAsgInformation10 | ASG_INFORMATION10 | — | — |
| 7 | AssignmentAsgInformation11 | ASG_INFORMATION11 | — | — |
| 8 | AssignmentAsgInformation12 | ASG_INFORMATION12 | — | — |
| 9 | AssignmentAsgInformation13 | ASG_INFORMATION13 | — | — |
| 10 | AssignmentAsgInformation14 | ASG_INFORMATION14 | — | — |
| 11 | AssignmentAsgInformation15 | ASG_INFORMATION15 | — | — |
| 12 | AssignmentAsgInformation16 | ASG_INFORMATION16 | — | — |
| 13 | AssignmentAsgInformation17 | ASG_INFORMATION17 | — | — |
| 14 | AssignmentAsgInformation18 | ASG_INFORMATION18 | — | — |
| 15 | AssignmentAsgInformation19 | ASG_INFORMATION19 | — | — |
| 16 | AssignmentAsgInformation2 | ASG_INFORMATION2 | — | — |
| 17 | AssignmentAsgInformation20 | ASG_INFORMATION20 | — | — |
| 18 | AssignmentAsgInformation21 | ASG_INFORMATION21 | — | — |
| 19 | AssignmentAsgInformation22 | ASG_INFORMATION22 | — | — |
| 20 | AssignmentAsgInformation23 | ASG_INFORMATION23 | — | — |
| 21 | AssignmentAsgInformation24 | ASG_INFORMATION24 | — | — |
| 22 | AssignmentAsgInformation25 | ASG_INFORMATION25 | — | — |
| 23 | AssignmentAsgInformation26 | ASG_INFORMATION26 | — | — |
| 24 | AssignmentAsgInformation27 | ASG_INFORMATION27 | — | — |
| 25 | AssignmentAsgInformation28 | ASG_INFORMATION28 | — | — |
| 26 | AssignmentAsgInformation29 | ASG_INFORMATION29 | — | — |
| 27 | AssignmentAsgInformation3 | ASG_INFORMATION3 | — | — |
| 28 | AssignmentAsgInformation30 | ASG_INFORMATION30 | — | — |
| 29 | AssignmentAsgInformation31 | ASG_INFORMATION31 | — | — |
| 30 | AssignmentAsgInformation32 | ASG_INFORMATION32 | — | — |
| 31 | AssignmentAsgInformation33 | ASG_INFORMATION33 | — | — |
| 32 | AssignmentAsgInformation34 | ASG_INFORMATION34 | — | — |
| 33 | AssignmentAsgInformation35 | ASG_INFORMATION35 | — | — |
| 34 | AssignmentAsgInformation36 | ASG_INFORMATION36 | — | — |
| 35 | AssignmentAsgInformation37 | ASG_INFORMATION37 | — | — |
| 36 | AssignmentAsgInformation38 | ASG_INFORMATION38 | — | — |
| 37 | AssignmentAsgInformation39 | ASG_INFORMATION39 | — | — |
| 38 | AssignmentAsgInformation4 | ASG_INFORMATION4 | — | — |
| 39 | AssignmentAsgInformation40 | ASG_INFORMATION40 | — | — |
| 40 | AssignmentAsgInformation41 | ASG_INFORMATION41 | — | — |
| 41 | AssignmentAsgInformation42 | ASG_INFORMATION42 | — | — |
| 42 | AssignmentAsgInformation43 | ASG_INFORMATION43 | — | — |
| 43 | AssignmentAsgInformation44 | ASG_INFORMATION44 | — | — |
| 44 | AssignmentAsgInformation45 | ASG_INFORMATION45 | — | — |
| 45 | AssignmentAsgInformation46 | ASG_INFORMATION46 | — | — |
| 46 | AssignmentAsgInformation47 | ASG_INFORMATION47 | — | — |
| 47 | AssignmentAsgInformation48 | ASG_INFORMATION48 | — | — |
| 48 | AssignmentAsgInformation49 | ASG_INFORMATION49 | — | — |
| 49 | AssignmentAsgInformation5 | ASG_INFORMATION5 | — | — |
| 50 | AssignmentAsgInformation50 | ASG_INFORMATION50 | — | — |
| 51 | AssignmentAsgInformation6 | ASG_INFORMATION6 | — | — |
| 52 | AssignmentAsgInformation7 | ASG_INFORMATION7 | — | — |
| 53 | AssignmentAsgInformation8 | ASG_INFORMATION8 | — | — |
| 54 | AssignmentAsgInformation9 | ASG_INFORMATION9 | — | — |
| 55 | AssignmentAsgInformationCategory | ASG_INFORMATION_CATEGORY | — | — |
| 56 | AssignmentAsgInformationDate1 | ASG_INFORMATION_DATE1 | — | — |
| 57 | AssignmentAsgInformationDate10 | ASG_INFORMATION_DATE10 | — | — |
| 58 | AssignmentAsgInformationDate11 | ASG_INFORMATION_DATE11 | — | — |
| 59 | AssignmentAsgInformationDate12 | ASG_INFORMATION_DATE12 | — | — |
| 60 | AssignmentAsgInformationDate13 | ASG_INFORMATION_DATE13 | — | — |
| 61 | AssignmentAsgInformationDate14 | ASG_INFORMATION_DATE14 | — | — |
| 62 | AssignmentAsgInformationDate15 | ASG_INFORMATION_DATE15 | — | — |
| 63 | AssignmentAsgInformationDate2 | ASG_INFORMATION_DATE2 | — | — |
| 64 | AssignmentAsgInformationDate3 | ASG_INFORMATION_DATE3 | — | — |
| 65 | AssignmentAsgInformationDate4 | ASG_INFORMATION_DATE4 | — | — |
| 66 | AssignmentAsgInformationDate5 | ASG_INFORMATION_DATE5 | — | — |
| 67 | AssignmentAsgInformationDate6 | ASG_INFORMATION_DATE6 | — | — |
| 68 | AssignmentAsgInformationDate7 | ASG_INFORMATION_DATE7 | — | — |
| 69 | AssignmentAsgInformationDate8 | ASG_INFORMATION_DATE8 | — | — |
| 70 | AssignmentAsgInformationDate9 | ASG_INFORMATION_DATE9 | — | — |
| 71 | AssignmentAsgInformationNumber1 | ASG_INFORMATION_NUMBER1 | — | — |
| 72 | AssignmentAsgInformationNumber10 | ASG_INFORMATION_NUMBER10 | — | — |
| 73 | AssignmentAsgInformationNumber11 | ASG_INFORMATION_NUMBER11 | — | — |
| 74 | AssignmentAsgInformationNumber12 | ASG_INFORMATION_NUMBER12 | — | — |
| 75 | AssignmentAsgInformationNumber13 | ASG_INFORMATION_NUMBER13 | — | — |
| 76 | AssignmentAsgInformationNumber14 | ASG_INFORMATION_NUMBER14 | — | — |
| 77 | AssignmentAsgInformationNumber15 | ASG_INFORMATION_NUMBER15 | — | — |
| 78 | AssignmentAsgInformationNumber16 | ASG_INFORMATION_NUMBER16 | — | — |
| 79 | AssignmentAsgInformationNumber17 | ASG_INFORMATION_NUMBER17 | — | — |
| 80 | AssignmentAsgInformationNumber18 | ASG_INFORMATION_NUMBER18 | — | — |
| 81 | AssignmentAsgInformationNumber19 | ASG_INFORMATION_NUMBER19 | — | — |
| 82 | AssignmentAsgInformationNumber2 | ASG_INFORMATION_NUMBER2 | — | — |
| 83 | AssignmentAsgInformationNumber20 | ASG_INFORMATION_NUMBER20 | — | — |
| 84 | AssignmentAsgInformationNumber3 | ASG_INFORMATION_NUMBER3 | — | — |
| 85 | AssignmentAsgInformationNumber4 | ASG_INFORMATION_NUMBER4 | — | — |
| 86 | AssignmentAsgInformationNumber5 | ASG_INFORMATION_NUMBER5 | — | — |
| 87 | AssignmentAsgInformationNumber6 | ASG_INFORMATION_NUMBER6 | — | — |
| 88 | AssignmentAsgInformationNumber7 | ASG_INFORMATION_NUMBER7 | — | — |
| 89 | AssignmentAsgInformationNumber8 | ASG_INFORMATION_NUMBER8 | — | — |
| 90 | AssignmentAsgInformationNumber9 | ASG_INFORMATION_NUMBER9 | — | — |
| 91 | AssignmentAssAttribute1 | ASS_ATTRIBUTE1 | — | — |
| 92 | AssignmentAssAttribute10 | ASS_ATTRIBUTE10 | — | — |
| 93 | AssignmentAssAttribute11 | ASS_ATTRIBUTE11 | — | — |
| 94 | AssignmentAssAttribute12 | ASS_ATTRIBUTE12 | — | — |
| 95 | AssignmentAssAttribute13 | ASS_ATTRIBUTE13 | — | — |
| 96 | AssignmentAssAttribute14 | ASS_ATTRIBUTE14 | — | — |
| 97 | AssignmentAssAttribute15 | ASS_ATTRIBUTE15 | — | — |
| 98 | AssignmentAssAttribute16 | ASS_ATTRIBUTE16 | — | — |
| 99 | AssignmentAssAttribute17 | ASS_ATTRIBUTE17 | — | — |
| 100 | AssignmentAssAttribute18 | ASS_ATTRIBUTE18 | — | — |
| 101 | AssignmentAssAttribute19 | ASS_ATTRIBUTE19 | — | — |
| 102 | AssignmentAssAttribute2 | ASS_ATTRIBUTE2 | — | — |
| 103 | AssignmentAssAttribute20 | ASS_ATTRIBUTE20 | — | — |
| 104 | AssignmentAssAttribute21 | ASS_ATTRIBUTE21 | — | — |
| 105 | AssignmentAssAttribute22 | ASS_ATTRIBUTE22 | — | — |
| 106 | AssignmentAssAttribute23 | ASS_ATTRIBUTE23 | — | — |
| 107 | AssignmentAssAttribute24 | ASS_ATTRIBUTE24 | — | — |
| 108 | AssignmentAssAttribute25 | ASS_ATTRIBUTE25 | — | — |
| 109 | AssignmentAssAttribute26 | ASS_ATTRIBUTE26 | — | — |
| 110 | AssignmentAssAttribute27 | ASS_ATTRIBUTE27 | — | — |
| 111 | AssignmentAssAttribute28 | ASS_ATTRIBUTE28 | — | — |
| 112 | AssignmentAssAttribute29 | ASS_ATTRIBUTE29 | — | — |
| 113 | AssignmentAssAttribute3 | ASS_ATTRIBUTE3 | — | — |
| 114 | AssignmentAssAttribute30 | ASS_ATTRIBUTE30 | — | — |
| 115 | AssignmentAssAttribute31 | ASS_ATTRIBUTE31 | — | — |
| 116 | AssignmentAssAttribute32 | ASS_ATTRIBUTE32 | — | — |
| 117 | AssignmentAssAttribute33 | ASS_ATTRIBUTE33 | — | — |
| 118 | AssignmentAssAttribute34 | ASS_ATTRIBUTE34 | — | — |
| 119 | AssignmentAssAttribute35 | ASS_ATTRIBUTE35 | — | — |
| 120 | AssignmentAssAttribute36 | ASS_ATTRIBUTE36 | — | — |
| 121 | AssignmentAssAttribute37 | ASS_ATTRIBUTE37 | — | — |
| 122 | AssignmentAssAttribute38 | ASS_ATTRIBUTE38 | — | — |
| 123 | AssignmentAssAttribute39 | ASS_ATTRIBUTE39 | — | — |
| 124 | AssignmentAssAttribute4 | ASS_ATTRIBUTE4 | — | — |
| 125 | AssignmentAssAttribute40 | ASS_ATTRIBUTE40 | — | — |
| 126 | AssignmentAssAttribute41 | ASS_ATTRIBUTE41 | — | — |
| 127 | AssignmentAssAttribute42 | ASS_ATTRIBUTE42 | — | — |
| 128 | AssignmentAssAttribute43 | ASS_ATTRIBUTE43 | — | — |
| 129 | AssignmentAssAttribute44 | ASS_ATTRIBUTE44 | — | — |
| 130 | AssignmentAssAttribute45 | ASS_ATTRIBUTE45 | — | — |
| 131 | AssignmentAssAttribute46 | ASS_ATTRIBUTE46 | — | — |
| 132 | AssignmentAssAttribute47 | ASS_ATTRIBUTE47 | — | — |
| 133 | AssignmentAssAttribute48 | ASS_ATTRIBUTE48 | — | — |
| 134 | AssignmentAssAttribute49 | ASS_ATTRIBUTE49 | — | — |
| 135 | AssignmentAssAttribute5 | ASS_ATTRIBUTE5 | — | — |
| 136 | AssignmentAssAttribute50 | ASS_ATTRIBUTE50 | — | — |
| 137 | AssignmentAssAttribute6 | ASS_ATTRIBUTE6 | — | — |
| 138 | AssignmentAssAttribute7 | ASS_ATTRIBUTE7 | — | — |
| 139 | AssignmentAssAttribute8 | ASS_ATTRIBUTE8 | — | — |
| 140 | AssignmentAssAttribute9 | ASS_ATTRIBUTE9 | — | — |
| 141 | AssignmentAssAttributeCategory | ASS_ATTRIBUTE_CATEGORY | — | — |
| 142 | AssignmentAssAttributeDate1 | ASS_ATTRIBUTE_DATE1 | — | — |
| 143 | AssignmentAssAttributeDate10 | ASS_ATTRIBUTE_DATE10 | — | — |
| 144 | AssignmentAssAttributeDate11 | ASS_ATTRIBUTE_DATE11 | — | — |
| 145 | AssignmentAssAttributeDate12 | ASS_ATTRIBUTE_DATE12 | — | — |
| 146 | AssignmentAssAttributeDate13 | ASS_ATTRIBUTE_DATE13 | — | — |
| 147 | AssignmentAssAttributeDate14 | ASS_ATTRIBUTE_DATE14 | — | — |
| 148 | AssignmentAssAttributeDate15 | ASS_ATTRIBUTE_DATE15 | — | — |
| 149 | AssignmentAssAttributeDate2 | ASS_ATTRIBUTE_DATE2 | — | — |
| 150 | AssignmentAssAttributeDate3 | ASS_ATTRIBUTE_DATE3 | — | — |
| 151 | AssignmentAssAttributeDate4 | ASS_ATTRIBUTE_DATE4 | — | — |
| 152 | AssignmentAssAttributeDate5 | ASS_ATTRIBUTE_DATE5 | — | — |
| 153 | AssignmentAssAttributeDate6 | ASS_ATTRIBUTE_DATE6 | — | — |
| 154 | AssignmentAssAttributeDate7 | ASS_ATTRIBUTE_DATE7 | — | — |
| 155 | AssignmentAssAttributeDate8 | ASS_ATTRIBUTE_DATE8 | — | — |
| 156 | AssignmentAssAttributeDate9 | ASS_ATTRIBUTE_DATE9 | — | — |
| 157 | AssignmentAssAttributeNumber1 | ASS_ATTRIBUTE_NUMBER1 | — | — |
| 158 | AssignmentAssAttributeNumber10 | ASS_ATTRIBUTE_NUMBER10 | — | — |
| 159 | AssignmentAssAttributeNumber11 | ASS_ATTRIBUTE_NUMBER11 | — | — |
| 160 | AssignmentAssAttributeNumber12 | ASS_ATTRIBUTE_NUMBER12 | — | — |
| 161 | AssignmentAssAttributeNumber13 | ASS_ATTRIBUTE_NUMBER13 | — | — |
| 162 | AssignmentAssAttributeNumber14 | ASS_ATTRIBUTE_NUMBER14 | — | — |
| 163 | AssignmentAssAttributeNumber15 | ASS_ATTRIBUTE_NUMBER15 | — | — |
| 164 | AssignmentAssAttributeNumber16 | ASS_ATTRIBUTE_NUMBER16 | — | — |
| 165 | AssignmentAssAttributeNumber17 | ASS_ATTRIBUTE_NUMBER17 | — | — |
| 166 | AssignmentAssAttributeNumber18 | ASS_ATTRIBUTE_NUMBER18 | — | — |
| 167 | AssignmentAssAttributeNumber19 | ASS_ATTRIBUTE_NUMBER19 | — | — |
| 168 | AssignmentAssAttributeNumber2 | ASS_ATTRIBUTE_NUMBER2 | — | — |
| 169 | AssignmentAssAttributeNumber20 | ASS_ATTRIBUTE_NUMBER20 | — | — |
| 170 | AssignmentAssAttributeNumber3 | ASS_ATTRIBUTE_NUMBER3 | — | — |
| 171 | AssignmentAssAttributeNumber4 | ASS_ATTRIBUTE_NUMBER4 | — | — |
| 172 | AssignmentAssAttributeNumber5 | ASS_ATTRIBUTE_NUMBER5 | — | — |
| 173 | AssignmentAssAttributeNumber6 | ASS_ATTRIBUTE_NUMBER6 | — | — |
| 174 | AssignmentAssAttributeNumber7 | ASS_ATTRIBUTE_NUMBER7 | — | — |
| 175 | AssignmentAssAttributeNumber8 | ASS_ATTRIBUTE_NUMBER8 | — | — |
| 176 | AssignmentAssAttributeNumber9 | ASS_ATTRIBUTE_NUMBER9 | — | — |
| 177 | AssignmentAssignmentId | ASSIGNMENT_ID | — | — |
| 178 | AssignmentAssignmentName | ASSIGNMENT_NAME | — | — |
| 179 | AssignmentAssignmentNumber | ASSIGNMENT_NUMBER | — | — |
| 180 | AssignmentAssignmentSequence | ASSIGNMENT_SEQUENCE | — | — |
| 181 | AssignmentAssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | ✅ |
| 182 | AssignmentAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | — |
| 183 | AssignmentAssignmentType | ASSIGNMENT_TYPE | — | — |
| 184 | AssignmentAutoEndFlag | AUTO_END_FLAG | — | — |
| 185 | AssignmentBargainingUnitCode | BARGAINING_UNIT_CODE | — | — |
| 186 | AssignmentBillingTitle | BILLING_TITLE | — | — |
| 187 | AssignmentBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 188 | AssignmentBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 189 | AssignmentCagrGradeDefId | CAGR_GRADE_DEF_ID | — | — |
| 190 | AssignmentCagrIdFlexNum | CAGR_ID_FLEX_NUM | — | — |
| 191 | AssignmentCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 192 | AssignmentContractId | CONTRACT_ID | — | — |
| 193 | AssignmentCreatedBy | CREATED_BY | — | — |
| 194 | AssignmentCreationDate | CREATION_DATE | — | — |
| 195 | AssignmentDateProbationEnd | DATE_PROBATION_END | — | — |
| 196 | AssignmentDefaultCodeCombId | DEFAULT_CODE_COMB_ID | — | — |
| 197 | AssignmentDutiesType | DUTIES_TYPE | — | — |
| 198 | AssignmentEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 199 | AssignmentEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 200 | AssignmentEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 201 | AssignmentEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 202 | AssignmentEmployeeCategory | EMPLOYEE_CATEGORY | — | — |
| 203 | AssignmentEmploymentCategory | EMPLOYMENT_CATEGORY | — | — |
| 204 | AssignmentEstablishmentId | ESTABLISHMENT_ID | — | — |
| 205 | AssignmentExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | — |
| 206 | AssignmentFreezeStartDate | FREEZE_START_DATE | — | — |
| 207 | AssignmentFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 208 | AssignmentFrequency | FREQUENCY | — | — |
| 209 | AssignmentGradeId | GRADE_ID | — | — |
| 210 | AssignmentGradeLadderPgmId | GRADE_LADDER_PGM_ID | — | — |
| 211 | AssignmentHourlySalariedCode | HOURLY_SALARIED_CODE | — | — |
| 212 | AssignmentIdFlexNum | ID_FLEX_NUM | — | — |
| 213 | AssignmentInternalBuilding | INTERNAL_BUILDING | — | — |
| 214 | AssignmentInternalFloor | INTERNAL_FLOOR | — | — |
| 215 | AssignmentInternalLocation | INTERNAL_LOCATION | — | — |
| 216 | AssignmentInternalMailstop | INTERNAL_MAILSTOP | — | — |
| 217 | AssignmentInternalOfficeNumber | INTERNAL_OFFICE_NUMBER | — | — |
| 218 | AssignmentJobId | JOB_ID | — | — |
| 219 | AssignmentJobPostSourceName | JOB_POST_SOURCE_NAME | — | — |
| 220 | AssignmentLabourUnionMemberFlag | LABOUR_UNION_MEMBER_FLAG | — | — |
| 221 | AssignmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 222 | AssignmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 223 | AssignmentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 224 | AssignmentLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 225 | AssignmentLegislationCode | LEGISLATION_CODE | — | — |
| 226 | AssignmentLinkageType | LINKAGE_TYPE | — | — |
| 227 | AssignmentLocationId | LOCATION_ID | — | — |
| 228 | AssignmentManagerFlag | MANAGER_FLAG | — | — |
| 229 | AssignmentNormalHours | NORMAL_HOURS | — | — |
| 230 | AssignmentNoticePeriod | NOTICE_PERIOD | — | — |
| 231 | AssignmentNoticePeriodUom | NOTICE_PERIOD_UOM | — | — |
| 232 | AssignmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 233 | AssignmentOrganizationId | ORGANIZATION_ID | — | — |
| 234 | AssignmentParentAssignmentId | PARENT_ASSIGNMENT_ID | — | — |
| 235 | AssignmentPeopleGroupId | PEOPLE_GROUP_ID | — | — |
| 236 | AssignmentPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 237 | AssignmentPersonId | PERSON_ID | — | — |
| 238 | AssignmentPersonReferredById | PERSON_REFERRED_BY_ID | — | — |
| 239 | AssignmentPersonTypeId | PERSON_TYPE_ID | — | — |
| 240 | AssignmentPoHeaderId | PO_HEADER_ID | — | — |
| 241 | AssignmentPoLineId | PO_LINE_ID | — | — |
| 242 | AssignmentPositionId | POSITION_ID | — | — |
| 243 | AssignmentPositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | — |
| 244 | AssignmentPostingContentId | POSTING_CONTENT_ID | — | — |
| 245 | AssignmentPrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | — |
| 246 | AssignmentPrimaryFlag | PRIMARY_FLAG | — | — |
| 247 | AssignmentPrimaryWorkRelationFlag | PRIMARY_WORK_RELATION_FLAG | — | — |
| 248 | AssignmentPrimaryWorkTermsFlag | PRIMARY_WORK_TERMS_FLAG | — | — |
| 249 | AssignmentProbationPeriod | PROBATION_PERIOD | — | — |
| 250 | AssignmentProbationUnit | PROBATION_UNIT | — | — |
| 251 | AssignmentProjectTitle | PROJECT_TITLE | — | — |
| 252 | AssignmentProjectedAssignmentEnd | PROJECTED_ASSIGNMENT_END | — | — |
| 253 | AssignmentProjectedStartDate | PROJECTED_START_DATE | — | — |
| 254 | AssignmentProposedWorkerType | PROPOSED_WORKER_TYPE | — | — |
| 255 | AssignmentReasonCode | REASON_CODE | — | — |
| 256 | AssignmentRecordCreator | RECORD_CREATOR | — | — |
| 257 | AssignmentRecruiterId | RECRUITER_ID | — | — |
| 258 | AssignmentRecruitmentActivityId | RECRUITMENT_ACTIVITY_ID | — | — |
| 259 | AssignmentRetirementAge | RETIREMENT_AGE | — | — |
| 260 | AssignmentRetirementDate | RETIREMENT_DATE | — | — |
| 261 | AssignmentSalReviewPeriod | SAL_REVIEW_PERIOD | — | — |
| 262 | AssignmentSalReviewPeriodFrequency | SAL_REVIEW_PERIOD_FREQUENCY | — | — |
| 263 | AssignmentSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 264 | AssignmentSoftCodingKeyflexId | SOFT_CODING_KEYFLEX_ID | — | — |
| 265 | AssignmentSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 266 | AssignmentSourceType | SOURCE_TYPE | — | — |
| 267 | AssignmentSpecialCeilingStepId | SPECIAL_CEILING_STEP_ID | — | — |
| 268 | AssignmentStepEntryDate | STEP_ENTRY_DATE | — | — |
| 269 | AssignmentSystemPersonType | SYSTEM_PERSON_TYPE | — | — |
| 270 | AssignmentTaxAddressId | TAX_ADDRESS_ID | — | — |
| 271 | AssignmentTimeNormalFinish | TIME_NORMAL_FINISH | — | — |
| 272 | AssignmentTimeNormalStart | TIME_NORMAL_START | — | — |
| 273 | AssignmentVacancyId | VACANCY_ID | — | — |
| 274 | AssignmentVendorAssignmentNumber | VENDOR_ASSIGNMENT_NUMBER | — | — |
| 275 | AssignmentVendorEmployeeNumber | VENDOR_EMPLOYEE_NUMBER | — | — |
| 276 | AssignmentVendorId | VENDOR_ID | — | — |
| 277 | AssignmentVendorSiteId | VENDOR_SITE_ID | — | — |
| 278 | AssignmentWorkAtHome | WORK_AT_HOME | — | — |
| 279 | AssignmentWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonApplicantNumber | APPLICANT_NUMBER | — | — |
| 2 | PersonBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | PersonCreatedBy | CREATED_BY | — | — |
| 4 | PersonCreationDate | CREATION_DATE | — | — |
| 5 | PersonEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | PersonEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | PersonLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PersonLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PersonLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PersonMailingAddressId | MAILING_ADDRESS_ID | — | — |
| 11 | PersonObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PersonPersonId | PERSON_ID | — | — |
| 13 | PersonPersonNumber | PERSON_NUMBER | — | — |
| 14 | PersonPrimaryEmailId | PRIMARY_EMAIL_ID | — | — |
| 15 | PersonPrimaryNidId | PRIMARY_NID_ID | — | — |
| 16 | PersonPrimaryNidNumber | PRIMARY_NID_NUMBER | — | — |
| 17 | PersonPrimaryPhoneId | PRIMARY_PHONE_ID | — | — |
| 18 | PersonStartDate | START_DATE | — | — |
| 19 | PersonWaiveDataProtect | WAIVE_DATA_PROTECT | — | — |

### [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentSupervisorActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | AssignmentSupervisorAssignmentId | ASSIGNMENT_ID | — | — |
| 3 | AssignmentSupervisorAssignmentSupervisorId | ASSIGNMENT_SUPERVISOR_ID | — | — |
| 4 | AssignmentSupervisorBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | AssignmentSupervisorCreatedBy | CREATED_BY | — | — |
| 6 | AssignmentSupervisorCreationDate | CREATION_DATE | — | — |
| 7 | AssignmentSupervisorEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | AssignmentSupervisorEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | AssignmentSupervisorFreezeStartDate | FREEZE_START_DATE | — | — |
| 10 | AssignmentSupervisorFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 11 | AssignmentSupervisorLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | AssignmentSupervisorLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | AssignmentSupervisorLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | AssignmentSupervisorManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | — |
| 15 | AssignmentSupervisorManagerId | MANAGER_ID | — | — |
| 16 | AssignmentSupervisorManagerType | MANAGER_TYPE | — | — |
| 17 | AssignmentSupervisorObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | AssignmentSupervisorPersonId | PERSON_ID | — | — |
| 19 | AssignmentSupervisorPrimaryFlag | PRIMARY_FLAG | — | — |
| 20 | AssignmentSupervisorSupAttribute1 | SUP_ATTRIBUTE1 | — | — |
| 21 | AssignmentSupervisorSupAttribute10 | SUP_ATTRIBUTE10 | — | — |
| 22 | AssignmentSupervisorSupAttribute11 | SUP_ATTRIBUTE11 | — | — |
| 23 | AssignmentSupervisorSupAttribute12 | SUP_ATTRIBUTE12 | — | — |
| 24 | AssignmentSupervisorSupAttribute13 | SUP_ATTRIBUTE13 | — | — |
| 25 | AssignmentSupervisorSupAttribute14 | SUP_ATTRIBUTE14 | — | — |
| 26 | AssignmentSupervisorSupAttribute15 | SUP_ATTRIBUTE15 | — | — |
| 27 | AssignmentSupervisorSupAttribute16 | SUP_ATTRIBUTE16 | — | — |
| 28 | AssignmentSupervisorSupAttribute17 | SUP_ATTRIBUTE17 | — | — |
| 29 | AssignmentSupervisorSupAttribute18 | SUP_ATTRIBUTE18 | — | — |
| 30 | AssignmentSupervisorSupAttribute19 | SUP_ATTRIBUTE19 | — | — |
| 31 | AssignmentSupervisorSupAttribute2 | SUP_ATTRIBUTE2 | — | — |
| 32 | AssignmentSupervisorSupAttribute20 | SUP_ATTRIBUTE20 | — | — |
| 33 | AssignmentSupervisorSupAttribute21 | SUP_ATTRIBUTE21 | — | — |
| 34 | AssignmentSupervisorSupAttribute22 | SUP_ATTRIBUTE22 | — | — |
| 35 | AssignmentSupervisorSupAttribute23 | SUP_ATTRIBUTE23 | — | — |
| 36 | AssignmentSupervisorSupAttribute24 | SUP_ATTRIBUTE24 | — | — |
| 37 | AssignmentSupervisorSupAttribute25 | SUP_ATTRIBUTE25 | — | — |
| 38 | AssignmentSupervisorSupAttribute26 | SUP_ATTRIBUTE26 | — | — |
| 39 | AssignmentSupervisorSupAttribute27 | SUP_ATTRIBUTE27 | — | — |
| 40 | AssignmentSupervisorSupAttribute28 | SUP_ATTRIBUTE28 | — | — |
| 41 | AssignmentSupervisorSupAttribute29 | SUP_ATTRIBUTE29 | — | — |
| 42 | AssignmentSupervisorSupAttribute3 | SUP_ATTRIBUTE3 | — | — |
| 43 | AssignmentSupervisorSupAttribute30 | SUP_ATTRIBUTE30 | — | — |
| 44 | AssignmentSupervisorSupAttribute4 | SUP_ATTRIBUTE4 | — | — |
| 45 | AssignmentSupervisorSupAttribute5 | SUP_ATTRIBUTE5 | — | — |
| 46 | AssignmentSupervisorSupAttribute6 | SUP_ATTRIBUTE6 | — | — |
| 47 | AssignmentSupervisorSupAttribute7 | SUP_ATTRIBUTE7 | — | — |
| 48 | AssignmentSupervisorSupAttribute8 | SUP_ATTRIBUTE8 | — | — |
| 49 | AssignmentSupervisorSupAttribute9 | SUP_ATTRIBUTE9 | — | — |
| 50 | AssignmentSupervisorSupAttributeCategory | SUP_ATTRIBUTE_CATEGORY | — | — |
| 51 | AssignmentSupervisorWorkingPercentage | WORKING_PERCENTAGE | — | — |
| 52 | SupervisorNameActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 53 | SupervisorNameAssignmentId | ASSIGNMENT_ID | — | — |
| 54 | SupervisorNameAssignmentSupervisorId | ASSIGNMENT_SUPERVISOR_ID | — | — |
| 55 | SupervisorNameBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 56 | SupervisorNameCreatedBy | CREATED_BY | — | — |
| 57 | SupervisorNameCreationDate | CREATION_DATE | — | — |
| 58 | SupervisorNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 59 | SupervisorNameEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 60 | SupervisorNameFreezeStartDate | FREEZE_START_DATE | — | — |
| 61 | SupervisorNameFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 62 | SupervisorNameLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 63 | SupervisorNameLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 64 | SupervisorNameLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 65 | SupervisorNameManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | — |
| 66 | SupervisorNameManagerId | MANAGER_ID | — | — |
| 67 | SupervisorNameManagerType | MANAGER_TYPE | — | — |
| 68 | SupervisorNameObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 69 | SupervisorNamePersonId | PERSON_ID | — | — |
| 70 | SupervisorNamePrimaryFlag | PRIMARY_FLAG | — | — |
| 71 | SupervisorNameSupAttribute1 | SUP_ATTRIBUTE1 | — | — |
| 72 | SupervisorNameSupAttribute10 | SUP_ATTRIBUTE10 | — | — |
| 73 | SupervisorNameSupAttribute11 | SUP_ATTRIBUTE11 | — | — |
| 74 | SupervisorNameSupAttribute12 | SUP_ATTRIBUTE12 | — | — |
| 75 | SupervisorNameSupAttribute13 | SUP_ATTRIBUTE13 | — | — |
| 76 | SupervisorNameSupAttribute14 | SUP_ATTRIBUTE14 | — | — |
| 77 | SupervisorNameSupAttribute15 | SUP_ATTRIBUTE15 | — | — |
| 78 | SupervisorNameSupAttribute16 | SUP_ATTRIBUTE16 | — | — |
| 79 | SupervisorNameSupAttribute17 | SUP_ATTRIBUTE17 | — | — |
| 80 | SupervisorNameSupAttribute18 | SUP_ATTRIBUTE18 | — | — |
| 81 | SupervisorNameSupAttribute19 | SUP_ATTRIBUTE19 | — | — |
| 82 | SupervisorNameSupAttribute2 | SUP_ATTRIBUTE2 | — | — |
| 83 | SupervisorNameSupAttribute20 | SUP_ATTRIBUTE20 | — | — |
| 84 | SupervisorNameSupAttribute21 | SUP_ATTRIBUTE21 | — | — |
| 85 | SupervisorNameSupAttribute22 | SUP_ATTRIBUTE22 | — | — |
| 86 | SupervisorNameSupAttribute23 | SUP_ATTRIBUTE23 | — | — |
| 87 | SupervisorNameSupAttribute24 | SUP_ATTRIBUTE24 | — | — |
| 88 | SupervisorNameSupAttribute25 | SUP_ATTRIBUTE25 | — | — |
| 89 | SupervisorNameSupAttribute26 | SUP_ATTRIBUTE26 | — | — |
| 90 | SupervisorNameSupAttribute27 | SUP_ATTRIBUTE27 | — | — |
| 91 | SupervisorNameSupAttribute28 | SUP_ATTRIBUTE28 | — | — |
| 92 | SupervisorNameSupAttribute29 | SUP_ATTRIBUTE29 | — | — |
| 93 | SupervisorNameSupAttribute3 | SUP_ATTRIBUTE3 | — | — |
| 94 | SupervisorNameSupAttribute30 | SUP_ATTRIBUTE30 | — | — |
| 95 | SupervisorNameSupAttribute4 | SUP_ATTRIBUTE4 | — | — |
| 96 | SupervisorNameSupAttribute5 | SUP_ATTRIBUTE5 | — | — |
| 97 | SupervisorNameSupAttribute6 | SUP_ATTRIBUTE6 | — | — |
| 98 | SupervisorNameSupAttribute7 | SUP_ATTRIBUTE7 | — | — |
| 99 | SupervisorNameSupAttribute8 | SUP_ATTRIBUTE8 | — | — |
| 100 | SupervisorNameSupAttribute9 | SUP_ATTRIBUTE9 | — | — |
| 101 | SupervisorNameSupAttributeCategory | SUP_ATTRIBUTE_CATEGORY | — | — |
| 102 | SupervisorNameWorkingPercentage | WORKING_PERCENTAGE | — | — |

### [[per_email_addresses|PER_EMAIL_ADDRESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EmailAddressBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | EmailAddressCreatedBy | CREATED_BY | — | — |
| 3 | EmailAddressCreationDate | CREATION_DATE | — | — |
| 4 | EmailAddressDateFrom | DATE_FROM | — | — |
| 5 | EmailAddressDateTo | DATE_TO | — | — |
| 6 | EmailAddressEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 7 | EmailAddressEmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 8 | EmailAddressEmailType | EMAIL_TYPE | — | — |
| 9 | EmailAddressLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | EmailAddressLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | EmailAddressLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | EmailAddressObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | EmailAddressPersonId | PERSON_ID | — | — |

### [[per_jobs_f|PER_JOBS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobsActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | JobsActiveStatus | ACTIVE_STATUS | — | — |
| 3 | JobsApprovalAuthority | APPROVAL_AUTHORITY | — | — |
| 4 | JobsBenchmarkJobFlag | BENCHMARK_JOB_FLAG | — | — |
| 5 | JobsBenchmarkJobId | BENCHMARK_JOB_ID | — | — |
| 6 | JobsBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 7 | JobsCreatedBy | CREATED_BY | — | — |
| 8 | JobsCreationDate | CREATION_DATE | — | — |
| 9 | JobsEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 10 | JobsEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 11 | JobsFullPartTime | FULL_PART_TIME | — | — |
| 12 | JobsJobCode | JOB_CODE | — | — |
| 13 | JobsJobFamilyId | JOB_FAMILY_ID | — | — |
| 14 | JobsJobFunctionCode | JOB_FUNCTION_CODE | — | — |
| 15 | JobsJobId | JOB_ID | — | — |
| 16 | JobsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | JobsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | JobsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | JobsManagerLevel | MANAGER_LEVEL | — | — |
| 20 | JobsMedCheckupReq | MED_CHECKUP_REQ | — | — |
| 21 | JobsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | JobsRegularTemporary | REGULAR_TEMPORARY | — | — |
| 23 | JobsSetId | SET_ID | — | — |

### [[per_jobs_f_tl|PER_JOBS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | JobTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | JobTranslationPEOJobId | JOB_ID | — | — |
| 4 | JobTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | JobTranslationPEOName | NAME | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNameBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | PersonNameCreatedBy | CREATED_BY | — | — |
| 3 | PersonNameCreationDate | CREATION_DATE | — | — |
| 4 | PersonNameDisplayName | DISPLAY_NAME | — | — |
| 5 | PersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | PersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | PersonNameFirstName | FIRST_NAME | — | — |
| 8 | PersonNameFullName | FULL_NAME | — | ✅ |
| 9 | PersonNameHonors | HONORS | — | — |
| 10 | PersonNameKnownAs | KNOWN_AS | — | — |
| 11 | PersonNameLastName | LAST_NAME | — | — |
| 12 | PersonNameLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PersonNameLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | PersonNameLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | PersonNameLegislationCode | LEGISLATION_CODE | — | — |
| 16 | PersonNameListName | LIST_NAME | — | — |
| 17 | PersonNameMiddleNames | MIDDLE_NAMES | — | — |
| 18 | PersonNameMilitaryRank | MILITARY_RANK | — | — |
| 19 | PersonNameNamInformation1 | NAM_INFORMATION1 | — | — |
| 20 | PersonNameNamInformation10 | NAM_INFORMATION10 | — | — |
| 21 | PersonNameNamInformation11 | NAM_INFORMATION11 | — | — |
| 22 | PersonNameNamInformation12 | NAM_INFORMATION12 | — | — |
| 23 | PersonNameNamInformation13 | NAM_INFORMATION13 | — | — |
| 24 | PersonNameNamInformation14 | NAM_INFORMATION14 | — | — |
| 25 | PersonNameNamInformation15 | NAM_INFORMATION15 | — | — |
| 26 | PersonNameNamInformation16 | NAM_INFORMATION16 | — | — |
| 27 | PersonNameNamInformation17 | NAM_INFORMATION17 | — | — |
| 28 | PersonNameNamInformation18 | NAM_INFORMATION18 | — | — |
| 29 | PersonNameNamInformation19 | NAM_INFORMATION19 | — | — |
| 30 | PersonNameNamInformation2 | NAM_INFORMATION2 | — | — |
| 31 | PersonNameNamInformation20 | NAM_INFORMATION20 | — | — |
| 32 | PersonNameNamInformation21 | NAM_INFORMATION21 | — | — |
| 33 | PersonNameNamInformation22 | NAM_INFORMATION22 | — | — |
| 34 | PersonNameNamInformation23 | NAM_INFORMATION23 | — | — |
| 35 | PersonNameNamInformation24 | NAM_INFORMATION24 | — | — |
| 36 | PersonNameNamInformation25 | NAM_INFORMATION25 | — | — |
| 37 | PersonNameNamInformation26 | NAM_INFORMATION26 | — | — |
| 38 | PersonNameNamInformation27 | NAM_INFORMATION27 | — | — |
| 39 | PersonNameNamInformation28 | NAM_INFORMATION28 | — | — |
| 40 | PersonNameNamInformation29 | NAM_INFORMATION29 | — | — |
| 41 | PersonNameNamInformation3 | NAM_INFORMATION3 | — | — |
| 42 | PersonNameNamInformation30 | NAM_INFORMATION30 | — | — |
| 43 | PersonNameNamInformation4 | NAM_INFORMATION4 | — | — |
| 44 | PersonNameNamInformation5 | NAM_INFORMATION5 | — | — |
| 45 | PersonNameNamInformation6 | NAM_INFORMATION6 | — | — |
| 46 | PersonNameNamInformation7 | NAM_INFORMATION7 | — | — |
| 47 | PersonNameNamInformation8 | NAM_INFORMATION8 | — | — |
| 48 | PersonNameNamInformation9 | NAM_INFORMATION9 | — | — |
| 49 | PersonNameNamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 50 | PersonNameNameType | NAME_TYPE | — | — |
| 51 | PersonNameObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 52 | PersonNameOrderName | ORDER_NAME | — | — |
| 53 | PersonNamePersonId | PERSON_ID | — | — |
| 54 | PersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 55 | PersonNamePreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 56 | PersonNamePreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 57 | PersonNameSuffix | SUFFIX | — | — |
| 58 | PersonNameTitle | TITLE | — | — |
| 59 | SupervisorNamePEODisplayName | DISPLAY_NAME | — | — |
| 60 | SupervisorNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 61 | SupervisorNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 62 | SupervisorNamePEOFirstName | FIRST_NAME | — | — |
| 63 | SupervisorNamePEOFullName | FULL_NAME | — | ✅ |
| 64 | SupervisorNamePEOHonors | HONORS | — | — |
| 65 | SupervisorNamePEOKnownAs | KNOWN_AS | — | — |
| 66 | SupervisorNamePEOLastName | LAST_NAME | — | — |
| 67 | SupervisorNamePEOListName | LIST_NAME | — | — |
| 68 | SupervisorNamePEOMiddleNames | MIDDLE_NAMES | — | — |
| 69 | SupervisorNamePEOMilitaryRank | MILITARY_RANK | — | — |
| 70 | SupervisorNamePEONameType | NAME_TYPE | — | — |
| 71 | SupervisorNamePEOPersonNameId | PERSON_NAME_ID | — | — |

### [[per_phones|PER_PHONES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhoneAreaCode | AREA_CODE | — | — |
| 2 | PhoneBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | PhoneCountryCodeNumber | COUNTRY_CODE_NUMBER | — | — |
| 4 | PhoneCreatedBy | CREATED_BY | — | — |
| 5 | PhoneCreationDate | CREATION_DATE | — | — |
| 6 | PhoneDateFrom | DATE_FROM | — | — |
| 7 | PhoneDateTo | DATE_TO | — | — |
| 8 | PhoneExtension | EXTENSION | — | — |
| 9 | PhoneLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | PhoneLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | PhoneLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | PhoneLegislationCode | LEGISLATION_CODE | — | — |
| 13 | PhoneObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | PhonePersonId | PERSON_ID | — | — |
| 15 | PhonePhoneId | PHONE_ID | — | — |
| 16 | PhonePhoneNumber | PHONE_NUMBER | — | ✅ |
| 17 | PhonePhoneType | PHONE_TYPE | — | — |
| 18 | PhoneSearchPhoneNumber | SEARCH_PHONE_NUMBER | — | — |
| 19 | PhoneSpeedDialNumber | SPEED_DIAL_NUMBER | — | — |
| 20 | PhoneValidity | VALIDITY | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserPEOUserId | USER_ID | — | — |
| 2 | UserPEOUsername | USERNAME | — | ✅ |

### [[po_agents_v|PO_AGENTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgentId | AGENT_ID | 🔑 | ✅ |

### [[po_agent_assignments|PO_AGENT_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BuyerAssignmentActiveFlag | ACTIVE_FLAG | — | — |
| 2 | BuyerAssignmentAgentId | AGENT_ID | — | — |
| 3 | BuyerAssignmentAssignmentId | ASSIGNMENT_ID | — | — |
| 4 | BuyerAssignmentCreatedBy | CREATED_BY | — | — |
| 5 | BuyerAssignmentCreationDate | CREATION_DATE | — | — |
| 6 | BuyerAssignmentDefaultReqBuId | DEFAULT_REQ_BU_ID | — | — |
| 7 | BuyerAssignmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | BuyerAssignmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | BuyerAssignmentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | BuyerAssignmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | BuyerAssignmentPrcBuId | PRC_BU_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
