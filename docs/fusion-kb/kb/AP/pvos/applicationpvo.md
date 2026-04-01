---
id: DOC-AP-PVO-ApplicationPVO
doc_type: system-doc
title: "ApplicationPVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ApplicationPVO
  - applicationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ApplicationPVO

## 📌 Visão Geral

Extrai dados de candidaturas a programas de recrutamento e seleção, incluindo informações do candidato, programa vinculado e formulários associados. Suporta análise de funil de recrutamento, rastreamento de candidatos e métricas de eficiência dos processos seletivos.

**Caminho:** `FscmTopModelAM.HedHeqAdmissionApplicationAM.ApplicationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 367 | 4 | 1 | 17 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[heq_application|HEQ_APPLICATION]] — 85 atributos (1 PKs, 14 BICC)
- [[heq_appl_program|HEQ_APPL_PROGRAM]] — 77 atributos (1 BICC)
- [[hey_form_vl|HEY_FORM_VL]] — 64 atributos (2 BICC)
- [[hz_parties|HZ_PARTIES]] — 141 atributos

---

## ⚙️ Atributos

### [[heq_application|HEQ_APPLICATION]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationPEOAcademicLevelId | ACADEMIC_LEVEL_ID | — | — |
| 2 | ApplicationPEOAcademicLoadId | ACADEMIC_LOAD_ID | — | — |
| 3 | ApplicationPEOAdmitAcademicPeriodId | ADMIT_ACADEMIC_PERIOD_ID | — | — |
| 4 | ApplicationPEOAdmitEndDate | ADMIT_END_DATE | — | ✅ |
| 5 | ApplicationPEOAdmitStartDate | ADMIT_START_DATE | — | ✅ |
| 6 | ApplicationPEOAdmitStartTypeCode | ADMIT_START_TYPE_CODE | — | ✅ |
| 7 | ApplicationPEOAdmitTypeCode | ADMIT_TYPE_CODE | — | ✅ |
| 8 | ApplicationPEOApplicationCenterCode | APPLICATION_CENTER_CODE | — | — |
| 9 | ApplicationPEOApplicationDate | APPLICATION_DATE | — | ✅ |
| 10 | ApplicationPEOApplicationExtIdentifier | APPLICATION_EXT_IDENTIFIER | — | — |
| 11 | ApplicationPEOApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 12 | ApplicationPEOApplicationSourceCode | APPLICATION_SOURCE_CODE | — | — |
| 13 | ApplicationPEOAttribute1 | ATTRIBUTE1 | — | — |
| 14 | ApplicationPEOAttribute10 | ATTRIBUTE10 | — | — |
| 15 | ApplicationPEOAttribute11 | ATTRIBUTE11 | — | — |
| 16 | ApplicationPEOAttribute12 | ATTRIBUTE12 | — | — |
| 17 | ApplicationPEOAttribute13 | ATTRIBUTE13 | — | — |
| 18 | ApplicationPEOAttribute14 | ATTRIBUTE14 | — | — |
| 19 | ApplicationPEOAttribute15 | ATTRIBUTE15 | — | — |
| 20 | ApplicationPEOAttribute16 | ATTRIBUTE16 | — | — |
| 21 | ApplicationPEOAttribute17 | ATTRIBUTE17 | — | — |
| 22 | ApplicationPEOAttribute18 | ATTRIBUTE18 | — | — |
| 23 | ApplicationPEOAttribute19 | ATTRIBUTE19 | — | — |
| 24 | ApplicationPEOAttribute2 | ATTRIBUTE2 | — | — |
| 25 | ApplicationPEOAttribute20 | ATTRIBUTE20 | — | — |
| 26 | ApplicationPEOAttribute3 | ATTRIBUTE3 | — | — |
| 27 | ApplicationPEOAttribute4 | ATTRIBUTE4 | — | — |
| 28 | ApplicationPEOAttribute5 | ATTRIBUTE5 | — | — |
| 29 | ApplicationPEOAttribute6 | ATTRIBUTE6 | — | — |
| 30 | ApplicationPEOAttribute7 | ATTRIBUTE7 | — | — |
| 31 | ApplicationPEOAttribute8 | ATTRIBUTE8 | — | — |
| 32 | ApplicationPEOAttribute9 | ATTRIBUTE9 | — | — |
| 33 | ApplicationPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 34 | ApplicationPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 35 | ApplicationPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 36 | ApplicationPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 37 | ApplicationPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 38 | ApplicationPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 39 | ApplicationPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 40 | ApplicationPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 41 | ApplicationPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 42 | ApplicationPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 43 | ApplicationPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 44 | ApplicationPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 45 | ApplicationPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 46 | ApplicationPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 47 | ApplicationPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 48 | ApplicationPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 49 | ApplicationPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 50 | ApplicationPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 51 | ApplicationPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 52 | ApplicationPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 53 | ApplicationPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 54 | ApplicationPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 55 | ApplicationPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 56 | ApplicationPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 57 | ApplicationPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 58 | ApplicationPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 59 | ApplicationPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 60 | ApplicationPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 61 | ApplicationPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 62 | ApplicationPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 63 | ApplicationPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 64 | ApplicationPEOBaseApplicationId | BASE_APPLICATION_ID | — | — |
| 65 | ApplicationPEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 66 | ApplicationPEOCreatedBy | CREATED_BY | — | — |
| 67 | ApplicationPEOCreationDate | CREATION_DATE | — | ✅ |
| 68 | ApplicationPEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 69 | ApplicationPEOCurrencyCode | CURRENCY_CODE | — | — |
| 70 | ApplicationPEOEvaluationStatusCode | EVALUATION_STATUS_CODE | — | ✅ |
| 71 | ApplicationPEOEvaluatorComment | EVALUATOR_COMMENT | — | — |
| 72 | ApplicationPEOEvaluatorId | EVALUATOR_ID | — | — |
| 73 | ApplicationPEOInstitutionId | INSTITUTION_ID | — | — |
| 74 | ApplicationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 75 | ApplicationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 76 | ApplicationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 77 | ApplicationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 78 | ApplicationPEOPartyId | PARTY_ID | — | ✅ |
| 79 | ApplicationPEOPaymentStatusCode | PAYMENT_STATUS_CODE | — | — |
| 80 | ApplicationPEOPercentComplete | PERCENT_COMPLETE | — | ✅ |
| 81 | ApplicationPEOPreferredStartDate | PREFERRED_START_DATE | — | ✅ |
| 82 | ApplicationPEOReapplicationFlag | REAPPLICATION_FLAG | — | ✅ |
| 83 | ApplicationPEORowSequenceNumber | ROW_SEQUENCE_NUMBER | — | — |
| 84 | ApplicationPEORowTypeCode | ROW_TYPE_CODE | — | — |
| 85 | ApplicationPEOSourceInterestCode | SOURCE_INTEREST_CODE | — | — |

### [[heq_appl_program|HEQ_APPL_PROGRAM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationProgramPEOAcadGroupActionReasonId | ACAD_GROUP_ACTION_REASON_ID | — | — |
| 2 | ApplicationProgramPEOAcademicGroupActionCode | ACADEMIC_GROUP_ACTION_CODE | — | — |
| 3 | ApplicationProgramPEOAcademicGroupActionDate | ACADEMIC_GROUP_ACTION_DATE | — | — |
| 4 | ApplicationProgramPEOAcademicGroupItemId | ACADEMIC_GROUP_ITEM_ID | — | — |
| 5 | ApplicationProgramPEOAcademicGroupStatusCode | ACADEMIC_GROUP_STATUS_CODE | — | ✅ |
| 6 | ApplicationProgramPEOAcademicGroupStatusDate | ACADEMIC_GROUP_STATUS_DATE | — | — |
| 7 | ApplicationProgramPEOAcademicLevelId | ACADEMIC_LEVEL_ID | — | — |
| 8 | ApplicationProgramPEOAcademicProgramItemId | ACADEMIC_PROGRAM_ITEM_ID | — | — |
| 9 | ApplicationProgramPEOApplProgramId | APPL_PROGRAM_ID | — | — |
| 10 | ApplicationProgramPEOApplicationId | APPLICATION_ID | — | — |
| 11 | ApplicationProgramPEOAttribute1 | ATTRIBUTE1 | — | — |
| 12 | ApplicationProgramPEOAttribute10 | ATTRIBUTE10 | — | — |
| 13 | ApplicationProgramPEOAttribute11 | ATTRIBUTE11 | — | — |
| 14 | ApplicationProgramPEOAttribute12 | ATTRIBUTE12 | — | — |
| 15 | ApplicationProgramPEOAttribute13 | ATTRIBUTE13 | — | — |
| 16 | ApplicationProgramPEOAttribute14 | ATTRIBUTE14 | — | — |
| 17 | ApplicationProgramPEOAttribute15 | ATTRIBUTE15 | — | — |
| 18 | ApplicationProgramPEOAttribute16 | ATTRIBUTE16 | — | — |
| 19 | ApplicationProgramPEOAttribute17 | ATTRIBUTE17 | — | — |
| 20 | ApplicationProgramPEOAttribute18 | ATTRIBUTE18 | — | — |
| 21 | ApplicationProgramPEOAttribute19 | ATTRIBUTE19 | — | — |
| 22 | ApplicationProgramPEOAttribute2 | ATTRIBUTE2 | — | — |
| 23 | ApplicationProgramPEOAttribute20 | ATTRIBUTE20 | — | — |
| 24 | ApplicationProgramPEOAttribute3 | ATTRIBUTE3 | — | — |
| 25 | ApplicationProgramPEOAttribute4 | ATTRIBUTE4 | — | — |
| 26 | ApplicationProgramPEOAttribute5 | ATTRIBUTE5 | — | — |
| 27 | ApplicationProgramPEOAttribute6 | ATTRIBUTE6 | — | — |
| 28 | ApplicationProgramPEOAttribute7 | ATTRIBUTE7 | — | — |
| 29 | ApplicationProgramPEOAttribute8 | ATTRIBUTE8 | — | — |
| 30 | ApplicationProgramPEOAttribute9 | ATTRIBUTE9 | — | — |
| 31 | ApplicationProgramPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | ApplicationProgramPEOAttributeDate | ATTRIBUTE_DATE2 | — | — |
| 33 | ApplicationProgramPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 34 | ApplicationProgramPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 35 | ApplicationProgramPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 36 | ApplicationProgramPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 37 | ApplicationProgramPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 38 | ApplicationProgramPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 39 | ApplicationProgramPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 40 | ApplicationProgramPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 41 | ApplicationProgramPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 42 | ApplicationProgramPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 43 | ApplicationProgramPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 44 | ApplicationProgramPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 45 | ApplicationProgramPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 46 | ApplicationProgramPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 47 | ApplicationProgramPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 48 | ApplicationProgramPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 49 | ApplicationProgramPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 50 | ApplicationProgramPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 51 | ApplicationProgramPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 52 | ApplicationProgramPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 53 | ApplicationProgramPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 54 | ApplicationProgramPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 55 | ApplicationProgramPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 56 | ApplicationProgramPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 57 | ApplicationProgramPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 58 | ApplicationProgramPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 59 | ApplicationProgramPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 60 | ApplicationProgramPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 61 | ApplicationProgramPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 62 | ApplicationProgramPEOCampusId | CAMPUS_ID | — | — |
| 63 | ApplicationProgramPEOCreatedBy | CREATED_BY | — | — |
| 64 | ApplicationProgramPEOCreationDate | CREATION_DATE | — | — |
| 65 | ApplicationProgramPEOInstitutionId | INSTITUTION_ID | — | — |
| 66 | ApplicationProgramPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 67 | ApplicationProgramPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 68 | ApplicationProgramPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 69 | ApplicationProgramPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 70 | ApplicationProgramPEOPreferredStartDate | PREFERRED_START_DATE | — | — |
| 71 | ApplicationProgramPEOPrimaryProgramFlag | PRIMARY_PROGRAM_FLAG | — | — |
| 72 | ApplicationProgramPEOProgramActionCode | PROGRAM_ACTION_CODE | — | — |
| 73 | ApplicationProgramPEOProgramActionDate | PROGRAM_ACTION_DATE | — | — |
| 74 | ApplicationProgramPEOProgramActionReasonId | PROGRAM_ACTION_REASON_ID | — | — |
| 75 | ApplicationProgramPEOProgramSequence | PROGRAM_SEQUENCE | — | — |
| 76 | ApplicationProgramPEOProgramStatusCode | PROGRAM_STATUS_CODE | — | — |
| 77 | ApplicationProgramPEOProgramStatusDate | PROGRAM_STATUS_DATE | — | — |

### [[hey_form_vl|HEY_FORM_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FormPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | FormPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | FormPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | FormPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | FormPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | FormPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | FormPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | FormPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | FormPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | FormPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | FormPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | FormPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | FormPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | FormPEOAttribute3 | ATTRIBUTE3 | — | — |
| 15 | FormPEOAttribute4 | ATTRIBUTE4 | — | — |
| 16 | FormPEOAttribute5 | ATTRIBUTE5 | — | — |
| 17 | FormPEOAttribute6 | ATTRIBUTE6 | — | — |
| 18 | FormPEOAttribute7 | ATTRIBUTE7 | — | — |
| 19 | FormPEOAttribute8 | ATTRIBUTE8 | — | — |
| 20 | FormPEOAttribute9 | ATTRIBUTE9 | — | — |
| 21 | FormPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | FormPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | FormPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | FormPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | FormPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | FormPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | FormPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | FormPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | FormPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | FormPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | FormPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | FormPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | FormPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | FormPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | FormPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | FormPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | FormPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | FormPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | FormPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | FormPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | FormPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | FormPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | FormPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | FormPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | FormPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | FormPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | FormPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | FormPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | FormPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | FormPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | FormPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | FormPEOClonedFormId | CLONED_FORM_ID | — | — |
| 53 | FormPEOCreatedBy | CREATED_BY | — | — |
| 54 | FormPEOCreationDate | CREATION_DATE | — | — |
| 55 | FormPEODisplayName | DISPLAY_NAME | — | ✅ |
| 56 | FormPEOFormCode | FORM_CODE | — | — |
| 57 | FormPEOFormId | FORM_ID | — | — |
| 58 | FormPEOFormTypeCode | FORM_TYPE_CODE | — | — |
| 59 | FormPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 60 | FormPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 61 | FormPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 62 | FormPEOName | NAME | — | ✅ |
| 63 | FormPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 64 | FormPEOStatusCode | STATUS_CODE | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPEOAddress1 | ADDRESS1 | — | — |
| 2 | PartyPEOAddress2 | ADDRESS2 | — | — |
| 3 | PartyPEOAddress3 | ADDRESS3 | — | — |
| 4 | PartyPEOAddress4 | ADDRESS4 | — | — |
| 5 | PartyPEOAnalysisFy | ANALYSIS_FY | — | — |
| 6 | PartyPEOAttribute1 | ATTRIBUTE1 | — | — |
| 7 | PartyPEOAttribute10 | ATTRIBUTE10 | — | — |
| 8 | PartyPEOAttribute11 | ATTRIBUTE11 | — | — |
| 9 | PartyPEOAttribute12 | ATTRIBUTE12 | — | — |
| 10 | PartyPEOAttribute13 | ATTRIBUTE13 | — | — |
| 11 | PartyPEOAttribute14 | ATTRIBUTE14 | — | — |
| 12 | PartyPEOAttribute15 | ATTRIBUTE15 | — | — |
| 13 | PartyPEOAttribute16 | ATTRIBUTE16 | — | — |
| 14 | PartyPEOAttribute17 | ATTRIBUTE17 | — | — |
| 15 | PartyPEOAttribute18 | ATTRIBUTE18 | — | — |
| 16 | PartyPEOAttribute19 | ATTRIBUTE19 | — | — |
| 17 | PartyPEOAttribute2 | ATTRIBUTE2 | — | — |
| 18 | PartyPEOAttribute20 | ATTRIBUTE20 | — | — |
| 19 | PartyPEOAttribute21 | ATTRIBUTE21 | — | — |
| 20 | PartyPEOAttribute22 | ATTRIBUTE22 | — | — |
| 21 | PartyPEOAttribute23 | ATTRIBUTE23 | — | — |
| 22 | PartyPEOAttribute24 | ATTRIBUTE24 | — | — |
| 23 | PartyPEOAttribute25 | ATTRIBUTE25 | — | — |
| 24 | PartyPEOAttribute26 | ATTRIBUTE26 | — | — |
| 25 | PartyPEOAttribute27 | ATTRIBUTE27 | — | — |
| 26 | PartyPEOAttribute28 | ATTRIBUTE28 | — | — |
| 27 | PartyPEOAttribute29 | ATTRIBUTE29 | — | — |
| 28 | PartyPEOAttribute3 | ATTRIBUTE3 | — | — |
| 29 | PartyPEOAttribute30 | ATTRIBUTE30 | — | — |
| 30 | PartyPEOAttribute4 | ATTRIBUTE4 | — | — |
| 31 | PartyPEOAttribute5 | ATTRIBUTE5 | — | — |
| 32 | PartyPEOAttribute6 | ATTRIBUTE6 | — | — |
| 33 | PartyPEOAttribute7 | ATTRIBUTE7 | — | — |
| 34 | PartyPEOAttribute8 | ATTRIBUTE8 | — | — |
| 35 | PartyPEOAttribute9 | ATTRIBUTE9 | — | — |
| 36 | PartyPEOAttributeCategory3 | ATTRIBUTE_CATEGORY | — | — |
| 37 | PartyPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 38 | PartyPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 39 | PartyPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 40 | PartyPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 41 | PartyPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 42 | PartyPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 43 | PartyPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 44 | PartyPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 45 | PartyPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 46 | PartyPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 47 | PartyPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 48 | PartyPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 49 | PartyPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 50 | PartyPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 51 | PartyPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 52 | PartyPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 53 | PartyPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 54 | PartyPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 55 | PartyPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 56 | PartyPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 57 | PartyPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 58 | PartyPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 59 | PartyPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 60 | PartyPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 61 | PartyPEOCategoryCode | CATEGORY_CODE | — | — |
| 62 | PartyPEOCeoName | CEO_NAME | — | — |
| 63 | PartyPEOCertReasonCode | CERT_REASON_CODE | — | — |
| 64 | PartyPEOCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 65 | PartyPEOCity | CITY | — | — |
| 66 | PartyPEOComments | COMMENTS | — | — |
| 67 | PartyPEOCountry | COUNTRY | — | — |
| 68 | PartyPEOCounty | COUNTY | — | — |
| 69 | PartyPEOCreatedBy | CREATED_BY | — | — |
| 70 | PartyPEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 71 | PartyPEOCreationDate | CREATION_DATE | — | — |
| 72 | PartyPEOCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 73 | PartyPEODateOfBirth | DATE_OF_BIRTH | — | — |
| 74 | PartyPEODunsNumberC | DUNS_NUMBER_C | — | — |
| 75 | PartyPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 76 | PartyPEOEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 77 | PartyPEOFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 78 | PartyPEOGender | GENDER | — | — |
| 79 | PartyPEOGroupType | GROUP_TYPE | — | — |
| 80 | PartyPEOGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 81 | PartyPEOHomeCountry | HOME_COUNTRY | — | — |
| 82 | PartyPEOHqBranchInd | HQ_BRANCH_IND | — | — |
| 83 | PartyPEOIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 84 | PartyPEOIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 85 | PartyPEOInternalFlag | INTERNAL_FLAG | — | — |
| 86 | PartyPEOJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 87 | PartyPEOLanguageName | LANGUAGE_NAME | — | — |
| 88 | PartyPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 89 | PartyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 90 | PartyPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 91 | PartyPEOMaritalStatus | MARITAL_STATUS | — | — |
| 92 | PartyPEOMissionStatement | MISSION_STATEMENT | — | — |
| 93 | PartyPEONextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 94 | PartyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 95 | PartyPEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 96 | PartyPEOPartyId | PARTY_ID | — | — |
| 97 | PartyPEOPartyName | PARTY_NAME | — | — |
| 98 | PartyPEOPartyNumber | PARTY_NUMBER | — | — |
| 99 | PartyPEOPartyType | PARTY_TYPE | — | — |
| 100 | PartyPEOPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 101 | PartyPEOPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 102 | PartyPEOPersonFirstName | PERSON_FIRST_NAME | — | — |
| 103 | PartyPEOPersonLastName | PERSON_LAST_NAME | — | — |
| 104 | PartyPEOPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 105 | PartyPEOPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 106 | PartyPEOPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 107 | PartyPEOPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 108 | PartyPEOPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 109 | PartyPEOPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 110 | PartyPEOPersonTitle | PERSON_TITLE | — | — |
| 111 | PartyPEOPersonalAddressFlag | PERSONAL_ADDRESS_FLAG | — | — |
| 112 | PartyPEOPersonalEmailFlag | PERSONAL_EMAIL_FLAG | — | — |
| 113 | PartyPEOPersonalPhoneFlag | PERSONAL_PHONE_FLAG | — | — |
| 114 | PartyPEOPostalCode | POSTAL_CODE | — | — |
| 115 | PartyPEOPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 116 | PartyPEOPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 117 | PartyPEOPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 118 | PartyPEOPreferredName | PREFERRED_NAME | — | — |
| 119 | PartyPEOPreferredNameId | PREFERRED_NAME_ID | — | — |
| 120 | PartyPEOPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 121 | PartyPEOPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 122 | PartyPEOPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 123 | PartyPEOPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 124 | PartyPEOPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 125 | PartyPEOPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 126 | PartyPEOPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 127 | PartyPEOPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 128 | PartyPEOPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 129 | PartyPEOProvince | PROVINCE | — | — |
| 130 | PartyPEORequestId | REQUEST_ID | — | — |
| 131 | PartyPEOSalutation | SALUTATION | — | — |
| 132 | PartyPEOSicCode | SIC_CODE | — | — |
| 133 | PartyPEOSicCodeType | SIC_CODE_TYPE | — | — |
| 134 | PartyPEOState | STATE | — | — |
| 135 | PartyPEOStatus | STATUS | — | — |
| 136 | PartyPEOThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 137 | PartyPEOTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 138 | PartyPEOUrl | URL | — | — |
| 139 | PartyPEOUserGuid | USER_GUID | — | — |
| 140 | PartyPEOValidatedFlag | VALIDATED_FLAG | — | — |
| 141 | PartyPEOYearEstablished | YEAR_ESTABLISHED | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
