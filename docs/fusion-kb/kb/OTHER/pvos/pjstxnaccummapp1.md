---
id: DOC-OTHER-PVO-PjsTxnAccumMapP1
doc_type: system-doc
title: "PjsTxnAccumMapP1 — PVO Cross-Module"
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
  - PjsTxnAccumMapP1
  - pjstxnaccummapp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjsTxnAccumMapP1

## 📌 Visão Geral

View Object para extração BICC de dados de Pjs Txn Accum Map P1. Acessa as tabelas: PJF_RBS_ELEMENTS_VL, PJF_RBS_PRJ_ASSIGNMENTS, PJF_RBS_TXN_ACCUM_MAP.

**Caminho:** `FscmTopModelAM.PjsProjectPerformanceAM.PjsTxnAccumMapP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 3 | 2 | 7 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]] — 7 atributos (2 BICC)
- [[pjf_rbs_prj_assignments|PJF_RBS_PRJ_ASSIGNMENTS]] — 2 atributos (2 BICC)
- [[pjf_rbs_txn_accum_map|PJF_RBS_TXN_ACCUM_MAP]] — 3 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RBSElementPEOExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | — |
| 2 | RBSElementPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 3 | RBSElementPEOJobId | JOB_ID | — | — |
| 4 | RBSElementPEOOrganizationId | ORGANIZATION_ID | — | — |
| 5 | RBSElementPEOPersonId | PERSON_ID | — | — |
| 6 | RBSElementPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 7 | RBSElementPEOResourceClassId | RESOURCE_CLASS_ID | — | ✅ |

### [[pjf_rbs_prj_assignments|PJF_RBS_PRJ_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectId | PROJECT_ID | — | ✅ |
| 2 | RbsPrjAssignmentId | RBS_PRJ_ASSIGNMENT_ID | — | ✅ |

### [[pjf_rbs_txn_accum_map|PJF_RBS_TXN_ACCUM_MAP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RBSTxnAccMapPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 2 | RbsVersionId | RBS_VERSION_ID | 🔑 | ✅ |
| 3 | TxnAccumHeaderId | TXN_ACCUM_HEADER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
