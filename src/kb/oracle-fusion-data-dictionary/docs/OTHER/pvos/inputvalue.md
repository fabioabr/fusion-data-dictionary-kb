---
id: DOC-OTHER-PVO-InputValue
doc_type: system-doc
title: "InputValue — PVO Cross-Module"
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
  - InputValue
  - inputvalue
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InputValue

## 📌 Visão Geral

View Object para extração BICC de dados de Input Value. Acessa as tabelas: PAY_INPUT_VALUES_F, PAY_INPUT_VALUES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmElementSetupAM.InputValue`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 2 | 3 | 21 | 62% |

---

## 🔗 Tabelas Relacionadas

- [[pay_input_values_f|PAY_INPUT_VALUES_F]] — 30 atributos (3 PKs, 19 BICC)
- [[pay_input_values_tl|PAY_INPUT_VALUES_TL]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[pay_input_values_f|PAY_INPUT_VALUES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | InputValueDPEOBaseName | BASE_NAME | — | ✅ |
| 4 | InputValueDPEOContextId | CONTEXT_ID | — | — |
| 5 | InputValueDPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | InputValueDPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | InputValueDPEODefaultValue | DEFAULT_VALUE | — | ✅ |
| 8 | InputValueDPEODisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 9 | InputValueDPEOElementTypeId | ELEMENT_TYPE_ID | — | ✅ |
| 10 | InputValueDPEOForceRrvMode | FORCE_RRV_MODE | — | — |
| 11 | InputValueDPEOFormulaId | FORMULA_ID | — | — |
| 12 | InputValueDPEOGenerateDbItemsFlag | GENERATE_DB_ITEMS_FLAG | — | — |
| 13 | InputValueDPEOHotDefaultFlag | HOT_DEFAULT_FLAG | — | ✅ |
| 14 | InputValueDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | InputValueDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | InputValueDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | InputValueDPEOLookupType | LOOKUP_TYPE | — | — |
| 18 | InputValueDPEOMandatoryFlag | MANDATORY_FLAG | — | ✅ |
| 19 | InputValueDPEOMaxValue | MAX_VALUE | — | ✅ |
| 20 | InputValueDPEOMinValue | MIN_VALUE | — | ✅ |
| 21 | InputValueDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | InputValueDPEOReservedInputValue | RESERVED_INPUT_VALUE | — | ✅ |
| 23 | InputValueDPEORetroStaticFlag | RETRO_STATIC_FLAG | — | — |
| 24 | InputValueDPEOUom | UOM | — | ✅ |
| 25 | InputValueDPEOUserDisplayFlag | USER_DISPLAY_FLAG | — | ✅ |
| 26 | InputValueDPEOUserEnterableFlag | USER_ENTERABLE_FLAG | — | — |
| 27 | InputValueDPEOValidationOverrideMessage | VALIDATION_OVERRIDE_MESSAGE | — | — |
| 28 | InputValueDPEOVoName | VO_NAME | — | ✅ |
| 29 | InputValueDPEOWarningOrError | WARNING_OR_ERROR | — | — |
| 30 | InputValueId | INPUT_VALUE_ID | 🔑 | ✅ |

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
