---
id: DOC-OTHER-PVO-FRMRolePVO
doc_type: system-doc
title: "FRMRolePVO — PVO Cross-Module"
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
  - FRMRolePVO
  - frmrolepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FRMRolePVO

## 📌 Visão Geral

View Object para extração BICC de dados de FRMRole. Acessa as tabelas: GRC_ACN_ROLE_INFO.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.FRMRolePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 2 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[grc_acn_role_info|GRC_ACN_ROLE_INFO]] — 12 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[grc_acn_role_info|GRC_ACN_ROLE_INFO]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ACNRoleInfoPEOChecksum | CHECKSUM | — | — |
| 2 | ACNRoleInfoPEOCreatedBy | CREATED_BY | — | — |
| 3 | ACNRoleInfoPEOCreationDate | CREATION_DATE | — | — |
| 4 | ACNRoleInfoPEOIsActvFlg | IS_ACTIVE_FLAG | — | — |
| 5 | ACNRoleInfoPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ACNRoleInfoPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ACNRoleInfoPEOLstUpdtDt | LAST_UPDATE_DATE | — | — |
| 8 | ACNRoleInfoPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 9 | ACNRoleInfoPEORoleDesc | ROLE_DESCRIPTION | — | — |
| 10 | ACNRoleInfoPEORoleId | ROLE_ID | — | — |
| 11 | ACNRoleInfoPEORoleInfoId | ROLE_INFO_ID | 🔑 | ✅ |
| 12 | ACNRoleInfoPEORoleName | ROLE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
