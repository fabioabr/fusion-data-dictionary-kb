---
id: DOC-OTHER-PVO-MaintenanceResourcePVO
doc_type: system-doc
title: "MaintenanceResourcePVO — PVO Cross-Module"
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
  - MaintenanceResourcePVO
  - maintenanceresourcepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceResourcePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance Resource. Acessa as tabelas: WIS_RESOURCES_B, WIS_RESOURCES_TL.

**Caminho:** `FscmTopModelAM.ResourceAM.MaintenanceResourcePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 2 | 1 | 7 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[wis_resources_b|WIS_RESOURCES_B]] — 15 atributos (1 PKs, 4 BICC)
- [[wis_resources_tl|WIS_RESOURCES_TL]] — 11 atributos (3 BICC)

---

## ⚙️ Atributos

### [[wis_resources_b|WIS_RESOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceId | RESOURCE_ID | 🔑 | ✅ |
| 2 | ResourcePEOAutoEquipmentFlag | AUTO_EQUIPMENT_FLAG | — | — |
| 3 | ResourcePEOCostedFlag | COSTED_FLAG | — | — |
| 4 | ResourcePEOCreatedBy | CREATED_BY | — | — |
| 5 | ResourcePEOCreationDate | CREATION_DATE | — | — |
| 6 | ResourcePEOInactiveDate | INACTIVE_DATE | — | — |
| 7 | ResourcePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ResourcePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ResourcePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ResourcePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ResourcePEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | ResourcePEOResourceClassCode | RESOURCE_CLASS_CODE | — | — |
| 13 | ResourcePEOResourceCode | RESOURCE_CODE | — | — |
| 14 | ResourcePEOResourceType | RESOURCE_TYPE | — | ✅ |
| 15 | ResourcePEOUomCode | UOM_CODE | — | ✅ |

### [[wis_resources_tl|WIS_RESOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ResourceTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ResourceTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | ResourceTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ResourceTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ResourceTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ResourceTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ResourceTranslationPEOResourceDescription | RESOURCE_DESCRIPTION | — | ✅ |
| 9 | ResourceTranslationPEOResourceId | RESOURCE_ID | — | — |
| 10 | ResourceTranslationPEOResourceName | RESOURCE_NAME | — | ✅ |
| 11 | ResourceTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
