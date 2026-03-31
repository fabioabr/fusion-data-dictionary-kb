---
id: DOC-HCM-PVO-OrgTreeBIRVOForFscm
doc_type: system-doc
title: "OrgTreeBIRVOForFscm — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - OrgTreeBIRVOForFscm
  - orgtreebirvoforfscm
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrgTreeBIRVOForFscm

## 📌 Visão Geral

Disponibiliza árvores organizacionais formatadas para integração com FSCM, incluindo ancestrais e nós de referência. Permite alinhamento entre hierarquias HCM e financeiras.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.OrganizationAM.OrgTreeBIRVOForFscm`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 86 | 4 | 6 | 28 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_tree_version_vl|FND_TREE_VERSION_VL]] — 23 atributos
- [[fnd_tree_vl|FND_TREE_VL]] — 11 atributos
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 24 atributos
- [[per_org_tree_node_rf|PER_ORG_TREE_NODE_RF]] — 28 atributos (6 PKs, 28 BICC)

---

## ⚙️ Atributos

### [[fnd_tree_version_vl|FND_TREE_VERSION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FndTreeVersionEffDateEOChangedSinceValidation | CHANGED_SINCE_VALIDATION | — | — |
| 2 | FndTreeVersionEffDateEOCreatedBy | CREATED_BY | — | — |
| 3 | FndTreeVersionEffDateEOCreationDate | CREATION_DATE | — | — |
| 4 | FndTreeVersionEffDateEODescription | DESCRIPTION | — | — |
| 5 | FndTreeVersionEffDateEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | FndTreeVersionEffDateEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | FndTreeVersionEffDateEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | FndTreeVersionEffDateEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | FndTreeVersionEffDateEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | FndTreeVersionEffDateEOLastValidationDate | LAST_VALIDATION_DATE | — | — |
| 11 | FndTreeVersionEffDateEOLastValidationResult | LAST_VALIDATION_RESULT | — | — |
| 12 | FndTreeVersionEffDateEOLastValidationResultId | LAST_VALIDATION_RESULT_ID | — | — |
| 13 | FndTreeVersionEffDateEOLevelCount | LEVEL_COUNT | — | — |
| 14 | FndTreeVersionEffDateEOLockDate | LOCK_DATE | — | — |
| 15 | FndTreeVersionEffDateEOLockedBy | LOCKED_BY | — | — |
| 16 | FndTreeVersionEffDateEONodeCount | NODE_COUNT | — | — |
| 17 | FndTreeVersionEffDateEOSourceTreeVersionId | SOURCE_TREE_VERSION_ID | — | — |
| 18 | FndTreeVersionEffDateEOStatus | STATUS | — | — |
| 19 | FndTreeVersionEffDateEOTreeCode | TREE_CODE | — | — |
| 20 | FndTreeVersionEffDateEOTreeStructureCode | TREE_STRUCTURE_CODE | — | — |
| 21 | FndTreeVersionEffDateEOTreeVersionId | TREE_VERSION_ID | — | — |
| 22 | FndTreeVersionEffDateEOTreeVersionName | TREE_VERSION_NAME | — | — |
| 23 | FndTreeVersionEffDateEOVersionComment | VERSION_COMMENT | — | — |

### [[fnd_tree_vl|FND_TREE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FndTreeEOCreatedBy | CREATED_BY | — | — |
| 2 | FndTreeEOCreationDate | CREATION_DATE | — | — |
| 3 | FndTreeEODescription | DESCRIPTION | — | — |
| 4 | FndTreeEOIconName | ICON_NAME | — | — |
| 5 | FndTreeEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | FndTreeEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | FndTreeEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | FndTreeEOSetId | SET_ID | — | — |
| 9 | FndTreeEOTreeCode | TREE_CODE | — | — |
| 10 | FndTreeEOTreeName | TREE_NAME | — | — |
| 11 | FndTreeEOTreeStructureCode | TREE_STRUCTURE_CODE | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AncestorOrgUnitTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | AncestorOrgUnitTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | AncestorOrgUnitTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | AncestorOrgUnitTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 5 | AncestorOrgUnitTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | AncestorOrgUnitTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | AncestorOrgUnitTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AncestorOrgUnitTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AncestorOrgUnitTranslationPEOName | NAME | — | — |
| 10 | AncestorOrgUnitTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | AncestorOrgUnitTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | AncestorOrgUnitTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 13 | ChildOrgUnitTranslationPEOCreatedBy | CREATED_BY | — | — |
| 14 | ChildOrgUnitTranslationPEOCreationDate | CREATION_DATE | — | — |
| 15 | ChildOrgUnitTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 16 | ChildOrgUnitTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 17 | ChildOrgUnitTranslationPEOLanguage | LANGUAGE | — | — |
| 18 | ChildOrgUnitTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 19 | ChildOrgUnitTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | ChildOrgUnitTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | ChildOrgUnitTranslationPEOName | NAME | — | — |
| 22 | ChildOrgUnitTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | ChildOrgUnitTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 24 | ChildOrgUnitTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[per_org_tree_node_rf|PER_ORG_TREE_NODE_RF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AncestorDataSourceId | ANCESTOR_DATA_SOURCE_ID | — | ✅ |
| 2 | AncestorPk1Value | ANCESTOR_PK1_VALUE | — | ✅ |
| 3 | AncestorPk2Value | ANCESTOR_PK2_VALUE | — | ✅ |
| 4 | AncestorPk3Value | ANCESTOR_PK3_VALUE | — | ✅ |
| 5 | AncestorPk4Value | ANCESTOR_PK4_VALUE | — | ✅ |
| 6 | AncestorPk5Value | ANCESTOR_PK5_VALUE | — | ✅ |
| 7 | AncestorTreeLabelId | ANCESTOR_TREE_LABEL_ID | — | ✅ |
| 8 | AncestorTreeNodeId | ANCESTOR_TREE_NODE_ID | — | ✅ |
| 9 | CreatedBy | CREATED_BY | — | ✅ |
| 10 | CreationDate | CREATION_DATE | — | ✅ |
| 11 | DataSourceId | DATA_SOURCE_ID | — | ✅ |
| 12 | Distance | DISTANCE | — | ✅ |
| 13 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 14 | IsLeaf | IS_LEAF | — | ✅ |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | Pk1Value | PK1_VALUE | — | ✅ |
| 19 | Pk2Value | PK2_VALUE | — | ✅ |
| 20 | Pk3Value | PK3_VALUE | — | ✅ |
| 21 | Pk4Value | PK4_VALUE | — | ✅ |
| 22 | Pk5Value | PK5_VALUE | — | ✅ |
| 23 | RfTreeNodeId | RF_TREE_NODE_ID | 🔑 | ✅ |
| 24 | TreeCode | TREE_CODE | 🔑 | ✅ |
| 25 | TreeLabelId | TREE_LABEL_ID | — | ✅ |
| 26 | TreeNodeId | TREE_NODE_ID | 🔑 | ✅ |
| 27 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |
| 28 | TreeVersionId | TREE_VERSION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
