---
id: DOC-HCM-PVO-WorkRelationshipPVO
doc_type: system-doc
title: "WorkRelationshipPVO — PVO Human Capital Management"
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
  - WorkRelationshipPVO
  - workrelationshippvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkRelationshipPVO

## 📌 Visão Geral

Extrai relações de trabalho (períodos de serviço) com datas de admissão e desligamento. Fundamental para análise de turnover e gestão do ciclo de vida do colaborador.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AssignmentAM.WorkRelationshipPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 1 | 1 | 31 | 91% |

---

## 🔗 Tabelas Relacionadas

- [[per_periods_of_service|PER_PERIODS_OF_SERVICE]] — 34 atributos (1 PKs, 31 BICC)

---

## ⚙️ Atributos

### [[per_periods_of_service|PER_PERIODS_OF_SERVICE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PeriodOfServiceId | PERIOD_OF_SERVICE_ID | 🔑 | ✅ |
| 2 | WorkRelationshipPEOAcceptedTerminationDate | ACCEPTED_TERMINATION_DATE | — | ✅ |
| 3 | WorkRelationshipPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 4 | WorkRelationshipPEOActualTerminationDate | ACTUAL_TERMINATION_DATE | — | ✅ |
| 5 | WorkRelationshipPEOAdjustedSvcDate | ADJUSTED_SVC_DATE | — | ✅ |
| 6 | WorkRelationshipPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 7 | WorkRelationshipPEOComments | COMMENTS | — | ✅ |
| 8 | WorkRelationshipPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | WorkRelationshipPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | WorkRelationshipPEODateEmployeeDataVerified | DATE_EMPLOYEE_DATA_VERIFIED | — | ✅ |
| 11 | WorkRelationshipPEODateStart | DATE_START | — | ✅ |
| 12 | WorkRelationshipPEOFastPathEmployee | FAST_PATH_EMPLOYEE | — | ✅ |
| 13 | WorkRelationshipPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | WorkRelationshipPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | WorkRelationshipPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | WorkRelationshipPEOLastWorkingDate | LAST_WORKING_DATE | — | ✅ |
| 17 | WorkRelationshipPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 18 | WorkRelationshipPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 19 | WorkRelationshipPEONotifiedTerminationDate | NOTIFIED_TERMINATION_DATE | — | ✅ |
| 20 | WorkRelationshipPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | WorkRelationshipPEOOnMilitaryService | ON_MILITARY_SERVICE | — | ✅ |
| 22 | WorkRelationshipPEOOriginalDateOfHire | ORIGINAL_DATE_OF_HIRE | — | ✅ |
| 23 | WorkRelationshipPEOPeriodType | PERIOD_TYPE | — | ✅ |
| 24 | WorkRelationshipPEOPersonId | PERSON_ID | — | ✅ |
| 25 | WorkRelationshipPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 26 | WorkRelationshipPEOProjectedTerminationDate | PROJECTED_TERMINATION_DATE | — | ✅ |
| 27 | WorkRelationshipPEORehireAuthorizerPersonId | REHIRE_AUTHORIZER_PERSON_ID | — | — |
| 28 | WorkRelationshipPEORehireAuthorizor | REHIRE_AUTHORIZOR | — | ✅ |
| 29 | WorkRelationshipPEORehireReason | REHIRE_REASON | — | ✅ |
| 30 | WorkRelationshipPEORehireRecommendation | REHIRE_RECOMMENDATION | — | ✅ |
| 31 | WorkRelationshipPEORevokeUserAccess | REVOKE_USER_ACCESS | — | ✅ |
| 32 | WorkRelationshipPEOTerminationAcceptedPersonId | TERMINATION_ACCEPTED_PERSON_ID | — | — |
| 33 | WorkRelationshipPEOWorkerComments | WORKER_COMMENTS | — | ✅ |
| 34 | WorkRelationshipPEOWorkerNumber | WORKER_NUMBER | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
