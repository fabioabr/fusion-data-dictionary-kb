---
id: DOC-HCM-132
doc_type: system-doc
title: "FND_KF_STR_INSTANCES_VL — (título a preencher)"
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
  - FND_KF_STR_INSTANCES_VL
  - fnd_kf_str_instances_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_KF_STR_INSTANCES_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | APPLICATION_ID | — | — | — | — | — | — |
| 2 | CREATED_BY | — | — | — | — | — | — |
| 3 | CREATION_DATE | — | — | — | — | — | — |
| 4 | DESCRIPTION | — | — | — | — | — | — |
| 5 | DYNAMIC_COMBO_CREATION_FLAG | — | — | — | — | — | — |
| 6 | ENABLED_FLAG | — | — | — | — | — | — |
| 7 | KEY_FLEXFIELD_CODE | — | — | — | — | — | — |
| 8 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 9 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 10 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 11 | NAME | — | — | — | — | — | — |
| 12 | SHA_ENABLED_FLAG | — | — | — | — | — | — |
| 13 | STRUCTURE_ID | — | — | — | — | — | — |
| 14 | STRUCTURE_INSTANCE_CODE | — | — | — | — | — | — |
| 15 | STRUCTURE_INSTANCE_ID | — | — | — | — | — | — |
| 16 | STRUCTURE_INSTANCE_IDENTIFIER | — | — | — | — | — | — |
| 17 | STRUCTURE_INSTANCE_NUMBER | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[budgetaccount|BudgetAccount]] (OTHER · BICC: 4/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | FlexStructInstancApplicationId | — |
| CREATED_BY | FlexStructInstancCreatedBy | — |
| CREATION_DATE | FlexStructInstancCreationDate | ✅ |
| DESCRIPTION | FlexStructInstancDescription | ✅ |
| DYNAMIC_COMBO_CREATION_FLAG | FlexStructInstancDynamicCombinationCreationAllowed | — |
| ENABLED_FLAG | FlexStructInstancEnabledFlag1 | — |
| KEY_FLEXFIELD_CODE | FlexStructInstancKeyFlexfieldCode | — |
| LAST_UPDATE_DATE | FlexStructInstancLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FlexStructInstancLastUpdateLogin | — |
| LAST_UPDATED_BY | FlexStructInstancLastUpdatedBy1 | — |
| NAME | FlexStructInstancName | ✅ |
| STRUCTURE_ID | FlexStructInstancStructureId | — |
| STRUCTURE_INSTANCE_CODE | FlexStructInstancStructureInstanceCode | — |
| STRUCTURE_INSTANCE_ID | FlexStructInstancStructureInstanceId | — |
| STRUCTURE_INSTANCE_IDENTIFIER | FlexStructInstancStructureInstanceIdentifier | — |
| STRUCTURE_INSTANCE_NUMBER | FlexStructInstancStructureInstanceNumber | — |

### [[codecombinationpvo|CodeCombinationPVO]] (GL · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | KeyFlexfieldStructureInstancApplicationId | — |
| CREATED_BY | KeyFlexfieldStructureInstancCreatedBy | — |
| CREATION_DATE | KeyFlexfieldStructureInstancCreationDate | — |
| DESCRIPTION | KeyFlexfieldStructureInstancDescription | — |
| ENABLED_FLAG | KeyFlexfieldStructureInstancEnabledFlag | — |
| KEY_FLEXFIELD_CODE | KeyFlexfieldStructureInstancKeyFlexfieldCode | — |
| LAST_UPDATE_DATE | KeyFlexfieldStructureInstancLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | KeyFlexfieldStructureInstancLastUpdateLogin | — |
| LAST_UPDATED_BY | KeyFlexfieldStructureInstancLastUpdatedBy | — |
| NAME | KeyFlexfieldStructureInstancName | ✅ |
| STRUCTURE_ID | KeyFlexfieldStructureInstancStructureId | — |
| STRUCTURE_INSTANCE_CODE | KeyFlexfieldStructureInstancStructureInstanceCode | — |
| STRUCTURE_INSTANCE_ID | KeyFlexfieldStructureInstancStructureInstanceId | — |
| STRUCTURE_INSTANCE_NUMBER | KeyFlexfieldStructureInstancStructureInstanceNumber | — |

### [[fndlookupsp1|FNDLookupsP1]] (OTHER · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | KeyFlexfieldStructureInstanc1ApplicationId | — |
| CREATED_BY | KeyFlexfieldStructureInstanc1CreatedBy | — |
| CREATION_DATE | KeyFlexfieldStructureInstanc1CreationDate | — |
| DESCRIPTION | KeyFlexfieldStructureInstanc1Description | — |
| ENABLED_FLAG | KeyFlexfieldStructureInstanc1EnabledFlag | — |
| KEY_FLEXFIELD_CODE | KeyFlexfieldStructureInstanc1KeyFlexfieldCode | ✅ |
| LAST_UPDATE_DATE | KeyFlexfieldStructureInstanc1LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | KeyFlexfieldStructureInstanc1LastUpdateLogin | — |
| LAST_UPDATED_BY | KeyFlexfieldStructureInstanc1LastUpdatedBy | — |
| NAME | KeyFlexfieldStructureInstanc1Name | — |
| STRUCTURE_ID | KeyFlexfieldStructureInstanc1StructureId | — |
| STRUCTURE_INSTANCE_CODE | KeyFlexfieldStructureInstanc1StructureInstanceCode | — |
| STRUCTURE_INSTANCE_ID | KeyFlexfieldStructureInstanc1StructureInstanceId | — |
| STRUCTURE_INSTANCE_NUMBER | KeyFlexfieldStructureInstanc1StructureInstanceNumber | — |

### [[hcmldgkeyflexfieldstructureinstancepvo|HcmLdgKeyFlexfieldStructureInstancePVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | ApplicationId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DESCRIPTION | Description | — |
| DYNAMIC_COMBO_CREATION_FLAG | DynamicCombinationCreationAllowed | — |
| ENABLED_FLAG | EnabledFlag | — |
| KEY_FLEXFIELD_CODE | KeyFlexfieldCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| NAME | Name | — |
| SHA_ENABLED_FLAG | ShorthandAliasEnabledFlag | — |
| STRUCTURE_ID | StructureId | — |
| STRUCTURE_INSTANCE_CODE | StructureInstanceCode | — |
| STRUCTURE_INSTANCE_ID | StructureInstanceId | — |
| STRUCTURE_INSTANCE_IDENTIFIER | StructureInstanceIdentifier | — |
| STRUCTURE_INSTANCE_NUMBER | StructureInstanceNumber | — |

### [[ledgerpvo|LedgerPVO]] (GL · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | KeyFlexfieldStructureInstancApplicationId | — |
| DESCRIPTION | KeyFlexfieldStructureInstancDescription | — |
| ENABLED_FLAG | KeyFlexfieldStructureInstancEnabledFlag | — |
| KEY_FLEXFIELD_CODE | KeyFlexfieldStructureInstancKeyFlexfieldCode | — |
| NAME | KeyFlexfieldStructureInstancName | ✅ |
| STRUCTURE_ID | KeyFlexfieldStructureInstancStructureId | — |
| STRUCTURE_INSTANCE_CODE | KeyFlexfieldStructureInstancStructureInstanceCode | — |
| STRUCTURE_INSTANCE_ID | KeyFlexfieldStructureInstancStructureInstanceId | — |
| STRUCTURE_INSTANCE_NUMBER | KeyFlexfieldStructureInstancStructureInstanceNumber | — |

### [[ledgersetpvo|LedgerSetPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | KeyFlexfieldStructureInstancApplicationId | — |
| DESCRIPTION | KeyFlexfieldStructureInstancDescription | — |
| ENABLED_FLAG | KeyFlexfieldStructureInstancEnabledFlag | — |
| KEY_FLEXFIELD_CODE | KeyFlexfieldStructureInstancKeyFlexfieldCode | — |
| NAME | KeyFlexfieldStructureInstancName | — |
| STRUCTURE_ID | KeyFlexfieldStructureInstancStructureId | — |
| STRUCTURE_INSTANCE_CODE | KeyFlexfieldStructureInstancStructureInstanceCode | — |
| STRUCTURE_INSTANCE_ID | KeyFlexfieldStructureInstancStructureInstanceId | — |
| STRUCTURE_INSTANCE_NUMBER | KeyFlexfieldStructureInstancStructureInstanceNumber | — |

### [[locatorflexfieldextractpvo|LocatorFlexfieldExtractPVO]] (OTHER · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | LocatorFlexfieldPVO_FLEX_ApplicationId | ✅ |
| KEY_FLEXFIELD_CODE | LocatorFlexfieldPVO_FLEX_KeyFlexfieldCode | ✅ |
| STRUCTURE_INSTANCE_CODE | LocatorFlexfieldPVO_FLEX_StructureInstanceCode | ✅ |
| STRUCTURE_INSTANCE_ID | LocatorFlexfieldPVO_FLEX_StructureInstanceId | ✅ |

### [[pricingcombinationpvo|PricingCombinationPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | KFFStrucInstApplicationId | — |
| KEY_FLEXFIELD_CODE | KFFStrucInstKeyFlexFieldCode | — |
| STRUCTURE_INSTANCE_ID | KFFStrucInstStructInstanceId | — |
