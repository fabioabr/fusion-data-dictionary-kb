---
id: DOC-OTHER-PVO-RelationConfigPVO
doc_type: system-doc
title: "RelationConfigPVO — PVO Cross-Module"
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
  - RelationConfigPVO
  - relationconfigpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RelationConfigPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Relation Config. Acessa as tabelas: HRT_RELATION_CONFIG_B, HRT_RELATION_CONFIG_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileSetupAM.RelationConfigPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 1 | 4 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_relation_config_b|HRT_RELATION_CONFIG_B]] — 14 atributos (1 PKs, 3 BICC)
- [[hrt_relation_config_tl|HRT_RELATION_CONFIG_TL]] — 11 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrt_relation_config_b|HRT_RELATION_CONFIG_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelationConfigBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RelationConfigBPEOCreatedBy | CREATED_BY | — | — |
| 3 | RelationConfigBPEOCreationDate | CREATION_DATE | — | — |
| 4 | RelationConfigBPEOEnabledFlag | ENABLED_FLAG | — | — |
| 5 | RelationConfigBPEOKeyTableName | KEY_TABLE_NAME | — | — |
| 6 | RelationConfigBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RelationConfigBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | RelationConfigBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | RelationConfigBPEOModuleId | MODULE_ID | — | — |
| 10 | RelationConfigBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | RelationConfigBPEORelationCode | RELATION_CODE | — | ✅ |
| 12 | RelationConfigBPEORelationId | RELATION_ID | 🔑 | ✅ |
| 13 | RelationConfigBPEORelationSeqNumber | RELATION_SEQ_NUMBER | — | — |
| 14 | RelationConfigBPEORelationTypeCode | RELATION_TYPE_CODE | — | — |

### [[hrt_relation_config_tl|HRT_RELATION_CONFIG_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelationConfigTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RelationConfigTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | RelationConfigTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | RelationConfigTranslationPEODescription | DESCRIPTION | — | — |
| 5 | RelationConfigTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | RelationConfigTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RelationConfigTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | RelationConfigTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | RelationConfigTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | RelationConfigTranslationPEORelationId | RELATION_ID | — | — |
| 11 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
