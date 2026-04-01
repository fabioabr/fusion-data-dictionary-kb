---
id: DOC-OTHER-PVO-MemoLineExtractPVO
doc_type: system-doc
title: "MemoLineExtractPVO — PVO Cross-Module"
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
  - MemoLineExtractPVO
  - memolineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MemoLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Memo Line Extract. Acessa as tabelas: AR_MEMO_LINES_ALL_B, AR_MEMO_LINES_ALL_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.MemoLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 80 | 2 | 1 | 33 | 41% |

---

## 🔗 Tabelas Relacionadas

- [[ar_memo_lines_all_b|AR_MEMO_LINES_ALL_B]] — 68 atributos (1 PKs, 21 BICC)
- [[ar_memo_lines_all_tl|AR_MEMO_LINES_ALL_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[ar_memo_lines_all_b|AR_MEMO_LINES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArMemoLineAccountingRuleId | ACCOUNTING_RULE_ID | — | ✅ |
| 2 | ArMemoLineAttribute1 | ATTRIBUTE1 | — | — |
| 3 | ArMemoLineAttribute10 | ATTRIBUTE10 | — | — |
| 4 | ArMemoLineAttribute11 | ATTRIBUTE11 | — | — |
| 5 | ArMemoLineAttribute12 | ATTRIBUTE12 | — | — |
| 6 | ArMemoLineAttribute13 | ATTRIBUTE13 | — | — |
| 7 | ArMemoLineAttribute14 | ATTRIBUTE14 | — | — |
| 8 | ArMemoLineAttribute15 | ATTRIBUTE15 | — | — |
| 9 | ArMemoLineAttribute2 | ATTRIBUTE2 | — | — |
| 10 | ArMemoLineAttribute3 | ATTRIBUTE3 | — | — |
| 11 | ArMemoLineAttribute4 | ATTRIBUTE4 | — | — |
| 12 | ArMemoLineAttribute5 | ATTRIBUTE5 | — | — |
| 13 | ArMemoLineAttribute6 | ATTRIBUTE6 | — | — |
| 14 | ArMemoLineAttribute7 | ATTRIBUTE7 | — | — |
| 15 | ArMemoLineAttribute8 | ATTRIBUTE8 | — | — |
| 16 | ArMemoLineAttribute9 | ATTRIBUTE9 | — | — |
| 17 | ArMemoLineAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 18 | ArMemoLineCreatedBy | CREATED_BY | — | ✅ |
| 19 | ArMemoLineCreationDate | CREATION_DATE | — | ✅ |
| 20 | ArMemoLineDescription | DESCRIPTION | — | ✅ |
| 21 | ArMemoLineEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 22 | ArMemoLineEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 23 | ArMemoLineGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 24 | ArMemoLineGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 25 | ArMemoLineGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 26 | ArMemoLineGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 27 | ArMemoLineGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 28 | ArMemoLineGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 29 | ArMemoLineGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 30 | ArMemoLineGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 31 | ArMemoLineGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 32 | ArMemoLineGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 33 | ArMemoLineGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 34 | ArMemoLineGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 35 | ArMemoLineGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 36 | ArMemoLineGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 37 | ArMemoLineGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 38 | ArMemoLineGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 39 | ArMemoLineGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 40 | ArMemoLineGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 41 | ArMemoLineGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 42 | ArMemoLineGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 43 | ArMemoLineGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 44 | ArMemoLineGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 45 | ArMemoLineGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 46 | ArMemoLineGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 47 | ArMemoLineGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 48 | ArMemoLineGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 49 | ArMemoLineGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 50 | ArMemoLineGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 51 | ArMemoLineGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 52 | ArMemoLineGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 53 | ArMemoLineGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 54 | ArMemoLineInvoicingRuleId | INVOICING_RULE_ID | — | ✅ |
| 55 | ArMemoLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 56 | ArMemoLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 57 | ArMemoLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 58 | ArMemoLineLineType | LINE_TYPE | — | ✅ |
| 59 | ArMemoLineMemoLineId | MEMO_LINE_ID | — | ✅ |
| 60 | ArMemoLineMemoLineSeqId | MEMO_LINE_SEQ_ID | 🔑 | ✅ |
| 61 | ArMemoLineName | NAME | — | ✅ |
| 62 | ArMemoLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 63 | ArMemoLineSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 64 | ArMemoLineSetId | SET_ID | — | ✅ |
| 65 | ArMemoLineTaxCode | TAX_CODE | — | ✅ |
| 66 | ArMemoLineTaxProductCategory | TAX_PRODUCT_CATEGORY | — | ✅ |
| 67 | ArMemoLineUnitStdPrice | UNIT_STD_PRICE | — | ✅ |
| 68 | ArMemoLineUomCode | UOM_CODE | — | ✅ |

### [[ar_memo_lines_all_tl|AR_MEMO_LINES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArMemoLineTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | ArMemoLineTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | ArMemoLineTLDescription | DESCRIPTION | — | ✅ |
| 4 | ArMemoLineTLLanguage | LANGUAGE | — | ✅ |
| 5 | ArMemoLineTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ArMemoLineTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ArMemoLineTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ArMemoLineTLMemoLineId | MEMO_LINE_ID | — | ✅ |
| 9 | ArMemoLineTLName | NAME | — | ✅ |
| 10 | ArMemoLineTLSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 11 | ArMemoLineTLSetId | SET_ID | — | ✅ |
| 12 | ArMemoLineTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
