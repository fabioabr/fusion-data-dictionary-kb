---
id: DOC-OTHER-PVO-InputValuePVO
doc_type: system-doc
title: "InputValuePVO — PVO Cross-Module"
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
  - InputValuePVO
  - inputvaluepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InputValuePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Input Value. Acessa as tabelas: PAY_INPUT_VALUES_F, PAY_INPUT_VALUES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmElementSetupAM.InputValuePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 2 | 1 | 20 | 59% |

---

## 🔗 Tabelas Relacionadas

- [[pay_input_values_f|PAY_INPUT_VALUES_F]] — 30 atributos (1 PKs, 18 BICC)
- [[pay_input_values_tl|PAY_INPUT_VALUES_TL]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[pay_input_values_f|PAY_INPUT_VALUES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InputValueId | INPUT_VALUE_ID | 🔑 | ✅ |
| 2 | InputValuePEOBaseName | BASE_NAME | — | — |
| 3 | InputValuePEOContextId | CONTEXT_ID | — | — |
| 4 | InputValuePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | InputValuePEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | InputValuePEODefaultValue | DEFAULT_VALUE | — | ✅ |
| 7 | InputValuePEODisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 8 | InputValuePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 9 | InputValuePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 10 | InputValuePEOElementTypeId | ELEMENT_TYPE_ID | — | ✅ |
| 11 | InputValuePEOForceRrvMode | FORCE_RRV_MODE | — | — |
| 12 | InputValuePEOFormulaId | FORMULA_ID | — | — |
| 13 | InputValuePEOGenerateDbItemsFlag | GENERATE_DB_ITEMS_FLAG | — | — |
| 14 | InputValuePEOHotDefaultFlag | HOT_DEFAULT_FLAG | — | ✅ |
| 15 | InputValuePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | InputValuePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | InputValuePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | InputValuePEOLookupType | LOOKUP_TYPE | — | — |
| 19 | InputValuePEOMandatoryFlag | MANDATORY_FLAG | — | ✅ |
| 20 | InputValuePEOMaxValue | MAX_VALUE | — | ✅ |
| 21 | InputValuePEOMinValue | MIN_VALUE | — | ✅ |
| 22 | InputValuePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | InputValuePEOReservedInputValue | RESERVED_INPUT_VALUE | — | ✅ |
| 24 | InputValuePEORetroStaticFlag | RETRO_STATIC_FLAG | — | — |
| 25 | InputValuePEOUom | UOM | — | ✅ |
| 26 | InputValuePEOUserDisplayFlag | USER_DISPLAY_FLAG | — | ✅ |
| 27 | InputValuePEOUserEnterableFlag | USER_ENTERABLE_FLAG | — | — |
| 28 | InputValuePEOValidationOverrideMessage | VALIDATION_OVERRIDE_MESSAGE | — | — |
| 29 | InputValuePEOVoName | VO_NAME | — | ✅ |
| 30 | InputValuePEOWarningOrError | WARNING_OR_ERROR | — | — |

### [[pay_input_values_tl|PAY_INPUT_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InputValueTranslationPEOInputValueId | INPUT_VALUE_ID | — | — |
| 2 | InputValueTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 3 | InputValueTranslationPEOName | NAME | — | ✅ |
| 4 | InputValueTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
