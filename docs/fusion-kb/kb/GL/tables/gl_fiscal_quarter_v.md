---
id: DOC-GL-016
doc_type: system-doc
title: "GL_FISCAL_QUARTER_V — View de Trimestres Fiscais"
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
  - calendario-fiscal
  - trimestres-fiscais
  - fiscal-calendar
aliases:
  - GL_FISCAL_QUARTER_V
  - gl_fiscal_quarter_v
  - trimestres-fiscais-gl
  - fiscal-quarter-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_FISCAL_QUARTER_V

## 📌 Visão Geral

View que expõe os **trimestres fiscais** do calendário contábil, consolidando as datas de início e fim de cada trimestre, o ano fiscal e a quantidade de períodos contidos. Facilita consultas analíticas e relatórios com granularidade trimestral sem necessidade de agregar manualmente os períodos mensais.

> [!note] Sufixo _V
> O sufixo `_V` indica uma **view** derivada de tabelas base do calendário fiscal.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Relatórios trimestrais:** ITR (Informações Trimestrais) e demonstrativos financeiros trimestrais.
- **Análise de performance:** Comparação quarter-over-quarter (QoQ) de receitas, despesas e margens.
- **Budget e Forecast:** Agrupamento de orçamento por trimestre fiscal.
- **Dashboards executivos:** Indicadores consolidados por trimestre.
- **ETL e Data Warehouse:** Dimensão de trimestre fiscal para cubos analíticos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERIOD_SET_NAME | VARCHAR2(15) | NOT NULL | FK | Nome do conjunto de períodos (calendário fiscal) | [[gl_period_sets]] | 🟡 75% |
| 2 | PERIOD_TYPE | VARCHAR2(15) | NOT NULL | Classificação | Tipo do período (ex: Month) | — | 🟡 75% |
| 3 | PERIOD_YEAR | NUMBER(15) | NOT NULL | Período | Ano fiscal | — | 🟡 80% |
| 4 | QUARTER_NUM | NUMBER(15) | NOT NULL | PK | Número do trimestre fiscal (1–4) | — | 🟡 80% |
| 5 | QUARTER_START_DATE | DATE | NOT NULL | Período | Data de início do trimestre fiscal | — | 🟡 75% |
| 6 | QUARTER_END_DATE | DATE | NOT NULL | Período | Data de fim do trimestre fiscal | — | 🟡 75% |
| 7 | NUM_PERIODS | NUMBER | NULL | Período | Quantidade de períodos (meses) no trimestre | — | 🟡 65% |
| 8 | NUM_DAYS | NUMBER | NULL | Período | Quantidade de dias no trimestre | — | 🟡 65% |
| 9 | YEAR_START_DATE | DATE | NULL | Período | Data de início do ano fiscal | — | 🟡 65% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_period_sets]] — via `PERIOD_SET_NAME` (definição do calendário fiscal)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma view de consulta (dimensão temporal).

---

## 📎 Uso Típico

### Listar trimestres de um ano fiscal
```sql
SELECT fq.QUARTER_NUM,
       fq.QUARTER_START_DATE,
       fq.QUARTER_END_DATE,
       fq.NUM_PERIODS
FROM   GL_FISCAL_QUARTER_V fq
WHERE  fq.PERIOD_SET_NAME = :p_calendar_name
  AND  fq.PERIOD_TYPE = 'Month'
  AND  fq.PERIOD_YEAR = 2026
ORDER BY fq.QUARTER_NUM;
```

### Saldos acumulados por trimestre fiscal
```sql
SELECT fq.QUARTER_NUM,
       SUM(b.PERIOD_NET_DR - b.PERIOD_NET_CR) AS movimento_trimestre
FROM   GL_BALANCES b
JOIN   GL_FISCAL_PERIOD_V fp
  ON   fp.PERIOD_NAME = b.PERIOD_NAME
  AND  fp.PERIOD_SET_NAME = :p_calendar_name
JOIN   GL_FISCAL_QUARTER_V fq
  ON   fq.PERIOD_SET_NAME = fp.PERIOD_SET_NAME
  AND  fq.PERIOD_YEAR = fp.PERIOD_YEAR
  AND  fq.QUARTER_NUM = fp.QUARTER_NUM
WHERE  b.LEDGER_ID = :p_ledger_id
  AND  b.ACTUAL_FLAG = 'A'
  AND  fq.PERIOD_YEAR = 2026
GROUP BY fq.QUARTER_NUM
ORDER BY fq.QUARTER_NUM;
```

### Filtros comuns
- `PERIOD_SET_NAME = 'Accounting'` — Calendário contábil principal
- `PERIOD_YEAR = 2026` — Ano fiscal específico
- `QUARTER_NUM = 1` — Primeiro trimestre

---

## 🔒 Observações

- Esta é uma **view**, não uma tabela física. Os dados derivam das configurações de calendário fiscal do GL.
- A granularidade é **por trimestre**, diferente de `GL_FISCAL_PERIOD_V` (mensal) e `GL_FISCAL_DAY_V` (diária).
- Tipicamente retorna 4 linhas por ano fiscal, mas pode variar conforme configuração do calendário.
- Útil em conjunto com `GL_FISCAL_PERIOD_V` para construir hierarquias temporais (dia → período → trimestre → ano).
- A confiança geral é moderada (🟡) pois a documentação oficial Oracle para views fiscais derivadas é limitada.

---

## 🔗 PVOs Relacionados

### [[fiscalperiodwithoutledgerpvo|FiscalPeriodWithoutLedgerPVO]] (GL · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| FISCAL_PERIOD_SET_ID | FiscalQuarterFiscalPeriodSetId | — |
| FISCAL_PERIOD_SET_NAME | FiscalQuarterFiscalPeriodSetName | — |
| FISCAL_PERIOD_TYPE | FiscalQuarterFiscalPeriodType | — |
| FISCAL_QUARTER_END_DATE | FiscalQuarterFiscalQuarterEndDate | ✅ |
| FISCAL_QUARTER_NUMBER | FiscalQuarterFiscalQuarterNumber | — |
| FISCAL_QUARTER_START_DATE | FiscalQuarterFiscalQuarterStartDate | ✅ |
| FISCAL_YEAR_END_DATE | FiscalQuarterFiscalYearEndDate | — |
| FISCAL_YEAR_NUMBER | FiscalQuarterFiscalYearNumber | — |
| FISCAL_YEAR_START_DATE | FiscalQuarterFiscalYearStartDate | — |

### [[glfiscalperiodpvo|GLFiscalPeriodPVO]] (GL · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| FISCAL_PERIOD_SET_ID | FiscalQuarterFiscalPeriodSetId | — |
| FISCAL_PERIOD_SET_NAME | FiscalQuarterFiscalPeriodSetName | — |
| FISCAL_PERIOD_TYPE | FiscalQuarterFiscalPeriodType | — |
| FISCAL_QUARTER_END_DATE | FiscalQuarterFiscalQuarterEndDate | ✅ |
| FISCAL_QUARTER_NUMBER | FiscalQuarterFiscalQuarterNumber | — |
| FISCAL_QUARTER_START_DATE | FiscalQuarterFiscalQuarterStartDate | ✅ |
| FISCAL_YEAR_END_DATE | FiscalQuarterFiscalYearEndDate | — |
| FISCAL_YEAR_NUMBER | FiscalQuarterFiscalYearNumber | — |
| FISCAL_YEAR_START_DATE | FiscalQuarterFiscalYearStartDate | — |

### [[glfiscalqtrpvo|GLFiscalQtrPVO]] (GL · BICC: 7/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| FISCAL_PERIOD_SET_ID | FiscalPeriodSetId | ✅ |
| FISCAL_PERIOD_SET_NAME | FiscalPeriodSetName | ✅ |
| FISCAL_PERIOD_TYPE | FiscalPeriodType | ✅ |
| FISCAL_QUARTER_END_DATE | FiscalQuarterFiscalQuarterEndDate | ✅ |
| FISCAL_QUARTER_NUMBER | FiscalQuarterNumber | ✅ |
| FISCAL_QUARTER_START_DATE | FiscalQuarterFiscalQuarterStartDate | ✅ |
| FISCAL_YEAR_END_DATE | FiscalQuarterFiscalYearEndDate | — |
| FISCAL_YEAR_NUMBER | FiscalYearNumber | ✅ |
| FISCAL_YEAR_START_DATE | FiscalQuarterFiscalYearStartDate | — |

---

## 📚 Referências

- [Oracle Docs — GL Fiscal Calendar Views](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glperiodstatuses-25740.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
