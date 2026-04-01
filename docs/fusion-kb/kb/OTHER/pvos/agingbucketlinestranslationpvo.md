---
id: DOC-OTHER-PVO-AgingBucketLinesTranslationPVO
doc_type: system-doc
title: "AgingBucketLinesTranslationPVO — PVO Cross-Module"
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
  - AgingBucketLinesTranslationPVO
  - agingbucketlinestranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AgingBucketLinesTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Aging Bucket Lines Translation. Acessa as tabelas: AR_AGING_BUCKET_LINES_TL.

**Caminho:** `FscmTopModelAM.FinCollSharedAM.AgingBucketLinesTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 9 | 75% |

---

## 🔗 Tabelas Relacionadas

- [[ar_aging_bucket_lines_tl|AR_AGING_BUCKET_LINES_TL]] — 12 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[ar_aging_bucket_lines_tl|AR_AGING_BUCKET_LINES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgingBucketLineId | AGING_BUCKET_LINE_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ReportHeading1 | REPORT_HEADING1 | — | ✅ |
| 10 | ReportHeading2 | REPORT_HEADING2 | — | ✅ |
| 11 | SetId | SET_ID | — | — |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
