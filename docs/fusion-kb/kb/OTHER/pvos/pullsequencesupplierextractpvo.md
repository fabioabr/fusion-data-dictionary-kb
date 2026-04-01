---
id: DOC-OTHER-PVO-PullSequenceSupplierExtractPVO
doc_type: system-doc
title: "PullSequenceSupplierExtractPVO — PVO Cross-Module"
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
  - PullSequenceSupplierExtractPVO
  - pullsequencesupplierextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PullSequenceSupplierExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Pull Sequence Supplier Extract. Acessa as tabelas: WIS_PULL_SEQ_SUPPLIERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WisBiccExtractAM.PullSequenceSupplierExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wis_pull_seq_suppliers|WIS_PULL_SEQ_SUPPLIERS]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[wis_pull_seq_suppliers|WIS_PULL_SEQ_SUPPLIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PullSequenceSupplierPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PullSequenceSupplierPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PullSequenceSupplierPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | PullSequenceSupplierPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | PullSequenceSupplierPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | PullSequenceSupplierPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | PullSequenceSupplierPEOPullSequenceId | PULL_SEQUENCE_ID | — | ✅ |
| 8 | PullSequenceSupplierPEOPullSequenceSupplierId | PULL_SEQUENCE_SUPPLIER_ID | 🔑 | ✅ |
| 9 | PullSequenceSupplierPEOSourcingPercentage | SOURCING_PERCENTAGE | — | ✅ |
| 10 | PullSequenceSupplierPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 11 | PullSequenceSupplierPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
