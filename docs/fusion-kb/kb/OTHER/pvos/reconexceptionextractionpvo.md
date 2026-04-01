---
id: DOC-OTHER-PVO-ReconExceptionExtractionPVO
doc_type: system-doc
title: "ReconExceptionExtractionPVO — PVO Cross-Module"
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
  - ReconExceptionExtractionPVO
  - reconexceptionextractionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReconExceptionExtractionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Recon Exception Extraction. Acessa as tabelas: CE_RECON_EXCEPTIONS.

**Caminho:** `FscmTopModelAM.FinExtractAM.CeBiccExtractAM.ReconExceptionExtractionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ce_recon_exceptions|CE_RECON_EXCEPTIONS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[ce_recon_exceptions|CE_RECON_EXCEPTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReconExceptionCreatedBy | CREATED_BY | — | ✅ |
| 2 | ReconExceptionCreationDate | CREATION_DATE | — | ✅ |
| 3 | ReconExceptionExceptionType | EXCEPTION_TYPE | — | ✅ |
| 4 | ReconExceptionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ReconExceptionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | ReconExceptionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ReconExceptionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ReconExceptionReconExceptionId | RECON_EXCEPTION_ID | 🔑 | ✅ |
| 9 | ReconExceptionReconMatchingRuleId | RECON_MATCHING_RULE_ID | — | ✅ |
| 10 | ReconExceptionReconToleranceRuleId | RECON_TOLERANCE_RULE_ID | — | ✅ |
| 11 | ReconExceptionStatementHeaderId | STATEMENT_HEADER_ID | — | ✅ |
| 12 | ReconExceptionStatementLineId | STATEMENT_LINE_ID | — | ✅ |
| 13 | ReconExceptionTransactionId | TRANSACTION_ID | — | ✅ |
| 14 | ReconExceptionTransactionSource | TRANSACTION_SOURCE | — | ✅ |
| 15 | ReconExceptionTrxLineId | TRX_LINE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
