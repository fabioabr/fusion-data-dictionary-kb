---
id: DOC-OTHER-PVO-StudentCredentialsDPVO
doc_type: system-doc
title: "StudentCredentialsDPVO — PVO Cross-Module"
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
  - StudentCredentialsDPVO
  - studentcredentialsdpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StudentCredentialsDPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Student Credentials D. Acessa as tabelas: HER_CREDENTIAL_VL, HER_SCT_CUR_CREDENTIAL_VL, HER_SCT_ITEM.

**Caminho:** `FscmTopModelAM.StudentEnrollmentAM.StudentCredentialsDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 208 | 3 | 1 | 18 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[her_credential_vl|HER_CREDENTIAL_VL]] — 66 atributos (10 BICC)
- [[her_sct_cur_credential_vl|HER_SCT_CUR_CREDENTIAL_VL]] — 71 atributos (1 PKs, 7 BICC)
- [[her_sct_item|HER_SCT_ITEM]] — 71 atributos (1 BICC)

---

## ⚙️ Atributos

### [[her_credential_vl|HER_CREDENTIAL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CredentialDPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | CredentialDPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | CredentialDPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | CredentialDPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | CredentialDPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | CredentialDPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | CredentialDPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | CredentialDPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | CredentialDPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | CredentialDPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | CredentialDPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | CredentialDPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | CredentialDPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | CredentialDPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | CredentialDPEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | CredentialDPEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | CredentialDPEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | CredentialDPEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | CredentialDPEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | CredentialDPEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | CredentialDPEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | CredentialDPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 23 | CredentialDPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | CredentialDPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 25 | CredentialDPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | CredentialDPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | CredentialDPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | CredentialDPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | CredentialDPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 30 | CredentialDPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 31 | CredentialDPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 32 | CredentialDPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 33 | CredentialDPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | CredentialDPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | CredentialDPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | CredentialDPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | CredentialDPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | CredentialDPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | CredentialDPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | CredentialDPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | CredentialDPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | CredentialDPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | CredentialDPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | CredentialDPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 45 | CredentialDPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 46 | CredentialDPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 47 | CredentialDPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 48 | CredentialDPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 49 | CredentialDPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 50 | CredentialDPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 51 | CredentialDPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 52 | CredentialDPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 53 | CredentialDPEOCreatedBy | CREATED_BY | — | — |
| 54 | CredentialDPEOCreationDate | CREATION_DATE | — | — |
| 55 | CredentialDPEOCredentialFormalName | CREDENTIAL_FORMAL_NAME | — | ✅ |
| 56 | CredentialDPEOCredentialId | CREDENTIAL_ID | — | ✅ |
| 57 | CredentialDPEOCredentialName | CREDENTIAL_NAME | — | ✅ |
| 58 | CredentialDPEOCredentialTypeCode | CREDENTIAL_TYPE_CODE | — | ✅ |
| 59 | CredentialDPEODescription | DESCRIPTION | — | ✅ |
| 60 | CredentialDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 61 | CredentialDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 62 | CredentialDPEOInternalFlag | INTERNAL_FLAG | — | — |
| 63 | CredentialDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 64 | CredentialDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 65 | CredentialDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 66 | CredentialDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[her_sct_cur_credential_vl|HER_SCT_CUR_CREDENTIAL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SctCredentialPEOAdministrationNotes | ADMINISTRATION_NOTES | — | ✅ |
| 2 | SctCredentialPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | SctCredentialPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | SctCredentialPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | SctCredentialPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | SctCredentialPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | SctCredentialPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | SctCredentialPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | SctCredentialPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | SctCredentialPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | SctCredentialPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | SctCredentialPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | SctCredentialPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | SctCredentialPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | SctCredentialPEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | SctCredentialPEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | SctCredentialPEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | SctCredentialPEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | SctCredentialPEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | SctCredentialPEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | SctCredentialPEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | SctCredentialPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | SctCredentialPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | SctCredentialPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 25 | SctCredentialPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | SctCredentialPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | SctCredentialPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | SctCredentialPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | SctCredentialPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 30 | SctCredentialPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 31 | SctCredentialPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 32 | SctCredentialPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 33 | SctCredentialPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | SctCredentialPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | SctCredentialPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | SctCredentialPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | SctCredentialPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | SctCredentialPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | SctCredentialPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | SctCredentialPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | SctCredentialPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | SctCredentialPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | SctCredentialPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | SctCredentialPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 45 | SctCredentialPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 46 | SctCredentialPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 47 | SctCredentialPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 48 | SctCredentialPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 49 | SctCredentialPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 50 | SctCredentialPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 51 | SctCredentialPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 52 | SctCredentialPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 53 | SctCredentialPEOCompletionPeriodId | COMPLETION_PERIOD_ID | — | ✅ |
| 54 | SctCredentialPEOConferralDate | CONFERRAL_DATE | — | ✅ |
| 55 | SctCredentialPEOCreatedBy | CREATED_BY | — | — |
| 56 | SctCredentialPEOCreationDate | CREATION_DATE | — | — |
| 57 | SctCredentialPEOCredentialId | CREDENTIAL_ID | — | — |
| 58 | SctCredentialPEOCredentialStatusCode | CREDENTIAL_STATUS_CODE | — | ✅ |
| 59 | SctCredentialPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 60 | SctCredentialPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 61 | SctCredentialPEOLastActionId | LAST_ACTION_ID | — | — |
| 62 | SctCredentialPEOLastActionType | LAST_ACTION_TYPE | — | — |
| 63 | SctCredentialPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 64 | SctCredentialPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 65 | SctCredentialPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 66 | SctCredentialPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 67 | SctCredentialPEORequestId | REQUEST_ID | — | — |
| 68 | SctCredentialPEOSctCredentialId | SCT_CREDENTIAL_ID | 🔑 | ✅ |
| 69 | SctCredentialPEOSctItemId | SCT_ITEM_ID | — | — |
| 70 | SctCredentialPEOShowStudentFlag | SHOW_STUDENT_FLAG | — | — |
| 71 | SctCredentialPEOStatusDate | STATUS_DATE | — | ✅ |

### [[her_sct_item|HER_SCT_ITEM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SctItemPEOAcademicLevelId | ACADEMIC_LEVEL_ID | — | — |
| 2 | SctItemPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | SctItemPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | SctItemPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | SctItemPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | SctItemPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | SctItemPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | SctItemPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | SctItemPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | SctItemPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | SctItemPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | SctItemPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | SctItemPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | SctItemPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | SctItemPEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | SctItemPEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | SctItemPEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | SctItemPEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | SctItemPEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | SctItemPEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | SctItemPEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | SctItemPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | SctItemPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | SctItemPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 25 | SctItemPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | SctItemPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | SctItemPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | SctItemPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | SctItemPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 30 | SctItemPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 31 | SctItemPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 32 | SctItemPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 33 | SctItemPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | SctItemPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | SctItemPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | SctItemPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | SctItemPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | SctItemPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | SctItemPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | SctItemPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | SctItemPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | SctItemPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | SctItemPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | SctItemPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 45 | SctItemPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 46 | SctItemPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 47 | SctItemPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 48 | SctItemPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 49 | SctItemPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 50 | SctItemPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 51 | SctItemPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 52 | SctItemPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 53 | SctItemPEOCampusId | CAMPUS_ID | — | — |
| 54 | SctItemPEOCreatedBy | CREATED_BY | — | — |
| 55 | SctItemPEOCreationDate | CREATION_DATE | — | — |
| 56 | SctItemPEOCurriculumId | CURRICULUM_ID | — | — |
| 57 | SctItemPEOCurriculumTypeId | CURRICULUM_TYPE_ID | — | — |
| 58 | SctItemPEOInstitutionId | INSTITUTION_ID | — | — |
| 59 | SctItemPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 60 | SctItemPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 61 | SctItemPEOLastActionId | LAST_ACTION_ID | — | — |
| 62 | SctItemPEOLastActionReasonId | LAST_ACTION_REASON_ID | — | — |
| 63 | SctItemPEOLastActionType | LAST_ACTION_TYPE | — | — |
| 64 | SctItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 65 | SctItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 66 | SctItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 67 | SctItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | SctItemPEORecordStatus | RECORD_STATUS | — | — |
| 69 | SctItemPEORequestId | REQUEST_ID | — | — |
| 70 | SctItemPEOSctItemId | SCT_ITEM_ID | — | — |
| 71 | SctItemPEOStudentPartyId | STUDENT_PARTY_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
