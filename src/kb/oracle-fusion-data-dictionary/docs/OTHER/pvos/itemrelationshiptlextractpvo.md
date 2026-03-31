---
id: DOC-OTHER-PVO-ItemRelationshipTLExtractPVO
doc_type: system-doc
title: "ItemRelationshipTLExtractPVO — PVO Cross-Module"
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
  - ItemRelationshipTLExtractPVO
  - itemrelationshiptlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemRelationshipTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Relationship TLExtract. Acessa as tabelas: egp_item_relationships_tl.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.ItemRelationshipTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_relationships_tl|egp_item_relationships_tl]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[egp_item_relationships_tl|egp_item_relationships_tl]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemRelationshipTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ItemRelationshipTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ItemRelationshipTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | ItemRelationshipTLPEOItemRelationshipId | ITEM_RELATIONSHIP_ID | 🔑 | ✅ |
| 5 | ItemRelationshipTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | ItemRelationshipTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ItemRelationshipTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ItemRelationshipTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ItemRelationshipTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
