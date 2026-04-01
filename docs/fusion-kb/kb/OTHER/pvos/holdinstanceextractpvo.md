---
id: DOC-OTHER-PVO-HoldInstanceExtractPVO
doc_type: system-doc
title: "HoldInstanceExtractPVO — PVO Cross-Module"
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
  - HoldInstanceExtractPVO
  - holdinstanceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HoldInstanceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Hold Instance Extract. Acessa as tabelas: DOO_HOLD_INSTANCES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.HoldInstanceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 1 | 26 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_hold_instances|DOO_HOLD_INSTANCES]] — 26 atributos (1 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[doo_hold_instances|DOO_HOLD_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HoldInstanceActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | HoldInstanceApplyDate | APPLY_DATE | — | ✅ |
| 3 | HoldInstanceApplySystem | APPLY_SYSTEM | — | ✅ |
| 4 | HoldInstanceApplyUserId | APPLY_USER_ID | — | ✅ |
| 5 | HoldInstanceCreatedBy | CREATED_BY | — | ✅ |
| 6 | HoldInstanceCreationDate | CREATION_DATE | — | ✅ |
| 7 | HoldInstanceDeletedFlag | DELETED_FLAG | — | ✅ |
| 8 | HoldInstanceHoldCodeId | HOLD_CODE_ID | — | ✅ |
| 9 | HoldInstanceHoldComments | HOLD_COMMENTS | — | ✅ |
| 10 | HoldInstanceHoldInstanceId | HOLD_INSTANCE_ID | 🔑 | ✅ |
| 11 | HoldInstanceHoldReleaseComments | HOLD_RELEASE_COMMENTS | — | ✅ |
| 12 | HoldInstanceHoldReleaseReasonCode | HOLD_RELEASE_REASON_CODE | — | ✅ |
| 13 | HoldInstanceHoldRunningTaskFlag | HOLD_RUNNING_TASK_FLAG | — | ✅ |
| 14 | HoldInstanceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | HoldInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | HoldInstanceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | HoldInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | HoldInstanceReleaseDate | RELEASE_DATE | — | ✅ |
| 19 | HoldInstanceReleaseUserId | RELEASE_USER_ID | — | ✅ |
| 20 | HoldInstanceSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 21 | HoldInstanceSourceOrderId | SOURCE_ORDER_ID | — | ✅ |
| 22 | HoldInstanceSourceOrderRevision | SOURCE_ORDER_REVISION | — | ✅ |
| 23 | HoldInstanceSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | ✅ |
| 24 | HoldInstanceSourceRequestId | SOURCE_REQUEST_ID | — | ✅ |
| 25 | HoldInstanceTransactionEntityId1 | TRANSACTION_ENTITY_ID1 | — | ✅ |
| 26 | HoldInstanceTransactionEntityName1 | TRANSACTION_ENTITY_NAME1 | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
