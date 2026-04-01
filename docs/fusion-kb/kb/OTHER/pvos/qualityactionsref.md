---
id: DOC-OTHER-PVO-QualityActionsRef
doc_type: system-doc
title: "QualityActionsRef — PVO Cross-Module"
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
  - QualityActionsRef
  - qualityactionsref
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualityActionsRef

## 📌 Visão Geral

View Object para extração BICC de dados de Quality Actions Ref. Acessa as tabelas: ENQ_ACTIONS_B, ENQ_ACTIONS_TL, ENQ_ACTION_WORKFLOW_DATES_V.

**Caminho:** `FscmTopModelAM.QualityActionsAnalyticsAM.QualityActionsRef`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 3 | 1 | 35 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[enq_actions_b|ENQ_ACTIONS_B]] — 24 atributos (1 PKs, 24 BICC)
- [[enq_actions_tl|ENQ_ACTIONS_TL]] — 8 atributos (8 BICC)
- [[enq_action_workflow_dates_v|ENQ_ACTION_WORKFLOW_DATES_V]] — 4 atributos (3 BICC)

---

## ⚙️ Atributos

### [[enq_actions_b|ENQ_ACTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionsBasePEOActionAutonumber | ACTION_AUTONUMBER | — | ✅ |
| 2 | ActionsBasePEOActionId | ACTION_ID | 🔑 | ✅ |
| 3 | ActionsBasePEOActionType | ACTION_TYPE | — | ✅ |
| 4 | ActionsBasePEOActualResolutionDate | ACTUAL_RESOLUTION_DATE | — | ✅ |
| 5 | ActionsBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | ActionsBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | ActionsBasePEOCustomerId | CUSTOMER_ID | — | ✅ |
| 8 | ActionsBasePEODateReleased | DATE_RELEASED | — | ✅ |
| 9 | ActionsBasePEODateSubmitted | DATE_SUBMITTED | — | ✅ |
| 10 | ActionsBasePEODisposition | DISPOSITION | — | ✅ |
| 11 | ActionsBasePEOExpectedResolutionDate | EXPECTED_RESOLUTION_DATE | — | ✅ |
| 12 | ActionsBasePEOFinalCompletionDate | FINAL_COMPLETION_DATE | — | ✅ |
| 13 | ActionsBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ActionsBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | ActionsBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ActionsBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | ActionsBasePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 18 | ActionsBasePEOOwner | OWNER | — | ✅ |
| 19 | ActionsBasePEOPriority | PRIORITY | — | ✅ |
| 20 | ActionsBasePEOProductLineId | PRODUCT_LINE_ID | — | ✅ |
| 21 | ActionsBasePEOSource | SOURCE | — | ✅ |
| 22 | ActionsBasePEOStatus | STATUS | — | ✅ |
| 23 | ActionsBasePEOSupplierId | SUPPLIER_ID | — | ✅ |
| 24 | ActionsBasePEOWorkflowId | WORKFLOW_ID | — | ✅ |

### [[enq_actions_tl|ENQ_ACTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionsTranslationPEOActionId | ACTION_ID | — | ✅ |
| 2 | ActionsTranslationPEODescription | DESCRIPTION | — | ✅ |
| 3 | ActionsTranslationPEODispositionComment | DISPOSITION_COMMENT | — | ✅ |
| 4 | ActionsTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | ActionsTranslationPEOName | NAME | — | ✅ |
| 6 | ActionsTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | ActionsTranslationPEOResolutionDescription | RESOLUTION_DESCRIPTION | — | ✅ |
| 8 | ActionsTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[enq_action_workflow_dates_v|ENQ_ACTION_WORKFLOW_DATES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionDatesPEOApprovalWorkflowStartDate | APPROVAL_WORKFLOW_START_DATE | — | ✅ |
| 2 | ActionDatesPEOObjectPk1 | OBJECT_PK1 | — | ✅ |
| 3 | ActionDatesPEOWorkflowCompletiondate | WORKFLOW_END_DATE | — | — |
| 4 | ActionDatesPEOWorkflowStartdate | WORKFLOW_START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
