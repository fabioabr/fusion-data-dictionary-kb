---
id: DOC-HCM-113
doc_type: system-doc
title: "FND_BPM_TASK_COMMENT — (título a preencher)"
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
  - FND_BPM_TASK_COMMENT
  - fnd_bpm_task_comment
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_BPM_TASK_COMMENT

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | COMMENT_BY | — | — | — | — | — | — |
| 2 | COMMENT_DATE | — | — | — | — | — | — |
| 3 | COMMENT_ID | — | — | — | — | — | — |
| 4 | COMMENT_TEXT | — | — | — | — | — | — |
| 5 | COMMENT_VERSION | — | — | — | — | — | — |
| 6 | CREATED_BY | — | — | — | — | — | — |
| 7 | CREATION_DATE | — | — | — | — | — | — |
| 8 | DOMAIN | — | — | — | — | — | — |
| 9 | INITIATED_DATE | — | — | — | — | — | — |
| 10 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 11 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 12 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 13 | ROOT_TASK_ID | — | — | — | — | — | — |
| 14 | TASK_ID | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[hcmapprovalstaskcommentsp1|HCMApprovalsTaskCommentsP1]] (AP · BICC: 6/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_BY | FndBpmTaskCommentPEOCommentBy | ✅ |
| COMMENT_DATE | FndBpmTaskCommentPEOCommentDate | ✅ |
| COMMENT_ID | FndBpmTaskCommentPEOCommentId | ✅ |
| COMMENT_TEXT | FndBpmTaskCommentPEOCommentText | ✅ |
| COMMENT_VERSION | FndBpmTaskCommentPEOCommentVersion | ✅ |
| CREATED_BY | FndBpmTaskCommentPEOCreatedBy | — |
| CREATION_DATE | FndBpmTaskCommentPEOCreationDate | — |
| DOMAIN | FndBpmTaskCommentPEODomain | — |
| INITIATED_DATE | FndBpmTaskCommentPEOInitiatedDate | — |
| LAST_UPDATE_DATE | FndBpmTaskCommentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FndBpmTaskCommentPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | FndBpmTaskCommentPEOLastUpdatedBy | — |
| ROOT_TASK_ID | FndBpmTaskCommentPEORootTaskId | — |
| TASK_ID | FndBpmTaskCommentPEOTaskId | — |
