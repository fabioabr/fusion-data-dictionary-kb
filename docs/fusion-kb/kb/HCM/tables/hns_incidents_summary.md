---
id: DOC-HCM-103
doc_type: system-doc
title: "HNS_INCIDENTS_SUMMARY — Resumo de Incidentes de Segurança"
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
  - resumo-incidentes
  - indicadores
  - hns
aliases:
  - HNS_INCIDENTS_SUMMARY
  - hns_incidents_summary
  - hns-incidents-summary
  - DOC-HCM-103
  - resumo-de-incidentes-de-segurança
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_INCIDENTS_SUMMARY

## 📌 Visão Geral

Armazena o **resumo consolidado de incidentes** de saúde e segurança. Fornece uma visão sumarizada com contagens, classificações e indicadores agregados.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Visão consolidada:** Resumo de dados de incidentes para gestão.
- **Indicadores KPI:** Base para cálculo de taxa de frequência e gravidade.
- **Relatórios executivos:** Dados agregados para alta gestão.
- **Benchmarking:** Comparação de indicadores entre períodos e unidades.
- **Compliance:** Dados para relatórios regulatórios periódicos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INCIDENT_SUMMARY_ID | NUMBER(18) | NOT NULL | PK | Identificador do resumo | — | 🟡 80% |
| 2 | INCIDENT_ID | NUMBER(18) | NOT NULL | FK | Incidente detalhado | [[hns_incidents_detail]] | 🟢 90% |
| 3 | SUMMARY_TEXT | VARCHAR2(4000) | NULL | Texto | Texto resumido do incidente | — | 🟡 80% |
| 4 | TOTAL_INJURED | NUMBER | NULL | Indicador | Total de pessoas lesionadas | — | 🟡 75% |
| 5 | DAYS_LOST | NUMBER | NULL | Indicador | Dias perdidos | — | 🟡 75% |
| 6 | COST_ESTIMATE | NUMBER | NULL | Financeiro | Estimativa de custo | — | 🟡 70% |
| 7 | CURRENCY_CODE | VARCHAR2(30) | NULL | Referência | Moeda | — | 🟡 75% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_incidents_detail]] — via `INCIDENT_ID` (detalhe do incidente resumido)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Resumos por período
```sql
SELECT s.INCIDENT_ID, s.SUMMARY_TEXT, s.TOTAL_INJURED, s.DAYS_LOST
FROM   HNS_INCIDENTS_SUMMARY s
JOIN   HNS_INCIDENTS_DETAIL d ON s.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

### Custo total por período
```sql
SELECT SUM(s.COST_ESTIMATE) AS custo_total, SUM(s.DAYS_LOST) AS dias_perdidos
FROM   HNS_INCIDENTS_SUMMARY s
JOIN   HNS_INCIDENTS_DETAIL d ON s.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

---

## 🔒 Observações

- Complementa `HNS_INCIDENTS_DETAIL` com dados sumarizados.
- `DAYS_LOST` é fundamental para cálculo de taxa de gravidade.
- `COST_ESTIMATE` permite análise financeira do impacto de incidentes.
- Um incidente pode ter um ou mais registros de resumo dependendo das atualizações.

---

## 🔗 PVOs Relacionados

### [[hnsincidenteventpvo|HNSIncidentEventPVO]] (HCM · BICC: 65/109)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REQUIRED_FLAG | HNSIncidentsPEOActionReqrdFlag | ✅ |
| ACTUAL_COMPLETION_DATE | HNSIncidentsPEOActualCompletionDate | ✅ |
| ATTRIBUTE1 | HNSIncidentsPEOAttribute1 | — |
| ATTRIBUTE10 | HNSIncidentsPEOAttribute10 | — |
| ATTRIBUTE11 | HNSIncidentsPEOAttribute11 | — |
| ATTRIBUTE12 | HNSIncidentsPEOAttribute12 | — |
| ATTRIBUTE13 | HNSIncidentsPEOAttribute13 | — |
| ATTRIBUTE14 | HNSIncidentsPEOAttribute14 | — |
| ATTRIBUTE15 | HNSIncidentsPEOAttribute15 | — |
| ATTRIBUTE16 | HNSIncidentsPEOAttribute16 | — |
| ATTRIBUTE17 | HNSIncidentsPEOAttribute17 | — |
| ATTRIBUTE18 | HNSIncidentsPEOAttribute18 | — |
| ATTRIBUTE19 | HNSIncidentsPEOAttribute19 | — |
| ATTRIBUTE2 | HNSIncidentsPEOAttribute2 | — |
| ATTRIBUTE20 | HNSIncidentsPEOAttribute20 | — |
| ATTRIBUTE3 | HNSIncidentsPEOAttribute3 | — |
| ATTRIBUTE4 | HNSIncidentsPEOAttribute4 | — |
| ATTRIBUTE5 | HNSIncidentsPEOAttribute5 | — |
| ATTRIBUTE6 | HNSIncidentsPEOAttribute6 | — |
| ATTRIBUTE7 | HNSIncidentsPEOAttribute7 | — |
| ATTRIBUTE8 | HNSIncidentsPEOAttribute8 | — |
| ATTRIBUTE9 | HNSIncidentsPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSIncidentsPEOAttrCategory | — |
| ATTRIBUTE_NUMBER1 | HNSIncidentsPEOAttrNumber1 | — |
| ATTRIBUTE_NUMBER10 | HNSIncidentsPEOAttrNumber10 | — |
| ATTRIBUTE_NUMBER2 | HNSIncidentsPEOAttrNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSIncidentsPEOAttrNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSIncidentsPEOAttrNumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSIncidentsPEOAttrNumber5 | — |
| ATTRIBUTE_NUMBER6 | HNSIncidentsPEOAttrNumber6 | — |
| ATTRIBUTE_NUMBER7 | HNSIncidentsPEOAttrNumber7 | — |
| ATTRIBUTE_NUMBER8 | HNSIncidentsPEOAttrNumber8 | — |
| ATTRIBUTE_NUMBER9 | HNSIncidentsPEOAttrNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSIncidentsPEOAttrTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | HNSIncidentsPEOAttrTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSIncidentsPEOAttrTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSIncidentsPEOAttrTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSIncidentsPEOAttrTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSIncidentsPEOAttrTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | HNSIncidentsPEOAttrTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | HNSIncidentsPEOAttrTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | HNSIncidentsPEOAttrTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | HNSIncidentsPEOAttrTimestamp9 | — |
| BIZ_CONT_PLAN_ACT_BY_EMPID | HNSIncidentsPEOBizConPlnAcEmid | ✅ |
| BIZ_CONT_PLAN_ACTIVATED_AT | HNSIncidentsPEOBizContPlnActAt | ✅ |
| BIZ_CONT_PLAN_ACTIVATED_FLAG | HNSIncidentsPEOBizConPlnActdFl | ✅ |
| COMPLETED_FLAG | HNSIncidentsPEOCompletedFlag | ✅ |
| CONFIDENTIAL_FLAG | HNSIncidentsPEOConfidentialFlag | ✅ |
| CREATED_BY | HNSIncidentsPEOCreatedBy | ✅ |
| CREATION_DATE | HNSIncidentsPEOCreationDate | ✅ |
| DELETED_FLAG | HNSIncidentsPEODeletedFlag | ✅ |
| EMERG_ACTION_PLAN_ACT_BY_EMPID | HNSIncidentsPEOEmrAcPlnAcByEmid | ✅ |
| EMERG_ACTION_PLAN_ACT_FLAG | HNSIncidentsPEOEmergAcPlnAcFlg | ✅ |
| EMERG_ACTION_PLAN_ACTIVATED_AT | HNSIncidentsPEOEmergActPlanActvtdAt | ✅ |
| EMERGENCY_FLAG | HNSIncidentsPEOEmergencyFlag | ✅ |
| EMPLOYEE_ID | HNSIncidentsPEOEmployeeId | ✅ |
| EVACUATION_FLAG | HNSIncidentsPEOEvacuationFlag | ✅ |
| EVACUATION_LENGTH_OF_TIME | HNSIncidentsPEOEvacLengthOfTim | ✅ |
| EVACUATION_ORDERED_AT | HNSIncidentsPEOEvacOrderedAt | ✅ |
| EVACUATION_ORDERED_BY_EMP_ID | HNSIncidentsPEOEvacOrdrByEmpId | ✅ |
| EVACUATION_TYPE_CODE | HNSIncidentsPEOEvacTypeCode | ✅ |
| FACILITY_CLOSED_AT | HNSIncidentsPEOFacilityClsdAt | ✅ |
| FACILITY_CLOSED_BY_EMP_ID | HNSIncidentsPEOFacClsdByEmpId | ✅ |
| FACILITY_CLOSED_FLAG | HNSIncidentsPEOFacClsdFlag | ✅ |
| FACILITY_CLOSED_LENGTH_OF_TIME | HNSIncidentsPEOFacClsdLngOfTim | ✅ |
| INCIDENT_APPROVER_EMAIL_FLAG | HNSIncidentsPEOIncidentApproverEmailFlag | ✅ |
| INCIDENT_CREATE_DATE | HNSIncidentsPEOIncidentCreateDate | ✅ |
| INCIDENT_DATE | HNSIncidentsPEOIncidentDate | ✅ |
| INCIDENT_DESCRIPTION | HNSIncidentsPEOIncidentDescription | ✅ |
| INCIDENT_ID | HNSIncidentsPEOIncidentId | ✅ |
| INCIDENT_IMME_ACT_DESCR | HNSIncidentsPEOIncidentImmeActDescr | ✅ |
| INCIDENT_NO | HNSIncidentsPEOIncidentNo | ✅ |
| INCIDENT_OWNER_ASSIGN_ID | HNSIncidentsPEOIncOwnAsnId | — |
| INCIDENT_OWNER_ID | HNSIncidentsPEOIncidentOwnerId | ✅ |
| INCIDENT_REPORTED_DATE | HNSIncidentsPEOIncRprtdDt | ✅ |
| INCIDENT_REVIEWER_EMAIL_FLAG | HNSIncidentsPEOIncidentReviewerEmailFlag | ✅ |
| INCIDENT_SOURCE_CODE | HNSIncidentsPEOIncidentSrcCode | ✅ |
| INCIDENT_STATUS_CODE | HNSIncidentsPEOIncidentStatusCode | ✅ |
| INCIDENT_SUMMARY | HNSIncidentsPEOIncidentSummary | ✅ |
| INCIDENT_TYPE_CODE | HNSIncidentsPEOIncidentTypCode | ✅ |
| LAST_UPDATE_DATE | HNSIncidentsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HNSIncidentsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | HNSIncidentsPEOLastUpdatedBy | ✅ |
| LESSONS_LEARNED | HNSIncidentsPEOLessonsLearned | ✅ |
| LOCATION_ID | HNSIncidentsPEOLocationId | ✅ |
| LOCATION_TYPE_CODE | HNSIncidentsPEOLocationTypeCode | ✅ |
| NOTIFIED_PER_ASSIGN_ID | HNSIncidentsPEONtfdPerAsnId | — |
| NOTIFIED_PERSON_ID | HNSIncidentsPEONtfdPerId | ✅ |
| OBJECT_VERSION_NUMBER | HNSIncidentsPEOObjectVersionNumber | ✅ |
| OFFSITE_LOC_TYPE_CODE | HNSIncidentsPEOOffsiteLocTypeCode | ✅ |
| RADIUS | HNSIncidentsPEORadius | ✅ |
| RADIUS_UNIT_CD | HNSIncidentsPEORadiusUnitCd | ✅ |
| REPORTER_ASSIGNMENT_ID | HNSIncidentsPEORptrAsntId | — |
| REPORTER_TYPE_CODE | HNSIncidentsPEOReporterTypeCode | ✅ |
| REPTR_ADDR_LINE1 | HNSIncidentsPEOReptrAddrLine1 | ✅ |
| REPTR_ADDR_LINE2 | HNSIncidentsPEOReptrAddrLine2 | ✅ |
| REPTR_AREA_CODE | HNSIncidentsPEOReptrAreaCode | ✅ |
| REPTR_CITY | HNSIncidentsPEOReptrCity | ✅ |
| REPTR_COUNTRY | HNSIncidentsPEOReptrCountry | ✅ |
| REPTR_COUNTRY_CODE_NUM | HNSIncidentsPEOReptrCountryCodeNum | ✅ |
| REPTR_EMAIL | HNSIncidentsPEOReptrEmail | ✅ |
| REPTR_NAME | HNSIncidentsPEOReptrName | ✅ |
| REPTR_NONEMP_TYPE_CODE | HNSIncidentsPEOReptrNonempTypeCode | ✅ |
| REPTR_PHONE_NO | HNSIncidentsPEOReptrPhoneNo | ✅ |
| REPTR_SPECIFIC_LOCATION | HNSIncidentsPEOReptrSpecificLocation | ✅ |
| REPTR_STATE | HNSIncidentsPEOReptrState | ✅ |
| REPTR_ZIP_CODE | HNSIncidentsPEOReptrZipCode | ✅ |
| SEVERITY_LEVEL_CODE | HNSIncidentsPEOSeverityLevelCode | ✅ |
| TARGET_COMPLETION_DATE | HNSIncidentsPEOTargetCompletionDate | ✅ |

### [[hnsincidentspvo|HNSIncidentsPVO]] (HCM · BICC: 63/104)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REQUIRED_FLAG | HNSIncidentsPEOActionReqrdFlag | ✅ |
| ACTUAL_COMPLETION_DATE | HNSIncidentsPEOActualCompletionDate | ✅ |
| ATTRIBUTE1 | HNSIncidentsPEOAttribute1 | — |
| ATTRIBUTE10 | HNSIncidentsPEOAttribute10 | — |
| ATTRIBUTE11 | HNSIncidentsPEOAttribute11 | — |
| ATTRIBUTE12 | HNSIncidentsPEOAttribute12 | — |
| ATTRIBUTE13 | HNSIncidentsPEOAttribute13 | — |
| ATTRIBUTE14 | HNSIncidentsPEOAttribute14 | — |
| ATTRIBUTE15 | HNSIncidentsPEOAttribute15 | — |
| ATTRIBUTE16 | HNSIncidentsPEOAttribute16 | — |
| ATTRIBUTE17 | HNSIncidentsPEOAttribute17 | — |
| ATTRIBUTE18 | HNSIncidentsPEOAttribute18 | — |
| ATTRIBUTE19 | HNSIncidentsPEOAttribute19 | — |
| ATTRIBUTE2 | HNSIncidentsPEOAttribute2 | — |
| ATTRIBUTE20 | HNSIncidentsPEOAttribute20 | — |
| ATTRIBUTE3 | HNSIncidentsPEOAttribute3 | — |
| ATTRIBUTE4 | HNSIncidentsPEOAttribute4 | — |
| ATTRIBUTE5 | HNSIncidentsPEOAttribute5 | — |
| ATTRIBUTE6 | HNSIncidentsPEOAttribute6 | — |
| ATTRIBUTE7 | HNSIncidentsPEOAttribute7 | — |
| ATTRIBUTE8 | HNSIncidentsPEOAttribute8 | — |
| ATTRIBUTE9 | HNSIncidentsPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSIncidentsPEOAttrCategory | — |
| ATTRIBUTE_NUMBER1 | HNSIncidentsPEOAttrNumber1 | — |
| ATTRIBUTE_NUMBER10 | HNSIncidentsPEOAttrNumber10 | — |
| ATTRIBUTE_NUMBER2 | HNSIncidentsPEOAttrNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSIncidentsPEOAttrNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSIncidentsPEOAttrNumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSIncidentsPEOAttrNumber5 | — |
| ATTRIBUTE_NUMBER6 | HNSIncidentsPEOAttrNumber6 | — |
| ATTRIBUTE_NUMBER7 | HNSIncidentsPEOAttrNumber7 | — |
| ATTRIBUTE_NUMBER8 | HNSIncidentsPEOAttrNumber8 | — |
| ATTRIBUTE_NUMBER9 | HNSIncidentsPEOAttrNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSIncidentsPEOAttrTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | HNSIncidentsPEOAttrTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSIncidentsPEOAttrTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSIncidentsPEOAttrTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSIncidentsPEOAttrTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSIncidentsPEOAttrTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | HNSIncidentsPEOAttrTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | HNSIncidentsPEOAttrTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | HNSIncidentsPEOAttrTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | HNSIncidentsPEOAttrTimestamp9 | — |
| BIZ_CONT_PLAN_ACT_BY_EMPID | HNSIncidentsPEOBizConPlnAcEmid | ✅ |
| BIZ_CONT_PLAN_ACTIVATED_AT | HNSIncidentsPEOBizContPlnActAt | ✅ |
| BIZ_CONT_PLAN_ACTIVATED_FLAG | HNSIncidentsPEOBizConPlnActdFl | ✅ |
| COMPLETED_FLAG | HNSIncidentsPEOCompletedFlag | ✅ |
| CONFIDENTIAL_FLAG | HNSIncidentsPEOConfidentialFlag | ✅ |
| CREATED_BY | HNSIncidentsPEOCreatedBy | ✅ |
| CREATION_DATE | HNSIncidentsPEOCreationDate | ✅ |
| DELETED_FLAG | HNSIncidentsPEODeletedFlag | ✅ |
| EMERG_ACTION_PLAN_ACT_BY_EMPID | HNSIncidentsPEOEmrAcPlnAcByEmid | ✅ |
| EMERG_ACTION_PLAN_ACT_FLAG | HNSIncidentsPEOEmergAcPlnAcFlg | ✅ |
| EMERG_ACTION_PLAN_ACTIVATED_AT | HNSIncidentsPEOEmergActPlanActvtdAt | ✅ |
| EMERGENCY_FLAG | HNSIncidentsPEOEmergencyFlag | ✅ |
| EMPLOYEE_ID | HNSIncidentsPEOEmployeeId | ✅ |
| EVACUATION_FLAG | HNSIncidentsPEOEvacuationFlag | ✅ |
| EVACUATION_LENGTH_OF_TIME | HNSIncidentsPEOEvacLengthOfTim | ✅ |
| EVACUATION_ORDERED_AT | HNSIncidentsPEOEvacOrderedAt | ✅ |
| EVACUATION_ORDERED_BY_EMP_ID | HNSIncidentsPEOEvacOrdrByEmpId | ✅ |
| EVACUATION_TYPE_CODE | HNSIncidentsPEOEvacTypeCode | ✅ |
| FACILITY_CLOSED_AT | HNSIncidentsPEOFacilityClsdAt | ✅ |
| FACILITY_CLOSED_BY_EMP_ID | HNSIncidentsPEOFacClsdByEmpId | ✅ |
| FACILITY_CLOSED_FLAG | HNSIncidentsPEOFacClsdFlag | ✅ |
| FACILITY_CLOSED_LENGTH_OF_TIME | HNSIncidentsPEOFacClsdLngOfTim | ✅ |
| INCIDENT_APPROVER_EMAIL_FLAG | HNSIncidentsPEOIncidentApproverEmailFlag | ✅ |
| INCIDENT_CREATE_DATE | HNSIncidentsPEOIncidentCreateDate | ✅ |
| INCIDENT_DATE | HNSIncidentsPEOIncidentDate | ✅ |
| INCIDENT_DESCRIPTION | HNSIncidentsPEOIncidentDescription | ✅ |
| INCIDENT_ID | HNSIncidentsPEOIncidentId | ✅ |
| INCIDENT_IMME_ACT_DESCR | HNSIncidentsPEOIncidentImmeActDescr | ✅ |
| INCIDENT_NO | HNSIncidentsPEOIncidentNo | ✅ |
| INCIDENT_OWNER_ID | HNSIncidentsPEOIncidentOwnerId | ✅ |
| INCIDENT_REVIEWER_EMAIL_FLAG | HNSIncidentsPEOIncidentReviewerEmailFlag | ✅ |
| INCIDENT_SOURCE_CODE | HNSIncidentsPEOIncidentSrcCode | ✅ |
| INCIDENT_STATUS_CODE | HNSIncidentsPEOIncidentStatusCode | ✅ |
| INCIDENT_SUMMARY | HNSIncidentsPEOIncidentSummary | ✅ |
| INCIDENT_TYPE_CODE | HNSIncidentsPEOIncidentTypCode | ✅ |
| LAST_UPDATE_DATE | HNSIncidentsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HNSIncidentsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | HNSIncidentsPEOLastUpdatedBy | ✅ |
| LESSONS_LEARNED | HNSIncidentsPEOLessonsLearned | ✅ |
| LOCATION_ID | HNSIncidentsPEOLocationId | ✅ |
| LOCATION_TYPE_CODE | HNSIncidentsPEOLocationTypeCode | ✅ |
| OBJECT_VERSION_NUMBER | HNSIncidentsPEOObjectVersionNumber | ✅ |
| OFFSITE_LOC_TYPE_CODE | HNSIncidentsPEOOffsiteLocTypeCode | ✅ |
| RADIUS | HNSIncidentsPEORadius | ✅ |
| RADIUS_UNIT_CD | HNSIncidentsPEORadiusUnitCd | ✅ |
| REPORTER_TYPE_CODE | HNSIncidentsPEOReporterTypeCode | ✅ |
| REPTR_ADDR_LINE1 | HNSIncidentsPEOReptrAddrLine1 | ✅ |
| REPTR_ADDR_LINE2 | HNSIncidentsPEOReptrAddrLine2 | ✅ |
| REPTR_AREA_CODE | HNSIncidentsPEOReptrAreaCode | ✅ |
| REPTR_CITY | HNSIncidentsPEOReptrCity | ✅ |
| REPTR_COUNTRY | HNSIncidentsPEOReptrCountry | ✅ |
| REPTR_COUNTRY_CODE_NUM | HNSIncidentsPEOReptrCountryCodeNum | ✅ |
| REPTR_EMAIL | HNSIncidentsPEOReptrEmail | ✅ |
| REPTR_NAME | HNSIncidentsPEOReptrName | ✅ |
| REPTR_NONEMP_TYPE_CODE | HNSIncidentsPEOReptrNonempTypeCode | ✅ |
| REPTR_PHONE_NO | HNSIncidentsPEOReptrPhoneNo | ✅ |
| REPTR_SPECIFIC_LOCATION | HNSIncidentsPEOReptrSpecificLocation | ✅ |
| REPTR_STATE | HNSIncidentsPEOReptrState | ✅ |
| REPTR_ZIP_CODE | HNSIncidentsPEOReptrZipCode | ✅ |
| SEVERITY_LEVEL_CODE | HNSIncidentsPEOSeverityLevelCode | ✅ |
| TARGET_COMPLETION_DATE | HNSIncidentsPEOTargetCompletionDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_INCIDENTS_SUMMARY](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsincidentssummary.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
