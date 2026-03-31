---
id: DOC-OTHER-PVO-ProjectResourceBreakdownStructureTransactionAccumMapExtractPVO
doc_type: system-doc
title: "ProjectResourceBreakdownStructureTransactionAccumMapExtractPVO — PVO Cross-Module"
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
  - ProjectResourceBreakdownStructureTransactionAccumMapExtractPVO
  - projectresourcebreakdownstructuretransactionaccummapextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectResourceBreakdownStructureTransactionAccumMapExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Resource Breakdown Structure Transaction Accum Map Extract. Acessa as tabelas: PJF_RBS_TXN_ACCUM_MAP.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectResourceBreakdownStructureTransactionAccumMapExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_rbs_txn_accum_map|PJF_RBS_TXN_ACCUM_MAP]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[pjf_rbs_txn_accum_map|PJF_RBS_TXN_ACCUM_MAP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectRBSTxnAccumMapPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectRBSTxnAccumMapPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectRBSTxnAccumMapPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | ProjectRBSTxnAccumMapPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | ProjectRBSTxnAccumMapPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ProjectRBSTxnAccumMapPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | ProjectRBSTxnAccumMapPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 8 | ProjectRBSTxnAccumMapPEORbsVersionId | RBS_VERSION_ID | 🔑 | ✅ |
| 9 | ProjectRBSTxnAccumMapPEOTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
