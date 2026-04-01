---
id: DOC-AP-PVO-HCMApprovalsTaskAttachmentP1
doc_type: system-doc
title: "HCMApprovalsTaskAttachmentP1 — PVO Accounts Payable"
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
  - HCMApprovalsTaskAttachmentP1
  - hcmapprovalstaskattachmentp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HCMApprovalsTaskAttachmentP1

## 📌 Visão Geral

Extrai os anexos vinculados a tarefas de aprovação de transações de RH, incluindo nome do arquivo, tipo e data de upload. Garante rastreabilidade documental nos workflows de aprovação de gestão de pessoas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmApprovalsReportingAM.HCMApprovalsTaskAttachmentP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 7 | 39% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_bpm_task_attachment|FND_BPM_TASK_ATTACHMENT]] — 18 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[fnd_bpm_task_attachment|FND_BPM_TASK_ATTACHMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FndBpmTaskAttachmentPEOAttachedBy | ATTACHED_BY | — | ✅ |
| 2 | FndBpmTaskAttachmentPEOAttachedDate | ATTACHED_DATE | — | ✅ |
| 3 | FndBpmTaskAttachmentPEOAttachmentId | ATTACHMENT_ID | 🔑 | ✅ |
| 4 | FndBpmTaskAttachmentPEOAttachmentName | ATTACHMENT_NAME | — | ✅ |
| 5 | FndBpmTaskAttachmentPEOAttachmentSize | ATTACHMENT_SIZE | — | — |
| 6 | FndBpmTaskAttachmentPEOAttachmentVersion | ATTACHMENT_VERSION | — | ✅ |
| 7 | FndBpmTaskAttachmentPEOCreatedBy | CREATED_BY | — | — |
| 8 | FndBpmTaskAttachmentPEOCreationDate | CREATION_DATE | — | — |
| 9 | FndBpmTaskAttachmentPEODescription | DESCRIPTION | — | — |
| 10 | FndBpmTaskAttachmentPEODomain | DOMAIN | — | — |
| 11 | FndBpmTaskAttachmentPEOEncoding | ENCODING | — | — |
| 12 | FndBpmTaskAttachmentPEOFndAttachmentId | FND_ATTACHMENT_ID | — | ✅ |
| 13 | FndBpmTaskAttachmentPEOInitiatedDate | INITIATED_DATE | — | — |
| 14 | FndBpmTaskAttachmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | FndBpmTaskAttachmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | FndBpmTaskAttachmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | FndBpmTaskAttachmentPEORootTaskId | ROOT_TASK_ID | — | — |
| 18 | FndBpmTaskAttachmentPEOTaskId | TASK_ID | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
