---
id: DOC-GL-015
doc_type: system-doc
title: "GL_FISCAL_PERIOD_V — View de Períodos Fiscais"
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
  - periodos-fiscais
  - fiscal-calendar
aliases:
  - GL_FISCAL_PERIOD_V
  - gl_fiscal_period_v
  - periodos-fiscais-gl
  - fiscal-period-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_FISCAL_PERIOD_V

## 📌 Visão Geral

View que expõe os **períodos fiscais** do calendário contábil, consolidando informações de cada período (mês fiscal) com suas datas de início e fim, número do trimestre e ano fiscal. Permite consultas analíticas e operacionais sobre a estrutura temporal do calendário fiscal configurado no General Ledger.

> [!note] Sufixo _V
> O sufixo `_V` indica uma **view** derivada de tabelas base do calendário fiscal.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Navegação por períodos:** Listar todos os períodos fiscais disponíveis em um calendário.
- **Relatórios financeiros:** Determinar datas de corte para fechamento mensal.
- **Validação de GL_DATE:** Verificar se uma data contábil está dentro de um período fiscal válido.
- **ETL e Data Warehouse:** Dimensão de período para cubos analíticos e tabelas fato.
- **Comparativo período a período:** Análise de variações mensais com base na estrutura fiscal.

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
| 3 | PERIOD_NAME | VARCHAR2(15) | NOT NULL | PK | Nome do período fiscal (ex: JAN-26) | — | 🟡 80% |
| 4 | PERIOD_YEAR | NUMBER(15) | NOT NULL | Período | Ano fiscal | — | 🟡 80% |
| 5 | PERIOD_NUM | NUMBER(15) | NOT NULL | Período | Número sequencial do período no ano fiscal (1–12+) | — | 🟡 80% |
| 6 | QUARTER_NUM | NUMBER(15) | NOT NULL | Período | Número do trimestre fiscal (1–4) | — | 🟡 75% |
| 7 | START_DATE | DATE | NOT NULL | Período | Data de início do período fiscal | — | 🟡 80% |
| 8 | END_DATE | DATE | NOT NULL | Período | Data de fim do período fiscal | — | 🟡 80% |
| 9 | NUM_DAYS | NUMBER | NULL | Período | Quantidade de dias no período | — | 🟡 65% |
| 10 | YEAR_START_DATE | DATE | NULL | Período | Data de início do ano fiscal | — | 🟡 65% |
| 11 | QUARTER_START_DATE | DATE | NULL | Período | Data de início do trimestre fiscal | — | 🟡 65% |
| 12 | ENTERED_PERIOD_NAME | VARCHAR2(15) | NULL | Período | Nome do período conforme inserido (pode diferir do canônico) | — | 🟡 60% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_period_sets]] — via `PERIOD_SET_NAME` (definição do calendário fiscal)
- [[gl_periods]] — via `PERIOD_SET_NAME` + `PERIOD_NAME` (definição dos períodos)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma view de consulta (dimensão temporal).

---

## 📎 Uso Típico

### Listar períodos de um ano fiscal
```sql
SELECT fp.PERIOD_NAME,
       fp.PERIOD_NUM,
       fp.QUARTER_NUM,
       fp.START_DATE,
       fp.END_DATE
FROM   GL_FISCAL_PERIOD_V fp
WHERE  fp.PERIOD_SET_NAME = :p_calendar_name
  AND  fp.PERIOD_TYPE = 'Month'
  AND  fp.PERIOD_YEAR = 2026
ORDER BY fp.PERIOD_NUM;
```

### Encontrar o período fiscal de uma data
```sql
SELECT fp.PERIOD_NAME,
       fp.PERIOD_YEAR,
       fp.QUARTER_NUM
FROM   GL_FISCAL_PERIOD_V fp
WHERE  fp.PERIOD_SET_NAME = :p_calendar_name
  AND  fp.PERIOD_TYPE = 'Month'
  AND  :p_date BETWEEN fp.START_DATE AND fp.END_DATE;
```

### Filtros comuns
- `PERIOD_SET_NAME = 'Accounting'` — Calendário contábil principal
- `PERIOD_TYPE = 'Month'` — Períodos mensais
- `PERIOD_YEAR = 2026` — Ano fiscal específico

---

## 🔒 Observações

- Esta é uma **view**, não uma tabela física. Os dados derivam das configurações de calendário fiscal do GL.
- A granularidade é **por período** (tipicamente mensal), diferente de `GL_FISCAL_DAY_V` que é diária.
- O `PERIOD_SET_NAME` permite distinguir entre múltiplos calendários fiscais na mesma instância.
- Períodos de ajuste (adjustment periods) podem ter `PERIOD_NUM` maior que 12.
- Útil em JOINs com `GL_BALANCES` e `GL_PERIOD_STATUSES` para enriquecer consultas com datas e trimestres.

---

## 📚 Referências

- [Oracle Docs — GL Fiscal Calendar Views](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glperiodstatuses-25740.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
