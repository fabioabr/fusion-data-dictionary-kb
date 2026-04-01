---
id: DOC-OTHER-PVO-WOOperationTranslationExtractPVO
doc_type: system-doc
title: "WOOperationTranslationExtractPVO — PVO Cross-Module"
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
  - WOOperationTranslationExtractPVO
  - wooperationtranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOOperationTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOOperation Translation Extract. Acessa as tabelas: WIE_WO_OPERATIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WieBiccExtractAM.WOOperationTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wie_wo_operations_tl|WIE_WO_OPERATIONS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[wie_wo_operations_tl|WIE_WO_OPERATIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOOperationTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | WOOperationTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WOOperationTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | WOOperationTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | WOOperationTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | WOOperationTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | WOOperationTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | WOOperationTLPEOOperationDescription | OPERATION_DESCRIPTION | — | ✅ |
| 9 | WOOperationTLPEOOperationName | OPERATION_NAME | — | ✅ |
| 10 | WOOperationTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 11 | WOOperationTLPEOWoOperationId | WO_OPERATION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
