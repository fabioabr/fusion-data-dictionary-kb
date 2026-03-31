---
id: DOC-OTHER-PVO-WarrantyCoverageTxnCodeExtractPVO
doc_type: system-doc
title: "WarrantyCoverageTxnCodeExtractPVO — PVO Cross-Module"
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
  - WarrantyCoverageTxnCodeExtractPVO
  - warrantycoveragetxncodeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WarrantyCoverageTxnCodeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Warranty Coverage Txn Code Extract. Acessa as tabelas: CSE_W_COVERAGE_TXN_CODES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.WarrantyCoverageTxnCodeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_w_coverage_txn_codes|CSE_W_COVERAGE_TXN_CODES]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[cse_w_coverage_txn_codes|CSE_W_COVERAGE_TXN_CODES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | CoverageId | COVERAGE_ID | — | ✅ |
| 3 | CoverageTxnCodeId | COVERAGE_TXN_CODE_ID | 🔑 | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 7 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | RequestId | REQUEST_ID | — | ✅ |
| 13 | TransactionCodeId | TRANSACTION_CODE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
