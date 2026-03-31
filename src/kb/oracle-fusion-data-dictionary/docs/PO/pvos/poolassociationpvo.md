---
id: DOC-PO-PVO-PoolAssociationPVO
doc_type: system-doc
title: "PoolAssociationPVO — PVO Purchasing"
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
  - PoolAssociationPVO
  - poolassociationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PoolAssociationPVO

## 📌 Visão Geral

Extrai as associações entre pools de candidatos e requisições ou vagas, vinculando banco de talentos a demandas ativas. Permite análise de utilização e eficácia dos pools na contratação.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfilePoolsAM.PoolAssociationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 3 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_pool_associations|HRT_POOL_ASSOCIATIONS]] — 11 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hrt_pool_associations|HRT_POOL_ASSOCIATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 2 | PoolAssociationId | POOL_ASSOCIATION_ID | 🔑 | ✅ |
| 3 | PoolAssociationPEOCreatedBy | CREATED_BY | — | — |
| 4 | PoolAssociationPEOCreationDate | CREATION_DATE | — | — |
| 5 | PoolAssociationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PoolAssociationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | PoolAssociationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | PoolAssociationPEOObjectId | OBJECT_ID | — | — |
| 9 | PoolAssociationPEOObjectType | OBJECT_TYPE | — | — |
| 10 | PoolAssociationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PoolAssociationPEOPoolId | POOL_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
