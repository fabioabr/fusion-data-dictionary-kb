---
id: DOC-HCM-703
doc_type: system-doc
title: "PER_RATES_F — Definição de Taxas/Valores"
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
  - taxas
  - rates
  - remuneracao
  - valores
aliases:
  - PER_RATES_F
  - per_rates_f
  - definicao-taxas
  - rates-hcm
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_RATES_F

## Visão Geral

Armazena as **definições de taxas/valores** (rates) utilizadas no módulo HCM. Define tipos de taxa como salários, horas extras, adicionais, subsídios, entre outros, com vigência temporal.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de tipos de remuneração** — cadastrar taxas e valores disponíveis
- **Tabelas salariais** — base para definição de faixas e grades salariais
- **Cálculos de folha** — referência para cálculos de horas extras, adicionais
- **Planejamento de compensação** — tipos de taxa utilizados em planos
- **Benchmarking salarial** — categorização de componentes de remuneração

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RATE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da taxa | — | 🟢 90% |
| 2 | RATE_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo da taxa (SALARY, ALLOWANCE, etc.) | — | 🟢 85% |
| 3 | RATE_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código da taxa | — | 🟡 80% |
| 4 | LEGISLATION_CODE | VARCHAR2(4) | NULL | Classificação | Código do país/legislação | — | 🟡 75% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 7 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda da taxa (BRL, USD, etc.) | — | 🟡 75% |
| 8 | UOM | VARCHAR2(30) | NULL | Configuração | Unidade de medida (HOURLY, MONTHLY, ANNUAL) | — | 🟡 75% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma — tabela de configuração/referência.

### Tabelas-filha (FK de saída)
- [[per_rates_f_tl]] — via `RATE_ID` (traduções da taxa salarial)
- [[per_rate_values_f]] — via `RATE_ID` (valores atribuídos à taxa salarial)

---

## Uso Típico

### Listar taxas ativas do tipo salário
```sql
SELECT r.RATE_ID, r.RATE_CODE, r.CURRENCY_CODE, r.UOM
FROM   PER_RATES_F r
WHERE  r.RATE_TYPE = 'SALARY'
  AND  SYSDATE BETWEEN r.EFFECTIVE_START_DATE AND r.EFFECTIVE_END_DATE;
```

---

## Observações

- Tabela date-effective: sempre filtrar por vigência.
- Define tipos de taxa — os valores efetivos estão em `PER_RATE_VALUES_F`.
- Nomes descritivos estão na tabela de tradução `PER_RATES_F_TL`.
- `UOM` define a periodicidade: HOURLY (hora), MONTHLY (mês), ANNUAL (ano).

---

## Referências

- [Oracle Docs — PER_RATES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perratesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[gradeladderpvo|GradeLadderPVO]] (GL · BICC: 3/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | SalaryUpdateRatePEOActionOccurrenceId | — |
| ACTIVE_STATUS | SalaryUpdateRatePEOActiveStatus | — |
| ANNUALIZATION_FACTOR | SalaryUpdateRatePEOAnnualizationFactor | ✅ |
| BUSINESS_GROUP_ID | SalaryUpdateRatePEOBusinessGroupId | — |
| CURRENCY_CODE | SalaryUpdateRatePEOCurrencyCode | ✅ |
| EFFECTIVE_END_DATE | SalaryUpdateRatePEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | SalaryUpdateRatePEOEffectiveStartDate | — |
| GRADE_LADDER_ID | SalaryUpdateRatePEOGradeLadderId | — |
| LEGISLATION_CODE | SalaryUpdateRatePEOLegislationCode | — |
| LEGISLATIVE_DATA_GROUP_ID | SalaryUpdateRatePEOLegislativeDataGroupId | — |
| PROGRESSION_RATE_FLAG | SalaryUpdateRatePEOProgressionRateFlag | — |
| RATE_FREQUENCY | SalaryUpdateRatePEORateFrequency | ✅ |
| RATE_ID | SalaryUpdateRatePEORateId | — |
| RATE_OBJECT_TYPE | SalaryUpdateRatePEORateObjectType | — |
| RATE_TYPE | SalaryUpdateRatePEORateType | — |
| RATE_UOM | SalaryUpdateRatePEORateUom | — |

### [[ratepvo|RatePVO]] (GL · BICC: 21/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | RatePEOActionOccurrenceId | ✅ |
| ACTIVE_STATUS | RatePEOActiveStatus | ✅ |
| ANNUALIZATION_FACTOR | RatePEOAnnualizationFactor | ✅ |
| CREATED_BY | RatePEOCreatedBy | ✅ |
| CREATION_DATE | RatePEOCreationDate | ✅ |
| CURRENCY_CODE | RatePEOCurrencyCode | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| GRADE_LADDER_ID | RatePEOGradeLadderId | ✅ |
| LAST_UPDATE_DATE | RatePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RatePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RatePEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | RatePEOLegislationCode | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | RatePEOLegislativeDataGroupId | ✅ |
| OBJECT_VERSION_NUMBER | RatePEOObjectVersionNumber | ✅ |
| PAY_SCALE_ID | RatePEOPayScaleId | ✅ |
| PROGRESSION_RATE_FLAG | RatePEOProgressionRateFlag | ✅ |
| RATE_FREQUENCY | RatePEORateFrequency | ✅ |
| RATE_ID | RateId | ✅ |
| RATE_OBJECT_TYPE | RatePEORateObjectType | ✅ |
| RATE_TYPE | RatePEORateType | ✅ |
| RATE_UOM | RatePEORateUom | ✅ |
