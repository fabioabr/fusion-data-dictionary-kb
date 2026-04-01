---
id: DOC-OTHER-PVO-ProdGroupsPVO
doc_type: system-doc
title: "ProdGroupsPVO — PVO Cross-Module"
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
  - ProdGroupsPVO
  - prodgroupspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProdGroupsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Prod Groups. Acessa as tabelas: QSC_PROD_GROUPS_VL.

**Caminho:** `FscmTopModelAM.PartsAnalyticsAM.ProdGroupsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 1 | 1 | 4 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[qsc_prod_groups_vl|QSC_PROD_GROUPS_VL]] — 24 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[qsc_prod_groups_vl|QSC_PROD_GROUPS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductGroupPEOAdminProdGrpDescText | ADMIN_PROD_GRP_DESC_TEXT | — | — |
| 2 | ProductGroupPEOAdminProdGrpName | ADMIN_PROD_GRP_NAME | — | — |
| 3 | ProductGroupPEOAdminRevisionNum | ADMIN_REVISION_NUM | — | — |
| 4 | ProductGroupPEOAdminStatePendingNum | ADMIN_STATE_PENDING_NUM | — | — |
| 5 | ProductGroupPEOBatchKey | BATCH_KEY | — | — |
| 6 | ProductGroupPEOCreatedBy | CREATED_BY | — | — |
| 7 | ProductGroupPEOCreationDate | CREATION_DATE | — | — |
| 8 | ProductGroupPEOImageIdentifierPath | IMAGE_IDENTIFIER_PATH | — | — |
| 9 | ProductGroupPEOInternalName | INTERNAL_NAME | — | — |
| 10 | ProductGroupPEOLanguage | LANGUAGE | — | — |
| 11 | ProductGroupPEOLastStructChangeDate | LAST_STRUCT_CHANGE_DATE | — | — |
| 12 | ProductGroupPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | ProductGroupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | ProductGroupPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | ProductGroupPEOLockedByUserGuid | LOCKED_BY_USER_GUID | — | — |
| 16 | ProductGroupPEOLockedDate | LOCKED_DATE | — | — |
| 17 | ProductGroupPEOLockedFlag | LOCKED_FLAG | — | — |
| 18 | ProductGroupPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | ProductGroupPEOProdGroupDescTxt | PROD_GROUP_DESC_TEXT | — | — |
| 20 | ProductGroupPEOProdGroupId | PROD_GROUP_ID | 🔑 | ✅ |
| 21 | ProductGroupPEOProdGroupName | PROD_GROUP_NAME | — | ✅ |
| 22 | ProductGroupPEORefNumber | REF_NUMBER | — | — |
| 23 | ProductGroupPEORuntimeRevisionNum | RUNTIME_REVISION_NUM | — | — |
| 24 | ProductGroupPEOUserLastUpdateDate | USER_LAST_UPDATE_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
