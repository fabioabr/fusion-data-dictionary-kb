---
id: DOC-PO-PVO-SearchActionPVO
doc_type: system-doc
title: "SearchActionPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SearchActionPVO
  - searchactionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SearchActionPVO

## 📌 Visão Geral

Extrai as ações realizadas após buscas no sistema de recrutamento (clique, seleção, descarte). Suporta análise de eficácia da busca e identificação de melhorias na experiência do recrutador.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecSourcingCoreAM.SearchActionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 2 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[irc_search_actions|IRC_SEARCH_ACTIONS]] — 11 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[irc_search_actions|IRC_SEARCH_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionId | ACTION_ID | 🔑 | ✅ |
| 2 | SearchActionPEOAction | ACTION | — | ✅ |
| 3 | SearchActionPEOCreatedBy | CREATED_BY | — | — |
| 4 | SearchActionPEOCreationDate | CREATION_DATE | — | — |
| 5 | SearchActionPEOEntityIds | ENTITY_IDS | — | — |
| 6 | SearchActionPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | SearchActionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | SearchActionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | SearchActionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | SearchActionPEOSearchId | SEARCH_ID | — | — |
| 11 | SearchActionPEOSelectedCandidates | SELECTED_CANDIDATES | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
