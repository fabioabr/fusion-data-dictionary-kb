---
id: DOC-AP-026
doc_type: system-doc
title: "AP_SYSTEM_PARAMETERS_ALL — Parâmetros de Sistema do Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, parametros-sistema, configuracao, setup-ap]
aliases: [AP_SYSTEM_PARAMETERS_ALL, ap_system_parameters_all, system_params_ap, parametros_sistema_ap, config_ap]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_SYSTEM_PARAMETERS_ALL

## Visão Geral

Tabela central de configuração do módulo Accounts Payable no Oracle Fusion. Armazena os parâmetros de sistema por business unit (Operating Unit), incluindo contas contábeis padrão, regras de validação, opções de pagamento, tolerâncias de matching e demais configurações que governam o comportamento do módulo AP.

## Propósito de Negócio

Define o comportamento padrão do módulo AP para cada unidade de negócio. É essencial para: (1) configuração de contas contábeis padrão (liability, prepayment, discount, etc.), (2) definição de regras de matching e tolerâncias, (3) controle de numeração automática de faturas e pagamentos, (4) integração com outros módulos (GL, PO, iExpenses), (5) auditoria de configuração e troubleshooting.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ORG_ID | NUMBER(15) | NOT NULL | PK/Partição | Chave primária. Identificador da business unit (Operating Unit). | — | 🟢 100% |
| 2 | SET_OF_BOOKS_ID | NUMBER(15) | NOT NULL | FK | FK para GL_LEDGERS. Ledger associado à business unit. | — | 🟢 100% |
| 3 | ACCTS_PAY_CODE_COMBINATION_ID | NUMBER(15) | NULL | FK | FK para [[gl_code_combinations]]. Conta padrão de contas a pagar (liability). | [[gl_code_combinations]] | 🟢 100% |
| 4 | PREPAY_CODE_COMBINATION_ID | NUMBER(15) | NULL | FK | FK para [[gl_code_combinations]]. Conta padrão de pré-pagamentos. | [[gl_code_combinations]] | 🟢 95% |
| 5 | DISCOUNT_CODE_COMBINATION_ID | NUMBER(15) | NULL | FK | FK para [[gl_code_combinations]]. Conta padrão de descontos obtidos. | [[gl_code_combinations]] | 🟢 95% |
| 6 | FUTURE_DATED_PMT_CCID | NUMBER(15) | NULL | FK | FK para [[gl_code_combinations]]. Conta de pagamentos futuros. | [[gl_code_combinations]] | 🟡 80% |
| 7 | AUTO_TAX_CALC_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se cálculo automático de impostos está ativo (Y/N). | — | 🟢 90% |
| 8 | MATCH_OPTION | VARCHAR2(25) | NULL | Configuração | Opção de matching padrão (PURCHASE_ORDER, RECEIPT). | — | 🟢 90% |
| 9 | BASE_CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Financeiro | Moeda funcional da business unit (ex.: BRL). | — | 🟢 100% |
| 10 | PAYMENT_METHOD_CODE | VARCHAR2(30) | NULL | Configuração | Método de pagamento padrão. | — | 🟡 75% |
| 11 | TERMS_ID | NUMBER(15) | NULL | FK | FK para [[ap_terms_b]]. Condição de pagamento padrão. | [[ap_terms_b]] | 🟢 90% |
| 12 | GL_DATE_FROM_RECEIPT_FLAG | VARCHAR2(1) | NULL | Configuração | Herdar data GL do recebimento (Y/N). | — | 🟡 70% |
| 13 | INVOICE_CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda padrão para criação de faturas. | — | 🟡 75% |
| 14 | APPROVAL_WORKFLOW_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se workflow de aprovação está ativo (Y/N). | — | 🟢 85% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 16 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[gl_code_combinations]]** — Contas contábeis padrão (N:1 via múltiplos CCIDs).
- **[[ap_terms_b]]** — Condição de pagamento padrão (N:1 via `TERMS_ID`).

### Tabelas-filha

- Nenhuma tabela-filha direta (tabela de configuração referenciada por todo o módulo AP).

## Uso Típico

```sql
-- Configuração AP de todas as business units
SELECT asp.ORG_ID,
       asp.BASE_CURRENCY_CODE,
       gcc_liab.CONCATENATED_SEGMENTS AS conta_liability,
       gcc_prep.CONCATENATED_SEGMENTS AS conta_prepay,
       asp.MATCH_OPTION,
       asp.AUTO_TAX_CALC_FLAG,
       asp.APPROVAL_WORKFLOW_FLAG
  FROM AP_SYSTEM_PARAMETERS_ALL asp
  LEFT JOIN GL_CODE_COMBINATIONS gcc_liab
    ON gcc_liab.CODE_COMBINATION_ID = asp.ACCTS_PAY_CODE_COMBINATION_ID
  LEFT JOIN GL_CODE_COMBINATIONS gcc_prep
    ON gcc_prep.CODE_COMBINATION_ID = asp.PREPAY_CODE_COMBINATION_ID
 ORDER BY asp.ORG_ID;
```

## Observações

- Existe um registro por `ORG_ID` — a tabela é particionada por business unit.
- As contas contábeis definidas aqui são defaults; podem ser sobrescritas em nível de fornecedor, site ou fatura.
- Alterações nesta tabela impactam o comportamento de todo o módulo AP para a business unit.
- Estrutura análoga a [[ar_system_parameters_all]] do módulo AR.
- Consultar esta tabela para troubleshooting de configuração e validação de setup.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — AP System Parameters Setup Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).

---

## 🔗 PVOs Relacionados

### [[disbursementheaderpvo|DisbursementHeaderPVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | SystemOptionObjectVersionNumber | — |
| ORG_ID | SystemOptionOrgId | — |
| WHEN_TO_ACCOUNT_PMT | SystemOptionWhenToAccountPmt | ✅ |

### [[disbursementhistoryheaderpvo|DisbursementHistoryHeaderPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | SystemOptionObjectVersionNumber | — |
| ORG_ID | SystemOptionOrgId | — |
| WHEN_TO_ACCOUNT_PMT | SystemOptionWhenToAccountPmt | — |

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | SystemOptionObjectVersionNumber | — |
| ORG_ID | SystemOptionOrgId | — |
| WHEN_TO_ACCOUNT_PMT | SystemOptionWhenToAccountPmt | ✅ |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | SystemOptionLastUpdateDate | ✅ |
| OBJECT_VERSION_NUMBER | SystemOptionObjectVersionNumber | — |
| ORG_ID | SystemOptionOrgId | — |
| WHEN_TO_ACCOUNT_PMT | SystemOptionWhenToAccountPmt | ✅ |
