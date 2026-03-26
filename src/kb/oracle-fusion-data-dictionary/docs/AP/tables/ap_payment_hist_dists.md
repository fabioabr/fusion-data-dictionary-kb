---
id: DOC-AP-019
doc_type: system-doc
title: "AP_PAYMENT_HIST_DISTS — Distribuições de Eventos de Pagamento"
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
  - distribuicoes-pagamento
  - payment-history-distributions
  - contabilidade
aliases:
  - AP_PAYMENT_HIST_DISTS
  - ap_payment_hist_dists
  - distribuicoes-pagamento-ap
  - payment-hist-dists
  - distribuicoes-evento-pagamento
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_PAYMENT_HIST_DISTS

## 📌 Visão Geral

Armazena as **distribuições contábeis** associadas a cada evento do histórico de pagamento em [[ap_payment_history_all]]. Cada registro vincula um evento de pagamento (criação, clearing, void) a uma distribuição de fatura em [[ap_invoice_distributions_all]], com os valores em múltiplas moedas (banco, pagamento, funcional). Fornece o detalhe necessário para contabilização no Subledger Accounting.

> [!note] Tabela de interseção
> Esta tabela é uma **tabela de interseção** entre o histórico de pagamento e as distribuições de fatura, permitindo rastrear como cada distribuição de fatura foi afetada por cada evento de pagamento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Contabilização detalhada:** Fornece o mapeamento entre eventos de pagamento e distribuições de fatura para geração de lançamentos no GL.
- **Clearing contábil:** Na compensação bancária, registra as distribuições que movem valores de "AP liability" para "cash clearing".
- **Reversão de pagamento:** Registra distribuições de reversão quando um pagamento é anulado (void).
- **Auditoria contábil:** Trilha completa do impacto contábil de cada evento de pagamento em nível de distribuição.
- **Reconciliação:** Base para verificar consistência entre valores de pagamento e valores contabilizados.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAYMENT_HIST_DIST_ID | NUMBER(18) | NOT NULL | PK | Identificador único da distribuição do evento | — | 🟢 100% |
| 2 | PAYMENT_HISTORY_ID | NUMBER(18) | NOT NULL | FK | Evento do histórico de pagamento | [[ap_payment_history_all]] | 🟢 100% |
| 3 | INVOICE_DISTRIBUTION_ID | NUMBER(18) | NOT NULL | FK | Distribuição da fatura associada | [[ap_invoice_distributions_all]] | 🟢 100% |
| 4 | INVOICE_PAYMENT_ID | NUMBER(18) | NULL | FK | Pagamento da fatura associado | [[ap_invoice_payments_all]] | 🟢 100% |
| 5 | PAY_DIST_LOOKUP_CODE | VARCHAR2(30) | NOT NULL | Classificação | Tipo da distribuição de pagamento (AP LIABILITY/CASH/AWT/etc.) | — | 🟢 100% |
| 6 | INVOICE_DIST_AMOUNT | NUMBER | NULL | Financeiro | Valor da distribuição da fatura | — | 🟢 100% |
| 7 | INVOICE_DIST_BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda funcional da distribuição da fatura | — | 🟢 100% |
| 8 | INVOICE_ADJ_AMOUNT | NUMBER | NULL | Financeiro | Valor de ajuste da fatura | — | 🟡 75% |
| 9 | INVOICE_ADJ_BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor de ajuste na moeda funcional | — | 🟡 75% |
| 10 | AMOUNT | NUMBER | NULL | Financeiro | Valor da distribuição na moeda do pagamento | — | 🟢 100% |
| 11 | BANK_CURR_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda do banco | — | 🟢 100% |
| 12 | CLEARED_BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor compensado na moeda funcional | — | 🟡 75% |
| 13 | PAID_BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor pago na moeda funcional | — | 🟢 100% |
| 14 | MATURED_BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor maturado na moeda funcional | — | 🟡 70% |
| 15 | ACCOUNTING_EVENT_ID | NUMBER(18) | NULL | Contabilidade | Evento contábil do Subledger Accounting | [[xla_events]] | 🟢 100% |
| 16 | REVERSAL_FLAG | VARCHAR2(1) | NULL | Status | Indica se é distribuição de reversão (Y/N) | — | 🟢 100% |
| 17 | REVERSED_PAYMENT_HIST_DIST_ID | NUMBER(18) | NULL | Referência cruzada | ID da distribuição original revertida | [[ap_payment_hist_dists]] | 🟢 100% |
| 18 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 19 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 20 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 21 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 22 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ap_payment_history_all]] — via `PAYMENT_HISTORY_ID` (evento de pagamento)
- [[ap_invoice_distributions_all]] — via `INVOICE_DISTRIBUTION_ID` (distribuição da fatura)
- [[ap_invoice_payments_all]] — via `INVOICE_PAYMENT_ID` (pagamento da fatura)
- [[xla_events]] — via `ACCOUNTING_EVENT_ID` (evento contábil SLA)

### Tabelas-filha (FK de saída)
- [[ap_payment_hist_dists]] — via `REVERSED_PAYMENT_HIST_DIST_ID` (auto-referência para reversões)

---

## 📎 Uso Típico

### Distribuições de um evento de pagamento
```sql
SELECT phd.PAY_DIST_LOOKUP_CODE, phd.AMOUNT,
       phd.PAID_BASE_AMOUNT, phd.REVERSAL_FLAG,
       aid.DIST_CODE_COMBINATION_ID
FROM   AP_PAYMENT_HIST_DISTS phd
JOIN   AP_INVOICE_DISTRIBUTIONS_ALL aid
  ON   aid.INVOICE_DISTRIBUTION_ID = phd.INVOICE_DISTRIBUTION_ID
WHERE  phd.PAYMENT_HISTORY_ID = :p_payment_history_id;
```

### Rastrear contabilização de um check
```sql
SELECT aph.TRANSACTION_TYPE, phd.PAY_DIST_LOOKUP_CODE,
       phd.AMOUNT, phd.PAID_BASE_AMOUNT
FROM   AP_PAYMENT_HIST_DISTS phd
JOIN   AP_PAYMENT_HISTORY_ALL aph ON aph.PAYMENT_HISTORY_ID = phd.PAYMENT_HISTORY_ID
WHERE  aph.CHECK_ID = :p_check_id
ORDER BY aph.ACCOUNTING_DATE, phd.PAYMENT_HIST_DIST_ID;
```

### Filtros comuns
- `PAY_DIST_LOOKUP_CODE = 'AP LIABILITY'` — Distribuições de liability
- `PAY_DIST_LOOKUP_CODE = 'CASH'` — Distribuições de caixa
- `REVERSAL_FLAG IS NULL` — Exclui reversões

---

## 🔒 Observações

- O campo `PAY_DIST_LOOKUP_CODE` classifica a natureza contábil: **AP LIABILITY** (passivo AP), **CASH** (caixa), **DISCOUNT** (desconto), **AWT** (withholding tax), **ROUNDING** (arredondamento), **EXCHANGE RATE VARIANCE** (variação cambial).
- A tabela vincula três entidades: evento de pagamento, distribuição de fatura e pagamento de fatura, formando a base para contabilização via Subledger Accounting.
- O campo `REVERSAL_FLAG = 'Y'` indica distribuição de reversão, com `REVERSED_PAYMENT_HIST_DIST_ID` apontando para a original.
- Os valores são armazenados em múltiplas moedas: moeda do pagamento (`AMOUNT`), moeda do banco (`BANK_CURR_AMOUNT`) e moeda funcional (`PAID_BASE_AMOUNT`).
- É tabela de alta volumetria — cada evento de pagamento gera múltiplas distribuições.

---

## 📚 Referências

- [Oracle Docs — AP_PAYMENT_HIST_DISTS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/appaymenthistdists-25734.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
