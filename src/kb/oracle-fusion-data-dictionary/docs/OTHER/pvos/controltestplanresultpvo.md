---
id: DOC-OTHER-PVO-ControlTestPlanResultPVO
doc_type: system-doc
title: "ControlTestPlanResultPVO — PVO Cross-Module"
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
  - ControlTestPlanResultPVO
  - controltestplanresultpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ControlTestPlanResultPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Control Test Plan Result. Acessa as tabelas: GRC_ACTV_ACTIVITY_TL, GRC_ACTV_RESPONSE_VL, GRC_ASMT_CTRLRSLT (+7).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.ControlTestPlanResultPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 105 | 10 | 6 | 26 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[grc_actv_activity_tl|GRC_ACTV_ACTIVITY_TL]] — 11 atributos (2 BICC)
- [[grc_actv_response_vl|GRC_ACTV_RESPONSE_VL]] — 17 atributos (2 BICC)
- [[grc_asmt_ctrlrslt|GRC_ASMT_CTRLRSLT]] — 4 atributos (3 BICC)
- [[grc_ctrl_testplan_b|GRC_CTRL_TESTPLAN_B]] — 14 atributos (5 BICC)
- [[grc_ctrl_testplan_result_v|GRC_CTRL_TESTPLAN_RESULT_V]] — 8 atributos (6 PKs, 8 BICC)
- [[grc_ctrl_testplan_tl|GRC_CTRL_TESTPLAN_TL]] — 11 atributos (2 BICC)
- [[gtg_asmt_tstplan_rslt|GTG_ASMT_TSTPLAN_RSLT]] — 15 atributos (1 BICC)
- [[gtg_ctrl_step_b|GTG_CTRL_STEP_B]] — 13 atributos (2 BICC)
- [[gtg_ctrl_step_tl|GTG_CTRL_STEP_TL]] — 9 atributos (1 BICC)
- [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]] — 3 atributos

---

## ⚙️ Atributos

### [[grc_actv_activity_tl|GRC_ACTV_ACTIVITY_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityPEOActivityCode | ACTIVITY_CODE | — | — |
| 2 | ActivityPEOBindKey | BIND_KEY | — | — |
| 3 | ActivityPEOCreatedBy | CREATED_BY | — | — |
| 4 | ActivityPEOCreationDate | CREATION_DATE | — | — |
| 5 | ActivityPEODescription | DESCRIPTION | — | — |
| 6 | ActivityPEOLanguage | LANGUAGE | — | — |
| 7 | ActivityPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ActivityPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ActivityPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ActivityPEOName | NAME | — | ✅ |
| 11 | ActivityPEOSourceLang | SOURCE_LANG | — | — |

### [[grc_actv_response_vl|GRC_ACTV_RESPONSE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityResponsePEOBindKey | BIND_KEY | — | — |
| 2 | ActivityResponsePEOCreatedBy | CREATED_BY | — | — |
| 3 | ActivityResponsePEOCreationDate | CREATION_DATE | — | — |
| 4 | ActivityResponsePEODescription | DESCRIPTION | — | — |
| 5 | ActivityResponsePEOIconFileName | ICON_FILE_NAME | — | — |
| 6 | ActivityResponsePEOIsActive | IS_ACTIVE | — | — |
| 7 | ActivityResponsePEOIsSeeded | IS_SEEDED | — | — |
| 8 | ActivityResponsePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ActivityResponsePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ActivityResponsePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ActivityResponsePEOName | NAME | — | ✅ |
| 12 | ActivityResponsePEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 13 | ActivityResponsePEOResponseCode | RESPONSE_CODE | — | — |
| 14 | ActivityResponsePEORowID | ROWID | — | — |
| 15 | ActivityResponsePEORowId1 | ROW_ID | — | — |
| 16 | ActivityResponsePEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 17 | ActivityResponsePEOSuccessGrade | SUCCESS_GRADE | — | — |

### [[grc_asmt_ctrlrslt|GRC_ASMT_CTRLRSLT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentCtrlRsltPEOAsmtId | ASSESSMENT_ID | — | ✅ |
| 2 | AssessmentCtrlRsltPEOControlId | CONTROL_ID | — | ✅ |
| 3 | AssessmentCtrlRsltPEOResultId | RESULT_ID | — | ✅ |
| 4 | AssessmentCtrlRsltPEOStateCode | STATE_CODE | — | — |

### [[grc_ctrl_testplan_b|GRC_CTRL_TESTPLAN_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlTestPlanPEOControlId | CONTROL_ID | — | — |
| 2 | ControlTestPlanPEOCreatedBy | CREATED_BY | — | — |
| 3 | ControlTestPlanPEOCreationDate | CREATION_DATE | — | — |
| 4 | ControlTestPlanPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | ControlTestPlanPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ControlTestPlanPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ControlTestPlanPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ControlTestPlanPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ControlTestPlanPEORevisionDate | REVISION_DATE | — | ✅ |
| 10 | ControlTestPlanPEOSampleSize | SAMPLE_SIZE | — | ✅ |
| 11 | ControlTestPlanPEOStartDate | START_DATE | — | — |
| 12 | ControlTestPlanPEOTestPlanFrequency | TEST_PLAN_FREQUENCY | — | ✅ |
| 13 | ControlTestPlanPEOTestPlanId | TEST_PLAN_ID | — | — |
| 14 | ControlTestPlanPEOTestPlanType | TEST_PLAN_TYPE | — | ✅ |

### [[grc_ctrl_testplan_result_v|GRC_CTRL_TESTPLAN_RESULT_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlTestPlanResultPEOActivityCode | ACTIVITY_CODE | 🔑 | ✅ |
| 2 | ControlTestPlanResultPEOAssessmentId | ASSESSMENT_ID | 🔑 | ✅ |
| 3 | ControlTestPlanResultPEOControlId | CONTROL_ID | 🔑 | ✅ |
| 4 | ControlTestPlanResultPEOTestInstructionId | TEST_INSTRUCTION_ID | 🔑 | ✅ |
| 5 | ControlTestPlanResultPEOTestPlanId | TEST_PLAN_ID | 🔑 | ✅ |
| 6 | ControlTestPlanResultPEOTestStepId | TEST_STEP_ID | 🔑 | ✅ |
| 7 | ControlTestPlanResultPEOTestStepResult | TEST_STEP_RESULT | — | ✅ |
| 8 | ControlTestPlanResultPEOTestStepRsltSum | TEST_STEP_RESULT_SUMMARY | — | ✅ |

### [[grc_ctrl_testplan_tl|GRC_CTRL_TESTPLAN_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlTestPlanTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ControlTestPlanTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ControlTestPlanTranslationPEODescription | DESCRIPTION | — | — |
| 4 | ControlTestPlanTranslationPEODetailedDescr | DETAILED_DESCRIPTION | — | ✅ |
| 5 | ControlTestPlanTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | ControlTestPlanTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | ControlTestPlanTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ControlTestPlanTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ControlTestPlanTranslationPEOName | NAME | — | ✅ |
| 10 | ControlTestPlanTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 11 | ControlTestPlanTranslationPEOTestPlanId | TEST_PLAN_ID | — | — |

### [[gtg_asmt_tstplan_rslt|GTG_ASMT_TSTPLAN_RSLT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AsmtTestPlanResultPEOActvCd | ACTIVITY_CODE | — | — |
| 2 | AsmtTestPlanResultPEOAsmntId | ASSESSMENT_ID | — | — |
| 3 | AsmtTestPlanResultPEOClctdSmpls | COLLECTED_SAMPLES | — | ✅ |
| 4 | AsmtTestPlanResultPEOControlId | CONTROL_ID | — | — |
| 5 | AsmtTestPlanResultPEOCreatedBy | CREATED_BY | — | — |
| 6 | AsmtTestPlanResultPEOCrtnDt | CREATION_DATE | — | — |
| 7 | AsmtTestPlanResultPEOCtrlRsltId | CONTROL_RESULT_ID | — | — |
| 8 | AsmtTestPlanResultPEOLstUpdtDt | LAST_UPDATE_DATE | — | — |
| 9 | AsmtTestPlanResultPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 10 | AsmtTestPlanResultPEOLstUpdtdBy | LAST_UPDATED_BY | — | — |
| 11 | AsmtTestPlanResultPEOPlnEffSeq | PLAN_EFFECTIVE_SEQUENCE | — | — |
| 12 | AsmtTestPlanResultPEORsltSum | RESULT_SUMMARY | — | — |
| 13 | AsmtTestPlanResultPEORspnseCd | RESPONSE_CODE | — | — |
| 14 | AsmtTestPlanResultPEOTstPlaRsltId | TEST_PLAN_RESULT_ID | — | — |
| 15 | AsmtTestPlanResultPEOTstPlnId | TEST_PLAN_ID | — | — |

### [[gtg_ctrl_step_b|GTG_CTRL_STEP_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlStepPEOAttrCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | ControlStepPEOCreatedBy | CREATED_BY | — | — |
| 3 | ControlStepPEOCreationDate | CREATION_DATE | — | — |
| 4 | ControlStepPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | ControlStepPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ControlStepPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ControlStepPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ControlStepPEOObjVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ControlStepPEORevisionDate | REVISION_DATE | — | — |
| 10 | ControlStepPEOStartDate | START_DATE | — | — |
| 11 | ControlStepPEOStepId | STEP_ID | — | — |
| 12 | ControlStepPEOStepOrder | STEP_ORDER | — | ✅ |
| 13 | ControlStepPEOTestPlanId | TEST_PLAN_ID | — | — |

### [[gtg_ctrl_step_tl|GTG_CTRL_STEP_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlTestStepTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ControlTestStepTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ControlTestStepTranslationPEODetailedDescr | DETAILED_DESCRIPTION | — | — |
| 4 | ControlTestStepTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | ControlTestStepTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ControlTestStepTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ControlTestStepTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ControlTestStepTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 9 | ControlTestStepTranslationPEOTestStepId | STEP_ID | — | — |

### [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FRCSecurityPEOSecurableId | SECURABLE_ID | — | — |
| 2 | FRCSecurityPEOSecurableType | SECURABLE_TYPE | — | — |
| 3 | FRCSecurityPEOUserId | USER_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
