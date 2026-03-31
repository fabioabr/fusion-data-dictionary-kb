---
id: DOC-OTHER-PVO-RateDimTier
doc_type: system-doc
title: "RateDimTier — PVO Cross-Module"
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
  - RateDimTier
  - ratedimtier
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RateDimTier

## 📌 Visão Geral

View Object para extração BICC de dados de Rate Dim Tier. Acessa as tabelas: CN_EXPRESSIONS_ALL_TL, CN_RATE_DIM_TIERS_ALL.

**Caminho:** `FscmTopModelAM.RateTableAM.RateDimTier`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 1 | 17 | 85% |

---

## 🔗 Tabelas Relacionadas

- [[cn_expressions_all_tl|CN_EXPRESSIONS_ALL_TL]] — 4 atributos (4 BICC)
- [[cn_rate_dim_tiers_all|CN_RATE_DIM_TIERS_ALL]] — 16 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[cn_expressions_all_tl|CN_EXPRESSIONS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MaxExpressionId | EXPRESSION_ID | — | ✅ |
| 2 | MaxExpressionName | EXPRESSION_NAME | — | ✅ |
| 3 | MinExpressionId | EXPRESSION_ID | — | ✅ |
| 4 | MinExpressionName | EXPRESSION_NAME | — | ✅ |

### [[cn_rate_dim_tiers_all|CN_RATE_DIM_TIERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DimUnitCode | DIM_UNIT_CODE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | MaxExpId | MAX_EXP_ID | — | ✅ |
| 8 | MaximumAmount | MAXIMUM_AMOUNT | — | ✅ |
| 9 | MinExpId | MIN_EXP_ID | — | ✅ |
| 10 | MinimumAmount | MINIMUM_AMOUNT | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | OrgId | ORG_ID | — | — |
| 13 | RateDimTierId | RATE_DIM_TIER_ID | 🔑 | ✅ |
| 14 | RateDimensionId | RATE_DIMENSION_ID | — | — |
| 15 | StringValue | STRING_VALUE | — | ✅ |
| 16 | TierSequence | TIER_SEQUENCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
