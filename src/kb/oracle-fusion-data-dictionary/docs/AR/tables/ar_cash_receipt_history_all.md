---
id: DOC-AR-018
doc_type: system-doc
title: "AR_CASH_RECEIPT_HISTORY_ALL — Histórico de Recebimentos"
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
  - historico-recebimentos
  - receipt-history
  - ciclo-vida
aliases:
  - AR_CASH_RECEIPT_HISTORY_ALL
  - ar_cash_receipt_history_all
  - historico-recebimentos-ar
  - cash-receipt-history
  - receipt-lifecycle
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_CASH_RECEIPT_HISTORY_ALL

## 📌 Visão Geral

Armazena o **histórico do ciclo de vida de cada recebimento** do módulo Accounts Receivable. Cada registro representa uma etapa na evolução do recebimento: criação, confirmação, remessa ao banco, compensação (clearing) e reversão. Permite rastrear a progressão completa de um receipt desde sua entrada até a baixa contábil.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Rastreamento de ciclo de vida:** Cada mudança de status do recebimento gera um novo registro, formando uma trilha de auditoria completa.
- **Contabilização:** Cada etapa pode gerar lançamentos contábeis — a coluna `POSTABLE_FLAG` identifica quais registros foram contabilizados.
- **Remessa bancária:** Rastreamento de quando o recebimento foi enviado ao banco e quando foi compensado.
- **Reversão:** Registro detalhado de reversões com data contábil específica.
- **Reconciliação GL:** Vinculação com combinação de contas contábeis via `ACCOUNT_CODE_COMBINATION_ID`.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CASH_RECEIPT_HISTORY_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de histórico | — | 🟢 100% |
| 2 | CASH_RECEIPT_ID | NUMBER(18) | NOT NULL | FK | Recebimento associado | [[ar_cash_receipts_all]] | 🟢 100% |
| 3 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status nesta etapa do ciclo (APPROVED/CONFIRMED/REMITTED/CLEARED/REVERSED) | — | 🟢 100% |
| 4 | TRX_DATE | DATE | NOT NULL | Data | Data da transação nesta etapa | — | 🟢 100% |
| 5 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor do recebimento nesta etapa | — | 🟢 100% |
| 6 | FACTOR_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se o recebimento foi fatorado (Y/N) | — | 🟢 100% |
| 7 | FIRST_POSTED_RECORD_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se é o primeiro registro contabilizado (Y/N) | — | 🟢 100% |
| 8 | POSTABLE_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se este registro gera lançamento contábil (Y/N) | — | 🟢 100% |
| 9 | GL_DATE | DATE | NULL | Contabilidade | Data contábil (General Ledger) | — | 🟢 100% |
| 10 | GL_POSTED_DATE | DATE | NULL | Contabilidade | Data em que foi efetivamente contabilizado no GL | — | 🟢 100% |
| 11 | POSTING_CONTROL_ID | NUMBER(18) | NULL | Contabilidade | ID do processo de posting que contabilizou | — | 🟢 100% |
| 12 | BATCH_ID | NUMBER(18) | NULL | Classificação | Lote de recebimentos associado | [[ar_batches_all]] | 🟢 100% |
| 13 | ACCOUNT_CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Combinação de contas contábeis (CCID) | [[gl_code_combinations]] | 🟢 100% |
| 14 | BANK_CHARGE_ACCOUNT_CCID | NUMBER(18) | NULL | Contabilidade | CCID para despesas bancárias | [[gl_code_combinations]] | 🟢 100% |
| 15 | REVERSAL_GL_DATE | DATE | NULL | Contabilidade | Data contábil da reversão | — | 🟢 100% |
| 16 | REVERSAL_POSTING_CONTROL_ID | NUMBER(18) | NULL | Contabilidade | ID do posting de reversão | — | 🟢 100% |
| 17 | CURRENT_RECORD_FLAG | VARCHAR2(1) | NULL | Status | Indica se é o registro mais recente do recebimento (Y/N) | — | 🟢 100% |
| 18 | EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio | [[gl_daily_conversion_types]] | 🟢 100% |
| 19 | EXCHANGE_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio aplicada | — | 🟢 100% |
| 20 | EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 100% |
| 21 | NOTE_STATUS | VARCHAR2(30) | NULL | Classificação | Status da nota promissória (bills receivable) | — | 🟡 70% |
| 22 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 23 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 24 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 25 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 26 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 27 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ar_cash_receipts_all]] — via `CASH_RECEIPT_ID` (recebimento principal)
- [[ar_batches_all]] — via `BATCH_ID` (lote de recebimentos)
- [[gl_code_combinations]] — via `ACCOUNT_CODE_COMBINATION_ID` (conta contábil do histórico de recebimento)
- [[gl_daily_conversion_types]] — via `EXCHANGE_RATE_TYPE` (tipo de câmbio do histórico de recebimento)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do histórico de recebimento)

### Tabelas-filha (FK de saída)
- [[ar_distributions_all]] — via `SOURCE_ID` onde `SOURCE_TABLE = 'CRH'` (distribuições contábeis)

---

## 📎 Uso Típico

### Histórico completo de um recebimento
```sql
SELECT crh.STATUS, crh.TRX_DATE, crh.AMOUNT,
       crh.GL_DATE, crh.POSTABLE_FLAG, crh.CURRENT_RECORD_FLAG
FROM   AR_CASH_RECEIPT_HISTORY_ALL crh
WHERE  crh.CASH_RECEIPT_ID = :p_cash_receipt_id
ORDER BY crh.CASH_RECEIPT_HISTORY_ID;
```

### Recebimentos compensados em um período
```sql
SELECT cr.RECEIPT_NUMBER, crh.TRX_DATE AS cleared_date, crh.AMOUNT
FROM   AR_CASH_RECEIPT_HISTORY_ALL crh
JOIN   AR_CASH_RECEIPTS_ALL cr ON cr.CASH_RECEIPT_ID = crh.CASH_RECEIPT_ID
WHERE  crh.STATUS = 'CLEARED'
  AND  crh.CURRENT_RECORD_FLAG = 'Y'
  AND  crh.TRX_DATE BETWEEN :start_date AND :end_date
  AND  crh.ORG_ID = :p_org_id;
```

### Filtros comuns
- `STATUS = 'APPROVED'` — Recebimentos aprovados
- `STATUS = 'CLEARED'` — Recebimentos compensados
- `CURRENT_RECORD_FLAG = 'Y'` — Apenas o registro mais recente
- `POSTABLE_FLAG = 'Y'` — Registros contabilizáveis

---

## 🔒 Observações

- Cada mudança de status gera um **novo registro** — a tabela nunca é atualizada in-place para manter a trilha de auditoria.
- O campo `CURRENT_RECORD_FLAG = 'Y'` identifica o registro mais recente; a coluna correspondente em [[ar_cash_receipts_all]] (`CASH_RECEIPT_HISTORY_ID`) também aponta para ele.
- Os status seguem a progressão: **APPROVED → CONFIRMED → REMITTED → CLEARED**. Reversões podem ocorrer em qualquer etapa.
- O `POSTING_CONTROL_ID = -3` indica registros **ainda não contabilizados** no GL.

---

## 📚 Referências

- [Oracle Docs — AR_CASH_RECEIPT_HISTORY_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arcashreceipthistoryall-25077.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
