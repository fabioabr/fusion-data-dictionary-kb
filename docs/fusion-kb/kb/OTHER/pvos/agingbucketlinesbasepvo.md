---
id: DOC-OTHER-PVO-AgingBucketLinesBasePVO
doc_type: system-doc
title: "AgingBucketLinesBasePVO — PVO Cross-Module"
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
  - AgingBucketLinesBasePVO
  - agingbucketlinesbasepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AgingBucketLinesBasePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Aging Bucket Lines Base. Acessa as tabelas: AR_AGING_BUCKETS, AR_AGING_BUCKET_LINES_B.

**Caminho:** `FscmTopModelAM.FinCollSharedAM.AgingBucketLinesBasePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 2 | 1 | 12 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[ar_aging_buckets|AR_AGING_BUCKETS]] — 12 atributos (4 BICC)
- [[ar_aging_bucket_lines_b|AR_AGING_BUCKET_LINES_B]] — 15 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[ar_aging_buckets|AR_AGING_BUCKETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgingBucketsAgingBucketId | AGING_BUCKET_ID | — | — |
| 2 | AgingBucketsAgingType | AGING_TYPE | — | ✅ |
| 3 | AgingBucketsBucketName | BUCKET_NAME | — | ✅ |
| 4 | AgingBucketsCreatedBy | CREATED_BY | — | — |
| 5 | AgingBucketsCreationDate | CREATION_DATE | — | — |
| 6 | AgingBucketsDescription | DESCRIPTION | — | — |
| 7 | AgingBucketsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AgingBucketsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | AgingBucketsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | AgingBucketsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | AgingBucketsSetId | SET_ID | — | — |
| 12 | AgingBucketsStatus | STATUS | — | ✅ |

### [[ar_aging_bucket_lines_b|AR_AGING_BUCKET_LINES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgingBucketLineId | AGING_BUCKET_LINE_ID | 🔑 | ✅ |
| 2 | AgingBucketsLinesAgingBucketId | AGING_BUCKET_ID | — | — |
| 3 | AgingBucketsLinesBucketSequenceNum | BUCKET_SEQUENCE_NUM | — | ✅ |
| 4 | AgingBucketsLinesCreatedBy | CREATED_BY | — | ✅ |
| 5 | AgingBucketsLinesCreationDate | CREATION_DATE | — | ✅ |
| 6 | AgingBucketsLinesDaysStart | DAYS_START | — | ✅ |
| 7 | AgingBucketsLinesDaysTo | DAYS_TO | — | ✅ |
| 8 | AgingBucketsLinesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | AgingBucketsLinesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | AgingBucketsLinesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | AgingBucketsLinesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | AgingBucketsLinesReportHeading1 | REPORT_HEADING1 | — | — |
| 13 | AgingBucketsLinesReportHeading2 | REPORT_HEADING2 | — | — |
| 14 | AgingBucketsLinesSetId | SET_ID | — | — |
| 15 | AgingBucketsLinesType | TYPE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
