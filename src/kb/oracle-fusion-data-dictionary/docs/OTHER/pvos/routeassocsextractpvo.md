---
id: DOC-OTHER-PVO-RouteAssocsExtractPVO
doc_type: system-doc
title: "RouteAssocsExtractPVO — PVO Cross-Module"
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
  - RouteAssocsExtractPVO
  - routeassocsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RouteAssocsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Route Assocs Extract. Acessa as tabelas: EGO_ROUTE_ASSOCS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.RouteAssocsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 1 | 1 | 24 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_route_assocs|EGO_ROUTE_ASSOCS]] — 24 atributos (1 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[ego_route_assocs|EGO_ROUTE_ASSOCS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RouteAssociationsPEOAdhocFlag | ADHOC_FLAG | — | ✅ |
| 2 | RouteAssociationsPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | RouteAssociationsPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | RouteAssociationsPEODefinitionEntityName | DEFINITION_ENTITY_NAME | — | ✅ |
| 5 | RouteAssociationsPEODefinitionEntityPk1 | DEFINITION_ENTITY_PK1 | — | ✅ |
| 6 | RouteAssociationsPEODefinitionEntityPk2 | DEFINITION_ENTITY_PK2 | — | ✅ |
| 7 | RouteAssociationsPEODefinitionEntityPk3 | DEFINITION_ENTITY_PK3 | — | ✅ |
| 8 | RouteAssociationsPEODefinitionEntityPk4 | DEFINITION_ENTITY_PK4 | — | ✅ |
| 9 | RouteAssociationsPEODefinitionEntityPk5 | DEFINITION_ENTITY_PK5 | — | ✅ |
| 10 | RouteAssociationsPEODefinitionStatus | DEFINITION_STATUS | — | ✅ |
| 11 | RouteAssociationsPEOInheritedFlag | INHERITED_FLAG | — | ✅ |
| 12 | RouteAssociationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | RouteAssociationsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | RouteAssociationsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | RouteAssociationsPEOMandatoryFlag | MANDATORY_FLAG | — | ✅ |
| 16 | RouteAssociationsPEOObjectName | OBJECT_NAME | — | ✅ |
| 17 | RouteAssociationsPEOObjectPk1 | OBJECT_PK1 | — | ✅ |
| 18 | RouteAssociationsPEOObjectPk2 | OBJECT_PK2 | — | ✅ |
| 19 | RouteAssociationsPEOObjectPk3 | OBJECT_PK3 | — | ✅ |
| 20 | RouteAssociationsPEOObjectPk4 | OBJECT_PK4 | — | ✅ |
| 21 | RouteAssociationsPEOObjectPk5 | OBJECT_PK5 | — | ✅ |
| 22 | RouteAssociationsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | RouteAssociationsPEORouteAssocId | ROUTE_ASSOC_ID | 🔑 | ✅ |
| 24 | RouteAssociationsPEORoutePeopleId | ROUTE_PEOPLE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
