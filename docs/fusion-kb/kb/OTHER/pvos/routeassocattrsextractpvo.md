---
id: DOC-OTHER-PVO-RouteAssocAttrsExtractPVO
doc_type: system-doc
title: "RouteAssocAttrsExtractPVO — PVO Cross-Module"
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
  - RouteAssocAttrsExtractPVO
  - routeassocattrsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RouteAssocAttrsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Route Assoc Attrs Extract. Acessa as tabelas: EGO_ROUTE_ASSOC_ATTRS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.RouteAssocAttrsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_route_assoc_attrs|EGO_ROUTE_ASSOC_ATTRS]] — 18 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[ego_route_assoc_attrs|EGO_ROUTE_ASSOC_ATTRS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RouteAssocAttrsPEOAttrGroupInternalName | ATTR_GROUP_INTERNAL_NAME | — | ✅ |
| 2 | RouteAssocAttrsPEOAttrInternalName | ATTR_INTERNAL_NAME | — | ✅ |
| 3 | RouteAssocAttrsPEOAttrType | ATTR_TYPE | — | ✅ |
| 4 | RouteAssocAttrsPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | RouteAssocAttrsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | RouteAssocAttrsPEOInheritedFlag | INHERITED_FLAG | — | ✅ |
| 7 | RouteAssocAttrsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | RouteAssocAttrsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | RouteAssocAttrsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | RouteAssocAttrsPEOObjectName | OBJECT_NAME | — | ✅ |
| 11 | RouteAssocAttrsPEOObjectPk1 | OBJECT_PK1 | — | ✅ |
| 12 | RouteAssocAttrsPEOObjectPk2 | OBJECT_PK2 | — | ✅ |
| 13 | RouteAssocAttrsPEOObjectPk3 | OBJECT_PK3 | — | ✅ |
| 14 | RouteAssocAttrsPEOObjectPk4 | OBJECT_PK4 | — | ✅ |
| 15 | RouteAssocAttrsPEOObjectPk5 | OBJECT_PK5 | — | ✅ |
| 16 | RouteAssocAttrsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | RouteAssocAttrsPEORouteAssocId | ROUTE_ASSOC_ID | — | ✅ |
| 18 | RouteAssocAttrsPEORouteAttrId | ROUTE_ATTR_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
