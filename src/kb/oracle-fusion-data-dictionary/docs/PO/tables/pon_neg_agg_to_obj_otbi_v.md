---
id: DOC-PO-024
doc_type: system-doc
title: "PON_NEG_AGG_TO_OBJ_OTBI_V — Agregação de Negociações por Objetivo (View OTBI)"
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
  - negotiation
  - objectives
  - otbi
  - analytics
aliases:
  - PON_NEG_AGG_TO_OBJ_OTBI_V
  - pon_neg_agg_to_obj_otbi_v
  - agregacao-negociacao-objetivo-otbi
  - neg-agg-obj-otbi
  - pon-neg-agg-obj
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_NEG_AGG_TO_OBJ_OTBI_V

## 📌 Visão Geral

View de analytics (OTBI) que apresenta dados **agregados de negociações vinculadas a objetivos** dentro de programas de sourcing. Consolida métricas como quantidade de negociações, valores totais e status por objetivo, permitindo análises de desempenho no Oracle Transactional Business Intelligence (OTBI).

> [!note] Sufixo _OTBI_V
> O sufixo `_OTBI_V` indica uma **view otimizada para OTBI** (Oracle Transactional Business Intelligence), pré-agregada para uso em dashboards e relatórios analíticos.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Análise de programas de sourcing:** Métricas de negociações por objetivo dentro de programas estratégicos.
- **Dashboard de procurement:** Alimenta indicadores de progresso (quantas negociações completadas vs. planejadas por objetivo).
- **KPIs de sourcing:** Acompanhamento de economia (savings), número de fornecedores participantes e tempo médio de ciclo por objetivo.
- **Relatórios OTBI:** View pré-otimizada para subject areas de Procurement no BI Publisher e Smart View.
- **Governança de programas:** Visibilidade executiva sobre o progresso de objetivos estratégicos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | OBJECTIVE_ID | NUMBER(18) | NOT NULL | FK | Identificador do objetivo | [[pon_objective_negotiations]] | 🟡 75% |
| 2 | PROGRAM_ID | NUMBER(18) | NOT NULL | FK | Identificador do programa de sourcing | [[pon_program_headers]] | 🟡 75% |
| 3 | NEGOTIATION_ID | NUMBER(18) | NULL | FK | Identificador da negociação | — | 🟡 70% |
| 4 | NEGOTIATION_STATUS | VARCHAR2(30) | NULL | Classificação | Status da negociação (DRAFT, ACTIVE, CLOSED, AWARDED, CANCELLED) | — | 🟡 70% |
| 5 | TOTAL_AMOUNT | NUMBER | NULL | Financeiro | Valor total estimado da negociação | — | 🟡 65% |
| 6 | AWARDED_AMOUNT | NUMBER | NULL | Financeiro | Valor total adjudicado | — | 🟡 65% |
| 7 | SAVINGS_AMOUNT | NUMBER | NULL | Financeiro | Economia realizada (diferença entre estimado e adjudicado) | — | 🟡 60% |
| 8 | SUPPLIER_COUNT | NUMBER | NULL | Métrica | Número de fornecedores participantes | — | 🟡 60% |
| 9 | RESPONSE_COUNT | NUMBER | NULL | Métrica | Número de respostas/lances recebidos | — | 🟡 60% |
| 10 | BU_ID | NUMBER(18) | NULL | Multi-Org | Business unit | — | 🟡 65% |
| 11 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda | — | 🟡 70% |
| 12 | OPEN_DATE | DATE | NULL | Data | Data de abertura da negociação | — | 🟡 65% |
| 13 | CLOSE_DATE | DATE | NULL | Data | Data de fechamento da negociação | — | 🟡 65% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_program_headers]] — via `PROGRAM_ID` (programa de sourcing)
- [[pon_objective_negotiations]] — via `OBJECTIVE_ID` (objetivo do programa)
- [[pon_program_objectives]] — via `OBJECTIVE_ID` (definição do objetivo)

### Tabelas-filha (FK de saída)
- View OTBI — consumida por dashboards; não possui tabelas-filha.

---

## 📎 Uso Típico

### Progresso de negociações por objetivo
```sql
SELECT v.OBJECTIVE_ID, v.NEGOTIATION_STATUS,
       COUNT(*) AS qtd_negociacoes,
       SUM(v.TOTAL_AMOUNT) AS valor_total
FROM   PON_NEG_AGG_TO_OBJ_OTBI_V v
WHERE  v.PROGRAM_ID = :p_program_id
GROUP BY v.OBJECTIVE_ID, v.NEGOTIATION_STATUS;
```

### Economia total por programa
```sql
SELECT v.PROGRAM_ID,
       SUM(v.SAVINGS_AMOUNT) AS economia_total,
       SUM(v.AWARDED_AMOUNT) AS total_adjudicado
FROM   PON_NEG_AGG_TO_OBJ_OTBI_V v
GROUP BY v.PROGRAM_ID;
```

---

## 🔒 Observações

- Esta é uma **view OTBI pré-agregada** — não armazena dados diretamente; é derivada de tabelas transacionais do módulo Sourcing.
- Os valores financeiros estão na moeda indicada por `CURRENCY_CODE`; conversão para moeda funcional deve ser feita no relatório.
- A view é otimizada para leitura analítica — **não** deve ser utilizada em processos transacionais.
- A disponibilidade de colunas pode variar conforme o release do Oracle Fusion. Validar no ambiente antes de construir relatórios dependentes.

---

## 📚 Referências

- [Oracle Docs — Sourcing OTBI Subject Areas](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pon-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
