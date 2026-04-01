---
id: DOC-OTHER-PVO-RequestShortlistPVO
doc_type: system-doc
title: "RequestShortlistPVO — PVO Cross-Module"
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
  - RequestShortlistPVO
  - requestshortlistpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequestShortlistPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Request Shortlist. Acessa as tabelas: PJR_REQUEST_SHORTLIST.

**Caminho:** `FscmTopModelAM.PjrResourceRequestAM.RequestShortlistPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 4 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[pjr_request_shortlist|PJR_REQUEST_SHORTLIST]] — 9 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[pjr_request_shortlist|PJR_REQUEST_SHORTLIST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LShortlistPEOastUpdatedBy | LAST_UPDATED_BY | — | — |
| 2 | ShortlistId | SHORTLIST_ID | 🔑 | ✅ |
| 3 | ShortlistPEOCreatedBy | CREATED_BY | — | — |
| 4 | ShortlistPEOCreationDate | CREATION_DATE | — | — |
| 5 | ShortlistPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ShortlistPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ShortlistPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ShortlistPEOResourceId | RESOURCE_ID | — | ✅ |
| 9 | ShortlistPEOResourceRequestId | RESOURCE_REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
