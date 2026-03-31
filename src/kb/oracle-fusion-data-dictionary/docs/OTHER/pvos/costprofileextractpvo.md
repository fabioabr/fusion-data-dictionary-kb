---
id: DOC-OTHER-PVO-CostProfileExtractPVO
doc_type: system-doc
title: "CostProfileExtractPVO — PVO Cross-Module"
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
  - CostProfileExtractPVO
  - costprofileextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostProfileExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Profile Extract. Acessa as tabelas: CST_COST_PROFILES_B, CST_COST_PROFILES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CostProfileExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 74 | 2 | 1 | 72 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_profiles_b|CST_COST_PROFILES_B]] — 65 atributos (1 PKs, 65 BICC)
- [[cst_cost_profiles_tl|CST_COST_PROFILES_TL]] — 9 atributos (7 BICC)

---

## ⚙️ Atributos

### [[cst_cost_profiles_b|CST_COST_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostProfileBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | CostProfileBPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | CostProfileBPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | CostProfileBPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | CostProfileBPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | CostProfileBPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | CostProfileBPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | CostProfileBPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | CostProfileBPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 10 | CostProfileBPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 11 | CostProfileBPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 12 | CostProfileBPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 13 | CostProfileBPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 14 | CostProfileBPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 15 | CostProfileBPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 16 | CostProfileBPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 17 | CostProfileBPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 18 | CostProfileBPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 19 | CostProfileBPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 20 | CostProfileBPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 21 | CostProfileBPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 22 | CostProfileBPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 23 | CostProfileBPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 24 | CostProfileBPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 25 | CostProfileBPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 26 | CostProfileBPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 27 | CostProfileBPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 28 | CostProfileBPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 29 | CostProfileBPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 30 | CostProfileBPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | CostProfileBPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 32 | CostProfileBPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 33 | CostProfileBPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 34 | CostProfileBPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 35 | CostProfileBPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 36 | CostProfileBPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 37 | CostProfileBPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 38 | CostProfileBPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 39 | CostProfileBPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 40 | CostProfileBPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 41 | CostProfileBPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 42 | CostProfileBPEOCostAdjustmentLevelCode | COST_ADJUSTMENT_LEVEL_CODE | — | ✅ |
| 43 | CostProfileBPEOCostByUomType | COST_BY_UOM_TYPE | — | ✅ |
| 44 | CostProfileBPEOCostMethodCode | COST_METHOD_CODE | — | ✅ |
| 45 | CostProfileBPEOCostProfileCode | COST_PROFILE_CODE | — | ✅ |
| 46 | CostProfileBPEOCostProfileId | COST_PROFILE_ID | 🔑 | ✅ |
| 47 | CostProfileBPEOCreateAcctForConsTxns | CREATE_ACCT_FOR_CONS_TXNS | — | ✅ |
| 48 | CostProfileBPEOCreatedBy | CREATED_BY | — | ✅ |
| 49 | CostProfileBPEOCreationDate | CREATION_DATE | — | ✅ |
| 50 | CostProfileBPEOEnforceTxnDateOrderFlag | ENFORCE_TXN_DATE_ORDER_FLAG | — | ✅ |
| 51 | CostProfileBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 52 | CostProfileBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 53 | CostProfileBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 54 | CostProfileBPEOOperationScrapCostType | OPERATION_SCRAP_COST_TYPE | — | ✅ |
| 55 | CostProfileBPEOOperationScrapValuationType | OPERATION_SCRAP_VALUATION_TYPE | — | ✅ |
| 56 | CostProfileBPEOProcessProvCompletionType | PROCESS_PROV_COMPLETION_TYPE | — | ✅ |
| 57 | CostProfileBPEOPropagateCostAdjFlag | PROPAGATE_COST_ADJ_FLAG | — | ✅ |
| 58 | CostProfileBPEOProvisionalCompletionType | PROVISIONAL_COMPLETION_TYPE | — | ✅ |
| 59 | CostProfileBPEOQuantityFlowCode | QUANTITY_FLOW_CODE | — | ✅ |
| 60 | CostProfileBPEOReceiptWithoutCostCode | RECEIPT_WITHOUT_COST_CODE | — | ✅ |
| 61 | CostProfileBPEOReferencedRmaCostCode | REFERENCED_RMA_COST_CODE | — | ✅ |
| 62 | CostProfileBPEOSetId | SET_ID | — | ✅ |
| 63 | CostProfileBPEOSummarizeLotsFlag | SUMMARIZE_LOTS_FLAG | — | ✅ |
| 64 | CostProfileBPEOSummarizeSerialsFlag | SUMMARIZE_SERIALS_FLAG | — | ✅ |
| 65 | CostProfileBPEOValStructureId | VAL_STRUCTURE_ID | — | ✅ |

### [[cst_cost_profiles_tl|CST_COST_PROFILES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostProfileTLPEOCostProfileDesc | COST_PROFILE_DESC | — | ✅ |
| 2 | CostProfileTLPEOCostProfileId | COST_PROFILE_ID | — | ✅ |
| 3 | CostProfileTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CostProfileTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CostProfileTLPEOLanguage | LANGUAGE | — | — |
| 6 | CostProfileTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CostProfileTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CostProfileTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CostProfileTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
