---
id: DOC-OTHER-PVO-ManagerHrchyBottomUpPVOLineManager
doc_type: system-doc
title: "ManagerHrchyBottomUpPVOLineManager — PVO Cross-Module"
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
  - ManagerHrchyBottomUpPVOLineManager
  - managerhrchybottomuppvolinemanager
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ManagerHrchyBottomUpPVOLineManager

## 📌 Visão Geral

View Object para extração BICC de dados de Manager Hrchy Bottom Up Line Manager. Acessa as tabelas: PER_ALL_PEOPLE_F, PER_EMAIL_ADDRESSES, PER_MANAGER_HRCHY_CF (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ManagerHierarchyAM.ManagerHrchyBottomUpPVOLineManager`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 314 | 4 | 5 | 91 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 80 atributos (35 BICC)
- [[per_email_addresses|PER_EMAIL_ADDRESSES]] — 80 atributos (15 BICC)
- [[per_manager_hrchy_cf|PER_MANAGER_HRCHY_CF]] — 54 atributos (5 PKs, 6 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 100 atributos (35 BICC)

---

## ⚙️ Atributos

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOL10EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDetailsPEOL10EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDetailsPEOL10PersonId | PERSON_ID | — | — |
| 4 | PersonDetailsPEOL10PersonNumber | PERSON_NUMBER | — | ✅ |
| 5 | PersonDetailsPEOL11EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | PersonDetailsPEOL11EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | PersonDetailsPEOL11PersonId | PERSON_ID | — | — |
| 8 | PersonDetailsPEOL11PersonNumber | PERSON_NUMBER | — | ✅ |
| 9 | PersonDetailsPEOL12EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 10 | PersonDetailsPEOL12EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 11 | PersonDetailsPEOL12PersonId | PERSON_ID | — | — |
| 12 | PersonDetailsPEOL12PersonNumber | PERSON_NUMBER | — | ✅ |
| 13 | PersonDetailsPEOL13EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 14 | PersonDetailsPEOL13EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 15 | PersonDetailsPEOL13PersonId | PERSON_ID | — | — |
| 16 | PersonDetailsPEOL13PersonNumber | PERSON_NUMBER | — | ✅ |
| 17 | PersonDetailsPEOL14EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | PersonDetailsPEOL14EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 19 | PersonDetailsPEOL14PersonId | PERSON_ID | — | — |
| 20 | PersonDetailsPEOL14PersonNumber | PERSON_NUMBER | — | ✅ |
| 21 | PersonDetailsPEOL15EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 22 | PersonDetailsPEOL15EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 23 | PersonDetailsPEOL15PersonId | PERSON_ID | — | — |
| 24 | PersonDetailsPEOL15PersonNumber | PERSON_NUMBER | — | ✅ |
| 25 | PersonDetailsPEOL16EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 26 | PersonDetailsPEOL16EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 27 | PersonDetailsPEOL16PersonId | PERSON_ID | — | — |
| 28 | PersonDetailsPEOL16PersonNumber | PERSON_NUMBER | — | — |
| 29 | PersonDetailsPEOL17EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 30 | PersonDetailsPEOL17EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 31 | PersonDetailsPEOL17PersonId | PERSON_ID | — | — |
| 32 | PersonDetailsPEOL17PersonNumber | PERSON_NUMBER | — | — |
| 33 | PersonDetailsPEOL18EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 34 | PersonDetailsPEOL18EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 35 | PersonDetailsPEOL18PersonId | PERSON_ID | — | — |
| 36 | PersonDetailsPEOL18PersonNumber | PERSON_NUMBER | — | — |
| 37 | PersonDetailsPEOL19EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 38 | PersonDetailsPEOL19EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 39 | PersonDetailsPEOL19PersonId | PERSON_ID | — | — |
| 40 | PersonDetailsPEOL19PersonNumber | PERSON_NUMBER | — | — |
| 41 | PersonDetailsPEOL1EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 42 | PersonDetailsPEOL1EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 43 | PersonDetailsPEOL1PersonId | PERSON_ID | — | — |
| 44 | PersonDetailsPEOL1PersonNumber | PERSON_NUMBER | — | ✅ |
| 45 | PersonDetailsPEOL20EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 46 | PersonDetailsPEOL20EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 47 | PersonDetailsPEOL20PersonId | PERSON_ID | — | — |
| 48 | PersonDetailsPEOL20PersonNumber | PERSON_NUMBER | — | — |
| 49 | PersonDetailsPEOL2EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 50 | PersonDetailsPEOL2EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 51 | PersonDetailsPEOL2PersonId | PERSON_ID | — | — |
| 52 | PersonDetailsPEOL2PersonNumber | PERSON_NUMBER | — | ✅ |
| 53 | PersonDetailsPEOL3EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 54 | PersonDetailsPEOL3EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 55 | PersonDetailsPEOL3PersonId | PERSON_ID | — | — |
| 56 | PersonDetailsPEOL3PersonNumber | PERSON_NUMBER | — | ✅ |
| 57 | PersonDetailsPEOL4EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 58 | PersonDetailsPEOL4EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 59 | PersonDetailsPEOL4PersonId | PERSON_ID | — | — |
| 60 | PersonDetailsPEOL4PersonNumber | PERSON_NUMBER | — | ✅ |
| 61 | PersonDetailsPEOL5EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 62 | PersonDetailsPEOL5EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 63 | PersonDetailsPEOL5PersonId | PERSON_ID | — | — |
| 64 | PersonDetailsPEOL5PersonNumber | PERSON_NUMBER | — | ✅ |
| 65 | PersonDetailsPEOL6EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 66 | PersonDetailsPEOL6EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 67 | PersonDetailsPEOL6PersonId | PERSON_ID | — | — |
| 68 | PersonDetailsPEOL6PersonNumber | PERSON_NUMBER | — | ✅ |
| 69 | PersonDetailsPEOL7EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 70 | PersonDetailsPEOL7EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 71 | PersonDetailsPEOL7PersonId | PERSON_ID | — | — |
| 72 | PersonDetailsPEOL7PersonNumber | PERSON_NUMBER | — | ✅ |
| 73 | PersonDetailsPEOL8EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 74 | PersonDetailsPEOL8EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 75 | PersonDetailsPEOL8PersonId | PERSON_ID | — | — |
| 76 | PersonDetailsPEOL8PersonNumber | PERSON_NUMBER | — | ✅ |
| 77 | PersonDetailsPEOL9EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 78 | PersonDetailsPEOL9EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 79 | PersonDetailsPEOL9PersonId | PERSON_ID | — | — |
| 80 | PersonDetailsPEOL9PersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_email_addresses|PER_EMAIL_ADDRESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkEmailAddressesPEOL10EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 2 | WorkEmailAddressesPEOL10EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 3 | WorkEmailAddressesPEOL10EmailType | EMAIL_TYPE | — | — |
| 4 | WorkEmailAddressesPEOL10PersonId | PERSON_ID | — | — |
| 5 | WorkEmailAddressesPEOL11EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 6 | WorkEmailAddressesPEOL11EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 7 | WorkEmailAddressesPEOL11EmailType | EMAIL_TYPE | — | — |
| 8 | WorkEmailAddressesPEOL11PersonId | PERSON_ID | — | — |
| 9 | WorkEmailAddressesPEOL12EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 10 | WorkEmailAddressesPEOL12EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 11 | WorkEmailAddressesPEOL12EmailType | EMAIL_TYPE | — | — |
| 12 | WorkEmailAddressesPEOL12PersonId | PERSON_ID | — | — |
| 13 | WorkEmailAddressesPEOL13EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 14 | WorkEmailAddressesPEOL13EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 15 | WorkEmailAddressesPEOL13EmailType | EMAIL_TYPE | — | — |
| 16 | WorkEmailAddressesPEOL13PersonId | PERSON_ID | — | — |
| 17 | WorkEmailAddressesPEOL14EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 18 | WorkEmailAddressesPEOL14EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 19 | WorkEmailAddressesPEOL14EmailType | EMAIL_TYPE | — | — |
| 20 | WorkEmailAddressesPEOL14PersonId | PERSON_ID | — | — |
| 21 | WorkEmailAddressesPEOL15EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 22 | WorkEmailAddressesPEOL15EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 23 | WorkEmailAddressesPEOL15EmailType | EMAIL_TYPE | — | — |
| 24 | WorkEmailAddressesPEOL15PersonId | PERSON_ID | — | — |
| 25 | WorkEmailAddressesPEOL16EmailAddress | EMAIL_ADDRESS | — | — |
| 26 | WorkEmailAddressesPEOL16EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 27 | WorkEmailAddressesPEOL16EmailType | EMAIL_TYPE | — | — |
| 28 | WorkEmailAddressesPEOL16PersonId | PERSON_ID | — | — |
| 29 | WorkEmailAddressesPEOL17EmailAddress | EMAIL_ADDRESS | — | — |
| 30 | WorkEmailAddressesPEOL17EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 31 | WorkEmailAddressesPEOL17EmailType | EMAIL_TYPE | — | — |
| 32 | WorkEmailAddressesPEOL17PersonId | PERSON_ID | — | — |
| 33 | WorkEmailAddressesPEOL18EmailAddress | EMAIL_ADDRESS | — | — |
| 34 | WorkEmailAddressesPEOL18EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 35 | WorkEmailAddressesPEOL18EmailType | EMAIL_TYPE | — | — |
| 36 | WorkEmailAddressesPEOL18PersonId | PERSON_ID | — | — |
| 37 | WorkEmailAddressesPEOL19EmailAddress | EMAIL_ADDRESS | — | — |
| 38 | WorkEmailAddressesPEOL19EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 39 | WorkEmailAddressesPEOL19EmailType | EMAIL_TYPE | — | — |
| 40 | WorkEmailAddressesPEOL19PersonId | PERSON_ID | — | — |
| 41 | WorkEmailAddressesPEOL1EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 42 | WorkEmailAddressesPEOL1EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 43 | WorkEmailAddressesPEOL1EmailType | EMAIL_TYPE | — | — |
| 44 | WorkEmailAddressesPEOL1PersonId | PERSON_ID | — | — |
| 45 | WorkEmailAddressesPEOL20EmailAddress | EMAIL_ADDRESS | — | — |
| 46 | WorkEmailAddressesPEOL20EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 47 | WorkEmailAddressesPEOL20EmailType | EMAIL_TYPE | — | — |
| 48 | WorkEmailAddressesPEOL20PersonId | PERSON_ID | — | — |
| 49 | WorkEmailAddressesPEOL2EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 50 | WorkEmailAddressesPEOL2EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 51 | WorkEmailAddressesPEOL2EmailType | EMAIL_TYPE | — | — |
| 52 | WorkEmailAddressesPEOL2PersonId | PERSON_ID | — | — |
| 53 | WorkEmailAddressesPEOL3EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 54 | WorkEmailAddressesPEOL3EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 55 | WorkEmailAddressesPEOL3EmailType | EMAIL_TYPE | — | — |
| 56 | WorkEmailAddressesPEOL3PersonId | PERSON_ID | — | — |
| 57 | WorkEmailAddressesPEOL4EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 58 | WorkEmailAddressesPEOL4EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 59 | WorkEmailAddressesPEOL4EmailType | EMAIL_TYPE | — | — |
| 60 | WorkEmailAddressesPEOL4PersonId | PERSON_ID | — | — |
| 61 | WorkEmailAddressesPEOL5EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 62 | WorkEmailAddressesPEOL5EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 63 | WorkEmailAddressesPEOL5EmailType | EMAIL_TYPE | — | — |
| 64 | WorkEmailAddressesPEOL5PersonId | PERSON_ID | — | — |
| 65 | WorkEmailAddressesPEOL6EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 66 | WorkEmailAddressesPEOL6EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 67 | WorkEmailAddressesPEOL6EmailType | EMAIL_TYPE | — | — |
| 68 | WorkEmailAddressesPEOL6PersonId | PERSON_ID | — | — |
| 69 | WorkEmailAddressesPEOL7EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 70 | WorkEmailAddressesPEOL7EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 71 | WorkEmailAddressesPEOL7EmailType | EMAIL_TYPE | — | — |
| 72 | WorkEmailAddressesPEOL7PersonId | PERSON_ID | — | — |
| 73 | WorkEmailAddressesPEOL8EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 74 | WorkEmailAddressesPEOL8EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 75 | WorkEmailAddressesPEOL8EmailType | EMAIL_TYPE | — | — |
| 76 | WorkEmailAddressesPEOL8PersonId | PERSON_ID | — | — |
| 77 | WorkEmailAddressesPEOL9EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 78 | WorkEmailAddressesPEOL9EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 79 | WorkEmailAddressesPEOL9EmailType | EMAIL_TYPE | — | — |
| 80 | WorkEmailAddressesPEOL9PersonId | PERSON_ID | — | — |

### [[per_manager_hrchy_cf|PER_MANAGER_HRCHY_CF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 5 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 6 | EnterpriseId | ENTERPRISE_ID | — | — |
| 7 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 8 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | Level10ManagerAssignmentId | LEVEL10_MANAGER_ASSIGNMENT_ID | — | — |
| 13 | Level10ManagerId | LEVEL10_MANAGER_ID | — | — |
| 14 | Level11ManagerAssignmentId | LEVEL11_MANAGER_ASSIGNMENT_ID | — | — |
| 15 | Level11ManagerId | LEVEL11_MANAGER_ID | — | — |
| 16 | Level12ManagerAssignmentId | LEVEL12_MANAGER_ASSIGNMENT_ID | — | — |
| 17 | Level12ManagerId | LEVEL12_MANAGER_ID | — | — |
| 18 | Level13ManagerAssignmentId | LEVEL13_MANAGER_ASSIGNMENT_ID | — | — |
| 19 | Level13ManagerId | LEVEL13_MANAGER_ID | — | — |
| 20 | Level14ManagerAssignmentId | LEVEL14_MANAGER_ASSIGNMENT_ID | — | — |
| 21 | Level14ManagerId | LEVEL14_MANAGER_ID | — | — |
| 22 | Level15ManagerAssignmentId | LEVEL15_MANAGER_ASSIGNMENT_ID | — | — |
| 23 | Level15ManagerId | LEVEL15_MANAGER_ID | — | — |
| 24 | Level16ManagerAssignmentId | LEVEL16_MANAGER_ASSIGNMENT_ID | — | — |
| 25 | Level16ManagerId | LEVEL16_MANAGER_ID | — | — |
| 26 | Level17ManagerAssignmentId | LEVEL17_MANAGER_ASSIGNMENT_ID | — | — |
| 27 | Level17ManagerId | LEVEL17_MANAGER_ID | — | — |
| 28 | Level18ManagerAssignmentId | LEVEL18_MANAGER_ASSIGNMENT_ID | — | — |
| 29 | Level18ManagerId | LEVEL18_MANAGER_ID | — | — |
| 30 | Level19ManagerAssignmentId | LEVEL19_MANAGER_ASSIGNMENT_ID | — | — |
| 31 | Level19ManagerId | LEVEL19_MANAGER_ID | — | — |
| 32 | Level1ManagerAssignmentId | LEVEL1_MANAGER_ASSIGNMENT_ID | — | — |
| 33 | Level1ManagerId | LEVEL1_MANAGER_ID | — | — |
| 34 | Level20ManagerAssignmentId | LEVEL20_MANAGER_ASSIGNMENT_ID | — | — |
| 35 | Level20ManagerId | LEVEL20_MANAGER_ID | — | — |
| 36 | Level2ManagerAssignmentId | LEVEL2_MANAGER_ASSIGNMENT_ID | — | — |
| 37 | Level2ManagerId | LEVEL2_MANAGER_ID | — | — |
| 38 | Level3ManagerAssignmentId | LEVEL3_MANAGER_ASSIGNMENT_ID | — | — |
| 39 | Level3ManagerId | LEVEL3_MANAGER_ID | — | — |
| 40 | Level4ManagerAssignmentId | LEVEL4_MANAGER_ASSIGNMENT_ID | — | — |
| 41 | Level4ManagerId | LEVEL4_MANAGER_ID | — | — |
| 42 | Level5ManagerAssignmentId | LEVEL5_MANAGER_ASSIGNMENT_ID | — | — |
| 43 | Level5ManagerId | LEVEL5_MANAGER_ID | — | — |
| 44 | Level6ManagerAssignmentId | LEVEL6_MANAGER_ASSIGNMENT_ID | — | — |
| 45 | Level6ManagerId | LEVEL6_MANAGER_ID | — | — |
| 46 | Level7ManagerAssignmentId | LEVEL7_MANAGER_ASSIGNMENT_ID | — | — |
| 47 | Level7ManagerId | LEVEL7_MANAGER_ID | — | — |
| 48 | Level8ManagerAssignmentId | LEVEL8_MANAGER_ASSIGNMENT_ID | — | — |
| 49 | Level8ManagerId | LEVEL8_MANAGER_ID | — | — |
| 50 | Level9ManagerAssignmentId | LEVEL9_MANAGER_ASSIGNMENT_ID | — | — |
| 51 | Level9ManagerId | LEVEL9_MANAGER_ID | — | — |
| 52 | ManagerType | MANAGER_TYPE | 🔑 | ✅ |
| 53 | PersonId | PERSON_ID | 🔑 | ✅ |
| 54 | RequestId | REQUEST_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNamePEOL10DisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonNamePEOL10EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNamePEOL10EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonNamePEOL10FullName | FULL_NAME | — | — |
| 5 | PersonNamePEOL10PersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonNamePEOL11DisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonNamePEOL11EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonNamePEOL11EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | PersonNamePEOL11FullName | FULL_NAME | — | — |
| 10 | PersonNamePEOL11PersonNameId | PERSON_NAME_ID | — | — |
| 11 | PersonNamePEOL12DisplayName | DISPLAY_NAME | — | ✅ |
| 12 | PersonNamePEOL12EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | PersonNamePEOL12EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 14 | PersonNamePEOL12FullName | FULL_NAME | — | — |
| 15 | PersonNamePEOL12PersonNameId | PERSON_NAME_ID | — | — |
| 16 | PersonNamePEOL13DisplayName | DISPLAY_NAME | — | ✅ |
| 17 | PersonNamePEOL13EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | PersonNamePEOL13EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 19 | PersonNamePEOL13FullName | FULL_NAME | — | — |
| 20 | PersonNamePEOL13PersonNameId | PERSON_NAME_ID | — | — |
| 21 | PersonNamePEOL14DisplayName | DISPLAY_NAME | — | ✅ |
| 22 | PersonNamePEOL14EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 23 | PersonNamePEOL14EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 24 | PersonNamePEOL14FullName | FULL_NAME | — | — |
| 25 | PersonNamePEOL14PersonNameId | PERSON_NAME_ID | — | — |
| 26 | PersonNamePEOL15DisplayName | DISPLAY_NAME | — | ✅ |
| 27 | PersonNamePEOL15EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 28 | PersonNamePEOL15EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 29 | PersonNamePEOL15FullName | FULL_NAME | — | — |
| 30 | PersonNamePEOL15PersonNameId | PERSON_NAME_ID | — | — |
| 31 | PersonNamePEOL16DisplayName | DISPLAY_NAME | — | — |
| 32 | PersonNamePEOL16EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 33 | PersonNamePEOL16EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 34 | PersonNamePEOL16FullName | FULL_NAME | — | — |
| 35 | PersonNamePEOL16PersonNameId | PERSON_NAME_ID | — | — |
| 36 | PersonNamePEOL17DisplayName | DISPLAY_NAME | — | — |
| 37 | PersonNamePEOL17EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 38 | PersonNamePEOL17EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 39 | PersonNamePEOL17FullName | FULL_NAME | — | — |
| 40 | PersonNamePEOL17PersonNameId | PERSON_NAME_ID | — | — |
| 41 | PersonNamePEOL18DisplayName | DISPLAY_NAME | — | — |
| 42 | PersonNamePEOL18EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 43 | PersonNamePEOL18EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 44 | PersonNamePEOL18FullName | FULL_NAME | — | — |
| 45 | PersonNamePEOL18PersonNameId | PERSON_NAME_ID | — | — |
| 46 | PersonNamePEOL19DisplayName | DISPLAY_NAME | — | — |
| 47 | PersonNamePEOL19EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 48 | PersonNamePEOL19EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 49 | PersonNamePEOL19FullName | FULL_NAME | — | — |
| 50 | PersonNamePEOL19PersonNameId | PERSON_NAME_ID | — | — |
| 51 | PersonNamePEOL1DisplayName | DISPLAY_NAME | — | ✅ |
| 52 | PersonNamePEOL1EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 53 | PersonNamePEOL1EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 54 | PersonNamePEOL1FullName | FULL_NAME | — | — |
| 55 | PersonNamePEOL1PersonNameId | PERSON_NAME_ID | — | — |
| 56 | PersonNamePEOL20DisplayName | DISPLAY_NAME | — | — |
| 57 | PersonNamePEOL20EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 58 | PersonNamePEOL20EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 59 | PersonNamePEOL20FullName | FULL_NAME | — | — |
| 60 | PersonNamePEOL20PersonNameId | PERSON_NAME_ID | — | — |
| 61 | PersonNamePEOL2DisplayName | DISPLAY_NAME | — | ✅ |
| 62 | PersonNamePEOL2EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 63 | PersonNamePEOL2EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 64 | PersonNamePEOL2FullName | FULL_NAME | — | — |
| 65 | PersonNamePEOL2PersonNameId | PERSON_NAME_ID | — | — |
| 66 | PersonNamePEOL3DisplayName | DISPLAY_NAME | — | ✅ |
| 67 | PersonNamePEOL3EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 68 | PersonNamePEOL3EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 69 | PersonNamePEOL3FullName | FULL_NAME | — | — |
| 70 | PersonNamePEOL3PersonNameId | PERSON_NAME_ID | — | — |
| 71 | PersonNamePEOL4DisplayName | DISPLAY_NAME | — | ✅ |
| 72 | PersonNamePEOL4EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 73 | PersonNamePEOL4EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 74 | PersonNamePEOL4FullName | FULL_NAME | — | — |
| 75 | PersonNamePEOL4PersonNameId | PERSON_NAME_ID | — | — |
| 76 | PersonNamePEOL5DisplayName | DISPLAY_NAME | — | ✅ |
| 77 | PersonNamePEOL5EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 78 | PersonNamePEOL5EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 79 | PersonNamePEOL5FullName | FULL_NAME | — | — |
| 80 | PersonNamePEOL5PersonNameId | PERSON_NAME_ID | — | — |
| 81 | PersonNamePEOL6DisplayName | DISPLAY_NAME | — | ✅ |
| 82 | PersonNamePEOL6EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 83 | PersonNamePEOL6EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 84 | PersonNamePEOL6FullName | FULL_NAME | — | — |
| 85 | PersonNamePEOL6PersonNameId | PERSON_NAME_ID | — | — |
| 86 | PersonNamePEOL7DisplayName | DISPLAY_NAME | — | ✅ |
| 87 | PersonNamePEOL7EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 88 | PersonNamePEOL7EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 89 | PersonNamePEOL7FullName | FULL_NAME | — | — |
| 90 | PersonNamePEOL7PersonNameId | PERSON_NAME_ID | — | — |
| 91 | PersonNamePEOL8DisplayName | DISPLAY_NAME | — | ✅ |
| 92 | PersonNamePEOL8EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 93 | PersonNamePEOL8EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 94 | PersonNamePEOL8FullName | FULL_NAME | — | — |
| 95 | PersonNamePEOL8PersonNameId | PERSON_NAME_ID | — | — |
| 96 | PersonNamePEOL9DisplayName | DISPLAY_NAME | — | ✅ |
| 97 | PersonNamePEOL9EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 98 | PersonNamePEOL9EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 99 | PersonNamePEOL9FullName | FULL_NAME | — | — |
| 100 | PersonNamePEOL9PersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
