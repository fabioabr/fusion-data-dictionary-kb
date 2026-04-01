---
id: DOC-OTHER-PVO-DataSourcePVO
doc_type: system-doc
title: "DataSourcePVO — PVO Cross-Module"
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
  - DataSourcePVO
  - datasourcepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DataSourcePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Data Source. Acessa as tabelas: GRC_JOB, GRC_SYNC, GTG_DATASOURCE_B (+5).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.DataSourcePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 88 | 8 | 1 | 18 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[grc_job|GRC_JOB]] — 4 atributos (2 BICC)
- [[grc_sync|GRC_SYNC]] — 6 atributos (4 BICC)
- [[gtg_datasource_b|GTG_DATASOURCE_B]] — 20 atributos (1 PKs, 3 BICC)
- [[gtg_datasource_tl|GTG_DATASOURCE_TL]] — 11 atributos (3 BICC)
- [[gtg_datasource_type_b|GTG_DATASOURCE_TYPE_B]] — 12 atributos (1 BICC)
- [[gtg_datasource_type_tl|GTG_DATASOURCE_TYPE_TL]] — 11 atributos (2 BICC)
- [[gtg_datasource_typver_b|GTG_DATASOURCE_TYPVER_B]] — 13 atributos (1 BICC)
- [[gtg_datasource_typver_tl|GTG_DATASOURCE_TYPVER_TL]] — 11 atributos (2 BICC)

---

## ⚙️ Atributos

### [[grc_job|GRC_JOB]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobPEOAccessId | ID | — | — |
| 2 | JobPEOAccessStatusId | STATUS_ID | — | ✅ |
| 3 | JobPEOTransId | ID | — | — |
| 4 | JobPEOTransStatusId | STATUS_ID | — | ✅ |

### [[grc_sync|GRC_SYNC]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SyncPEOAccessId | ID | — | — |
| 2 | SyncPEOAccessLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | SyncPEOAccessStatus | STATUS | — | ✅ |
| 4 | SyncPEOTransId | ID | — | — |
| 5 | SyncPEOTransLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SyncPEOTransStatus | STATUS | — | ✅ |

### [[gtg_datasource_b|GTG_DATASOURCE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DatasourceBasePEOCreatedBy | CREATED_BY | — | — |
| 2 | DatasourceBasePEOCreationDate | CREATION_DATE | — | — |
| 3 | DatasourceBasePEODatabaseTypeId | DATABASE_TYPE_ID | — | — |
| 4 | DatasourceBasePEODatasourceTypeId | DATASOURCE_TYPE_ID | — | — |
| 5 | DatasourceBasePEODsTypeVersionKey | DS_TYPE_VERSION_KEY | — | — |
| 6 | DatasourceBasePEOId | ID | 🔑 | ✅ |
| 7 | DatasourceBasePEOIsActive | IS_ACTIVE | — | — |
| 8 | DatasourceBasePEOIsDefault | IS_DEFAULT | — | ✅ |
| 9 | DatasourceBasePEOIsSeeded | IS_SEEDED | — | — |
| 10 | DatasourceBasePEOLastAcgSyncId | LAST_ACG_SYNC_ID | — | — |
| 11 | DatasourceBasePEOLastTcgSyncId | LAST_TCG_SYNC_ID | — | — |
| 12 | DatasourceBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | DatasourceBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | DatasourceBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | DatasourceBasePEOLatestAccEtlJobId | LATEST_ACC_ETL_JOB_ID | — | — |
| 16 | DatasourceBasePEOLatestTcgEtlJobId | LATEST_TCG_ETL_JOB_ID | — | — |
| 17 | DatasourceBasePEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 18 | DatasourceBasePEOSguid | SGUID | — | — |
| 19 | DatasourceBasePEOSyncState | SYNC_STATE | — | — |
| 20 | DatasourceBasePEOTnsAlias | TNS_ALIAS | — | — |

### [[gtg_datasource_tl|GTG_DATASOURCE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DatasourceTransalationPEOCreatedBy | CREATED_BY | — | — |
| 2 | DatasourceTransalationPEOCreationDate | CREATION_DATE | — | — |
| 3 | DatasourceTransalationPEODescription | DESCRIPTION | — | ✅ |
| 4 | DatasourceTransalationPEOId | ID | — | — |
| 5 | DatasourceTransalationPEOLanguage | LANGUAGE | — | — |
| 6 | DatasourceTransalationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DatasourceTransalationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | DatasourceTransalationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | DatasourceTransalationPEOName | NAME | — | ✅ |
| 10 | DatasourceTransalationPEOSeedDS | SEED_DATA_SOURCE | — | — |
| 11 | DatasourceTransalationPEOSourceLang | SOURCE_LANG | — | — |

### [[gtg_datasource_type_b|GTG_DATASOURCE_TYPE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DatasourceTypeBasePEOBindKey | BIND_KEY | — | — |
| 2 | DatasourceTypeBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | DatasourceTypeBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | DatasourceTypeBasePEOId | ID | — | — |
| 5 | DatasourceTypeBasePEOIsActive | IS_ACTIVE | — | — |
| 6 | DatasourceTypeBasePEOIsSeeded | IS_SEEDED | — | — |
| 7 | DatasourceTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | DatasourceTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | DatasourceTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | DatasourceTypeBasePEOReadOnly | READ_ONLY | — | — |
| 11 | DatasourceTypeBasePEOSeedDS | SEED_DATA_SOURCE | — | — |
| 12 | DatasourceTypeBasePEOSguid | SGUID | — | — |

### [[gtg_datasource_type_tl|GTG_DATASOURCE_TYPE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DatasourceTypeTransPEOCreatedBy | CREATED_BY | — | — |
| 2 | DatasourceTypeTransPEOCreationDate | CREATION_DATE | — | — |
| 3 | DatasourceTypeTransPEODescription | DESCRIPTION | — | — |
| 4 | DatasourceTypeTransPEOId | ID | — | — |
| 5 | DatasourceTypeTransPEOLanguage | LANGUAGE | — | — |
| 6 | DatasourceTypeTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DatasourceTypeTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | DatasourceTypeTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | DatasourceTypeTransPEOName | NAME | — | ✅ |
| 10 | DatasourceTypeTransPEOSeedDS | SEED_DATA_SOURCE | — | — |
| 11 | DatasourceTypeTransPEOSourceLang | SOURCE_LANG | — | — |

### [[gtg_datasource_typver_b|GTG_DATASOURCE_TYPVER_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DatasourceTypeVerBasePEOCreatedBy | CREATED_BY | — | — |
| 2 | DatasourceTypeVerBasePEOCreationDate | CREATION_DATE | — | — |
| 3 | DatasourceTypeVerBasePEODatasourceTypeId | DATASOURCE_TYPE_ID | — | — |
| 4 | DatasourceTypeVerBasePEOEtlAdapterPath | ETL_ADAPTER_PATH | — | — |
| 5 | DatasourceTypeVerBasePEOId | ID | — | — |
| 6 | DatasourceTypeVerBasePEOIsActive | IS_ACTIVE | — | — |
| 7 | DatasourceTypeVerBasePEOIsSeeded | IS_SEEDED | — | — |
| 8 | DatasourceTypeVerBasePEOKey1 | KEY | — | — |
| 9 | DatasourceTypeVerBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | DatasourceTypeVerBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | DatasourceTypeVerBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | DatasourceTypeVerBasePEOSeedDS | SEED_DATA_SOURCE | — | — |
| 13 | DatasourceTypeVerBasePEOSguid | SGUID | — | — |

### [[gtg_datasource_typver_tl|GTG_DATASOURCE_TYPVER_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DatasourceTypeVerTransPEOCreatedBy | CREATED_BY | — | — |
| 2 | DatasourceTypeVerTransPEOCreationDate | CREATION_DATE | — | — |
| 3 | DatasourceTypeVerTransPEODescription | DESCRIPTION | — | — |
| 4 | DatasourceTypeVerTransPEOId | ID | — | — |
| 5 | DatasourceTypeVerTransPEOLanguage | LANGUAGE | — | — |
| 6 | DatasourceTypeVerTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DatasourceTypeVerTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | DatasourceTypeVerTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | DatasourceTypeVerTransPEOName | NAME | — | ✅ |
| 10 | DatasourceTypeVerTransPEOSeedDS | SEED_DATA_SOURCE | — | — |
| 11 | DatasourceTypeVerTransPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
