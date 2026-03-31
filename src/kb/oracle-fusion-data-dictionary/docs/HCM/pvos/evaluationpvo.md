---
id: DOC-HCM-PVO-EvaluationPVO
doc_type: system-doc
title: "EvaluationPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
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
  - pvo
  - bicc
aliases:
  - EvaluationPVO
  - evaluationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EvaluationPVO

## 📌 Visão Geral

Disponibiliza avaliações de desempenho com assignment e auditoria. Visão analítica para acompanhamento de ciclos de performance por colaborador.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.EvaluationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hra_evaluations|HRA_EVALUATIONS]] — 17 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[hra_evaluations|HRA_EVALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EvaluationId | EVALUATION_ID | 🔑 | ✅ |
| 4 | EvaluationPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 5 | EvaluationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 6 | EvaluationPEOEndDate | END_DATE | — | ✅ |
| 7 | EvaluationPEOManagerId | MANAGER_ID | — | ✅ |
| 8 | EvaluationPEOStartDate | START_DATE | — | ✅ |
| 9 | EvaluationPEOStatusCode | STATUS_CODE | — | ✅ |
| 10 | EvaluationPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | ✅ |
| 11 | EvaluationPEOTmplPeriodId | TMPL_PERIOD_ID | — | ✅ |
| 12 | EvaluationPEOWorkerComments | WORKER_COMMENTS | — | ✅ |
| 13 | EvaluationPEOWorkerId | WORKER_ID | — | ✅ |
| 14 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
