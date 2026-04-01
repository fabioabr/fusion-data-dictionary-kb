---
id: DOC-OTHER-PVO-ClaimLineUtilExtractPVO
doc_type: system-doc
title: "ClaimLineUtilExtractPVO — PVO Cross-Module"
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
  - ClaimLineUtilExtractPVO
  - claimlineutilextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClaimLineUtilExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Claim Line Util Extract. Acessa as tabelas: CJM_CLAIM_LINES_UTIL_ALL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ClaimLineUtilExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 1 | 1 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_claim_lines_util_all|CJM_CLAIM_LINES_UTIL_ALL]] — 23 atributos (1 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[cjm_claim_lines_util_all|CJM_CLAIM_LINES_UTIL_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 2 | Amount | AMOUNT | — | ✅ |
| 3 | AssociationId | ASSOCIATION_ID | — | ✅ |
| 4 | BuId | BU_ID | — | ✅ |
| 5 | ClaimLineId | CLAIM_LINE_ID | — | ✅ |
| 6 | ClaimLineUtilId | CLAIM_LINE_UTIL_ID | 🔑 | ✅ |
| 7 | CreatedBy | CREATED_BY | — | ✅ |
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 10 | ExchangeRate | EXCHANGE_RATE | — | ✅ |
| 11 | ExchangeRateDate | EXCHANGE_RATE_DATE | — | ✅ |
| 12 | ExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 13 | FxglAcctdAmount | FXGL_ACCTD_AMOUNT | — | ✅ |
| 14 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | ProgramAmount | PROGRAM_AMOUNT | — | ✅ |
| 20 | RequestId | REQUEST_ID | — | ✅ |
| 21 | UtilCurrAmount | UTIL_CURR_AMOUNT | — | ✅ |
| 22 | UtilizationId | UTILIZATION_ID | — | ✅ |
| 23 | UtilizedAcctdAmount | UTILIZED_ACCTD_AMOUNT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
