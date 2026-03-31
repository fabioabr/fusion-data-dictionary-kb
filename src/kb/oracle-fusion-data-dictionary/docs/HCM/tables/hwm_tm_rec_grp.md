---
id: DOC-HCM-382
doc_type: system-doc
title: "HWM_TM_REC_GRP — Grupos de Registros de Time Management"
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
  - record-group
  - grupo-registros
aliases:
  - HWM_TM_REC_GRP
  - hwm_tm_rec_grp
  - hwm-tm-rec-grp
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_REC_GRP

## 📌 Visão Geral

Armazena os **agrupamentos de registros de tempo** (time record groups). Permite organizar registros de tempo em grupos lógicos para processamento em lote.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Processamento em lote:** agrupa registros de tempo para submissão conjunta.
- **Organização:** facilita a gestão de múltiplos registros de tempo.
- **Workflow de aprovação:** permite aprovar grupos inteiros de registros.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REC_GRP_ID | NUMBER(18) | NOT NULL | PK | Identificador único do grupo | — | 🟡 70% |
| 2 | GROUP_NAME | VARCHAR2(240) | NULL | Identificação | Nome do grupo de registros | — | 🟡 60% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do colaborador | PER_ALL_PEOPLE_F | 🟡 70% |
| 4 | GROUP_DATE | DATE | NULL | Período | Data do grupo | — | 🟡 60% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do grupo | — | 🟡 65% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa do grupo de registros de tempo)

### Tabelas-filha (FK de saída)
- [[hwm_tm_rec_grp_usages]] — via `REC_GRP_ID` (usos do grupo de registros de tempo)

---

## 📎 Uso Típico

### Grupos de registros por colaborador
```sql
SELECT g.REC_GRP_ID, g.GROUP_NAME, g.STATUS
FROM   HWM_TM_REC_GRP g
WHERE  g.PERSON_ID = :p_person_id;
```

### Filtros comuns
- `PERSON_ID = :p_person_id — Filtrar por colaborador`
- `STATUS = :p_status — Filtrar por status`

---

## 🔒 Observações

- Tabela de agrupamento para processamento em lote de time records.
- Grupos facilitam a submissão e aprovação de múltiplos registros.

---

## 🔗 PVOs Relacionados

### [[absencetimeentrypvo|AbsenceTimeEntryPVO]] (HCM · BICC: 3/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| GRP_TYPE_ID | AncHeaderGroupTypeId | ✅ |
| TM_REC_GRP_ID | AncHeaderTimeRecordGroupId | ✅ |
| TM_REC_GRP_VERSION | AncHeaderTimeRecordGroupVersion | ✅ |

### [[compliancemessagepvo|ComplianceMessagePVO]] (HCM · BICC: 9/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | TimeRecordGroupPEOCommentText | — |
| COMMIT_TIMESTAMP | TimeRecordGroupPEOCommitTimestamp | ✅ |
| CREATED_BY | TimeRecordGroupPEOCreatedBy | ✅ |
| CREATION_DATE | TimeRecordGroupPEOCreationDate | ✅ |
| DATA_SET_ID | TimeRecordGroupPEODataSetId | — |
| DATE_FROM | TimeRecordGroupPEODateFrom | — |
| DATE_TO | TimeRecordGroupPEODateTo | — |
| DELETE_FLAG | TimeRecordGroupPEODeleteFlag | — |
| ENTERPRISE_ID | TimeRecordGroupPEOEnterpriseId | — |
| GRP_TYPE_ID | TimeRecordGroupPEOGroupTypeId | — |
| LAST_UPDATE_DATE | TimeRecordGroupPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TimeRecordGroupPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TimeRecordGroupPEOLastUpdatedBy | ✅ |
| LATEST_VERSION | TimeRecordGroupPEOLatestVersion | — |
| LAYER_CODE | TimeRecordGroupPEOLayerCode | — |
| LAYER_TM_REC_GRP_ID | TimeRecordGroupPEOLayerTimeRecordGroupId | — |
| LAYER_TM_REC_GRP_VERSION | TimeRecordGroupPEOLayerTimeRecordGroupVersion | — |
| MEASURE | TimeRecordGroupPEOMeasure | — |
| OBJECT_VERSION_NUMBER | TimeRecordGroupPEOObjectVersionNumber | — |
| ORDER_ENTERED | TimeRecordGroupPEOOrderEntered | — |
| ORIG_TM_REC_GRP_ID | TimeRecordGroupPEOOriginalTimeRecordGroupId | — |
| ORIG_TM_REC_GRP_VERSION | TimeRecordGroupPEOOriginalTimeRecordGroupVersion | — |
| PARENT_TM_REC_GRP_ID | TimeRecordGroupPEOParentTimeRecordGroupId | — |
| PARENT_TM_REC_GRP_VERSION | TimeRecordGroupPEOParentTimeRecordGroupVersion | — |
| RESOURCE_ID | TimeRecordGroupPEOResourceId | — |
| RESOURCE_TYPE | TimeRecordGroupPEOResourceType | — |
| START_TIME | TimeRecordGroupPEOStartTime | ✅ |
| STOP_TIME | TimeRecordGroupPEOStopTime | ✅ |
| SUBRESOURCE_ID | TimeRecordGroupPEOSubresourceId | — |
| TCSMR_CONFIG_SET_ID | TimeRecordGroupPEOTimeConsumerConfigurationSetId | — |
| TCSMR_SET_ID | TimeRecordGroupPEOTimeConsumerSetId | — |
| TIME_REPORTER_ID | TimeRecordGroupPEOTimeReporterId | — |
| TM_REC_GRP_ID | TimeRecordGroupPEOTimeRecordGroupId | ✅ |
| TM_REC_GRP_VERSION | TimeRecordGroupPEOTimeRecordGroupVersion | — |
| UNIT_OF_MEASURE | TimeRecordGroupPEOUnitOfMeasure | — |
| USER_STATUS | TimeRecordGroupPEOUserStatus | — |

### [[compliancepvo|CompliancePVO]] (HCM · BICC: 10/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | TimeRecrodGroupPEOCommentText | — |
| COMMIT_TIMESTAMP | TimeRecordGroupPEOCommitTimestamp | ✅ |
| CREATED_BY | TimeRecordGroupPEOCreatedBy | ✅ |
| CREATION_DATE | TimeRecordGroupPEOCreationDate | ✅ |
| DATA_SET_ID | TimeRecordGroupPEODataSetId | — |
| DATE_FROM | TimeRecordGroupPEODateFrom | — |
| DATE_TO | TimeRecordGroupPEODateTo | — |
| DELETE_FLAG | TimeRecordGroupPEODeleteFlag | — |
| ENTERPRISE_ID | TimeRecordGroupPEOEnterpriseId | — |
| GRP_TYPE_ID | TimeRecordGroupPEOGroupTypeId | — |
| LAST_UPDATE_DATE | TimeRecordGroupPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TimeRecordGroupPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TimeRecordGroupPEOLastUpdatedBy | ✅ |
| LATEST_VERSION | TimeRecordGroupPEOLatestVersion | — |
| LAYER_CODE | TimeRecordGroupPEOLayerCode | — |
| LAYER_TM_REC_GRP_ID | TimeRecordGroupPEOLayerTimeRecordGroupId | — |
| LAYER_TM_REC_GRP_VERSION | TimeRecordGroupPEOLayerTimeRecordGroupVersion | — |
| MEASURE | TimeRecordGroupPEOMeasure | — |
| OBJECT_VERSION_NUMBER | TimeRecordGroupPEOObjectVersionNumber | — |
| ORDER_ENTERED | TimeRecordGroupPEOOrderEntered | — |
| ORIG_TM_REC_GRP_ID | TimeRecordGroupPEOOriginalTimeRecordGroupId | — |
| ORIG_TM_REC_GRP_VERSION | TimeRecordGroupPEOOriginalTimeRecordGroupVersion | — |
| PARENT_TM_REC_GRP_ID | TimeRecordGroupPEOParentTimeRecordGroupId | — |
| PARENT_TM_REC_GRP_VERSION | TimeRecordGroupPEOParentTimeRecordGroupVersion | — |
| RESOURCE_ID | TimeRecordGroupPEOResourceId | — |
| RESOURCE_TYPE | TimeRecordGroupPEOResourceType | — |
| START_TIME | TimeRecordGroupPEOStartTime | ✅ |
| STOP_TIME | TimeRecordGroupPEOStopTime | ✅ |
| SUBRESOURCE_ID | TimeRecordGroupPEOSubresourceId | — |
| TCSMR_CONFIG_SET_ID | TimeRecordGroupPEOTimeConsumerConfigurationSetId | — |
| TCSMR_SET_ID | TimeRecordGroupPEOTimeConsumerSetId | — |
| TIME_REPORTER_ID | TimeRecordGroupPEOTimeReporterId | — |
| TM_REC_GRP_ID | TimeRecordGroupPEOTimeRecordGroupId | ✅ |
| TM_REC_GRP_VERSION | TimeRecordGroupPEOTimeRecordGroupVersion | ✅ |
| UNIT_OF_MEASURE | TimeRecordGroupPEOUnitOfMeasure | — |
| USER_STATUS | TimeRecordGroupPEOUserStatus | — |

### [[historicabsencetimeentrypvo|HistoricAbsenceTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| GRP_TYPE_ID | AncHeaderGroupTypeId | — |
| TM_REC_GRP_ID | AncHeaderTimeRecordGroupId | — |
| TM_REC_GRP_VERSION | AncHeaderTimeRecordGroupVersion | — |

### [[historicprocessedtimeentrypvo|HistoricProcessedTimeEntryPVO]] (HCM · BICC: 37/58)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | DayCommentText | ✅ |
| COMMENT_TEXT | TimeCardCommentText | ✅ |
| COMMIT_TIMESTAMP | DayCommitTimestamp | — |
| COMMIT_TIMESTAMP | TimeCardCommitTimestamp | ✅ |
| CREATED_BY | DayCreatedBy | ✅ |
| CREATED_BY | TimeCardCreatedBy | ✅ |
| CREATION_DATE | DayCreationDate | ✅ |
| CREATION_DATE | TimeCardCreationDate | ✅ |
| DATA_SET_ID | DayDataSetId | — |
| DATA_SET_ID | TimeCardDataSetId | — |
| DATE_FROM | DayDateFrom | ✅ |
| DATE_FROM | TimeCardDateFrom | ✅ |
| DATE_TO | DayDateTo | ✅ |
| DATE_TO | TimeCardDateTo | ✅ |
| DELETE_FLAG | DayDeleteFlag | ✅ |
| DELETE_FLAG | TimeCardDeleteFlag | ✅ |
| ENTERPRISE_ID | DayEnterpriseId | — |
| ENTERPRISE_ID | TimeCardEnterpriseId | — |
| GRP_TYPE_ID | DayGroupTypeId | ✅ |
| GRP_TYPE_ID | TimeCardGroupTypeId | ✅ |
| LAST_UPDATE_DATE | DayLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TimeCardLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DayLastUpdateLogin | ✅ |
| LAST_UPDATE_LOGIN | TimeCardLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | DayLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | TimeCardLastUpdatedBy | ✅ |
| LATEST_VERSION | DayLatestVersion | ✅ |
| LATEST_VERSION | TimeCardLatestVersion | ✅ |
| LAYER_CODE | DayLayerCode | ✅ |
| LAYER_CODE | TimeCardLayerCode | ✅ |
| ORDER_ENTERED | DayOrderEntered | — |
| ORDER_ENTERED | TimeCardOrderEntered | — |
| ORIG_TM_REC_GRP_ID | DayOriginalTimeRecordGroupId | ✅ |
| ORIG_TM_REC_GRP_ID | TimeCardOriginalTimeRecordGroupId | ✅ |
| ORIG_TM_REC_GRP_VERSION | DayOriginalTimeRecordGroupVersion | ✅ |
| ORIG_TM_REC_GRP_VERSION | TimeCardOriginalTimeRecordGroupVersion | ✅ |
| RESOURCE_ID | DayResourceId | — |
| RESOURCE_ID | TimeCardResourceId | — |
| RESOURCE_TYPE | DayResourceType | — |
| RESOURCE_TYPE | TimeCardResourceType | — |
| START_TIME | DayStartTime | ✅ |
| START_TIME | TimeCardStartTime | ✅ |
| STOP_TIME | DayStopTime | ✅ |
| STOP_TIME | TimeCardStopTime | ✅ |
| SUBRESOURCE_ID | DaySubresourceId | — |
| SUBRESOURCE_ID | TimeCardSubresourceId | — |
| TCSMR_CONFIG_SET_ID | DayTimeConsumerConfigurationSetId | — |
| TCSMR_CONFIG_SET_ID | TimeCardTimeConsumerConfigurationSetId | — |
| TCSMR_SET_ID | DayTimeConsumerSetId | — |
| TCSMR_SET_ID | TimeCardTimeConsumerSetId | — |
| TIME_REPORTER_ID | DayTimeReporterId | — |
| TIME_REPORTER_ID | TimeCardTimeReporterId | — |
| TM_REC_GRP_ID | DayTimeRecordGroupId | ✅ |
| TM_REC_GRP_ID | TimeCardTimeRecordGroupId | ✅ |
| TM_REC_GRP_VERSION | DayTimeRecordGroupVersion | ✅ |
| TM_REC_GRP_VERSION | TimeCardTimeRecordGroupVersion | ✅ |
| USER_STATUS | DayUserStatus | — |
| USER_STATUS | TimeCardUserStatus | — |

### [[historicreportedtimeentrypvo|HistoricReportedTimeEntryPVO]] (HCM · BICC: 33/54)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | DayCommentText | ✅ |
| COMMENT_TEXT | TimeCardCommentText | ✅ |
| COMMIT_TIMESTAMP | DayCommitTimestamp | — |
| COMMIT_TIMESTAMP | TimeCardCommitTimestamp | ✅ |
| CREATED_BY | DayCreatedBy | ✅ |
| CREATED_BY | TimeCardCreatedBy | ✅ |
| CREATION_DATE | DayCreationDate | ✅ |
| CREATION_DATE | TimeCardCreationDate | ✅ |
| DATA_SET_ID | DayDataSetId | — |
| DATA_SET_ID | TimeCardDataSetId | — |
| DATE_FROM | DayDateFrom | ✅ |
| DATE_FROM | TimeCardDateFrom | ✅ |
| DATE_TO | DayDateTo | ✅ |
| DATE_TO | TimeCardDateTo | ✅ |
| DELETE_FLAG | DayDeleteFlag | ✅ |
| DELETE_FLAG | TimeCardDeleteFlag | ✅ |
| ENTERPRISE_ID | DayEnterpriseId | — |
| ENTERPRISE_ID | TimeCardEnterpriseId | — |
| GRP_TYPE_ID | DayGroupTypeId | ✅ |
| GRP_TYPE_ID | TimeCardGroupTypeId | ✅ |
| LAST_UPDATE_DATE | DayLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TimeCardLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DayLastUpdateLogin | ✅ |
| LAST_UPDATE_LOGIN | TimeCardLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | DayLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | TimeCardLastUpdatedBy | ✅ |
| LATEST_VERSION | DayLatestVersion | ✅ |
| LATEST_VERSION | TimeCardLatestVersion | ✅ |
| LAYER_CODE | DayLayerCode | ✅ |
| LAYER_CODE | TimeCardLayerCode | ✅ |
| ORDER_ENTERED | DayOrderEntered | — |
| ORDER_ENTERED | TimeCardOrderEntered | — |
| RESOURCE_ID | DayResourceId | — |
| RESOURCE_ID | TimeCardResourceId | — |
| RESOURCE_TYPE | DayResourceType | — |
| RESOURCE_TYPE | TimeCardResourceType | — |
| START_TIME | DayStartTime | ✅ |
| START_TIME | TimeCardStartTime | ✅ |
| STOP_TIME | DayStopTime | ✅ |
| STOP_TIME | TimeCardStopTime | ✅ |
| SUBRESOURCE_ID | DaySubresourceId | — |
| SUBRESOURCE_ID | TimeCardSubresourceId | — |
| TCSMR_CONFIG_SET_ID | DayTimeConsumerConfigurationSetId | — |
| TCSMR_CONFIG_SET_ID | TimeCardTimeConsumerConfigurationSetId | — |
| TCSMR_SET_ID | DayTimeConsumerSetId | — |
| TCSMR_SET_ID | TimeCardTimeConsumerSetId | — |
| TIME_REPORTER_ID | DayTimeReporterId | — |
| TIME_REPORTER_ID | TimeCardTimeReporterId | — |
| TM_REC_GRP_ID | DayTimeRecordGroupId | ✅ |
| TM_REC_GRP_ID | TimeCardTimeRecordGroupId | ✅ |
| TM_REC_GRP_VERSION | DayTimeRecordGroupVersion | ✅ |
| TM_REC_GRP_VERSION | TimeCardTimeRecordGroupVersion | ✅ |
| USER_STATUS | DayUserStatus | — |
| USER_STATUS | TimeCardUserStatus | — |

### [[plannedscheduleshiftentrypvo|PlannedScheduleShiftEntryPVO]] (HCM · BICC: 28/75)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | dayCommentText | — |
| COMMENT_TEXT | periodCommentText | — |
| COMMENT_TEXT | shiftCommentText | — |
| COMMIT_TIMESTAMP | dayCommitTimestamp | — |
| COMMIT_TIMESTAMP | periodCommitTimestamp | ✅ |
| COMMIT_TIMESTAMP | shiftCommitTimestamp | — |
| CREATED_BY | dayCreatedBy | ✅ |
| CREATED_BY | periodCreatedBy | ✅ |
| CREATED_BY | shiftCreatedBy | ✅ |
| CREATION_DATE | dayCreationDate | ✅ |
| CREATION_DATE | periodCreationDate | ✅ |
| CREATION_DATE | shiftCreationDate | ✅ |
| DATE_FROM | dayDateFrom | — |
| DATE_FROM | periodDateFrom | — |
| DATE_FROM | shiftDateFrom | — |
| DATE_TO | dayDateTo | — |
| DATE_TO | periodDateTo | — |
| DATE_TO | shiftDateTo | — |
| DELETE_FLAG | dayDeleteFlag | — |
| DELETE_FLAG | periodDeleteFlag | — |
| DELETE_FLAG | shiftDeleteFlag | — |
| GRP_TYPE_ID | dayGroupTypeId | — |
| GRP_TYPE_ID | periodGroupTypeId | — |
| GRP_TYPE_ID | shiftGroupTypeId | — |
| LAST_UPDATE_DATE | dayLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | periodLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | shiftLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | dayLastUpdateLogin | ✅ |
| LAST_UPDATE_LOGIN | periodLastUpdateLogin | ✅ |
| LAST_UPDATE_LOGIN | shiftLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | dayLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | periodLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | shiftLastUpdatedBy | ✅ |
| LATEST_VERSION | dayLatestVersion | — |
| LATEST_VERSION | periodLatestVersion | — |
| LATEST_VERSION | shiftLatestVersion | — |
| LAYER_CODE | dayLayerCode | — |
| LAYER_CODE | periodLayerCode | — |
| LAYER_CODE | shiftLayerCode | — |
| PARENT_TM_REC_GRP_ID | dayParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_ID | periodParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_ID | shiftParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_VERSION | dayParentTmRecGrpVersion | — |
| PARENT_TM_REC_GRP_VERSION | periodParentTmRecGrpVersion | — |
| PARENT_TM_REC_GRP_VERSION | shiftParentTmRecGrpVersion | — |
| RESOURCE_ID | dayResourceId | — |
| RESOURCE_ID | periodResourceId | — |
| RESOURCE_ID | shiftResourceId | — |
| RESOURCE_TYPE | dayResourceType | — |
| RESOURCE_TYPE | periodResourceType | — |
| RESOURCE_TYPE | shiftResourceType | — |
| START_TIME | dayStartTime | ✅ |
| START_TIME | periodStartTime | ✅ |
| START_TIME | shiftStartTime | ✅ |
| STOP_TIME | dayStopTime | ✅ |
| STOP_TIME | periodStopTime | ✅ |
| STOP_TIME | shiftStopTime | ✅ |
| SUBRESOURCE_ID | daySubresourceId | — |
| SUBRESOURCE_ID | periodSubresourceId | — |
| SUBRESOURCE_ID | shiftSubresourceId | — |
| TCSMR_CONFIG_SET_ID | dayTcsmrConfigSetId | — |
| TCSMR_CONFIG_SET_ID | periodTcsmrConfigSetId | — |
| TCSMR_CONFIG_SET_ID | shiftTcsmrConfigSetId | — |
| TCSMR_SET_ID | dayTcsmrSetId | — |
| TCSMR_SET_ID | periodTcsmrSetId | — |
| TCSMR_SET_ID | shiftTcsmrSetId | — |
| TIME_REPORTER_ID | dayTimeReporterId | — |
| TIME_REPORTER_ID | periodTimeReporterId | — |
| TIME_REPORTER_ID | shiftTimeReporterId | — |
| TM_REC_GRP_ID | dayTmRecGrpId | ✅ |
| TM_REC_GRP_ID | periodTmRecGrpId | ✅ |
| TM_REC_GRP_ID | shiftTmRecGrpId | ✅ |
| TM_REC_GRP_VERSION | dayTmRecGrpVersion | ✅ |
| TM_REC_GRP_VERSION | periodTmRecGrpVersion | ✅ |
| TM_REC_GRP_VERSION | shiftTmRecGrpVersion | ✅ |

### [[processedtimeentrypvo|ProcessedTimeEntryPVO]] (HCM · BICC: 37/58)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | DayCommentText | ✅ |
| COMMENT_TEXT | TimeCardCommentText | ✅ |
| COMMIT_TIMESTAMP | DayCommitTimestamp | — |
| COMMIT_TIMESTAMP | TimeCardCommitTimestamp | ✅ |
| CREATED_BY | DayCreatedBy | ✅ |
| CREATED_BY | TimeCardCreatedBy | ✅ |
| CREATION_DATE | DayCreationDate | ✅ |
| CREATION_DATE | TimeCardCreationDate | ✅ |
| DATA_SET_ID | DayDataSetId | — |
| DATA_SET_ID | TimeCardDataSetId | — |
| DATE_FROM | DayDateFrom | ✅ |
| DATE_FROM | TimeCardDateFrom | ✅ |
| DATE_TO | DayDateTo | ✅ |
| DATE_TO | TimeCardDateTo | ✅ |
| DELETE_FLAG | DayDeleteFlag | ✅ |
| DELETE_FLAG | TimeCardDeleteFlag | ✅ |
| ENTERPRISE_ID | DayEnterpriseId | — |
| ENTERPRISE_ID | TimeCardEnterpriseId | — |
| GRP_TYPE_ID | DayGroupTypeId | ✅ |
| GRP_TYPE_ID | TimeCardGroupTypeId | ✅ |
| LAST_UPDATE_DATE | DayLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TimeCardLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DayLastUpdateLogin | ✅ |
| LAST_UPDATE_LOGIN | TimeCardLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | DayLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | TimeCardLastUpdatedBy | ✅ |
| LATEST_VERSION | DayLatestVersion | ✅ |
| LATEST_VERSION | TimeCardLatestVersion | ✅ |
| LAYER_CODE | DayLayerCode | ✅ |
| LAYER_CODE | TimeCardLayerCode | ✅ |
| ORDER_ENTERED | DayOrderEntered | — |
| ORDER_ENTERED | TimeCardOrderEntered | — |
| ORIG_TM_REC_GRP_ID | DayOriginalTimeRecordGroupId | ✅ |
| ORIG_TM_REC_GRP_ID | TimeCardOriginalTimeRecordGroupId | ✅ |
| ORIG_TM_REC_GRP_VERSION | DayOriginalTimeRecordGroupVersion | ✅ |
| ORIG_TM_REC_GRP_VERSION | TimeCardOriginalTimeRecordGroupVersion | ✅ |
| RESOURCE_ID | DayResourceId | — |
| RESOURCE_ID | TimeCardResourceId | — |
| RESOURCE_TYPE | DayResourceType | — |
| RESOURCE_TYPE | TimeCardResourceType | — |
| START_TIME | DayStartTime | ✅ |
| START_TIME | TimeCardStartTime | ✅ |
| STOP_TIME | DayStopTime | ✅ |
| STOP_TIME | TimeCardStopTime | ✅ |
| SUBRESOURCE_ID | DaySubresourceId | — |
| SUBRESOURCE_ID | TimeCardSubresourceId | — |
| TCSMR_CONFIG_SET_ID | DayTimeConsumerConfigurationSetId | — |
| TCSMR_CONFIG_SET_ID | TimeCardTimeConsumerConfigurationSetId | — |
| TCSMR_SET_ID | DayTimeConsumerSetId | — |
| TCSMR_SET_ID | TimeCardTimeConsumerSetId | — |
| TIME_REPORTER_ID | DayTimeReporterId | — |
| TIME_REPORTER_ID | TimeCardTimeReporterId | — |
| TM_REC_GRP_ID | DayTimeRecordGroupId | ✅ |
| TM_REC_GRP_ID | TimeCardTimeRecordGroupId | ✅ |
| TM_REC_GRP_VERSION | DayTimeRecordGroupVersion | ✅ |
| TM_REC_GRP_VERSION | TimeCardTimeRecordGroupVersion | ✅ |
| USER_STATUS | DayUserStatus | — |
| USER_STATUS | TimeCardUserStatus | — |

### [[publishedscheduleshiftentrypvo|PublishedScheduleShiftEntryPVO]] (HCM · BICC: 28/75)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | dayCommentText | — |
| COMMENT_TEXT | periodCommentText | — |
| COMMENT_TEXT | shiftCommentText | — |
| COMMIT_TIMESTAMP | dayCommitTimestamp | — |
| COMMIT_TIMESTAMP | periodCommitTimestamp | ✅ |
| COMMIT_TIMESTAMP | shiftCommitTimestamp | — |
| CREATED_BY | dayCreatedBy | ✅ |
| CREATED_BY | periodCreatedBy | ✅ |
| CREATED_BY | shiftCreatedBy | ✅ |
| CREATION_DATE | dayCreationDate | ✅ |
| CREATION_DATE | periodCreationDate | ✅ |
| CREATION_DATE | shiftCreationDate | ✅ |
| DATE_FROM | dayDateFrom | — |
| DATE_FROM | periodDateFrom | — |
| DATE_FROM | shiftDateFrom | — |
| DATE_TO | dayDateTo | — |
| DATE_TO | periodDateTo | — |
| DATE_TO | shiftDateTo | — |
| DELETE_FLAG | dayDeleteFlag | — |
| DELETE_FLAG | periodDeleteFlag | — |
| DELETE_FLAG | shiftDeleteFlag | — |
| GRP_TYPE_ID | dayGroupTypeId | — |
| GRP_TYPE_ID | periodGroupTypeId | — |
| GRP_TYPE_ID | shiftGroupTypeId | — |
| LAST_UPDATE_DATE | dayLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | periodLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | shiftLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | dayLastUpdateLogin | ✅ |
| LAST_UPDATE_LOGIN | periodLastUpdateLogin | ✅ |
| LAST_UPDATE_LOGIN | shiftLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | dayLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | periodLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | shiftLastUpdatedBy | ✅ |
| LATEST_VERSION | dayLatestVersion | — |
| LATEST_VERSION | periodLatestVersion | — |
| LATEST_VERSION | shiftLatestVersion | — |
| LAYER_CODE | dayLayerCode | — |
| LAYER_CODE | periodLayerCode | — |
| LAYER_CODE | shiftLayerCode | — |
| PARENT_TM_REC_GRP_ID | dayParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_ID | periodParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_ID | shiftParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_VERSION | dayParentTmRecGrpVersion | — |
| PARENT_TM_REC_GRP_VERSION | periodParentTmRecGrpVersion | — |
| PARENT_TM_REC_GRP_VERSION | shiftParentTmRecGrpVersion | — |
| RESOURCE_ID | dayResourceId | — |
| RESOURCE_ID | periodResourceId | — |
| RESOURCE_ID | shiftResourceId | — |
| RESOURCE_TYPE | dayResourceType | — |
| RESOURCE_TYPE | periodResourceType | — |
| RESOURCE_TYPE | shiftResourceType | — |
| START_TIME | dayStartTime | ✅ |
| START_TIME | periodStartTime | ✅ |
| START_TIME | shiftStartTime | ✅ |
| STOP_TIME | dayStopTime | ✅ |
| STOP_TIME | periodStopTime | ✅ |
| STOP_TIME | shiftStopTime | ✅ |
| SUBRESOURCE_ID | daySubresourceId | — |
| SUBRESOURCE_ID | periodSubresourceId | — |
| SUBRESOURCE_ID | shiftSubresourceId | — |
| TCSMR_CONFIG_SET_ID | dayTcsmrConfigSetId | — |
| TCSMR_CONFIG_SET_ID | periodTcsmrConfigSetId | — |
| TCSMR_CONFIG_SET_ID | shiftTcsmrConfigSetId | — |
| TCSMR_SET_ID | dayTcsmrSetId | — |
| TCSMR_SET_ID | periodTcsmrSetId | — |
| TCSMR_SET_ID | shiftTcsmrSetId | — |
| TIME_REPORTER_ID | dayTimeReporterId | — |
| TIME_REPORTER_ID | periodTimeReporterId | — |
| TIME_REPORTER_ID | shiftTimeReporterId | — |
| TM_REC_GRP_ID | dayTmRecGrpId | ✅ |
| TM_REC_GRP_ID | periodTmRecGrpId | ✅ |
| TM_REC_GRP_ID | shiftTmRecGrpId | ✅ |
| TM_REC_GRP_VERSION | dayTmRecGrpVersion | ✅ |
| TM_REC_GRP_VERSION | periodTmRecGrpVersion | ✅ |
| TM_REC_GRP_VERSION | shiftTmRecGrpVersion | ✅ |

### [[reportedtimeentrypvo|ReportedTimeEntryPVO]] (HCM · BICC: 33/54)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | DayCommentText | ✅ |
| COMMENT_TEXT | TimeCardCommentText | ✅ |
| COMMIT_TIMESTAMP | DayCommitTimestamp | — |
| COMMIT_TIMESTAMP | TimeCardCommitTimestamp | ✅ |
| CREATED_BY | DayCreatedBy | ✅ |
| CREATED_BY | TimeCardCreatedBy | ✅ |
| CREATION_DATE | DayCreationDate | ✅ |
| CREATION_DATE | TimeCardCreationDate | ✅ |
| DATA_SET_ID | DayDataSetId | — |
| DATA_SET_ID | TimeCardDataSetId | — |
| DATE_FROM | DayDateFrom | ✅ |
| DATE_FROM | TimeCardDateFrom | ✅ |
| DATE_TO | DayDateTo | ✅ |
| DATE_TO | TimeCardDateTo | ✅ |
| DELETE_FLAG | DayDeleteFlag | ✅ |
| DELETE_FLAG | TimeCardDeleteFlag | ✅ |
| ENTERPRISE_ID | DayEnterpriseId | — |
| ENTERPRISE_ID | TimeCardEnterpriseId | — |
| GRP_TYPE_ID | DayGroupTypeId | ✅ |
| GRP_TYPE_ID | TimeCardGroupTypeId | ✅ |
| LAST_UPDATE_DATE | DayLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TimeCardLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DayLastUpdateLogin | ✅ |
| LAST_UPDATE_LOGIN | TimeCardLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | DayLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | TimeCardLastUpdatedBy | ✅ |
| LATEST_VERSION | DayLatestVersion | ✅ |
| LATEST_VERSION | TimeCardLatestVersion | ✅ |
| LAYER_CODE | DayLayerCode | ✅ |
| LAYER_CODE | TimeCardLayerCode | ✅ |
| ORDER_ENTERED | DayOrderEntered | — |
| ORDER_ENTERED | TimeCardOrderEntered | — |
| RESOURCE_ID | DayResourceId | — |
| RESOURCE_ID | TimeCardResourceId | — |
| RESOURCE_TYPE | DayResourceType | — |
| RESOURCE_TYPE | TimeCardResourceType | — |
| START_TIME | DayStartTime | ✅ |
| START_TIME | TimeCardStartTime | ✅ |
| STOP_TIME | DayStopTime | ✅ |
| STOP_TIME | TimeCardStopTime | ✅ |
| SUBRESOURCE_ID | DaySubresourceId | — |
| SUBRESOURCE_ID | TimeCardSubresourceId | — |
| TCSMR_CONFIG_SET_ID | DayTimeConsumerConfigurationSetId | — |
| TCSMR_CONFIG_SET_ID | TimeCardTimeConsumerConfigurationSetId | — |
| TCSMR_SET_ID | DayTimeConsumerSetId | — |
| TCSMR_SET_ID | TimeCardTimeConsumerSetId | — |
| TIME_REPORTER_ID | DayTimeReporterId | — |
| TIME_REPORTER_ID | TimeCardTimeReporterId | — |
| TM_REC_GRP_ID | DayTimeRecordGroupId | ✅ |
| TM_REC_GRP_ID | TimeCardTimeRecordGroupId | ✅ |
| TM_REC_GRP_VERSION | DayTimeRecordGroupVersion | ✅ |
| TM_REC_GRP_VERSION | TimeCardTimeRecordGroupVersion | ✅ |
| USER_STATUS | DayUserStatus | — |
| USER_STATUS | TimeCardUserStatus | — |

### [[scheduledaypvo|ScheduleDayPVO]] (HCM · BICC: 9/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | DayTimeRecordGroupPEOCommentText | — |
| COMMIT_TIMESTAMP | DayTimeRecordGroupPEOCommitTimestamp | — |
| CREATED_BY | DayTimeRecordGroupPEOCreatedBy | ✅ |
| CREATION_DATE | DayTimeRecordGroupPEOCreationDate | ✅ |
| DATA_SET_ID | DayTimeRecordGroupPEODataSetId | — |
| DATE_FROM | DayTimeRecordGroupPEODateFrom | — |
| DATE_TO | DayTimeRecordGroupPEODateTo | — |
| DELETE_FLAG | DayTimeRecordGroupPEODeleteFlag | — |
| ENTERPRISE_ID | DayTimeRecordGroupPEOEnterpriseId | — |
| GRP_TYPE_ID | DayTimeRecordGroupPEOGroupTypeId | — |
| LAST_UPDATE_DATE | DayTimeRecordGroupPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DayTimeRecordGroupPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | DayTimeRecordGroupPEOLastUpdatedBy | ✅ |
| LATEST_VERSION | DayTimeRecordGroupPEOLatestVersion | — |
| LAYER_CODE | DayTimeRecordGroupPEOLayerCode | — |
| LAYER_TM_REC_GRP_ID | DayTimeRecordGroupPEOLayerTimeRecordGroupId | — |
| LAYER_TM_REC_GRP_VERSION | DayTimeRecordGroupPEOLayerTimeRecordGroupVersion | — |
| MEASURE | DayTimeRecordGroupPEOMeasure | — |
| OBJECT_VERSION_NUMBER | DayTimeRecordGroupPEOObjectVersionNumber | — |
| ORDER_ENTERED | DayTimeRecordGroupPEOOrderEntered | — |
| ORIG_TM_REC_GRP_ID | DayTimeRecordGroupPEOOriginalTimeRecordGroupId | — |
| ORIG_TM_REC_GRP_VERSION | DayTimeRecordGroupPEOOriginalTimeRecordGroupVersion | — |
| PARENT_TM_REC_GRP_ID | DayTimeRecordGroupPEOParentTimeRecordGroupId | — |
| PARENT_TM_REC_GRP_VERSION | DayTimeRecordGroupPEOParentTimeRecordGroupVersion | — |
| RESOURCE_ID | DayTimeRecordGroupPEOResourceId | — |
| RESOURCE_TYPE | DayTimeRecordGroupPEOResourceType | — |
| START_TIME | DayTimeRecordGroupPEOStartTime | ✅ |
| STOP_TIME | DayTimeRecordGroupPEOStopTime | ✅ |
| SUBRESOURCE_ID | DayTimeRecordGroupPEOSubresourceId | — |
| TCSMR_CONFIG_SET_ID | DayTimeRecordGroupPEOTimeConsumerConfigurationSetId | — |
| TCSMR_SET_ID | DayTimeRecordGroupPEOTimeConsumerSetId | — |
| TIME_REPORTER_ID | DayTimeRecordGroupPEOTimeReporterId | — |
| TM_REC_GRP_ID | DayTimeRecordGroupPEOTimeRecordGroupId | ✅ |
| TM_REC_GRP_VERSION | DayTimeRecordGroupPEOTimeRecordGroupVersion | ✅ |
| UNIT_OF_MEASURE | DayTimeRecordGroupPEOUnitOfMeasure | — |
| USER_STATUS | DayTimeRecordGroupPEOUserStatus | — |

### [[timerecordgroupextractp1|TimeRecordGroupExtractP1]] (HCM · BICC: 36/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | CommentText | ✅ |
| COMMIT_TIMESTAMP | CommitTimestamp | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATA_SET_ID | DataSetId | ✅ |
| DATE_FROM | DateFrom | ✅ |
| DATE_TO | DateTo | ✅ |
| DELETE_FLAG | DeleteFlag | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| GRP_TYPE_ID | GroupTypeId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LATEST_VERSION | LatestVersion | ✅ |
| LAYER_CODE | LayerCode | ✅ |
| LAYER_TM_REC_GRP_ID | LayerTimeRecordGroupId | ✅ |
| LAYER_TM_REC_GRP_VERSION | LayerTimeRecordGroupVersion | ✅ |
| MEASURE | Measure | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORDER_ENTERED | OrderEntered | ✅ |
| ORIG_TM_REC_GRP_ID | OriginalTimeRecordGroupId | ✅ |
| ORIG_TM_REC_GRP_VERSION | OriginalTimeRecordGroupVersion | ✅ |
| PARENT_TM_REC_GRP_ID | ParentTimeRecordGroupId | ✅ |
| PARENT_TM_REC_GRP_VERSION | ParentTimeRecordGroupVersion | ✅ |
| RESOURCE_ID | ResourceId | ✅ |
| RESOURCE_TYPE | ResourceType | ✅ |
| START_TIME | StartTime | ✅ |
| STOP_TIME | StopTime | ✅ |
| SUBRESOURCE_ID | SubresourceId | ✅ |
| TCSMR_CONFIG_SET_ID | TimeConsumerConfigurationSetId | ✅ |
| TCSMR_SET_ID | TimeConsumerSetId | ✅ |
| TIME_REPORTER_ID | TimeReporterId | ✅ |
| TM_REC_GRP_ID | TimeRecordGroupId | ✅ |
| TM_REC_GRP_VERSION | TimeRecordGroupVersion | ✅ |
| UNIT_OF_MEASURE | UnitOfMeasure | ✅ |
| USER_STATUS | UserStatus | ✅ |

### [[timerecordgrouppvo|TimeRecordGroupPVO]] (HCM · BICC: 36/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | CommentText | ✅ |
| COMMIT_TIMESTAMP | CommitTimestamp | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATA_SET_ID | DataSetId | ✅ |
| DATE_FROM | DateFrom | ✅ |
| DATE_TO | DateTo | ✅ |
| DELETE_FLAG | DeleteFlag | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| GRP_TYPE_ID | GroupTypeId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LATEST_VERSION | LatestVersion | ✅ |
| LAYER_CODE | LayerCode | ✅ |
| LAYER_TM_REC_GRP_ID | LayerTimeRecordGroupId | ✅ |
| LAYER_TM_REC_GRP_VERSION | LayerTimeRecordGroupVersion | ✅ |
| MEASURE | Measure | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORDER_ENTERED | OrderEntered | ✅ |
| ORIG_TM_REC_GRP_ID | OriginalTimeRecordGroupId | ✅ |
| ORIG_TM_REC_GRP_VERSION | OriginalTimeRecordGroupVersion | ✅ |
| PARENT_TM_REC_GRP_ID | ParentTimeRecordGroupId | ✅ |
| PARENT_TM_REC_GRP_VERSION | ParentTimeRecordGroupVersion | ✅ |
| RESOURCE_ID | ResourceId | ✅ |
| RESOURCE_TYPE | ResourceType | ✅ |
| START_TIME | StartTime | ✅ |
| STOP_TIME | StopTime | ✅ |
| SUBRESOURCE_ID | SubresourceId | ✅ |
| TCSMR_CONFIG_SET_ID | TimeConsumerConfigurationSetId | ✅ |
| TCSMR_SET_ID | TimeConsumerSetId | ✅ |
| TIME_REPORTER_ID | TimeReporterId | ✅ |
| TM_REC_GRP_ID | TimeRecordGroupId | ✅ |
| TM_REC_GRP_VERSION | TimeRecordGroupVersion | ✅ |
| UNIT_OF_MEASURE | UnitOfMeasure | ✅ |
| USER_STATUS | UserStatus | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_TM_REC_GRP](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmrecgrp.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
