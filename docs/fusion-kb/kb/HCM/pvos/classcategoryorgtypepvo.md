---
id: DOC-HCM-PVO-ClassCategoryOrgTypePVO
doc_type: system-doc
title: "ClassCategoryOrgTypePVO — PVO Human Capital Management"
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
  - ClassCategoryOrgTypePVO
  - classcategoryorgtypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClassCategoryOrgTypePVO

## 📌 Visão Geral

Extrai classificacoes de tipo de organizacao via code assignments do TCA (Trading Community). Suporta categorizacao de entidades parceiras.

**Caminho:** `FscmTopModelAM.PartiesAnalyticsAM.ClassCategoryOrgTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 1 | 1 | 4 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[hz_code_assignments|HZ_CODE_ASSIGNMENTS]] — 24 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hz_code_assignments|HZ_CODE_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | ClassCategory | CLASS_CATEGORY | — | ✅ |
| 3 | ClassCode | CLASS_CODE | — | ✅ |
| 4 | CodeAssignmentId | CODE_ASSIGNMENT_ID | 🔑 | ✅ |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreatedByModule | CREATED_BY_MODULE | — | — |
| 7 | CreationDate | CREATION_DATE | — | — |
| 8 | EndDateActive | END_DATE_ACTIVE | — | — |
| 9 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | OwnerTableId | OWNER_TABLE_ID | — | — |
| 15 | OwnerTableKey1 | OWNER_TABLE_KEY_1 | — | — |
| 16 | OwnerTableKey2 | OWNER_TABLE_KEY_2 | — | — |
| 17 | OwnerTableKey3 | OWNER_TABLE_KEY_3 | — | — |
| 18 | OwnerTableKey4 | OWNER_TABLE_KEY_4 | — | — |
| 19 | OwnerTableKey5 | OWNER_TABLE_KEY_5 | — | — |
| 20 | OwnerTableName | OWNER_TABLE_NAME | — | — |
| 21 | PrimaryFlag | PRIMARY_FLAG | — | — |
| 22 | Rank | RANK | — | — |
| 23 | StartDateActive | START_DATE_ACTIVE | — | — |
| 24 | Status | STATUS | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
