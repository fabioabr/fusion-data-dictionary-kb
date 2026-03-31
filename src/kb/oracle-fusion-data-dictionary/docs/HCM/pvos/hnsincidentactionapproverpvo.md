---
id: DOC-HCM-PVO-HNSIncidentActionApproverPVO
doc_type: system-doc
title: "HNSIncidentActionApproverPVO — PVO Human Capital Management"
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
  - HNSIncidentActionApproverPVO
  - hnsincidentactionapproverpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HNSIncidentActionApproverPVO

## 📌 Visão Geral

Extrai aprovadores de ações corretivas de incidentes de SST. Utilizado para gestão de workflow de aprovação de medidas corretivas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HealthandSafetyAM.HNSIncidentActionApproverPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 17 | 94% |

---

## 🔗 Tabelas Relacionadas

- [[hns_persons|HNS_PERSONS]] — 18 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[hns_persons|HNS_PERSONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSPersonsPEOActionReqFlag | ACTION_REQUIRED_FLAG | — | ✅ |
| 2 | HNSPersonsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 3 | HNSPersonsPEOCompletedFlag | COMPLETED_FLAG | — | ✅ |
| 4 | HNSPersonsPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | HNSPersonsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | HNSPersonsPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 7 | HNSPersonsPEOEmployeeId | EMPLOYEE_ID | — | ✅ |
| 8 | HNSPersonsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | HNSPersonsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | HNSPersonsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | HNSPersonsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | HNSPersonsPEOPerAssignId | PERSON_ASSIGN_ID | — | — |
| 13 | HNSPersonsPEOPersonId | PERSON_ID | 🔑 | ✅ |
| 14 | HNSPersonsPEOResultCode | RESULT_CODE | — | ✅ |
| 15 | HNSPersonsPEORoleCode | ROLE_CODE | — | ✅ |
| 16 | HNSPersonsPEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | ✅ |
| 17 | HNSPersonsPEOTaskId | TASK_ID | — | ✅ |
| 18 | HNSPersonsPEOTaskTypeCode | TASK_TYPE_CODE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
