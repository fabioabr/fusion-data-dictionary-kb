---
id: DOC-AR-025
doc_type: system-doc
title: "AR_ADJUSTMENTS_ALL — Ajustes de Faturas"
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
  - ajustes
  - adjustments
  - write-offs
aliases:
  - AR_ADJUSTMENTS_ALL
  - ar_adjustments_all
  - ajustes-faturas-ar
  - ar-adjustments
  - write-offs-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_ADJUSTMENTS_ALL

## 📌 Visão Geral

Armazena os **ajustes de faturas** do módulo Accounts Receivable — write-offs (baixas), reclassificações contábeis e outros ajustes que alteram o saldo em aberto de transações. Cada registro representa um ajuste individual aplicado a uma fatura específica, com valor, tipo, status de aprovação e conta contábil de destino.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Write-offs:** Baixa de valores irrecuperáveis de faturas (total ou parcial).
- **Reclassificação contábil:** Transferência de valores entre contas contábeis sem alterar o saldo do cliente.
- **Ajustes de imposto/frete:** Correção de componentes específicos da fatura.
- **Aprovação de ajustes:** Controle de workflow de aprovação (automático ou manual).
- **Reconciliação AR × GL:** Rastreamento de ajustes que impactam o subledger e o General Ledger.
- **Auditoria:** Registro completo de motivo, comentário e associação com recebimentos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ADJUSTMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do ajuste | — | 🟢 100% |
| 2 | CUSTOMER_TRX_ID | NUMBER(18) | NOT NULL | FK | Transação (fatura) ajustada | [[ra_customer_trx_all]] | 🟢 100% |
| 3 | PAYMENT_SCHEDULE_ID | NUMBER(18) | NOT NULL | FK | Schedule de pagamento afetado | [[ar_payment_schedules_all]] | 🟢 100% |
| 4 | RECEIVABLES_TRX_ID | NUMBER(18) | NOT NULL | FK | Tipo de atividade de recebimento (define a conta contábil) | [[ar_receivables_trx_all]] | 🟢 100% |
| 5 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor do ajuste na moeda da transação | — | 🟢 100% |
| 6 | ACCTD_AMOUNT | NUMBER | NULL | Financeiro | Valor do ajuste na moeda funcional | — | 🟢 100% |
| 7 | TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo do ajuste: INVOICE, LINE, TAX, FREIGHT, CHARGES | — | 🟢 100% |
| 8 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status do ajuste: A (aprovado), R (rejeitado), W (pendente), M (pendente manual) | — | 🟢 100% |
| 9 | APPLY_DATE | DATE | NOT NULL | Data | Data de aplicação do ajuste | — | 🟢 100% |
| 10 | GL_DATE | DATE | NOT NULL | Contabilidade | Data contábil (General Ledger) | — | 🟢 100% |
| 11 | GL_POSTED_DATE | DATE | NULL | Contabilidade | Data em que foi contabilizado no GL | — | 🟢 100% |
| 12 | POSTING_CONTROL_ID | NUMBER(18) | NULL | Contabilidade | ID do processo de posting | — | 🟢 100% |
| 13 | CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Combinação de contas contábeis (CCID) | [[gl_code_combinations]] | 🟢 100% |
| 14 | REASON_CODE | VARCHAR2(30) | NULL | Classificação | Código do motivo do ajuste | — | 🟢 100% |
| 15 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Comentários sobre o ajuste | — | 🟢 100% |
| 16 | ASSOCIATED_CASH_RECEIPT_ID | NUMBER(18) | NULL | Referência cruzada | Recebimento associado (e.g., ajuste gerado por NSF) | [[ar_cash_receipts_all]] | 🟢 100% |
| 17 | CUSTOMER_TRX_LINE_ID | NUMBER(18) | NULL | FK | Linha específica da fatura ajustada (line-level) | [[ra_customer_trx_lines_all]] | 🟢 100% |
| 18 | SUBSEQUENT_TRX_ID | NUMBER(18) | NULL | Referência cruzada | Transação subsequente gerada pelo ajuste | [[ra_customer_trx_all]] | 🟡 70% |
| 19 | ADJUSTMENT_NUMBER | VARCHAR2(30) | NULL | Identificação | Número do ajuste visível ao usuário | — | 🟢 100% |
| 20 | DOC_SEQUENCE_ID | NUMBER(18) | NULL | Identificação | ID da sequência de documento | [[fnd_document_sequences]] | 🟢 100% |
| 21 | DOC_SEQUENCE_VALUE | NUMBER(15) | NULL | Identificação | Número de sequência de documento legal | — | 🟢 100% |
| 22 | CREATED_FROM | VARCHAR2(30) | NULL | Sistema | Origem da criação do ajuste (ARAPPRV/ARXTWADJ/etc.) | — | 🟢 100% |
| 23 | APPROVED_BY | NUMBER(18) | NULL | Aprovação | Usuário que aprovou o ajuste | — | 🟢 100% |
| 24 | LINE_ADJUSTED | NUMBER | NULL | Financeiro | Valor ajustado na linha | — | 🟢 100% |
| 25 | TAX_ADJUSTED | NUMBER | NULL | Financeiro | Valor ajustado no imposto | — | 🟢 100% |
| 26 | FREIGHT_ADJUSTED | NUMBER | NULL | Financeiro | Valor ajustado no frete | — | 🟢 100% |
| 27 | RECEIVABLES_CHARGES_ADJUSTED | NUMBER | NULL | Financeiro | Valor ajustado nas taxas | — | 🟢 100% |
| 28 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 29 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 30 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 31 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 32 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 33 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 34 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 35 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_customer_trx_all]] — via `CUSTOMER_TRX_ID` (transação ajustada)
- [[ar_payment_schedules_all]] — via `PAYMENT_SCHEDULE_ID` (schedule afetado)
- [[ar_receivables_trx_all]] — via `RECEIVABLES_TRX_ID` (tipo de atividade)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (conta contábil do ajuste de recebíveis)
- [[ra_customer_trx_lines_all]] — via `CUSTOMER_TRX_LINE_ID` (linha da fatura)
- [[ar_cash_receipts_all]] — via `ASSOCIATED_CASH_RECEIPT_ID` (recebimento associado)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do ajuste de recebíveis)

### Tabelas-filha (FK de saída)
- [[ar_distributions_all]] — via `SOURCE_ID` onde `SOURCE_TABLE = 'ADJ'` (distribuições contábeis)

---

## 📎 Uso Típico

### Ajustes aprovados por fatura
```sql
SELECT adj.ADJUSTMENT_NUMBER, adj.AMOUNT, adj.TYPE, adj.STATUS,
       adj.APPLY_DATE, adj.REASON_CODE, adj.COMMENTS
FROM   AR_ADJUSTMENTS_ALL adj
WHERE  adj.CUSTOMER_TRX_ID = :p_customer_trx_id
  AND  adj.STATUS = 'A';
```

### Total de write-offs por período
```sql
SELECT SUM(adj.AMOUNT) AS total_writeoff,
       COUNT(*) AS qtd_ajustes
FROM   AR_ADJUSTMENTS_ALL adj
WHERE  adj.STATUS = 'A'
  AND  adj.GL_DATE BETWEEN :start_date AND :end_date
  AND  adj.ORG_ID = :p_org_id;
```

### Filtros comuns
- `STATUS = 'A'` — Ajustes aprovados
- `STATUS = 'W'` — Ajustes pendentes de aprovação
- `TYPE = 'INVOICE'` — Ajustes a nível de fatura
- `TYPE = 'LINE'` — Ajustes a nível de linha

---

## 🔒 Observações

- O campo `STATUS` controla o workflow: **A** (aprovado), **R** (rejeitado), **W** (pendente workflow automático), **M** (pendente aprovação manual).
- O `TYPE` determina em que nível o ajuste é aplicado: **INVOICE** (toda a fatura), **LINE** (linha específica), **TAX** (imposto), **FREIGHT** (frete), **CHARGES** (encargos).
- Os campos `LINE_ADJUSTED`, `TAX_ADJUSTED`, `FREIGHT_ADJUSTED`, `RECEIVABLES_CHARGES_ADJUSTED` detalham como o valor total foi distribuído entre componentes.
- Ajustes gerados automaticamente por NSF (insuficiência de fundos) preenchem `ASSOCIATED_CASH_RECEIPT_ID`.
- O `POSTING_CONTROL_ID = -3` indica ajustes **ainda não contabilizados** no GL.

---

## 📚 Referências

- [Oracle Docs — AR_ADJUSTMENTS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/aradjustmentsall-10034.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
