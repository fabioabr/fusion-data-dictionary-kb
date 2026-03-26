---
id: DOC-AP-018
doc_type: system-doc
title: "AP_PAYMENT_HISTORY_ALL — Histórico de Eventos de Pagamento"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-payable
  - data-dictionary
  - historico-pagamento
  - payment-history
  - payment-events
aliases:
  - AP_PAYMENT_HISTORY_ALL
  - ap_payment_history_all
  - historico-pagamento-ap
  - payment-history-ap
  - eventos-pagamento
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_PAYMENT_HISTORY_ALL

## 📌 Visão Geral

Armazena o **histórico de eventos** de cada pagamento (check) do módulo Accounts Payable. Cada registro representa um evento no ciclo de vida do pagamento — criação, validação, compensação (clearing), anulação (void), reconciliação, stop — com data, valor e referências contábeis. Permite rastrear toda a evolução de um pagamento desde a emissão até a compensação bancária.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Ciclo de vida do pagamento:** Registro de cada transição de status (emissão → compensação → reconciliação).
- **Compensação bancária (clearing):** Evento de clearing registra quando o banco processou o pagamento.
- **Anulação de pagamentos (void):** Registro do evento de void com data e motivo.
- **Conciliação bancária:** Base para reconciliar pagamentos emitidos com extratos bancários.
- **Contabilização:** Cada evento pode gerar lançamentos contábeis distintos (ex: clearing cria lançamento de cash para accrual basis).
- **Auditoria:** Trilha completa de todos os eventos de pagamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAYMENT_HISTORY_ID | NUMBER(18) | NOT NULL | PK | Identificador único do evento de histórico | — | 🟢 100% |
| 2 | CHECK_ID | NUMBER(18) | NOT NULL | FK | Identificador do check/pagamento | [[ap_checks_all]] | 🟢 100% |
| 3 | TRANSACTION_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo do evento (PAYMENT CREATED/PAYMENT CLEARING/PAYMENT VOID/etc.) | — | 🟢 100% |
| 4 | ACCOUNTING_DATE | DATE | NOT NULL | Contabilidade | Data contábil do evento | — | 🟢 100% |
| 5 | TRX_BANK_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda do banco | — | 🟢 100% |
| 6 | TRX_PMT_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda do pagamento | — | 🟢 100% |
| 7 | TRX_BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda funcional (ledger) | — | 🟢 100% |
| 8 | ERRORS_BANK_AMOUNT | NUMBER | NULL | Financeiro | Valor de erro na moeda do banco | — | 🟡 75% |
| 9 | ERRORS_PMT_AMOUNT | NUMBER | NULL | Financeiro | Valor de erro na moeda do pagamento | — | 🟡 75% |
| 10 | ERRORS_BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor de erro na moeda funcional | — | 🟡 75% |
| 11 | CHARGES_BANK_AMOUNT | NUMBER | NULL | Financeiro | Encargos bancários na moeda do banco | — | 🟡 75% |
| 12 | CHARGES_PMT_AMOUNT | NUMBER | NULL | Financeiro | Encargos bancários na moeda do pagamento | — | 🟡 75% |
| 13 | CHARGES_BASE_AMOUNT | NUMBER | NULL | Financeiro | Encargos bancários na moeda funcional | — | 🟡 75% |
| 14 | MATCHED_FLAG | VARCHAR2(1) | NULL | Status | Indica se foi reconciliado com extrato (Y/N) | — | 🟢 100% |
| 15 | ACCOUNTING_EVENT_ID | NUMBER(18) | NULL | Contabilidade | Evento contábil do Subledger Accounting | [[xla_events]] | 🟢 100% |
| 16 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 17 | RELATED_EVENT_ID | NUMBER(18) | NULL | Referência cruzada | Evento relacionado (ex: clearing do payment) | [[ap_payment_history_all]] | 🟡 75% |
| 18 | HISTORICAL_FLAG | VARCHAR2(1) | NULL | Controle | Indica se é registro migrado/histórico (Y/N) | — | 🟡 70% |
| 19 | INVOICE_ADJUSTMENT_EVENT_ID | NUMBER(18) | NULL | Contabilidade | Evento de ajuste de fatura | [[xla_events]] | 🟡 70% |
| 20 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 21 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 22 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 23 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 24 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ap_checks_all]] — via `CHECK_ID` (pagamento/check)
- [[xla_events]] — via `ACCOUNTING_EVENT_ID` (evento contábil SLA)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do histórico de pagamento)

### Tabelas-filha (FK de saída)
- [[ap_payment_hist_dists]] — via `PAYMENT_HISTORY_ID` (distribuições do evento)
- [[ap_payment_history_all]] — via `RELATED_EVENT_ID` (auto-referência para eventos relacionados)

---

## 📎 Uso Típico

### Histórico de eventos de um pagamento
```sql
SELECT aph.TRANSACTION_TYPE, aph.ACCOUNTING_DATE,
       aph.TRX_PMT_AMOUNT, aph.MATCHED_FLAG
FROM   AP_PAYMENT_HISTORY_ALL aph
WHERE  aph.CHECK_ID = :p_check_id
ORDER BY aph.ACCOUNTING_DATE, aph.PAYMENT_HISTORY_ID;
```

### Pagamentos pendentes de clearing
```sql
SELECT ac.CHECK_NUMBER, ac.AMOUNT, aph.ACCOUNTING_DATE
FROM   AP_PAYMENT_HISTORY_ALL aph
JOIN   AP_CHECKS_ALL ac ON ac.CHECK_ID = aph.CHECK_ID
WHERE  aph.TRANSACTION_TYPE = 'PAYMENT CREATED'
  AND  NOT EXISTS (
    SELECT 1 FROM AP_PAYMENT_HISTORY_ALL aph2
    WHERE aph2.CHECK_ID = aph.CHECK_ID
      AND aph2.TRANSACTION_TYPE = 'PAYMENT CLEARING'
  )
  AND  aph.ORG_ID = :p_org_id;
```

### Filtros comuns
- `TRANSACTION_TYPE = 'PAYMENT CREATED'` — Criação do pagamento
- `TRANSACTION_TYPE = 'PAYMENT CLEARING'` — Compensação bancária
- `TRANSACTION_TYPE = 'PAYMENT VOID'` — Anulação do pagamento
- `MATCHED_FLAG = 'Y'` — Reconciliado com extrato

---

## 🔒 Observações

- O campo `TRANSACTION_TYPE` define o evento: **PAYMENT CREATED** (emissão), **PAYMENT CLEARING** (compensação), **PAYMENT VOID** (anulação), **PAYMENT MATURITY** (vencimento de letra), **PAYMENT UNCLEARING** (estorno de compensação).
- Cada evento pode gerar lançamentos contábeis via `ACCOUNTING_EVENT_ID` no Subledger Accounting ([[xla_events]]).
- As colunas `TRX_*_AMOUNT` armazenam o valor em três moedas: banco, pagamento e funcional.
- Os campos `ERRORS_*` e `CHARGES_*` capturam diferenças e encargos bancários identificados na reconciliação.
- A tabela é apenas de inserção (append-only) para garantir integridade da trilha de auditoria.

---

## 📚 Referências

- [Oracle Docs — AP_PAYMENT_HISTORY_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/appaymenthistoryall-25730.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
