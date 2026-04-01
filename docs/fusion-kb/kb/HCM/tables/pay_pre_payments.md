---
id: DOC-HCM-593
doc_type: system-doc
title: "PAY_PRE_PAYMENTS — Pre-Pagamentos"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - payroll
  - pre-payments
  - pre-pagamentos
  - pay-pre-payments
aliases:
  - PAY_PRE_PAYMENTS
  - pay_pre_payments
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_PRE_PAYMENTS

## 📌 Visão Geral

Armazena os **pre-pagamentos** gerados durante o processamento de folha. O pre-pagamento eh a etapa que calcula os valores liquidos a serem pagos por metodo de pagamento antes da geracao efetiva do pagamento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Calculo de valores liquidos por metodo de pagamento
- Preparacao de arquivos bancarios e cheques
- Reconciliacao entre valores brutos e liquidos
- Base para geracao de pagamentos efetivos

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PRE_PAYMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do pre-pagamento | --- | 🟢 90% |
| 2 | PAYROLL_REL_ACTION_ID | NUMBER(18) | NOT NULL | FK | ID da acao por relacionamento | PAY_PAYROLL_REL_ACTIONS | 🟢 85% |
| 3 | PERSONAL_PAYMENT_METHOD_ID | NUMBER(18) | NULL | FK | ID do metodo de pagamento pessoal | PAY_PERSON_PAY_METHODS_F | 🟢 85% |
| 4 | ORG_PAYMENT_METHOD_ID | NUMBER(18) | NULL | FK | ID do metodo de pagamento org | PAY_ORG_PAY_METHODS_F | 🟢 85% |
| 5 | VALUE | NUMBER | NULL | Dados | Valor do pre-pagamento | --- | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_payroll_rel_actions]] --- via `PAYROLL_REL_ACTION_ID` (ação de folha que gerou o pré-pagamento)
- [[pay_person_pay_methods_f]] --- via `PERSONAL_PAYMENT_METHOD_ID` (método pessoal de pagamento utilizado)
- [[pay_org_pay_methods_f]] --- via `ORG_PAYMENT_METHOD_ID` (método organizacional de pagamento utilizado)

### Tabelas-filha (FK de saída)
- [[pay_payment_costs]] --- via `PRE_PAYMENT_ID` (custos de pagamento do pré-pagamento)

---

## 📎 Uso Típico

### Pre-pagamentos de uma acao de folha
```sql
SELECT pp.PRE_PAYMENT_ID, pp.VALUE, pp.PERSONAL_PAYMENT_METHOD_ID
FROM   PAY_PRE_PAYMENTS pp
WHERE  pp.PAYROLL_REL_ACTION_ID = :p_rel_action_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[prepaymentcosting|PrePaymentCosting]] (GL · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BASE_CURRENCY_VALUE | PrePaymentBaseCurrencyValue | ✅ |
| CALC_BREAKDOWN_ID | PrePaymentCalcBreakdownId | — |
| EFFECTIVE_DATE | PrePaymentEffectiveDate | ✅ |
| ORG_PAYMENT_METHOD_ID | PrePaymentOrgPaymentMethodId | — |
| PAYEE_BANK_ACCOUNT_ID | PrePaymentPayeeBankAccountId | — |
| PAYEE_ORG_PAYMENT_METHOD_ID | PrePaymentPayeeOrgPaymentMethodId | — |
| PAYER_BANK_ACCOUNT_ID | PrePaymentPayerBankAccountId | — |
| PAYROLL_ACTION_ID | PrePaymentPayrollActionId | — |
| PAYROLL_REL_ACTION_ID | PrePaymentPayrollRelActionId | — |
| PERSONAL_PAYMENT_METHOD_ID | PrePaymentPersonalPaymentMethodId | — |
| PRE_PAYMENT_ID | PrePaymentPrePaymentId | — |
| SOURCE_ACTION_ID | PrePaymentSourceActionId | — |
| THIRD_PARTY_PAYEE_ID | PrePaymentThirdPartyPayeeId | — |
| VALUE | PrePaymentValue | — |

### [[prepayments|PrePayments]] (AP · BICC: 4/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BASE_CURRENCY_VALUE | PrePaymentBaseCurrencyValue | ✅ |
| CALC_BREAKDOWN_ID | PrePaymentCalcBreakdownId | — |
| EFFECTIVE_DATE | PrePaymentEffectiveDate | ✅ |
| ORG_PAYMENT_METHOD_ID | PrePaymentOrgPaymentMethodId | — |
| PAYEE_BANK_ACCOUNT_ID | PrePaymentPayeeBankAccountId | — |
| PAYEE_ORG_PAYMENT_METHOD_ID | PrePaymentPayeeOrgPaymentMethodId | — |
| PAYER_BANK_ACCOUNT_ID | PrePaymentPayerBankAccountId | — |
| PAYROLL_ACTION_ID | PrePaymentPayrollActionId | — |
| PAYROLL_REL_ACTION_ID | PrePaymentPayrollRelActionId | — |
| PERSONAL_PAYMENT_METHOD_ID | PrePaymentPersonalPaymentMethodId | — |
| PRE_PAYMENT_ID | PrePaymentPrePaymentId | ✅ |
| SOURCE_ACTION_ID | PrePaymentSourceActionId | — |
| THIRD_PARTY_PAYEE_ID | PrePaymentThirdPartyPayeeId | — |
| VALUE | PrePaymentValue | ✅ |

---

## 📚 Referências

- [Oracle Docs — PAY_PRE_PAYMENTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payprepayments.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
