---
id: DOC-OTHER-PVO-InvMaterialStatusesExtractPVO
doc_type: system-doc
title: "InvMaterialStatusesExtractPVO — PVO Cross-Module"
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
  - InvMaterialStatusesExtractPVO
  - invmaterialstatusesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvMaterialStatusesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Material Statuses Extract. Acessa as tabelas: INV_MATERIAL_STATUSES_B, INV_MATERIAL_STATUSES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.InvMaterialStatusesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 2 | 2 | 30 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_material_statuses_b|INV_MATERIAL_STATUSES_B]] — 19 atributos (19 BICC)
- [[inv_material_statuses_tl|INV_MATERIAL_STATUSES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[inv_material_statuses_b|INV_MATERIAL_STATUSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvMaterialStatusBPEOAvailabilityType | AVAILABILITY_TYPE | — | ✅ |
| 2 | InvMaterialStatusBPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | InvMaterialStatusBPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | InvMaterialStatusBPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 5 | InvMaterialStatusBPEOInventoryAtpCode | INVENTORY_ATP_CODE | — | ✅ |
| 6 | InvMaterialStatusBPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 7 | InvMaterialStatusBPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 8 | InvMaterialStatusBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | InvMaterialStatusBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | InvMaterialStatusBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | InvMaterialStatusBPEOLocatorControl | LOCATOR_CONTROL | — | ✅ |
| 12 | InvMaterialStatusBPEOLotControl | LOT_CONTROL | — | ✅ |
| 13 | InvMaterialStatusBPEOLpnControl | LPN_CONTROL | — | ✅ |
| 14 | InvMaterialStatusBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | InvMaterialStatusBPEORequestId | REQUEST_ID | — | ✅ |
| 16 | InvMaterialStatusBPEOReservableType | RESERVABLE_TYPE | — | ✅ |
| 17 | InvMaterialStatusBPEOSerialControl | SERIAL_CONTROL | — | ✅ |
| 18 | InvMaterialStatusBPEOStatusId | STATUS_ID | — | ✅ |
| 19 | InvMaterialStatusBPEOZoneControl | ZONE_CONTROL | — | ✅ |

### [[inv_material_statuses_tl|INV_MATERIAL_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvStatusTlPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InvStatusTlPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InvStatusTlPEODescription | DESCRIPTION | — | ✅ |
| 4 | InvStatusTlPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | InvStatusTlPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | InvStatusTlPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | InvStatusTlPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | InvStatusTlPEOSourceLang | SOURCE_LANG | — | ✅ |
| 9 | InvStatusTlPEOStatusCode | STATUS_CODE | — | ✅ |
| 10 | Language | LANGUAGE | 🔑 | ✅ |
| 11 | StatusId | STATUS_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
