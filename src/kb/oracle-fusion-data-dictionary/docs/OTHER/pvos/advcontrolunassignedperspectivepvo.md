---
id: DOC-OTHER-PVO-AdvControlUnassignedPerspectivePVO
doc_type: system-doc
title: "AdvControlUnassignedPerspectivePVO — PVO Cross-Module"
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
  - AdvControlUnassignedPerspectivePVO
  - advcontrolunassignedperspectivepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdvControlUnassignedPerspectivePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Adv Control Unassigned Perspective. Acessa as tabelas: GRC_OTBI_UNASG_PERSP_RPT.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.AdvControlUnassignedPerspectivePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 3 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[grc_otbi_unasg_persp_rpt|GRC_OTBI_UNASG_PERSP_RPT]] — 10 atributos (3 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[grc_otbi_unasg_persp_rpt|GRC_OTBI_UNASG_PERSP_RPT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnassignedPerspectivePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | UnassignedPerspectivePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | UnassignedPerspectivePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | UnassignedPerspectivePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | UnassignedPerspectivePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | UnassignedPerspectivePEOMdlId | MDL_ID | 🔑 | ✅ |
| 7 | UnassignedPerspectivePEOPerspItemId | PERSPECTIVE_ITEM_ID | 🔑 | ✅ |
| 8 | UnassignedPerspectivePEOPerspItemName | PERSPECTIVE_ITEM_NAME | — | ✅ |
| 9 | UnassignedPerspectivePEOPerspTreeId | PERSPECTIVE_TREE_ID | 🔑 | ✅ |
| 10 | UnassignedPerspectivePEOPerspTreeName | PERSPECTIVE_TREE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
