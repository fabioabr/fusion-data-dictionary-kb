---
id: DOC-OTHER-PVO-ClaimLineExtractPVO
doc_type: system-doc
title: "ClaimLineExtractPVO — PVO Cross-Module"
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
  - ClaimLineExtractPVO
  - claimlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClaimLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Claim Line Extract. Acessa as tabelas: CJM_CLAIM_LINES_ALL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ClaimLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 1 | 1 | 34 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_claim_lines_all|CJM_CLAIM_LINES_ALL]] — 34 atributos (1 PKs, 34 BICC)

---

## ⚙️ Atributos

### [[cjm_claim_lines_all|CJM_CLAIM_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 2 | ActivityId | ACTIVITY_ID | — | ✅ |
| 3 | ActivityTypeCode | ACTIVITY_TYPE_CODE | — | ✅ |
| 4 | Amount | AMOUNT | — | ✅ |
| 5 | AssociationId | ASSOCIATION_ID | — | ✅ |
| 6 | BuId | BU_ID | — | ✅ |
| 7 | ClaimId | CLAIM_ID | — | ✅ |
| 8 | ClaimLineId | CLAIM_LINE_ID | 🔑 | ✅ |
| 9 | CreatedBy | CREATED_BY | — | ✅ |
| 10 | CreationDate | CREATION_DATE | — | ✅ |
| 11 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 12 | Description | DESCRIPTION | — | ✅ |
| 13 | EarningsAssociatedFlag | EARNINGS_ASSOCIATED_FLAG | — | ✅ |
| 14 | ExchangeRate | EXCHANGE_RATE | — | ✅ |
| 15 | ExchangeRateDate | EXCHANGE_RATE_DATE | — | ✅ |
| 16 | ExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 17 | ItemId | ITEM_ID | — | ✅ |
| 18 | ItemLevelCode | ITEM_LEVEL_CODE | — | ✅ |
| 19 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 20 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | LineComments | LINE_COMMENTS | — | ✅ |
| 24 | LineNumber | LINE_NUMBER | — | ✅ |
| 25 | LineSourceTypeCode | LINE_SOURCE_TYPE_CODE | — | ✅ |
| 26 | MemoLineSeqId | MEMO_LINE_SEQ_ID | — | ✅ |
| 27 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 28 | Quantity | QUANTITY | — | ✅ |
| 29 | QuantityUomCode | QUANTITY_UOM_CODE | — | ✅ |
| 30 | Rate | RATE | — | ✅ |
| 31 | RequestId | REQUEST_ID | — | ✅ |
| 32 | SettlementLineFlag | SETTLEMENT_LINE_FLAG | — | ✅ |
| 33 | SourceObjectLineId | SOURCE_OBJECT_LINE_ID | — | ✅ |
| 34 | SourceObjectTypeId | SOURCE_OBJECT_TYPE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
