---
id: DOC-OTHER-PVO-WorkflowStatus
doc_type: system-doc
title: "WorkflowStatus — PVO Cross-Module"
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
  - WorkflowStatus
  - workflowstatus
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkflowStatus

## 📌 Visão Geral

View Object para extração BICC de dados de Workflow Status. Acessa as tabelas: ENQ_WORKFLOW_OTBI_VL.

**Caminho:** `FscmTopModelAM.QualityCommonAnalyticsAM.WorkflowStatus`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 1 | 8 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[enq_workflow_otbi_vl|ENQ_WORKFLOW_OTBI_VL]] — 8 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[enq_workflow_otbi_vl|ENQ_WORKFLOW_OTBI_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkflowStatusOtbiPEOName | NAME | — | ✅ |
| 2 | WorkflowStatusOtbiPEOObjectCode | OBJECT_CODE | — | ✅ |
| 3 | WorkflowStatusOtbiPEOObjectPk1 | OBJECT_PK1 | 🔑 | ✅ |
| 4 | WorkflowStatusOtbiPEOStatusName | STATUS_NAME | — | ✅ |
| 5 | WorkflowStatusOtbiPEOStatusType | STATUS_TYPE | — | ✅ |
| 6 | WorkflowStatusOtbiPEOStatusTypeName | STATUS_TYPE_NAME | — | ✅ |
| 7 | WorkflowStatusOtbiPEOSubStatusName | SUB_STATUS_NAME | — | ✅ |
| 8 | WorkflowStatusOtbiPEOSubStatusType | SUB_STATUS_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
