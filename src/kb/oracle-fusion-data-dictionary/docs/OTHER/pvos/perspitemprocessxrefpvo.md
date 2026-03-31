---
id: DOC-OTHER-PVO-PerspItemProcessXrefPVO
doc_type: system-doc
title: "PerspItemProcessXrefPVO — PVO Cross-Module"
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
  - PerspItemProcessXrefPVO
  - perspitemprocessxrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerspItemProcessXrefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Persp Item Process Xref. Acessa as tabelas: GRC_PERSP_ITEMPROC_XREF.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.PerspItemProcessXrefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 3 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[grc_persp_itemproc_xref|GRC_PERSP_ITEMPROC_XREF]] — 9 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[grc_persp_itemproc_xref|GRC_PERSP_ITEMPROC_XREF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerspItemProcessXrefPEOCreatedBy | CREATED_BY | — | — |
| 2 | PerspItemProcessXrefPEOCreationDate | CREATION_DATE | — | — |
| 3 | PerspItemProcessXrefPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | PerspItemProcessXrefPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | PerspItemProcessXrefPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | PerspItemProcessXrefPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | PerspItemProcessXrefPEOPerspItemId | PERSP_ITEM_ID | 🔑 | ✅ |
| 8 | PerspItemProcessXrefPEOProcessId | PROCESS_ID | 🔑 | ✅ |
| 9 | PerspItemProcessXrefPEORelationshipTypeCode | RELATIONSHIP_TYPE_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
