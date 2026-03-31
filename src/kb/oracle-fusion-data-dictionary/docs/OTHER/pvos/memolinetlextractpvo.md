---
id: DOC-OTHER-PVO-MemoLineTLExtractPVO
doc_type: system-doc
title: "MemoLineTLExtractPVO — PVO Cross-Module"
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
  - MemoLineTLExtractPVO
  - memolinetlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MemoLineTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Memo Line TLExtract. Acessa as tabelas: AR_MEMO_LINES_ALL_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.MemoLineTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 3 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ar_memo_lines_all_tl|AR_MEMO_LINES_ALL_TL]] — 13 atributos (3 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[ar_memo_lines_all_tl|AR_MEMO_LINES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArMemoLineTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | ArMemoLineTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | ArMemoLineTLDescription | DESCRIPTION | — | ✅ |
| 4 | ArMemoLineTLLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | ArMemoLineTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ArMemoLineTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ArMemoLineTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ArMemoLineTLMemoLineId | MEMO_LINE_ID | 🔑 | ✅ |
| 9 | ArMemoLineTLName | NAME | — | ✅ |
| 10 | ArMemoLineTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ArMemoLineTLSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | ArMemoLineTLSetId | SET_ID | 🔑 | ✅ |
| 13 | ArMemoLineTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
