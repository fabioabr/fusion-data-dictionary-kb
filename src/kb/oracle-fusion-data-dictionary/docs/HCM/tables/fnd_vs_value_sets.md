---
id: DOC-HCM-145
doc_type: system-doc
title: "FND_VS_VALUE_SETS — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - FND_VS_VALUE_SETS
  - fnd_vs_value_sets
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_VS_VALUE_SETS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | DATA_SECURITY_OBJECT_NAME | — | — | — | — | — | — |
| 4 | DESCRIPTION | — | — | — | — | — | — |
| 5 | ENTERPRISE_ID | — | — | — | — | — | — |
| 6 | INDEPENDENT_VALUE_SET_ID | — | — | — | — | — | — |
| 7 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 8 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 9 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 10 | MAXIMUM_LENGTH | — | — | — | — | — | — |
| 11 | MAXIMUM_VALUE | — | — | — | — | — | — |
| 12 | MAXIMUM_VALUE_DATE | — | — | — | — | — | — |
| 13 | MAXIMUM_VALUE_NUMBER | — | — | — | — | — | — |
| 14 | MAXIMUM_VALUE_TIMESTAMP | — | — | — | — | — | — |
| 15 | MINIMUM_VALUE | — | — | — | — | — | — |
| 16 | MINIMUM_VALUE_DATE | — | — | — | — | — | — |
| 17 | MINIMUM_VALUE_NUMBER | — | — | — | — | — | — |
| 18 | MINIMUM_VALUE_TIMESTAMP | — | — | — | — | — | — |
| 19 | MODULE_ID | — | — | — | — | — | — |
| 20 | PRECISION | — | — | — | — | — | — |
| 21 | PROTECTED_FLAG | — | — | — | — | — | — |
| 22 | SCALE | — | — | — | — | — | — |
| 23 | SECURITY_ENABLED_FLAG | — | — | — | — | — | — |
| 24 | UPPERCASE_ONLY_FLAG | — | — | — | — | — | — |
| 25 | VALIDATION_TYPE | — | — | — | — | — | — |
| 26 | VALUE_DATA_TYPE | — | — | — | — | — | — |
| 27 | VALUE_SET_CODE | — | — | — | — | — | — |
| 28 | VALUE_SET_ID | — | — | — | — | — | — |
| 29 | VALUE_SUBTYPE | — | — | — | — | — | — |
| 30 | ZERO_FILL_FLAG | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[fndlookupsp1|FNDLookupsP1]] (OTHER · BICC: 2/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ValueSetPEOCreatedBy | — |
| CREATION_DATE | ValueSetPEOCreationDate | — |
| DATA_SECURITY_OBJECT_NAME | ValueSetPEODataSecurityObjectName | — |
| DESCRIPTION | ValueSetPEODescription | — |
| INDEPENDENT_VALUE_SET_ID | ValueSetPEOIndependentValueSetId | — |
| LAST_UPDATE_DATE | ValueSetPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ValueSetPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ValueSetPEOLastUpdatedBy | — |
| MAXIMUM_LENGTH | ValueSetPEOMaximumLength | — |
| MAXIMUM_VALUE | ValueSetPEOMaximumValue | — |
| MINIMUM_VALUE | ValueSetPEOMinimumValue | — |
| MODULE_ID | ValueSetPEOModuleId | — |
| PRECISION | ValueSetPEOPrecision | — |
| SCALE | ValueSetPEOScale | — |
| SECURITY_ENABLED_FLAG | ValueSetPEOSecurityEnabledFlag | — |
| UPPERCASE_ONLY_FLAG | ValueSetPEOUppercaseOnlyFlag | — |
| VALIDATION_TYPE | ValueSetPEOValidationType | ✅ |
| VALUE_DATA_TYPE | ValueSetPEOValueDataType | — |
| VALUE_SET_CODE | ValueSetPEOValueSetCode | — |
| VALUE_SET_ID | ValueSetPEOValueSetId | — |
| VALUE_SUBTYPE | ValueSetPEOValueSubtype | — |
| ZERO_FILL_FLAG | ValueSetPEOZeroFillFlag | — |

### [[fndvaluesp1|FNDValuesP1]] (OTHER · BICC: 2/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ValueSetPEOCreatedBy | — |
| CREATION_DATE | ValueSetPEOCreationDate | — |
| DATA_SECURITY_OBJECT_NAME | ValueSetPEODataSecurityObjectName | — |
| DESCRIPTION | ValueSetPEODescription | — |
| INDEPENDENT_VALUE_SET_ID | ValueSetPEOIndependentValueSetId | — |
| LAST_UPDATE_DATE | ValueSetPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ValueSetPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ValueSetPEOLastUpdatedBy | — |
| MAXIMUM_LENGTH | ValueSetPEOMaximumLength | — |
| MAXIMUM_VALUE | ValueSetPEOMaximumValue | — |
| MINIMUM_VALUE | ValueSetPEOMinimumValue | — |
| MODULE_ID | ValueSetPEOModuleId | — |
| PRECISION | ValueSetPEOPrecision | — |
| SCALE | ValueSetPEOScale | — |
| SECURITY_ENABLED_FLAG | ValueSetPEOSecurityEnabledFlag | — |
| UPPERCASE_ONLY_FLAG | ValueSetPEOUppercaseOnlyFlag | — |
| VALIDATION_TYPE | ValueSetPEOValidationType | ✅ |
| VALUE_DATA_TYPE | ValueSetPEOValueDataType | — |
| VALUE_SET_CODE | ValueSetPEOValueSetCode | — |
| VALUE_SET_ID | ValueSetPEOValueSetId | — |
| VALUE_SUBTYPE | ValueSetPEOValueSubtype | — |
| ZERO_FILL_FLAG | ValueSetPEOZeroFillFlag | — |

### [[groupinclobjectspvo|GroupInclObjectsPVO]] (GL · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ENTERPRISE_ID | ValueSetsBPEOEnterpriseId | — |
| VALUE_SET_CODE | ValueSetsBPEOValueSetCode | ✅ |
| VALUE_SET_ID | ValueSetsBPEOValueSetId | — |

### [[legalentitybalancingsegmentvaluespvo|LegalEntityBalancingSegmentValuesPVO]] (GL · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ENTERPRISE_ID | ValueSetsEnterpriseId | — |
| VALUE_SET_CODE | ValueSetsValueSetCode | ✅ |
| VALUE_SET_ID | ValueSetsValueSetId | — |

### [[ruleinputpvo|RuleInputPVO]] (GL · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ENTERPRISE_ID | ValueSetsBPEOEnterpriseId | — |
| VALUE_SET_CODE | ValueSetsBPEOValueSetCode | ✅ |
| VALUE_SET_ID | ValueSetsBPEOValueSetId | — |

### [[ruleoutputpvo|RuleOutputPVO]] (GL · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ENTERPRISE_ID | ValueSetsBPEOEnterpriseId | — |
| VALUE_SET_CODE | ValueSetsBPEOValueSetCode | ✅ |
| VALUE_SET_ID | ValueSetsBPEOValueSetId | — |

### [[ruletemplateinputpvo|RuleTemplateInputPVO]] (GL · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ENTERPRISE_ID | ValueSetsBPEOEnterpriseId | — |
| VALUE_SET_CODE | ValueSetsBPEOValueSetCode | ✅ |
| VALUE_SET_ID | ValueSetsBPEOValueSetId | — |

### [[ruletemplateusagepvo|RuleTemplateUsagePVO]] (GL · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ENTERPRISE_ID | ValueSetsBPEOEnterpriseId | — |
| VALUE_SET_CODE | ValueSetsBPEOValueSetCode | ✅ |
| VALUE_SET_ID | ValueSetsBPEOValueSetId | — |

### [[timeattributefieldallocationpvo|TimeAttributeFieldAllocationPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ENTERPRISE_ID | ValueSetsBPEOEnterpriseId | — |
| VALUE_SET_CODE | ValueSetsBPEOValueSetCode | — |
| VALUE_SET_ID | ValueSetsBPEOValueSetId | — |

### [[timeattributefieldcomponentpvo|TimeAttributeFieldComponentPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ENTERPRISE_ID | ValueSetsBPEOEnterpriseId | — |
| VALUE_SET_CODE | ValueSetsBPEOValueSetCode | — |
| VALUE_SET_ID | ValueSetsBPEOValueSetId | — |

### [[timeattributefieldcustompvo|TimeAttributeFieldCustomPVO]] (GL · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ENTERPRISE_ID | ValueSetsBPEOEnterpriseId | — |
| VALUE_SET_CODE | ValueSetsBPEOValueSetCode | ✅ |
| VALUE_SET_ID | ValueSetsBPEOValueSetId | — |

### [[timeattributefieldpvo|TimeAttributeFieldPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ENTERPRISE_ID | ValueSetsBPEOEnterpriseId | — |
| VALUE_SET_CODE | ValueSetsBPEOValueSetCode | — |
| VALUE_SET_ID | ValueSetsBPEOValueSetId | — |

### [[valuesetspvo|ValueSetsPVO]] (OTHER · BICC: 29/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATA_SECURITY_OBJECT_NAME | DataSecurityObjectName | ✅ |
| DESCRIPTION | Description | ✅ |
| INDEPENDENT_VALUE_SET_ID | IndependentValueSetId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MAXIMUM_LENGTH | MaximumLength | ✅ |
| MAXIMUM_VALUE | MaximumValue | ✅ |
| MAXIMUM_VALUE_DATE | MaximumValueDate | ✅ |
| MAXIMUM_VALUE_NUMBER | MaximumValueNumber | ✅ |
| MAXIMUM_VALUE_TIMESTAMP | MaximumValueTimestamp | ✅ |
| MINIMUM_VALUE | MinimumValue | ✅ |
| MINIMUM_VALUE_DATE | MinimumValueDate | ✅ |
| MINIMUM_VALUE_NUMBER | MinimumValueNumber | ✅ |
| MINIMUM_VALUE_TIMESTAMP | MinimumValueTimestamp | ✅ |
| MODULE_ID | ModuleId | ✅ |
| PRECISION | Precision | ✅ |
| PROTECTED_FLAG | ProtectedFlag | ✅ |
| SCALE | Scale | ✅ |
| SECURITY_ENABLED_FLAG | SecurityEnabledFlag | ✅ |
| UPPERCASE_ONLY_FLAG | UppercaseOnlyFlag | ✅ |
| VALIDATION_TYPE | ValidationType | ✅ |
| VALUE_DATA_TYPE | ValueDataType | ✅ |
| VALUE_SET_CODE | ValueSetCode | ✅ |
| VALUE_SET_ID | ValueSetId | ✅ |
| VALUE_SUBTYPE | ValueSubtype | ✅ |
| ZERO_FILL_FLAG | ZeroFillFlag | ✅ |

### [[valuesettypedvaluespvo|ValueSetTypedValuesPVO]] (HCM · BICC: 23/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy1 | ✅ |
| CREATION_DATE | CreationDate1 | ✅ |
| DATA_SECURITY_OBJECT_NAME | DataSecurityObjectName | ✅ |
| DESCRIPTION | Description | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| INDEPENDENT_VALUE_SET_ID | IndependentValueSetId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy1 | ✅ |
| MAXIMUM_LENGTH | MaximumLength | ✅ |
| MAXIMUM_VALUE | MaximumValue | ✅ |
| MINIMUM_VALUE | MinimumValue | ✅ |
| MODULE_ID | ModuleId | ✅ |
| PRECISION | Precision | ✅ |
| SCALE | Scale | ✅ |
| SECURITY_ENABLED_FLAG | SecurityEnabledFlag | ✅ |
| UPPERCASE_ONLY_FLAG | UppercaseOnlyFlag | ✅ |
| VALIDATION_TYPE | ValidationType | ✅ |
| VALUE_DATA_TYPE | ValueDataType | ✅ |
| VALUE_SET_CODE | ValueSetCode | ✅ |
| VALUE_SET_ID | ValueSetId1 | ✅ |
| VALUE_SUBTYPE | ValueSubtype | ✅ |
| ZERO_FILL_FLAG | ZeroFillFlag | ✅ |

### [[valuesettypedvaluestlpvo|ValueSetTypedValuesTLPVO]] (HCM · BICC: 3/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy2 | — |
| CREATION_DATE | CreationDate2 | — |
| DATA_SECURITY_OBJECT_NAME | DataSecurityObjectName | — |
| DESCRIPTION | Description1 | — |
| ENTERPRISE_ID | EnterpriseId | — |
| INDEPENDENT_VALUE_SET_ID | IndependentValueSetId | — |
| LAST_UPDATE_DATE | LastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin2 | — |
| LAST_UPDATED_BY | LastUpdatedBy2 | — |
| MAXIMUM_LENGTH | MaximumLength | — |
| MAXIMUM_VALUE | MaximumValue | — |
| MINIMUM_VALUE | MinimumValue | — |
| MODULE_ID | ModuleId | — |
| PRECISION | Precision | — |
| SCALE | Scale | — |
| SECURITY_ENABLED_FLAG | SecurityEnabledFlag | — |
| UPPERCASE_ONLY_FLAG | UppercaseOnlyFlag | — |
| VALIDATION_TYPE | ValidationType | ✅ |
| VALUE_DATA_TYPE | ValueDataType | — |
| VALUE_SET_CODE | ValueSetCode | ✅ |
| VALUE_SET_ID | ValueSetId1 | — |
| VALUE_SUBTYPE | ValueSubtype | — |
| ZERO_FILL_FLAG | ZeroFillFlag | — |
