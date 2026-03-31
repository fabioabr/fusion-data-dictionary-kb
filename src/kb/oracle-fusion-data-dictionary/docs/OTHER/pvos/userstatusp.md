---
id: DOC-OTHER-PVO-UserStatusP
doc_type: system-doc
title: "UserStatusP — PVO Cross-Module"
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
  - UserStatusP
  - userstatusp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# UserStatusP

## 📌 Visão Geral

View Object para extração BICC de dados de User Status P. Acessa as tabelas: OKC_USER_STATUSES_VL.

**Caminho:** `FscmTopModelAM.ContractsCoreAM.UserStatusP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 1 | 8 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[okc_user_statuses_vl|OKC_USER_STATUSES_VL]] — 8 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[okc_user_statuses_vl|OKC_USER_STATUSES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | StatusMeaning | STATUS_MEANING | — | ✅ |
| 8 | UserStatusCode | USER_STATUS_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
