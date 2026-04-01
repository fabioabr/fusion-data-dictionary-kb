---
id: DOC-OTHER-PVO-SubledgerMappingSetValueExtractPVO
doc_type: system-doc
title: "SubledgerMappingSetValueExtractPVO — PVO Cross-Module"
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
  - SubledgerMappingSetValueExtractPVO
  - subledgermappingsetvalueextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerMappingSetValueExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Mapping Set Value Extract. Acessa as tabelas: XLA_MAPPING_SET_VALUES.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SubledgerMappingSetValueExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 1 | 1 | 31 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_mapping_set_values|XLA_MAPPING_SET_VALUES]] — 31 atributos (1 PKs, 31 BICC)

---

## ⚙️ Atributos

### [[xla_mapping_set_values|XLA_MAPPING_SET_VALUES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MappingSetValueAmbContextCode | AMB_CONTEXT_CODE | — | ✅ |
| 2 | MappingSetValueApplicationId | APPLICATION_ID | — | ✅ |
| 3 | MappingSetValueConcatInput | CONCAT_INPUT | — | ✅ |
| 4 | MappingSetValueCreatedBy | CREATED_BY | — | ✅ |
| 5 | MappingSetValueCreationDate | CREATION_DATE | — | ✅ |
| 6 | MappingSetValueEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 7 | MappingSetValueEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | MappingSetValueEnabledFlag | ENABLED_FLAG | — | ✅ |
| 9 | MappingSetValueInputHash | INPUT_HASH | — | ✅ |
| 10 | MappingSetValueInputValueConstant1 | INPUT_VALUE_CONSTANT1 | — | ✅ |
| 11 | MappingSetValueInputValueConstant10 | INPUT_VALUE_CONSTANT10 | — | ✅ |
| 12 | MappingSetValueInputValueConstant2 | INPUT_VALUE_CONSTANT2 | — | ✅ |
| 13 | MappingSetValueInputValueConstant3 | INPUT_VALUE_CONSTANT3 | — | ✅ |
| 14 | MappingSetValueInputValueConstant4 | INPUT_VALUE_CONSTANT4 | — | ✅ |
| 15 | MappingSetValueInputValueConstant5 | INPUT_VALUE_CONSTANT5 | — | ✅ |
| 16 | MappingSetValueInputValueConstant6 | INPUT_VALUE_CONSTANT6 | — | ✅ |
| 17 | MappingSetValueInputValueConstant7 | INPUT_VALUE_CONSTANT7 | — | ✅ |
| 18 | MappingSetValueInputValueConstant8 | INPUT_VALUE_CONSTANT8 | — | ✅ |
| 19 | MappingSetValueInputValueConstant9 | INPUT_VALUE_CONSTANT9 | — | ✅ |
| 20 | MappingSetValueLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | MappingSetValueLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | MappingSetValueLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | MappingSetValueMapPrec | MAP_PREC | — | ✅ |
| 24 | MappingSetValueMappingSetCode | MAPPING_SET_CODE | — | ✅ |
| 25 | MappingSetValueMappingSetFlavorId | MAPPING_SET_FLAVOR_ID | — | ✅ |
| 26 | MappingSetValueMappingSetValueId | MAPPING_SET_VALUE_ID | 🔑 | ✅ |
| 27 | MappingSetValueObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 28 | MappingSetValueStripeId | STRIPE_ID | — | ✅ |
| 29 | MappingSetValueTransactionCoaId | TRANSACTION_COA_ID | — | ✅ |
| 30 | MappingSetValueValueCodeCombinationId | VALUE_CODE_COMBINATION_ID | — | ✅ |
| 31 | MappingSetValueValueConstant | VALUE_CONSTANT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
