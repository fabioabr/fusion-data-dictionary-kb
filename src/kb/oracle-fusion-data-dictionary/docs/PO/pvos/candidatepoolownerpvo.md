---
id: DOC-PO-PVO-CandidatePoolOwnerPVO
doc_type: system-doc
title: "CandidatePoolOwnerPVO — PVO Purchasing"
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
  - CandidatePoolOwnerPVO
  - candidatepoolownerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CandidatePoolOwnerPVO

## 📌 Visão Geral

Extrai os proprietários (gestores) de pools de candidatos, com permissões e responsabilidades atribuídas. Suporta governança e auditoria dos processos de gestão de talentos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecSourcingCandPoolsAM.CandidatePoolOwnerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 2 | 2 | 10 | 77% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_pools_vl|HRT_POOLS_VL]] — 2 atributos
- [[hrt_pool_owners|HRT_POOL_OWNERS]] — 11 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[hrt_pools_vl|HRT_POOLS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoolId1 | POOL_ID | — | — |
| 2 | PoolTypeCode | POOL_TYPE_CODE | — | — |

### [[hrt_pool_owners|HRT_POOL_OWNERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 4 | FavoriteFlag | FAVORITE_FLAG | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | OwnerPersonId | OWNER_PERSON_ID | — | — |
| 10 | PoolId | POOL_ID | — | ✅ |
| 11 | PoolOwnerId | POOL_OWNER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
