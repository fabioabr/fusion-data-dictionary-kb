---
id: DOC-HCM-381
doc_type: system-doc
title: "HWM_TM_REC — Registros de Time Management"
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
  - time-management
  - time-record
  - registro-tempo
aliases:
  - HWM_TM_REC
  - hwm_tm_rec
  - hwm-tm-rec
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_REC

## 📌 Visão Geral

Armazena os **registros de tempo** (time records) do módulo Time Management. Cada registro representa uma entrada de ponto ou tempo registrada por um colaborador.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de ponto:** armazena entradas de tempo dos colaboradores.
- **Base para folha de pagamento:** dados de horas trabalhadas alimentam o payroll.
- **Controle de jornada:** gestão de horas normais, extras e banco de horas.
- **Auditoria trabalhista:** evidência de jornada para conformidade legal.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TM_REC_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de tempo | — | 🟡 70% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do colaborador | PER_ALL_PEOPLE_F | 🟡 70% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Identificador da atribuição | PER_ALL_ASSIGNMENTS_M | 🟡 70% |
| 4 | REC_DATE | DATE | NOT NULL | Período | Data do registro de tempo | — | 🟡 65% |
| 5 | REC_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do registro (normal, extra, etc.) | — | 🟡 60% |
| 6 | MEASURE | NUMBER | NULL | Dados | Quantidade de tempo registrado | — | 🟡 60% |
| 7 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro | — | 🟡 65% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa do registro de tempo)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo do registro de tempo)

### Tabelas-filha (FK de saída)
- [[hwm_tm_rec_grp]] — via `TM_REC_ID` (agrupamento de registros)

---

## 📎 Uso Típico

### Registros de tempo por colaborador
```sql
SELECT r.TM_REC_ID, r.PERSON_ID, r.REC_DATE,
       r.MEASURE, r.STATUS
FROM   HWM_TM_REC r
WHERE  r.PERSON_ID = :p_person_id
  AND  r.REC_DATE BETWEEN :dt_ini AND :dt_fim;
```

### Filtros comuns
- `PERSON_ID = :p_person_id — Filtrar por colaborador`
- `REC_DATE BETWEEN :dt_ini AND :dt_fim — Período`
- `STATUS = 'APPROVED' — Registros aprovados`

---

## 🔒 Observações

- Tabela central do módulo Time Management.
- Registros devem ser aprovados antes de serem enviados ao payroll.
- Integração com HXT (Time & Labor) para configurações avançadas.

---

## 🔗 PVOs Relacionados

### [[deviceactivityinpvo|DeviceActivityInPVO]] (HCM · BICC: 9/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVITY_EVENT_TIME | TimeRecordPEOActivityEventTime | ✅ |
| ACTIVITY_TYPE | TimeRecordPEOActivityType | — |
| COMMENT_TEXT | TimeRecordPEOCommentText | — |
| CREATED_BY | TimeRecordPEOCreatedBy | ✅ |
| CREATION_DATE | TimeRecordPEOCreationDate | ✅ |
| DATA_SET_ID | TimeRecordPEODataSetId | — |
| DATE_FROM | TimeRecordPEODateFrom | — |
| DATE_TO | TimeRecordPEODateTo | — |
| DELETE_FLAG | TimeRecordPEODeleteFlag | — |
| ENTERPRISE_ID | TimeRecordPEOEnterpriseId | — |
| LAST_UPDATE_DATE | TimeRecordPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TimeRecordPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TimeRecordPEOLastUpdatedBy | ✅ |
| LATEST_VERSION | TimeRecordPEOLatestVersion | — |
| LAYER_CODE | TimeRecordPEOLayerCode | — |
| MEASURE | TimeRecordPEOMeasure | — |
| OBJECT_VERSION_NUMBER | TimeRecordPEOObjectVersionNumber | — |
| ORDER_ENTERED | TimeRecordPEOOrderEntered | — |
| ORIG_TM_REC_ID | TimeRecordPEOOriginalTimeRecordId | — |
| ORIG_TM_REC_VERSION | TimeRecordPEOOriginalTimeRecordVersion | — |
| RESOURCE_ID | TimeRecordPEOResourceId | — |
| RESOURCE_TYPE | TimeRecordPEOResourceType | — |
| START_TIME | TimeRecordPEOStartTime | — |
| STOP_TIME | TimeRecordPEOStopTime | — |
| SUBRESOURCE_ID | TimeRecordPEOSubresourceId | — |
| TCSMR_CONFIG_SET_ID | TimeRecordPEOTimeConsumerConfigurationSetId | — |
| TCSMR_SET_ID | TimeRecordPEOTimeConsumerSetId | — |
| TIME_REPORTER_ID | TimeRecordPEOTimeReporterId | ✅ |
| TM_REC_ID | TimeRecordPEOTimeRecordId | ✅ |
| TM_REC_TYPE | TimeRecordPEOTimeRecordType | — |
| TM_REC_VERSION | TimeRecordPEOTimeRecordVersion | ✅ |
| UNIT_OF_MEASURE | TimeRecordPEOUnitOfMeasure | — |
| USER_STATUS | TimeRecordPEOUserStatus | — |

### [[deviceactivityoutpvo|DeviceActivityOutPVO]] (HCM · BICC: 9/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVITY_EVENT_TIME | TimeRecordPEOActivityEventTime | ✅ |
| ACTIVITY_TYPE | TimeRecordPEOActivityType | — |
| COMMENT_TEXT | TimeRecordPEOCommentText | — |
| CREATED_BY | TimeRecordPEOCreatedBy | ✅ |
| CREATION_DATE | TimeRecordPEOCreationDate | ✅ |
| DATA_SET_ID | TimeRecordPEODataSetId | — |
| DATE_FROM | TimeRecordPEODateFrom | — |
| DATE_TO | TimeRecordPEODateTo | — |
| DELETE_FLAG | TimeRecordPEODeleteFlag | — |
| ENTERPRISE_ID | TimeRecordPEOEnterpriseId | — |
| LAST_UPDATE_DATE | TimeRecordPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TimeRecordPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TimeRecordPEOLastUpdatedBy | ✅ |
| LATEST_VERSION | TimeRecordPEOLatestVersion | — |
| LAYER_CODE | TimeRecordPEOLayerCode | — |
| MEASURE | TimeRecordPEOMeasure | — |
| OBJECT_VERSION_NUMBER | TimeRecordPEOObjectVersionNumber | — |
| ORDER_ENTERED | TimeRecordPEOOrderEntered | — |
| ORIG_TM_REC_ID | TimeRecordPEOOriginalTimeRecordId | — |
| ORIG_TM_REC_VERSION | TimeRecordPEOOriginalTimeRecordVersion | — |
| RESOURCE_ID | TimeRecordPEOResourceId | — |
| RESOURCE_TYPE | TimeRecordPEOResourceType | — |
| START_TIME | TimeRecordPEOStartTime | — |
| STOP_TIME | TimeRecordPEOStopTime | — |
| SUBRESOURCE_ID | TimeRecordPEOSubresourceId | — |
| TCSMR_CONFIG_SET_ID | TimeRecordPEOTimeConsumerConfigurationSetId | — |
| TCSMR_SET_ID | TimeRecordPEOTimeConsumerSetId | — |
| TIME_REPORTER_ID | TimeRecordPEOTimeReporterId | ✅ |
| TM_REC_ID | TimeRecordPEOTimeRecordId | ✅ |
| TM_REC_TYPE | TimeRecordPEOTimeRecordType | — |
| TM_REC_VERSION | TimeRecordPEOTimeRecordVersion | ✅ |
| UNIT_OF_MEASURE | TimeRecordPEOUnitOfMeasure | — |
| USER_STATUS | TimeRecordPEOUserStatus | — |

### [[deviceactivitypvo|DeviceActivityPVO]] (HCM · BICC: 10/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVITY_EVENT_TIME | TimeRecordPEOActivityEventTime | ✅ |
| ACTIVITY_TYPE | TimeRecordPEOActivityType | ✅ |
| COMMENT_TEXT | TimeRecordPEOCommentText | — |
| CREATED_BY | TimeRecordPEOCreatedBy | ✅ |
| CREATION_DATE | TimeRecordPEOCreationDate | ✅ |
| DATA_SET_ID | TimeRecordPEODataSetId | — |
| DATE_FROM | TimeRecordPEODateFrom | — |
| DATE_TO | TimeRecordPEODateTo | — |
| DELETE_FLAG | TimeRecordPEODeleteFlag | — |
| ENTERPRISE_ID | TimeRecordPEOEnterpriseId | — |
| LAST_UPDATE_DATE | TimeRecordPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TimeRecordPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TimeRecordPEOLastUpdatedBy | ✅ |
| LATEST_VERSION | TimeRecordPEOLatestVersion | — |
| LAYER_CODE | TimeRecordPEOLayerCode | — |
| MEASURE | TimeRecordPEOMeasure | — |
| OBJECT_VERSION_NUMBER | TimeRecordPEOObjectVersionNumber | — |
| ORDER_ENTERED | TimeRecordPEOOrderEntered | — |
| ORIG_TM_REC_ID | TimeRecordPEOOriginalTimeRecordId | — |
| ORIG_TM_REC_VERSION | TimeRecordPEOOriginalTimeRecordVersion | — |
| RESOURCE_ID | TimeRecordPEOResourceId | — |
| RESOURCE_TYPE | TimeRecordPEOResourceType | — |
| START_TIME | TimeRecordPEOStartTime | — |
| STOP_TIME | TimeRecordPEOStopTime | — |
| SUBRESOURCE_ID | TimeRecordPEOSubresourceId | — |
| TCSMR_CONFIG_SET_ID | TimeRecordPEOTimeConsumerConfigurationSetId | — |
| TCSMR_SET_ID | TimeRecordPEOTimeConsumerSetId | — |
| TIME_REPORTER_ID | TimeRecordPEOTimeReporterId | ✅ |
| TM_REC_ID | TimeRecordPEOTimeRecordId | ✅ |
| TM_REC_TYPE | TimeRecordPEOTimeRecordType | — |
| TM_REC_VERSION | TimeRecordPEOTimeRecordVersion | ✅ |
| UNIT_OF_MEASURE | TimeRecordPEOUnitOfMeasure | — |
| USER_STATUS | TimeRecordPEOUserStatus | — |

### [[historicprocessedtimeentrypvo|HistoricProcessedTimeEntryPVO]] (HCM · BICC: 24/35)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVITY_EVENT_TIME | TimeEntryActivityEventTime | — |
| ACTIVITY_TYPE | TimeEntryActivityType | — |
| ACTUAL_DATE | TimeEntryTimeRecordPEOActualDate | ✅ |
| COMMENT_TEXT | TimeEntryCommentText | ✅ |
| CREATED_BY | TimeEntryCreatedBy | ✅ |
| CREATION_DATE | TimeEntryCreationDate | ✅ |
| DATA_SET_ID | TimeEntryDataSetId | — |
| DATE_FROM | TimeEntryDateFrom | ✅ |
| DATE_TO | TimeEntryDateTo | ✅ |
| DELETE_FLAG | TimeEntryDeleteFlag | ✅ |
| ENTERPRISE_ID | TimeEntryEnterpriseId | — |
| LAST_UPDATE_DATE | TimeEntryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TimeEntryLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TimeEntryLastUpdatedBy | ✅ |
| LATEST_VERSION | TimeEntryLatestVersion | ✅ |
| LAYER_CODE | TimeEntryLayerCode | ✅ |
| MEASURE | TimeEntryMeasure | ✅ |
| ORDER_ENTERED | TimeEntryOrderEntered | — |
| ORIG_TM_REC_ID | TimeEntryOriginalTimeRecordId | ✅ |
| ORIG_TM_REC_VERSION | TimeEntryOriginalTimeRecordVersion | ✅ |
| REF_DATE | TimeEntryTimeRecordPEORefDate | ✅ |
| RESOURCE_ID | TimeEntryResourceId | — |
| RESOURCE_TYPE | TimeEntryResourceType | — |
| START_TIME | TimeEntryStartTime | ✅ |
| STOP_TIME | TimeEntryStopTime | ✅ |
| SUBRESOURCE_ID | TimeEntrySubresourceId | — |
| TCSMR_CONFIG_SET_ID | TimeEntryTimeConsumerConfigurationSetId | — |
| TCSMR_SET_ID | TimeEntryTimeConsumerSetId | ✅ |
| TIME_REPORTER_ID | TimeEntryTimeReporterId | ✅ |
| TM_REC_ID | TimeEntryTimeRecordId | ✅ |
| TM_REC_ROW_ID | TimeEntryTimeRecordRowId | — |
| TM_REC_TYPE | TimeEntryTimeRecordType | ✅ |
| TM_REC_VERSION | TimeEntryTimeRecordVersion | ✅ |
| UNIT_OF_MEASURE | TimeEntryUnitOfMeasure | ✅ |
| USER_STATUS | TimeEntryUserStatus | — |

### [[historicreportedtimeentrypvo|HistoricReportedTimeEntryPVO]] (HCM · BICC: 20/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVITY_EVENT_TIME | TimeEntryActivityEventTime | — |
| ACTIVITY_IN_ID | TimeEntryActivityInId | — |
| ACTIVITY_OUT_ID | TimeEntryActivityOutId | — |
| ACTIVITY_TYPE | TimeEntryActivityType | — |
| COMMENT_TEXT | TimeEntryCommentText | ✅ |
| CREATED_BY | TimeEntryCreatedBy | ✅ |
| CREATION_DATE | TimeEntryCreationDate | ✅ |
| DATA_SET_ID | TimeEntryDataSetId | — |
| DATE_FROM | TimeEntryDateFrom | ✅ |
| DATE_TO | TimeEntryDateTo | ✅ |
| DELETE_FLAG | TimeEntryDeleteFlag | ✅ |
| ENTERPRISE_ID | TimeEntryEnterpriseId | — |
| LAST_UPDATE_DATE | TimeEntryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TimeEntryLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TimeEntryLastUpdatedBy | ✅ |
| LATEST_VERSION | TimeEntryLatestVersion | ✅ |
| LAYER_CODE | TimeEntryLayerCode | ✅ |
| MEASURE | TimeEntryMeasure | ✅ |
| ORDER_ENTERED | TimeEntryOrderEntered | — |
| RESOURCE_ID | TimeEntryResourceId | — |
| RESOURCE_TYPE | TimeEntryResourceType | — |
| START_TIME | TimeEntryStartTime | ✅ |
| STOP_TIME | TimeEntryStopTime | ✅ |
| SUBRESOURCE_ID | TimeEntrySubresourceId | — |
| TCSMR_CONFIG_SET_ID | TimeEntryTimeConsumerConfigurationSetId | — |
| TCSMR_SET_ID | TimeEntryTimeConsumerSetId | ✅ |
| TIME_REPORTER_ID | TimeEntryTimeReporterId | ✅ |
| TM_REC_ID | TimeEntryTimeRecordId | ✅ |
| TM_REC_TYPE | TimeEntryTimeRecordType | ✅ |
| TM_REC_VERSION | TimeEntryTimeRecordVersion | ✅ |
| UNIT_OF_MEASURE | TimeEntryUnitOfMeasure | ✅ |
| USER_STATUS | TimeEntryUserStatus | — |

### [[plannedscheduleshiftentrypvo|PlannedScheduleShiftEntryPVO]] (HCM · BICC: 11/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | entryCommentText | — |
| CREATED_BY | entryCreatedBy | ✅ |
| CREATION_DATE | entryCreationDate | ✅ |
| DATE_FROM | entryDateFrom | — |
| DATE_TO | entryDateTo | — |
| DELETE_FLAG | entryDeleteFlag | — |
| LAST_UPDATE_DATE | entryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | entryLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | entryLastUpdatedBy | ✅ |
| LATEST_VERSION | entryLatestVersion | — |
| LAYER_CODE | entryLayerCode | — |
| MEASURE | entryMeasure | ✅ |
| RESOURCE_ID | entryResourceId | ✅ |
| RESOURCE_TYPE | entryResourceType | — |
| START_TIME | entryStartTime | ✅ |
| STOP_TIME | entryStopTime | ✅ |
| SUBRESOURCE_ID | entrySubresourceId | — |
| TCSMR_CONFIG_SET_ID | entryTcsmrConfigSetId | — |
| TCSMR_SET_ID | entryTcsmrSetId | — |
| TIME_REPORTER_ID | entryTimeReporterId | — |
| TM_REC_ID | entryTmRecId | ✅ |
| TM_REC_TYPE | entryTmRecType | — |
| TM_REC_VERSION | entryTmRecVersion | ✅ |
| UNIT_OF_MEASURE | entryUnitOfMeasure | — |

### [[processedtimeentrypvo|ProcessedTimeEntryPVO]] (HCM · BICC: 24/35)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVITY_EVENT_TIME | TimeEntryActivityEventTime | — |
| ACTIVITY_TYPE | TimeEntryActivityType | — |
| ACTUAL_DATE | TimeEntryTimeRecordPEOActualDate | ✅ |
| COMMENT_TEXT | TimeEntryCommentText | ✅ |
| CREATED_BY | TimeEntryCreatedBy | ✅ |
| CREATION_DATE | TimeEntryCreationDate | ✅ |
| DATA_SET_ID | TimeEntryDataSetId | — |
| DATE_FROM | TimeEntryDateFrom | ✅ |
| DATE_TO | TimeEntryDateTo | ✅ |
| DELETE_FLAG | TimeEntryDeleteFlag | ✅ |
| ENTERPRISE_ID | TimeEntryEnterpriseId | — |
| LAST_UPDATE_DATE | TimeEntryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TimeEntryLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TimeEntryLastUpdatedBy | ✅ |
| LATEST_VERSION | TimeEntryLatestVersion | ✅ |
| LAYER_CODE | TimeEntryLayerCode | ✅ |
| MEASURE | TimeEntryMeasure | ✅ |
| ORDER_ENTERED | TimeEntryOrderEntered | — |
| ORIG_TM_REC_ID | TimeEntryOriginalTimeRecordId | ✅ |
| ORIG_TM_REC_VERSION | TimeEntryOriginalTimeRecordVersion | ✅ |
| REF_DATE | TimeEntryTimeRecordPEORefDate | ✅ |
| RESOURCE_ID | TimeEntryResourceId | — |
| RESOURCE_TYPE | TimeEntryResourceType | — |
| START_TIME | TimeEntryStartTime | ✅ |
| STOP_TIME | TimeEntryStopTime | ✅ |
| SUBRESOURCE_ID | TimeEntrySubresourceId | — |
| TCSMR_CONFIG_SET_ID | TimeEntryTimeConsumerConfigurationSetId | — |
| TCSMR_SET_ID | TimeEntryTimeConsumerSetId | ✅ |
| TIME_REPORTER_ID | TimeEntryTimeReporterId | ✅ |
| TM_REC_ID | TimeEntryTimeRecordId | ✅ |
| TM_REC_ROW_ID | TimeEntryTimeRecordRowId | — |
| TM_REC_TYPE | TimeEntryTimeRecordType | ✅ |
| TM_REC_VERSION | TimeEntryTimeRecordVersion | ✅ |
| UNIT_OF_MEASURE | TimeEntryUnitOfMeasure | ✅ |
| USER_STATUS | TimeEntryUserStatus | — |

### [[publishedscheduleshiftentrypvo|PublishedScheduleShiftEntryPVO]] (HCM · BICC: 11/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | entryCommentText | — |
| CREATED_BY | entryCreatedBy | ✅ |
| CREATION_DATE | entryCreationDate | ✅ |
| DATE_FROM | entryDateFrom | — |
| DATE_TO | entryDateTo | — |
| DELETE_FLAG | entryDeleteFlag | — |
| LAST_UPDATE_DATE | entryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | entryLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | entryLastUpdatedBy | ✅ |
| LATEST_VERSION | entryLatestVersion | — |
| LAYER_CODE | entryLayerCode | — |
| MEASURE | entryMeasure | ✅ |
| RESOURCE_ID | entryResourceId | ✅ |
| RESOURCE_TYPE | entryResourceType | — |
| START_TIME | entryStartTime | ✅ |
| STOP_TIME | entryStopTime | ✅ |
| SUBRESOURCE_ID | entrySubresourceId | — |
| TCSMR_CONFIG_SET_ID | entryTcsmrConfigSetId | — |
| TCSMR_SET_ID | entryTcsmrSetId | — |
| TIME_REPORTER_ID | entryTimeReporterId | — |
| TM_REC_ID | entryTmRecId | ✅ |
| TM_REC_TYPE | entryTmRecType | — |
| TM_REC_VERSION | entryTmRecVersion | ✅ |
| UNIT_OF_MEASURE | entryUnitOfMeasure | — |

### [[reportedtimeentrypvo|ReportedTimeEntryPVO]] (HCM · BICC: 20/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVITY_EVENT_TIME | TimeEntryActivityEventTime | — |
| ACTIVITY_IN_ID | TimeEntryActivityInId | — |
| ACTIVITY_OUT_ID | TimeEntryActivityOutId | — |
| ACTIVITY_TYPE | TimeEntryActivityType | — |
| COMMENT_TEXT | TimeEntryCommentText | ✅ |
| CREATED_BY | TimeEntryCreatedBy | ✅ |
| CREATION_DATE | TimeEntryCreationDate | ✅ |
| DATA_SET_ID | TimeEntryDataSetId | — |
| DATE_FROM | TimeEntryDateFrom | ✅ |
| DATE_TO | TimeEntryDateTo | ✅ |
| DELETE_FLAG | TimeEntryDeleteFlag | ✅ |
| ENTERPRISE_ID | TimeEntryEnterpriseId | — |
| LAST_UPDATE_DATE | TimeEntryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TimeEntryLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TimeEntryLastUpdatedBy | ✅ |
| LATEST_VERSION | TimeEntryLatestVersion | ✅ |
| LAYER_CODE | TimeEntryLayerCode | ✅ |
| MEASURE | TimeEntryMeasure | ✅ |
| ORDER_ENTERED | TimeEntryOrderEntered | — |
| RESOURCE_ID | TimeEntryResourceId | — |
| RESOURCE_TYPE | TimeEntryResourceType | — |
| START_TIME | TimeEntryStartTime | ✅ |
| STOP_TIME | TimeEntryStopTime | ✅ |
| SUBRESOURCE_ID | TimeEntrySubresourceId | — |
| TCSMR_CONFIG_SET_ID | TimeEntryTimeConsumerConfigurationSetId | — |
| TCSMR_SET_ID | TimeEntryTimeConsumerSetId | ✅ |
| TIME_REPORTER_ID | TimeEntryTimeReporterId | ✅ |
| TM_REC_ID | TimeEntryTimeRecordId | ✅ |
| TM_REC_TYPE | TimeEntryTimeRecordType | ✅ |
| TM_REC_VERSION | TimeEntryTimeRecordVersion | ✅ |
| UNIT_OF_MEASURE | TimeEntryUnitOfMeasure | ✅ |
| USER_STATUS | TimeEntryUserStatus | — |

### [[timerecordextractp1|TimeRecordExtractP1]] (HCM · BICC: 45/45)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVITY_EVENT_TIME | ActivityEventTime | ✅ |
| ACTIVITY_IN_ID | ActivityInId | ✅ |
| ACTIVITY_OUT_ID | ActivityOutId | ✅ |
| ACTIVITY_TYPE | ActivityType | ✅ |
| ACTUAL_DATE | ActualDate | ✅ |
| COMMENT_TEXT | CommentText | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATA_SET_ID | DataSetId | ✅ |
| DATE_FROM | DateFrom | ✅ |
| DATE_TO | DateTo | ✅ |
| DELETE_FLAG | DeleteFlag | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| GRP_TYPE_ID | GrpTypeId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LATEST_VERSION | LatestVersion | ✅ |
| LAYER_CODE | LayerCode | ✅ |
| MEASURE | Measure | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORDER_ENTERED | OrderEntered | ✅ |
| ORIG_TM_REC_ID | OriginalTimeRecordId | ✅ |
| ORIG_TM_REC_VERSION | OriginalTimeRecordVersion | ✅ |
| PART_DATE | PartDate | ✅ |
| REF_DATE | RefDate | ✅ |
| RESOURCE_ID | ResourceId | ✅ |
| RESOURCE_TYPE | ResourceType | ✅ |
| START_GMT_OFFSET | StartGmtOffset | ✅ |
| START_TIME | StartTime | ✅ |
| START_TIMEZONE_CODE | StartTimezoneCode | ✅ |
| STOP_GMT_OFFSET | StopGmtOffset | ✅ |
| STOP_TIME | StopTime | ✅ |
| STOP_TIMEZONE_CODE | StopTimezoneCode | ✅ |
| SUBRESOURCE_ID | SubresourceId | ✅ |
| TCSMR_CONFIG_SET_ID | TimeConsumerConfigurationSetId | ✅ |
| TCSMR_SET_ID | TimeConsumerSetId | ✅ |
| TIME_REPORTER_ID | TimeReporterId | ✅ |
| TM_REC_ID | TimeRecordId | ✅ |
| TM_REC_ROW_ID | TmRecRowId | ✅ |
| TM_REC_TYPE | TimeRecordType | ✅ |
| TM_REC_VERSION | TimeRecordVersion | ✅ |
| UNIT_OF_MEASURE | UnitOfMeasure | ✅ |
| USER_STATUS | UserStatus | ✅ |
| ZONE_TYPE | ZoneType | ✅ |

### [[timerecordpvo|TimeRecordPVO]] (HCM · BICC: 33/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVITY_EVENT_TIME | ActivityEventTime | ✅ |
| ACTIVITY_TYPE | ActivityType | ✅ |
| COMMENT_TEXT | CommentText | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATA_SET_ID | DataSetId | ✅ |
| DATE_FROM | DateFrom | ✅ |
| DATE_TO | DateTo | ✅ |
| DELETE_FLAG | DeleteFlag | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LATEST_VERSION | LatestVersion | ✅ |
| LAYER_CODE | LayerCode | ✅ |
| MEASURE | Measure | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORDER_ENTERED | OrderEntered | ✅ |
| ORIG_TM_REC_ID | OriginalTimeRecordId | ✅ |
| ORIG_TM_REC_VERSION | OriginalTimeRecordVersion | ✅ |
| RESOURCE_ID | ResourceId | ✅ |
| RESOURCE_TYPE | ResourceType | ✅ |
| START_TIME | StartTime | ✅ |
| STOP_TIME | StopTime | ✅ |
| SUBRESOURCE_ID | SubresourceId | ✅ |
| TCSMR_CONFIG_SET_ID | TimeConsumerConfigurationSetId | ✅ |
| TCSMR_SET_ID | TimeConsumerSetId | ✅ |
| TIME_REPORTER_ID | TimeReporterId | ✅ |
| TM_REC_ID | TimeRecordId | ✅ |
| TM_REC_TYPE | TimeRecordType | ✅ |
| TM_REC_VERSION | TimeRecordVersion | ✅ |
| UNIT_OF_MEASURE | UnitOfMeasure | ✅ |
| USER_STATUS | UserStatus | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_TM_REC](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmrec.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
