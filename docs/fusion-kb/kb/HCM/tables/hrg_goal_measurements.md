---
id: DOC-HCM-168
doc_type: system-doc
title: "HRG_GOAL_MEASUREMENTS — Métricas de Objetivos"
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
  - goals
  - measurements
aliases:
  - HRG_GOAL_MEASUREMENTS
  - hrg_goal_measurements
  - métricas-de-objetivos
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRG_GOAL_MEASUREMENTS

## 📌 Visão Geral

Armazena **métricas e indicadores** de objetivos. Valores-alvo, atuais e unidades de medida.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Mensuração:** Critérios quantitativos de progresso.
- **KPIs individuais:** Indicadores por meta.
- **Acompanhamento automatizado:** Progresso numérico.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GOAL_MEASUREMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | GOAL_ID | NUMBER(18) | NOT NULL | FK | Objetivo | [[hrg_goals]] | 🟢 90% |
| 3 | MEASUREMENT_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome da métrica | — | 🟡 80% |
| 4 | TARGET_VALUE | NUMBER | NULL | Métrica | Valor-alvo | — | 🟡 80% |
| 5 | ACTUAL_VALUE | NUMBER | NULL | Métrica | Valor atual | — | 🟡 80% |
| 6 | UOM_CODE | VARCHAR2(30) | NULL | Classificação | Unidade de medida | — | 🟡 70% |
| 7 | START_DATE | DATE | NULL | Data | Início | — | 🟡 75% |
| 8 | TARGET_DATE | DATE | NULL | Data | Data-alvo | — | 🟡 75% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrg_goals]] — via `GOAL_ID` (meta da medicao de progresso)

---

## 📎 Uso Típico

### Métricas e progresso
```sql
SELECT m.MEASUREMENT_NAME, m.TARGET_VALUE, m.ACTUAL_VALUE,
       ROUND(m.ACTUAL_VALUE/NULLIF(m.TARGET_VALUE,0)*100,1) AS pct
FROM   HRG_GOAL_MEASUREMENTS m
WHERE  m.GOAL_ID = :p_goal_id;
```

---

## 🔒 Observações

- Múltiplas métricas por objetivo.
- Progresso = `ACTUAL_VALUE / TARGET_VALUE * 100`.

---

## 🔗 PVOs Relacionados

### [[careerdevgoalpvo|CareerDevGoalPVO]] (HCM · BICC: 15/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue_1 | — |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId2_1 | — |
| COMMENTS | MeasurementPEOComments1_1 | ✅ |
| CREATED_BY | MeasurementPEOCreatedBy2_1 | — |
| CREATION_DATE | MeasurementPEOCreationDate2_1 | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | ✅ |
| END_DATE | MeasurementPEOEndDate | ✅ |
| GOAL_ID | MeasurementPEOGoalId3_1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate2_1 | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin2_1 | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy2_1 | — |
| MAX_TARGET | MeasurementPEOMaxTarget | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode_1 | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | ✅ |
| MIN_TARGET | MeasurementPEOMinTarget | ✅ |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber2_1 | — |
| START_DATE | MeasurementPEOStartDate1_1 | ✅ |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | ✅ |
| TARGET_TYPE | MeasurementPEOTargetType | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | ✅ |
| UOM_CODE | MeasurementPEOUomCode_1 | — |

### [[careerdevgoalpvoviewall|CareerDevGoalPVOViewAll]] (HCM · BICC: 15/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue_1 | — |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId2_1 | — |
| COMMENTS | MeasurementPEOComments1_1 | ✅ |
| CREATED_BY | MeasurementPEOCreatedBy2_1 | — |
| CREATION_DATE | MeasurementPEOCreationDate2_1 | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | ✅ |
| END_DATE | MeasurementPEOEndDate | ✅ |
| GOAL_ID | MeasurementPEOGoalId3_1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate2_1 | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin2_1 | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy2_1 | — |
| MAX_TARGET | MeasurementPEOMaxTarget | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode_1 | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | ✅ |
| MIN_TARGET | MeasurementPEOMinTarget | ✅ |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber2_1 | — |
| START_DATE | MeasurementPEOStartDate1_1 | ✅ |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | ✅ |
| TARGET_TYPE | MeasurementPEOTargetType | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | ✅ |
| UOM_CODE | MeasurementPEOUomCode_1 | — |

### [[careerdevgoalversionpvo|CareerDevGoalVersionPVO]] (HCM · BICC: 15/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue_1 | — |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId2_1 | — |
| COMMENTS | MeasurementPEOComments1_1 | ✅ |
| CREATED_BY | MeasurementPEOCreatedBy2_1 | — |
| CREATION_DATE | MeasurementPEOCreationDate2_1 | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | ✅ |
| END_DATE | MeasurementPEOEndDate | ✅ |
| GOAL_ID | MeasurementPEOGoalId3_1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate2_1 | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin2_1 | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy2_1 | — |
| MAX_TARGET | MeasurementPEOMaxTarget | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode_1 | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | ✅ |
| MIN_TARGET | MeasurementPEOMinTarget | ✅ |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber2_1 | — |
| START_DATE | MeasurementPEOStartDate1_1 | ✅ |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | ✅ |
| TARGET_TYPE | MeasurementPEOTargetType | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | ✅ |
| UOM_CODE | MeasurementPEOUomCode_1 | — |

### [[careerdevgoalversionpvoviewall|CareerDevGoalVersionPVOViewAll]] (HCM · BICC: 15/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue_1 | — |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId2_1 | — |
| COMMENTS | MeasurementPEOComments1_1 | ✅ |
| CREATED_BY | MeasurementPEOCreatedBy2_1 | — |
| CREATION_DATE | MeasurementPEOCreationDate2_1 | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | ✅ |
| END_DATE | MeasurementPEOEndDate | ✅ |
| GOAL_ID | MeasurementPEOGoalId3_1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate2_1 | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin2_1 | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy2_1 | — |
| MAX_TARGET | MeasurementPEOMaxTarget | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode_1 | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | ✅ |
| MIN_TARGET | MeasurementPEOMinTarget | ✅ |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber2_1 | — |
| START_DATE | MeasurementPEOStartDate1_1 | ✅ |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | ✅ |
| TARGET_TYPE | MeasurementPEOTargetType | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | ✅ |
| UOM_CODE | MeasurementPEOUomCode_1 | — |

### [[careerdevpvo|CareerDevPVO]] (HCM · BICC: 3/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | — |
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight_1 | — |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId | — |
| COMMENTS | MeasurementPEOComments | — |
| CREATED_BY | MeasurementPEOCreatedBy | — |
| CREATION_DATE | MeasurementPEOCreationDate | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | — |
| END_DATE | MeasurementPEOEndDate | — |
| GOAL_ID | MeasurementPEOGoalId1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy | — |
| MAX_TARGET | MeasurementPEOMaxTarget | — |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | — |
| MIN_TARGET | MeasurementPEOMinTarget | — |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber | — |
| START_DATE | MeasurementPEOStartDate | — |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | — |
| TARGET_TYPE | MeasurementPEOTargetType | — |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | — |

### [[careerdevversionpvo|CareerDevVersionPVO]] (HCM · BICC: 3/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | — |
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight_1 | — |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId | — |
| COMMENTS | MeasurementPEOComments | — |
| CREATED_BY | MeasurementPEOCreatedBy | — |
| CREATION_DATE | MeasurementPEOCreationDate | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | — |
| END_DATE | MeasurementPEOEndDate | — |
| GOAL_ID | MeasurementPEOGoalId1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy | — |
| MAX_TARGET | MeasurementPEOMaxTarget | — |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | — |
| MIN_TARGET | MeasurementPEOMinTarget | — |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber | — |
| START_DATE | MeasurementPEOStartDate | — |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | — |
| TARGET_TYPE | MeasurementPEOTargetType | — |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | — |

### [[developmentgoalpvo|DevelopmentGoalPVO]] (HCM · BICC: 15/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue_1 | — |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId2_1 | — |
| COMMENTS | MeasurementPEOComments1_1 | ✅ |
| CREATED_BY | MeasurementPEOCreatedBy2_1 | — |
| CREATION_DATE | MeasurementPEOCreationDate2_1 | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | ✅ |
| END_DATE | MeasurementPEOEndDate | ✅ |
| GOAL_ID | MeasurementPEOGoalId3_1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate2_1 | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin2_1 | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy2_1 | — |
| MAX_TARGET | MeasurementPEOMaxTarget | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode_1 | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | ✅ |
| MIN_TARGET | MeasurementPEOMinTarget | ✅ |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber2_1 | — |
| START_DATE | MeasurementPEOStartDate1_1 | ✅ |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | ✅ |
| TARGET_TYPE | MeasurementPEOTargetType | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | ✅ |
| UOM_CODE | MeasurementPEOUomCode_1 | — |

### [[developmentgoalpvoviewall|DevelopmentGoalPVOViewAll]] (HCM · BICC: 15/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue_1 | — |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId2_1 | — |
| COMMENTS | MeasurementPEOComments1_1 | ✅ |
| CREATED_BY | MeasurementPEOCreatedBy2_1 | — |
| CREATION_DATE | MeasurementPEOCreationDate2_1 | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | ✅ |
| END_DATE | MeasurementPEOEndDate | ✅ |
| GOAL_ID | MeasurementPEOGoalId3_1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate2_1 | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin2_1 | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy2_1 | — |
| MAX_TARGET | MeasurementPEOMaxTarget | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode_1 | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | ✅ |
| MIN_TARGET | MeasurementPEOMinTarget | ✅ |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber2_1 | — |
| START_DATE | MeasurementPEOStartDate1_1 | ✅ |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | ✅ |
| TARGET_TYPE | MeasurementPEOTargetType | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | ✅ |
| UOM_CODE | MeasurementPEOUomCode_1 | — |

### [[goalitempvo|GoalItemPVO]] (HCM · BICC: 8/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE | GoalPEOActualValue | ✅ |
| COMMENTS | GoalPEOMeasureComments | ✅ |
| DISPLAY_SEQUENCE | DisplaySequence | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate | ✅ |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | ✅ |
| MEASUREMENT_ID | MeasurementId | — |
| MEASUREMENT_NAME | GoalPEOMeasureName | ✅ |
| TARGET_TYPE | GoalPEOTargetType | ✅ |
| TARGET_VALUE | GoalPEOTargetValue | ✅ |
| UOM_CODE | GoalPEOUomCode | ✅ |

### [[goalmeasurementextractpvo|GoalMeasurementExtractPVO]] (HCM · BICC: 23/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | AchievedWeight | ✅ |
| ACTUAL_VALUE | ActualValue | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| COMMENTS | Comments | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DISPLAY_SEQUENCE | DisplaySequence | ✅ |
| END_DATE | EndDate | ✅ |
| GOAL_ID | GoalId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MAX_TARGET | MaxTarget | ✅ |
| MEASURE_TYPE_CODE | MeasureTypeCode | ✅ |
| MEASUREMENT_ID | MeasurementId | ✅ |
| MEASUREMENT_NAME | MeasurementName | ✅ |
| MIN_TARGET | MinTarget | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| START_DATE | StartDate | ✅ |
| TARGET_PERCENTAGE | TargetPercentage | ✅ |
| TARGET_TYPE | TargetType | ✅ |
| TARGET_VALUE | TargetValue | ✅ |
| UOM_CODE | UomCode | ✅ |

### [[goalppvo1|GoalPPVO1]] (HCM · BICC: 8/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | — |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue_1 | — |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId2_1 | — |
| COMMENTS | MeasurementPEOComments1_1 | ✅ |
| CREATED_BY | MeasurementPEOCreatedBy2_1 | — |
| CREATION_DATE | MeasurementPEOCreationDate2_1 | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | — |
| END_DATE | MeasurementPEOEndDate | — |
| GOAL_ID | MeasurementPEOGoalId3_1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate2_1 | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin2_1 | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy2_1 | — |
| MAX_TARGET | MeasurementPEOMaxTarget | — |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode_1 | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | ✅ |
| MIN_TARGET | MeasurementPEOMinTarget | — |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber2_1 | — |
| START_DATE | MeasurementPEOStartDate1_1 | — |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | — |
| TARGET_TYPE | MeasurementPEOTargetType | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | ✅ |
| UOM_CODE | MeasurementPEOUomCode_1 | — |

### [[goalpvo_copy|GoalPVO_Copy]] (HCM · BICC: 1/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | — |
| ACTUAL_VALUE | MeasurementPEOActualValue | — |
| ACTUAL_VALUE | MeasurementPEOActualValue_1 | — |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId2_1 | — |
| COMMENTS | MeasurementPEOComments1_1 | — |
| CREATED_BY | MeasurementPEOCreatedBy2_1 | — |
| CREATION_DATE | MeasurementPEOCreationDate2_1 | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | — |
| END_DATE | MeasurementPEOEndDate | — |
| GOAL_ID | MeasurementPEOGoalId3_1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate2_1 | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin2_1 | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy2_1 | — |
| MAX_TARGET | MeasurementPEOMaxTarget | — |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | — |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode_1 | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | — |
| MIN_TARGET | MeasurementPEOMinTarget | — |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber2_1 | — |
| START_DATE | MeasurementPEOStartDate1_1 | — |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | — |
| TARGET_TYPE | MeasurementPEOTargetType | — |
| TARGET_VALUE | MeasurementPEOTargetValue | — |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | — |
| UOM_CODE | MeasurementPEOUomCode_1 | — |

### [[goalstatusoverviewpvo|GoalStatusOverviewPVO]] (HCM · BICC: 8/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | — |
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight_1 | — |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId | — |
| COMMENTS | MeasurementPEOComments | ✅ |
| CREATED_BY | MeasurementPEOCreatedBy | — |
| CREATION_DATE | MeasurementPEOCreationDate | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | — |
| END_DATE | MeasurementPEOEndDate | — |
| GOAL_ID | MeasurementPEOGoalId1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy | — |
| MAX_TARGET | MeasurementPEOMaxTarget | — |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | ✅ |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | ✅ |
| MIN_TARGET | MeasurementPEOMinTarget | — |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber | — |
| START_DATE | MeasurementPEOStartDate | — |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | — |
| TARGET_TYPE | MeasurementPEOTargetType | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | ✅ |

### [[goalversionstatusoverviewpvo|GoalVersionStatusOverviewPVO]] (HCM · BICC: 8/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | — |
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight_1 | — |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId | — |
| COMMENTS | MeasurementPEOComments | ✅ |
| CREATED_BY | MeasurementPEOCreatedBy | — |
| CREATION_DATE | MeasurementPEOCreationDate | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | — |
| END_DATE | MeasurementPEOEndDate | — |
| GOAL_ID | MeasurementPEOGoalId1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy | — |
| MAX_TARGET | MeasurementPEOMaxTarget | — |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | ✅ |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | ✅ |
| MIN_TARGET | MeasurementPEOMinTarget | — |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber | — |
| START_DATE | MeasurementPEOStartDate | — |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | — |
| TARGET_TYPE | MeasurementPEOTargetType | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | ✅ |

### [[organizationgoalpvo|OrganizationGoalPVO]] (HCM · BICC: 7/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | — |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId3 | — |
| COMMENTS | MeasurementPEOComments | ✅ |
| CREATED_BY | MeasurementPEOCreatedBy3 | — |
| CREATION_DATE | MeasurementPEOCreationDate3 | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | — |
| END_DATE | MeasurementPEOEndDate | — |
| GOAL_ID | MeasurementPEOGoalId2 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate3 | — |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin3 | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy3 | — |
| MAX_TARGET | MeasurementPEOMaxTarget | — |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | ✅ |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | ✅ |
| MIN_TARGET | MeasurementPEOMinTarget | — |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber2 | — |
| START_DATE | MeasurementPEOStartDate | — |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | — |
| TARGET_TYPE | MeasurementPEOTargetType | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| UOM_CODE | MeasurementPEOUomCode | ✅ |

### [[performancegoalpvo|PerformanceGoalPVO]] (HCM · BICC: 15/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue_1 | — |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId2_1 | — |
| COMMENTS | MeasurementPEOComments1_1 | ✅ |
| CREATED_BY | MeasurementPEOCreatedBy2_1 | — |
| CREATION_DATE | MeasurementPEOCreationDate2_1 | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | ✅ |
| END_DATE | MeasurementPEOEndDate | ✅ |
| GOAL_ID | MeasurementPEOGoalId3_1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate2_1 | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin2_1 | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy2_1 | — |
| MAX_TARGET | MeasurementPEOMaxTarget | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode_1 | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | ✅ |
| MIN_TARGET | MeasurementPEOMinTarget | ✅ |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber2_1 | — |
| START_DATE | MeasurementPEOStartDate1_1 | ✅ |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | ✅ |
| TARGET_TYPE | MeasurementPEOTargetType | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | ✅ |
| UOM_CODE | MeasurementPEOUomCode_1 | — |

### [[performancegoalpvoviewall|PerformanceGoalPVOViewAll]] (HCM · BICC: 15/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue_1 | — |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId2_1 | — |
| COMMENTS | MeasurementPEOComments1_1 | ✅ |
| CREATED_BY | MeasurementPEOCreatedBy2_1 | — |
| CREATION_DATE | MeasurementPEOCreationDate2_1 | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | ✅ |
| END_DATE | MeasurementPEOEndDate | ✅ |
| GOAL_ID | MeasurementPEOGoalId3_1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate2_1 | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin2_1 | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy2_1 | — |
| MAX_TARGET | MeasurementPEOMaxTarget | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode_1 | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | ✅ |
| MIN_TARGET | MeasurementPEOMinTarget | ✅ |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber2_1 | — |
| START_DATE | MeasurementPEOStartDate1_1 | ✅ |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | ✅ |
| TARGET_TYPE | MeasurementPEOTargetType | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | ✅ |
| UOM_CODE | MeasurementPEOUomCode_1 | — |

### [[performancegoalversionpvo|PerformanceGoalVersionPVO]] (HCM · BICC: 15/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue_1 | — |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId2_1 | — |
| COMMENTS | MeasurementPEOComments1_1 | ✅ |
| CREATED_BY | MeasurementPEOCreatedBy2_1 | — |
| CREATION_DATE | MeasurementPEOCreationDate2_1 | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | ✅ |
| END_DATE | MeasurementPEOEndDate | ✅ |
| GOAL_ID | MeasurementPEOGoalId3_1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate2_1 | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin2_1 | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy2_1 | — |
| MAX_TARGET | MeasurementPEOMaxTarget | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode_1 | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | ✅ |
| MIN_TARGET | MeasurementPEOMinTarget | ✅ |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber2_1 | — |
| START_DATE | MeasurementPEOStartDate1_1 | ✅ |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | ✅ |
| TARGET_TYPE | MeasurementPEOTargetType | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | ✅ |
| UOM_CODE | MeasurementPEOUomCode_1 | — |

### [[performancegoalversionpvoviewall|PerformanceGoalVersionPVOViewAll]] (HCM · BICC: 15/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue | ✅ |
| ACTUAL_VALUE | MeasurementPEOActualValue_1 | — |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId2_1 | — |
| COMMENTS | MeasurementPEOComments1_1 | ✅ |
| CREATED_BY | MeasurementPEOCreatedBy2_1 | — |
| CREATION_DATE | MeasurementPEOCreationDate2_1 | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | ✅ |
| END_DATE | MeasurementPEOEndDate | ✅ |
| GOAL_ID | MeasurementPEOGoalId3_1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate2_1 | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin2_1 | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy2_1 | — |
| MAX_TARGET | MeasurementPEOMaxTarget | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | ✅ |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode_1 | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | ✅ |
| MIN_TARGET | MeasurementPEOMinTarget | ✅ |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber2_1 | — |
| START_DATE | MeasurementPEOStartDate1_1 | ✅ |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | ✅ |
| TARGET_TYPE | MeasurementPEOTargetType | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue | ✅ |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | ✅ |
| UOM_CODE | MeasurementPEOUomCode_1 | — |

### [[personalgoalpvo|PersonalGoalPVO]] (HCM · BICC: 1/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVED_WEIGHT | MeasurementPEOAchievedWeight | — |
| ACTUAL_VALUE | MeasurementPEOActualValue | — |
| ACTUAL_VALUE | MeasurementPEOActualValue_1 | — |
| BUSINESS_GROUP_ID | MeasurementPEOBusinessGroupId2_1 | — |
| COMMENTS | MeasurementPEOComments1_1 | — |
| CREATED_BY | MeasurementPEOCreatedBy2_1 | — |
| CREATION_DATE | MeasurementPEOCreationDate2_1 | — |
| DISPLAY_SEQUENCE | MeasurementPEODisplaySequence | — |
| END_DATE | MeasurementPEOEndDate | — |
| GOAL_ID | MeasurementPEOGoalId3_1 | — |
| LAST_UPDATE_DATE | MeasurementPEOLastUpdateDate2_1 | ✅ |
| LAST_UPDATE_LOGIN | MeasurementPEOLastUpdateLogin2_1 | — |
| LAST_UPDATED_BY | MeasurementPEOLastUpdatedBy2_1 | — |
| MAX_TARGET | MeasurementPEOMaxTarget | — |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode | — |
| MEASURE_TYPE_CODE | MeasurementPEOMeasureTypeCode_1 | — |
| MEASUREMENT_ID | MeasurementPEOMeasurementId | — |
| MEASUREMENT_NAME | MeasurementPEOMeasurementName | — |
| MIN_TARGET | MeasurementPEOMinTarget | — |
| OBJECT_VERSION_NUMBER | MeasurementPEOObjectVersionNumber2_1 | — |
| START_DATE | MeasurementPEOStartDate1_1 | — |
| TARGET_PERCENTAGE | MeasurementPEOTargetPercentage | — |
| TARGET_TYPE | MeasurementPEOTargetType | — |
| TARGET_VALUE | MeasurementPEOTargetValue | — |
| TARGET_VALUE | MeasurementPEOTargetValue_1 | — |
| UOM_CODE | MeasurementPEOUomCode | — |
| UOM_CODE | MeasurementPEOUomCode_1 | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
