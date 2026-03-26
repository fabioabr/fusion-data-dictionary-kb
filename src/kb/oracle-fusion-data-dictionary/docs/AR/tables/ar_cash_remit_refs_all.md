---
id: DOC-AR-019
doc_type: system-doc
title: "AR_CASH_REMIT_REFS_ALL — Referências de Remessa de Recebimentos"
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
  - remessa
  - remittance-references
  - receipts
aliases:
  - AR_CASH_REMIT_REFS_ALL
  - ar_cash_remit_refs_all
  - referencias-remessa-ar
  - cash-remit-refs
  - remittance-references
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_CASH_REMIT_REFS_ALL

## 📌 Visão Geral

Armazena as **referências de remessa** associadas a recebimentos no módulo Accounts Receivable. Cada registro vincula um recebimento a uma referência bancária de remessa, permitindo rastreabilidade entre o receipt e a conta bancária de destino. Utilizada principalmente em processos de remessa automática e reconciliação bancária.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Rastreamento de remessas:** Vincula cada recebimento à referência bancária de remessa correspondente.
- **Reconciliação bancária:** Permite identificar quais recebimentos foram enviados a qual conta bancária.
- **Auditoria de pagamentos:** Fornece a referência de remessa para rastreabilidade completa do fluxo de caixa.
- **Integração bancária:** Suporte a processos automatizados de envio de remessas ao banco.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CASH_REMIT_REF_ID | NUMBER(18) | NOT NULL | PK | Identificador único da referência de remessa | — | 🟢 100% |
| 2 | CASH_RECEIPT_ID | NUMBER(18) | NOT NULL | FK | Recebimento associado | [[ar_cash_receipts_all]] | 🟢 100% |
| 3 | RECEIPT_REFERENCE | VARCHAR2(240) | NULL | Identificação | Referência de remessa bancária | — | 🟢 100% |
| 4 | REMIT_BANK_ACCT_USE_ID | NUMBER(18) | NULL | Bancário | Conta bancária de remessa utilizada | [[ce_bank_acct_uses_all]] | 🟢 100% |
| 5 | CUSTOMER_BANK_ACCOUNT_ID | NUMBER(18) | NULL | Bancário | Conta bancária do cliente | — | 🟢 100% |
| 6 | RECEIPT_DATE | DATE | NULL | Data | Data do recebimento na referência | — | 🟡 75% |
| 7 | AMOUNT | NUMBER | NULL | Financeiro | Valor da referência de remessa | — | 🟡 75% |
| 8 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda | — | 🟡 75% |
| 9 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 14 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 15 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 16 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ar_cash_receipts_all]] — via `CASH_RECEIPT_ID` (recebimento principal)
- [[ce_bank_acct_uses_all]] — via `REMIT_BANK_ACCT_USE_ID` (conta bancária de remessa)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da referência de remessa)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha direta conhecida.

---

## 📎 Uso Típico

### Referências de remessa de um recebimento
```sql
SELECT crr.RECEIPT_REFERENCE, crr.REMIT_BANK_ACCT_USE_ID, crr.AMOUNT
FROM   AR_CASH_REMIT_REFS_ALL crr
WHERE  crr.CASH_RECEIPT_ID = :p_cash_receipt_id;
```

### Recebimentos com referência de remessa por período
```sql
SELECT cr.RECEIPT_NUMBER, crr.RECEIPT_REFERENCE, cr.AMOUNT
FROM   AR_CASH_REMIT_REFS_ALL crr
JOIN   AR_CASH_RECEIPTS_ALL cr ON cr.CASH_RECEIPT_ID = crr.CASH_RECEIPT_ID
WHERE  cr.RECEIPT_DATE BETWEEN :start_date AND :end_date
  AND  crr.ORG_ID = :p_org_id;
```

---

## 🔒 Observações

- Tabela complementar a [[ar_cash_receipts_all]] — nem todo recebimento terá registros aqui; depende do método de recebimento e do processo de remessa.
- Utilizada intensamente em integrações com **lockbox** e processos de **remessa automática**.
- O campo `REMIT_BANK_ACCT_USE_ID` referencia a conta bancária de uso no Cash Management.

---

## 📚 Referências

- [Oracle Docs — AR_CASH_REMIT_REFS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arcashremitrefsall-25079.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
