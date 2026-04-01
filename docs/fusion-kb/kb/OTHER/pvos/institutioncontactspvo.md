---
id: DOC-OTHER-PVO-InstitutionContactsPVO
doc_type: system-doc
title: "InstitutionContactsPVO — PVO Cross-Module"
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
  - InstitutionContactsPVO
  - institutioncontactspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InstitutionContactsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Institution Contacts. Acessa as tabelas: GMS_INSTITUTION_CONTACTS, HR_LOCATIONS_ALL_F_VL, PER_ALL_ASSIGNMENTS_M (+6).

**Caminho:** `FscmTopModelAM.GmsSetupAM.InstitutionContactsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 47 | 9 | 1 | 13 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[gms_institution_contacts|GMS_INSTITUTION_CONTACTS]] — 11 atributos (1 PKs, 2 BICC)
- [[hr_locations_all_f_vl|HR_LOCATIONS_ALL_F_VL]] — 4 atributos (2 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 10 atributos (1 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos (1 BICC)
- [[per_departments|PER_DEPARTMENTS]] — 4 atributos (1 BICC)
- [[per_display_phones_v|PER_DISPLAY_PHONES_V]] — 2 atributos (1 BICC)
- [[per_email_addresses|PER_EMAIL_ADDRESSES]] — 3 atributos (1 BICC)
- [[per_jobs_f_vl|PER_JOBS_F_VL]] — 5 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (2 BICC)

---

## ⚙️ Atributos

### [[gms_institution_contacts|GMS_INSTITUTION_CONTACTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstitutionContactsPEOCreatedBy | CREATED_BY | — | — |
| 2 | InstitutionContactsPEOCreationDate | CREATION_DATE | — | — |
| 3 | InstitutionContactsPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 4 | InstitutionContactsPEOInstitutionId | INSTITUTION_ID | — | — |
| 5 | InstitutionContactsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | InstitutionContactsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | InstitutionContactsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | InstitutionContactsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | InstitutionContactsPEOPersonId | PERSON_ID | — | — |
| 10 | InstitutionContactsPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 11 | InstnContactId | INSTN_CONTACT_ID | 🔑 | ✅ |

### [[hr_locations_all_f_vl|HR_LOCATIONS_ALL_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | LocationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | LocationDPEOLocationId | LOCATION_ID | — | — |
| 4 | LocationDPEOLocationName | LOCATION_NAME | — | ✅ |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentDPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentDPEOAssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | — |
| 3 | AssignmentDPEOAssignmentType | ASSIGNMENT_TYPE | — | — |
| 4 | AssignmentDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | AssignmentDPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 6 | AssignmentDPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 7 | AssignmentDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | AssignmentDPEOJobId | JOB_ID | — | — |
| 9 | AssignmentDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | AssignmentDPEOPrimaryFlag | PRIMARY_FLAG | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDPEOPersonId | PERSON_ID | — | — |

### [[per_departments|PER_DEPARTMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepartmentDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | DepartmentDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | DepartmentDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | DepartmentDPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[per_display_phones_v|PER_DISPLAY_PHONES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhonePEOPhoneId | PHONE_ID | — | — |
| 2 | PhonePEOPhoneNumber | PHONE_NUMBER | — | ✅ |

### [[per_email_addresses|PER_EMAIL_ADDRESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EmailAddressPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 2 | EmailAddressPEOEmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 3 | EmailAddressPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_jobs_f_vl|PER_JOBS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | JobDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | JobDPEOJobId | JOB_ID | — | — |
| 4 | JobDPEOName | NAME | — | ✅ |
| 5 | JobDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNameDPEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonNameDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | PersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
