---
id: DOC-AP-PVO-HCMApprovalsTaskCommentsP1
doc_type: system-doc
title: "HCMApprovalsTaskCommentsP1 — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - HCMApprovalsTaskCommentsP1
  - hcmapprovalstaskcommentsp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HCMApprovalsTaskCommentsP1

## 📌 Visão Geral

Extrai os comentários registrados em tarefas de aprovação de transações de RH, incluindo autor, data e conteúdo. Permite auditar as justificativas e comunicações realizadas durante os fluxos de aprovação de gestão de pessoas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmApprovalsReportingAM.HCMApprovalsTaskCommentsP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 6 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_bpm_task_comment|FND_BPM_TASK_COMMENT]] — 14 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[fnd_bpm_task_comment|FND_BPM_TASK_COMMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FndBpmTaskCommentPEOCommentBy | COMMENT_BY | — | ✅ |
| 2 | FndBpmTaskCommentPEOCommentDate | COMMENT_DATE | — | ✅ |
| 3 | FndBpmTaskCommentPEOCommentId | COMMENT_ID | 🔑 | ✅ |
| 4 | FndBpmTaskCommentPEOCommentText | COMMENT_TEXT | — | ✅ |
| 5 | FndBpmTaskCommentPEOCommentVersion | COMMENT_VERSION | — | ✅ |
| 6 | FndBpmTaskCommentPEOCreatedBy | CREATED_BY | — | — |
| 7 | FndBpmTaskCommentPEOCreationDate | CREATION_DATE | — | — |
| 8 | FndBpmTaskCommentPEODomain | DOMAIN | — | — |
| 9 | FndBpmTaskCommentPEOInitiatedDate | INITIATED_DATE | — | — |
| 10 | FndBpmTaskCommentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | FndBpmTaskCommentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | FndBpmTaskCommentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | FndBpmTaskCommentPEORootTaskId | ROOT_TASK_ID | — | — |
| 14 | FndBpmTaskCommentPEOTaskId | TASK_ID | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
