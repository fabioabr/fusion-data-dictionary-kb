---
id: DOC-OTHER-PVO-InvAbcAssignmentGroupExtractPVO
doc_type: system-doc
title: "InvAbcAssignmentGroupExtractPVO — PVO Cross-Module"
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
  - InvAbcAssignmentGroupExtractPVO
  - invabcassignmentgroupextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvAbcAssignmentGroupExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Abc Assignment Group Extract. Acessa as tabelas: INV_ABC_ASSIGNMENT_GROUPS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.InvAbcAssignmentGroupExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_abc_assignment_groups|INV_ABC_ASSIGNMENT_GROUPS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[inv_abc_assignment_groups|INV_ABC_ASSIGNMENT_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbcAssignmentGroupPEOAssignmentGroupId | ASSIGNMENT_GROUP_ID | 🔑 | ✅ |
| 2 | AbcAssignmentGroupPEOAssignmentGroupName | ASSIGNMENT_GROUP_NAME | — | ✅ |
| 3 | AbcAssignmentGroupPEOCompileId | COMPILE_ID | — | ✅ |
| 4 | AbcAssignmentGroupPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | AbcAssignmentGroupPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | AbcAssignmentGroupPEOItemScopeType | ITEM_SCOPE_TYPE | — | ✅ |
| 7 | AbcAssignmentGroupPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 8 | AbcAssignmentGroupPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 9 | AbcAssignmentGroupPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | AbcAssignmentGroupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | AbcAssignmentGroupPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | AbcAssignmentGroupPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | AbcAssignmentGroupPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 14 | AbcAssignmentGroupPEORequestId | REQUEST_ID | — | ✅ |
| 15 | AbcAssignmentGroupPEOSecondaryInventory | SECONDARY_INVENTORY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
