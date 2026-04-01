---
id: DOC-OTHER-PVO-RouteExtractPVO
doc_type: system-doc
title: "RouteExtractPVO — PVO Cross-Module"
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
  - RouteExtractPVO
  - routeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RouteExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Route Extract. Acessa as tabelas: EGO_ROUTES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.RouteExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_routes|EGO_ROUTES]] — 20 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[ego_routes|EGO_ROUTES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RoutePEOAppliedTemplateId | APPLIED_TEMPLATE_ID | — | ✅ |
| 2 | RoutePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | RoutePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | RoutePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RoutePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | RoutePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | RoutePEOObjectName | OBJECT_NAME | — | ✅ |
| 8 | RoutePEOObjectPk1 | OBJECT_PK1 | — | ✅ |
| 9 | RoutePEOObjectPk2 | OBJECT_PK2 | — | ✅ |
| 10 | RoutePEOObjectPk3 | OBJECT_PK3 | — | ✅ |
| 11 | RoutePEOObjectPk4 | OBJECT_PK4 | — | ✅ |
| 12 | RoutePEOObjectPk5 | OBJECT_PK5 | — | ✅ |
| 13 | RoutePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | RoutePEOResponseRequiredFrom | RESPONSE_REQUIRED_FROM | — | ✅ |
| 15 | RoutePEORouteId | ROUTE_ID | 🔑 | ✅ |
| 16 | RoutePEORouteInternalName | ROUTE_INTERNAL_NAME | — | ✅ |
| 17 | RoutePEORouteTypeCode | ROUTE_TYPE_CODE | — | ✅ |
| 18 | RoutePEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 19 | RoutePEOStatusCode | STATUS_CODE | — | ✅ |
| 20 | RoutePEOTemplateFlag | TEMPLATE_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
