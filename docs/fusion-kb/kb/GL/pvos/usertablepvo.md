---
id: DOC-GL-PVO-UserTablePVO
doc_type: system-doc
title: "UserTablePVO — PVO General Ledger"
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
  - UserTablePVO
  - usertablepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# UserTablePVO

## 📌 Visão Geral

View Object para extração BICC de dados de User Table. Acessa as tabelas: FF_USER_TABLES_VL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.UserTablesAM.UserTablePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ff_user_tables_vl|FF_USER_TABLES_VL]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[ff_user_tables_vl|FF_USER_TABLES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserTablePEOBaseUserTableName | BASE_USER_TABLE_NAME | — | ✅ |
| 2 | UserTablePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | UserTablePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | UserTablePEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | UserTablePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | UserTablePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | UserTablePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | UserTablePEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 9 | UserTablePEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 10 | UserTablePEOModuleId | MODULE_ID | — | ✅ |
| 11 | UserTablePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | UserTablePEORangeOrMatch | RANGE_OR_MATCH | — | ✅ |
| 13 | UserTablePEOUserKeyUnits | USER_KEY_UNITS | — | ✅ |
| 14 | UserTablePEOUserRowTitle | USER_ROW_TITLE | — | ✅ |
| 15 | UserTablePEOUserTableId | USER_TABLE_ID | 🔑 | ✅ |
| 16 | UserTablePEOUserTableName | USER_TABLE_NAME | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
