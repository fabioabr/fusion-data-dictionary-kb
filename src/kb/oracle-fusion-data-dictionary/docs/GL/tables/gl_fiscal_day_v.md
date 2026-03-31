---
id: DOC-GL-014
doc_type: system-doc
title: "GL_FISCAL_DAY_V — View de Dias Fiscais"
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
  - dias-fiscais
  - fiscal-calendar
aliases:
  - GL_FISCAL_DAY_V
  - gl_fiscal_day_v
  - dias-fiscais-gl
  - fiscal-day-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_FISCAL_DAY_V

## 📌 Visão Geral

View que expõe os **dias fiscais** do calendário contábil, permitindo mapear cada data do calendário gregoriano para o período fiscal, trimestre e ano fiscal correspondentes. Derivada das definições de calendário fiscal configuradas no General Ledger, esta view é utilizada para consultas de temporalidade fiscal em relatórios e análises.

> [!note] Sufixo _V
> O sufixo `_V` indica uma **view** derivada de tabelas base do calendário fiscal (`GL_PERIOD_STATUSES`, `GL_PERIODS`, etc.).

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Mapeamento data → período:** Determinar a qual período, trimestre e ano fiscal um dia calendário pertence.
- **Relatórios diários:** Consultas de movimentação financeira com granularidade diária no contexto fiscal.
- **Dashboards:** Indicadores de performance por dia fiscal (day-over-day).
- **ETL e Data Warehouse:** Dimensão de tempo fiscal para cubos analíticos.
- **Validação de datas:** Verificar se uma data está dentro de um período fiscal aberto.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | FISCAL_DAY | DATE | NOT NULL | PK | Data do dia fiscal (calendário gregoriano) | — | 🟡 75% |
| 2 | PERIOD_SET_NAME | VARCHAR2(15) | NOT NULL | FK | Nome do conjunto de períodos (calendário fiscal) | [[gl_period_sets]] | 🟡 75% |
| 3 | PERIOD_TYPE | VARCHAR2(15) | NOT NULL | Classificação | Tipo do período (ex: Month) | — | 🟡 75% |
| 4 | PERIOD_NAME | VARCHAR2(15) | NOT NULL | Período | Nome do período fiscal (ex: JAN-26) | — | 🟡 75% |
| 5 | PERIOD_YEAR | NUMBER(15) | NOT NULL | Período | Ano fiscal | — | 🟡 75% |
| 6 | PERIOD_NUM | NUMBER(15) | NOT NULL | Período | Número sequencial do período no ano fiscal | — | 🟡 75% |
| 7 | QUARTER_NUM | NUMBER(15) | NOT NULL | Período | Número do trimestre fiscal (1–4) | — | 🟡 75% |
| 8 | DAY_OF_PERIOD | NUMBER | NULL | Período | Dia sequencial dentro do período fiscal | — | 🟡 65% |
| 9 | DAY_OF_QUARTER | NUMBER | NULL | Período | Dia sequencial dentro do trimestre fiscal | — | 🟡 65% |
| 10 | DAY_OF_YEAR | NUMBER | NULL | Período | Dia sequencial dentro do ano fiscal | — | 🟡 65% |
| 11 | PERIOD_START_DATE | DATE | NOT NULL | Período | Data de início do período fiscal | — | 🟡 75% |
| 12 | PERIOD_END_DATE | DATE | NOT NULL | Período | Data de fim do período fiscal | — | 🟡 75% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_period_sets]] — via `PERIOD_SET_NAME` (definição do calendário fiscal)
- [[gl_periods]] — via `PERIOD_SET_NAME` + `PERIOD_NAME` (definição do período)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma view de consulta (dimensão temporal).

---

## 📎 Uso Típico

### Descobrir o período fiscal de uma data
```sql
SELECT fd.PERIOD_NAME,
       fd.PERIOD_YEAR,
       fd.QUARTER_NUM,
       fd.PERIOD_NUM
FROM   GL_FISCAL_DAY_V fd
WHERE  fd.FISCAL_DAY = DATE '2026-03-15'
  AND  fd.PERIOD_SET_NAME = :p_calendar_name
  AND  fd.PERIOD_TYPE = 'Month';
```

### Dias úteis fiscais em um período
```sql
SELECT fd.PERIOD_NAME,
       COUNT(*) AS total_dias_fiscais
FROM   GL_FISCAL_DAY_V fd
WHERE  fd.PERIOD_SET_NAME = :p_calendar_name
  AND  fd.PERIOD_TYPE = 'Month'
  AND  fd.PERIOD_YEAR = 2026
GROUP BY fd.PERIOD_NAME
ORDER BY MIN(fd.PERIOD_NUM);
```

### Filtros comuns
- `PERIOD_SET_NAME = 'Accounting'` — Calendário contábil principal
- `PERIOD_TYPE = 'Month'` — Períodos mensais
- `FISCAL_DAY BETWEEN :start_date AND :end_date` — Intervalo de datas

---

## 🔒 Observações

- Esta é uma **view**, não uma tabela física. Os dados derivam das configurações de calendário fiscal do GL.
- A granularidade é **diária** — cada data do calendário gregoriano dentro do range do calendário fiscal tem uma linha.
- O `PERIOD_SET_NAME` identifica qual calendário fiscal está sendo utilizado (uma organização pode ter múltiplos calendários).
- As colunas `DAY_OF_PERIOD`, `DAY_OF_QUARTER` e `DAY_OF_YEAR` são úteis para análises comparativas (day-over-day).
- A confiança geral desta view é moderada (🟡) pois a documentação oficial Oracle é limitada para views fiscais derivadas.

---

## 🔗 PVOs Relacionados

### [[fiscaldaypvo|FiscalDayPVO]] (GL · BICC: 18/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJUSTMENT_PERIOD_FLAG | FiscalPeriodAdjustmentPeriodFlag | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DAY_OF_MONTH | DayOfMonth | — |
| DAY_OF_WEEK | DayOfWeek | ✅ |
| DAY_OF_YEAR | DayOfYear | — |
| ENTERPRISE_ID | EnterpriseId | — |
| FISCAL_PERIOD_CREATION_DATE | FiscalPeriodCreationDate | — |
| FISCAL_PERIOD_END_DATE | FiscalPeriodEndDate | ✅ |
| FISCAL_PERIOD_LAST_UPDATE_DATE | FiscalPeriodLastUpdateDate | ✅ |
| FISCAL_PERIOD_NAME | FiscalPeriodName | ✅ |
| FISCAL_PERIOD_NUMBER | FiscalPeriodNumber | ✅ |
| FISCAL_PERIOD_SET_ID | FiscalPeriodSetId | ✅ |
| FISCAL_PERIOD_SET_NAME | FiscalPeriodSetName | ✅ |
| FISCAL_PERIOD_START_DATE | FiscalPeriodStartDate | ✅ |
| FISCAL_PERIOD_TYPE | FiscalPeriodType | ✅ |
| FISCAL_PERIODSET_CREATION_DATE | FiscalPeriodsetCreationDate | — |
| FISCAL_QUARTER_END_DATE | FiscalQuarterEndDate | ✅ |
| FISCAL_QUARTER_NUMBER | FiscalQuarterNumber | ✅ |
| FISCAL_QUARTER_START_DATE | FiscalQuarterStartDate | ✅ |
| FISCAL_YEAR_END_DATE | FiscalYearEndDate | ✅ |
| FISCAL_YEAR_NUMBER | FiscalYearNumber | ✅ |
| FISCAL_YEAR_START_DATE | FiscalYearStartDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| PARENT_MONTH | ParentMonth | — |
| PARENT_WEEK | ParentWeek | — |
| REPORT_DATE | ReportDate | ✅ |

### [[rmcsfiscaldaypvo|RMCSFiscalDayPVO]] (OTHER · BICC: 18/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJUSTMENT_PERIOD_FLAG | AdjustmentPeriodFlag | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DAY_OF_MONTH | DayOfMonth | — |
| DAY_OF_WEEK | DayOfWeek | ✅ |
| DAY_OF_YEAR | DayOfYear | — |
| ENTERPRISE_ID | EnterpriseId | — |
| FISCAL_PERIOD_CREATION_DATE | FiscalPeriodCreationDate | — |
| FISCAL_PERIOD_END_DATE | FiscalPeriodEndDate | ✅ |
| FISCAL_PERIOD_LAST_UPDATE_DATE | FiscalPeriodLastUpdateDate | ✅ |
| FISCAL_PERIOD_NAME | FiscalPeriodName | ✅ |
| FISCAL_PERIOD_NUMBER | FiscalPeriodNumber | ✅ |
| FISCAL_PERIOD_SET_ID | FiscalPeriodSetId | ✅ |
| FISCAL_PERIOD_SET_NAME | FiscalPeriodSetName | ✅ |
| FISCAL_PERIOD_START_DATE | FiscalPeriodStartDate | ✅ |
| FISCAL_PERIOD_TYPE | FiscalPeriodType | ✅ |
| FISCAL_PERIODSET_CREATION_DATE | FiscalPeriodsetCreationDate | — |
| FISCAL_QUARTER_END_DATE | FiscalQuarterEndDate | ✅ |
| FISCAL_QUARTER_NUMBER | FiscalQuarterNumber | ✅ |
| FISCAL_QUARTER_START_DATE | FiscalQuarterStartDate | ✅ |
| FISCAL_YEAR_END_DATE | FiscalYearEndDate | ✅ |
| FISCAL_YEAR_NUMBER | FiscalYearNumber | ✅ |
| FISCAL_YEAR_START_DATE | FiscalYearStartDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| PARENT_MONTH | ParentMonth | — |
| PARENT_WEEK | ParentWeek | — |
| REPORT_DATE | ReportDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — GL Fiscal Calendar Views](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glperiodstatuses-25740.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
