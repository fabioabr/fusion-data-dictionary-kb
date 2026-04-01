---
id: DOC-OTHER-PVO-ValueSetsPVO
doc_type: system-doc
title: "ValueSetsPVO — PVO Cross-Module"
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
  - ValueSetsPVO
  - valuesetspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ValueSetsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Value Sets. Acessa as tabelas: FND_VS_VALUE_SETS.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.ValueSetsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 0 | 29 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_vs_value_sets|FND_VS_VALUE_SETS]] — 29 atributos (29 BICC)

---

## ⚙️ Atributos

### [[fnd_vs_value_sets|FND_VS_VALUE_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DataSecurityObjectName | DATA_SECURITY_OBJECT_NAME | — | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | IndependentValueSetId | INDEPENDENT_VALUE_SET_ID | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | MaximumLength | MAXIMUM_LENGTH | — | ✅ |
| 10 | MaximumValue | MAXIMUM_VALUE | — | ✅ |
| 11 | MaximumValueDate | MAXIMUM_VALUE_DATE | — | ✅ |
| 12 | MaximumValueNumber | MAXIMUM_VALUE_NUMBER | — | ✅ |
| 13 | MaximumValueTimestamp | MAXIMUM_VALUE_TIMESTAMP | — | ✅ |
| 14 | MinimumValue | MINIMUM_VALUE | — | ✅ |
| 15 | MinimumValueDate | MINIMUM_VALUE_DATE | — | ✅ |
| 16 | MinimumValueNumber | MINIMUM_VALUE_NUMBER | — | ✅ |
| 17 | MinimumValueTimestamp | MINIMUM_VALUE_TIMESTAMP | — | ✅ |
| 18 | ModuleId | MODULE_ID | — | ✅ |
| 19 | Precision | PRECISION | — | ✅ |
| 20 | ProtectedFlag | PROTECTED_FLAG | — | ✅ |
| 21 | Scale | SCALE | — | ✅ |
| 22 | SecurityEnabledFlag | SECURITY_ENABLED_FLAG | — | ✅ |
| 23 | UppercaseOnlyFlag | UPPERCASE_ONLY_FLAG | — | ✅ |
| 24 | ValidationType | VALIDATION_TYPE | — | ✅ |
| 25 | ValueDataType | VALUE_DATA_TYPE | — | ✅ |
| 26 | ValueSetCode | VALUE_SET_CODE | — | ✅ |
| 27 | ValueSetId | VALUE_SET_ID | — | ✅ |
| 28 | ValueSubtype | VALUE_SUBTYPE | — | ✅ |
| 29 | ZeroFillFlag | ZERO_FILL_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
