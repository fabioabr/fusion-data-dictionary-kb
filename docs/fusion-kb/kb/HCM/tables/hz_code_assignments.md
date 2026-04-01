---
id: DOC-HCM-485
doc_type: system-doc
title: "HZ_CODE_ASSIGNMENTS — (título a preencher)"
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
  - HZ_CODE_ASSIGNMENTS
  - hz_code_assignments
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# HZ_CODE_ASSIGNMENTS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTUAL_CONTENT_SOURCE | — | — | — | — | — | — |
| 2 | CLASS_CATEGORY | — | — | — | — | — | — |
| 3 | CLASS_CODE | — | — | — | — | — | — |
| 4 | CODE_ASSIGNMENT_ID | — | — | — | — | — | — |
| 5 | CREATED_BY | — | — | — | — | — | — |
| 6 | CREATED_BY_MODULE | — | — | — | — | — | — |
| 7 | CREATION_DATE | — | — | — | — | — | — |
| 8 | END_DATE_ACTIVE | — | — | — | — | — | — |
| 9 | JOB_DEFINITION_NAME | — | — | — | — | — | — |
| 10 | JOB_DEFINITION_PACKAGE | — | — | — | — | — | — |
| 11 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 12 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 13 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 14 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 15 | OWNER_TABLE_ID | — | — | — | — | — | — |
| 16 | OWNER_TABLE_KEY_1 | — | — | — | — | — | — |
| 17 | OWNER_TABLE_KEY_2 | — | — | — | — | — | — |
| 18 | OWNER_TABLE_KEY_3 | — | — | — | — | — | — |
| 19 | OWNER_TABLE_KEY_4 | — | — | — | — | — | — |
| 20 | OWNER_TABLE_KEY_5 | — | — | — | — | — | — |
| 21 | OWNER_TABLE_NAME | — | — | — | — | — | — |
| 22 | PRIMARY_FLAG | — | — | — | — | — | — |
| 23 | RANK | — | — | — | — | — | — |
| 24 | START_DATE_ACTIVE | — | — | — | — | — | — |
| 25 | STATUS | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[classcategoryorgtypepvo|ClassCategoryOrgTypePVO]] (HCM · BICC: 4/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_CONTENT_SOURCE | ActualContentSource | — |
| CLASS_CATEGORY | ClassCategory | ✅ |
| CLASS_CODE | ClassCode | ✅ |
| CODE_ASSIGNMENT_ID | CodeAssignmentId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATED_BY_MODULE | CreatedByModule | — |
| CREATION_DATE | CreationDate | — |
| END_DATE_ACTIVE | EndDateActive | — |
| JOB_DEFINITION_NAME | JobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OWNER_TABLE_ID | OwnerTableId | — |
| OWNER_TABLE_KEY_1 | OwnerTableKey1 | — |
| OWNER_TABLE_KEY_2 | OwnerTableKey2 | — |
| OWNER_TABLE_KEY_3 | OwnerTableKey3 | — |
| OWNER_TABLE_KEY_4 | OwnerTableKey4 | — |
| OWNER_TABLE_KEY_5 | OwnerTableKey5 | — |
| OWNER_TABLE_NAME | OwnerTableName | — |
| PRIMARY_FLAG | PrimaryFlag | — |
| RANK | Rank | — |
| START_DATE_ACTIVE | StartDateActive | — |
| STATUS | Status | — |

### [[sitetaxclassification|SiteTaxClassification]] (AR · BICC: 4/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASS_CATEGORY | CodeAssignmentClassCategory | — |
| CLASS_CODE | CodeAssignmentClassCode | ✅ |
| CODE_ASSIGNMENT_ID | CodeAssignmentCodeAssignmentId | — |
| CREATED_BY | CodeAssignmentCreatedBy | — |
| CREATED_BY_MODULE | CodeAssignmentCreatedByModule | — |
| CREATION_DATE | CodeAssignmentCreationDate | — |
| END_DATE_ACTIVE | CodeAssignmentEndDateActive | ✅ |
| JOB_DEFINITION_NAME | CodeAssignmentJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | CodeAssignmentJobDefinitionPackage | — |
| LAST_UPDATE_DATE | CodeAssignmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CodeAssignmentLastUpdateLogin | — |
| LAST_UPDATED_BY | CodeAssignmentLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | CodeAssignmentObjectVersionNumber | — |
| OWNER_TABLE_ID | CodeAssignmentOwnerTableId | — |
| PRIMARY_FLAG | CodeAssignmentPrimaryFlag | — |
| RANK | CodeAssignmentRank | — |
| START_DATE_ACTIVE | CodeAssignmentStartDateActive | ✅ |
| STATUS | CodeAssignmentStatus | — |

### [[taxclassification|TaxClassification]] (AR · BICC: 4/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASS_CATEGORY | CodeAssignmentClassCategory | — |
| CLASS_CODE | CodeAssignmentClassCode | ✅ |
| CODE_ASSIGNMENT_ID | CodeAssignmentCodeAssignmentId | — |
| CREATED_BY | CodeAssignmentCreatedBy | — |
| CREATED_BY_MODULE | CodeAssignmentCreatedByModule | — |
| CREATION_DATE | CodeAssignmentCreationDate | — |
| END_DATE_ACTIVE | CodeAssignmentEndDateActive | ✅ |
| JOB_DEFINITION_NAME | CodeAssignmentJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | CodeAssignmentJobDefinitionPackage | — |
| LAST_UPDATE_DATE | CodeAssignmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CodeAssignmentLastUpdateLogin | — |
| LAST_UPDATED_BY | CodeAssignmentLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | CodeAssignmentObjectVersionNumber | — |
| OWNER_TABLE_ID | CodeAssignmentOwnerTableId | — |
| PRIMARY_FLAG | CodeAssignmentPrimaryFlag | — |
| RANK | CodeAssignmentRank | — |
| START_DATE_ACTIVE | CodeAssignmentStartDateActive | ✅ |
| STATUS | CodeAssignmentStatus | — |
