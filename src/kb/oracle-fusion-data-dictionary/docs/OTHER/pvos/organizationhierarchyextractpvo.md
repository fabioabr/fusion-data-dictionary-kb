---
id: DOC-OTHER-PVO-OrganizationHierarchyExtractPVO
doc_type: system-doc
title: "OrganizationHierarchyExtractPVO — PVO Cross-Module"
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
  - OrganizationHierarchyExtractPVO
  - organizationhierarchyextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrganizationHierarchyExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Organization Hierarchy Extract. Acessa as tabelas: PJF_ORG_HIERARCHY_DENORM.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.OrganizationHierarchyExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 5 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_org_hierarchy_denorm|PJF_ORG_HIERARCHY_DENORM]] — 13 atributos (5 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[pjf_org_hierarchy_denorm|PJF_ORG_HIERARCHY_DENORM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationHierarchyPEOChildLevel | CHILD_LEVEL | — | ✅ |
| 2 | OrganizationHierarchyPEOChildOrganizationId | CHILD_ORGANIZATION_ID | 🔑 | ✅ |
| 3 | OrganizationHierarchyPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | OrganizationHierarchyPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | OrganizationHierarchyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | OrganizationHierarchyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | OrganizationHierarchyPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | OrganizationHierarchyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | OrganizationHierarchyPEOParentLevel | PARENT_LEVEL | — | ✅ |
| 10 | OrganizationHierarchyPEOParentOrganizationId | PARENT_ORGANIZATION_ID | 🔑 | ✅ |
| 11 | OrganizationHierarchyPEOTreeCode | TREE_CODE | 🔑 | ✅ |
| 12 | OrganizationHierarchyPEOTreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |
| 13 | OrganizationHierarchyPEOTreeVersionId | TREE_VERSION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
