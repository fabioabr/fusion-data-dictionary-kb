---
id: DOC-HCM-143
doc_type: system-doc
title: "FND_TREE_VERSION_VL — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - FND_TREE_VERSION_VL
  - fnd_tree_version_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_TREE_VERSION_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHANGED_SINCE_VALIDATION | — | — | — | — | — | — |
| 2 | CREATED_BY | — | — | — | — | — | — |
| 3 | CREATION_DATE | — | — | — | — | — | — |
| 4 | DESCRIPTION | — | — | — | — | — | — |
| 5 | EFFECTIVE_END_DATE | — | — | — | — | — | — |
| 6 | EFFECTIVE_START_DATE | — | — | — | — | — | — |
| 7 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 8 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 9 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 10 | LAST_VALIDATION_DATE | — | — | — | — | — | — |
| 11 | LAST_VALIDATION_RESULT | — | — | — | — | — | — |
| 12 | LAST_VALIDATION_RESULT_ID | — | — | — | — | — | — |
| 13 | LEVEL_COUNT | — | — | — | — | — | — |
| 14 | LOCKED_BY | — | — | — | — | — | — |
| 15 | LOCK_DATE | — | — | — | — | — | — |
| 16 | NODE_COUNT | — | — | — | — | — | — |
| 17 | SOURCE_TREE_VERSION_ID | — | — | — | — | — | — |
| 18 | STATUS | — | — | — | — | — | — |
| 19 | TREE_CODE | — | — | — | — | — | — |
| 20 | TREE_STRUCTURE_CODE | — | — | — | — | — | — |
| 21 | TREE_VERSION_ID | — | — | — | — | — | — |
| 22 | TREE_VERSION_NAME | — | — | — | — | — | — |
| 23 | VERSION_COMMENT | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[depttreebicvo|DeptTreeBICVO]] (HCM · BICC: 5/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHANGED_SINCE_VALIDATION | FndTreeVersionEffDateEOChangedSinceValidation | — |
| CREATED_BY | FndTreeVersionEffDateEOCreatedBy | — |
| CREATION_DATE | FndTreeVersionEffDateEOCreationDate | — |
| DESCRIPTION | FndTreeVersionEffDateEODescription | — |
| EFFECTIVE_END_DATE | FndTreeVersionEffDateEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | FndTreeVersionEffDateEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | FndTreeVersionEffDateEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FndTreeVersionEffDateEOLastUpdateLogin | — |
| LAST_UPDATED_BY | FndTreeVersionEffDateEOLastUpdatedBy | — |
| LAST_VALIDATION_DATE | FndTreeVersionEffDateEOLastValidationDate | — |
| LAST_VALIDATION_RESULT | FndTreeVersionEffDateEOLastValidationResult | — |
| LAST_VALIDATION_RESULT_ID | FndTreeVersionEffDateEOLastValidationResultId | — |
| LEVEL_COUNT | FndTreeVersionEffDateEOLevelCount | — |
| LOCK_DATE | FndTreeVersionEffDateEOLockDate | — |
| LOCKED_BY | FndTreeVersionEffDateEOLockedBy | — |
| NODE_COUNT | FndTreeVersionEffDateEONodeCount | — |
| SOURCE_TREE_VERSION_ID | FndTreeVersionEffDateEOSourceTreeVersionId | — |
| STATUS | FndTreeVersionEffDateEOStatus | ✅ |
| TREE_CODE | FndTreeVersionEffDateEOTreeCode | — |
| TREE_STRUCTURE_CODE | FndTreeVersionEffDateEOTreeStructureCode | — |
| TREE_VERSION_ID | FndTreeVersionEffDateEOTreeVersionId | — |
| TREE_VERSION_NAME | FndTreeVersionEffDateEOTreeVersionName | ✅ |
| VERSION_COMMENT | FndTreeVersionEffDateEOVersionComment | — |

### [[flex_treecode_vs_fa_cost_ctr_vi|FLEX_TREECODE_VS_FA_COST_CTR_VI]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | VersionCreatedBy | — |
| CREATION_DATE | VersionCreationDate | — |
| DESCRIPTION | VersionDescription | — |
| EFFECTIVE_END_DATE | VersionEffectiveEndDate | — |
| EFFECTIVE_START_DATE | VersionEffectiveStartDate | — |
| LAST_UPDATE_DATE | VersionLastUpdateDate | — |
| LAST_UPDATE_LOGIN | VersionLastUpdateLogin | — |
| LAST_UPDATED_BY | VersionLastUpdatedBy | — |
| STATUS | VersionStatus | — |
| TREE_CODE | VersionTreeCode | — |
| TREE_STRUCTURE_CODE | VersionTreeStructureCode | — |
| TREE_VERSION_ID | TreeVersionId | — |
| TREE_VERSION_NAME | VersionName | — |

### [[flex_treecode_vs_gl_account_vi|FLEX_TREECODE_VS_GL_ACCOUNT_VI]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | VersionCreatedBy | — |
| CREATION_DATE | VersionCreationDate | — |
| DESCRIPTION | VersionDescription | — |
| EFFECTIVE_END_DATE | VersionEffectiveEndDate | — |
| EFFECTIVE_START_DATE | VersionEffectiveStartDate | — |
| LAST_UPDATE_DATE | VersionLastUpdateDate | — |
| LAST_UPDATE_LOGIN | VersionLastUpdateLogin | — |
| LAST_UPDATED_BY | VersionLastUpdatedBy | — |
| STATUS | VersionStatus | — |
| TREE_CODE | VersionTreeCode | — |
| TREE_STRUCTURE_CODE | VersionTreeStructureCode | — |
| TREE_VERSION_ID | TreeVersionId | — |
| TREE_VERSION_NAME | VersionName | — |

### [[flex_treecode_vs_gl_balancing_vi|FLEX_TREECODE_VS_GL_BALANCING_VI]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | VersionCreatedBy | — |
| CREATION_DATE | VersionCreationDate | — |
| DESCRIPTION | VersionDescription | — |
| EFFECTIVE_END_DATE | VersionEffectiveEndDate | — |
| EFFECTIVE_START_DATE | VersionEffectiveStartDate | — |
| LAST_UPDATE_DATE | VersionLastUpdateDate | — |
| LAST_UPDATE_LOGIN | VersionLastUpdateLogin | — |
| LAST_UPDATED_BY | VersionLastUpdatedBy | — |
| STATUS | VersionStatus | — |
| TREE_CODE | VersionTreeCode | — |
| TREE_STRUCTURE_CODE | VersionTreeStructureCode | — |
| TREE_VERSION_ID | TreeVersionId | — |
| TREE_VERSION_NAME | VersionName | — |

### [[fndtreeandversionvo|FndTreeAndVersionVO]] (HCM · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | VersionCreatedBy | ✅ |
| CREATION_DATE | VersionCreationDate | ✅ |
| DESCRIPTION | VersionDescription | ✅ |
| EFFECTIVE_END_DATE | VersionEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | VersionEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | VersionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | VersionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | VersionLastUpdatedBy | ✅ |
| STATUS | VersionStatus | ✅ |
| TREE_CODE | VersionTreeCode | ✅ |
| TREE_STRUCTURE_CODE | VersionTreeStructureCode | ✅ |
| TREE_VERSION_ID | TreeVersionId | ✅ |
| TREE_VERSION_NAME | VersionName | ✅ |

### [[fndtreeversiondeptvo|FndTreeVersionDeptVO]] (HCM · BICC: 6/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHANGED_SINCE_VALIDATION | ChangedSinceValidation | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DESCRIPTION | Description | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LAST_VALIDATION_DATE | LastValidationDate | — |
| LAST_VALIDATION_RESULT | LastValidationResult | — |
| LAST_VALIDATION_RESULT_ID | LastValidationResultId | — |
| LEVEL_COUNT | LevelCount | — |
| LOCK_DATE | LockDate | — |
| LOCKED_BY | LockedBy | — |
| NODE_COUNT | NodeCount | — |
| SOURCE_TREE_VERSION_ID | SourceTreeVersionId | — |
| STATUS | Status | — |
| TREE_CODE | TreeCode | ✅ |
| TREE_STRUCTURE_CODE | TreeStructureCode | ✅ |
| TREE_VERSION_ID | TreeVersionId | ✅ |
| TREE_VERSION_NAME | TreeVersionName | — |
| VERSION_COMMENT | VersionComment | — |

### [[fndtreeversionorgvo|FndTreeVersionOrgVO]] (HCM · BICC: 6/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHANGED_SINCE_VALIDATION | ChangedSinceValidation | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DESCRIPTION | Description | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LAST_VALIDATION_DATE | LastValidationDate | — |
| LAST_VALIDATION_RESULT | LastValidationResult | — |
| LAST_VALIDATION_RESULT_ID | LastValidationResultId | — |
| LEVEL_COUNT | LevelCount | — |
| LOCK_DATE | LockDate | — |
| LOCKED_BY | LockedBy | — |
| NODE_COUNT | NodeCount | — |
| SOURCE_TREE_VERSION_ID | SourceTreeVersionId | — |
| STATUS | Status | — |
| TREE_CODE | TreeCode | ✅ |
| TREE_STRUCTURE_CODE | TreeStructureCode | ✅ |
| TREE_VERSION_ID | TreeVersionId | ✅ |
| TREE_VERSION_NAME | TreeVersionName | — |
| VERSION_COMMENT | VersionComment | — |

### [[fndtreeversionvlextractpvo|FndTreeVersionVLExtractPVO]] (OTHER · BICC: 23/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHANGED_SINCE_VALIDATION | ChangedSinceValidation | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LAST_VALIDATION_DATE | LastValidationDate | ✅ |
| LAST_VALIDATION_RESULT | LastValidationResult | ✅ |
| LAST_VALIDATION_RESULT_ID | LastValidationResultId | ✅ |
| LEVEL_COUNT | LevelCount | ✅ |
| LOCK_DATE | LockDate | ✅ |
| LOCKED_BY | LockedBy | ✅ |
| NODE_COUNT | NodeCount | ✅ |
| SOURCE_TREE_VERSION_ID | SourceTreeVersionId | ✅ |
| STATUS | Status | ✅ |
| TREE_CODE | TreeCode | ✅ |
| TREE_STRUCTURE_CODE | TreeStructureCode | ✅ |
| TREE_VERSION_ID | TreeVersionId | ✅ |
| TREE_VERSION_NAME | TreeVersionName | ✅ |
| VERSION_COMMENT | VersionComment | ✅ |

### [[fndtreeversionvo|FndTreeVersionVO]] (HCM · BICC: 23/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHANGED_SINCE_VALIDATION | ChangedSinceValidation | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LAST_VALIDATION_DATE | LastValidationDate | ✅ |
| LAST_VALIDATION_RESULT | LastValidationResult | ✅ |
| LAST_VALIDATION_RESULT_ID | LastValidationResultId | ✅ |
| LEVEL_COUNT | LevelCount | ✅ |
| LOCK_DATE | LockDate | ✅ |
| LOCKED_BY | LockedBy | ✅ |
| NODE_COUNT | NodeCount | ✅ |
| SOURCE_TREE_VERSION_ID | SourceTreeVersionId | ✅ |
| STATUS | Status | ✅ |
| TREE_CODE | TreeCode | ✅ |
| TREE_STRUCTURE_CODE | TreeStructureCode | ✅ |
| TREE_VERSION_ID | TreeVersionId | ✅ |
| TREE_VERSION_NAME | TreeVersionName | ✅ |
| VERSION_COMMENT | VersionComment | ✅ |

### [[orgtreebicvo|OrgTreeBICVO]] (HCM · BICC: 5/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHANGED_SINCE_VALIDATION | FndTreeVersionEffDateEOChangedSinceValidation | — |
| CREATED_BY | FndTreeVersionEffDateEOCreatedBy | — |
| CREATION_DATE | FndTreeVersionEffDateEOCreationDate | — |
| DESCRIPTION | FndTreeVersionEffDateEODescription | — |
| EFFECTIVE_END_DATE | FndTreeVersionEffDateEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | FndTreeVersionEffDateEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | FndTreeVersionEffDateEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FndTreeVersionEffDateEOLastUpdateLogin | — |
| LAST_UPDATED_BY | FndTreeVersionEffDateEOLastUpdatedBy | — |
| LAST_VALIDATION_DATE | FndTreeVersionEffDateEOLastValidationDate | — |
| LAST_VALIDATION_RESULT | FndTreeVersionEffDateEOLastValidationResult | — |
| LAST_VALIDATION_RESULT_ID | FndTreeVersionEffDateEOLastValidationResultId | — |
| LEVEL_COUNT | FndTreeVersionEffDateEOLevelCount | — |
| LOCK_DATE | FndTreeVersionEffDateEOLockDate | — |
| LOCKED_BY | FndTreeVersionEffDateEOLockedBy | — |
| NODE_COUNT | FndTreeVersionEffDateEONodeCount | — |
| SOURCE_TREE_VERSION_ID | FndTreeVersionEffDateEOSourceTreeVersionId | — |
| STATUS | FndTreeVersionEffDateEOStatus | ✅ |
| TREE_CODE | FndTreeVersionEffDateEOTreeCode | — |
| TREE_STRUCTURE_CODE | FndTreeVersionEffDateEOTreeStructureCode | — |
| TREE_VERSION_ID | FndTreeVersionEffDateEOTreeVersionId | — |
| TREE_VERSION_NAME | FndTreeVersionEffDateEOTreeVersionName | ✅ |
| VERSION_COMMENT | FndTreeVersionEffDateEOVersionComment | — |

### [[orgtreebirvoforfscm|OrgTreeBIRVOForFscm]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHANGED_SINCE_VALIDATION | FndTreeVersionEffDateEOChangedSinceValidation | — |
| CREATED_BY | FndTreeVersionEffDateEOCreatedBy | — |
| CREATION_DATE | FndTreeVersionEffDateEOCreationDate | — |
| DESCRIPTION | FndTreeVersionEffDateEODescription | — |
| EFFECTIVE_END_DATE | FndTreeVersionEffDateEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | FndTreeVersionEffDateEOEffectiveStartDate | — |
| LAST_UPDATE_DATE | FndTreeVersionEffDateEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | FndTreeVersionEffDateEOLastUpdateLogin | — |
| LAST_UPDATED_BY | FndTreeVersionEffDateEOLastUpdatedBy | — |
| LAST_VALIDATION_DATE | FndTreeVersionEffDateEOLastValidationDate | — |
| LAST_VALIDATION_RESULT | FndTreeVersionEffDateEOLastValidationResult | — |
| LAST_VALIDATION_RESULT_ID | FndTreeVersionEffDateEOLastValidationResultId | — |
| LEVEL_COUNT | FndTreeVersionEffDateEOLevelCount | — |
| LOCK_DATE | FndTreeVersionEffDateEOLockDate | — |
| LOCKED_BY | FndTreeVersionEffDateEOLockedBy | — |
| NODE_COUNT | FndTreeVersionEffDateEONodeCount | — |
| SOURCE_TREE_VERSION_ID | FndTreeVersionEffDateEOSourceTreeVersionId | — |
| STATUS | FndTreeVersionEffDateEOStatus | — |
| TREE_CODE | FndTreeVersionEffDateEOTreeCode | — |
| TREE_STRUCTURE_CODE | FndTreeVersionEffDateEOTreeStructureCode | — |
| TREE_VERSION_ID | FndTreeVersionEffDateEOTreeVersionId | — |
| TREE_VERSION_NAME | FndTreeVersionEffDateEOTreeVersionName | — |
| VERSION_COMMENT | FndTreeVersionEffDateEOVersionComment | — |

### [[positiontreebicvo|PositionTreeBICVO]] (PO · BICC: 3/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHANGED_SINCE_VALIDATION | FndTreeVersionEffDateEOChangedSinceValidation | — |
| CREATED_BY | FndTreeVersionEffDateEOCreatedBy | — |
| CREATION_DATE | FndTreeVersionEffDateEOCreationDate | — |
| DESCRIPTION | FndTreeVersionEffDateEODescription | — |
| EFFECTIVE_END_DATE | FndTreeVersionEffDateEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | FndTreeVersionEffDateEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | FndTreeVersionEffDateEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FndTreeVersionEffDateEOLastUpdateLogin | — |
| LAST_UPDATED_BY | FndTreeVersionEffDateEOLastUpdatedBy | — |
| LAST_VALIDATION_DATE | FndTreeVersionEffDateEOLastValidationDate | — |
| LAST_VALIDATION_RESULT | FndTreeVersionEffDateEOLastValidationResult | — |
| LAST_VALIDATION_RESULT_ID | FndTreeVersionEffDateEOLastValidationResultId | — |
| LEVEL_COUNT | FndTreeVersionEffDateEOLevelCount | — |
| LOCK_DATE | FndTreeVersionEffDateEOLockDate | — |
| LOCKED_BY | FndTreeVersionEffDateEOLockedBy | — |
| NODE_COUNT | FndTreeVersionEffDateEONodeCount | — |
| SOURCE_TREE_VERSION_ID | FndTreeVersionEffDateEOSourceTreeVersionId | — |
| STATUS | FndTreeVersionEffDateEOStatus | ✅ |
| TREE_CODE | FndTreeVersionEffDateEOTreeCode | — |
| TREE_STRUCTURE_CODE | FndTreeVersionEffDateEOTreeStructureCode | — |
| TREE_VERSION_ID | FndTreeVersionEffDateEOTreeVersionId | — |
| TREE_VERSION_NAME | FndTreeVersionEffDateEOTreeVersionName | — |
| VERSION_COMMENT | FndTreeVersionEffDateEOVersionComment | — |

### [[resourcepartnerpvo|ResourcePartnerPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| STATUS | FndTreeVerStatus | — |
| TREE_CODE | TreeCode | — |
| TREE_STRUCTURE_CODE | TreeStructureCode | — |
| TREE_VERSION_ID | TreeVersionId | — |
