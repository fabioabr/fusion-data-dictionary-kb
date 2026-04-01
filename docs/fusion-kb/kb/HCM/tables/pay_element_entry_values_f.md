---
id: DOC-HCM-572
doc_type: system-doc
title: "PAY_ELEMENT_ENTRY_VALUES_F — Valores de Entradas de Elementos"
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
  - entry-values
  - valores
  - pay-entry-values
aliases:
  - PAY_ELEMENT_ENTRY_VALUES_F
  - pay_element_entry_values_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ELEMENT_ENTRY_VALUES_F

## 📌 Visão Geral

Armazena os **valores** de cada input value de uma entrada de elemento. Cada registro contem um valor especifico (ex.: valor monetario, quantidade de horas, percentual) associado a um input value de um element entry.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Armazenamento dos valores efetivos de cada entrada
- Detalhamento de valores por input value (montante, horas, percentual)
- Historico temporal de alteracoes de valores

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ELEMENT_ENTRY_VALUE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do valor | --- | 🟢 95% |
| 2 | ELEMENT_ENTRY_ID | NUMBER(18) | NOT NULL | FK | ID da entrada de elemento | PAY_ELEMENT_ENTRIES_F | 🟢 95% |
| 3 | INPUT_VALUE_ID | NUMBER(18) | NOT NULL | FK | ID do input value | PAY_INPUT_VALUES_F | 🟢 90% |
| 4 | SCREEN_ENTRY_VALUE | VARCHAR2(60) | NULL | Dados | Valor informado (como string) | --- | 🟢 85% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_element_entries_f]] --- via `ELEMENT_ENTRY_ID` (entrada de elemento à qual pertence o valor)
- [[pay_input_values_f]] --- via `INPUT_VALUE_ID` (definição do valor de entrada do elemento)

### Tabelas-filha (FK de saída)
- --- Tabela de valores, nivel mais granular

---

## 📎 Uso Típico

### Valores vigentes de uma entrada de elemento
```sql
SELECT eev.INPUT_VALUE_ID, eev.SCREEN_ENTRY_VALUE
FROM   PAY_ELEMENT_ENTRY_VALUES_F eev
WHERE  eev.ELEMENT_ENTRY_ID = :p_entry_id
  AND  SYSDATE BETWEEN eev.EFFECTIVE_START_DATE AND eev.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- O campo `SCREEN_ENTRY_VALUE` armazena o valor como string; tipo efetivo depende do `INPUT_VALUE_ID`.

---

## 🔗 PVOs Relacionados

### [[elemententryvalue|ElementEntryValue]] (HCM · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ElementEntryValueDPEOCreatedBy | ✅ |
| CREATION_DATE | ElementEntryValueDPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ELEMENT_ENTRY_ID | ElementEntryValueDPEOElementEntryId | ✅ |
| ELEMENT_ENTRY_VALUE_ID | ElementEntryValueId | ✅ |
| ENTRY_USAGE_ID | ElementEntryValueDPEOEntryUsageId | ✅ |
| INPUT_VALUE_ID | ElementEntryValueDPEOInputValueId | ✅ |
| LAST_UPDATE_DATE | ElementEntryValueDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ElementEntryValueDPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ElementEntryValueDPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ElementEntryValueDPEOObjectVersionNumber | ✅ |
| SCREEN_ENTRY_VALUE | ElementEntryValueDPEOScreenEntryValue | ✅ |

### [[elemententryvaluepvo|ElementEntryValuePVO]] (HCM · BICC: 5/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ElementEntryValuePEOCreatedBy | — |
| CREATION_DATE | ElementEntryValuePEOCreationDate | — |
| EFFECTIVE_END_DATE | ElementEntryValuePEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | ElementEntryValuePEOEffectiveStartDate | ✅ |
| ELEMENT_ENTRY_ID | ElementEntryValuePEOElementEntryId | — |
| ELEMENT_ENTRY_VALUE_ID | ElementEntryValueId | ✅ |
| ENTERPRISE_ID | EnterpriseId | — |
| ENTRY_USAGE_ID | ElementEntryValuePEOEntryUsageId | — |
| INPUT_VALUE_ID | ElementEntryValuePEOInputValueId | — |
| LAST_UPDATE_DATE | ElementEntryValuePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ElementEntryValuePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ElementEntryValuePEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ElementEntryValuePEOObjectVersionNumber | — |
| SCREEN_ENTRY_VALUE | ElementEntryValuePEOScreenEntryValue | ✅ |

### [[retroelemententry|RetroElementEntry]] (HCM · BICC: 5/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ElementEntryValueCreatedBy | — |
| CREATION_DATE | ElementEntryValueCreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ELEMENT_ENTRY_ID | ElementEntryValueElementEntryId | — |
| ELEMENT_ENTRY_VALUE_ID | ElementEntryValueId | ✅ |
| ENTRY_USAGE_ID | ElementEntryValueEntryUsageId | — |
| INPUT_VALUE_ID | ElementEntryValueInputValueId | — |
| LAST_UPDATE_DATE | ElementEntryValueLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ElementEntryValueLastUpdateLogin | — |
| LAST_UPDATED_BY | ElementEntryValueLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ElementEntryValueObjectVersionNumber | — |
| SCREEN_ENTRY_VALUE | ElementEntryValueScreenEntryValue | ✅ |

---

## 📚 Referências

- [Oracle Docs — PAY_ELEMENT_ENTRY_VALUES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payelemententryvaluesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
