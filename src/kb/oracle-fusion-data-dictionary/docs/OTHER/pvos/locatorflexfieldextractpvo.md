---
id: DOC-OTHER-PVO-LocatorFlexfieldExtractPVO
doc_type: system-doc
title: "LocatorFlexfieldExtractPVO — PVO Cross-Module"
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
  - LocatorFlexfieldExtractPVO
  - locatorflexfieldextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LocatorFlexfieldExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Locator Flexfield Extract. Acessa as tabelas: FND_KF_STR_INSTANCES_VL, INV_ITEM_LOCATIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.LocatorFlexfieldExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 2 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_kf_str_instances_vl|FND_KF_STR_INSTANCES_VL]] — 4 atributos (1 PKs, 4 BICC)
- [[inv_item_locations|INV_ITEM_LOCATIONS]] — 8 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[fnd_kf_str_instances_vl|FND_KF_STR_INSTANCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocatorFlexfieldPVO_FLEX_ApplicationId | APPLICATION_ID | — | ✅ |
| 2 | LocatorFlexfieldPVO_FLEX_KeyFlexfieldCode | KEY_FLEXFIELD_CODE | — | ✅ |
| 3 | LocatorFlexfieldPVO_FLEX_StructureInstanceCode | STRUCTURE_INSTANCE_CODE | — | ✅ |
| 4 | LocatorFlexfieldPVO_FLEX_StructureInstanceId | STRUCTURE_INSTANCE_ID | 🔑 | ✅ |

### [[inv_item_locations|INV_ITEM_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocatorFlexfieldPVOCreationDate | CREATION_DATE | — | ✅ |
| 2 | LocatorFlexfieldPVOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 3 | LocatorFlexfieldPVOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 4 | LocatorFlexfieldPVOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LocatorFlexfieldPVOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 6 | LocatorFlexfieldPVO_INVENTORY_LOCATION_ID | INVENTORY_LOCATION_ID | 🔑 | ✅ |
| 7 | LocatorFlexfieldPVO_STRUCTURE_INSTANCE_NUMBER | STRUCTURE_INSTANCE_NUMBER | — | ✅ |
| 8 | LocatorFlexfieldPVO_SUBINVENTORY_ID | SUBINVENTORY_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
