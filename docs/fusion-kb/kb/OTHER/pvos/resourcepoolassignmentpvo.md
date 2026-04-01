---
id: DOC-OTHER-PVO-ResourcePoolAssignmentPVO
doc_type: system-doc
title: "ResourcePoolAssignmentPVO — PVO Cross-Module"
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
  - ResourcePoolAssignmentPVO
  - resourcepoolassignmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourcePoolAssignmentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Resource Pool Assignment. Acessa as tabelas: PJR_RESOURCE_POOL_ASSIGNMENTS.

**Caminho:** `FscmTopModelAM.PjrResourceAM.ResourcePoolAssignmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 5 | 1 | 1 | 4 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[pjr_resource_pool_assignments|PJR_RESOURCE_POOL_ASSIGNMENTS]] — 5 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[pjr_resource_pool_assignments|PJR_RESOURCE_POOL_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FromDate | FROM_DATE | — | ✅ |
| 2 | PoolAssignmentId | POOL_ASSIGNMENT_ID | 🔑 | ✅ |
| 3 | PoolId | POOL_ID | — | — |
| 4 | ResourceId | RESOURCE_ID | — | ✅ |
| 5 | ToDate | TO_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
