---
id: DOC-AR-057
doc_type: system-doc
title: "AR_SALES_CREDIT_TYPES — Tipos de Crédito de Venda"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, sales-credit, comissao, receita]
aliases: [AR_SALES_CREDIT_TYPES, ar_sales_credit_types, sales_credit_types, tipos_credito_venda, ar_sc_types]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_SALES_CREDIT_TYPES

## 📌 Visão Geral

Tabela de cadastro de **tipos de crédito de venda** (sales credit types). Classifica os créditos como **revenue** (afetam reconhecimento de receita) ou **non-revenue** (apenas comissões, sem impacto em receita).

## 🧠 Propósito de Negócio

Os tipos de crédito de venda determinam como as comissões e atribuições de receita são tratadas. A distinção entre revenue e non-revenue é fundamental para garantir que a receita seja reconhecida corretamente sem duplicação, enquanto permite múltiplas atribuições de comissão.

Casos de uso principais:
- Classificação de comissões por vendedor (revenue vs. non-revenue)
- Controle de reconhecimento de receita por linha de fatura
- Atribuição de créditos a múltiplos vendedores sem duplicar receita
- Relatórios de performance comercial

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | SALES_CREDIT_TYPE_ID | NUMBER | PK. Identificador único do tipo de crédito de venda. | Chave | 🟢 100% |
| 2 | NAME | VARCHAR2 | Nome do tipo de crédito (exibido em LOVs). | Identificação | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2 | Descrição textual do tipo de crédito. | Identificação | 🟢 100% |
| 4 | TYPE | VARCHAR2 | Classificação: `R` (Revenue) ou `N` (Non-Revenue). | Classificação | 🟢 100% |
| 5 | ENABLED_FLAG | VARCHAR2 | Indica se o tipo está habilitado: `Y`/`N`. | Controle | 🟢 100% |
| 6 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 7 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 8 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 9 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ra_cust_trx_line_salesreps_all]] | SALES_CREDIT_TYPE_ID | Referenciada por | Atribuições de crédito de venda por linha |
| [[ra_salesreps_all]] | — | Referência | Vendedores que recebem créditos |

## 📎 Uso Típico

```sql
-- Listar tipos de crédito de venda ativos
SELECT sales_credit_type_id,
       name,
       type,
       description
  FROM ar_sales_credit_types
 WHERE enabled_flag = 'Y'
 ORDER BY type, name;
```

```sql
-- Créditos de venda por tipo em uma fatura
SELECT sct.name AS tipo_credito,
       sct.type AS classificacao,
       sr.name AS vendedor,
       lsr.revenue_amount_split,
       lsr.non_revenue_amount_split
  FROM ra_cust_trx_line_salesreps_all lsr
  JOIN ar_sales_credit_types sct ON sct.sales_credit_type_id = lsr.sales_credit_type_id
  JOIN ra_salesreps_all sr ON sr.salesrep_id = lsr.salesrep_id
 WHERE lsr.customer_trx_id = :p_trx_id;
```

## 🔒 Observações

- Cada linha de fatura deve ter **exatamente 100%** de crédito revenue (`TYPE = 'R'`) atribuído — caso contrário, a transação não pode ser completada.
- Créditos non-revenue (`TYPE = 'N'`) podem exceder 100% — são usados para bônus/comissões sem impacto na receita.
- A tabela é **compartilhada** entre todas as BUs (não particionada por ORG_ID).
- O tipo `R` (Revenue) é o padrão seeded pelo Oracle na instalação. Tipos adicionais podem ser criados conforme necessidade.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — Sales Credit Types View Object
- Oracle Fusion Cloud — Managing Sales Credits (Functional Guide)
