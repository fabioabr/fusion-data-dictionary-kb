---
id: DOC-AP-032
doc_type: system-doc
title: "AP_TRIAL_BALANCES — Balancete de Verificação do Contas a Pagar"
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
  - balancete
  - trial-balance
  - contabilidade
aliases:
  - AP_TRIAL_BALANCES
  - ap_trial_balances
  - balancete-ap
  - ap-trial-balance
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_TRIAL_BALANCES

## 📌 Visão Geral

Armazena os dados do **balancete de verificação (Trial Balance)** do módulo Accounts Payable. Cada registro representa o saldo de um fornecedor ou invoice em uma data de corte específica, permitindo reconciliação entre o subledger AP e o General Ledger. Populada pelo processo de geração de balancete (AP Trial Balance Report).

> [!note] Geração periódica
> Os dados desta tabela são gerados por processo batch (relatório/programa concorrente). Não é alimentada transacionalmente em tempo real.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Reconciliação AP × GL:** Comparação de saldos do subledger AP contra contas contábeis do General Ledger.
- **Relatório de Trial Balance:** Geração do balancete de fornecedores por período contábil.
- **Análise de saldo por fornecedor:** Saldos em aberto por fornecedor, site e moeda.
- **Auditoria de fechamento:** Verificação dos saldos de contas a pagar no encerramento contábil.
- **Controle de aging:** Base para relatórios de envelhecimento de saldos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TRIAL_BALANCE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de balancete | — | 🟡 75% |
| 2 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers_v]] | 🟢 95% |
| 3 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor | [[poz_supplier_sites_all_m]] | 🟢 90% |
| 4 | INVOICE_ID | NUMBER(18) | NULL | FK | Identificador da fatura | [[ap_invoices_all]] | 🟢 95% |
| 5 | INVOICE_NUM | VARCHAR2(50) | NULL | Identificação | Número da fatura | — | 🟢 90% |
| 6 | INVOICE_DATE | DATE | NULL | Data | Data da fatura | — | 🟢 90% |
| 7 | INVOICE_AMOUNT | NUMBER | NULL | Financeiro | Valor original da fatura na moeda da transação | — | 🟢 95% |
| 8 | AMOUNT_REMAINING | NUMBER | NULL | Financeiro | Saldo em aberto na moeda da transação | — | 🟢 95% |
| 9 | INVOICE_CURRENCY_CODE | VARCHAR2(15) | NULL | Moeda | Código da moeda da fatura | — | 🟢 90% |
| 10 | ENTERED_AMOUNT_REMAINING | NUMBER | NULL | Financeiro | Saldo remanescente na moeda de entrada | — | 🟡 75% |
| 11 | ACCTD_AMOUNT_REMAINING | NUMBER | NULL | Financeiro | Saldo remanescente na moeda funcional | — | 🟡 75% |
| 12 | CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Combinação de contas contábeis (Liability Account) | [[gl_code_combinations]] | 🟢 90% |
| 13 | AS_OF_DATE | DATE | NULL | Data | Data de corte do balancete | — | 🟢 90% |
| 14 | ACCOUNTING_DATE | DATE | NULL | Contabilidade | Data contábil do lançamento | — | 🟢 85% |
| 15 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | Contabilidade | Identificador do ledger/set of books | [[gl_ledgers]] | 🟢 85% |
| 16 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 17 | PAYMENT_STATUS_FLAG | VARCHAR2(1) | NULL | Classificação | Status de pagamento (Y=pago, N=não pago, P=parcial) | — | 🟡 75% |
| 18 | DUE_DATE | DATE | NULL | Data | Data de vencimento da fatura | — | 🟢 90% |
| 19 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 20 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 21 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 22 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 23 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers_v]] — via `VENDOR_ID` (fornecedor do saldo no balancete de AP)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor)
- [[ap_invoices_all]] — via `INVOICE_ID` (fatura de origem)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (conta contábil de passivo)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil do balancete de AP)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do balancete de contas a pagar)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada — tabela de resultado de processo batch.

---

## 📎 Uso Típico

### Saldo em aberto por fornecedor em data de corte
```sql
SELECT tb.VENDOR_ID, SUM(tb.AMOUNT_REMAINING) AS saldo_aberto,
       tb.INVOICE_CURRENCY_CODE
FROM   AP_TRIAL_BALANCES tb
WHERE  tb.AS_OF_DATE = :p_as_of_date
  AND  tb.ORG_ID = :p_org_id
GROUP BY tb.VENDOR_ID, tb.INVOICE_CURRENCY_CODE;
```

### Faturas não pagas por fornecedor
```sql
SELECT tb.VENDOR_ID, tb.INVOICE_NUM, tb.INVOICE_DATE,
       tb.INVOICE_AMOUNT, tb.AMOUNT_REMAINING, tb.DUE_DATE
FROM   AP_TRIAL_BALANCES tb
WHERE  tb.PAYMENT_STATUS_FLAG = 'N'
  AND  tb.ORG_ID = :p_org_id
ORDER BY tb.DUE_DATE;
```

### Filtros comuns
- `AS_OF_DATE = :data_corte` — Balancete em data específica
- `PAYMENT_STATUS_FLAG = 'N'` — Faturas não pagas
- `AMOUNT_REMAINING > 0` — Registros com saldo em aberto

---

## 🔒 Observações

- Os dados são gerados por processo batch; não refletem transações em tempo real.
- A cada execução do programa de Trial Balance, registros anteriores podem ser substituídos ou adicionados conforme a data de corte (`AS_OF_DATE`).
- O campo `CODE_COMBINATION_ID` representa a **Liability Account** da fatura, permitindo reconciliação direta com [[gl_balances]].
- Para conciliação precisa, é necessário considerar faturas em múltiplas moedas e utilizar `ACCTD_AMOUNT_REMAINING` na moeda funcional.

---

## 🔗 PVOs Relacionados

### [[trialbalancepvo|TrialBalancePVO]] (AP · BICC: 12/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_CR | TrialBalanceAccountedCr | ✅ |
| ACCOUNTED_DR | TrialBalanceAccountedDr | ✅ |
| ACCOUNTING_CLASS_CODE | TrialBalanceAccountingClassCode | ✅ |
| ACCOUNTING_DATE | AccountingDate | ✅ |
| AE_HEADER_ID | AeHeaderId | ✅ |
| BUSINESS_UNIT_ID | TrialBalanceBusinessUnitId | — |
| CODE_COMBINATION_ID | TrialBalanceCodeCombinationId | ✅ |
| CREATED_BY | TrialBalanceCreatedBy | ✅ |
| CREATION_DATE | TrialBalanceCreationDate | ✅ |
| ENTERED_CR | TrialBalanceEnteredCr | ✅ |
| ENTERED_DR | TrialBalanceEnteredDr | ✅ |
| INVOICE_ID | InvoiceId | ✅ |
| JOB_DEFINITION_NAME | TrialBalanceJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | TrialBalanceJobDefinitionPackage | — |
| LAST_UPDATE_DATE | TrialBalanceLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TrialBalanceLastUpdateLogin | — |
| LAST_UPDATED_BY | TrialBalanceLastUpdatedBy | — |
| LEDGER_ID | TrialBalanceLedgerId | — |
| OBJECT_VERSION_NUMBER | TrialBalanceObjectVersionNumber | — |
| PARTY_ID | TrialBalancePartyId | — |
| PARTY_SITE_ID | TrialBalancePartySiteId | — |
| PROGRAM_APPLICATION_ID | TrialBalanceProgramApplicationId | — |
| PROGRAM_ID | TrialBalanceProgramId | — |
| PROGRAM_UPDATE_DATE | TrialBalanceProgramUpdateDate | — |
| REQUEST_ID | TrialBalanceRequestId | — |
| TRX_CURRENCY_CODE | TrialBalanceTrxCurrencyCode | — |
| VENDOR_ID | TrialBalanceVendorId | — |
| VENDOR_SITE_ID | TrialBalanceVendorSiteId | — |

---

## 📚 Referências

- [Oracle Docs — AP_TRIAL_BALANCES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/aptrialbalances.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
