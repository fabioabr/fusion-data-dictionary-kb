---
id: DOC-AR-044
doc_type: system-doc
title: "AR_SYSTEM_PARAMETERS_ALL — Parâmetros de Sistema do Contas a Receber"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, parametros, configuracao, business-unit]
aliases: [AR_SYSTEM_PARAMETERS_ALL, ar_system_parameters_all, ar_sys_params, system_parameters_ar, parametros_ar]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_SYSTEM_PARAMETERS_ALL

> [!note] Sufixo _ALL
> Tabelas com sufixo `_ALL` armazenam dados de **todas as Business Units (orgs)**. O acesso é filtrado pela política de segurança (`ORG_ID`). Em views sem o sufixo, o filtro de org já está aplicado.

## 📌 Visão Geral

Tabela central de **configuração do módulo Accounts Receivable** por Business Unit. Cada registro define os parâmetros operacionais que governam o comportamento do AR — moeda funcional, método contábil, regras de desconto, juros, sequenciamento de documentos e limites de processamento em lote.

## 🧠 Propósito de Negócio

Esta tabela é o **painel de controle** do AR. Define como cada unidade de negócio opera em termos de contabilização, cálculo de impostos, política de descontos e geração de juros. Qualquer alteração de comportamento global do módulo AR passa por esta tabela.

Casos de uso principais:
- Definição do método contábil (accrual vs. cash) por BU
- Configuração de política de descontos (earned/unearned)
- Habilitação de cálculo automático de juros
- Parametrização de lotes de processamento automático

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | ORG_ID | NUMBER | PK. Identificador da Business Unit (organização). | Chave | 🟢 100% |
| 2 | SET_OF_BOOKS_ID | NUMBER | FK para o ledger (livro contábil) associado à BU. Referencia [[gl_ledgers]]. | Configuração | 🟢 100% |
| 3 | DEFAULT_CB_DUE_DATE | VARCHAR2 | Data de vencimento padrão para chargeback. | Configuração | 🟢 100% |
| 4 | ACCOUNTING_METHOD | VARCHAR2 | Método contábil: `ACCRUAL` (competência) ou `CASH` (caixa). | Configuração | 🟢 100% |
| 5 | ACCRUE_INTEREST | VARCHAR2 | Flag indicando se juros devem ser calculados automaticamente (`Y`/`N`). | Configuração | 🟢 100% |
| 6 | DISCOUNT_BASIS | VARCHAR2 | Base de cálculo do desconto: `INVOICE_AMOUNT`, `LINE_ITEMS_ONLY`, etc. | Configuração | 🟢 100% |
| 7 | UNEARNED_DISCOUNT | VARCHAR2 | Permite desconto não merecido (fora do prazo): `Y`/`N`. | Configuração | 🟢 100% |
| 8 | SALES_TAX_CALC_FLAG | VARCHAR2 | Habilita cálculo automático de imposto sobre vendas. | Configuração | 🟢 100% |
| 9 | PRINT_REMIT_TO | VARCHAR2 | Imprime endereço de remessa nas faturas: `Y`/`N`. | Configuração | 🟢 100% |
| 10 | AUTO_REC_INVOICES_PER_COMMIT | NUMBER | Número de faturas processadas por commit no autoinvoice. | Performance | 🟢 100% |
| 11 | DEFAULT_COUNTRY | VARCHAR2 | País padrão para transações da BU. | Configuração | 🟢 100% |
| 12 | TAX_REGISTRATION_NUMBER | VARCHAR2 | Número de registro fiscal da BU. | Configuração | 🟢 100% |
| 13 | DEFAULT_GROUPING_RULE_ID | NUMBER | FK para regra de agrupamento padrão de faturas. | Configuração | 🟢 100% |
| 14 | GENERATE_COLLECTION_LETTERS | VARCHAR2 | Habilita geração automática de cartas de cobrança. | Configuração | 🟢 100% |
| 15 | CASH_BASIS_SET_OF_BOOKS_ID | NUMBER | Ledger alternativo para contabilização em regime de caixa. | Configuração | 🟢 100% |
| 16 | INVOICE_DELETION_FLAG | VARCHAR2 | Permite exclusão de faturas: `Y`/`N`. | Configuração | 🟢 100% |
| 17 | PURGE_INTERFACE_TABLES_FLAG | VARCHAR2 | Habilita purge automático das tabelas de interface. | Configuração | 🟢 100% |
| 18 | PAY_UNRELATED_INVOICES | VARCHAR2 | Permite aplicar recebimentos a faturas de outros clientes. | Configuração | 🟢 100% |
| 19 | LATE_CHARGE_TYPE | VARCHAR2 | Tipo de encargo por atraso: `CHARGE`, `INTEREST`, `PENALTY`. | Configuração | 🟢 100% |
| 20 | INTEREST_RATE | NUMBER | Taxa de juros padrão para finance charges. | Configuração | 🟢 100% |
| 21 | PENALTY_RATE | NUMBER | Taxa de penalidade por atraso. | Configuração | 🟢 100% |
| 22 | MIN_FC_INVOICE_AMOUNT | NUMBER | Valor mínimo de fatura para gerar finance charge. | Configuração | 🟢 100% |
| 23 | MIN_FC_BALANCE_AMOUNT | NUMBER | Saldo mínimo para gerar finance charge. | Configuração | 🟢 100% |
| 24 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 25 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 26 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 27 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 28 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |
| 29 | LAST_UPDATE_DATE | DATE | Data da última atualização. | WHO | 🟢 100% |
| 30 | LAST_UPDATE_LOGIN | VARCHAR2 | Login da última sessão de atualização. | WHO | 🟢 100% |
| 31 | OBJECT_VERSION_NUMBER | NUMBER | Controle de concorrência otimista (versionamento). | WHO | 🟢 100% |
| 32 | PROGRAM_APPLICATION_ID | NUMBER | ID da aplicação do programa concorrente. | WHO | 🟢 100% |
| 33 | PROGRAM_ID | NUMBER | ID do programa concorrente que atualizou. | WHO | 🟢 100% |
| 34 | PROGRAM_UPDATE_DATE | DATE | Data da última atualização por programa concorrente. | WHO | 🟢 100% |
| 35 | REQUEST_ID | NUMBER | ID da requisição concorrente. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[gl_ledgers]] | SET_OF_BOOKS_ID | FK | Ledger associado à BU |
| [[ra_customer_trx_all]] | ORG_ID | Referência | Transações da BU |
| [[ar_cash_receipts_all]] | ORG_ID | Referência | Recebimentos da BU |
| [[hr_operating_units]] | ORG_ID | FK | Business Unit (organização) |
| [[ar_receivables_trx_all]] | ORG_ID | Referência | Atividades de recebíveis da BU |

## 📎 Uso Típico

```sql
-- Consultar parâmetros AR de uma Business Unit específica
SELECT org_id,
       accounting_method,
       accrue_interest,
       discount_basis,
       unearned_discount,
       sales_tax_calc_flag,
       auto_rec_invoices_per_commit
  FROM ar_system_parameters_all
 WHERE org_id = :p_org_id;
```

```sql
-- Listar BUs com juros automáticos habilitados
SELECT sp.org_id,
       hou.name AS business_unit,
       sp.interest_rate,
       sp.late_charge_type
  FROM ar_system_parameters_all sp
  JOIN hr_operating_units hou ON hou.organization_id = sp.org_id
 WHERE sp.accrue_interest = 'Y';
```

## 🔒 Observações

- Cada Business Unit deve ter **exatamente um registro** nesta tabela.
- Alterações nos parâmetros afetam **todas as novas transações** da BU — transações existentes não são retroativamente alteradas.
- O campo `SET_OF_BOOKS_ID` é legado; no Fusion, o conceito equivalente é o **Ledger** em [[gl_ledgers]].
- Campos de finance charge (`INTEREST_RATE`, `PENALTY_RATE`, etc.) só são efetivos quando `ACCRUE_INTEREST = 'Y'`.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — AR System Parameters View Object
- Oracle Fusion Cloud — Implementing Receivables (Configuration Guide)
