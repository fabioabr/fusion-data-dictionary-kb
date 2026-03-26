---
id: DOC-AR-004
doc_type: system-doc
title: "RA_CUST_TRX_LINE_SALESREPS_ALL — Créditos de Vendas por Linha"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-receivable
  - data-dictionary
  - vendedores
  - comissionamento
  - sales-credits
aliases:
  - RA_CUST_TRX_LINE_SALESREPS_ALL
  - ra_cust_trx_line_salesreps_all
  - creditos-vendas-ar
  - ar-salesreps
  - comissoes-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_CUST_TRX_LINE_SALESREPS_ALL

## 📌 Visão Geral

Armazena a **atribuição de vendedores (sales credits)** às linhas de transação do módulo Accounts Receivable. Permite que uma mesma linha tenha crédito de venda dividido entre **múltiplos vendedores**, tanto para receita (revenue credit) quanto para crédito não-receita (non-revenue credit, usado em bônus e reconhecimento).

É a tabela de referência para todo processo de **comissionamento e atribuição comercial** vinculado a transações AR.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Comissionamento:** Base para cálculo de comissões de vendedores, usando `REVENUE_AMOUNT_SPLIT` e `REVENUE_PERCENT_SPLIT`.
- **Relatórios de vendas por representante:** Associação de faturamento a vendedores individuais para análise de performance comercial.
- **Divisão de crédito:** Suporte a cenários onde múltiplos vendedores compartilham crédito sobre a mesma linha de transação.
- **Crédito não-receita:** Campos `NON_REVENUE_*` permitem atribuição de crédito para fins de reconhecimento/bônus sem impacto contábil na receita.
- **Grupos de venda:** Campos `REVENUE_SALESGROUP_ID` e `NON_REVENUE_SALESGROUP_ID` associam créditos a equipes/grupos comerciais.
- **Rastreabilidade:** `PREV_CUST_TRX_LINE_SALESREP_ID` mantém o histórico quando créditos são reatribuídos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CUST_TRX_LINE_SALESREP_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de crédito de venda | — | 🟢 100% |
| 2 | CUSTOMER_TRX_LINE_ID | NUMBER(18) | NULL | FK | Referência à linha da transação | [[ra_customer_trx_lines_all]] | 🟢 100% |
| 3 | CUSTOMER_TRX_ID | NUMBER(18) | NOT NULL | FK | Referência ao cabeçalho da transação | [[ra_customer_trx_all]] | 🟢 100% |
| 4 | SALESREP_ID | NUMBER(18) | NOT NULL | FK | Identificador do vendedor/representante | [[jtf_rs_salesreps]] | 🟢 100% |
| 5 | REVENUE_AMOUNT_SPLIT | NUMBER | NULL | Financeiro | Valor de receita atribuído ao vendedor | — | 🟢 100% |
| 6 | NON_REVENUE_AMOUNT_SPLIT | NUMBER | NULL | Financeiro | Valor de crédito não-receita atribuído ao vendedor | — | 🟢 100% |
| 7 | REVENUE_PERCENT_SPLIT | NUMBER | NULL | Financeiro | Percentual de crédito de receita (0-100) | — | 🟢 100% |
| 8 | NON_REVENUE_PERCENT_SPLIT | NUMBER | NULL | Financeiro | Percentual de crédito não-receita (0-100) | — | 🟢 100% |
| 9 | REVENUE_SALESGROUP_ID | NUMBER(18) | NULL | Comercial | Grupo de vendas para crédito de receita | [[jtf_rs_groups_b]] | 🟢 100% |
| 10 | NON_REVENUE_SALESGROUP_ID | NUMBER(18) | NULL | Comercial | Grupo de vendas para crédito não-receita | [[jtf_rs_groups_b]] | 🟢 100% |
| 11 | PREV_CUST_TRX_LINE_SALESREP_ID | NUMBER(18) | NULL | Referência cruzada | Registro anterior de crédito (reatribuição/credit memo) | self | 🟢 100% |
| 12 | ORIGINAL_LINE_SALESREP_ID | NUMBER(18) | NULL | Referência cruzada | Registro original de crédito (antes de ajustes) | self | 🟡 75% |
| 13 | SALESREP_REVENUE_BASIS | VARCHAR2(30) | NULL | Comercial | Base de cálculo do crédito de receita | — | 🟡 70% |
| 14 | REVENUE_ADJUSTMENT_ID | NUMBER(18) | NULL | Contabilidade | ID do ajuste de receita associado | — | 🟢 100% |
| 15 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 16 | ATTRIBUTE1 | VARCHAR2(150) | NULL | DFF | Atributo descritivo 1 | — | 🟢 100% |
| 17 | ATTRIBUTE2 | VARCHAR2(150) | NULL | DFF | Atributo descritivo 2 | — | 🟢 100% |
| 18 | ATTRIBUTE3 | VARCHAR2(150) | NULL | DFF | Atributo descritivo 3 | — | 🟢 100% |
| 19 | ATTRIBUTE4 | VARCHAR2(150) | NULL | DFF | Atributo descritivo 4 | — | 🟢 100% |
| 20 | ATTRIBUTE5 | VARCHAR2(150) | NULL | DFF | Atributo descritivo 5 | — | 🟢 100% |
| 21 | ATTRIBUTE6–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos 6 a 15 | — | 🟢 100% |
| 22 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 23 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 24 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 25 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 26 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 27 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_customer_trx_all]] — via `CUSTOMER_TRX_ID` (cabeçalho da transação)
- [[ra_customer_trx_lines_all]] — via `CUSTOMER_TRX_LINE_ID` (linha da transação)
- [[jtf_rs_salesreps]] — via `SALESREP_ID` (vendedor/representante)
- [[jtf_rs_groups_b]] — via `REVENUE_SALESGROUP_ID`, `NON_REVENUE_SALESGROUP_ID` (grupos de vendas)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da atribuição de vendedor na linha)

### Tabelas-filha (FK de saída)
- Não possui tabelas-filha diretas. Relaciona-se indiretamente com módulos de comissionamento e incentivos.

### Self-references
- `PREV_CUST_TRX_LINE_SALESREP_ID` — Registro anterior de crédito (quando reatribuído ou originado de credit memo)
- `ORIGINAL_LINE_SALESREP_ID` — Registro original antes de ajustes de receita

---

## 📎 Uso Típico

### Relatório de vendas por representante
```sql
SELECT sr.NAME AS vendedor,
       SUM(srep.REVENUE_AMOUNT_SPLIT) AS total_receita,
       COUNT(DISTINCT srep.CUSTOMER_TRX_ID) AS qtd_transacoes
FROM   RA_CUST_TRX_LINE_SALESREPS_ALL srep
JOIN   JTF_RS_SALESREPS sr
       ON sr.SALESREP_ID = srep.SALESREP_ID
WHERE  srep.ORG_ID = :p_org_id
GROUP BY sr.NAME
ORDER BY total_receita DESC;
```

### Linhas com crédito dividido entre vendedores
```sql
SELECT ct.TRX_NUMBER, ctl.LINE_NUMBER,
       sr.NAME AS vendedor,
       srep.REVENUE_PERCENT_SPLIT,
       srep.REVENUE_AMOUNT_SPLIT
FROM   RA_CUST_TRX_LINE_SALESREPS_ALL srep
JOIN   RA_CUSTOMER_TRX_ALL ct
       ON ct.CUSTOMER_TRX_ID = srep.CUSTOMER_TRX_ID
JOIN   RA_CUSTOMER_TRX_LINES_ALL ctl
       ON ctl.CUSTOMER_TRX_LINE_ID = srep.CUSTOMER_TRX_LINE_ID
JOIN   JTF_RS_SALESREPS sr
       ON sr.SALESREP_ID = srep.SALESREP_ID
WHERE  srep.ORG_ID = :p_org_id
ORDER BY ct.TRX_NUMBER, ctl.LINE_NUMBER;
```

### Filtros comuns
- `REVENUE_PERCENT_SPLIT > 0` — Apenas créditos com percentual de receita
- `NON_REVENUE_PERCENT_SPLIT > 0` — Apenas créditos não-receita (bônus/reconhecimento)
- `SALESREP_ID = :p_salesrep_id` — Filtrar por vendedor específico
- `REVENUE_SALESGROUP_ID = :p_group_id` — Filtrar por grupo de vendas

---

## 🔒 Observações

- A soma de `REVENUE_PERCENT_SPLIT` para todas as atribuições de uma mesma linha deve ser **100%**. Isso é validado pelo Oracle Fusion ao salvar a transação.
- O campo `NON_REVENUE_AMOUNT_SPLIT` não afeta a contabilidade; é usado apenas para fins de **relatório e comissionamento**.
- Quando um credit memo é gerado, os créditos de venda são copiados da transação original e `PREV_CUST_TRX_LINE_SALESREP_ID` aponta para o registro original.
- Em cenários de **Revenue Adjustment**, o `REVENUE_ADJUSTMENT_ID` conecta a alteração de crédito ao ajuste contábil correspondente.
- A tabela possui **Descriptive Flexfields (DFF)** via `ATTRIBUTE1–15` para customizações por implementação.
- O vendedor padrão da transação é definido em `PRIMARY_SALESREP_ID` no cabeçalho ([[ra_customer_trx_all]]), mas pode ser sobrescrito por linha nesta tabela.

---

## 📚 Referências

- [Oracle Docs — RA_CUST_TRX_LINE_SALESREPS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/racusttrxlinesalesrepsall-25222.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
