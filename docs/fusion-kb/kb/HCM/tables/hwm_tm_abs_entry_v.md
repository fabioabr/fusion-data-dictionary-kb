---
id: DOC-HCM-351
doc_type: system-doc
title: "HWM_TM_ABS_ENTRY_V — Entrada de Ausência em Time Management (View)"
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
  - ausencia
  - entrada
  - view
aliases:
  - HWM_TM_ABS_ENTRY_V
  - hwm_tm_abs_entry_v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_ABS_ENTRY_V

## 📌 Visão Geral

View que apresenta os registros de ausência integrados ao módulo de Time Management, conectando dados de Absence Management com o controle de ponto.

> [!note] Sufixo _V
> O sufixo `_V` indica **view** — objeto somente leitura que consolida dados de uma ou mais tabelas para facilitar consultas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de tempo:** Controle centralizado de registros de horas trabalhadas e ausências.
- **Fluxo de aprovação:** Suporte ao ciclo completo de submissão, aprovação e processamento.
- **Compliance:** Conformidade com políticas internas e regulamentações de jornada de trabalho.
- **Integração:** Conexão com Payroll, Project Costing e Absence Management.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | ABSENCE_ENTRY_ID | NUMBER(18) | NOT NULL | PK | Identificador da entrada de ausência | — | 🟡 80% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Referência à pessoa/trabalhador | PER_ALL_PEOPLE_F | 🟡 80% |
| 3 | ABSENCE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de ausência | ANC_ABSENCE_TYPES_F | 🟡 75% |
| 4 | START_DATE | DATE | NULL | Período | Data de início da ausência | — | 🟡 80% |
| 5 | END_DATE | DATE | NULL | Período | Data de fim da ausência | — | 🟡 80% |
| 6 | DURATION | NUMBER | NULL | Dados | Duração da ausência | — | 🟡 75% |
| 7 | STATUS | VARCHAR2(30) | NULL | Classificação | Status da entrada de ausência | — | 🟡 75% |
| 8 | APPROVAL_STATUS | VARCHAR2(30) | NULL | Classificação | Status de aprovação | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.PERSON_ID, t.START_DATE, t.END_DATE, t.STATUS
FROM   HWM_TM_ABS_ENTRY_V t
WHERE  t.STATUS = 'APPROVED'
```

### Filtros comuns
- `PERSON_ID = :p_person_id` — Filtro por trabalhador

---

## 🔒 Observações

- View somente leitura: não permite INSERT, UPDATE ou DELETE direto.
- Área funcional: Time Management dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[absencetimeentrypvo|AbsenceTimeEntryPVO]] (HCM · BICC: 53/84)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DAY_COMMENT_TEXT | DayCommentText | ✅ |
| DAY_COMMIT_TIMESTAMP | DayCommitTimestamp | — |
| DAY_CREATED_BY | DayCreatedBy | ✅ |
| DAY_CREATION_DATE | DayCreationDate | ✅ |
| DAY_DATA_SET_ID | DayDataSetId | — |
| DAY_DATE_FROM | DayDateFrom | ✅ |
| DAY_DATE_TO | DayDateTo | ✅ |
| DAY_DELETE_FLAG | DayDeleteFlag | ✅ |
| DAY_ENTERPRISE_ID | DayEnterpriseId | — |
| DAY_GRP_TYPE_ID | DayGroupTypeId | ✅ |
| DAY_LAST_UPDATE_DATE | DayLastUpdateDate | ✅ |
| DAY_LAST_UPDATE_LOGIN | DayLastUpdateLogin | ✅ |
| DAY_LAST_UPDATED_BY | DayLastUpdatedBy | ✅ |
| DAY_LATEST_VERSION | DayLatestVersion | ✅ |
| DAY_LAYER_CODE | DayLayerCode | ✅ |
| DAY_ORDER_ENTERED | DayOrderEntered | — |
| DAY_RESOURCE_ID | DayResourceId | — |
| DAY_RESOURCE_TYPE | DayResourceType | — |
| DAY_START_TIME | DayStartTime | ✅ |
| DAY_STOP_TIME | DayStopTime | ✅ |
| DAY_SUBRESOURCE_ID | DaySubresourceId | — |
| DAY_TCSMR_CONFIG_SET_ID | DayTimeConsumerConfigurationSetId | — |
| DAY_TCSMR_SET_ID | DayTimeConsumerSetId | — |
| DAY_TIME_REPORTER_ID | DayTimeReporterId | — |
| DAY_TM_REC_GRP_ID | DayTimeRecordGroupId | ✅ |
| DAY_TM_REC_GRP_VERSION | DayTimeRecordGroupVersion | ✅ |
| DAY_USER_STATUS | DayUserStatus | — |
| RESOURCE_ID | TimeEntryResourceId | — |
| TIME_CARD_COMMENT_TEXT | TimeCardCommentText | ✅ |
| TIME_CARD_COMMIT_TIMESTAMP | TimeCardCommitTimestamp | ✅ |
| TIME_CARD_CREATED_BY | TimeCardCreatedBy | ✅ |
| TIME_CARD_CREATION_DATE | TimeCardCreationDate | ✅ |
| TIME_CARD_DATA_SET_ID | TimeCardDataSetId | — |
| TIME_CARD_DATE_FROM | TimeCardDateFrom | ✅ |
| TIME_CARD_DATE_TO | TimeCardDateTo | ✅ |
| TIME_CARD_DELETE_FLAG | TimeCardDeleteFlag | ✅ |
| TIME_CARD_ENTERPRISE_ID | TimeCardEnterpriseId | — |
| TIME_CARD_GRP_TYPE_ID | TimeCardGroupTypeId | ✅ |
| TIME_CARD_LAST_UPDATE_DATE | TimeCardLastUpdateDate | ✅ |
| TIME_CARD_LAST_UPDATE_LOGIN | TimeCardLastUpdateLogin | ✅ |
| TIME_CARD_LAST_UPDATED_BY | TimeCardLastUpdatedBy | ✅ |
| TIME_CARD_LATEST_VERSION | TimeCardLatestVersion | ✅ |
| TIME_CARD_LAYER_CODE | TimeCardLayerCode | ✅ |
| TIME_CARD_ORDER_ENTERED | TimeCardOrderEntered | — |
| TIME_CARD_RESOURCE_ID | TimeCardResourceId | — |
| TIME_CARD_RESOURCE_TYPE | TimeCardResourceType | — |
| TIME_CARD_START_TIME | TimeCardStartTime | ✅ |
| TIME_CARD_STOP_TIME | TimeCardStopTime | ✅ |
| TIME_CARD_SUBRESOURCE_ID | TimeCardSubresourceId | — |
| TIME_CARD_TCSMR_CONFIG_SET_ID | TimeCardTimeConsumerConfigurationSetId | — |
| TIME_CARD_TCSMR_SET_ID | TimeCardTimeConsumerSetId | — |
| TIME_CARD_TIME_REPORTER_ID | TimeCardTimeReporterId | — |
| TIME_CARD_TM_REC_GRP_ID | TimeCardTimeRecordGroupId | ✅ |
| TIME_CARD_TM_REC_GRP_VERSION | TimeCardTimeRecordGroupVersion | ✅ |
| TIME_CARD_USER_STATUS | TimeCardUserStatus | — |
| TIME_ENTRY_ACTIVITY_EVENT_TIME | TimeEntryActivityEventTime | — |
| TIME_ENTRY_ACTIVITY_TYPE | TimeEntryActivityType | — |
| TIME_ENTRY_COMMENT_TEXT | TimeEntryCommentText | ✅ |
| TIME_ENTRY_CREATED_BY | TimeEntryCreatedBy | ✅ |
| TIME_ENTRY_CREATION_DATE | TimeEntryCreationDate | ✅ |
| TIME_ENTRY_DATA_SET_ID | TimeEntryDataSetId | — |
| TIME_ENTRY_DATE_FROM | TimeEntryDateFrom | ✅ |
| TIME_ENTRY_DATE_TO | TimeEntryDateTo | ✅ |
| TIME_ENTRY_DELETE_FLAG | TimeEntryDeleteFlag | ✅ |
| TIME_ENTRY_ENTERPRISE_ID | TimeEntryEnterpriseId | — |
| TIME_ENTRY_LAST_UPDATE_DATE | TimeEntryLastUpdateDate | ✅ |
| TIME_ENTRY_LAST_UPDATE_LOGIN | TimeEntryLastUpdateLogin | ✅ |
| TIME_ENTRY_LAST_UPDATED_BY | TimeEntryLastUpdatedBy | ✅ |
| TIME_ENTRY_LATEST_VERSION | TimeEntryLatestVersion | ✅ |
| TIME_ENTRY_LAYER_CODE | TimeEntryLayerCode | ✅ |
| TIME_ENTRY_MEASURE | TimeEntryMeasure | ✅ |
| TIME_ENTRY_ORDER_ENTERED | TimeEntryOrderEntered | — |
| TIME_ENTRY_RESOURCE_TYPE | TimeEntryResourceType | — |
| TIME_ENTRY_START_TIME | TimeEntryStartTime | ✅ |
| TIME_ENTRY_STOP_TIME | TimeEntryStopTime | ✅ |
| TIME_ENTRY_SUBRESOURCE_ID | TimeEntrySubresourceId | — |
| TIME_ENTRY_TCSMR_CONFIG_SET_ID | TimeEntryTimeConsumerConfigurationSetId | — |
| TIME_ENTRY_TCSMR_SET_ID | TimeEntryTimeConsumerSetId | ✅ |
| TIME_ENTRY_TIME_REPORTER_ID | TimeEntryTimeReporterId | ✅ |
| TIME_ENTRY_TM_REC_ID | TimeEntryTimeRecordId | ✅ |
| TIME_ENTRY_TM_REC_TYPE | TimeEntryTimeRecordType | ✅ |
| TIME_ENTRY_TM_REC_VERSION | TimeEntryTimeRecordVersion | ✅ |
| TIME_ENTRY_UNIT_OF_MEASURE | TimeEntryUnitOfMeasure | ✅ |
| TIME_ENTRY_USER_STATUS | TimeEntryUserStatus | — |

### [[historicabsencetimeentrypvo|HistoricAbsenceTimeEntryPVO]] (HCM · BICC: 53/84)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DAY_COMMENT_TEXT | DayCommentText | ✅ |
| DAY_COMMIT_TIMESTAMP | DayCommitTimestamp | — |
| DAY_CREATED_BY | DayCreatedBy | ✅ |
| DAY_CREATION_DATE | DayCreationDate | ✅ |
| DAY_DATA_SET_ID | DayDataSetId | — |
| DAY_DATE_FROM | DayDateFrom | ✅ |
| DAY_DATE_TO | DayDateTo | ✅ |
| DAY_DELETE_FLAG | DayDeleteFlag | ✅ |
| DAY_ENTERPRISE_ID | DayEnterpriseId | — |
| DAY_GRP_TYPE_ID | DayGroupTypeId | ✅ |
| DAY_LAST_UPDATE_DATE | DayLastUpdateDate | ✅ |
| DAY_LAST_UPDATE_LOGIN | DayLastUpdateLogin | ✅ |
| DAY_LAST_UPDATED_BY | DayLastUpdatedBy | ✅ |
| DAY_LATEST_VERSION | DayLatestVersion | ✅ |
| DAY_LAYER_CODE | DayLayerCode | ✅ |
| DAY_ORDER_ENTERED | DayOrderEntered | — |
| DAY_RESOURCE_ID | DayResourceId | — |
| DAY_RESOURCE_TYPE | DayResourceType | — |
| DAY_START_TIME | DayStartTime | ✅ |
| DAY_STOP_TIME | DayStopTime | ✅ |
| DAY_SUBRESOURCE_ID | DaySubresourceId | — |
| DAY_TCSMR_CONFIG_SET_ID | DayTimeConsumerConfigurationSetId | — |
| DAY_TCSMR_SET_ID | DayTimeConsumerSetId | — |
| DAY_TIME_REPORTER_ID | DayTimeReporterId | — |
| DAY_TM_REC_GRP_ID | DayTimeRecordGroupId | ✅ |
| DAY_TM_REC_GRP_VERSION | DayTimeRecordGroupVersion | ✅ |
| DAY_USER_STATUS | DayUserStatus | — |
| RESOURCE_ID | TimeEntryResourceId | — |
| TIME_CARD_COMMENT_TEXT | TimeCardCommentText | ✅ |
| TIME_CARD_COMMIT_TIMESTAMP | TimeCardCommitTimestamp | ✅ |
| TIME_CARD_CREATED_BY | TimeCardCreatedBy | ✅ |
| TIME_CARD_CREATION_DATE | TimeCardCreationDate | ✅ |
| TIME_CARD_DATA_SET_ID | TimeCardDataSetId | — |
| TIME_CARD_DATE_FROM | TimeCardDateFrom | ✅ |
| TIME_CARD_DATE_TO | TimeCardDateTo | ✅ |
| TIME_CARD_DELETE_FLAG | TimeCardDeleteFlag | ✅ |
| TIME_CARD_ENTERPRISE_ID | TimeCardEnterpriseId | — |
| TIME_CARD_GRP_TYPE_ID | TimeCardGroupTypeId | ✅ |
| TIME_CARD_LAST_UPDATE_DATE | TimeCardLastUpdateDate | ✅ |
| TIME_CARD_LAST_UPDATE_LOGIN | TimeCardLastUpdateLogin | ✅ |
| TIME_CARD_LAST_UPDATED_BY | TimeCardLastUpdatedBy | ✅ |
| TIME_CARD_LATEST_VERSION | TimeCardLatestVersion | ✅ |
| TIME_CARD_LAYER_CODE | TimeCardLayerCode | ✅ |
| TIME_CARD_ORDER_ENTERED | TimeCardOrderEntered | — |
| TIME_CARD_RESOURCE_ID | TimeCardResourceId | — |
| TIME_CARD_RESOURCE_TYPE | TimeCardResourceType | — |
| TIME_CARD_START_TIME | TimeCardStartTime | ✅ |
| TIME_CARD_STOP_TIME | TimeCardStopTime | ✅ |
| TIME_CARD_SUBRESOURCE_ID | TimeCardSubresourceId | — |
| TIME_CARD_TCSMR_CONFIG_SET_ID | TimeCardTimeConsumerConfigurationSetId | — |
| TIME_CARD_TCSMR_SET_ID | TimeCardTimeConsumerSetId | — |
| TIME_CARD_TIME_REPORTER_ID | TimeCardTimeReporterId | — |
| TIME_CARD_TM_REC_GRP_ID | TimeCardTimeRecordGroupId | ✅ |
| TIME_CARD_TM_REC_GRP_VERSION | TimeCardTimeRecordGroupVersion | ✅ |
| TIME_CARD_USER_STATUS | TimeCardUserStatus | — |
| TIME_ENTRY_ACTIVITY_EVENT_TIME | TimeEntryActivityEventTime | — |
| TIME_ENTRY_ACTIVITY_TYPE | TimeEntryActivityType | — |
| TIME_ENTRY_COMMENT_TEXT | TimeEntryCommentText | ✅ |
| TIME_ENTRY_CREATED_BY | TimeEntryCreatedBy | ✅ |
| TIME_ENTRY_CREATION_DATE | TimeEntryCreationDate | ✅ |
| TIME_ENTRY_DATA_SET_ID | TimeEntryDataSetId | — |
| TIME_ENTRY_DATE_FROM | TimeEntryDateFrom | ✅ |
| TIME_ENTRY_DATE_TO | TimeEntryDateTo | ✅ |
| TIME_ENTRY_DELETE_FLAG | TimeEntryDeleteFlag | ✅ |
| TIME_ENTRY_ENTERPRISE_ID | TimeEntryEnterpriseId | — |
| TIME_ENTRY_LAST_UPDATE_DATE | TimeEntryLastUpdateDate | ✅ |
| TIME_ENTRY_LAST_UPDATE_LOGIN | TimeEntryLastUpdateLogin | ✅ |
| TIME_ENTRY_LAST_UPDATED_BY | TimeEntryLastUpdatedBy | ✅ |
| TIME_ENTRY_LATEST_VERSION | TimeEntryLatestVersion | ✅ |
| TIME_ENTRY_LAYER_CODE | TimeEntryLayerCode | ✅ |
| TIME_ENTRY_MEASURE | TimeEntryMeasure | ✅ |
| TIME_ENTRY_ORDER_ENTERED | TimeEntryOrderEntered | — |
| TIME_ENTRY_RESOURCE_TYPE | TimeEntryResourceType | — |
| TIME_ENTRY_START_TIME | TimeEntryStartTime | ✅ |
| TIME_ENTRY_STOP_TIME | TimeEntryStopTime | ✅ |
| TIME_ENTRY_SUBRESOURCE_ID | TimeEntrySubresourceId | — |
| TIME_ENTRY_TCSMR_CONFIG_SET_ID | TimeEntryTimeConsumerConfigurationSetId | — |
| TIME_ENTRY_TCSMR_SET_ID | TimeEntryTimeConsumerSetId | ✅ |
| TIME_ENTRY_TIME_REPORTER_ID | TimeEntryTimeReporterId | ✅ |
| TIME_ENTRY_TM_REC_ID | TimeEntryTimeRecordId | ✅ |
| TIME_ENTRY_TM_REC_TYPE | TimeEntryTimeRecordType | ✅ |
| TIME_ENTRY_TM_REC_VERSION | TimeEntryTimeRecordVersion | ✅ |
| TIME_ENTRY_UNIT_OF_MEASURE | TimeEntryUnitOfMeasure | ✅ |
| TIME_ENTRY_USER_STATUS | TimeEntryUserStatus | — |

---

## 📚 Referências

- [Oracle Docs — HWM_TM_ABS_ENTRY_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tm_abs_entry_v.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
