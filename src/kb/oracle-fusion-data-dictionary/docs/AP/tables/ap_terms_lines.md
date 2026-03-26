---
id: DOC-AP-028
doc_type: system-doc
title: "AP_TERMS_LINES — Linhas de Condições de Pagamento"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, condicoes-pagamento, parcelas, linhas-terms]
aliases: [AP_TERMS_LINES, ap_terms_lines, payment_terms_lines, linhas_condicao_pagamento, parcelas_terms]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_TERMS_LINES

## Visão Geral

Tabela que armazena as linhas (parcelas) de cada condição de pagamento definida em [[ap_terms_b]]. Cada linha especifica o prazo de vencimento, o percentual do valor da fatura, descontos por antecipação e regras de cálculo de datas. Uma condição pode ter múltiplas linhas para parcelamentos.

## Propósito de Negócio

Detalha como o valor de uma fatura é distribuído em parcelas ao longo do tempo, incluindo descontos por pagamento antecipado. É essencial para: (1) cálculo de datas de vencimento por parcela, (2) definição de percentuais de desconto por antecipação, (3) planejamento de fluxo de caixa com parcelamentos, (4) geração automática de payment schedules nas faturas.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TERM_ID | NUMBER(15) | NOT NULL | PK/FK | FK para [[ap_terms_b]]. Condição de pagamento pai. | [[ap_terms_b]] | 🟢 100% |
| 2 | SEQUENCE_NUM | NUMBER | NOT NULL | PK | Número sequencial da linha/parcela (compõe PK com TERM_ID). | — | 🟢 100% |
| 3 | DUE_PERCENT | NUMBER | NULL | Regra | Percentual do valor da fatura devido nesta parcela. | — | 🟢 100% |
| 4 | DUE_AMOUNT | NUMBER | NULL | Financeiro | Valor fixo devido nesta parcela (alternativa a DUE_PERCENT). | — | 🟢 90% |
| 5 | DUE_DAYS | NUMBER | NULL | Regra | Dias após a data-base para vencimento desta parcela. | — | 🟢 100% |
| 6 | DUE_DAY_OF_MONTH | NUMBER | NULL | Regra | Dia fixo do mês para vencimento (ex.: 15, 30). | — | 🟢 95% |
| 7 | DUE_MONTHS_FORWARD | NUMBER | NULL | Regra | Meses à frente da data-base para vencimento. | — | 🟢 90% |
| 8 | DISCOUNT_PERCENT | NUMBER | NULL | Desconto | Percentual de desconto por pagamento antecipado (1o período). | — | 🟢 100% |
| 9 | DISCOUNT_DAYS | NUMBER | NULL | Desconto | Dias para elegibilidade ao desconto (1o período). | — | 🟢 100% |
| 10 | DISCOUNT_PERCENT_2 | NUMBER | NULL | Desconto | Percentual de desconto — 2o período. | — | 🟢 90% |
| 11 | DISCOUNT_DAYS_2 | NUMBER | NULL | Desconto | Dias para elegibilidade ao desconto — 2o período. | — | 🟢 90% |
| 12 | DISCOUNT_PERCENT_3 | NUMBER | NULL | Desconto | Percentual de desconto — 3o período. | — | 🟢 90% |
| 13 | DISCOUNT_DAYS_3 | NUMBER | NULL | Desconto | Dias para elegibilidade ao desconto — 3o período. | — | 🟢 90% |
| 14 | CALENDAR | VARCHAR2(15) | NULL | Configuração | Calendário de vencimentos (se aplicável). | — | 🟡 70% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 16 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[ap_terms_b]]** — Condição de pagamento (N:1 via `TERM_ID`).

### Tabelas-filha

- Nenhuma tabela-filha direta identificada.

## Uso Típico

```sql
-- Parcelas e descontos de uma condição de pagamento específica
SELECT tl.TERM_ID,
       tb.NAME,
       tl.SEQUENCE_NUM,
       tl.DUE_PERCENT,
       tl.DUE_DAYS,
       tl.DUE_DAY_OF_MONTH,
       tl.DISCOUNT_PERCENT,
       tl.DISCOUNT_DAYS
  FROM AP_TERMS_LINES tl
  JOIN AP_TERMS_B tb
    ON tb.TERM_ID = tl.TERM_ID
 WHERE tb.NAME = :p_term_name
 ORDER BY tl.SEQUENCE_NUM;
```

## Observações

- A PK composta é (`TERM_ID`, `SEQUENCE_NUM`).
- Para condições simples (ex.: NET30), existe apenas uma linha com `DUE_PERCENT = 100` e `DUE_DAYS = 30`.
- Para parcelamentos, a soma de `DUE_PERCENT` de todas as linhas deve totalizar 100%.
- Descontos em cascata são configurados via `DISCOUNT_PERCENT`, `DISCOUNT_PERCENT_2` e `DISCOUNT_PERCENT_3` com seus respectivos `DISCOUNT_DAYS`.
- `DUE_DAYS` e `DUE_DAY_OF_MONTH` são mutuamente exclusivos na maioria das implementações.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Payment Terms Setup Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
