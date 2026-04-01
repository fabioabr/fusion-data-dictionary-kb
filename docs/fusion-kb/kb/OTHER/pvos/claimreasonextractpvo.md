---
id: DOC-OTHER-PVO-ClaimReasonExtractPVO
doc_type: system-doc
title: "ClaimReasonExtractPVO — PVO Cross-Module"
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
  - ClaimReasonExtractPVO
  - claimreasonextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClaimReasonExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Claim Reason Extract. Acessa as tabelas: CJM_CLAIM_REASON_CODES_B.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ClaimReasonExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_claim_reason_codes_b|CJM_CLAIM_REASON_CODES_B]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[cjm_claim_reason_codes_b|CJM_CLAIM_REASON_CODES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentReasonCode | ADJUSTMENT_REASON_CODE | — | ✅ |
| 2 | BuySideFlag | BUY_SIDE_FLAG | — | ✅ |
| 3 | ClaimReasonCode | CLAIM_REASON_CODE | — | ✅ |
| 4 | CmReasonCode | CM_REASON_CODE | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | EndDate | END_DATE | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ReasonCodeId | REASON_CODE_ID | 🔑 | ✅ |
| 13 | SellSideFlag | SELL_SIDE_FLAG | — | ✅ |
| 14 | SetId | SET_ID | — | ✅ |
| 15 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
