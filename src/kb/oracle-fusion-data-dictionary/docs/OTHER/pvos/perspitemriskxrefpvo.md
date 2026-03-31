---
id: DOC-OTHER-PVO-PerspItemRiskXrefPVO
doc_type: system-doc
title: "PerspItemRiskXrefPVO — PVO Cross-Module"
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
  - PerspItemRiskXrefPVO
  - perspitemriskxrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerspItemRiskXrefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Persp Item Risk Xref. Acessa as tabelas: GRC_PERSP_ITEMRISK_XREF.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.PerspItemRiskXrefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 3 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[grc_persp_itemrisk_xref|GRC_PERSP_ITEMRISK_XREF]] — 9 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[grc_persp_itemrisk_xref|GRC_PERSP_ITEMRISK_XREF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerspItemRiskXrefPEOCreatedBy | CREATED_BY | — | — |
| 2 | PerspItemRiskXrefPEOCreationDate | CREATION_DATE | — | — |
| 3 | PerspItemRiskXrefPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | PerspItemRiskXrefPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | PerspItemRiskXrefPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | PerspItemRiskXrefPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | PerspItemRiskXrefPEOPerspItemId | PERSP_ITEM_ID | 🔑 | ✅ |
| 8 | PerspItemRiskXrefPEORelationshipTypeCode | RELATIONSHIP_TYPE_CODE | — | — |
| 9 | PerspItemRiskXrefPEORiskId | RISK_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
