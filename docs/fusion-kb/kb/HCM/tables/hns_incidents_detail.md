---
id: DOC-HCM-102
doc_type: system-doc
title: "HNS_INCIDENTS_DETAIL — Detalhes de Incidentes de Segurança"
system: Oracle Fusion Cloud HCM
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
  - health-safety
  - incidentes
  - seguranca
  - hns
aliases:
  - HNS_INCIDENTS_DETAIL
  - hns_incidents_detail
  - hns-incidents-detail
  - DOC-HCM-102
  - detalhes-de-incidentes-de-segurança
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_INCIDENTS_DETAIL

## 📌 Visão Geral

Armazena os **detalhes completos de incidentes** de saúde e segurança. Cada registro contém informações sobre o tipo de incidente, local, data/hora, descrição detalhada e classificação de severidade.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de incidentes:** Documentação completa de eventos de segurança.
- **Classificação de severidade:** Categorização por gravidade do incidente.
- **Investigação:** Base para processos de investigação de causas.
- **Compliance:** Documentação para atender requisitos regulatórios.
- **Estatísticas:** Dados para indicadores de segurança (taxa de frequência, gravidade).

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INCIDENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do incidente | — | 🟢 95% |
| 2 | INCIDENT_NUMBER | VARCHAR2(30) | NULL | Identificação | Número do incidente | — | 🟢 90% |
| 3 | INCIDENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do incidente | — | 🟡 80% |
| 4 | INCIDENT_DATE | DATE | NOT NULL | Data | Data do incidente | — | 🟢 95% |
| 5 | INCIDENT_TIME | VARCHAR2(10) | NULL | Data | Hora do incidente | — | 🟡 80% |
| 6 | LOCATION_ID | NUMBER(18) | NULL | FK | Local do incidente | [[hr_locations_all]] | 🟡 80% |
| 7 | SEVERITY | VARCHAR2(30) | NULL | Classificação | Severidade (MINOR, MAJOR, CRITICAL, FATAL) | — | 🟡 80% |
| 8 | DESCRIPTION | VARCHAR2(4000) | NULL | Texto | Descrição detalhada | — | 🟢 90% |
| 9 | STATUS | VARCHAR2(30) | NULL | Status | Status do incidente (REPORTED, INVESTIGATING, CLOSED) | — | 🟡 80% |
| 10 | REPORTED_BY_PERSON_ID | NUMBER(18) | NULL | FK | Pessoa que reportou | [[per_all_people_f]] | 🟡 80% |
| 11 | REPORTED_DATE | DATE | NULL | Data | Data do reporte | — | 🟡 80% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_locations_all]] — via `LOCATION_ID` (local de ocorrencia do incidente)
- [[per_all_people_f]] — via `REPORTED_BY_PERSON_ID` (pessoa que reportou o incidente)

### Tabelas-filha (FK de saída)
- [[hns_injured_persons]] — via `INCIDENT_ID` (pessoas lesionadas)
- [[hns_actions]] — via `INCIDENT_ID` (acoes corretivas do incidente)
- [[hns_investigations_summary]] — via `INCIDENT_ID` (investigacoes do incidente)
- [[hns_notes]] — via `INCIDENT_ID` (notas e observacoes do incidente)

---

## 📎 Uso Típico

### Incidentes por período
```sql
SELECT d.INCIDENT_NUMBER, d.INCIDENT_TYPE, d.INCIDENT_DATE,
       d.SEVERITY, d.STATUS
FROM   HNS_INCIDENTS_DETAIL d
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

### Incidentes críticos abertos
```sql
SELECT d.INCIDENT_NUMBER, d.DESCRIPTION, d.INCIDENT_DATE
FROM   HNS_INCIDENTS_DETAIL d
WHERE  d.SEVERITY IN ('CRITICAL', 'FATAL')
  AND  d.STATUS != 'CLOSED';
```

---

## 🔒 Observações

- Tabela central de incidentes — todas as outras tabelas HNS referenciam esta.
- A `SEVERITY` classifica: MINOR, MAJOR, CRITICAL, FATAL.
- O `STATUS` controla o fluxo: REPORTED -> INVESTIGATING -> CLOSED.
- Integra-se com tabelas de eventos específicos (fogo, veicular, ergonômico, etc.).

---

## 🔗 PVOs Relacionados

### [[hnsincidenteventpvo|HNSIncidentEventPVO]] (HCM · BICC: 27/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REQUIRED_FLAG | HNSIncidentEventDetailsPEOActionRqrdFlag | ✅ |
| ACTUAL_COMPLETION_DATE | HNSIncidentEventDetailsPEOActualCompletionDate | ✅ |
| COMPLETED_FLAG | HNSIncidentEventDetailsPEOCompletedFlag | ✅ |
| CREATED_BY | HNSIncidentEventDetailsPEOCreatedBy | ✅ |
| CREATION_DATE | HNSIncidentEventDetailsPEOCreationDate | ✅ |
| DATE_DISCLOSED | HNSIncidentEventDetailsPEODateDisclsd | ✅ |
| DELETED_FLAG | HNSIncidentEventDetailsPEODeletedFlag | ✅ |
| EMPLOYEE_ASSIGN_ID | HNSIncidentEventDetailsPEOEmpAsnId | — |
| EMPLOYEE_ID | HNSIncidentEventDetailsPEOEmployeeId | ✅ |
| EVENT_CREATION_DATE | HNSIncidentEventDetailsPEOEvntCreationDt | ✅ |
| INC_EVENT_OWNER_ASSIGN_ID | HNSIncidentEventDetailsPEOIncEvOwnAsnId | — |
| INCI_DETAIL_DESCR | HNSIncidentEventDetailsPEOInciDetailDescr | ✅ |
| INCI_EVENT_STATUS_CODE | HNSIncidentEventDetailsPEOInciEventStatusCode | ✅ |
| INCIDENT_DETAIL_ID | HNSIncidentEventDetailsPEOIncidentDetailId | ✅ |
| INCIDENT_EVENT_CODE | HNSIncidentEventDetailsPEOIncidentEventCode | ✅ |
| INCIDENT_EVENT_DATE | HNSIncidentEventDetailsPEOIncidentEventDate | ✅ |
| INCIDENT_EVENT_NO | HNSIncidentEventDetailsPEOIncidentEventNo | ✅ |
| INCIDENT_EVENT_OWNER_ID | HNSIncidentEventDetailsPEOIncidentEventOwnerId | ✅ |
| INCIDENT_EVENT_SUMMARY | HNSIncidentEventDetailsPEOIncidentEventSummary | ✅ |
| INCIDENT_ID | HNSIncidentEventDetailsPEOIncidentId | ✅ |
| LAST_UPDATE_DATE | HNSIncidentEventDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HNSIncidentEventDetailsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | HNSIncidentEventDetailsPEOLastUpdatedBy | ✅ |
| LESSONS_LEARNED | HNSIncidentEventDetailsPEOLessonsLearned | ✅ |
| OBJECT_VERSION_NUMBER | HNSIncidentEventDetailsPEOObjectVersionNumber | ✅ |
| RESULT_CODE | HNSIncidentEventDetailsPEOResultCode | ✅ |
| SEVERITY_LEVEL_CODE | HNSIncidentEventDetailsPEOSeverityLevelCode | ✅ |
| TARGET_COMPLETION_DATE | HNSIncidentEventDetailsPEOTargetCompletionDate | ✅ |
| THIRD_PARTY_DETAILS | HNSIncidentEventDetailsPEOThirdPartyDetails | ✅ |

### [[hnsinjuredpersonspvo|HNSInjuredPersonsPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INCIDENT_DETAIL_ID | HNSIncidentEventDetailsPEOIncidentDetailId | — |
| INCIDENT_EVENT_DATE | DerivedEventDate | — |

### [[hnsvehicleeventpvo|HNSVehicleEventPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REQUIRED_FLAG | HNSIncidentEventDetailsPEOActionRequiredFlag | — |
| ACTUAL_COMPLETION_DATE | HNSIncidentEventDetailsPEOActualCompletionDate | — |
| AIR_QUALITY_TYPE_CODE | HNSIncidentEventDetailsPEOAirQualityTypeCode | — |
| AMOUNT_RECOVERED | HNSIncidentEventDetailsPEOAmountRecovered | — |
| AMOUNT_RECOVERED_UNIT_CD | HNSIncidentEventDetailsPEOAmountRecoveredUnitCd | — |
| AMOUNT_SPILLED | HNSIncidentEventDetailsPEOAmountSpilled | — |
| AMOUNT_SPILLED_UNIT_CD | HNSIncidentEventDetailsPEOAmountSpilledUnitCd | — |
| ATTRIBUTE1 | HNSIncidentEventDetailsPEOAttribute1 | — |
| ATTRIBUTE10 | HNSIncidentEventDetailsPEOAttribute10 | — |
| ATTRIBUTE11 | HNSIncidentEventDetailsPEOAttribute11 | — |
| ATTRIBUTE12 | HNSIncidentEventDetailsPEOAttribute12 | — |
| ATTRIBUTE13 | HNSIncidentEventDetailsPEOAttribute13 | — |
| ATTRIBUTE14 | HNSIncidentEventDetailsPEOAttribute14 | — |
| ATTRIBUTE15 | HNSIncidentEventDetailsPEOAttribute15 | — |
| ATTRIBUTE16 | HNSIncidentEventDetailsPEOAttribute16 | — |
| ATTRIBUTE17 | HNSIncidentEventDetailsPEOAttribute17 | — |
| ATTRIBUTE18 | HNSIncidentEventDetailsPEOAttribute18 | — |
| ATTRIBUTE19 | HNSIncidentEventDetailsPEOAttribute19 | — |
| ATTRIBUTE2 | HNSIncidentEventDetailsPEOAttribute2 | — |
| ATTRIBUTE20 | HNSIncidentEventDetailsPEOAttribute20 | — |
| ATTRIBUTE21 | HNSIncidentEventDetailsPEOAttribute21 | — |
| ATTRIBUTE22 | HNSIncidentEventDetailsPEOAttribute22 | — |
| ATTRIBUTE23 | HNSIncidentEventDetailsPEOAttribute23 | — |
| ATTRIBUTE24 | HNSIncidentEventDetailsPEOAttribute24 | — |
| ATTRIBUTE25 | HNSIncidentEventDetailsPEOAttribute25 | — |
| ATTRIBUTE26 | HNSIncidentEventDetailsPEOAttribute26 | — |
| ATTRIBUTE27 | HNSIncidentEventDetailsPEOAttribute27 | — |
| ATTRIBUTE28 | HNSIncidentEventDetailsPEOAttribute28 | — |
| ATTRIBUTE29 | HNSIncidentEventDetailsPEOAttribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | HNSIncidentEventDetailsPEOAttribute30 | — |
| ATTRIBUTE4 | HNSIncidentEventDetailsPEOAttribute4 | — |
| ATTRIBUTE5 | HNSIncidentEventDetailsPEOAttribute5 | — |
| ATTRIBUTE6 | HNSIncidentEventDetailsPEOAttribute6 | — |
| ATTRIBUTE7 | HNSIncidentEventDetailsPEOAttribute7 | — |
| ATTRIBUTE8 | HNSIncidentEventDetailsPEOAttribute8 | — |
| ATTRIBUTE9 | HNSIncidentEventDetailsPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSIncidentEventDetailsPEOAttributeCategory | — |
| ATTRIBUTE_NUMBER1 | HNSIncidentEventDetailsPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | HNSIncidentEventDetailsPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER2 | HNSIncidentEventDetailsPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSIncidentEventDetailsPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSIncidentEventDetailsPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSIncidentEventDetailsPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | HNSIncidentEventDetailsPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | HNSIncidentEventDetailsPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | HNSIncidentEventDetailsPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | HNSIncidentEventDetailsPEOAttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSIncidentEventDetailsPEOAttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | HNSIncidentEventDetailsPEOAttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSIncidentEventDetailsPEOAttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSIncidentEventDetailsPEOAttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSIncidentEventDetailsPEOAttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSIncidentEventDetailsPEOAttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | HNSIncidentEventDetailsPEOAttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | HNSIncidentEventDetailsPEOAttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | HNSIncidentEventDetailsPEOAttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | HNSIncidentEventDetailsPEOAttributeTimestamp9 | — |
| CITATION_NUM | HNSIncidentEventDetailsPEOCitationNum | — |
| CLEANUP_TEAM_NOTIFIED | HNSIncidentEventDetailsPEOCleanupTeamNotified | — |
| CLEANUP_TEAM_NOTIFIED_AT | HNSIncidentEventDetailsPEOCleanupTeamNotifiedAt | — |
| COMPLETED_FLAG | HNSIncidentEventDetailsPEOCompletedFlag | — |
| CREATED_BY | HNSIncidentEventDetailsPEOCreatedBy | — |
| CREATION_DATE | HNSIncidentEventDetailsPEOCreationDate | — |
| DATE_DISCLOSED | HNSIncidentEventDetailsPEODateDisclosed | — |
| DELETED_FLAG | HNSIncidentEventDetailsPEODeletedFlag | — |
| DELETED_FLAG | HNSIncidentEventDetailsPEODeletedFlag1 | — |
| EMPLOYEE_ASSIGN_ID | HNSIncidentEventDetailsPEOEmployeeAssignId | — |
| EMPLOYEE_ID | HNSIncidentEventDetailsPEOEmployeeId1 | — |
| ERGONOMIC_ASS_REQ_CODE | HNSIncidentEventDetailsPEOErgonomicAssReqCode | — |
| ERGONOMIC_TYPE_CODE | HNSIncidentEventDetailsPEOErgonomicTypeCode | — |
| EVENT_CREATION_DATE | HNSIncidentEventDetailsPEOEventCreationDate | — |
| IMPROVEMENT_TYPE_CODE | HNSIncidentEventDetailsPEOImprovementTypeCode | — |
| INC_EVENT_OWNER_ASSIGN_ID | HNSIncidentEventDetailsPEOIncEventOwnerAssignId | — |
| INCI_DETAIL_DESCR | HNSIncidentEventDetailsPEOInciDetailDescr | — |
| INCI_EVENT_STATUS_CODE | HNSIncidentEventDetailsPEOInciEventStatusCode | — |
| INCIDENT_DETAIL_ID | HNSIncidentEventDetailsPEOIncidentDetailId | — |
| INCIDENT_EVENT_CODE | HNSIncidentEventDetailsPEOIncidentEventCode | — |
| INCIDENT_EVENT_DATE | HNSIncidentEventDetailsPEOIncidentEventDate | — |
| INCIDENT_EVENT_NO | HNSIncidentEventDetailsPEOIncidentEventNo | — |
| INCIDENT_EVENT_OWNER_ID | HNSIncidentEventDetailsPEOIncidentEventOwnerId | — |
| INCIDENT_EVENT_SUMMARY | HNSIncidentEventDetailsPEOIncidentEventSummary | — |
| INCIDENT_ID | HNSIncidentEventDetailsPEOIncidentId | — |
| ISSUE_TYPE_CODE | HNSIncidentEventDetailsPEOIssueTypeCode | — |
| LESSONS_LEARNED | HNSIncidentEventDetailsPEOLessonsLearned | — |
| LIGHT_CONDITION_CODE | HNSIncidentEventDetailsPEOLightConditionCode | — |
| NEAR_MISS_CODE | HNSIncidentEventDetailsPEONearMissCode | — |
| NOTICE_OF_VIOLATION_CD | HNSIncidentEventDetailsPEONoticeOfViolationCd | — |
| OBJECT_VERSION_NUMBER | HNSIncidentEventDetailsPEOObjectVersionNumber | — |
| POLICE_AGENCY_LOCATION | PoliceAgencyLocation | — |
| POLICE_BADGE_NUM | HNSIncidentEventDetailsPEOPoliceBadgeNum | — |
| POLICE_REPORT_FLAG | HNSIncidentEventDetailsPEOPoliceReportFlag | — |
| PROPERTY_DAMAGE_CODE | HNSIncidentEventDetailsPEOPropertyDamageCode | — |
| REPLN_SPILL_KIT_FLAG | HNSIncidentEventDetailsPEOReplnSpillKitFlag | — |
| RESULT_CODE | HNSIncidentEventDetailsPEOResultCode | — |
| ROAD_CONDITION_CODE | HNSIncidentEventDetailsPEORoadConditionCode | — |
| SEVERITY_LEVEL_CODE | HNSIncidentEventDetailsPEOSeverityLevelCode | — |
| SPILL_POSSIBLE_CAUSE_CODE | HNSIncidentEventDetailsPEOSpillPossibleCauseCode | — |
| SPILL_RELEASE_CODE | HNSIncidentEventDetailsPEOSpillReleaseCode | — |
| SPILL_SOURCE_CODE | HNSIncidentEventDetailsPEOSpillSourceCode | — |
| SPILLKIT_DEPLOYED_FLAG | HNSIncidentEventDetailsPEOSpillkitDeployedFlag | — |
| TARGET_COMPLETION_DATE | HNSIncidentEventDetailsPEOTargetCompletionDate | — |
| THIRD_PARTY_DETAILS | HNSIncidentEventDetailsPEOThirdPartyDetails | — |
| TRAFFIC_CONDITION_CODE | HNSIncidentEventDetailsPEOTrafficConditionCode | — |
| TRAFFIC_CONTROLS_CODE | HNSIncidentEventDetailsPEOTrafficControlsCode | — |
| UNSAFE_ACT_TYPE_CODE | HNSIncidentEventDetailsPEOUnsafeActTypeCode | — |
| UNSAFE_CONDITION_CODE | HNSIncidentEventDetailsPEOUnsafeConditionCode | — |
| VEHICLE_ACC_CATEGORY_CODE | HNSIncidentEventDetailsPEOVehicleAccCategoryCode | — |
| VEHICLE_COLLISION_TYPE_CODE | HNSIncidentEventDetailsPEOVehicleCollisionTypeCode | — |
| VEHICLE_SPEED_LIMIT | HNSIncidentEventDetailsPEOVehicleSpeedLimit | — |
| VEHICLE_SPEED_UNIT_CD | HNSIncidentEventDetailsPEOVehicleSpeedUnitCd | — |
| VEHICLE_STRUCK_BY_CODE | HNSIncidentEventDetailsPEOVehicleStruckByCode1 | — |
| VEHICLE_STRUCK_CODE | HNSIncidentEventDetailsPEOVehicleStruckCode | — |
| WEATHER_CONDITION_CODE | HNSIncidentEventDetailsPEOWeatherConditionCode | — |
| WHAT_WAS_SPILLED_OR_RELEASED | HNSIncidentEventDetailsPEOWhatWasSpilledOrReleased | — |

---

## 📚 Referências

- [Oracle Docs — HNS_INCIDENTS_DETAIL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsincidentsdetail.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
