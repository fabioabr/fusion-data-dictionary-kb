---
id: DOC-OTHER-PVO-StepInstanceDetailExtractPVO
doc_type: system-doc
title: "StepInstanceDetailExtractPVO — PVO Cross-Module"
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
  - StepInstanceDetailExtractPVO
  - stepinstancedetailextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StepInstanceDetailExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Step Instance Detail Extract. Acessa as tabelas: DOO_STEP_INSTANCE_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.StepInstanceDetailExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_step_instance_details|DOO_STEP_INSTANCE_DETAILS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[doo_step_instance_details|DOO_STEP_INSTANCE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StepInstanceDetailCreatedBy | CREATED_BY | — | ✅ |
| 2 | StepInstanceDetailCreationDate | CREATION_DATE | — | ✅ |
| 3 | StepInstanceDetailFulfillLineId | FULFILL_LINE_ID | — | ✅ |
| 4 | StepInstanceDetailId | STEP_INSTANCE_DETAIL_ID | 🔑 | ✅ |
| 5 | StepInstanceDetailLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | StepInstanceDetailLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | StepInstanceDetailLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | StepInstanceDetailLineId | LINE_ID | — | ✅ |
| 9 | StepInstanceDetailObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | StepInstanceDetailSplitFromGroupFlag | SPLIT_FROM_GROUP_FLAG | — | ✅ |
| 11 | StepInstanceDetailStatusCode | STATUS_CODE | — | ✅ |
| 12 | StepInstanceDetailStepInstanceId | STEP_INSTANCE_ID | — | ✅ |
| 13 | StepInstanceDetailTaskEligibleFlag | TASK_ELIGIBLE_FLAG | — | ✅ |
| 14 | StepInstanceDetailTaskTypeId | TASK_TYPE_ID | — | ✅ |
| 15 | StepInstanceDetailWebServiceId | WEB_SERVICE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
