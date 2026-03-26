---
id: DOC-PO-028
doc_type: system-doc
title: "PON_OBJ_AGG_TO_PROG_OTBI_V — Agregação de Objetivos por Programa (View OTBI)"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - objectives
  - programs
  - otbi
  - analytics
aliases:
  - PON_OBJ_AGG_TO_PROG_OTBI_V
  - pon_obj_agg_to_prog_otbi_v
  - agregacao-objetivos-programa-otbi
  - obj-agg-prog-otbi
  - pon-obj-agg-prog
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_OBJ_AGG_TO_PROG_OTBI_V

## 📌 Visão Geral

View de analytics (OTBI) que apresenta dados **agregados de objetivos vinculados a programas** de sourcing. Consolida métricas no nível de objetivo dentro de cada programa — total de negociações por objetivo, valores estimados e realizados, economia e progresso — para consumo em dashboards executivos.

> [!note] Sufixo _OTBI_V
> O sufixo `_OTBI_V` indica uma **view otimizada para OTBI** (Oracle Transactional Business Intelligence), pré-agregada para dashboards e relatórios analíticos.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Monitoramento de objetivos:** Acompanhamento do progresso de cada objetivo dentro de um programa de sourcing.
- **Análise de aderência:** Avalia se os objetivos do programa estão sendo atendidos conforme planejado.
- **Dashboard executivo:** Indicadores de progresso por objetivo (% de negociações concluídas, economia realizada vs. meta).
- **Priorização de ações:** Identifica objetivos atrasados ou com desempenho abaixo do esperado.
- **Relatórios OTBI:** Subject area de Sourcing Programs para análises de portfólio.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROGRAM_ID | NUMBER(18) | NOT NULL | FK | Identificador do programa de sourcing | [[pon_program_headers]] | 🟡 75% |
| 2 | OBJECTIVE_ID | NUMBER(18) | NOT NULL | FK | Identificador do objetivo | [[pon_program_objectives]] | 🟡 75% |
| 3 | OBJECTIVE_NAME | VARCHAR2(240) | NULL | Descritivo | Nome do objetivo | — | 🟡 65% |
| 4 | OBJECTIVE_STATUS | VARCHAR2(30) | NULL | Classificação | Status do objetivo (OPEN, IN_PROGRESS, COMPLETED, CANCELLED) | — | 🟡 65% |
| 5 | NEGOTIATION_COUNT | NUMBER | NULL | Métrica | Total de negociações vinculadas ao objetivo | — | 🟡 65% |
| 6 | COMPLETED_NEG_COUNT | NUMBER | NULL | Métrica | Negociações concluídas/adjudicadas | — | 🟡 60% |
| 7 | TOTAL_ESTIMATED_AMOUNT | NUMBER | NULL | Financeiro | Valor total estimado das negociações do objetivo | — | 🟡 65% |
| 8 | TOTAL_AWARDED_AMOUNT | NUMBER | NULL | Financeiro | Valor total adjudicado | — | 🟡 65% |
| 9 | TOTAL_SAVINGS_AMOUNT | NUMBER | NULL | Financeiro | Economia total realizada no objetivo | — | 🟡 60% |
| 10 | TARGET_SAVINGS_AMOUNT | NUMBER | NULL | Financeiro | Meta de economia definida para o objetivo | — | 🟡 55% |
| 11 | COMPLETION_PERCENTAGE | NUMBER | NULL | Métrica | Percentual de conclusão do objetivo | — | 🟡 55% |
| 12 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda | — | 🟡 70% |
| 13 | OBJECTIVE_START_DATE | DATE | NULL | Data | Data de início do objetivo | — | 🟡 60% |
| 14 | OBJECTIVE_END_DATE | DATE | NULL | Data | Data de término do objetivo | — | 🟡 60% |
| 15 | BU_ID | NUMBER(18) | NULL | Multi-Org | Business unit | — | 🟡 65% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_program_headers]] — via `PROGRAM_ID` (programa de sourcing)
- [[pon_program_objectives]] — via `OBJECTIVE_ID` (definição do objetivo)

### Tabelas-filha (FK de saída)
- View OTBI — consumida por dashboards; não possui tabelas-filha.

---

## 📎 Uso Típico

### Progresso de objetivos por programa
```sql
SELECT v.OBJECTIVE_ID, v.OBJECTIVE_NAME, v.OBJECTIVE_STATUS,
       v.NEGOTIATION_COUNT, v.COMPLETED_NEG_COUNT,
       v.COMPLETION_PERCENTAGE
FROM   PON_OBJ_AGG_TO_PROG_OTBI_V v
WHERE  v.PROGRAM_ID = :p_program_id
ORDER BY v.COMPLETION_PERCENTAGE DESC;
```

### Objetivos com economia abaixo da meta
```sql
SELECT v.OBJECTIVE_NAME, v.TARGET_SAVINGS_AMOUNT,
       v.TOTAL_SAVINGS_AMOUNT,
       (v.TOTAL_SAVINGS_AMOUNT / NULLIF(v.TARGET_SAVINGS_AMOUNT, 0)) * 100
         AS pct_meta_atingida
FROM   PON_OBJ_AGG_TO_PROG_OTBI_V v
WHERE  v.PROGRAM_ID = :p_program_id
  AND  v.TOTAL_SAVINGS_AMOUNT < v.TARGET_SAVINGS_AMOUNT;
```

---

## 🔒 Observações

- Esta é uma **view OTBI pré-agregada** no nível de objetivo — complementa [[pon_neg_agg_to_prog_otbi_v]] (nível programa) e [[pon_neg_agg_to_obj_otbi_v]] (nível negociação por objetivo).
- As métricas calculadas (`COMPLETION_PERCENTAGE`, `TARGET_SAVINGS_AMOUNT`) podem não existir em todos os releases; validar disponibilidade no ambiente.
- Valores financeiros estão na moeda indicada por `CURRENCY_CODE`.
- Para detalhes de negociações individuais dentro de um objetivo, utilizar [[pon_objective_negotiations]].

---

## 📚 Referências

- [Oracle Docs — Sourcing OTBI Subject Areas](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pon-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
