---
id: DOC-OTHER-PVO-WOAssetExtractPVO
doc_type: system-doc
title: "WOAssetExtractPVO — PVO Cross-Module"
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
  - WOAssetExtractPVO
  - woassetextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOAssetExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOAsset Extract. Acessa as tabelas: WIE_WO_ASSETS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WieBiccExtractAM.WOAssetExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wie_wo_assets|WIE_WO_ASSETS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[wie_wo_assets|WIE_WO_ASSETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOAssetPEOAssetId | ASSET_ID | — | ✅ |
| 2 | WOAssetPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | WOAssetPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | WOAssetPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 5 | WOAssetPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 6 | WOAssetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | WOAssetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | WOAssetPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | WOAssetPEOLastWoOperationId | LAST_WO_OPERATION_ID | — | ✅ |
| 10 | WOAssetPEOMntCompleteFlag | MNT_COMPLETE_FLAG | — | ✅ |
| 11 | WOAssetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | WOAssetPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 13 | WOAssetPEORequestId | REQUEST_ID | — | ✅ |
| 14 | WOAssetPEOWoAssetId | WO_ASSET_ID | 🔑 | ✅ |
| 15 | WOAssetPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
