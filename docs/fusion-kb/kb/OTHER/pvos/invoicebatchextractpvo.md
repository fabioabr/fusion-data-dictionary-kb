---
id: DOC-OTHER-PVO-InvoiceBatchExtractPVO
doc_type: system-doc
title: "InvoiceBatchExtractPVO — PVO Cross-Module"
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
  - InvoiceBatchExtractPVO
  - invoicebatchextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvoiceBatchExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Invoice Batch Extract. Acessa as tabelas: AP_BATCHES_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ApBiccExtractAM.InvoiceBatchExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ap_batches_all|AP_BATCHES_ALL]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[ap_batches_all|AP_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApBatchesAllBatchDate | BATCH_DATE | — | ✅ |
| 2 | ApBatchesAllBatchId | BATCH_ID | 🔑 | ✅ |
| 3 | ApBatchesAllBatchName | BATCH_NAME | — | ✅ |
| 4 | ApBatchesAllCreatedBy | CREATED_BY | — | ✅ |
| 5 | ApBatchesAllCreationDate | CREATION_DATE | — | ✅ |
| 6 | ApBatchesAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ApBatchesAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ApBatchesAllLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ApBatchesAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ApBatchesAllOrgId | ORG_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
