---
id: DOC-OTHER-PVO-IncidentPerspectiveXrefPVO
doc_type: system-doc
title: "IncidentPerspectiveXrefPVO — PVO Cross-Module"
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
  - IncidentPerspectiveXrefPVO
  - incidentperspectivexrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IncidentPerspectiveXrefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Incident Perspective Xref. Acessa as tabelas: GRC_INC_PERSP_XREF.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.IncidentPerspectiveXrefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 3 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[grc_inc_persp_xref|GRC_INC_PERSP_XREF]] — 9 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[grc_inc_persp_xref|GRC_INC_PERSP_XREF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IncidentPerspectiveXrefPEOCreatedBy | CREATED_BY | — | — |
| 2 | IncidentPerspectiveXrefPEOCreationDate | CREATION_DATE | — | — |
| 3 | IncidentPerspectiveXrefPEOGrccControlId | GRCC_CONTROL_ID | — | — |
| 4 | IncidentPerspectiveXrefPEOIncidentId | INCIDENT_ID | 🔑 | ✅ |
| 5 | IncidentPerspectiveXrefPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | IncidentPerspectiveXrefPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | IncidentPerspectiveXrefPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | IncidentPerspectiveXrefPEOPerspItemId | PERSP_ITEM_ID | 🔑 | ✅ |
| 9 | IncidentPerspectiveXrefPEOPerspTreeId | PERSP_TREE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
