---
id: DOC-GL-017
doc_type: system-doc
title: "GL_FISCAL_YEAR_V — View de Anos Fiscais"
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
  - anos-fiscais
  - fiscal-calendar
aliases:
  - GL_FISCAL_YEAR_V
  - gl_fiscal_year_v
  - anos-fiscais-gl
  - fiscal-year-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_FISCAL_YEAR_V

## 📌 Visão Geral

View que expõe os **anos fiscais** do calendário contábil, consolidando as datas de início e fim de cada exercício fiscal, a quantidade de períodos e trimestres. Fornece a visão de mais alto nível da hierarquia temporal fiscal, utilizada para relatórios anuais e comparações year-over-year (YoY).

> [!note] Sufixo _V
> O sufixo `_V` indica uma **view** derivada de tabelas base do calendário fiscal.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Demonstrativos anuais:** Balanço patrimonial, DRE anual e demais demonstrativos de exercício.
- **Comparação YoY:** Análise de variação de receitas e despesas entre exercícios fiscais.
- **Planejamento orçamentário:** Definição de horizonte temporal para budget anual.
- **Fechamento contábil:** Identificação das datas de início e fim do exercício fiscal para processos de encerramento.
- **ETL e Data Warehouse:** Dimensão de ano fiscal para cubos analíticos.

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
| 3 | PERIOD_YEAR | NUMBER(15) | NOT NULL | PK | Ano fiscal | — | 🟡 80% |
| 4 | YEAR_START_DATE | DATE | NOT NULL | Período | Data de início do ano fiscal | — | 🟡 75% |
| 5 | YEAR_END_DATE | DATE | NOT NULL | Período | Data de fim do ano fiscal | — | 🟡 75% |
| 6 | NUM_QUARTERS | NUMBER | NULL | Período | Quantidade de trimestres no ano fiscal | — | 🟡 65% |
| 7 | NUM_PERIODS | NUMBER | NULL | Período | Quantidade de períodos (meses) no ano fiscal | — | 🟡 65% |
| 8 | NUM_DAYS | NUMBER | NULL | Período | Quantidade de dias no ano fiscal | — | 🟡 65% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_period_sets]] — via `PERIOD_SET_NAME` (definição do calendário fiscal)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma view de consulta (dimensão temporal).

---

## 📎 Uso Típico

### Listar anos fiscais disponíveis
```sql
SELECT fy.PERIOD_YEAR,
       fy.YEAR_START_DATE,
       fy.YEAR_END_DATE,
       fy.NUM_PERIODS,
       fy.NUM_QUARTERS
FROM   GL_FISCAL_YEAR_V fy
WHERE  fy.PERIOD_SET_NAME = :p_calendar_name
  AND  fy.PERIOD_TYPE = 'Month'
ORDER BY fy.PERIOD_YEAR;
```

### Comparação YoY de saldos
```sql
SELECT b.PERIOD_YEAR,
       SUM(b.PERIOD_NET_DR - b.PERIOD_NET_CR) AS movimento_anual
FROM   GL_BALANCES b
WHERE  b.LEDGER_ID = :p_ledger_id
  AND  b.ACTUAL_FLAG = 'A'
  AND  b.CODE_COMBINATION_ID = :p_ccid
  AND  b.CURRENCY_CODE = 'BRL'
GROUP BY b.PERIOD_YEAR
ORDER BY b.PERIOD_YEAR;
```

### Filtros comuns
- `PERIOD_SET_NAME = 'Accounting'` — Calendário contábil principal
- `PERIOD_YEAR = 2026` — Ano fiscal específico
- `PERIOD_TYPE = 'Month'` — Período mensal (padrão)

---

## 🔒 Observações

- Esta é uma **view**, não uma tabela física. Os dados derivam das configurações de calendário fiscal do GL.
- A granularidade é **por ano fiscal**, o nível mais alto da hierarquia temporal.
- O ano fiscal pode não coincidir com o ano calendário — depende da configuração (ex: exercício abril/março).
- `NUM_PERIODS` pode ser maior que 12 se houver períodos de ajuste configurados.
- Complementa a hierarquia: `GL_FISCAL_DAY_V` → `GL_FISCAL_PERIOD_V` → `GL_FISCAL_QUARTER_V` → `GL_FISCAL_YEAR_V`.

---

## 🔗 PVOs Relacionados

### [[fiscalperiodwithoutledgerpvo|FiscalPeriodWithoutLedgerPVO]] (GL · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| FISCAL_PERIOD_SET_ID | FiscalYearFiscalPeriodSetId | — |
| FISCAL_PERIOD_SET_NAME | FiscalYearFiscalPeriodSetName | — |
| FISCAL_PERIOD_TYPE | FiscalYearFiscalPeriodType | — |
| FISCAL_YEAR_END_DATE | FiscalYearFiscalYearEndDate | ✅ |
| FISCAL_YEAR_NUMBER | FiscalYearFiscalYearNumber | — |
| FISCAL_YEAR_START_DATE | FiscalYearFiscalYearStartDate | ✅ |

### [[glfiscalperiodpvo|GLFiscalPeriodPVO]] (GL · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| FISCAL_PERIOD_SET_ID | FiscalYearFiscalPeriodSetId | — |
| FISCAL_PERIOD_SET_NAME | FiscalYearFiscalPeriodSetName | — |
| FISCAL_PERIOD_TYPE | FiscalYearFiscalPeriodType | — |
| FISCAL_YEAR_END_DATE | FiscalYearFiscalYearEndDate | ✅ |
| FISCAL_YEAR_NUMBER | FiscalYearFiscalYearNumber | — |
| FISCAL_YEAR_START_DATE | FiscalYearFiscalYearStartDate | ✅ |

### [[glfiscalqtrpvo|GLFiscalQtrPVO]] (GL · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| FISCAL_PERIOD_SET_ID | FiscalYearFiscalPeriodSetId | — |
| FISCAL_PERIOD_SET_NAME | FiscalYearFiscalPeriodSetName | — |
| FISCAL_PERIOD_TYPE | FiscalYearFiscalPeriodType | — |
| FISCAL_YEAR_END_DATE | FiscalYearFiscalYearEndDate | ✅ |
| FISCAL_YEAR_NUMBER | FiscalYearFiscalYearNumber | — |
| FISCAL_YEAR_START_DATE | FiscalYearFiscalYearStartDate | ✅ |

### [[glfiscalyearpvo|GLFiscalYearPVO]] (GL · BICC: 6/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| FISCAL_PERIOD_SET_ID | FiscalPeriodSetId | ✅ |
| FISCAL_PERIOD_SET_NAME | FiscalPeriodSetName | ✅ |
| FISCAL_PERIOD_TYPE | FiscalPeriodType | ✅ |
| FISCAL_YEAR_END_DATE | FiscalYearEndDate | ✅ |
| FISCAL_YEAR_NUMBER | FiscalYearNumber | ✅ |
| FISCAL_YEAR_START_DATE | FiscalYearStartDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — GL Fiscal Calendar Views](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glperiodstatuses-25740.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
