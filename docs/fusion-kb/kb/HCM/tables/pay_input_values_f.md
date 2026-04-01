---
id: DOC-HCM-579
doc_type: system-doc
title: "PAY_INPUT_VALUES_F — Valores de Entrada de Elementos (Input Values)"
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
  - input-values
  - valores-entrada
  - pay-input-values
aliases:
  - PAY_INPUT_VALUES_F
  - pay_input_values_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_INPUT_VALUES_F

## 📌 Visão Geral

Armazena as **definicoes de input values** de cada tipo de elemento de folha. Input values sao os parametros que um elemento aceita (ex.: Amount, Hours, Rate, Percentage). Date-effective (`_F`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao de parametros aceitos por tipo de elemento
- Configuracao de valores padrao e limites de validacao
- Base para captura de valores em entradas de elementos

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INPUT_VALUE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do input value | --- | 🟢 95% |
| 2 | ELEMENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | ID do tipo de elemento | PAY_ELEMENT_TYPES_F | 🟢 95% |
| 3 | NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome do input value | --- | 🟢 90% |
| 4 | UOM | VARCHAR2(30) | NULL | Classificacao | Unidade de medida (M=Money, H=Hours, N=Number) | --- | 🟢 85% |
| 5 | DEFAULT_VALUE | VARCHAR2(60) | NULL | Dados | Valor padrao | --- | 🟡 80% |
| 6 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 7 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_element_types_f]] --- via `ELEMENT_TYPE_ID` (tipo de elemento do valor de entrada)

### Tabelas-filha (FK de saída)
- [[pay_element_entry_values_f]] --- via `INPUT_VALUE_ID` (valores preenchidos para este input)
- [[pay_input_values_tl]] --- via `INPUT_VALUE_ID` (traduções do valor de entrada)

---

## 📎 Uso Típico

### Input values vigentes de um tipo de elemento
```sql
SELECT iv.INPUT_VALUE_ID, iv.NAME, iv.UOM, iv.DEFAULT_VALUE
FROM   PAY_INPUT_VALUES_F iv
WHERE  iv.ELEMENT_TYPE_ID = :p_element_type_id
  AND  SYSDATE BETWEEN iv.EFFECTIVE_START_DATE AND iv.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- UOM: M=Monetario, H=Horas, N=Numerico, D=Data.
- Cada element type tem pelo menos um input value (tipicamente 'Pay Value').

---

## 🔗 PVOs Relacionados

### [[accrualcalculationruleinputvaluepvo|AccrualCalculationRuleInputValuePVO]] (GL · BICC: 2/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BASE_NAME | InputValueDPEOBaseName | — |
| CONTEXT_ID | InputValueDPEOContextId | — |
| CREATED_BY | InputValueDPEOCreatedBy | — |
| CREATION_DATE | InputValueDPEOCreationDate | — |
| DEFAULT_VALUE | InputValueDPEODefaultValue | — |
| DISPLAY_SEQUENCE | InputValueDPEODisplaySequence | — |
| EFFECTIVE_END_DATE | InputValueDPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InputValueDPEOEffectiveStartDate | ✅ |
| ELEMENT_TYPE_ID | InputValueDPEOElementTypeId | — |
| FORCE_RRV_MODE | InputValueDPEOForceRrvMode | — |
| FORMULA_ID | InputValueDPEOFormulaId | — |
| GENERATE_DB_ITEMS_FLAG | InputValueDPEOGenerateDbItemsFlag | — |
| HOT_DEFAULT_FLAG | InputValueDPEOHotDefaultFlag | — |
| INPUT_VALUE_ID | InputValueDPEOInputValueId | — |
| LAST_UPDATE_DATE | InputValueDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InputValueDPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InputValueDPEOLastUpdatedBy | — |
| LOOKUP_TYPE | InputValueDPEOLookupType | — |
| MANDATORY_FLAG | InputValueDPEOMandatoryFlag | — |
| MAX_VALUE | InputValueDPEOMaxValue | — |
| MIN_VALUE | InputValueDPEOMinValue | — |
| OBJECT_VERSION_NUMBER | InputValueDPEOObjectVersionNumber | — |
| RESERVED_INPUT_VALUE | InputValueDPEOReservedInputValue | — |
| RETRO_STATIC_FLAG | InputValueDPEORetroStaticFlag | — |
| UOM | InputValueDPEOUom | — |
| USER_DISPLAY_FLAG | InputValueDPEOUserDisplayFlag | — |
| USER_ENTERABLE_FLAG | InputValueDPEOUserEnterableFlag | — |
| VALIDATION_OVERRIDE_MESSAGE | InputValueDPEOValidationOverrideMessage | — |
| VO_NAME | InputValueDPEOVoName | — |
| WARNING_OR_ERROR | InputValueDPEOWarningOrError | — |

### [[inputvalue|InputValue]] (HCM · BICC: 19/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BASE_NAME | InputValueDPEOBaseName | ✅ |
| CONTEXT_ID | InputValueDPEOContextId | — |
| CREATED_BY | InputValueDPEOCreatedBy | ✅ |
| CREATION_DATE | InputValueDPEOCreationDate | ✅ |
| DEFAULT_VALUE | InputValueDPEODefaultValue | ✅ |
| DISPLAY_SEQUENCE | InputValueDPEODisplaySequence | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ELEMENT_TYPE_ID | InputValueDPEOElementTypeId | ✅ |
| FORCE_RRV_MODE | InputValueDPEOForceRrvMode | — |
| FORMULA_ID | InputValueDPEOFormulaId | — |
| GENERATE_DB_ITEMS_FLAG | InputValueDPEOGenerateDbItemsFlag | — |
| HOT_DEFAULT_FLAG | InputValueDPEOHotDefaultFlag | ✅ |
| INPUT_VALUE_ID | InputValueId | ✅ |
| LAST_UPDATE_DATE | InputValueDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InputValueDPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InputValueDPEOLastUpdatedBy | ✅ |
| LOOKUP_TYPE | InputValueDPEOLookupType | — |
| MANDATORY_FLAG | InputValueDPEOMandatoryFlag | ✅ |
| MAX_VALUE | InputValueDPEOMaxValue | ✅ |
| MIN_VALUE | InputValueDPEOMinValue | ✅ |
| OBJECT_VERSION_NUMBER | InputValueDPEOObjectVersionNumber | — |
| RESERVED_INPUT_VALUE | InputValueDPEOReservedInputValue | ✅ |
| RETRO_STATIC_FLAG | InputValueDPEORetroStaticFlag | — |
| UOM | InputValueDPEOUom | ✅ |
| USER_DISPLAY_FLAG | InputValueDPEOUserDisplayFlag | ✅ |
| USER_ENTERABLE_FLAG | InputValueDPEOUserEnterableFlag | — |
| VALIDATION_OVERRIDE_MESSAGE | InputValueDPEOValidationOverrideMessage | — |
| VO_NAME | InputValueDPEOVoName | ✅ |
| WARNING_OR_ERROR | InputValueDPEOWarningOrError | — |

### [[inputvaluepvo|InputValuePVO]] (HCM · BICC: 18/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BASE_NAME | InputValuePEOBaseName | — |
| CONTEXT_ID | InputValuePEOContextId | — |
| CREATED_BY | InputValuePEOCreatedBy | ✅ |
| CREATION_DATE | InputValuePEOCreationDate | ✅ |
| DEFAULT_VALUE | InputValuePEODefaultValue | ✅ |
| DISPLAY_SEQUENCE | InputValuePEODisplaySequence | ✅ |
| EFFECTIVE_END_DATE | InputValuePEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | InputValuePEOEffectiveStartDate | ✅ |
| ELEMENT_TYPE_ID | InputValuePEOElementTypeId | ✅ |
| FORCE_RRV_MODE | InputValuePEOForceRrvMode | — |
| FORMULA_ID | InputValuePEOFormulaId | — |
| GENERATE_DB_ITEMS_FLAG | InputValuePEOGenerateDbItemsFlag | — |
| HOT_DEFAULT_FLAG | InputValuePEOHotDefaultFlag | ✅ |
| INPUT_VALUE_ID | InputValueId | ✅ |
| LAST_UPDATE_DATE | InputValuePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InputValuePEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | InputValuePEOLastUpdatedBy | — |
| LOOKUP_TYPE | InputValuePEOLookupType | — |
| MANDATORY_FLAG | InputValuePEOMandatoryFlag | ✅ |
| MAX_VALUE | InputValuePEOMaxValue | ✅ |
| MIN_VALUE | InputValuePEOMinValue | ✅ |
| OBJECT_VERSION_NUMBER | InputValuePEOObjectVersionNumber | — |
| RESERVED_INPUT_VALUE | InputValuePEOReservedInputValue | ✅ |
| RETRO_STATIC_FLAG | InputValuePEORetroStaticFlag | — |
| UOM | InputValuePEOUom | ✅ |
| USER_DISPLAY_FLAG | InputValuePEOUserDisplayFlag | ✅ |
| USER_ENTERABLE_FLAG | InputValuePEOUserEnterableFlag | — |
| VALIDATION_OVERRIDE_MESSAGE | InputValuePEOValidationOverrideMessage | — |
| VO_NAME | InputValuePEOVoName | ✅ |
| WARNING_OR_ERROR | InputValuePEOWarningOrError | — |

---

## 📚 Referências

- [Oracle Docs — PAY_INPUT_VALUES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payinputvaluesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
