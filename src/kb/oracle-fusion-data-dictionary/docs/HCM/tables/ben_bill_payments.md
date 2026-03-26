---
id: DOC-HCM-033
doc_type: system-doc
title: "BEN_BILL_PAYMENTS — Pagamentos de Benefícios (Billing)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - benefits
  - pagamentos
  - bill-payments
aliases:
  - BEN_BILL_PAYMENTS
  - ben_bill_payments
  - pagamentos-beneficios
  - bill-payments
  - ben-bill-payments
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_PAYMENTS

## 📌 Visão Geral

Armazena os **pagamentos consolidados** no sistema de billing de benefícios. Registro de lote de pagamentos processados.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Pagamentos de Benefícios (Billing).
- **Controle de cobranças:** Rastreamento de valores devidos e pagos.
- **Reconciliação:** Base para reconciliação financeira de benefícios.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BILL_PAYMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do pagamento | — | 🟢 90% |
| 2 | PAYMENT_BATCH_ID | NUMBER(18) | NULL | Referência | ID do lote de pagamento | — | 🟡 75% |
| 3 | TOTAL_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor total do pagamento | — | 🟢 85% |
| 4 | PAYMENT_DATE | DATE | NOT NULL | Data | Data do pagamento | — | 🟢 85% |
| 5 | PAYMENT_STATUS | VARCHAR2(30) | NULL | Classificação | Status (PROCESSED, PENDING, FAILED) | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada direta.

### Tabelas-filha (FK de saída)
- [[ben_bill_charge_payments]] — via `BILL_PAYMENT_ID` (cobranças pagas)

---

## 📎 Uso Típico

### Pagamentos por período
```sql
SELECT bp.BILL_PAYMENT_ID, bp.TOTAL_AMOUNT, bp.PAYMENT_DATE, bp.PAYMENT_STATUS
FROM   BEN_BILL_PAYMENTS bp
WHERE  bp.PAYMENT_DATE BETWEEN :start_date AND :end_date;
```

### Filtros comuns
- `PAYMENT_STATUS = 'PROCESSED'` — Pagamentos processados

---

## 🔒 Observações

- Registro consolidado de pagamentos de benefícios.
- Vinculado a cobranças individuais via `BEN_BILL_CHARGE_PAYMENTS`.

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_PAYMENTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillpayments.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
