---
id: DOC-OTHER-PVO-WOStatusTranslationExtractPVO
doc_type: system-doc
title: "WOStatusTranslationExtractPVO — PVO Cross-Module"
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
  - WOStatusTranslationExtractPVO
  - wostatustranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOStatusTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOStatus Translation Extract. Acessa as tabelas: WIE_WO_STATUSES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WieBiccExtractAM.WOStatusTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wie_wo_statuses_tl|WIE_WO_STATUSES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[wie_wo_statuses_tl|WIE_WO_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOStatusTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | WOStatusTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WOStatusTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | WOStatusTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | WOStatusTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | WOStatusTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | WOStatusTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | WOStatusTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 9 | WOStatusTLPEOWoStatusDescription | WO_STATUS_DESCRIPTION | — | ✅ |
| 10 | WOStatusTLPEOWoStatusId | WO_STATUS_ID | 🔑 | ✅ |
| 11 | WOStatusTLPEOWoStatusName | WO_STATUS_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
