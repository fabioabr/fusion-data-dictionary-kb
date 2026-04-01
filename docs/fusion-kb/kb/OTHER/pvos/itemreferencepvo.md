---
id: DOC-OTHER-PVO-ItemReferencePVO
doc_type: system-doc
title: "ItemReferencePVO — PVO Cross-Module"
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
  - ItemReferencePVO
  - itemreferencepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemReferencePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Reference. Acessa as tabelas: EGO_CHANGE_LINES_B, EGP_ITEM_CLASSES_B_V, EGP_ITEM_CLASSES_TL (+5).

**Caminho:** `FscmTopModelAM.ChangeObjectsAM.ItemReferencePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 8 | 2 | 5 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_lines_b|EGO_CHANGE_LINES_B]] — 3 atributos
- [[egp_item_classes_b_v|EGP_ITEM_CLASSES_B_V]] — 2 atributos
- [[egp_item_classes_tl|EGP_ITEM_CLASSES_TL]] — 3 atributos (1 BICC)
- [[egp_phases_vl|EGP_PHASES_VL]] — 2 atributos (2 BICC)
- [[egp_system_items_all_v|EGP_SYSTEM_ITEMS_ALL_V]] — 8 atributos (2 PKs, 2 BICC)
- [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]] — 3 atributos
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 3 atributos
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 4 atributos

---

## ⚙️ Atributos

### [[ego_change_lines_b|EGO_CHANGE_LINES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CLBPEOChangeLineId | CHANGE_LINE_ID | — | — |
| 2 | CLBPEOImplementationDate1_1 | IMPLEMENTATION_DATE | — | — |
| 3 | CLBPEOScheduledDate | SCHEDULED_DATE | — | — |

### [[egp_item_classes_b_v|EGP_ITEM_CLASSES_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemClassBasePEOItemClassCode1_1 | ITEM_CLASS_CODE | — | — |
| 2 | ItemClassBasePEOItemClassId | ITEM_CLASS_ID | — | — |

### [[egp_item_classes_tl|EGP_ITEM_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemClassTranPEOItemClassId1_1 | ITEM_CLASS_ID | — | — |
| 2 | ItemClassTranPEOItemClassName | ITEM_CLASS_NAME | — | ✅ |
| 3 | ItemClassTranPEOLanguage3_1 | LANGUAGE | — | — |

### [[egp_phases_vl|EGP_PHASES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhasesPEOPhaseCode | PHASE_CODE | — | ✅ |
| 2 | PhasesPEOPhaseName | PHASE_NAME | — | ✅ |

### [[egp_system_items_all_v|EGP_SYSTEM_ITEMS_ALL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurrentPhaseCode | CURRENT_PHASE_CODE | — | — |
| 2 | ImplementationDate | IMPLEMENTATION_DATE | — | — |
| 3 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 4 | InventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 5 | ItemCatalogGroupId | ITEM_CATALOG_GROUP_ID | — | — |
| 6 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 7 | VersionEndDate | VERSION_END_DATE | — | — |
| 8 | VersionStartDate | VERSION_START_DATE | — | — |

### [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemTranslationPEOInventoryItemId1_1 | INVENTORY_ITEM_ID | — | — |
| 2 | ItemTranslationPEOLanguage | LANGUAGE | — | — |
| 3 | ItemTranslationPEOOrganizationId1_1 | ORGANIZATION_ID | — | — |

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationUnitPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrganizationUnitPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | OrganizationUnitPEOOrganizationId3_1 | ORGANIZATION_ID | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgUnitTransPEOEffectiveEndDate1_1 | EFFECTIVE_END_DATE | — | — |
| 2 | OrgUnitTransPEOEffectiveStartDate1_1 | EFFECTIVE_START_DATE | — | — |
| 3 | OrgUnitTransPEOLanguage2_1 | LANGUAGE | — | — |
| 4 | OrgUnitTransPEOOrganizationId2_1 | ORGANIZATION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
