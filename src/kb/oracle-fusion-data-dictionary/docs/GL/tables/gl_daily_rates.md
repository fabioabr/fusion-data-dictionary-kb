---
id: DOC-GL-010
doc_type: system-doc
title: "GL_DAILY_RATES — Taxas de Câmbio Diárias"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - general-ledger
  - data-dictionary
  - cambio
  - taxas
  - moeda
  - fx-rates
aliases:
  - GL_DAILY_RATES
  - gl_daily_rates
  - taxas-cambio-diarias
  - daily-rates-gl
  - fx-rates
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_DAILY_RATES

## Visao Geral

Armazena as **taxas de câmbio diárias** entre pares de moedas no General Ledger. Cada registro contém a taxa de conversão de uma moeda de origem para uma moeda de destino em uma data específica, vinculada a um tipo de conversão. É a tabela central de cotação cambial utilizada por todos os módulos financeiros do Oracle Fusion.

> [!note] Alta volumetria
> Esta tabela cresce diariamente com uma linha para cada combinação de par de moedas × tipo de conversão × data. Em ambientes com múltiplas moedas, o volume pode ser significativo. O Oracle armazena taxas nos dois sentidos (FROM→TO e TO→FROM).

---

## Proposito de Negocio

Esta tabela é utilizada nos seguintes processos:

- **Conversão de transações:** Fornece a taxa para converter valores de moeda estrangeira para moeda funcional.
- **Lançamentos contábeis:** GL utiliza a taxa da data do lançamento para calcular o valor na moeda funcional.
- **Contas a pagar (AP):** Conversão de faturas em moeda estrangeira no momento do pagamento.
- **Contas a receber (AR):** Conversão de recebimentos em moeda estrangeira.
- **Revalorização cambial:** Base para reavaliação de saldos em moeda estrangeira ao final do período.
- **Relatórios multi-moeda:** Conversão de valores para moeda de reporte.
- **Integração com provedores de taxa:** Taxas podem ser carregadas via API/interface do mercado (BACEN, ECB, etc.).

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | FROM_CURRENCY | VARCHAR2(15) | NOT NULL | PK | Código da moeda de origem (ex: USD) | [[fnd_currencies]] | 🟢 95% |
| 2 | TO_CURRENCY | VARCHAR2(15) | NOT NULL | PK | Código da moeda de destino (ex: BRL) | [[fnd_currencies]] | 🟢 95% |
| 3 | CONVERSION_DATE | DATE | NOT NULL | PK | Data da taxa de conversão | — | 🟢 95% |
| 4 | CONVERSION_TYPE | VARCHAR2(30) | NOT NULL | PK | Tipo de conversão (ex: Spot, Corporate) | [[gl_daily_conversion_types]] | 🟢 95% |
| 5 | CONVERSION_RATE | NUMBER | NOT NULL | Financeiro | Taxa de conversão (FROM → TO) | — | 🟢 95% |
| 6 | STATUS_CODE | VARCHAR2(1) | NULL | Controle | Status da taxa: I (informada), D (derivada), O (inversa) | — | 🟡 75% |
| 7 | ATTRIBUTE1–5 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis | — | 🟡 70% |
| 8 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟡 70% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Sistema | Controle de versionamento otimista (locking) | — | 🟢 90% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 14 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_daily_conversion_types]] — via `CONVERSION_TYPE` (tipo de conversão)
- [[fnd_currencies]] — via `FROM_CURRENCY` e `TO_CURRENCY` (moeda de origem da taxa de câmbio diária)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela de referência consultada por todo o ERP.

---

## Uso Tipico

### Taxa de câmbio USD→BRL em uma data
```sql
SELECT dr.CONVERSION_RATE, dr.CONVERSION_TYPE, dr.CONVERSION_DATE
FROM   GL_DAILY_RATES dr
WHERE  dr.FROM_CURRENCY = 'USD'
  AND  dr.TO_CURRENCY = 'BRL'
  AND  dr.CONVERSION_DATE = DATE '2026-03-25'
  AND  dr.CONVERSION_TYPE = 'Corporate';
```

### Histórico de taxas por período
```sql
SELECT dr.CONVERSION_DATE, dr.CONVERSION_RATE
FROM   GL_DAILY_RATES dr
WHERE  dr.FROM_CURRENCY = 'USD'
  AND  dr.TO_CURRENCY = 'BRL'
  AND  dr.CONVERSION_TYPE = 'Spot'
  AND  dr.CONVERSION_DATE BETWEEN DATE '2026-01-01' AND DATE '2026-03-31'
ORDER BY dr.CONVERSION_DATE;
```

### Verificar taxas faltantes
```sql
SELECT cal.CONVERSION_DATE
FROM   (SELECT DATE '2026-03-01' + LEVEL - 1 AS CONVERSION_DATE
        FROM   DUAL
        CONNECT BY LEVEL <= 31) cal
WHERE  NOT EXISTS (
    SELECT 1 FROM GL_DAILY_RATES dr
    WHERE  dr.FROM_CURRENCY = 'USD'
      AND  dr.TO_CURRENCY = 'BRL'
      AND  dr.CONVERSION_TYPE = 'Corporate'
      AND  dr.CONVERSION_DATE = cal.CONVERSION_DATE
);
```

### Filtros comuns
- `CONVERSION_TYPE = 'Corporate'` — Taxa corporativa
- `CONVERSION_TYPE = 'Spot'` — Taxa de mercado
- `FROM_CURRENCY = 'USD' AND TO_CURRENCY = 'BRL'` — Par dólar/real

---

## Observacoes

- A chave primária é composta por `FROM_CURRENCY` + `TO_CURRENCY` + `CONVERSION_DATE` + `CONVERSION_TYPE`.
- O Oracle armazena taxas nos **dois sentidos** (USD→BRL e BRL→USD) — a taxa inversa é calculada automaticamente (1/taxa).
- Se não houver taxa para uma data específica, o sistema pode retornar erro em transações multi-moeda. É essencial manter as taxas carregadas para todos os dias úteis.
- O `CONVERSION_RATE` é multiplicativo: valor_origem × taxa = valor_destino.
- Para ambientes brasileiros, recomenda-se criar um tipo de conversão "BACEN" e carregar a PTAX diariamente.
- Taxas podem ser carregadas manualmente, via arquivo de importação ou via integração com provedores de dados de mercado.

---

## Referencias

- [Oracle Docs — GL_DAILY_RATES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/gldailyrates-25082.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
