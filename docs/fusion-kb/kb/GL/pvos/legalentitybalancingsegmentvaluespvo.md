---
id: DOC-GL-PVO-LegalEntityBalancingSegmentValuesPVO
doc_type: system-doc
title: "LegalEntityBalancingSegmentValuesPVO — PVO General Ledger"
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
  - LegalEntityBalancingSegmentValuesPVO
  - legalentitybalancingsegmentvaluespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LegalEntityBalancingSegmentValuesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Legal Entity Balancing Segment Values. Acessa as tabelas: FND_VS_VALUE_SETS, GL_LEDGER_CONFIG_DETAILS, GL_LEGAL_ENTITIES_BSVS.

**Caminho:** `FscmTopModelAM.FinGlLedgerDefnAM.LegalEntityBalancingSegmentValuesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 3 | 6 | 8 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_vs_value_sets|FND_VS_VALUE_SETS]] — 3 atributos (1 PKs, 1 BICC)
- [[gl_ledger_config_details|GL_LEDGER_CONFIG_DETAILS]] — 26 atributos (4 PKs, 5 BICC)
- [[gl_legal_entities_bsvs|GL_LEGAL_ENTITIES_BSVS]] — 11 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[fnd_vs_value_sets|FND_VS_VALUE_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValueSetsEnterpriseId | ENTERPRISE_ID | — | — |
| 2 | ValueSetsValueSetCode | VALUE_SET_CODE | 🔑 | ✅ |
| 3 | ValueSetsValueSetId | VALUE_SET_ID | — | — |

### [[gl_ledger_config_details|GL_LEDGER_CONFIG_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConfigurationId | CONFIGURATION_ID | 🔑 | ✅ |
| 2 | GlLedgerConfigDetailsCreatedBy | CREATED_BY | — | — |
| 3 | GlLedgerConfigDetailsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 4 | GlLedgerConfigDetailsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 5 | GlLedgerConfigDetailsNextActionCode | NEXT_ACTION_CODE | — | — |
| 6 | GlLedgerConfigDetailsObjectName | OBJECT_NAME | — | — |
| 7 | GlLedgerConfigDetailsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | GlLedgerConfigDetailsStatusCode | STATUS_CODE | — | — |
| 9 | GlLedgerConfigDetailsTaxDefaultLeFlag | TAX_DEFAULT_LE_FLAG | — | — |
| 10 | GlLedgerConfigDetailsTimeZoneDefaultLeFlag | TIME_ZONE_DEFAULT_LE_FLAG | — | — |
| 11 | LeLedgerConfigDtlsConfigurationId | CONFIGURATION_ID | — | — |
| 12 | LeLedgerConfigDtlsCreatedBy | CREATED_BY | — | — |
| 13 | LeLedgerConfigDtlsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | LeLedgerConfigDtlsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | LeLedgerConfigDtlsNextActionCode | NEXT_ACTION_CODE | — | — |
| 16 | LeLedgerConfigDtlsObjectId | OBJECT_ID | — | ✅ |
| 17 | LeLedgerConfigDtlsObjectName | OBJECT_NAME | — | — |
| 18 | LeLedgerConfigDtlsObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 19 | LeLedgerConfigDtlsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | LeLedgerConfigDtlsSetupStepCode | SETUP_STEP_CODE | — | — |
| 21 | LeLedgerConfigDtlsStatusCode | STATUS_CODE | — | — |
| 22 | LeLedgerConfigDtlsTaxDefaultLeFlag | TAX_DEFAULT_LE_FLAG | — | — |
| 23 | LeLedgerConfigDtlsTimeZoneDefaultLeFlag | TIME_ZONE_DEFAULT_LE_FLAG | — | — |
| 24 | ObjectId | OBJECT_ID | 🔑 | ✅ |
| 25 | ObjectTypeCode | OBJECT_TYPE_CODE | 🔑 | ✅ |
| 26 | SetupStepCode | SETUP_STEP_CODE | 🔑 | ✅ |

### [[gl_legal_entities_bsvs|GL_LEGAL_ENTITIES_BSVS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLegalEntitiesBsvsCreatedBy | CREATED_BY | — | — |
| 2 | GlLegalEntitiesBsvsCreationDate | CREATION_DATE | — | — |
| 3 | GlLegalEntitiesBsvsEndDate | END_DATE | — | — |
| 4 | GlLegalEntitiesBsvsFlexSegmentValue | FLEX_SEGMENT_VALUE | 🔑 | ✅ |
| 5 | GlLegalEntitiesBsvsFlexValueSetId | FLEX_VALUE_SET_ID | — | — |
| 6 | GlLegalEntitiesBsvsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | GlLegalEntitiesBsvsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | GlLegalEntitiesBsvsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | GlLegalEntitiesBsvsLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 10 | GlLegalEntitiesBsvsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | GlLegalEntitiesBsvsStartDate | START_DATE | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
