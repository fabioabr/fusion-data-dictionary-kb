---
id: DOC-HCM-079
doc_type: system-doc
title: "CMP_CWB_XCHG — Taxas de Câmbio do Compensation Workbench"
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
  - compensation
  - cwb
  - cambio
  - exchange-rate
aliases:
  - CMP_CWB_XCHG
  - cmp_cwb_xchg
  - cmp-cwb-xchg
  - DOC-HCM-079
  - taxas-de-câmbio-do-compensation-workbench
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_CWB_XCHG

## 📌 Visão Geral

Armazena as **taxas de câmbio** utilizadas nos cálculos do Compensation Workbench para conversão de moedas em planos de compensação multinacionais. Cada registro define a taxa de conversão entre duas moedas em uma data específica do plano.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Conversão de moedas:** Taxas de câmbio para planos CWB internacionais.
- **Padronização de valores:** Conversão de salários locais para moeda de referência.
- **Orçamento consolidado:** Permite consolidação de orçamentos em uma moeda única.
- **Relatórios globais:** Base para relatórios de compensação multi-moeda.
- **Auditoria financeira:** Rastreamento das taxas utilizadas nas decisões.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | XCHG_ID | NUMBER(18) | NOT NULL | PK | Identificador único da taxa de câmbio | — | 🟡 80% |
| 2 | PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano CWB associado | [[cmp_cwb_plan_definitions]] | 🟢 90% |
| 3 | FROM_CURRENCY_CODE | VARCHAR2(30) | NOT NULL | Referência | Moeda de origem | — | 🟡 80% |
| 4 | TO_CURRENCY_CODE | VARCHAR2(30) | NOT NULL | Referência | Moeda de destino | — | 🟡 80% |
| 5 | EXCHANGE_RATE | NUMBER | NOT NULL | Financeiro | Taxa de conversão | — | 🟡 80% |
| 6 | EXCHANGE_DATE | DATE | NULL | Data | Data da taxa de câmbio | — | 🟡 75% |
| 7 | CONVERSION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de conversão (SPOT, CORPORATE) | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[cmp_cwb_plan_definitions]] — via `PLAN_ID` (plano CWB da taxa de cambio)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Taxas de câmbio por plano
```sql
SELECT x.FROM_CURRENCY_CODE, x.TO_CURRENCY_CODE,
       x.EXCHANGE_RATE, x.EXCHANGE_DATE
FROM   CMP_CWB_XCHG x
WHERE  x.PLAN_ID = :p_plan_id;
```

### Taxa de câmbio para moeda específica
```sql
SELECT x.EXCHANGE_RATE, x.EXCHANGE_DATE
FROM   CMP_CWB_XCHG x
WHERE  x.PLAN_ID = :p_plan_id
  AND  x.FROM_CURRENCY_CODE = 'BRL'
  AND  x.TO_CURRENCY_CODE = 'USD';
```

---

## 🔒 Observações

- As taxas de câmbio são específicas por plano CWB — não compartilhadas entre planos.
- O `CONVERSION_TYPE` pode ser SPOT (mercado), CORPORATE (taxa interna) ou outro tipo definido.
- Utilizada internamente pelo Compensation Workbench para normalizar valores de diferentes moedas.
- Para planos locais (single-currency), esta tabela pode não conter registros.

---

## 🔗 PVOs Relacionados

### [[personratespvo|PersonRatesPVO]] (HCM · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY | ExchangeRatePEOCurrency | ✅ |
| PERIOD_ID | ExchangeRatePEOPeriodId | ✅ |
| PLAN_ID | ExchangeRatePEOPlanId | ✅ |
| XCHG_RATE | ExchangeRatePEOXchgRate | ✅ |

### [[personratespvoviewall|PersonRatesPVOViewAll]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY | ExchangeRatePEOCurrency | ✅ |
| PERIOD_ID | ExchangeRatePEOPeriodId | — |
| PLAN_ID | ExchangeRatePEOPlanId | — |
| XCHG_RATE | ExchangeRatePEOXchgRate | — |

---

## 📚 Referências

- [Oracle Docs — CMP_CWB_XCHG](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpcwbxchg.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
