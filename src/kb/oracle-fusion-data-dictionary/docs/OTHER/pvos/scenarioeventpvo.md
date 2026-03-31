---
id: DOC-OTHER-PVO-ScenarioEventPVO
doc_type: system-doc
title: "ScenarioEventPVO — PVO Cross-Module"
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
  - ScenarioEventPVO
  - scenarioeventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ScenarioEventPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Scenario Event. Acessa as tabelas: CST_SCENARIO_EVENTS, CST_SCENARIO_EVENT_MESSAGES.

**Caminho:** `FscmTopModelAM.ScenariosAM.ScenarioEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 2 | 2 | 18 | 39% |

---

## 🔗 Tabelas Relacionadas

- [[cst_scenario_events|CST_SCENARIO_EVENTS]] — 20 atributos (1 PKs, 12 BICC)
- [[cst_scenario_event_messages|CST_SCENARIO_EVENT_MESSAGES]] — 26 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[cst_scenario_events|CST_SCENARIO_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | ScenarioEventId | SCENARIO_EVENT_ID | 🔑 | ✅ |
| 3 | ScenarioEventPEOCompletedCount | COMPLETED_COUNT | — | ✅ |
| 4 | ScenarioEventPEOCreatedBy | CREATED_BY | — | — |
| 5 | ScenarioEventPEOCreationDate | CREATION_DATE | — | — |
| 6 | ScenarioEventPEOEndTime | END_TIME | — | ✅ |
| 7 | ScenarioEventPEOFailedCount | FAILED_COUNT | — | ✅ |
| 8 | ScenarioEventPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 9 | ScenarioEventPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 10 | ScenarioEventPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ScenarioEventPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ScenarioEventPEOPercentComplete | PERCENT_COMPLETE | — | ✅ |
| 13 | ScenarioEventPEORequestId | REQUEST_ID | — | — |
| 14 | ScenarioEventPEOScenarioEventDate | SCENARIO_EVENT_DATE | — | ✅ |
| 15 | ScenarioEventPEOScenarioEventNumber | SCENARIO_EVENT_NUMBER | — | ✅ |
| 16 | ScenarioEventPEOScenarioEventType | SCENARIO_EVENT_TYPE | — | ✅ |
| 17 | ScenarioEventPEOScenarioId | SCENARIO_ID | — | — |
| 18 | ScenarioEventPEOStartTime | START_TIME | — | ✅ |
| 19 | ScenarioEventPEOStatusCode | STATUS_CODE | — | ✅ |
| 20 | ScenarioEventPEOTotalCount | TOTAL_COUNT | — | ✅ |

### [[cst_scenario_event_messages|CST_SCENARIO_EVENT_MESSAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScenarioEventMessageId | SCENARIO_EVENT_MESSAGE_ID | 🔑 | ✅ |
| 2 | ScenarioEventMessagePEOCreatedBy | CREATED_BY | — | — |
| 3 | ScenarioEventMessagePEOCreationDate | CREATION_DATE | — | — |
| 4 | ScenarioEventMessagePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 5 | ScenarioEventMessagePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 6 | ScenarioEventMessagePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | ScenarioEventMessagePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ScenarioEventMessagePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ScenarioEventMessagePEOMessageName | MESSAGE_NAME | — | ✅ |
| 10 | ScenarioEventMessagePEOMessageText | MESSAGE_TEXT | — | ✅ |
| 11 | ScenarioEventMessagePEOMessageType | MESSAGE_TYPE | — | ✅ |
| 12 | ScenarioEventMessagePEORequestId | REQUEST_ID | — | — |
| 13 | ScenarioEventMessagePEORowCount | ROW_COUNT | — | — |
| 14 | ScenarioEventMessagePEOScenarioEventId | SCENARIO_EVENT_ID | — | — |
| 15 | ScenarioEventMessagePEOToken1Name | TOKEN1_NAME | — | ✅ |
| 16 | ScenarioEventMessagePEOToken1Value | TOKEN1_VALUE | — | ✅ |
| 17 | ScenarioEventMessagePEOToken2Name | TOKEN2_NAME | — | — |
| 18 | ScenarioEventMessagePEOToken2Value | TOKEN2_VALUE | — | — |
| 19 | ScenarioEventMessagePEOToken3Name | TOKEN3_NAME | — | — |
| 20 | ScenarioEventMessagePEOToken3Value | TOKEN3_VALUE | — | — |
| 21 | ScenarioEventMessagePEOToken4Name | TOKEN4_NAME | — | — |
| 22 | ScenarioEventMessagePEOToken4Value | TOKEN4_VALUE | — | — |
| 23 | ScenarioEventMessagePEOToken5Name | TOKEN5_NAME | — | — |
| 24 | ScenarioEventMessagePEOToken5Value | TOKEN5_VALUE | — | — |
| 25 | ScenarioEventMessagePEOToken6Name | TOKEN6_NAME | — | — |
| 26 | ScenarioEventMessagePEOToken6Value | TOKEN6_VALUE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
