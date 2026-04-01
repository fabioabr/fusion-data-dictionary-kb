---
id: DOC-OTHER-PVO-AgingBucketLinesExtractPVO
doc_type: system-doc
title: "AgingBucketLinesExtractPVO — PVO Cross-Module"
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
  - AgingBucketLinesExtractPVO
  - agingbucketlinesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AgingBucketLinesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Aging Bucket Lines Extract. Acessa as tabelas: AR_AGING_BUCKET_LINES_B, AR_AGING_BUCKET_LINES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.IexBiccExtractAM.AgingBucketLinesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 2 | 1 | 27 | 63% |

---

## 🔗 Tabelas Relacionadas

- [[ar_aging_bucket_lines_b|AR_AGING_BUCKET_LINES_B]] — 31 atributos (1 PKs, 15 BICC)
- [[ar_aging_bucket_lines_tl|AR_AGING_BUCKET_LINES_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[ar_aging_bucket_lines_b|AR_AGING_BUCKET_LINES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArAgingBucketLinesBAgingBucketId | AGING_BUCKET_ID | — | ✅ |
| 2 | ArAgingBucketLinesBAgingBucketLineId | AGING_BUCKET_LINE_ID | 🔑 | ✅ |
| 3 | ArAgingBucketLinesBAttribute1 | ATTRIBUTE1 | — | — |
| 4 | ArAgingBucketLinesBAttribute10 | ATTRIBUTE10 | — | — |
| 5 | ArAgingBucketLinesBAttribute11 | ATTRIBUTE11 | — | — |
| 6 | ArAgingBucketLinesBAttribute12 | ATTRIBUTE12 | — | — |
| 7 | ArAgingBucketLinesBAttribute13 | ATTRIBUTE13 | — | — |
| 8 | ArAgingBucketLinesBAttribute14 | ATTRIBUTE14 | — | — |
| 9 | ArAgingBucketLinesBAttribute15 | ATTRIBUTE15 | — | — |
| 10 | ArAgingBucketLinesBAttribute2 | ATTRIBUTE2 | — | — |
| 11 | ArAgingBucketLinesBAttribute3 | ATTRIBUTE3 | — | — |
| 12 | ArAgingBucketLinesBAttribute4 | ATTRIBUTE4 | — | — |
| 13 | ArAgingBucketLinesBAttribute5 | ATTRIBUTE5 | — | — |
| 14 | ArAgingBucketLinesBAttribute6 | ATTRIBUTE6 | — | — |
| 15 | ArAgingBucketLinesBAttribute7 | ATTRIBUTE7 | — | — |
| 16 | ArAgingBucketLinesBAttribute8 | ATTRIBUTE8 | — | — |
| 17 | ArAgingBucketLinesBAttribute9 | ATTRIBUTE9 | — | — |
| 18 | ArAgingBucketLinesBAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | ArAgingBucketLinesBBucketSequenceNum | BUCKET_SEQUENCE_NUM | — | ✅ |
| 20 | ArAgingBucketLinesBCreatedBy | CREATED_BY | — | ✅ |
| 21 | ArAgingBucketLinesBCreationDate | CREATION_DATE | — | ✅ |
| 22 | ArAgingBucketLinesBDaysStart | DAYS_START | — | ✅ |
| 23 | ArAgingBucketLinesBDaysTo | DAYS_TO | — | ✅ |
| 24 | ArAgingBucketLinesBLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | ArAgingBucketLinesBLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 26 | ArAgingBucketLinesBLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | ArAgingBucketLinesBObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 28 | ArAgingBucketLinesBReportHeading1 | REPORT_HEADING1 | — | ✅ |
| 29 | ArAgingBucketLinesBReportHeading2 | REPORT_HEADING2 | — | ✅ |
| 30 | ArAgingBucketLinesBSetId | SET_ID | — | ✅ |
| 31 | ArAgingBucketLinesBType | TYPE | — | ✅ |

### [[ar_aging_bucket_lines_tl|AR_AGING_BUCKET_LINES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArAgingBucketLinesTLAgingBucketLineId1 | AGING_BUCKET_LINE_ID | — | ✅ |
| 2 | ArAgingBucketLinesTLCreatedBy | CREATED_BY | — | ✅ |
| 3 | ArAgingBucketLinesTLCreationDate | CREATION_DATE | — | ✅ |
| 4 | ArAgingBucketLinesTLLanguage | LANGUAGE | — | ✅ |
| 5 | ArAgingBucketLinesTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ArAgingBucketLinesTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ArAgingBucketLinesTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ArAgingBucketLinesTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ArAgingBucketLinesTLReportHeading1 | REPORT_HEADING1 | — | ✅ |
| 10 | ArAgingBucketLinesTLReportHeading2 | REPORT_HEADING2 | — | ✅ |
| 11 | ArAgingBucketLinesTLSetId | SET_ID | — | ✅ |
| 12 | ArAgingBucketLinesTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
