---
id: DOC-OTHER-PVO-ClaimSettlementDocumentExtractPVO
doc_type: system-doc
title: "ClaimSettlementDocumentExtractPVO — PVO Cross-Module"
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
  - ClaimSettlementDocumentExtractPVO
  - claimsettlementdocumentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClaimSettlementDocumentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Claim Settlement Document Extract. Acessa as tabelas: CJM_SETTLEMENT_DOCS_ALL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ClaimSettlementDocumentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 1 | 1 | 24 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_settlement_docs_all|CJM_SETTLEMENT_DOCS_ALL]] — 24 atributos (1 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[cjm_settlement_docs_all|CJM_SETTLEMENT_DOCS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BuId | BU_ID | — | ✅ |
| 2 | ClaimId | CLAIM_ID | — | ✅ |
| 3 | ClaimPaymentId | CLAIM_PAYMENT_ID | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 12 | RequestId | REQUEST_ID | — | ✅ |
| 13 | SettlementAcctdAmount | SETTLEMENT_ACCTD_AMOUNT | — | ✅ |
| 14 | SettlementAmount | SETTLEMENT_AMOUNT | — | ✅ |
| 15 | SettlementCurrencyCode | SETTLEMENT_CURRENCY_CODE | — | ✅ |
| 16 | SettlementDate | SETTLEMENT_DATE | — | ✅ |
| 17 | SettlementDocId | SETTLEMENT_DOC_ID | 🔑 | ✅ |
| 18 | SettlementDocTypeCode | SETTLEMENT_DOC_TYPE_CODE | — | ✅ |
| 19 | SettlementId | SETTLEMENT_ID | — | ✅ |
| 20 | SettlementNumber | SETTLEMENT_NUMBER | — | ✅ |
| 21 | SettlementTaxAmount | SETTLEMENT_TAX_AMOUNT | — | ✅ |
| 22 | SettlementType | SETTLEMENT_TYPE | — | ✅ |
| 23 | SettlementTypeId | SETTLEMENT_TYPE_ID | — | ✅ |
| 24 | StatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
