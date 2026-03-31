---
id: DOC-OTHER-PVO-BuUsageExtractPVO
doc_type: system-doc
title: "BuUsageExtractPVO — PVO Cross-Module"
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
  - BuUsageExtractPVO
  - buusageextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BuUsageExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bu Usage Extract. Acessa as tabelas: FUN_BU_USAGES.

**Caminho:** `FscmTopModelAM.FinExtractAM.FunBiccExtractAM.BuUsageExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fun_bu_usages|FUN_BU_USAGES]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[fun_bu_usages|FUN_BU_USAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BuUsageBusinessUnitId | BUSINESS_UNIT_ID | 🔑 | ✅ |
| 2 | BuUsageConfigurationStatus | CONFIGURATION_STATUS | — | ✅ |
| 3 | BuUsageCreatedBy | CREATED_BY | — | ✅ |
| 4 | BuUsageCreationDate | CREATION_DATE | — | ✅ |
| 5 | BuUsageLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | BuUsageLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | BuUsageLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | BuUsageModuleId | MODULE_ID | 🔑 | ✅ |
| 9 | BuUsageObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
