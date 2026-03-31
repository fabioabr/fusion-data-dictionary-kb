---
id: DOC-OTHER-PVO-PerspItemIssueXrefPVO
doc_type: system-doc
title: "PerspItemIssueXrefPVO — PVO Cross-Module"
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
  - PerspItemIssueXrefPVO
  - perspitemissuexrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerspItemIssueXrefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Persp Item Issue Xref. Acessa as tabelas: GRC_ISSU_PRSPITEM_XREF.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.PerspItemIssueXrefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 4 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[grc_issu_prspitem_xref|GRC_ISSU_PRSPITEM_XREF]] — 12 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[grc_issu_prspitem_xref|GRC_ISSU_PRSPITEM_XREF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrspItemIsuueXrefPEOAssessmentResultId | ASSESSMENT_RESULT_ID | — | ✅ |
| 2 | PrspItemIsuueXrefPEOCreatedBy | CREATED_BY | — | — |
| 3 | PrspItemIsuueXrefPEOCreationDate | CREATION_DATE | — | — |
| 4 | PrspItemIsuueXrefPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | PrspItemIsuueXrefPEOIssueId | ISSUE_ID | 🔑 | ✅ |
| 6 | PrspItemIsuueXrefPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PrspItemIsuueXrefPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PrspItemIsuueXrefPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | PrspItemIsuueXrefPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PrspItemIsuueXrefPEOPerspectiveItemId | PERSPECTIVE_ITEM_ID | 🔑 | ✅ |
| 11 | PrspItemIsuueXrefPEORevisionDate | REVISION_DATE | — | — |
| 12 | PrspItemIsuueXrefPEORevisionNumber | REVISION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
