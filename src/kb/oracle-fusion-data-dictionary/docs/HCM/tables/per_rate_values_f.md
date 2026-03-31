---
id: DOC-HCM-705
doc_type: system-doc
title: "PER_RATE_VALUES_F — Valores de Taxas"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - valores-taxas
  - rate-values
  - remuneracao
  - salario
aliases:
  - PER_RATE_VALUES_F
  - per_rate_values_f
  - valores-taxas
  - rate-values-hcm
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_RATE_VALUES_F

## Visão Geral

Armazena os **valores efetivos** das taxas definidas em `PER_RATES_F`. Contém os valores numéricos (mínimo, máximo, midpoint) para cada taxa, associados a atribuições ou grades. Tabela date-effective.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Faixas salariais** — definir valores mínimo, máximo e midpoint por grade
- **Cálculos de compensação** — valores-base para processamento de folha
- **Planejamento salarial** — referência para propostas de aumento
- **Compliance trabalhista** — validar que salários estão dentro das faixas
- **Benchmarking** — comparar valores de mercado com valores internos

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RATE_VALUE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do valor | — | 🟢 90% |
| 2 | RATE_ID | NUMBER(18) | NOT NULL | FK | Referência à definição de taxa | PER_RATES_F | 🟢 90% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Vínculo/atribuição associada | PER_ALL_ASSIGNMENTS_M | 🟡 75% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 6 | MINIMUM | NUMBER | NULL | Valor | Valor mínimo da faixa | — | 🟡 80% |
| 7 | MAXIMUM | NUMBER | NULL | Valor | Valor máximo da faixa | — | 🟡 80% |
| 8 | MID_VALUE | NUMBER | NULL | Valor | Valor do midpoint da faixa | — | 🟡 75% |
| 9 | VALUE | NUMBER | NULL | Valor | Valor efetivo/atribuído | — | 🟡 80% |
| 10 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda do valor | — | 🟡 75% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 15 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_rates_f]] — via `RATE_ID` (taxa salarial do valor)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vínculo ao qual o valor de taxa se aplica)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Valor atual de uma taxa para uma atribuição
```sql
SELECT rv.VALUE, rv.MINIMUM, rv.MAXIMUM, rv.CURRENCY_CODE
FROM   PER_RATE_VALUES_F rv
WHERE  rv.ASSIGNMENT_ID = :p_assignment_id
  AND  rv.RATE_ID = :p_rate_id
  AND  SYSDATE BETWEEN rv.EFFECTIVE_START_DATE AND rv.EFFECTIVE_END_DATE;
```

---

## Observações

- Tabela date-effective: sempre filtrar por vigência.
- `VALUE` contém o valor efetivo; `MINIMUM`, `MAXIMUM` e `MID_VALUE` definem a faixa.
- Contém dados sensíveis de remuneração — acesso deve ser restrito.
- Pode conter valores em diferentes moedas — verificar `CURRENCY_CODE`.

---

## Referências

- [Oracle Docs — PER_RATE_VALUES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perratevaluesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[ratevaluepvo|RateValuePVO]] (GL · BICC: 17/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | RateValuePEOActionOccurrenceId | ✅ |
| CREATED_BY | RateValuePEOCreatedBy | ✅ |
| CREATION_DATE | RateValuePEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | RateValuePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RateValuePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RateValuePEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | RateValuePEOLegislationCode | ✅ |
| MAXIMUM | RateValuePEOMaximum | ✅ |
| MID_VALUE | RateValuePEOMidValue | ✅ |
| MINIMUM | RateValuePEOMinimum | ✅ |
| OBJECT_VERSION_NUMBER | RateValuePEOObjectVersionNumber | — |
| RATE_ID | RateValuePEORateId | ✅ |
| RATE_OBJECT_ID | RateValuePEORateObjectId | ✅ |
| RATE_OBJECT_TYPE | RateValuePEORateObjectType | ✅ |
| RATE_VALUE_ID | RateValueId | ✅ |
| SEQUENCE | RateValuePEOSequence | ✅ |
| VALUE | RateValuePEOValue | ✅ |
