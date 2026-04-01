---
id: DOC-OTHER-PVO-ChangeActionsExtractPVO
doc_type: system-doc
title: "ChangeActionsExtractPVO — PVO Cross-Module"
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
  - ChangeActionsExtractPVO
  - changeactionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeActionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Actions Extract. Acessa as tabelas: EGO_CHANGE_ACTIONS_B, EGO_CHANGE_ACTIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.ChangeActionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 1 | 19 | 86% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_actions_b|EGO_CHANGE_ACTIONS_B]] — 19 atributos (1 PKs, 19 BICC)
- [[ego_change_actions_tl|EGO_CHANGE_ACTIONS_TL]] — 3 atributos

---

## ⚙️ Atributos

### [[ego_change_actions_b|EGO_CHANGE_ACTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeActionsBasePEOActionId | ACTION_ID | 🔑 | ✅ |
| 2 | ChangeActionsBasePEOActionType | ACTION_TYPE | — | ✅ |
| 3 | ChangeActionsBasePEOAssigneeId | ASSIGNEE_ID | — | ✅ |
| 4 | ChangeActionsBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | ChangeActionsBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | ChangeActionsBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ChangeActionsBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ChangeActionsBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ChangeActionsBasePEOObjectId1 | OBJECT_ID1 | — | ✅ |
| 10 | ChangeActionsBasePEOObjectId2 | OBJECT_ID2 | — | ✅ |
| 11 | ChangeActionsBasePEOObjectId3 | OBJECT_ID3 | — | ✅ |
| 12 | ChangeActionsBasePEOObjectId4 | OBJECT_ID4 | — | ✅ |
| 13 | ChangeActionsBasePEOObjectId5 | OBJECT_ID5 | — | ✅ |
| 14 | ChangeActionsBasePEOObjectName | OBJECT_NAME | — | ✅ |
| 15 | ChangeActionsBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | ChangeActionsBasePEOParentActionId | PARENT_ACTION_ID | — | ✅ |
| 17 | ChangeActionsBasePEOSourceChangeId | SOURCE_CHANGE_ID | — | ✅ |
| 18 | ChangeActionsBasePEOStatusCode | STATUS_CODE | — | ✅ |
| 19 | ChangeActionsBasePEOTargetChangeId | TARGET_CHANGE_ID | — | ✅ |

### [[ego_change_actions_tl|EGO_CHANGE_ACTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeActionsTranslationPEOActionId | ACTION_ID | — | — |
| 2 | ChangeActionsTranslationPEODescription | DESCRIPTION | — | — |
| 3 | ChangeActionsTranslationPEOLanguage | LANGUAGE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
