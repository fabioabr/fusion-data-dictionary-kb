---
id: DOC-OTHER-PVO-LearningARRelationsPVO
doc_type: system-doc
title: "LearningARRelationsPVO — PVO Cross-Module"
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
  - LearningARRelationsPVO
  - learningarrelationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LearningARRelationsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Learning ARRelations. Acessa as tabelas: WLF_AR_RELATIONS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.LearningARRelationsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 3 | 7 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_ar_relations_f|WLF_AR_RELATIONS_F]] — 14 atributos (3 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[wlf_ar_relations_f|WLF_AR_RELATIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LearningARRelationsDEOAssignmentRecordId | ASSIGNMENT_RECORD_ID | — | — |
| 2 | LearningARRelationsDEOCreatedBy | CREATED_BY | — | — |
| 3 | LearningARRelationsDEOCreationDate | CREATION_DATE | — | — |
| 4 | LearningARRelationsDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 5 | LearningARRelationsDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 6 | LearningARRelationsDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 7 | LearningARRelationsDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LearningARRelationsDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LearningARRelationsDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | LearningARRelationsDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | LearningARRelationsDEORelatedObjectId | RELATED_OBJECT_ID | — | ✅ |
| 12 | LearningARRelationsDEORelatedObjectType | RELATED_OBJECT_TYPE | — | ✅ |
| 13 | LearningARRelationsDEORelationId | RELATION_ID | 🔑 | ✅ |
| 14 | LearningARRelationsDEORelationType | RELATION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
