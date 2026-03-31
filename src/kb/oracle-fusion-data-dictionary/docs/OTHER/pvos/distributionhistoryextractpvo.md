---
id: DOC-OTHER-PVO-DistributionHistoryExtractPVO
doc_type: system-doc
title: "DistributionHistoryExtractPVO — PVO Cross-Module"
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
  - DistributionHistoryExtractPVO
  - distributionhistoryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DistributionHistoryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Distribution History Extract. Acessa as tabelas: FA_DISTRIBUTION_HISTORY.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.DistributionHistoryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_distribution_history|FA_DISTRIBUTION_HISTORY]] — 20 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[fa_distribution_history|FA_DISTRIBUTION_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionHistoryAssetId | ASSET_ID | — | ✅ |
| 2 | DistributionHistoryAssignedTo | ASSIGNED_TO | — | ✅ |
| 3 | DistributionHistoryBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 4 | DistributionHistoryCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 5 | DistributionHistoryCreatedBy | CREATED_BY | — | ✅ |
| 6 | DistributionHistoryCreationDate | CREATION_DATE | — | ✅ |
| 7 | DistributionHistoryDateEffective | DATE_EFFECTIVE | — | ✅ |
| 8 | DistributionHistoryDateIneffective | DATE_INEFFECTIVE | — | ✅ |
| 9 | DistributionHistoryDistributionId | DISTRIBUTION_ID | 🔑 | ✅ |
| 10 | DistributionHistoryInventoryDateTaken | INVENTORY_DATE_TAKEN | — | ✅ |
| 11 | DistributionHistoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | DistributionHistoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | DistributionHistoryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | DistributionHistoryLocationId | LOCATION_ID | — | ✅ |
| 15 | DistributionHistoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | DistributionHistoryRetirementId | RETIREMENT_ID | — | ✅ |
| 17 | DistributionHistoryTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | ✅ |
| 18 | DistributionHistoryTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | ✅ |
| 19 | DistributionHistoryTransactionUnits | TRANSACTION_UNITS | — | ✅ |
| 20 | DistributionHistoryUnitsAssigned | UNITS_ASSIGNED | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
