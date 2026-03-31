---
id: DOC-GL-PVO-UserColumnInstanceDPVO
doc_type: system-doc
title: "UserColumnInstanceDPVO — PVO General Ledger"
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
  - UserColumnInstanceDPVO
  - usercolumninstancedpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# UserColumnInstanceDPVO

## 📌 Visão Geral

View Object para extração BICC de dados de User Column Instance D. Acessa as tabelas: FF_USER_COLUMN_INSTANCES_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.UserTablesAM.UserColumnInstanceDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 3 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ff_user_column_instances_f|FF_USER_COLUMN_INSTANCES_F]] — 16 atributos (3 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[ff_user_column_instances_f|FF_USER_COLUMN_INSTANCES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserColumnInstanceDPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | UserColumnInstanceDPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | UserColumnInstanceDPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 4 | UserColumnInstanceDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 5 | UserColumnInstanceDPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 6 | UserColumnInstanceDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | UserColumnInstanceDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | UserColumnInstanceDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | UserColumnInstanceDPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 10 | UserColumnInstanceDPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 11 | UserColumnInstanceDPEOModuleId | MODULE_ID | — | ✅ |
| 12 | UserColumnInstanceDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | UserColumnInstanceDPEOUserColumnId | USER_COLUMN_ID | — | ✅ |
| 14 | UserColumnInstanceDPEOUserColumnInstanceId | USER_COLUMN_INSTANCE_ID | 🔑 | ✅ |
| 15 | UserColumnInstanceDPEOUserRowId | USER_ROW_ID | — | ✅ |
| 16 | UserColumnInstanceDPEOValue | VALUE | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
