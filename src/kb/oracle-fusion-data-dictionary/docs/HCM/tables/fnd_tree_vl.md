---
id: DOC-HCM-144
doc_type: system-doc
title: "FND_TREE_VL — (título a preencher)"
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
  - FND_TREE_VL
  - fnd_tree_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_TREE_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | DESCRIPTION | — | — | — | — | — | — |
| 4 | ICON_NAME | — | — | — | — | — | — |
| 5 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 6 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 7 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 8 | SET_ID | — | — | — | — | — | — |
| 9 | TREE_CODE | — | — | — | — | — | — |
| 10 | TREE_NAME | — | — | — | — | — | — |
| 11 | TREE_STRUCTURE_CODE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[depttreebicvo|DeptTreeBICVO]] (HCM · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | FndTreeEOCreatedBy | — |
| CREATION_DATE | FndTreeEOCreationDate | — |
| DESCRIPTION | FndTreeEODescription | — |
| ICON_NAME | FndTreeEOIconName | — |
| LAST_UPDATE_DATE | FndTreeEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FndTreeEOLastUpdateLogin | — |
| LAST_UPDATED_BY | FndTreeEOLastUpdatedBy | — |
| SET_ID | FndTreeEOSetId | — |
| TREE_CODE | FndTreeEOTreeCode | ✅ |
| TREE_NAME | FndTreeEOTreeName | ✅ |
| TREE_STRUCTURE_CODE | FndTreeEOTreeStructureCode | — |

### [[flex_treecode_vs_fa_cost_ctr_vi|FLEX_TREECODE_VS_FA_COST_CTR_VI]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TreeCreatedBy | — |
| CREATION_DATE | TreeCreationDate | — |
| DESCRIPTION | TreeDescription | — |
| ICON_NAME | TreeIconName | — |
| LAST_UPDATE_DATE | TreeLastUpdateDate | — |
| LAST_UPDATE_LOGIN | TreeLastUpdateLogin | — |
| LAST_UPDATED_BY | TreeLastUpdatedBy | — |
| SET_ID | TreeSetId | — |
| TREE_CODE | TreeCode | — |
| TREE_NAME | TreeName | — |
| TREE_STRUCTURE_CODE | TreeStructureCode | — |

### [[flex_treecode_vs_gl_account_vi|FLEX_TREECODE_VS_GL_ACCOUNT_VI]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TreeCreatedBy | — |
| CREATION_DATE | TreeCreationDate | — |
| DESCRIPTION | TreeDescription | — |
| ICON_NAME | TreeIconName | — |
| LAST_UPDATE_DATE | TreeLastUpdateDate | — |
| LAST_UPDATE_LOGIN | TreeLastUpdateLogin | — |
| LAST_UPDATED_BY | TreeLastUpdatedBy | — |
| SET_ID | TreeSetId | — |
| TREE_CODE | TreeCode | — |
| TREE_NAME | TreeName | — |
| TREE_STRUCTURE_CODE | TreeStructureCode | — |

### [[flex_treecode_vs_gl_balancing_vi|FLEX_TREECODE_VS_GL_BALANCING_VI]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TreeCreatedBy | — |
| CREATION_DATE | TreeCreationDate | — |
| DESCRIPTION | TreeDescription | — |
| ICON_NAME | TreeIconName | — |
| LAST_UPDATE_DATE | TreeLastUpdateDate | — |
| LAST_UPDATE_LOGIN | TreeLastUpdateLogin | — |
| LAST_UPDATED_BY | TreeLastUpdatedBy | — |
| SET_ID | TreeSetId | — |
| TREE_CODE | TreeCode | — |
| TREE_NAME | TreeName | — |
| TREE_STRUCTURE_CODE | TreeStructureCode | — |

### [[fndtreeandversionvo|FndTreeAndVersionVO]] (HCM · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TreeCreatedBy | ✅ |
| CREATION_DATE | TreeCreationDate | ✅ |
| DESCRIPTION | TreeDescription | ✅ |
| ICON_NAME | TreeIconName | ✅ |
| LAST_UPDATE_DATE | TreeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TreeLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TreeLastUpdatedBy | ✅ |
| SET_ID | TreeSetId | ✅ |
| TREE_CODE | TreeCode | ✅ |
| TREE_NAME | TreeName | ✅ |
| TREE_STRUCTURE_CODE | TreeStructureCode | ✅ |

### [[fndtreevlextractpvo|FndTreeVLExtractPVO]] (OTHER · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| ICON_NAME | IconName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| SET_ID | SetId | ✅ |
| TREE_CODE | TreeCode | ✅ |
| TREE_NAME | TreeName | ✅ |
| TREE_STRUCTURE_CODE | TreeStructureCode | ✅ |

### [[orgtreebicvo|OrgTreeBICVO]] (HCM · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | FndTreeEOCreatedBy | — |
| CREATION_DATE | FndTreeEOCreationDate | — |
| DESCRIPTION | FndTreeEODescription | — |
| ICON_NAME | FndTreeEOIconName | — |
| LAST_UPDATE_DATE | FndTreeEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FndTreeEOLastUpdateLogin | — |
| LAST_UPDATED_BY | FndTreeEOLastUpdatedBy | — |
| SET_ID | FndTreeEOSetId | — |
| TREE_CODE | FndTreeEOTreeCode | ✅ |
| TREE_NAME | FndTreeEOTreeName | ✅ |
| TREE_STRUCTURE_CODE | FndTreeEOTreeStructureCode | — |

### [[orgtreebirvoforfscm|OrgTreeBIRVOForFscm]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | FndTreeEOCreatedBy | — |
| CREATION_DATE | FndTreeEOCreationDate | — |
| DESCRIPTION | FndTreeEODescription | — |
| ICON_NAME | FndTreeEOIconName | — |
| LAST_UPDATE_DATE | FndTreeEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | FndTreeEOLastUpdateLogin | — |
| LAST_UPDATED_BY | FndTreeEOLastUpdatedBy | — |
| SET_ID | FndTreeEOSetId | — |
| TREE_CODE | FndTreeEOTreeCode | — |
| TREE_NAME | FndTreeEOTreeName | — |
| TREE_STRUCTURE_CODE | FndTreeEOTreeStructureCode | — |

### [[positiontreebicvo|PositionTreeBICVO]] (PO · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | FndTreeEOCreatedBy | — |
| CREATION_DATE | FndTreeEOCreationDate | — |
| DESCRIPTION | FndTreeEODescription | — |
| ICON_NAME | FndTreeEOIconName | — |
| LAST_UPDATE_DATE | FndTreeEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FndTreeEOLastUpdateLogin | — |
| LAST_UPDATED_BY | FndTreeEOLastUpdatedBy | — |
| SET_ID | FndTreeEOSetId | — |
| TREE_CODE | FndTreeEOTreeCode | ✅ |
| TREE_NAME | FndTreeEOTreeName | ✅ |
| TREE_STRUCTURE_CODE | FndTreeEOTreeStructureCode | — |
