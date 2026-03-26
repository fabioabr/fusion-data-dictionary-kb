---
id: DOC-AP-030
doc_type: system-doc
title: "AP_TERMS_VL — View de Condições de Pagamento (Base + Tradução)"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, condicoes-pagamento, view-mls, terms-consolidada]
aliases: [AP_TERMS_VL, ap_terms_vl, payment_terms_view, view_condicoes_pagamento, terms_vl_ap]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_TERMS_VL

## Visão Geral

View consolidada (Virtual Language) que combina os atributos estruturais de [[ap_terms_b]] com o nome e descrição traduzidos de [[ap_terms_tl]], filtrando automaticamente pelo idioma da sessão do usuário. Segue o padrão Oracle MLS `_VL` e é o ponto de acesso recomendado para consultas que necessitam de dados traduzidos das condições de pagamento.

## Propósito de Negócio

Simplifica o acesso às condições de pagamento ao eliminar a necessidade de join manual entre `_B` e `_TL`. É o objeto recomendado para: (1) consultas em relatórios e BI, (2) LOVs (List of Values) em interfaces, (3) integração com ferramentas de extração (BICC/Incorta), (4) qualquer cenário onde nome e descrição traduzidos são necessários junto com os atributos técnicos.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TERM_ID | NUMBER(15) | NOT NULL | PK | Identificador único da condição de pagamento (de [[ap_terms_b]]). | — | 🟢 100% |
| 2 | NAME | VARCHAR2(50) | NOT NULL | Tradução | Nome da condição no idioma da sessão (de [[ap_terms_tl]]). | — | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Tradução | Descrição da condição no idioma da sessão (de [[ap_terms_tl]]). | — | 🟢 100% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Status | Indica se a condição está ativa (Y/N) (de [[ap_terms_b]]). | — | 🟢 100% |
| 5 | START_DATE_ACTIVE | DATE | NULL | Temporal | Data de início da vigência (de [[ap_terms_b]]). | — | 🟢 95% |
| 6 | END_DATE_ACTIVE | DATE | NULL | Temporal | Data de fim da vigência (de [[ap_terms_b]]). | — | 🟢 95% |
| 7 | DUE_CUTOFF_DAY | NUMBER | NULL | Regra | Dia de corte para cálculo de vencimento (de [[ap_terms_b]]). | — | 🟢 90% |
| 8 | RANK | NUMBER | NULL | Classificação | Prioridade da condição (de [[ap_terms_b]]). | — | 🟡 70% |
| 9 | TYPE | VARCHAR2(25) | NULL | Classificação | Tipo da condição — STANDARD, PREPAYMENT (de [[ap_terms_b]]). | — | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 11 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[ap_terms_b]]** — Tabela base com atributos estruturais.
- **[[ap_terms_tl]]** — Tabela de traduções (nome/descrição por idioma).

### Tabelas-filha

- **[[ap_terms_lines]]** — Linhas de parcelas/descontos (1:N via `TERM_ID`).
- **[[ap_invoices_all]]** — Faturas que utilizam esta condição (1:N via `TERMS_ID`).

## Uso Típico

```sql
-- Condições de pagamento ativas com descrição traduzida
SELECT tv.TERM_ID,
       tv.NAME,
       tv.DESCRIPTION,
       tv.ENABLED_FLAG,
       tv.START_DATE_ACTIVE,
       tv.END_DATE_ACTIVE,
       tv.TYPE
  FROM AP_TERMS_VL tv
 WHERE tv.ENABLED_FLAG = 'Y'
   AND NVL(tv.END_DATE_ACTIVE, SYSDATE + 1) > SYSDATE
 ORDER BY tv.NAME;
```

## Observações

- Esta view é o ponto de acesso recomendado para qualquer consulta que necessite de nome/descrição traduzidos.
- Internamente, a view faz join entre [[ap_terms_b]] e [[ap_terms_tl]] com filtro `LANGUAGE = USERENV('LANG')`.
- Para extração via Incorta/BICC, verificar se a view está disponível no data model ou se é necessário extrair `_B` e `_TL` separadamente e reconstruir o join.
- Não é uma tabela física — alterações devem ser feitas nas tabelas base [[ap_terms_b]] e [[ap_terms_tl]].
- Estrutura análoga a [[ra_terms_vl]] do módulo AR.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Multi-Language Support (MLS) Architecture.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
