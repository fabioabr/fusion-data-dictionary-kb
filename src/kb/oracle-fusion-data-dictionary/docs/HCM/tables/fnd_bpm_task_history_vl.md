---
id: DOC-HCM-114
doc_type: system-doc
title: "FND_BPM_TASK_HISTORY_VL — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - FND_BPM_TASK_HISTORY_VL
  - fnd_bpm_task_history_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_BPM_TASK_HISTORY_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACQUIRED_BY | — | — | — | — | — | — |
| 2 | COMPLETED_DATE | — | — | — | — | — | — |
| 3 | CREATED_BY | — | — | — | — | — | — |
| 4 | CREATION_DATE | — | — | — | — | — | — |
| 5 | DOMAIN | — | — | — | — | — | — |
| 6 | FROM_USER | — | — | — | — | — | — |
| 7 | IDENTIFICATION_KEY | — | — | — | — | — | — |
| 8 | INITIATED_DATE | — | — | — | — | — | — |
| 9 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 10 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 11 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 12 | OUTCOME | — | — | — | — | — | — |
| 13 | OUTCOME_CODE | — | — | — | — | — | — |
| 14 | PARENT_TASK_ID | — | — | — | — | — | — |
| 15 | PARTICIPANT | — | — | — | — | — | — |
| 16 | PARTICIPANT_CODE | — | — | — | — | — | — |
| 17 | ROOT_TASK_ID | — | — | — | — | — | — |
| 18 | STAGE | — | — | — | — | — | — |
| 19 | STAGE_CODE | — | — | — | — | — | — |
| 20 | STATUS_CODE | — | — | — | — | — | — |
| 21 | TASK_ID | — | — | — | — | — | — |
| 22 | TASK_NUMBER | — | — | — | — | — | — |
| 23 | VERSION | — | — | — | — | — | — |
| 24 | VERSION_REASON | — | — | — | — | — | — |
| 25 | WORKFLOWPATTERN_CODE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[hcmapprovalstaskp1|HcmApprovalsTaskP1]] (AP · BICC: 13/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACQUIRED_BY | FndBpmTaskHistoryPEOAcquiredBy | ✅ |
| COMPLETED_DATE | FndBpmTaskHistoryPEOCompletedDate2 | — |
| CREATED_BY | FndBpmTaskHistoryPEOCreatedBy3 | — |
| CREATION_DATE | FndBpmTaskHistoryPEOCreationDate3 | — |
| DOMAIN | FndBpmTaskHistoryPEODomain4 | — |
| FROM_USER | FndBpmTaskHistoryPEOFromUser | ✅ |
| IDENTIFICATION_KEY | FndBpmTaskHistoryPEOIdentificationKey1 | — |
| INITIATED_DATE | FndBpmTaskHistoryPEOInitiatedDate4 | — |
| LAST_UPDATE_DATE | FndBpmTaskHistoryPEOLastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | FndBpmTaskHistoryPEOLastUpdateLogin3 | — |
| LAST_UPDATED_BY | FndBpmTaskHistoryPEOLastUpdatedBy3 | — |
| OUTCOME | FndBpmTaskHistoryPEOOutcome1 | ✅ |
| OUTCOME_CODE | FndBpmTaskHistoryPEOOutcomeCode1 | ✅ |
| PARENT_TASK_ID | FndBpmTaskHistoryPEOParentTaskId1 | — |
| PARTICIPANT | FndBpmTaskHistoryPEOParticipant | ✅ |
| PARTICIPANT_CODE | FndBpmTaskHistoryPEOParticipantCode | ✅ |
| ROOT_TASK_ID | FndBpmTaskHistoryPEORootTaskId3 | — |
| STAGE | FndBpmTaskHistoryPEOStage | ✅ |
| STAGE_CODE | FndBpmTaskHistoryPEOStageCode | ✅ |
| STATUS_CODE | FndBpmTaskHistoryPEOStatusCode1 | ✅ |
| TASK_ID | FndBpmTaskHistoryPEOTaskId4 | — |
| TASK_NUMBER | FndBpmTaskHistoryPEOTaskNumber1 | ✅ |
| VERSION | FndBpmTaskHistoryPEOVersion | ✅ |
| VERSION_REASON | FndBpmTaskHistoryPEOVersionReason | ✅ |
| WORKFLOWPATTERN_CODE | FndBpmTaskHistoryPEOWorkflowpatternCode | — |
