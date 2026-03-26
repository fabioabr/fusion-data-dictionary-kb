---
id: DOC-AR-035
doc_type: system-doc
title: "AR_DISPUTE_HISTORY — Histórico de Disputas de Faturas"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, disputas, historico, cobranca]
aliases: [AR_DISPUTE_HISTORY, ar_dispute_history, dispute_history, historico_disputas, disputas_ar]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_DISPUTE_HISTORY

## 📌 Visão Geral

Tabela que registra o histórico completo de disputas de faturas no Accounts Receivable. Cada registro documenta quando um valor em disputa foi criado, alterado ou resolvido, incluindo motivo, comentários e datas do ciclo de vida da disputa.

## 🧠 Propósito de Negócio

Disputas ocorrem quando clientes contestam valores cobrados. O histórico de disputas é essencial para: (1) acompanhar o ciclo de vida de cada contestação, (2) calcular provisões para perdas, (3) medir SLA de resolução, (4) fornecer evidências para auditoria. A rastreabilidade completa do processo de disputa é um requisito regulatório para instituições financeiras.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | DISPUTE_HISTORY_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único do registro de disputa. | PK | 🟢 100% |
| 2 | PAYMENT_SCHEDULE_ID | NUMBER(15) | NOT NULL | FK para AR_PAYMENT_SCHEDULES_ALL. Parcela em disputa. | FK | 🟢 100% |
| 3 | CUSTOMER_TRX_ID | NUMBER(15) | NOT NULL | Identificador da transação (fatura) associada. | FK | 🟢 100% |
| 4 | AMOUNT_IN_DISPUTE | NUMBER | NOT NULL | Valor em disputa na moeda da transação. | Financeiro | 🟢 100% |
| 5 | DISPUTE_DATE | DATE | NOT NULL | Data em que a disputa foi registrada. | Temporal | 🟢 100% |
| 6 | START_DATE | DATE | NULL | Data de início efetivo da disputa. | Temporal | 🟢 100% |
| 7 | END_DATE | DATE | NULL | Data de encerramento/resolução da disputa. | Temporal | 🟢 100% |
| 8 | REASON_CODE | VARCHAR2(30) | NULL | Código do motivo da disputa (lookup). | Classificação | 🟢 100% |
| 9 | COMMENTS | VARCHAR2(240) | NULL | Comentários livres sobre a disputa. | Negócio | 🟢 100% |
| 10 | STATUS | VARCHAR2(30) | NULL | Status da disputa (ex.: OPEN, CLOSED, PENDING). | Controle | 🟢 100% |
| 11 | CURRENT_RECORD_FLAG | VARCHAR2(1) | NULL | Indica se é o registro mais recente da disputa (Y/N). | Controle | 🟢 100% |
| 12 | UNDER_DISPUTE_FLAG | VARCHAR2(1) | NULL | Flag indicando se o valor ainda está em disputa. | Controle | 🟢 100% |
| 13 | ACCTD_AMOUNT_IN_DISPUTE | NUMBER | NULL | Valor em disputa na moeda funcional (contábil). | Financeiro | 🟢 100% |
| 14 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 16 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 18 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **AR_PAYMENT_SCHEDULES_ALL** — Parcela em disputa (N:1 via `PAYMENT_SCHEDULE_ID`).
- **RA_CUSTOMER_TRX_ALL** — Transação/fatura associada (N:1 via `CUSTOMER_TRX_ID`).
- **[[ar_collectors]]** — Cobrador responsável (via perfil do cliente na transação).

## 📎 Uso Típico

```sql
-- Disputas em aberto com valor e idade
SELECT dh.DISPUTE_HISTORY_ID,
       dh.CUSTOMER_TRX_ID,
       dh.AMOUNT_IN_DISPUTE,
       dh.DISPUTE_DATE,
       dh.REASON_CODE,
       TRUNC(SYSDATE) - dh.DISPUTE_DATE AS dias_em_disputa
  FROM AR_DISPUTE_HISTORY dh
 WHERE dh.END_DATE IS NULL
   AND NVL(dh.CURRENT_RECORD_FLAG, 'Y') = 'Y'
 ORDER BY dh.AMOUNT_IN_DISPUTE DESC;
```

## 🔒 Observações

- Cada alteração no status da disputa gera um novo registro histórico; use `CURRENT_RECORD_FLAG = 'Y'` para obter o estado atual.
- O campo `REASON_CODE` referencia lookups configuráveis por organização.
- Disputas impactam o cálculo de aging: valores em disputa podem ser excluídos ou segregados conforme política da empresa.
- Para instituições financeiras, o histórico completo de disputas é requerido para compliance regulatório.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Dispute Management Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
