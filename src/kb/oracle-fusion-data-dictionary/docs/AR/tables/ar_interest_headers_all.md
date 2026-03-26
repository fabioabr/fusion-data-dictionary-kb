---
id: DOC-AR-037
doc_type: system-doc
title: "AR_INTEREST_HEADERS_ALL — Cabeçalhos de Cobranças de Juros"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, juros, finance-charges, late-charges]
aliases: [AR_INTEREST_HEADERS_ALL, ar_interest_headers_all, interest_headers, cabecalho_juros, juros_ar]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_INTEREST_HEADERS_ALL

> [!note] Sufixo _ALL
> Tabela particionada por `ORG_ID`. O sufixo `_ALL` indica que contém dados de todas as business units. Acessos via views sem sufixo filtram automaticamente pelo contexto de segurança da sessão.

## 📌 Visão Geral

Tabela de cabeçalhos de cobranças de juros (late charges / finance charges) do Accounts Receivable. Cada registro representa um lote de cálculo de juros para um cliente em uma moeda específica, agrupando as linhas de detalhe em [[ar_interest_lines_all]].

## 🧠 Propósito de Negócio

O cálculo de juros sobre faturas em atraso é parte fundamental do processo de cobrança. Esta tabela registra os cabeçalhos dos lotes de cálculo, permitindo rastrear quando e para quem os juros foram calculados, o status do processamento e se os valores foram apresentados ao cliente. É essencial para gestão de receita financeira e compliance com termos contratuais.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | INTEREST_HEADER_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único do cabeçalho de juros. | PK | 🟢 100% |
| 2 | CUSTOMER_ID | NUMBER(15) | NOT NULL | FK para HZ_CUST_ACCOUNTS. Cliente ao qual os juros se referem. | FK | 🟢 100% |
| 3 | CUSTOMER_SITE_USE_ID | NUMBER(15) | NULL | FK para HZ_CUST_SITE_USES_ALL. Site de uso do cliente. | FK | 🟢 100% |
| 4 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Código da moeda dos juros calculados. | Financeiro | 🟢 100% |
| 5 | INTEREST_BATCH_ID | NUMBER(15) | NULL | Identificador do lote de processamento de juros. | FK | 🟢 100% |
| 6 | HEADER_TYPE | VARCHAR2(30) | NOT NULL | Tipo do cabeçalho (ex.: LATE_CHARGE, FINANCE_CHARGE). | Classificação | 🟢 100% |
| 7 | DISPLAY_FLAG | VARCHAR2(1) | NULL | Flag indicando se o registro deve ser exibido ao cliente (Y/N). | Controle | 🟢 100% |
| 8 | PROCESS_STATUS | VARCHAR2(30) | NOT NULL | Status do processamento (ex.: NEW, PROCESSED, ERROR). | Controle | 🟢 100% |
| 9 | PROCESS_MESSAGE | VARCHAR2(240) | NULL | Mensagem de erro ou processamento. | Controle | 🟡 75% |
| 10 | PAYMENT_SCHEDULE_ID | NUMBER(15) | NULL | FK para a parcela gerada pela cobrança de juros. | FK | 🟢 100% |
| 11 | CUSTOMER_TRX_ID | NUMBER(15) | NULL | FK para a transação de juros gerada (debit memo). | FK | 🟢 100% |
| 12 | TOTAL_INTEREST_AMOUNT | NUMBER | NULL | Valor total dos juros calculados no cabeçalho. | Financeiro | 🟢 100% |
| 13 | CHARGE_DATE | DATE | NULL | Data base do cálculo dos juros. | Temporal | 🟢 100% |
| 14 | ORG_ID | NUMBER(15) | NOT NULL | Identificador da business unit (Operating Unit). | Partição | 🟢 100% |
| 15 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 16 | REQUEST_ID | NUMBER(15) | NULL | Identificador da requisição concorrente que gerou o registro. | Técnico | 🟢 100% |
| 17 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 18 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 19 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 20 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **[[ar_interest_lines_all]]** — Linhas de detalhe dos juros (1:N via `INTEREST_HEADER_ID`).
- **HZ_CUST_ACCOUNTS** — Cliente associado (N:1 via `CUSTOMER_ID`).
- **HZ_CUST_SITE_USES_ALL** — Site de uso do cliente (N:1 via `CUSTOMER_SITE_USE_ID`).
- **RA_CUSTOMER_TRX_ALL** — Debit memo gerado (via `CUSTOMER_TRX_ID`).

## 📎 Uso Típico

```sql
-- Resumo de juros calculados por cliente e status
SELECT ih.CUSTOMER_ID,
       ih.CURRENCY_CODE,
       ih.PROCESS_STATUS,
       SUM(ih.TOTAL_INTEREST_AMOUNT) AS total_juros
  FROM AR_INTEREST_HEADERS_ALL ih
 WHERE ih.ORG_ID = :p_org_id
   AND ih.CHARGE_DATE BETWEEN :p_data_ini AND :p_data_fim
 GROUP BY ih.CUSTOMER_ID, ih.CURRENCY_CODE, ih.PROCESS_STATUS
 ORDER BY total_juros DESC;
```

## 🔒 Observações

- O processamento de juros pode gerar automaticamente debit memos (registrados em `CUSTOMER_TRX_ID`).
- `PROCESS_STATUS` controla o fluxo: registros com status ERROR devem ser investigados.
- A coluna `DISPLAY_FLAG` permite ocultar cobranças de teste ou canceladas.
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Late Charges and Finance Charges Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
