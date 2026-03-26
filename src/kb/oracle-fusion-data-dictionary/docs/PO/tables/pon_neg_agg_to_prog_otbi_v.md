---
id: DOC-PO-025
doc_type: system-doc
title: "PON_NEG_AGG_TO_PROG_OTBI_V — Agregação de Negociações por Programa (View OTBI)"
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
  - programs
  - otbi
  - analytics
aliases:
  - PON_NEG_AGG_TO_PROG_OTBI_V
  - pon_neg_agg_to_prog_otbi_v
  - agregacao-negociacao-programa-otbi
  - neg-agg-prog-otbi
  - pon-neg-agg-prog
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_NEG_AGG_TO_PROG_OTBI_V

## 📌 Visão Geral

View de analytics (OTBI) que apresenta dados **agregados de negociações vinculadas a programas** de sourcing. Consolida métricas no nível de programa — total de negociações, valores, savings, status e progresso — para consumo em dashboards e relatórios analíticos do Oracle Transactional Business Intelligence.

> [!note] Sufixo _OTBI_V
> O sufixo `_OTBI_V` indica uma **view otimizada para OTBI**, pré-agregada para uso em dashboards e relatórios analíticos no BI Publisher / Smart View.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Acompanhamento de programas de sourcing:** Métricas consolidadas de todas as negociações vinculadas a um programa.
- **Dashboard executivo:** Indicadores de economia total, percentual de conclusão e efetividade do programa.
- **Comparação entre programas:** Análise comparativa de desempenho entre diferentes programas de sourcing.
- **Relatórios OTBI:** Subject area de Procurement Programs para análises self-service.
- **Governança estratégica:** Visão macro do portfólio de programas de procurement.

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
| 2 | PROGRAM_NAME | VARCHAR2(240) | NULL | Descritivo | Nome do programa | — | 🟡 70% |
| 3 | PROGRAM_STATUS | VARCHAR2(30) | NULL | Classificação | Status do programa (DRAFT, ACTIVE, COMPLETED, CANCELLED) | — | 🟡 70% |
| 4 | NEGOTIATION_COUNT | NUMBER | NULL | Métrica | Total de negociações vinculadas ao programa | — | 🟡 65% |
| 5 | COMPLETED_NEG_COUNT | NUMBER | NULL | Métrica | Negociações concluídas/adjudicadas | — | 🟡 60% |
| 6 | ACTIVE_NEG_COUNT | NUMBER | NULL | Métrica | Negociações atualmente ativas | — | 🟡 60% |
| 7 | TOTAL_ESTIMATED_AMOUNT | NUMBER | NULL | Financeiro | Valor total estimado de todas as negociações | — | 🟡 65% |
| 8 | TOTAL_AWARDED_AMOUNT | NUMBER | NULL | Financeiro | Valor total adjudicado | — | 🟡 65% |
| 9 | TOTAL_SAVINGS_AMOUNT | NUMBER | NULL | Financeiro | Economia total realizada pelo programa | — | 🟡 60% |
| 10 | SAVINGS_PERCENTAGE | NUMBER | NULL | Métrica | Percentual de economia (savings / estimado × 100) | — | 🟡 55% |
| 11 | SUPPLIER_COUNT | NUMBER | NULL | Métrica | Total de fornecedores participantes no programa | — | 🟡 60% |
| 12 | BU_ID | NUMBER(18) | NULL | Multi-Org | Business unit | — | 🟡 65% |
| 13 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda | — | 🟡 70% |
| 14 | PROGRAM_START_DATE | DATE | NULL | Data | Data de início do programa | — | 🟡 65% |
| 15 | PROGRAM_END_DATE | DATE | NULL | Data | Data de término do programa | — | 🟡 65% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_program_headers]] — via `PROGRAM_ID` (cabeçalho do programa de sourcing)

### Tabelas-filha (FK de saída)
- View OTBI — consumida por dashboards; não possui tabelas-filha.

---

## 📎 Uso Típico

### Resumo de desempenho por programa
```sql
SELECT v.PROGRAM_ID, v.PROGRAM_NAME, v.PROGRAM_STATUS,
       v.NEGOTIATION_COUNT, v.COMPLETED_NEG_COUNT,
       v.TOTAL_SAVINGS_AMOUNT, v.SAVINGS_PERCENTAGE
FROM   PON_NEG_AGG_TO_PROG_OTBI_V v
WHERE  v.PROGRAM_STATUS = 'ACTIVE'
ORDER BY v.TOTAL_SAVINGS_AMOUNT DESC;
```

### Top 10 programas por economia
```sql
SELECT v.PROGRAM_NAME, v.TOTAL_ESTIMATED_AMOUNT,
       v.TOTAL_AWARDED_AMOUNT, v.TOTAL_SAVINGS_AMOUNT,
       v.SAVINGS_PERCENTAGE
FROM   PON_NEG_AGG_TO_PROG_OTBI_V v
WHERE  v.TOTAL_SAVINGS_AMOUNT > 0
ORDER BY v.TOTAL_SAVINGS_AMOUNT DESC
FETCH FIRST 10 ROWS ONLY;
```

---

## 🔒 Observações

- Esta é uma **view OTBI pré-agregada** no nível de programa — não armazena dados diretamente.
- Para detalhamento por objetivo, utilizar [[pon_neg_agg_to_obj_otbi_v]].
- A coluna `SAVINGS_PERCENTAGE` pode ser calculada ou derivada; verificar no ambiente se está disponível ou se deve ser calculada manualmente.
- Valores financeiros estão na moeda indicada por `CURRENCY_CODE`; conversão deve ser feita no relatório se necessário.
- A view é otimizada para leitura analítica — **não** deve ser utilizada em processos transacionais.

---

## 📚 Referências

- [Oracle Docs — Sourcing OTBI Subject Areas](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pon-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
