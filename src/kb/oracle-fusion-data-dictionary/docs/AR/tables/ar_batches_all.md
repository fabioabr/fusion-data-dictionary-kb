---
id: DOC-AR-023
doc_type: system-doc
title: "AR_BATCHES_ALL — Lotes de Recebimentos"
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
  - lotes-recebimentos
  - receipt-batches
  - batches
aliases:
  - AR_BATCHES_ALL
  - ar_batches_all
  - lotes-recebimentos-ar
  - receipt-batches
  - ar-batches
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_BATCHES_ALL

## 📌 Visão Geral

Armazena os **lotes de recebimentos** (receipt batches) do módulo Accounts Receivable. Cada registro representa um lote que agrupa múltiplos recebimentos para processamento conjunto — entrada manual em lote, importação via lockbox ou remessa bancária. Contém totais de controle (contagem e valor esperados vs. reais) para validação de integridade.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

**Nota:** Esta tabela é diferente de [[ra_batches_all]], que armazena lotes de *transações* (faturas). AR_BATCHES_ALL armazena lotes de *recebimentos*.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Entrada em lote:** Agrupamento de múltiplos recebimentos para digitação simultânea.
- **Lockbox:** Cada arquivo de lockbox importado gera um lote de recebimentos.
- **Controle de qualidade:** Validação de contagem e valor total do lote (controle vs. real).
- **Remessa bancária:** Lotes de recebimentos vinculados a um método e conta bancária.
- **Auditoria:** Rastreabilidade de quando e como os recebimentos foram registrados no sistema.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BATCH_ID | NUMBER(18) | NOT NULL | PK | Identificador único do lote de recebimentos | — | 🟢 100% |
| 2 | NAME | VARCHAR2(30) | NOT NULL | Identificação | Nome do lote | — | 🟢 100% |
| 3 | BATCH_DATE | DATE | NOT NULL | Data | Data do lote | — | 🟢 100% |
| 4 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status do lote (e.g., OP, CL) | — | 🟢 100% |
| 5 | TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do lote (MANUAL/LOCKBOX/REMITTANCE) | — | 🟢 100% |
| 6 | CONTROL_COUNT | NUMBER | NULL | Controle | Contagem esperada de recebimentos no lote | — | 🟢 100% |
| 7 | CONTROL_AMOUNT | NUMBER | NULL | Controle | Valor total esperado do lote | — | 🟢 100% |
| 8 | ACTUAL_COUNT | NUMBER | NULL | Controle | Contagem real de recebimentos no lote | — | 🟢 100% |
| 9 | ACTUAL_AMOUNT | NUMBER | NULL | Controle | Valor total real do lote | — | 🟢 100% |
| 10 | BATCH_SOURCE_ID | NUMBER(18) | NULL | Classificação | Fonte do lote | [[ra_batch_sources_all]] | 🟢 100% |
| 11 | RECEIPT_CLASS_ID | NUMBER(18) | NULL | Classificação | Classe do recebimento | — | 🟢 100% |
| 12 | RECEIPT_METHOD_ID | NUMBER(18) | NULL | Classificação | Método de recebimento | [[ar_receipt_methods]] | 🟢 100% |
| 13 | REMITTANCE_BANK_ACCOUNT_ID | NUMBER(18) | NULL | Bancário | Conta bancária de remessa | [[ce_bank_acct_uses_all]] | 🟢 100% |
| 14 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda do lote | — | 🟢 100% |
| 15 | EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio | — | 🟢 100% |
| 16 | EXCHANGE_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio | — | 🟢 100% |
| 17 | EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 100% |
| 18 | GL_DATE | DATE | NULL | Contabilidade | Data contábil padrão para recebimentos do lote | — | 🟢 100% |
| 19 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Comentários sobre o lote | — | 🟢 100% |
| 20 | LOCKBOX_ID | NUMBER(18) | NULL | Classificação | Identificador do lockbox de origem | — | 🟢 100% |
| 21 | LOCKBOX_BATCH_NAME | VARCHAR2(30) | NULL | Identificação | Nome do lote no lockbox | — | 🟡 75% |
| 22 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 23 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 24 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 25 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 26 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 27 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 28 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 29 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_batch_sources_all]] — via `BATCH_SOURCE_ID` (fonte de transação que originou o lote)
- [[ar_receipt_methods]] — via `RECEIPT_METHOD_ID` (método de recebimento)
- [[ce_bank_acct_uses_all]] — via `REMITTANCE_BANK_ACCOUNT_ID` (conta bancária de remessa do lote)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do lote de transações AR)

### Tabelas-filha (FK de saída)
- [[ar_cash_receipts_all]] — via `BATCH_ID` (recebimentos do lote, indireto via history)
- [[ar_cash_receipt_history_all]] — via `BATCH_ID` (histórico de recebimentos do lote)

---

## 📎 Uso Típico

### Lotes de recebimento com diferença de controle
```sql
SELECT b.NAME, b.BATCH_DATE, b.STATUS,
       b.CONTROL_COUNT, b.ACTUAL_COUNT,
       b.CONTROL_AMOUNT, b.ACTUAL_AMOUNT,
       b.CONTROL_AMOUNT - b.ACTUAL_AMOUNT AS diferenca
FROM   AR_BATCHES_ALL b
WHERE  b.CONTROL_AMOUNT <> b.ACTUAL_AMOUNT
  AND  b.ORG_ID = :p_org_id;
```

### Recebimentos de um lote
```sql
SELECT cr.RECEIPT_NUMBER, cr.AMOUNT, cr.RECEIPT_DATE, cr.STATUS
FROM   AR_CASH_RECEIPT_HISTORY_ALL crh
JOIN   AR_CASH_RECEIPTS_ALL cr ON cr.CASH_RECEIPT_ID = crh.CASH_RECEIPT_ID
WHERE  crh.BATCH_ID = :p_batch_id
  AND  crh.CURRENT_RECORD_FLAG = 'Y';
```

---

## 🔒 Observações

- **Não confundir** com [[ra_batches_all]], que armazena lotes de *transações* (faturas). Esta tabela (`AR_BATCHES_ALL`) armazena lotes de *recebimentos*.
- Os totais de controle (`CONTROL_COUNT`/`CONTROL_AMOUNT`) são inseridos pelo usuário; os reais (`ACTUAL_COUNT`/`ACTUAL_AMOUNT`) são calculados pelo sistema.
- Lotes de **lockbox** possuem `LOCKBOX_ID` preenchido, permitindo rastrear a origem da importação.
- O campo `RECEIPT_CLASS_ID` identifica a classe do recebimento (e.g., cheque, transferência, boleto).

---

## 📚 Referências

- [Oracle Docs — AR_BATCHES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arbatchesall-25065.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
