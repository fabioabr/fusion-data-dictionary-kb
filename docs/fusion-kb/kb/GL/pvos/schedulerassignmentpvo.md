---
id: DOC-GL-PVO-SchedulerAssignmentPVO
doc_type: system-doc
title: "SchedulerAssignmentPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SchedulerAssignmentPVO
  - schedulerassignmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SchedulerAssignmentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Scheduler Assignment. Acessa as tabelas: HXT_SCH_ASGS_DEFAULT_VIEW.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.SetupOptionsAM.SchedulerAssignmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 1 | 1 | 18 | 72% |

---

## 🔗 Tabelas Relacionadas

- [[hxt_sch_asgs_default_view|HXT_SCH_ASGS_DEFAULT_VIEW]] — 25 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[hxt_sch_asgs_default_view|HXT_SCH_ASGS_DEFAULT_VIEW]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignTo | ASSIGN_TO | — | — |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DateFrom | DATE_FROM | — | ✅ |
| 5 | DateTo | DATE_TO | — | ✅ |
| 6 | GrpId | GRP_ID | — | — |
| 7 | GrpInclMemberId | GRP_INCL_MEMBER_ID | — | — |
| 8 | InclMemberId | INCL_MEMBER_ID | — | — |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ObjectId | OBJECT_ID | — | — |
| 13 | ProductArea | PRODUCT_AREA | — | — |
| 14 | ProfileCreatedBy | PROFILE_CREATED_BY | — | ✅ |
| 15 | ProfileCreationDate | PROFILE_CREATION_DATE | — | ✅ |
| 16 | ProfileDescription | PROFILE_DESCRIPTION | — | ✅ |
| 17 | ProfileLastUpdateDate | PROFILE_LAST_UPDATE_DATE | — | ✅ |
| 18 | ProfileLastUpdateLogin | PROFILE_LAST_UPDATE_LOGIN | — | ✅ |
| 19 | ProfileLastUpdatedBy | PROFILE_LAST_UPDATED_BY | — | ✅ |
| 20 | ProfileName | PROFILE_NAME | — | ✅ |
| 21 | ProfilePrecedence | PROFILE_PRECEDENCE | — | — |
| 22 | SetupProfileAsgCd | SETUP_PROFILE_ASG_CD | — | ✅ |
| 23 | SetupProfileAsgId | SETUP_PROFILE_ASG_ID | 🔑 | ✅ |
| 24 | SetupProfileCd | SETUP_PROFILE_CD | — | ✅ |
| 25 | SetupProfileId | SETUP_PROFILE_ID | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
