---
id: DOC-OTHER-PVO-HoldStepInstanceExtractPVO
doc_type: system-doc
title: "HoldStepInstanceExtractPVO — PVO Cross-Module"
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
  - HoldStepInstanceExtractPVO
  - holdstepinstanceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HoldStepInstanceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Hold Step Instance Extract. Acessa as tabelas: DOO_HOLD_STEP_INSTANCES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.HoldStepInstanceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_hold_step_instances|DOO_HOLD_STEP_INSTANCES]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[doo_hold_step_instances|DOO_HOLD_STEP_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HoldStepInstanceCreatedBy | CREATED_BY | — | ✅ |
| 2 | HoldStepInstanceCreationDate | CREATION_DATE | — | ✅ |
| 3 | HoldStepInstanceHoldInstanceId | HOLD_INSTANCE_ID | 🔑 | ✅ |
| 4 | HoldStepInstanceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | HoldStepInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | HoldStepInstanceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | HoldStepInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | HoldStepInstanceStepInstanceId | STEP_INSTANCE_ID | 🔑 | ✅ |
| 9 | HoldStepInstanceTaskInstanceId | TASK_INSTANCE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
