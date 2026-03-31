---
id: DOC-OTHER-PVO-RoutePeopleCommentsExtractPVO
doc_type: system-doc
title: "RoutePeopleCommentsExtractPVO — PVO Cross-Module"
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
  - RoutePeopleCommentsExtractPVO
  - routepeoplecommentsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RoutePeopleCommentsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Route People Comments Extract. Acessa as tabelas: EGO_ROUTE_PEOPLE_COMMENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.RoutePeopleCommentsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_route_people_comments|EGO_ROUTE_PEOPLE_COMMENTS]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[ego_route_people_comments|EGO_ROUTE_PEOPLE_COMMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RoutePeopleCommentsPEOCommentsDate | COMMENTS_DATE | — | ✅ |
| 2 | RoutePeopleCommentsPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | RoutePeopleCommentsPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | RoutePeopleCommentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RoutePeopleCommentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | RoutePeopleCommentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | RoutePeopleCommentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | RoutePeopleCommentsPEOResponseComment | RESPONSE_COMMENT | — | ✅ |
| 9 | RoutePeopleCommentsPEORoutePeopleCommentId | ROUTE_PEOPLE_COMMENT_ID | 🔑 | ✅ |
| 10 | RoutePeopleCommentsPEORoutePeopleId | ROUTE_PEOPLE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
