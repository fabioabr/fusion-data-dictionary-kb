---
id: DOC-PO-PVO-RequisitionLanguagePVO
doc_type: system-doc
title: "RequisitionLanguagePVO — PVO Purchasing"
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
  - RequisitionLanguagePVO
  - requisitionlanguagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequisitionLanguagePVO

## 📌 Visão Geral

Extrai dados de idioma das requisições de contratação, suportando operações multilíngues onde vagas podem ser publicadas em diferentes idiomas conforme a localidade.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecHiringRequisitionAM.RequisitionLanguagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 2 | 3 | 10 | 77% |

---

## 🔗 Tabelas Relacionadas

- [[irc_requisitions_tl|IRC_REQUISITIONS_TL]] — 3 atributos (2 BICC)
- [[irc_req_languages|IRC_REQ_LANGUAGES]] — 10 atributos (3 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[irc_requisitions_tl|IRC_REQUISITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionLanguage | LANGUAGE | — | ✅ |
| 2 | RequisitionSourceLang | SOURCE_LANG | — | ✅ |
| 3 | RequisitionTLPEORequisitionId | REQUISITION_ID | — | — |

### [[irc_req_languages|IRC_REQ_LANGUAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | IsBaseFlag | IS_BASE_FLAG | — | ✅ |
| 4 | LanguageCode | LANGUAGE_CODE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ReqLanguageId | REQ_LANGUAGE_ID | 🔑 | ✅ |
| 10 | RequisitionId | REQUISITION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
