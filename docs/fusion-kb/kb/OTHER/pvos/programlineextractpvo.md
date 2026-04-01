---
id: DOC-OTHER-PVO-ProgramLineExtractPVO
doc_type: system-doc
title: "ProgramLineExtractPVO — PVO Cross-Module"
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
  - ProgramLineExtractPVO
  - programlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProgramLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Program Line Extract. Acessa as tabelas: CJM_PROGRAM_LINES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ProgramLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 61 | 1 | 1 | 61 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_program_lines|CJM_PROGRAM_LINES]] — 61 atributos (1 PKs, 61 BICC)

---

## ⚙️ Atributos

### [[cjm_program_lines|CJM_PROGRAM_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrualFlag | ACCRUAL_FLAG | — | ✅ |
| 2 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 3 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 4 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 5 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 6 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 7 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 8 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 9 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 10 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 11 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 12 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 13 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 14 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 15 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 16 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 17 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 18 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 19 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 20 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 21 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 22 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 23 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 24 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 25 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 26 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 27 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 28 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 29 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 30 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 31 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 32 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 33 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 34 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 35 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 36 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 37 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 38 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 39 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 40 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 41 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 42 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 43 | CreatedBy | CREATED_BY | — | ✅ |
| 44 | CreationDate | CREATION_DATE | — | ✅ |
| 45 | DiscountAmount | DISCOUNT_AMOUNT | — | ✅ |
| 46 | DiscountTypeCode | DISCOUNT_TYPE_CODE | — | ✅ |
| 47 | EndDate | END_DATE | — | ✅ |
| 48 | ItemId | ITEM_ID | — | ✅ |
| 49 | ItemLevelCode | ITEM_LEVEL_CODE | — | ✅ |
| 50 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 51 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 52 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 53 | MaxQuantity | MAX_QUANTITY | — | ✅ |
| 54 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 55 | ProgramHeaderId | PROGRAM_HEADER_ID | — | ✅ |
| 56 | ProgramLineId | PROGRAM_LINE_ID | 🔑 | ✅ |
| 57 | ProgramLineNumber | PROGRAM_LINE_NUMBER | — | ✅ |
| 58 | ProgramTierHeaderId | PROGRAM_TIER_HEADER_ID | — | ✅ |
| 59 | StartDate | START_DATE | — | ✅ |
| 60 | TpItemId | TP_ITEM_ID | — | ✅ |
| 61 | UomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
