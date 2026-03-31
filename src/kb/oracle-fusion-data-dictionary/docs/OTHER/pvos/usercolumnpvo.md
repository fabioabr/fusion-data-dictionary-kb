---
id: DOC-OTHER-PVO-UserColumnPVO
doc_type: system-doc
title: "UserColumnPVO — PVO Cross-Module"
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
  - UserColumnPVO
  - usercolumnpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# UserColumnPVO

## 📌 Visão Geral

View Object para extração BICC de dados de User Column. Acessa as tabelas: FF_USER_COLUMNS_VL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.UserTablesAM.UserColumnPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ff_user_columns_vl|FF_USER_COLUMNS_VL]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[ff_user_columns_vl|FF_USER_COLUMNS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserColumnPEOBaseUserColumnName | BASE_USER_COLUMN_NAME | — | ✅ |
| 2 | UserColumnPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | UserColumnPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | UserColumnPEODataType | DATA_TYPE | — | ✅ |
| 5 | UserColumnPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 6 | UserColumnPEOFormulaId | FORMULA_ID | — | ✅ |
| 7 | UserColumnPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | UserColumnPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | UserColumnPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | UserColumnPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 11 | UserColumnPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 12 | UserColumnPEOModuleId | MODULE_ID | — | ✅ |
| 13 | UserColumnPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | UserColumnPEOUserColumnId | USER_COLUMN_ID | 🔑 | ✅ |
| 15 | UserColumnPEOUserColumnName | USER_COLUMN_NAME | — | ✅ |
| 16 | UserColumnPEOUserTableId | USER_TABLE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
