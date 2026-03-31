---
id: DOC-OTHER-PVO-WorkCenterResourceExceptionExtractPVO
doc_type: system-doc
title: "WorkCenterResourceExceptionExtractPVO — PVO Cross-Module"
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
  - WorkCenterResourceExceptionExtractPVO
  - workcenterresourceexceptionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkCenterResourceExceptionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Center Resource Exception Extract. Acessa as tabelas: RCS_WC_RESOURCE_EXC.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.WorkCenterResourceExceptionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[rcs_wc_resource_exc|RCS_WC_RESOURCE_EXC]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[rcs_wc_resource_exc|RCS_WC_RESOURCE_EXC]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssociatedShiftId | ASSOCIATED_SHIFT_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EndDate | END_DATE | — | ✅ |
| 5 | ExcEndTime | EXC_END_TIME | — | ✅ |
| 6 | ExcStartTime | EXC_START_TIME | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 12 | PlantShiftExcId | PLANT_SHIFT_EXC_ID | — | ✅ |
| 13 | ScheduleId | SCHEDULE_ID | — | ✅ |
| 14 | StandaloneWcExcFlag | STANDALONE_WC_EXC_FLAG | — | ✅ |
| 15 | StartDate | START_DATE | — | ✅ |
| 16 | WcResourceExcId | WC_RESOURCE_EXC_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
