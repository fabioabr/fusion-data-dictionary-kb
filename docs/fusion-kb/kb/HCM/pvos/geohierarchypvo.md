---
id: DOC-HCM-PVO-GeoHierarchyPVO
doc_type: system-doc
title: "GeoHierarchyPVO — PVO Human Capital Management"
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
  - GeoHierarchyPVO
  - geohierarchypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GeoHierarchyPVO

## 📌 Visão Geral

Extrai hierarquias geográficas de recrutamento. Utilizado para definir estruturas de localidade em processos seletivos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingSetupAM.GeoHierarchyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 7 | 70% |

---

## 🔗 Tabelas Relacionadas

- [[irc_geo_hierarchies|IRC_GEO_HIERARCHIES]] — 10 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[irc_geo_hierarchies|IRC_GEO_HIERARCHIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GeoHierarchyPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | GeoHierarchyPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | GeoHierarchyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | GeoHierarchyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | GeoHierarchyPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | GeoHierarchyPEOName | NAME | — | ✅ |
| 7 | GeoHierarchyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | GeoHierarchyPEOStartDate | START_DATE | — | ✅ |
| 9 | GeoHierarchyPEOStatusCode | STATUS_CODE | — | ✅ |
| 10 | HierarchyId | HIERARCHY_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
