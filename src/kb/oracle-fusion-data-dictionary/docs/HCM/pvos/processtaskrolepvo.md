---
id: DOC-HCM-PVO-ProcessTaskRolePVO
doc_type: system-doc
title: "ProcessTaskRolePVO — PVO Human Capital Management"
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
  - ProcessTaskRolePVO
  - processtaskrolepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProcessTaskRolePVO

## 📌 Visão Geral

Disponibiliza papéis atribuídos a tarefas em processos de avaliação de desempenho. Suporta a configuração de responsabilidades por etapa no ciclo de performance.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceSetupAM.ProcessTaskRolePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 2 | 3 | 8 | 47% |

---

## 🔗 Tabelas Relacionadas

- [[hra_pf_task_roles_b|HRA_PF_TASK_ROLES_B]] — 11 atributos (2 PKs, 5 BICC)
- [[hra_pf_task_roles_tl|HRA_PF_TASK_ROLES_TL]] — 6 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hra_pf_task_roles_b|HRA_PF_TASK_ROLES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ProcessTaskRoleBPEOProcessFlowId | PROCESS_FLOW_ID | — | — |
| 9 | ProcessTaskRoleBPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 10 | ProcessTaskRoleBPEOTaskCode | TASK_CODE | — | ✅ |
| 11 | ProcessTaskRoleId | PROCESS_TASK_ROLE_ID | 🔑 | ✅ |

### [[hra_pf_task_roles_tl|HRA_PF_TASK_ROLES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | ProcessTaskRoleTransPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ProcessTaskRoleTransPEOMgrTaskName | MGR_TASK_NAME | — | ✅ |
| 4 | ProcessTaskRoleTransPEOProcessTaskRoleId | PROCESS_TASK_ROLE_ID | — | — |
| 5 | ProcessTaskRoleTransPEOWkrTaskName | WKR_TASK_NAME | — | ✅ |
| 6 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
