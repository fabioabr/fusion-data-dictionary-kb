---
id: DOC-OTHER-PVO-AwardPersonnelPVO
doc_type: system-doc
title: "AwardPersonnelPVO — PVO Cross-Module"
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
  - AwardPersonnelPVO
  - awardpersonnelpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardPersonnelPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Personnel. Acessa as tabelas: GMS_AWARD_EXTERNAL_CONTACTS_V, GMS_AWARD_PERSONNEL, GMS_AWARD_PROJECTS (+3).

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardPersonnelPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 42 | 6 | 1 | 41 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_external_contacts_v|GMS_AWARD_EXTERNAL_CONTACTS_V]] — 7 atributos (7 BICC)
- [[gms_award_personnel|GMS_AWARD_PERSONNEL]] — 17 atributos (1 PKs, 17 BICC)
- [[gms_award_projects|GMS_AWARD_PROJECTS]] — 2 atributos (2 BICC)
- [[gms_internal_contacts_v|GMS_INTERNAL_CONTACTS_V]] — 7 atributos (7 BICC)
- [[gms_persons|GMS_PERSONS]] — 4 atributos (3 BICC)
- [[gms_roles_v|GMS_ROLES_V]] — 5 atributos (5 BICC)

---

## ⚙️ Atributos

### [[gms_award_external_contacts_v|GMS_AWARD_EXTERNAL_CONTACTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardExternalContactsPEOContactNumber | CONTACT_NUMBER | — | ✅ |
| 2 | AwardExternalContactsPEODepartment1 | DEPARTMENT | — | ✅ |
| 3 | AwardExternalContactsPEOEmailAddress2 | EMAIL_ADDRESS | — | ✅ |
| 4 | AwardExternalContactsPEOJobTitle2 | JOB_TITLE | — | ✅ |
| 5 | AwardExternalContactsPEOPartyId | PARTY_ID | — | ✅ |
| 6 | AwardExternalContactsPEOPartyName | PARTY_NAME | — | ✅ |
| 7 | AwardExternalContactsPEOPrimaryPhoneNumber1 | PRIMARY_PHONE_NUMBER | — | ✅ |

### [[gms_award_personnel|GMS_AWARD_PERSONNEL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardPersonnelPEOAwardId | AWARD_ID | — | ✅ |
| 2 | AwardPersonnelPEOAwdProjectLnkId | AWD_PROJECT_LNK_ID | — | ✅ |
| 3 | AwardPersonnelPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AwardPersonnelPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AwardPersonnelPEOCreditPercent | CREDIT_PERCENT | — | ✅ |
| 6 | AwardPersonnelPEOEndDate | END_DATE | — | ✅ |
| 7 | AwardPersonnelPEOInternalFlag | INTERNAL_FLAG | — | ✅ |
| 8 | AwardPersonnelPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | AwardPersonnelPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | AwardPersonnelPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | AwardPersonnelPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | AwardPersonnelPEOPartyId | PARTY_ID | — | ✅ |
| 13 | AwardPersonnelPEOPersonnelId | PERSONNEL_ID | — | ✅ |
| 14 | AwardPersonnelPEORole | ROLE | — | ✅ |
| 15 | AwardPersonnelPEORoleId | ROLE_ID | — | ✅ |
| 16 | AwardPersonnelPEOStartDate | START_DATE | — | ✅ |
| 17 | Id | ID | 🔑 | ✅ |

### [[gms_award_projects|GMS_AWARD_PROJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardProjectPEOId | ID | — | ✅ |
| 2 | AwardProjectPEOProjectId | PROJECT_ID | — | ✅ |

### [[gms_internal_contacts_v|GMS_INTERNAL_CONTACTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GrantsInternalContactPEODepartment | DEPARTMENT | — | ✅ |
| 2 | GrantsInternalContactPEOEmailAddress1 | EMAIL_ADDRESS | — | ✅ |
| 3 | GrantsInternalContactPEOJobTitle1 | JOB_TITLE | — | ✅ |
| 4 | GrantsInternalContactPEOName | NAME | — | ✅ |
| 5 | GrantsInternalContactPEOPersonId | PERSON_ID | — | ✅ |
| 6 | GrantsInternalContactPEOPersonNumber1 | PERSON_NUMBER | — | ✅ |
| 7 | GrantsInternalContactPEOPhoneNumber | PHONE_NUMBER | — | ✅ |

### [[gms_persons|GMS_PERSONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GrantPersonnelPEOConflictOfInterestComplete | CONFLICT_OF_INTEREST_COMPLETE | — | ✅ |
| 2 | GrantPersonnelPEOEligiblePi | ELIGIBLE_PI | — | ✅ |
| 3 | GrantsPersonnelPEOConflOfInterestCompDate | CONFL_OF_INTEREST_COMP_DATE | — | ✅ |
| 4 | GrantsPersonnelPEOPersonId | PERSON_ID | — | — |

### [[gms_roles_v|GMS_ROLES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GrantsRolesPEODescription | DESCRIPTION | — | ✅ |
| 2 | GrantsRolesPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 3 | GrantsRolesPEOProjectRoleId | PROJECT_ROLE_ID | — | ✅ |
| 4 | GrantsRolesPEOProjectRoleName | PROJECT_ROLE_NAME | — | ✅ |
| 5 | GrantsRolesPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
