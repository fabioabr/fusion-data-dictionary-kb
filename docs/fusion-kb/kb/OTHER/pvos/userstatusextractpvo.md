---
id: DOC-OTHER-PVO-UserStatusExtractPVO
doc_type: system-doc
title: "UserStatusExtractPVO — PVO Cross-Module"
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
  - UserStatusExtractPVO
  - userstatusextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# UserStatusExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de User Status Extract. Acessa as tabelas: CJM_USER_STATUSES_B.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.UserStatusExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_user_statuses_b|CJM_USER_STATUSES_B]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[cjm_user_statuses_b|CJM_USER_STATUSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BuySideFlag | BUY_SIDE_FLAG | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DefaultFlag | DEFAULT_FLAG | — | ✅ |
| 5 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | SeededFlag | SEEDED_FLAG | — | ✅ |
| 11 | SellSideDefaultFlag | SELL_SIDE_DEFAULT_FLAG | — | ✅ |
| 12 | SellSideFlag | SELL_SIDE_FLAG | — | ✅ |
| 13 | SystemStatusCode | SYSTEM_STATUS_CODE | — | ✅ |
| 14 | SystemStatusType | SYSTEM_STATUS_TYPE | — | ✅ |
| 15 | UserStatusCode | USER_STATUS_CODE | — | ✅ |
| 16 | UserStatusId | USER_STATUS_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
