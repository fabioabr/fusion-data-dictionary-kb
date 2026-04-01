---
id: DOC-PO-PVO-CandidatePoolPVO
doc_type: system-doc
title: "CandidatePoolPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CandidatePoolPVO
  - candidatepoolpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CandidatePoolPVO

## 📌 Visão Geral

Extrai os pools de candidatos para requisições de contratação, com nome, descrição e critérios de elegibilidade. Suporta processos de sourcing de mão de obra e gestão estratégica de talentos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecSourcingCandPoolsAM.CandidatePoolPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 8 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_pools_vl|HRT_POOLS_VL]] — 19 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[hrt_pools_vl|HRT_POOLS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DepartmentId | DEPARTMENT_ID | — | — |
| 5 | Description | DESCRIPTION | — | ✅ |
| 6 | EnterpriseId | ENTERPRISE_ID | — | — |
| 7 | GradeId | GRADE_ID | — | — |
| 8 | JobFamilyId | JOB_FAMILY_ID | — | — |
| 9 | JobId | JOB_ID | — | — |
| 10 | JobProfileId | JOB_PROFILE_ID | — | — |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | PoolId | POOL_ID | 🔑 | ✅ |
| 16 | PoolName | POOL_NAME | — | ✅ |
| 17 | PoolTypeCode | POOL_TYPE_CODE | — | ✅ |
| 18 | PositionId | POSITION_ID | — | — |
| 19 | Status | STATUS | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
