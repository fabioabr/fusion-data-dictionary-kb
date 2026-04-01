---
id: DOC-OTHER-PVO-ProcessClassStatusExtractPVO
doc_type: system-doc
title: "ProcessClassStatusExtractPVO — PVO Cross-Module"
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
  - ProcessClassStatusExtractPVO
  - processclassstatusextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProcessClassStatusExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Process Class Status Extract. Acessa as tabelas: DOO_PROCESS_CLASS_STATUSES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.ProcessClassStatusExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_process_class_statuses|DOO_PROCESS_CLASS_STATUSES]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[doo_process_class_statuses|DOO_PROCESS_CLASS_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrchestrationProcessClassCreatedBy | CREATED_BY | — | ✅ |
| 2 | OrchestrationProcessClassCreationDate | CREATION_DATE | — | ✅ |
| 3 | OrchestrationProcessClassDefaultFlag | DEFAULT_FLAG | — | ✅ |
| 4 | OrchestrationProcessClassLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | OrchestrationProcessClassLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | OrchestrationProcessClassLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | OrchestrationProcessClassObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | OrchestrationProcessClassOrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | ✅ |
| 9 | OrchestrationProcessClassProcessClassId | PROCESS_CLASS_ID | — | ✅ |
| 10 | OrchestrationProcessClassProcessClassStatusId | PROCESS_CLASS_STATUS_ID | 🔑 | ✅ |
| 11 | OrchestrationProcessClassStatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
