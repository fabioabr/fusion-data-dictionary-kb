---
id: DOC-HCM-887
doc_type: system-doc
title: "ZX_FC_TYPES_VL — (título a preencher)"
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
  - ZX_FC_TYPES_VL
  - zx_fc_types_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_FC_TYPES_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CLASSIFICATION_TYPE_CATEG_CODE | — | — | — | — | — | — |
| 2 | CLASSIFICATION_TYPE_CODE | — | — | — | — | — | — |
| 3 | CLASSIFICATION_TYPE_GROUP_CODE | — | — | — | — | — | — |
| 4 | CLASSIFICATION_TYPE_ID | — | — | — | — | — | — |
| 5 | CLASSIFICATION_TYPE_LEVEL_CODE | — | — | — | — | — | — |
| 6 | CLASSIFICATION_TYPE_NAME | — | — | — | — | — | — |
| 7 | CREATED_BY | — | — | — | — | — | — |
| 8 | CREATION_DATE | — | — | — | — | — | — |
| 9 | DELIMITER | — | — | — | — | — | — |
| 10 | EFFECTIVE_FROM | — | — | — | — | — | — |
| 11 | EFFECTIVE_TO | — | — | — | — | — | — |
| 12 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 13 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 14 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 15 | NUM_CHARACTERS | — | — | — | — | — | — |
| 16 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 17 | OWNER_ID_CHAR | — | — | — | — | — | — |
| 18 | OWNER_ID_NUM | — | — | — | — | — | — |
| 19 | OWNER_TABLE_CODE | — | — | — | — | — | — |
| 20 | PROGRAM_APP_NAME | — | — | — | — | — | — |
| 21 | PROGRAM_LOGIN_ID | — | — | — | — | — | — |
| 22 | PROGRAM_NAME | — | — | — | — | — | — |
| 23 | RECORD_TYPE_CODE | — | — | — | — | — | — |
| 24 | REQUEST_ID | — | — | — | — | — | — |
| 25 | START_POSITION | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[sitetaxclassification|SiteTaxClassification]] (AR · BICC: 3/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_TYPE_CATEG_CODE | FiscalClassTypeClassificationTypeCategCode | — |
| CLASSIFICATION_TYPE_CODE | FiscalClassTypeClassificationTypeCode | ✅ |
| CLASSIFICATION_TYPE_GROUP_CODE | FiscalClassTypeClassificationTypeGroupCode | — |
| CLASSIFICATION_TYPE_ID | FiscalClassTypeClassificationTypeId | — |
| CLASSIFICATION_TYPE_LEVEL_CODE | FiscalClassTypeClassificationTypeLevelCode | — |
| CLASSIFICATION_TYPE_NAME | FiscalClassTypeClassificationTypeName | ✅ |
| CREATED_BY | FiscalClassTypeCreatedBy | — |
| CREATION_DATE | FiscalClassTypeCreationDate | — |
| DELIMITER | FiscalClassTypeDelimiter | — |
| EFFECTIVE_FROM | FiscalClassTypeEffectiveFrom | — |
| EFFECTIVE_TO | FiscalClassTypeEffectiveTo | — |
| LAST_UPDATE_DATE | FiscalClassTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FiscalClassTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | FiscalClassTypeLastUpdatedBy | — |
| NUM_CHARACTERS | FiscalClassTypeNumCharacters | — |
| OBJECT_VERSION_NUMBER | FiscalClassTypeObjectVersionNumber | — |
| OWNER_ID_CHAR | FiscalClassTypeOwnerIdChar | — |
| OWNER_ID_NUM | FiscalClassTypeOwnerIdNum | — |
| OWNER_TABLE_CODE | FiscalClassTypeOwnerTableCode | — |
| PROGRAM_APP_NAME | FiscalClassTypeProgramAppName | — |
| PROGRAM_LOGIN_ID | FiscalClassTypeProgramLoginId | — |
| PROGRAM_NAME | FiscalClassTypeProgramName | — |
| RECORD_TYPE_CODE | FiscalClassTypeRecordTypeCode | — |
| REQUEST_ID | FiscalClassTypeRequestId | — |
| START_POSITION | FiscalClassTypeStartPosition | — |

### [[taxclassification|TaxClassification]] (AR · BICC: 3/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_TYPE_CATEG_CODE | FiscalClassTypeClassificationTypeCategCode | — |
| CLASSIFICATION_TYPE_CODE | FiscalClassTypeClassificationTypeCode | ✅ |
| CLASSIFICATION_TYPE_GROUP_CODE | FiscalClassTypeClassificationTypeGroupCode | — |
| CLASSIFICATION_TYPE_ID | FiscalClassTypeClassificationTypeId | — |
| CLASSIFICATION_TYPE_LEVEL_CODE | FiscalClassTypeClassificationTypeLevelCode | — |
| CLASSIFICATION_TYPE_NAME | FiscalClassTypeClassificationTypeName | ✅ |
| CREATED_BY | FiscalClassTypeCreatedBy | — |
| CREATION_DATE | FiscalClassTypeCreationDate | — |
| DELIMITER | FiscalClassTypeDelimiter | — |
| EFFECTIVE_FROM | FiscalClassTypeEffectiveFrom | — |
| EFFECTIVE_TO | FiscalClassTypeEffectiveTo | — |
| LAST_UPDATE_DATE | FiscalClassTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FiscalClassTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | FiscalClassTypeLastUpdatedBy | — |
| NUM_CHARACTERS | FiscalClassTypeNumCharacters | — |
| OBJECT_VERSION_NUMBER | FiscalClassTypeObjectVersionNumber | — |
| OWNER_ID_CHAR | FiscalClassTypeOwnerIdChar | — |
| OWNER_ID_NUM | FiscalClassTypeOwnerIdNum | — |
| OWNER_TABLE_CODE | FiscalClassTypeOwnerTableCode | — |
| PROGRAM_APP_NAME | FiscalClassTypeProgramAppName | — |
| PROGRAM_LOGIN_ID | FiscalClassTypeProgramLoginId | — |
| PROGRAM_NAME | FiscalClassTypeProgramName | — |
| RECORD_TYPE_CODE | FiscalClassTypeRecordTypeCode | — |
| REQUEST_ID | FiscalClassTypeRequestId | — |
| START_POSITION | FiscalClassTypeStartPosition | — |
