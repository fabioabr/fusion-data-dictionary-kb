---
id: DOC-OTHER-PVO-QaResultActionsExtractPVO
doc_type: system-doc
title: "QaResultActionsExtractPVO — PVO Cross-Module"
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
  - QaResultActionsExtractPVO
  - qaresultactionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QaResultActionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Qa Result Actions Extract. Acessa as tabelas: QA_RESULT_ACTIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.QaResultActionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 1 | 26 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[qa_result_actions|QA_RESULT_ACTIONS]] — 26 atributos (1 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[qa_result_actions|QA_RESULT_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QaResultActionsPEOActionRuleId | ACTION_RULE_ID | — | ✅ |
| 2 | QaResultActionsPEOActionRuleName | ACTION_RULE_NAME | — | ✅ |
| 3 | QaResultActionsPEOActionTaken | ACTION_TAKEN | — | ✅ |
| 4 | QaResultActionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | QaResultActionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | QaResultActionsPEOEmailId | EMAIL_ID | — | ✅ |
| 7 | QaResultActionsPEOIpEventId | IP_EVENT_ID | — | ✅ |
| 8 | QaResultActionsPEOIssueId | ISSUE_ID | — | ✅ |
| 9 | QaResultActionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | QaResultActionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | QaResultActionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | QaResultActionsPEOMaterialStatusLevel | MATERIAL_STATUS_LEVEL | — | ✅ |
| 13 | QaResultActionsPEOMessageName | MESSAGE_NAME | — | ✅ |
| 14 | QaResultActionsPEOMessageText | MESSAGE_TEXT | — | ✅ |
| 15 | QaResultActionsPEOMntConditionCode | MNT_CONDITION_CODE | — | ✅ |
| 16 | QaResultActionsPEONotifier | NOTIFIER | — | ✅ |
| 17 | QaResultActionsPEOResultActionId | RESULT_ACTION_ID | 🔑 | ✅ |
| 18 | QaResultActionsPEOResultEvaluationId | RESULT_EVALUATION_ID | — | ✅ |
| 19 | QaResultActionsPEOSampleId | SAMPLE_ID | — | ✅ |
| 20 | QaResultActionsPEOSampleResultId | SAMPLE_RESULT_ID | — | ✅ |
| 21 | QaResultActionsPEOStatusId | STATUS_ID | — | ✅ |
| 22 | QaResultActionsPEOWorkDefinitionNameId | WORK_DEFINITION_NAME_ID | — | ✅ |
| 23 | QaResultActionsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 24 | QaResultActionsPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | ✅ |
| 25 | QaResultActionsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | ✅ |
| 26 | QaResultActionsPEOWorkOrderType | WORK_ORDER_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
