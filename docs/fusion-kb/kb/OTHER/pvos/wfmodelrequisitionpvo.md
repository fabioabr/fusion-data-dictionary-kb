---
id: DOC-OTHER-PVO-WfModelRequisitionPVO
doc_type: system-doc
title: "WfModelRequisitionPVO — PVO Cross-Module"
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
  - WfModelRequisitionPVO
  - wfmodelrequisitionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WfModelRequisitionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Wf Model Requisition. Acessa as tabelas: IRC_PHASES_B, IRC_PHASES_TL, IRC_STATES_B (+4).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.WorkforceModelingAM.WfModelRequisitionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 49 | 7 | 1 | 13 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[irc_phases_b|IRC_PHASES_B]] — 3 atributos
- [[irc_phases_tl|IRC_PHASES_TL]] — 3 atributos
- [[irc_states_b|IRC_STATES_B]] — 3 atributos
- [[irc_states_tl|IRC_STATES_TL]] — 3 atributos
- [[irc_wfmodel_requisitions|IRC_WFMODEL_REQUISITIONS]] — 25 atributos (1 PKs, 7 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos (4 BICC)

---

## ⚙️ Atributos

### [[irc_phases_b|IRC_PHASES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhaseBPEOCode | CODE | — | — |
| 2 | PhaseBPEOPhaseId | PHASE_ID | — | — |
| 3 | PhaseBPEOTypeCode | TYPE_CODE | — | — |

### [[irc_phases_tl|IRC_PHASES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhaseTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | PhaseTranslationPEOName | NAME | — | — |
| 3 | PhaseTranslationPEOPhaseId | PHASE_ID | — | — |

### [[irc_states_b|IRC_STATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StateBPEOCode | CODE | — | — |
| 2 | StateBPEOStateId | STATE_ID | — | — |
| 3 | StateBPEOTypeCode | TYPE_CODE | — | — |

### [[irc_states_tl|IRC_STATES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StateTranslationLanguage | LANGUAGE | — | — |
| 2 | StateTranslationPEOName | NAME | — | — |
| 3 | StateTranslationStateId | STATE_ID | — | — |

### [[irc_wfmodel_requisitions|IRC_WFMODEL_REQUISITIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Comments | COMMENTS | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | GeographyNodeId | GEOGRAPHY_NODE_ID | — | — |
| 5 | HiringManagerId | HIRING_MANAGER_ID | — | — |
| 6 | JustificationCode | JUSTIFICATION_CODE | — | — |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | — |
| 11 | ManagerTitle | MANAGER_TITLE | — | ✅ |
| 12 | NumberToHire | NUMBER_TO_HIRE | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | PhaseId | PHASE_ID | — | — |
| 15 | RecruiterAssignmentId | RECRUITER_ASSIGNMENT_ID | — | — |
| 16 | RecruiterId | RECRUITER_ID | — | — |
| 17 | RecruitingTypeCode | RECRUITING_TYPE_CODE | — | — |
| 18 | RequisitionLanguage | REQUISITION_LANGUAGE | — | — |
| 19 | RequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 20 | SourceRequisitionId | SOURCE_REQUISITION_ID | — | — |
| 21 | StateId | STATE_ID | — | — |
| 22 | Title | TITLE | — | ✅ |
| 23 | UnlimitedHireFlag | UNLIMITED_HIRE_FLAG | — | ✅ |
| 24 | WfModelId | WF_MODEL_ID | — | — |
| 25 | WfModelRequisitionId | WF_MODEL_REQUISITION_ID | 🔑 | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HMPersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | HMPersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | HMPersonDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | HMPersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HMPersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | HMPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | HMPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | HMPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 5 | RecruiterPersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 6 | RecruiterPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | RecruiterPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | RecruiterPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
