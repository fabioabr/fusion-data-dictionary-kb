---
id: DOC-HCM-PVO-AssignmentStatusTypesPVO
doc_type: system-doc
title: "AssignmentStatusTypesPVO — PVO Human Capital Management"
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
  - AssignmentStatusTypesPVO
  - assignmentstatustypespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssignmentStatusTypesPVO

## 📌 Visão Geral

Cataloga tipos de status de assignment com traducoes. Tabela de referencia para classificacao de estados como ativo, suspenso, encerrado.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AssignmentAM.AssignmentStatusTypesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 2 | 1 | 2 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[per_assignment_status_types|PER_ASSIGNMENT_STATUS_TYPES]] — 19 atributos (1 PKs, 2 BICC)
- [[per_assignment_status_types_tl|PER_ASSIGNMENT_STATUS_TYPES_TL]] — 11 atributos

---

## ⚙️ Atributos

### [[per_assignment_status_types|PER_ASSIGNMENT_STATUS_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | 🔑 | ✅ |
| 2 | AssignmentStatusTypesPEOActiveFlag | ACTIVE_FLAG | — | — |
| 3 | AssignmentStatusTypesPEOAssignmentStatusCode | ASSIGNMENT_STATUS_CODE | — | — |
| 4 | AssignmentStatusTypesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | AssignmentStatusTypesPEOCreatedBy | CREATED_BY | — | — |
| 6 | AssignmentStatusTypesPEOCreationDate | CREATION_DATE | — | — |
| 7 | AssignmentStatusTypesPEODefaultFlag | DEFAULT_FLAG | — | — |
| 8 | AssignmentStatusTypesPEOEndDate | END_DATE | — | — |
| 9 | AssignmentStatusTypesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | AssignmentStatusTypesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | AssignmentStatusTypesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | AssignmentStatusTypesPEOLegislationCode | LEGISLATION_CODE | — | — |
| 13 | AssignmentStatusTypesPEOModuleId | MODULE_ID | — | — |
| 14 | AssignmentStatusTypesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | AssignmentStatusTypesPEOOrigAssignStatusTypeId | ORIG_ASSIGN_STATUS_TYPE_ID | — | — |
| 16 | AssignmentStatusTypesPEOPaySystemStatus | PAY_SYSTEM_STATUS | — | — |
| 17 | AssignmentStatusTypesPEOPerSystemStatus | PER_SYSTEM_STATUS | — | — |
| 18 | AssignmentStatusTypesPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 19 | AssignmentStatusTypesPEOStartDate | START_DATE | — | — |

### [[per_assignment_status_types_tl|PER_ASSIGNMENT_STATUS_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentStatusTypesTransPEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | — |
| 2 | AssignmentStatusTypesTransPEOCreatedBy | CREATED_BY | — | — |
| 3 | AssignmentStatusTypesTransPEOCreationDate | CREATION_DATE | — | — |
| 4 | AssignmentStatusTypesTransPEOExternalStatus | EXTERNAL_STATUS | — | — |
| 5 | AssignmentStatusTypesTransPEOLanguage | LANGUAGE | — | — |
| 6 | AssignmentStatusTypesTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | AssignmentStatusTypesTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AssignmentStatusTypesTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AssignmentStatusTypesTransPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | AssignmentStatusTypesTransPEOSourceLang | SOURCE_LANG | — | — |
| 11 | AssignmentStatusTypesTransPEOUserStatus | USER_STATUS | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
