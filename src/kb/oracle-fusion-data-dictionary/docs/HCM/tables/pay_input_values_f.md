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

## 📚 Referências

- [Oracle Docs — PAY_INPUT_VALUES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payinputvaluesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
