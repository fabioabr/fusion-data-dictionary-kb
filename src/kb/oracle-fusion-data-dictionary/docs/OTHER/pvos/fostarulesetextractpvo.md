---
id: DOC-OTHER-PVO-FosTaRuleSetExtractPVO
doc_type: system-doc
title: "FosTaRuleSetExtractPVO — PVO Cross-Module"
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
  - FosTaRuleSetExtractPVO
  - fostarulesetextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosTaRuleSetExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Ta Rule Set Extract. Acessa as tabelas: FOS_TA_RULE_SET_B_F, FOS_TA_RULE_SET_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosTaRuleSetExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 2 | 3 | 56 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[fos_ta_rule_set_b_f|FOS_TA_RULE_SET_B_F]] — 44 atributos (3 PKs, 44 BICC)
- [[fos_ta_rule_set_tl|FOS_TA_RULE_SET_TL]] — 14 atributos (12 BICC)

---

## ⚙️ Atributos

### [[fos_ta_rule_set_b_f|FOS_TA_RULE_SET_B_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaRuleSetBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | TaRuleSetBPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | TaRuleSetBPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | TaRuleSetBPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | TaRuleSetBPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | TaRuleSetBPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | TaRuleSetBPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | TaRuleSetBPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | TaRuleSetBPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 10 | TaRuleSetBPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 11 | TaRuleSetBPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 12 | TaRuleSetBPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 13 | TaRuleSetBPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 14 | TaRuleSetBPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 15 | TaRuleSetBPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 16 | TaRuleSetBPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 17 | TaRuleSetBPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 18 | TaRuleSetBPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 19 | TaRuleSetBPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 20 | TaRuleSetBPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 21 | TaRuleSetBPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 22 | TaRuleSetBPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 23 | TaRuleSetBPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 24 | TaRuleSetBPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 25 | TaRuleSetBPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 26 | TaRuleSetBPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 27 | TaRuleSetBPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 28 | TaRuleSetBPEOConversionType | CONVERSION_TYPE | — | ✅ |
| 29 | TaRuleSetBPEOCreatedBy | CREATED_BY | — | ✅ |
| 30 | TaRuleSetBPEOCreationDate | CREATION_DATE | — | ✅ |
| 31 | TaRuleSetBPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 32 | TaRuleSetBPEOCurrencyOption | CURRENCY_OPTION | — | ✅ |
| 33 | TaRuleSetBPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 34 | TaRuleSetBPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 35 | TaRuleSetBPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 36 | TaRuleSetBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | TaRuleSetBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 38 | TaRuleSetBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 39 | TaRuleSetBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | TaRuleSetBPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 41 | TaRuleSetBPEOStandardCurrency | STANDARD_CURRENCY | — | ✅ |
| 42 | TaRuleSetBPEOTaRuleSetId | TA_RULE_SET_ID | 🔑 | ✅ |
| 43 | TaRuleSetBPEOTaRuleSetName | TA_RULE_SET_NAME | — | ✅ |
| 44 | TaRuleSetBPEOTrackProfitsFlag | TRACK_PROFITS_FLAG | — | ✅ |

### [[fos_ta_rule_set_tl|FOS_TA_RULE_SET_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaRuleSetTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TaRuleSetTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TaRuleSetTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | TaRuleSetTLPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 5 | TaRuleSetTLPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | TaRuleSetTLPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 7 | TaRuleSetTLPEOLanguage | LANGUAGE | — | — |
| 8 | TaRuleSetTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | TaRuleSetTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | TaRuleSetTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | TaRuleSetTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | TaRuleSetTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 13 | TaRuleSetTLPEOSourceLang | SOURCE_LANG | — | — |
| 14 | TaRuleSetTLPEOTaRuleSetId | TA_RULE_SET_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
