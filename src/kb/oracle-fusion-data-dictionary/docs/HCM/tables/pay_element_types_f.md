---
id: DOC-HCM-573
doc_type: system-doc
title: "PAY_ELEMENT_TYPES_F — Tipos de Elementos de Folha"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - payroll
  - element-types
  - tipos-elementos
  - pay-elem-types
aliases:
  - PAY_ELEMENT_TYPES_F
  - pay_element_types_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ELEMENT_TYPES_F

## 📌 Visão Geral

Tabela central que armazena as **definicoes de tipos de elementos** de folha de pagamento (proventos, descontos, impostos, informacoes). Cada tipo de elemento define um componente de remuneracao com suas regras de calculo e classificacao.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao de elementos de folha (salario base, adicional noturno, INSS, etc.)
- Configuracao de regras de processamento por tipo
- Classificacao de elementos por categoria (earnings, deductions, etc.)
- Base para criacao de entradas de elementos

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ELEMENT_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do tipo de elemento | --- | 🟢 95% |
| 2 | ELEMENT_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome do tipo de elemento | --- | 🟢 95% |
| 3 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NOT NULL | FK | ID do grupo legislativo | --- | 🟢 90% |
| 4 | CLASSIFICATION_ID | NUMBER(18) | NOT NULL | FK | ID da classificacao do elemento | PAY_ELE_CLASSIFICATIONS | 🟢 90% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 7 | PROCESSING_PRIORITY | NUMBER | NULL | Dados | Prioridade de processamento | --- | 🟢 85% |
| 8 | PROCESSING_TYPE | VARCHAR2(1) | NULL | Classificacao | Tipo de processamento (R=Recurring, N=Nonrecurring) | --- | 🟢 85% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_ele_classifications]] --- via `CLASSIFICATION_ID` (classificação do tipo de elemento de folha)

### Tabelas-filha (FK de saída)
- [[pay_element_entries_f]] --- via `ELEMENT_TYPE_ID` (entradas de folha do tipo de elemento)
- [[pay_input_values_f]] --- via `ELEMENT_TYPE_ID` (valores de entrada do tipo de elemento)
- [[pay_element_types_tl]] --- via `ELEMENT_TYPE_ID` (traduções do tipo de elemento de folha)
- [[pay_element_criteria]] --- via `ELEMENT_TYPE_ID` (critérios de elegibilidade do tipo de elemento)

---

## 📎 Uso Típico

### Tipos de elementos vigentes por grupo legislativo
```sql
SELECT et.ELEMENT_TYPE_ID, et.ELEMENT_NAME, et.PROCESSING_TYPE
FROM   PAY_ELEMENT_TYPES_F et
WHERE  et.LEGISLATIVE_DATA_GROUP_ID = :p_ldg_id
  AND  SYSDATE BETWEEN et.EFFECTIVE_START_DATE AND et.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- Processing Type: R=Recorrente (todo periodo), N=Nao recorrente (pontual).
- Tabela fundamental do Payroll; todos os calculos de folha se baseiam em element types.

---

## 🔗 PVOs Relacionados

### [[bielementtype|BIElementType]] (HCM · BICC: 182/182)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_ENTRY_ALLOWED_FLAG | ElementTypeBaseDPEOAdditionalEntryAllowedFlag | ✅ |
| ADJUSTMENT_ONLY_FLAG | ElementTypeBaseDPEOAdjustmentOnlyFlag | ✅ |
| ATTRIBUTE1 | ElementTypeBaseDPEOAttribute1 | ✅ |
| ATTRIBUTE10 | ElementTypeBaseDPEOAttribute10 | ✅ |
| ATTRIBUTE11 | ElementTypeBaseDPEOAttribute11 | ✅ |
| ATTRIBUTE12 | ElementTypeBaseDPEOAttribute12 | ✅ |
| ATTRIBUTE13 | ElementTypeBaseDPEOAttribute13 | ✅ |
| ATTRIBUTE14 | ElementTypeBaseDPEOAttribute14 | ✅ |
| ATTRIBUTE15 | ElementTypeBaseDPEOAttribute15 | ✅ |
| ATTRIBUTE16 | ElementTypeBaseDPEOAttribute16 | ✅ |
| ATTRIBUTE17 | ElementTypeBaseDPEOAttribute17 | ✅ |
| ATTRIBUTE18 | ElementTypeBaseDPEOAttribute18 | ✅ |
| ATTRIBUTE19 | ElementTypeBaseDPEOAttribute19 | ✅ |
| ATTRIBUTE2 | ElementTypeBaseDPEOAttribute2 | ✅ |
| ATTRIBUTE20 | ElementTypeBaseDPEOAttribute20 | ✅ |
| ATTRIBUTE21 | ElementTypeBaseDPEOAttribute21 | ✅ |
| ATTRIBUTE22 | ElementTypeBaseDPEOAttribute22 | ✅ |
| ATTRIBUTE23 | ElementTypeBaseDPEOAttribute23 | ✅ |
| ATTRIBUTE24 | ElementTypeBaseDPEOAttribute24 | ✅ |
| ATTRIBUTE25 | ElementTypeBaseDPEOAttribute25 | ✅ |
| ATTRIBUTE26 | ElementTypeBaseDPEOAttribute26 | ✅ |
| ATTRIBUTE27 | ElementTypeBaseDPEOAttribute27 | ✅ |
| ATTRIBUTE28 | ElementTypeBaseDPEOAttribute28 | ✅ |
| ATTRIBUTE29 | ElementTypeBaseDPEOAttribute29 | ✅ |
| ATTRIBUTE3 | ElementTypeBaseDPEOAttribute3 | ✅ |
| ATTRIBUTE30 | ElementTypeBaseDPEOAttribute30 | ✅ |
| ATTRIBUTE4 | ElementTypeBaseDPEOAttribute4 | ✅ |
| ATTRIBUTE5 | ElementTypeBaseDPEOAttribute5 | ✅ |
| ATTRIBUTE6 | ElementTypeBaseDPEOAttribute6 | ✅ |
| ATTRIBUTE7 | ElementTypeBaseDPEOAttribute7 | ✅ |
| ATTRIBUTE8 | ElementTypeBaseDPEOAttribute8 | ✅ |
| ATTRIBUTE9 | ElementTypeBaseDPEOAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | ElementTypeBaseDPEOAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | ElementTypeBaseDPEOAttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | ElementTypeBaseDPEOAttributeDate10 | ✅ |
| ATTRIBUTE_DATE11 | ElementTypeBaseDPEOAttributeDate11 | ✅ |
| ATTRIBUTE_DATE12 | ElementTypeBaseDPEOAttributeDate12 | ✅ |
| ATTRIBUTE_DATE13 | ElementTypeBaseDPEOAttributeDate13 | ✅ |
| ATTRIBUTE_DATE14 | ElementTypeBaseDPEOAttributeDate14 | ✅ |
| ATTRIBUTE_DATE15 | ElementTypeBaseDPEOAttributeDate15 | ✅ |
| ATTRIBUTE_DATE2 | ElementTypeBaseDPEOAttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | ElementTypeBaseDPEOAttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | ElementTypeBaseDPEOAttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | ElementTypeBaseDPEOAttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | ElementTypeBaseDPEOAttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | ElementTypeBaseDPEOAttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | ElementTypeBaseDPEOAttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | ElementTypeBaseDPEOAttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | ElementTypeBaseDPEOAttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | ElementTypeBaseDPEOAttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER11 | ElementTypeBaseDPEOAttributeNumber11 | ✅ |
| ATTRIBUTE_NUMBER12 | ElementTypeBaseDPEOAttributeNumber12 | ✅ |
| ATTRIBUTE_NUMBER13 | ElementTypeBaseDPEOAttributeNumber13 | ✅ |
| ATTRIBUTE_NUMBER14 | ElementTypeBaseDPEOAttributeNumber14 | ✅ |
| ATTRIBUTE_NUMBER15 | ElementTypeBaseDPEOAttributeNumber15 | ✅ |
| ATTRIBUTE_NUMBER16 | ElementTypeBaseDPEOAttributeNumber16 | ✅ |
| ATTRIBUTE_NUMBER17 | ElementTypeBaseDPEOAttributeNumber17 | ✅ |
| ATTRIBUTE_NUMBER18 | ElementTypeBaseDPEOAttributeNumber18 | ✅ |
| ATTRIBUTE_NUMBER19 | ElementTypeBaseDPEOAttributeNumber19 | ✅ |
| ATTRIBUTE_NUMBER2 | ElementTypeBaseDPEOAttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER20 | ElementTypeBaseDPEOAttributeNumber20 | ✅ |
| ATTRIBUTE_NUMBER3 | ElementTypeBaseDPEOAttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | ElementTypeBaseDPEOAttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | ElementTypeBaseDPEOAttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | ElementTypeBaseDPEOAttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | ElementTypeBaseDPEOAttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | ElementTypeBaseDPEOAttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | ElementTypeBaseDPEOAttributeNumber9 | ✅ |
| BASE_ELEMENT_NAME | ElementTypeBaseDPEOBaseElementName | ✅ |
| CALCULATION_FORMULA_ID | ElementTypeBaseDPEOCalculationFormulaId | ✅ |
| CLASSIFICATION_ID | ElementTypeBaseDPEOClassificationId | ✅ |
| CLOSED_FOR_ENTRY_FLAG | ElementTypeBaseDPEOClosedForEntryFlag | ✅ |
| CREATED_BY | ElementTypeBaseDPEOCreatedBy | ✅ |
| CREATION_DATE | ElementTypeBaseDPEOCreationDate | ✅ |
| CREATOR_TYPE | ElementTypeBaseDPEOCreatorType | ✅ |
| DEDUCTION_OR_EXEMPTION | ElementTypeBaseDPEODeductionOrExemption | ✅ |
| DEDUCTION_TYPE_ID | ElementTypeBaseDPEODeductionTypeId | ✅ |
| DEFAULTING_FORMULA_ID | ElementTypeBaseDPEODefaultingFormulaId | ✅ |
| EFFECTIVE_END_DATE | ElementTypeBaseDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | ElementTypeBaseDPEOEffectiveStartDate | ✅ |
| ELEMENT_INFORMATION1 | ElementTypeBaseDPEOElementInformation1 | ✅ |
| ELEMENT_INFORMATION10 | ElementTypeBaseDPEOElementInformation10 | ✅ |
| ELEMENT_INFORMATION11 | ElementTypeBaseDPEOElementInformation11 | ✅ |
| ELEMENT_INFORMATION12 | ElementTypeBaseDPEOElementInformation12 | ✅ |
| ELEMENT_INFORMATION13 | ElementTypeBaseDPEOElementInformation13 | ✅ |
| ELEMENT_INFORMATION14 | ElementTypeBaseDPEOElementInformation14 | ✅ |
| ELEMENT_INFORMATION15 | ElementTypeBaseDPEOElementInformation15 | ✅ |
| ELEMENT_INFORMATION16 | ElementTypeBaseDPEOElementInformation16 | ✅ |
| ELEMENT_INFORMATION17 | ElementTypeBaseDPEOElementInformation17 | ✅ |
| ELEMENT_INFORMATION18 | ElementTypeBaseDPEOElementInformation18 | ✅ |
| ELEMENT_INFORMATION19 | ElementTypeBaseDPEOElementInformation19 | ✅ |
| ELEMENT_INFORMATION2 | ElementTypeBaseDPEOElementInformation2 | ✅ |
| ELEMENT_INFORMATION20 | ElementTypeBaseDPEOElementInformation20 | ✅ |
| ELEMENT_INFORMATION21 | ElementTypeBaseDPEOElementInformation21 | ✅ |
| ELEMENT_INFORMATION22 | ElementTypeBaseDPEOElementInformation22 | ✅ |
| ELEMENT_INFORMATION23 | ElementTypeBaseDPEOElementInformation23 | ✅ |
| ELEMENT_INFORMATION24 | ElementTypeBaseDPEOElementInformation24 | ✅ |
| ELEMENT_INFORMATION25 | ElementTypeBaseDPEOElementInformation25 | ✅ |
| ELEMENT_INFORMATION26 | ElementTypeBaseDPEOElementInformation26 | ✅ |
| ELEMENT_INFORMATION27 | ElementTypeBaseDPEOElementInformation27 | ✅ |
| ELEMENT_INFORMATION28 | ElementTypeBaseDPEOElementInformation28 | ✅ |
| ELEMENT_INFORMATION29 | ElementTypeBaseDPEOElementInformation29 | ✅ |
| ELEMENT_INFORMATION3 | ElementTypeBaseDPEOElementInformation3 | ✅ |
| ELEMENT_INFORMATION30 | ElementTypeBaseDPEOElementInformation30 | ✅ |
| ELEMENT_INFORMATION4 | ElementTypeBaseDPEOElementInformation4 | ✅ |
| ELEMENT_INFORMATION5 | ElementTypeBaseDPEOElementInformation5 | ✅ |
| ELEMENT_INFORMATION6 | ElementTypeBaseDPEOElementInformation6 | ✅ |
| ELEMENT_INFORMATION7 | ElementTypeBaseDPEOElementInformation7 | ✅ |
| ELEMENT_INFORMATION8 | ElementTypeBaseDPEOElementInformation8 | ✅ |
| ELEMENT_INFORMATION9 | ElementTypeBaseDPEOElementInformation9 | ✅ |
| ELEMENT_INFORMATION_CATEGORY | ElementTypeBaseDPEOElementInformationCategory | ✅ |
| ELEMENT_INFORMATION_DATE1 | ElementTypeBaseDPEOElementInformationDate1 | ✅ |
| ELEMENT_INFORMATION_DATE10 | ElementTypeBaseDPEOElementInformationDate10 | ✅ |
| ELEMENT_INFORMATION_DATE11 | ElementTypeBaseDPEOElementInformationDate11 | ✅ |
| ELEMENT_INFORMATION_DATE12 | ElementTypeBaseDPEOElementInformationDate12 | ✅ |
| ELEMENT_INFORMATION_DATE13 | ElementTypeBaseDPEOElementInformationDate13 | ✅ |
| ELEMENT_INFORMATION_DATE14 | ElementTypeBaseDPEOElementInformationDate14 | ✅ |
| ELEMENT_INFORMATION_DATE15 | ElementTypeBaseDPEOElementInformationDate15 | ✅ |
| ELEMENT_INFORMATION_DATE2 | ElementTypeBaseDPEOElementInformationDate2 | ✅ |
| ELEMENT_INFORMATION_DATE3 | ElementTypeBaseDPEOElementInformationDate3 | ✅ |
| ELEMENT_INFORMATION_DATE4 | ElementTypeBaseDPEOElementInformationDate4 | ✅ |
| ELEMENT_INFORMATION_DATE5 | ElementTypeBaseDPEOElementInformationDate5 | ✅ |
| ELEMENT_INFORMATION_DATE6 | ElementTypeBaseDPEOElementInformationDate6 | ✅ |
| ELEMENT_INFORMATION_DATE7 | ElementTypeBaseDPEOElementInformationDate7 | ✅ |
| ELEMENT_INFORMATION_DATE8 | ElementTypeBaseDPEOElementInformationDate8 | ✅ |
| ELEMENT_INFORMATION_DATE9 | ElementTypeBaseDPEOElementInformationDate9 | ✅ |
| ELEMENT_INFORMATION_NUMBER1 | ElementTypeBaseDPEOElementInformationNumber1 | ✅ |
| ELEMENT_INFORMATION_NUMBER10 | ElementTypeBaseDPEOElementInformationNumber10 | ✅ |
| ELEMENT_INFORMATION_NUMBER11 | ElementTypeBaseDPEOElementInformationNumber11 | ✅ |
| ELEMENT_INFORMATION_NUMBER12 | ElementTypeBaseDPEOElementInformationNumber12 | ✅ |
| ELEMENT_INFORMATION_NUMBER13 | ElementTypeBaseDPEOElementInformationNumber13 | ✅ |
| ELEMENT_INFORMATION_NUMBER14 | ElementTypeBaseDPEOElementInformationNumber14 | ✅ |
| ELEMENT_INFORMATION_NUMBER15 | ElementTypeBaseDPEOElementInformationNumber15 | ✅ |
| ELEMENT_INFORMATION_NUMBER16 | ElementTypeBaseDPEOElementInformationNumber16 | ✅ |
| ELEMENT_INFORMATION_NUMBER17 | ElementTypeBaseDPEOElementInformationNumber17 | ✅ |
| ELEMENT_INFORMATION_NUMBER18 | ElementTypeBaseDPEOElementInformationNumber18 | ✅ |
| ELEMENT_INFORMATION_NUMBER19 | ElementTypeBaseDPEOElementInformationNumber19 | ✅ |
| ELEMENT_INFORMATION_NUMBER2 | ElementTypeBaseDPEOElementInformationNumber2 | ✅ |
| ELEMENT_INFORMATION_NUMBER20 | ElementTypeBaseDPEOElementInformationNumber20 | ✅ |
| ELEMENT_INFORMATION_NUMBER3 | ElementTypeBaseDPEOElementInformationNumber3 | ✅ |
| ELEMENT_INFORMATION_NUMBER4 | ElementTypeBaseDPEOElementInformationNumber4 | ✅ |
| ELEMENT_INFORMATION_NUMBER5 | ElementTypeBaseDPEOElementInformationNumber5 | ✅ |
| ELEMENT_INFORMATION_NUMBER6 | ElementTypeBaseDPEOElementInformationNumber6 | ✅ |
| ELEMENT_INFORMATION_NUMBER7 | ElementTypeBaseDPEOElementInformationNumber7 | ✅ |
| ELEMENT_INFORMATION_NUMBER8 | ElementTypeBaseDPEOElementInformationNumber8 | ✅ |
| ELEMENT_INFORMATION_NUMBER9 | ElementTypeBaseDPEOElementInformationNumber9 | ✅ |
| ELEMENT_TYPE_ID | ElementTypeBaseDPEOElementTypeId | ✅ |
| ENDING_TIME_DEF_ID | ElementTypeBaseDPEOEndingTimeDefId | ✅ |
| FORMULA_ID | ElementTypeBaseDPEOFormulaId | ✅ |
| GROSSUP_FLAG | ElementTypeBaseDPEOGrossupFlag | ✅ |
| INDIRECT_ONLY_FLAG | ElementTypeBaseDPEOIndirectOnlyFlag | ✅ |
| INPUT_CURRENCY_CODE | ElementTypeBaseDPEOInputCurrencyCode | ✅ |
| ITERATIVE_FLAG | ElementTypeBaseDPEOIterativeFlag | ✅ |
| ITERATIVE_FORMULA_ID | ElementTypeBaseDPEOIterativeFormulaId | ✅ |
| ITERATIVE_PRIORITY | ElementTypeBaseDPEOIterativePriority | ✅ |
| LAST_UPDATE_DATE | ElementTypeBaseDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ElementTypeBaseDPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ElementTypeBaseDPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | ElementTypeBaseDPEOLegislationCode | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | ElementTypeBaseDPEOLegislativeDataGroupId | ✅ |
| MODULE_ID | ElementTypeBaseDPEOModuleId | ✅ |
| MULTIPLE_ENTRIES_ALLOWED_FLAG | ElementTypeBaseDPEOMultipleEntriesAllowedFlag | ✅ |
| OBJECT_VERSION_NUMBER | ElementTypeBaseDPEOObjectVersionNumber | ✅ |
| ONCE_EACH_PERIOD_FLAG | ElementTypeBaseDPEOOnceEachPeriodFlag | ✅ |
| OUTPUT_CURRENCY_CODE | ElementTypeBaseDPEOOutputCurrencyCode | ✅ |
| PROCESS_IN_RUN_FLAG | ElementTypeBaseDPEOProcessInRunFlag | ✅ |
| PROCESS_MODE | ElementTypeBaseDPEOProcessMode | ✅ |
| PROCESSING_PRIORITY | ElementTypeBaseDPEOProcessingPriority | ✅ |
| PROCESSING_TYPE | ElementTypeBaseDPEOProcessingType | ✅ |
| PRORATION_FORMULA_ID | ElementTypeBaseDPEOProrationFormulaId | ✅ |
| PRORATION_GROUP_ID | ElementTypeBaseDPEOProrationGroupId | ✅ |
| RECALC_EVENT_GROUP_ID | ElementTypeBaseDPEORecalcEventGroupId | ✅ |
| SECONDARY_CLASSIFICATION_ID | ElementTypeBaseDPEOSecondaryClassificationId | ✅ |
| STANDARD_LINK_FLAG | ElementTypeBaseDPEOStandardLinkFlag | ✅ |
| STARTING_TIME_DEF_ID | ElementTypeBaseDPEOStartingTimeDefId | ✅ |
| TIME_DEFINITION_ID | ElementTypeBaseDPEOTimeDefinitionId | ✅ |
| TIME_DEFINITION_TYPE | ElementTypeBaseDPEOTimeDefinitionType | ✅ |
| USE_AT_ASG_LEVEL | ElementTypeBaseDPEOUseAtAsgLevel | ✅ |
| USE_AT_REL_LEVEL | ElementTypeBaseDPEOUseAtRelLevel | ✅ |
| USE_AT_TERM_LEVEL | ElementTypeBaseDPEOUseAtTermLevel | ✅ |
| VALIDATION_FORMULA_ID | ElementTypeBaseDPEOValidationFormulaId | ✅ |
| VALIDATION_OVERRIDE_MESSAGE | ElementTypeBaseDPEOValidationOverrideMessage | ✅ |

### [[elementtypeclassificationpvo|ElementTypeClassificationPVO]] (GL · BICC: 4/50)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_ENTRY_ALLOWED_FLAG | ElementTypeDPEOAdditionalEntryAllowedFlag | — |
| ADJUSTMENT_ONLY_FLAG | ElementTypeDPEOAdjustmentOnlyFlag | — |
| BASE_ELEMENT_NAME | ElementTypeDPEOBaseElementName | — |
| CALCULATION_FORMULA_ID | ElementTypeDPEOCalculationFormulaId | — |
| CLASSIFICATION_ID | ElementTypeDPEOClassificationId | — |
| CLOSED_FOR_ENTRY_FLAG | ElementTypeDPEOClosedForEntryFlag | — |
| CREATED_BY | ElementTypeDPEOCreatedBy | — |
| CREATION_DATE | ElementTypeDPEOCreationDate | — |
| CREATOR_TYPE | ElementTypeDPEOCreatorType | — |
| DEDUCTION_OR_EXEMPTION | ElementTypeDPEODeductionOrExemption | — |
| DEDUCTION_TYPE_ID | ElementTypeDPEODeductionTypeId | — |
| DEFAULTING_FORMULA_ID | ElementTypeDPEODefaultingFormulaId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ELEMENT_TYPE_ID | ElementTypeId | ✅ |
| ENDING_TIME_DEF_ID | ElementTypeDPEOEndingTimeDefId | — |
| FORMULA_ID | ElementTypeDPEOFormulaId | — |
| GROSSUP_FLAG | ElementTypeDPEOGrossupFlag | — |
| INDIRECT_ONLY_FLAG | ElementTypeDPEOIndirectOnlyFlag | — |
| INPUT_CURRENCY_CODE | ElementTypeDPEOInputCurrencyCode | — |
| ITERATIVE_FLAG | ElementTypeDPEOIterativeFlag | — |
| ITERATIVE_FORMULA_ID | ElementTypeDPEOIterativeFormulaId | — |
| ITERATIVE_PRIORITY | ElementTypeDPEOIterativePriority | — |
| LAST_UPDATE_DATE | ElementTypeDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ElementTypeDPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ElementTypeDPEOLastUpdatedBy | — |
| LEGISLATION_CODE | ElementTypeDPEOLegislationCode | — |
| LEGISLATIVE_DATA_GROUP_ID | ElementTypeDPEOLegislativeDataGroupId | — |
| MODULE_ID | ElementTypeDPEOModuleId | — |
| MULTIPLE_ENTRIES_ALLOWED_FLAG | ElementTypeDPEOMultipleEntriesAllowedFlag | — |
| OBJECT_VERSION_NUMBER | ElementTypeDPEOObjectVersionNumber | — |
| ONCE_EACH_PERIOD_FLAG | ElementTypeDPEOOnceEachPeriodFlag | — |
| OUTPUT_CURRENCY_CODE | ElementTypeDPEOOutputCurrencyCode | — |
| PROCESS_IN_RUN_FLAG | ElementTypeDPEOProcessInRunFlag | — |
| PROCESS_MODE | ElementTypeDPEOProcessMode | — |
| PROCESSING_PRIORITY | ElementTypeDPEOProcessingPriority | — |
| PROCESSING_TYPE | ElementTypeDPEOProcessingType | — |
| PRORATION_FORMULA_ID | ElementTypeDPEOProrationFormulaId | — |
| PRORATION_GROUP_ID | ElementTypeDPEOProrationGroupId | — |
| RECALC_EVENT_GROUP_ID | ElementTypeDPEORecalcEventGroupId | — |
| SECONDARY_CLASSIFICATION_ID | ElementTypeDPEOSecondaryClassificationId | — |
| STANDARD_LINK_FLAG | ElementTypeDPEOStandardLinkFlag | — |
| STARTING_TIME_DEF_ID | ElementTypeDPEOStartingTimeDefId | — |
| TIME_DEFINITION_ID | ElementTypeDPEOTimeDefinitionId | — |
| TIME_DEFINITION_TYPE | ElementTypeDPEOTimeDefinitionType | — |
| USE_AT_ASG_LEVEL | ElementTypeDPEOUseAtAsgLevel | — |
| USE_AT_REL_LEVEL | ElementTypeDPEOUseAtRelLevel | — |
| USE_AT_TERM_LEVEL | ElementTypeDPEOUseAtTermLevel | — |
| VALIDATION_FORMULA_ID | ElementTypeDPEOValidationFormulaId | — |
| VALIDATION_OVERRIDE_MESSAGE | ElementTypeDPEOValidationOverrideMessage | — |

### [[originatingelement|OriginatingElement]] (HCM · BICC: 12/52)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_ENTRY_ALLOWED_FLAG | ElementTypeAdditionalEntryAllowedFlag | — |
| ADJUSTMENT_ONLY_FLAG | ElementTypeAdjustmentOnlyFlag | — |
| ATTRIBUTE_CATEGORY | ElementTypeAttributeCategory | — |
| BASE_ELEMENT_NAME | ElementTypeBaseElementName | — |
| CALCULATION_FORMULA_ID | ElementTypeCalculationFormulaId | — |
| CLASSIFICATION_ID | ElementTypeClassificationId | ✅ |
| CLOSED_FOR_ENTRY_FLAG | ElementTypeClosedForEntryFlag | — |
| CREATED_BY | ElementTypeCreatedBy | — |
| CREATION_DATE | ElementTypeCreationDate | — |
| CREATOR_TYPE | ElementTypeCreatorType | — |
| DEDUCTION_OR_EXEMPTION | ElementTypeDeductionOrExemption | — |
| DEDUCTION_TYPE_ID | ElementTypeDeductionTypeId | — |
| DEFAULTING_FORMULA_ID | ElementTypeDefaultingFormulaId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ELEMENT_INFORMATION_CATEGORY | ElementTypeElementInformationCategory | — |
| ELEMENT_TYPE_ID | ElementTypeId | ✅ |
| ENDING_TIME_DEF_ID | ElementTypeEndingTimeDefId | — |
| FORMULA_ID | ElementTypeFormulaId | — |
| GROSSUP_FLAG | ElementTypeGrossupFlag | — |
| INDIRECT_ONLY_FLAG | ElementTypeIndirectOnlyFlag | — |
| INPUT_CURRENCY_CODE | ElementTypeInputCurrencyCode | ✅ |
| ITERATIVE_FLAG | ElementTypeIterativeFlag | — |
| ITERATIVE_FORMULA_ID | ElementTypeIterativeFormulaId | — |
| ITERATIVE_PRIORITY | ElementTypeIterativePriority | — |
| LAST_UPDATE_DATE | ElementTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ElementTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | ElementTypeLastUpdatedBy | — |
| LEGISLATION_CODE | ElementTypeLegislationCode | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | ElementTypeLegislativeDataGroupId | ✅ |
| MODULE_ID | ElementTypeModuleId | — |
| MULTIPLE_ENTRIES_ALLOWED_FLAG | ElementTypeMultipleEntriesAllowedFlag | — |
| OBJECT_VERSION_NUMBER | ElementTypeObjectVersionNumber | — |
| ONCE_EACH_PERIOD_FLAG | ElementTypeOnceEachPeriodFlag | — |
| OUTPUT_CURRENCY_CODE | ElementTypeOutputCurrencyCode | ✅ |
| PROCESS_IN_RUN_FLAG | ElementTypeProcessInRunFlag | — |
| PROCESS_MODE | ElementTypeProcessMode | — |
| PROCESSING_PRIORITY | ElementTypeProcessingPriority | — |
| PROCESSING_TYPE | ElementTypeProcessingType | ✅ |
| PRORATION_FORMULA_ID | ElementTypeProrationFormulaId | — |
| PRORATION_GROUP_ID | ElementTypeProrationGroupId | — |
| RECALC_EVENT_GROUP_ID | ElementTypeRecalcEventGroupId | ✅ |
| SECONDARY_CLASSIFICATION_ID | ElementTypeSecondaryClassificationId | ✅ |
| STANDARD_LINK_FLAG | ElementTypeStandardLinkFlag | — |
| STARTING_TIME_DEF_ID | ElementTypeStartingTimeDefId | — |
| TIME_DEFINITION_ID | ElementTypeTimeDefinitionId | — |
| TIME_DEFINITION_TYPE | ElementTypeTimeDefinitionType | — |
| USE_AT_ASG_LEVEL | ElementTypeUseAtAsgLevel | — |
| USE_AT_REL_LEVEL | ElementTypeUseAtRelLevel | — |
| USE_AT_TERM_LEVEL | ElementTypeUseAtTermLevel | — |
| VALIDATION_FORMULA_ID | ElementTypeValidationFormulaId | — |
| VALIDATION_OVERRIDE_MESSAGE | ElementTypeValidationOverrideMessage | — |

---

## 📚 Referências

- [Oracle Docs — PAY_ELEMENT_TYPES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payelementtypesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
