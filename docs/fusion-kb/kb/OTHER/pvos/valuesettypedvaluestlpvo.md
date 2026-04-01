---
id: DOC-OTHER-PVO-ValueSetTypedValuesTLPVO
doc_type: system-doc
title: "ValueSetTypedValuesTLPVO — PVO Cross-Module"
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
  - ValueSetTypedValuesTLPVO
  - valuesettypedvaluestlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ValueSetTypedValuesTLPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Value Set Typed Values TL. Acessa as tabelas: FND_VS_VALUES_B, FND_VS_VALUES_TL, FND_VS_VALUE_SETS.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.ValueSetTypedValuesTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 47 | 3 | 1 | 47 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_vs_values_b|FND_VS_VALUES_B]] — 14 atributos (1 PKs, 14 BICC)
- [[fnd_vs_values_tl|FND_VS_VALUES_TL]] — 10 atributos (10 BICC)
- [[fnd_vs_value_sets|FND_VS_VALUE_SETS]] — 23 atributos (23 BICC)

---

## ⚙️ Atributos

### [[fnd_vs_values_b|FND_VS_VALUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 4 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 5 | IndependentValue | INDEPENDENT_VALUE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | SortOrder | SORT_ORDER | — | ✅ |
| 10 | StartDateActive | START_DATE_ACTIVE | — | ✅ |
| 11 | SummaryFlag | SUMMARY_FLAG | — | ✅ |
| 12 | Value | VALUE | — | ✅ |
| 13 | ValueId | VALUE_ID | 🔑 | ✅ |
| 14 | ValueSetId | VALUE_SET_ID | — | ✅ |

### [[fnd_vs_values_tl|FND_VS_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy1 | CREATED_BY | — | ✅ |
| 2 | CreationDate1 | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | — | ✅ |
| 5 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 8 | SourceLang | SOURCE_LANG | — | ✅ |
| 9 | TranslatedValue | TRANSLATED_VALUE | — | ✅ |
| 10 | ValueId1 | VALUE_ID | — | ✅ |

### [[fnd_vs_value_sets|FND_VS_VALUE_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy2 | CREATED_BY | — | ✅ |
| 2 | CreationDate2 | CREATION_DATE | — | ✅ |
| 3 | DataSecurityObjectName | DATA_SECURITY_OBJECT_NAME | — | ✅ |
| 4 | Description1 | DESCRIPTION | — | ✅ |
| 5 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 6 | IndependentValueSetId | INDEPENDENT_VALUE_SET_ID | — | ✅ |
| 7 | LastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy2 | LAST_UPDATED_BY | — | ✅ |
| 10 | MaximumLength | MAXIMUM_LENGTH | — | ✅ |
| 11 | MaximumValue | MAXIMUM_VALUE | — | ✅ |
| 12 | MinimumValue | MINIMUM_VALUE | — | ✅ |
| 13 | ModuleId | MODULE_ID | — | ✅ |
| 14 | Precision | PRECISION | — | ✅ |
| 15 | Scale | SCALE | — | ✅ |
| 16 | SecurityEnabledFlag | SECURITY_ENABLED_FLAG | — | ✅ |
| 17 | UppercaseOnlyFlag | UPPERCASE_ONLY_FLAG | — | ✅ |
| 18 | ValidationType | VALIDATION_TYPE | — | ✅ |
| 19 | ValueDataType | VALUE_DATA_TYPE | — | ✅ |
| 20 | ValueSetCode | VALUE_SET_CODE | — | ✅ |
| 21 | ValueSetId1 | VALUE_SET_ID | — | ✅ |
| 22 | ValueSubtype | VALUE_SUBTYPE | — | ✅ |
| 23 | ZeroFillFlag | ZERO_FILL_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
