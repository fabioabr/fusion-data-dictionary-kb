---
id: DOC-PO-PVO-TalentPoolUsersPVO
doc_type: system-doc
title: "TalentPoolUsersPVO — PVO Purchasing"
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
  - TalentPoolUsersPVO
  - talentpooluserspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TalentPoolUsersPVO

## 📌 Visão Geral

Extrai os usuários proprietários de pools de talentos, com permissões de gestão e administração. Suporta governança dos processos de gestão de talentos e auditoria de responsabilidades.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfilePoolsAM.TalentPoolUsersPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 3 | 3 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_pool_owners|HRT_POOL_OWNERS]] — 11 atributos (3 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hrt_pool_owners|HRT_POOL_OWNERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | FavoriteFlag | FAVORITE_FLAG | — | — |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | OwnerEnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 9 | OwnerPersonId | OWNER_PERSON_ID | 🔑 | ✅ |
| 10 | OwnerPoolId | POOL_ID | 🔑 | ✅ |
| 11 | PoolOwnerId | POOL_OWNER_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
