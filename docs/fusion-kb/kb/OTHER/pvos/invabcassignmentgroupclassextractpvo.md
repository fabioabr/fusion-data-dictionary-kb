---
id: DOC-OTHER-PVO-InvAbcAssignmentGroupClassExtractPVO
doc_type: system-doc
title: "InvAbcAssignmentGroupClassExtractPVO — PVO Cross-Module"
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
  - InvAbcAssignmentGroupClassExtractPVO
  - invabcassignmentgroupclassextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvAbcAssignmentGroupClassExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Abc Assignment Group Class Extract. Acessa as tabelas: INV_ABC_ASSGN_GROUP_CLASSES, INV_ABC_ASSIGNMENT_GROUPS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.InvAbcAssignmentGroupClassExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 63 | 2 | 3 | 31 | 49% |

---

## 🔗 Tabelas Relacionadas

- [[inv_abc_assgn_group_classes|INV_ABC_ASSGN_GROUP_CLASSES]] — 32 atributos (2 PKs, 16 BICC)
- [[inv_abc_assignment_groups|INV_ABC_ASSIGNMENT_GROUPS]] — 31 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[inv_abc_assgn_group_classes|INV_ABC_ASSGN_GROUP_CLASSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbcAsnmtGrpClsPEOAbcClassId | ABC_CLASS_ID | 🔑 | ✅ |
| 2 | AbcAsnmtGrpClsPEOAbcGroupClassId | ABC_GROUP_CLASS_ID | — | ✅ |
| 3 | AbcAsnmtGrpClsPEOAssignmentGroupId | ASSIGNMENT_GROUP_ID | 🔑 | ✅ |
| 4 | AbcAsnmtGrpClsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 5 | AbcAsnmtGrpClsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 6 | AbcAsnmtGrpClsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 7 | AbcAsnmtGrpClsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 8 | AbcAsnmtGrpClsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 9 | AbcAsnmtGrpClsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 10 | AbcAsnmtGrpClsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 11 | AbcAsnmtGrpClsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 12 | AbcAsnmtGrpClsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 13 | AbcAsnmtGrpClsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 14 | AbcAsnmtGrpClsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 15 | AbcAsnmtGrpClsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 16 | AbcAsnmtGrpClsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 17 | AbcAsnmtGrpClsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 18 | AbcAsnmtGrpClsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 19 | AbcAsnmtGrpClsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 20 | AbcAsnmtGrpClsPEOCreatedBy | CREATED_BY | — | ✅ |
| 21 | AbcAsnmtGrpClsPEOCreationDate | CREATION_DATE | — | ✅ |
| 22 | AbcAsnmtGrpClsPEOItemSeqNumber | ITEM_SEQ_NUMBER | — | ✅ |
| 23 | AbcAsnmtGrpClsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 24 | AbcAsnmtGrpClsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 25 | AbcAsnmtGrpClsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | AbcAsnmtGrpClsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 27 | AbcAsnmtGrpClsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | AbcAsnmtGrpClsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 29 | AbcAsnmtGrpClsPEOPercentOfItems | PERCENT_OF_ITEMS | — | ✅ |
| 30 | AbcAsnmtGrpClsPEOPercentOfValue | PERCENT_OF_VALUE | — | ✅ |
| 31 | AbcAsnmtGrpClsPEORequestId | REQUEST_ID | — | ✅ |
| 32 | AbcAsnmtGrpClsPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |

### [[inv_abc_assignment_groups|INV_ABC_ASSIGNMENT_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbcAssignmentGroupPEOAssignmentGroupId | ASSIGNMENT_GROUP_ID | 🔑 | ✅ |
| 2 | AbcAssignmentGroupPEOAssignmentGroupName | ASSIGNMENT_GROUP_NAME | — | ✅ |
| 3 | AbcAssignmentGroupPEOAttribute1 | ATTRIBUTE1 | — | — |
| 4 | AbcAssignmentGroupPEOAttribute10 | ATTRIBUTE10 | — | — |
| 5 | AbcAssignmentGroupPEOAttribute11 | ATTRIBUTE11 | — | — |
| 6 | AbcAssignmentGroupPEOAttribute12 | ATTRIBUTE12 | — | — |
| 7 | AbcAssignmentGroupPEOAttribute13 | ATTRIBUTE13 | — | — |
| 8 | AbcAssignmentGroupPEOAttribute14 | ATTRIBUTE14 | — | — |
| 9 | AbcAssignmentGroupPEOAttribute15 | ATTRIBUTE15 | — | — |
| 10 | AbcAssignmentGroupPEOAttribute2 | ATTRIBUTE2 | — | — |
| 11 | AbcAssignmentGroupPEOAttribute3 | ATTRIBUTE3 | — | — |
| 12 | AbcAssignmentGroupPEOAttribute4 | ATTRIBUTE4 | — | — |
| 13 | AbcAssignmentGroupPEOAttribute5 | ATTRIBUTE5 | — | — |
| 14 | AbcAssignmentGroupPEOAttribute6 | ATTRIBUTE6 | — | — |
| 15 | AbcAssignmentGroupPEOAttribute7 | ATTRIBUTE7 | — | — |
| 16 | AbcAssignmentGroupPEOAttribute8 | ATTRIBUTE8 | — | — |
| 17 | AbcAssignmentGroupPEOAttribute9 | ATTRIBUTE9 | — | — |
| 18 | AbcAssignmentGroupPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | AbcAssignmentGroupPEOCompileId | COMPILE_ID | — | ✅ |
| 20 | AbcAssignmentGroupPEOCreatedBy | CREATED_BY | — | ✅ |
| 21 | AbcAssignmentGroupPEOCreationDate | CREATION_DATE | — | ✅ |
| 22 | AbcAssignmentGroupPEOItemScopeType | ITEM_SCOPE_TYPE | — | ✅ |
| 23 | AbcAssignmentGroupPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 24 | AbcAssignmentGroupPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 25 | AbcAssignmentGroupPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | AbcAssignmentGroupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 27 | AbcAssignmentGroupPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | AbcAssignmentGroupPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 29 | AbcAssignmentGroupPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 30 | AbcAssignmentGroupPEORequestId | REQUEST_ID | — | ✅ |
| 31 | AbcAssignmentGroupPEOSecondaryInventory | SECONDARY_INVENTORY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
