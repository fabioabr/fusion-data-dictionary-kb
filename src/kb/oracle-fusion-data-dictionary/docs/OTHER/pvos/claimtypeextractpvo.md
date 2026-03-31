---
id: DOC-OTHER-PVO-ClaimTypeExtractPVO
doc_type: system-doc
title: "ClaimTypeExtractPVO — PVO Cross-Module"
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
  - ClaimTypeExtractPVO
  - claimtypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClaimTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Claim Type Extract. Acessa as tabelas: CJM_CLAIM_TYPES_B.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ClaimTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_claim_types_b|CJM_CLAIM_TYPES_B]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[cjm_claim_types_b|CJM_CLAIM_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BuySideFlag | BUY_SIDE_FLAG | — | ✅ |
| 2 | ClaimTypeCode | CLAIM_TYPE_CODE | — | ✅ |
| 3 | ClaimTypeId | CLAIM_TYPE_ID | 🔑 | ✅ |
| 4 | CmCustTrxTypeSeqId | CM_CUST_TRX_TYPE_SEQ_ID | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | EndDate | END_DATE | — | ✅ |
| 8 | InvCustTrxTypeSeqId | INV_CUST_TRX_TYPE_SEQ_ID | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | SellSideFlag | SELL_SIDE_FLAG | — | ✅ |
| 14 | SetId | SET_ID | — | ✅ |
| 15 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
