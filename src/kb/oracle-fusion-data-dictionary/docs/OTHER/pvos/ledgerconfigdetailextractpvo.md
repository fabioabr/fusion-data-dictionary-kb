---
id: DOC-OTHER-PVO-LedgerConfigDetailExtractPVO
doc_type: system-doc
title: "LedgerConfigDetailExtractPVO — PVO Cross-Module"
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
  - LedgerConfigDetailExtractPVO
  - ledgerconfigdetailextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LedgerConfigDetailExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ledger Config Detail Extract. Acessa as tabelas: GL_LEDGER_CONFIG_DETAILS.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.LedgerConfigDetailExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 4 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gl_ledger_config_details|GL_LEDGER_CONFIG_DETAILS]] — 15 atributos (4 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[gl_ledger_config_details|GL_LEDGER_CONFIG_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GLConfigDetailsConfigurationId | CONFIGURATION_ID | 🔑 | ✅ |
| 2 | GLConfigDetailsCreatedBy | CREATED_BY | — | ✅ |
| 3 | GLConfigDetailsCreationDate | CREATION_DATE | — | ✅ |
| 4 | GLConfigDetailsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | GLConfigDetailsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | GLConfigDetailsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | GLConfigDetailsNextActionCode | NEXT_ACTION_CODE | — | ✅ |
| 8 | GLConfigDetailsObjectId | OBJECT_ID | 🔑 | ✅ |
| 9 | GLConfigDetailsObjectName | OBJECT_NAME | — | ✅ |
| 10 | GLConfigDetailsObjectTypeCode | OBJECT_TYPE_CODE | 🔑 | ✅ |
| 11 | GLConfigDetailsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | GLConfigDetailsSetupStepCode | SETUP_STEP_CODE | 🔑 | ✅ |
| 13 | GLConfigDetailsStatusCode | STATUS_CODE | — | ✅ |
| 14 | GLConfigDetailsTaxDefaultLeFlag | TAX_DEFAULT_LE_FLAG | — | ✅ |
| 15 | GLConfigDetailsTimeZoneDefaultLeFlag | TIME_ZONE_DEFAULT_LE_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
