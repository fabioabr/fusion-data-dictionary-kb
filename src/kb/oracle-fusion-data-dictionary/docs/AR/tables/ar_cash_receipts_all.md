---
id: DOC-AR-017
doc_type: system-doc
title: "AR_CASH_RECEIPTS_ALL — Recebimentos (Receipts)"
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
  - recebimentos
  - receipts
  - cash-receipts
aliases:
  - AR_CASH_RECEIPTS_ALL
  - ar_cash_receipts_all
  - recebimentos-ar
  - cash-receipts
  - receipts-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_CASH_RECEIPTS_ALL

## 📌 Visão Geral

Armazena um registro para **cada recebimento** (receipt) do módulo Accounts Receivable. Cada linha representa um recebimento individual, contendo valor, moeda, data, status do ciclo de vida (APP, UNAPP, UNID, NSF, REV, STOP) e referência ao cliente pagador. É a tabela central para rastreamento de todos os recebimentos de caixa, sejam eles manuais, automáticos ou importados via interface.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de recebimentos:** Cada pagamento recebido de clientes gera um registro nesta tabela, incluindo recebimentos manuais, automáticos e por lockbox.
- **Controle de status:** Rastreamento do ciclo de vida do recebimento — aplicado, não-aplicado, não-identificado, NSF, revertido ou parado.
- **Conciliação bancária:** Vinculação de recebimentos a contas bancárias de remessa para reconciliação.
- **Aging de recebimentos:** Base para análise de recebimentos não-aplicados por faixa de data.
- **Auditoria e compliance:** Rastreabilidade completa de cada recebimento com sequência de documento e WHO columns.
- **Câmbio:** Suporte a recebimentos em moeda estrangeira com taxa de conversão.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CASH_RECEIPT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do recebimento | — | 🟢 100% |
| 2 | RECEIPT_NUMBER | VARCHAR2(30) | NOT NULL | Identificação | Número do recebimento visível ao usuário | — | 🟢 100% |
| 3 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor do recebimento na moeda da transação | — | 🟢 100% |
| 4 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Financeiro | Código da moeda do recebimento (ISO 4217) | — | 🟢 100% |
| 5 | RECEIPT_DATE | DATE | NOT NULL | Data | Data do recebimento | — | 🟢 100% |
| 6 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status do recebimento (APP/UNAPP/UNID/NSF/REV/STOP) | — | 🟢 100% |
| 7 | TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do recebimento (CASH/MISC) | — | 🟢 100% |
| 8 | PAY_FROM_CUSTOMER | NUMBER(18) | NULL | Cliente | Conta do cliente pagador | [[hz_cust_accounts]] | 🟢 100% |
| 9 | CUSTOMER_SITE_USE_ID | NUMBER(18) | NULL | Cliente | Site de uso do cliente | [[hz_cust_site_uses_all]] | 🟢 100% |
| 10 | RECEIPT_METHOD_ID | NUMBER(18) | NOT NULL | Classificação | Método de recebimento utilizado | [[ar_receipt_methods]] | 🟢 100% |
| 11 | REMITTANCE_BANK_ACCOUNT_ID | NUMBER(18) | NULL | Bancário | Conta bancária de remessa | [[ce_bank_acct_uses_all]] | 🟢 100% |
| 12 | DOC_SEQUENCE_ID | NUMBER(18) | NULL | Identificação | ID da sequência de documento | [[fnd_document_sequences]] | 🟢 100% |
| 13 | DOC_SEQUENCE_VALUE | NUMBER(15) | NULL | Identificação | Número de sequência de documento legal | — | 🟢 100% |
| 14 | EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio | [[gl_daily_conversion_types]] | 🟢 100% |
| 15 | EXCHANGE_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio aplicada | — | 🟢 100% |
| 16 | EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 100% |
| 17 | DEPOSIT_DATE | DATE | NULL | Data | Data do depósito bancário | — | 🟢 100% |
| 18 | GL_DATE | DATE | NULL | Contabilidade | Data contábil (General Ledger) | — | 🟢 100% |
| 19 | REVERSAL_DATE | DATE | NULL | Data | Data de reversão do recebimento | — | 🟢 100% |
| 20 | REVERSAL_REASON_CODE | VARCHAR2(30) | NULL | Classificação | Motivo da reversão | — | 🟢 100% |
| 21 | REVERSAL_CATEGORY | VARCHAR2(30) | NULL | Classificação | Categoria da reversão (NSF/DEBIT/REV) | — | 🟢 100% |
| 22 | CASH_RECEIPT_HISTORY_ID | NUMBER(18) | NULL | Referência cruzada | Registro atual do histórico | [[ar_cash_receipt_history_all]] | 🟢 100% |
| 23 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Comentários livres sobre o recebimento | — | 🟢 100% |
| 24 | CUSTOMER_RECEIPT_REFERENCE | VARCHAR2(30) | NULL | Referência externa | Referência do cliente para o pagamento | — | 🟢 100% |
| 25 | ANTICIPATED_CLEARING_DATE | DATE | NULL | Data | Data prevista de compensação | — | 🟢 100% |
| 26 | CONFIRMED_FLAG | VARCHAR2(1) | NULL | Status | Indica se recebimento foi confirmado (Y/N) | — | 🟢 100% |
| 27 | OVERRIDE_REMIT_ACCOUNT_FLAG | VARCHAR2(1) | NULL | Controle | Conta de remessa sobrescrita manualmente (Y/N) | — | 🟡 75% |
| 28 | MISC_PAYMENT_SOURCE | VARCHAR2(30) | NULL | Classificação | Origem de recebimentos avulsos | — | 🟢 100% |
| 29 | DISTRIBUTION_SET_ID | NUMBER(18) | NULL | Contabilidade | Conjunto de distribuição para misc receipts | [[ar_distribution_sets_all]] | 🟢 100% |
| 30 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 31 | LEGAL_ENTITY_ID | NUMBER(18) | NULL | Multi-Org | Entidade legal | [[xle_entity_profiles]] | 🟢 100% |
| 32 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 33 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 34 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 35 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 36 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 37 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 38 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 39 | GLOBAL_ATTRIBUTE1–20 | VARCHAR2(150) | NULL | DFF | Atributos globais (localizações por país) | — | 🟢 100% |
| 40 | GLOBAL_ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Global Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hz_cust_accounts]] — via `PAY_FROM_CUSTOMER` (cliente pagador)
- [[hz_cust_site_uses_all]] — via `CUSTOMER_SITE_USE_ID` (site do cliente)
- [[ar_receipt_methods]] — via `RECEIPT_METHOD_ID` (método de recebimento)
- [[ce_bank_acct_uses_all]] — via `REMITTANCE_BANK_ACCOUNT_ID` (conta bancária de depósito do recebimento)
- [[ar_distribution_sets_all]] — via `DISTRIBUTION_SET_ID` (distribuição para misc receipts)
- [[gl_daily_conversion_types]] — via `EXCHANGE_RATE_TYPE` (tipo de câmbio aplicado ao recebimento)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do recebimento de caixa)
- [[xle_entity_profiles]] — via `LEGAL_ENTITY_ID` (entidade legal do recebimento de caixa)

### Tabelas-filha (FK de saída)
- [[ar_cash_receipt_history_all]] — via `CASH_RECEIPT_ID` (histórico do recebimento)
- [[ar_receivable_applications_all]] — via `CASH_RECEIPT_ID` (aplicações de recebimento contra faturas ou contas)
- [[ar_payment_schedules_all]] — via `CASH_RECEIPT_ID` (schedule de pagamento)
- [[ar_misc_cash_distributions_all]] — via `CASH_RECEIPT_ID` (distribuições de misc receipts)
- [[ar_cash_remit_refs_all]] — via `CASH_RECEIPT_ID` (referências de remessa)

---

## 📎 Uso Típico

### Listar recebimentos não-aplicados
```sql
SELECT cr.RECEIPT_NUMBER, cr.AMOUNT, cr.CURRENCY_CODE,
       cr.RECEIPT_DATE, cr.STATUS
FROM   AR_CASH_RECEIPTS_ALL cr
WHERE  cr.STATUS = 'UNAPP'
  AND  cr.ORG_ID = :p_org_id;
```

### Recebimentos com dados do cliente
```sql
SELECT cr.RECEIPT_NUMBER, cr.AMOUNT, cr.RECEIPT_DATE,
       hca.ACCOUNT_NUMBER, hca.ACCOUNT_NAME
FROM   AR_CASH_RECEIPTS_ALL cr
JOIN   HZ_CUST_ACCOUNTS hca ON hca.CUST_ACCOUNT_ID = cr.PAY_FROM_CUSTOMER
WHERE  cr.RECEIPT_DATE BETWEEN :start_date AND :end_date
  AND  cr.ORG_ID = :p_org_id;
```

### Filtros comuns
- `STATUS = 'APP'` — Recebimentos aplicados
- `STATUS = 'UNAPP'` — Recebimentos não-aplicados
- `TYPE = 'CASH'` — Apenas recebimentos de caixa (exclui misc)
- `RECEIPT_DATE BETWEEN :start AND :end` — Período

---

## 🔒 Observações

- O campo `STATUS` controla o ciclo de vida: **APP** (aplicado), **UNAPP** (não-aplicado), **UNID** (não-identificado), **NSF** (sem fundos), **REV** (revertido), **STOP** (parado).
- Recebimentos do tipo **MISC** (avulsos) utilizam `DISTRIBUTION_SET_ID` para contabilização direta, sem vinculação a faturas.
- A coluna `CASH_RECEIPT_HISTORY_ID` aponta para o registro **mais recente** do histórico em [[ar_cash_receipt_history_all]].
- Campos `REVERSAL_*` são preenchidos apenas quando o recebimento é revertido.
- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.

---

## 📚 Referências

- [Oracle Docs — AR_CASH_RECEIPTS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arcashreceiptsall-10044.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
