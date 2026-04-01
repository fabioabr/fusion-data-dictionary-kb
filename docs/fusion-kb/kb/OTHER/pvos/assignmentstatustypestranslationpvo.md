---
id: DOC-OTHER-PVO-AssignmentStatusTypesTranslationPVO
doc_type: system-doc
title: "AssignmentStatusTypesTranslationPVO — PVO Cross-Module"
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
  - AssignmentStatusTypesTranslationPVO
  - assignmentstatustypestranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssignmentStatusTypesTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Assignment Status Types Translation. Acessa as tabelas: PER_ASSIGNMENT_STATUS_TYPES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AssignmentAM.AssignmentStatusTypesTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 4 | 36% |

---

## 🔗 Tabelas Relacionadas

- [[per_assignment_status_types_tl|PER_ASSIGNMENT_STATUS_TYPES_TL]] — 11 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[per_assignment_status_types_tl|PER_ASSIGNMENT_STATUS_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentStatusTranslationCreatedBy | CREATED_BY | — | — |
| 2 | AssignmentStatusTranslationCreationDate | CREATION_DATE | — | — |
| 3 | AssignmentStatusTranslationExternalStatus | EXTERNAL_STATUS | — | — |
| 4 | AssignmentStatusTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | AssignmentStatusTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | AssignmentStatusTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | AssignmentStatusTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | AssignmentStatusTranslationSourceLang | SOURCE_LANG | — | — |
| 9 | AssignmentStatusTranslationUserStatus | USER_STATUS | — | ✅ |
| 10 | AssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | 🔑 | ✅ |
| 11 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
