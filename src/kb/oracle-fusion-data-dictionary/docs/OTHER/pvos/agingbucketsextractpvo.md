---
id: DOC-OTHER-PVO-AgingBucketsExtractPVO
doc_type: system-doc
title: "AgingBucketsExtractPVO — PVO Cross-Module"
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
  - AgingBucketsExtractPVO
  - agingbucketsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AgingBucketsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Aging Buckets Extract. Acessa as tabelas: AR_AGING_BUCKETS.

**Caminho:** `FscmTopModelAM.FinExtractAM.IexBiccExtractAM.AgingBucketsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 1 | 1 | 12 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[ar_aging_buckets|AR_AGING_BUCKETS]] — 28 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[ar_aging_buckets|AR_AGING_BUCKETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArAgingBucketsAgingBucketId | AGING_BUCKET_ID | 🔑 | ✅ |
| 2 | ArAgingBucketsAgingType | AGING_TYPE | — | ✅ |
| 3 | ArAgingBucketsAttribute1 | ATTRIBUTE1 | — | — |
| 4 | ArAgingBucketsAttribute10 | ATTRIBUTE10 | — | — |
| 5 | ArAgingBucketsAttribute11 | ATTRIBUTE11 | — | — |
| 6 | ArAgingBucketsAttribute12 | ATTRIBUTE12 | — | — |
| 7 | ArAgingBucketsAttribute13 | ATTRIBUTE13 | — | — |
| 8 | ArAgingBucketsAttribute14 | ATTRIBUTE14 | — | — |
| 9 | ArAgingBucketsAttribute15 | ATTRIBUTE15 | — | — |
| 10 | ArAgingBucketsAttribute2 | ATTRIBUTE2 | — | — |
| 11 | ArAgingBucketsAttribute3 | ATTRIBUTE3 | — | — |
| 12 | ArAgingBucketsAttribute4 | ATTRIBUTE4 | — | — |
| 13 | ArAgingBucketsAttribute5 | ATTRIBUTE5 | — | — |
| 14 | ArAgingBucketsAttribute6 | ATTRIBUTE6 | — | — |
| 15 | ArAgingBucketsAttribute7 | ATTRIBUTE7 | — | — |
| 16 | ArAgingBucketsAttribute8 | ATTRIBUTE8 | — | — |
| 17 | ArAgingBucketsAttribute9 | ATTRIBUTE9 | — | — |
| 18 | ArAgingBucketsAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | ArAgingBucketsBucketName | BUCKET_NAME | — | ✅ |
| 20 | ArAgingBucketsCreatedBy | CREATED_BY | — | ✅ |
| 21 | ArAgingBucketsCreationDate | CREATION_DATE | — | ✅ |
| 22 | ArAgingBucketsDescription | DESCRIPTION | — | ✅ |
| 23 | ArAgingBucketsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | ArAgingBucketsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 25 | ArAgingBucketsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | ArAgingBucketsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | ArAgingBucketsSetId | SET_ID | — | ✅ |
| 28 | ArAgingBucketsStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
