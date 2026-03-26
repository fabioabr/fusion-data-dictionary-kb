---
id: DOC-AR-027
doc_type: system-doc
title: "AR_RATE_ADJUSTMENTS_ALL — Ajustes de Taxa de Câmbio"
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
  - ajuste-cambio
  - rate-adjustments
  - exchange-rate
aliases:
  - AR_RATE_ADJUSTMENTS_ALL
  - ar_rate_adjustments_all
  - ajuste-cambio-ar
  - rate-adjustments
  - exchange-rate-adjustments
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_RATE_ADJUSTMENTS_ALL

## 📌 Visão Geral

Armazena os **ajustes de taxa de câmbio** aplicados a transações do módulo Accounts Receivable. Cada registro representa uma alteração na taxa de câmbio de uma fatura em moeda estrangeira, recalculando o valor na moeda funcional. Utilizada quando a taxa de câmbio originalmente registrada precisa ser corrigida ou atualizada.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Correção de câmbio:** Ajuste da taxa de câmbio de faturas emitidas em moeda estrangeira.
- **Reavaliação cambial:** Atualização de valores na moeda funcional quando a taxa de câmbio muda.
- **Variação cambial:** Registro da diferença entre taxa original e nova taxa.
- **Reconciliação GL:** Rastreamento de ajustes cambiais para conciliação com o General Ledger.
- **Auditoria:** Rastreabilidade completa de alterações de taxa com valores antigos e novos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RATE_ADJUSTMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do ajuste de taxa | — | 🟢 100% |
| 2 | CUSTOMER_TRX_ID | NUMBER(18) | NOT NULL | FK | Transação (fatura) com taxa ajustada | [[ra_customer_trx_all]] | 🟢 100% |
| 3 | OLD_EXCHANGE_RATE | NUMBER | NOT NULL | Financeiro | Taxa de câmbio anterior | — | 🟢 100% |
| 4 | NEW_EXCHANGE_RATE | NUMBER | NOT NULL | Financeiro | Nova taxa de câmbio | — | 🟢 100% |
| 5 | OLD_EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa anterior | [[gl_daily_conversion_types]] | 🟢 100% |
| 6 | NEW_EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa novo | [[gl_daily_conversion_types]] | 🟢 100% |
| 7 | OLD_EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa anterior | — | 🟢 100% |
| 8 | NEW_EXCHANGE_DATE | DATE | NULL | Financeiro | Data da nova taxa | — | 🟢 100% |
| 9 | GL_DATE | DATE | NOT NULL | Contabilidade | Data contábil do ajuste | — | 🟢 100% |
| 10 | GL_POSTED_DATE | DATE | NULL | Contabilidade | Data em que foi contabilizado no GL | — | 🟡 75% |
| 11 | POSTING_CONTROL_ID | NUMBER(18) | NULL | Contabilidade | ID do processo de posting | — | 🟢 100% |
| 12 | GAIN_LOSS_AMOUNT | NUMBER | NULL | Financeiro | Valor do ganho/perda cambial na moeda funcional | — | 🟡 75% |
| 13 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 18 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_customer_trx_all]] — via `CUSTOMER_TRX_ID` (transação ajustada)
- [[gl_daily_conversion_types]] — via `OLD_EXCHANGE_RATE_TYPE` e `NEW_EXCHANGE_RATE_TYPE` (tipo de câmbio anterior ao ajuste de taxa)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do ajuste de taxa de câmbio)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Ajustes de câmbio por transação
```sql
SELECT ra.RATE_ADJUSTMENT_ID, ra.OLD_EXCHANGE_RATE, ra.NEW_EXCHANGE_RATE,
       ra.GL_DATE, ra.GAIN_LOSS_AMOUNT
FROM   AR_RATE_ADJUSTMENTS_ALL ra
WHERE  ra.CUSTOMER_TRX_ID = :p_customer_trx_id
ORDER BY ra.GL_DATE;
```

### Total de ganho/perda cambial por período
```sql
SELECT SUM(ra.GAIN_LOSS_AMOUNT) AS total_variacao_cambial,
       COUNT(*) AS qtd_ajustes
FROM   AR_RATE_ADJUSTMENTS_ALL ra
WHERE  ra.GL_DATE BETWEEN :start_date AND :end_date
  AND  ra.ORG_ID = :p_org_id;
```

---

## 🔒 Observações

- Ajustes de taxa de câmbio **não alteram o valor na moeda da transação** — apenas recalculam o valor na moeda funcional.
- O campo `GAIN_LOSS_AMOUNT` registra a variação cambial (positivo = ganho, negativo = perda).
- Quando a taxa é ajustada, as distribuições contábeis em [[ra_cust_trx_line_gl_dist_all]] são recalculadas com a nova taxa.
- Essa tabela complementa o processo de **reavaliação cambial** do módulo GL — aqui o ajuste é feito no nível da transação AR.

---

## 📚 Referências

- [Oracle Docs — AR_RATE_ADJUSTMENTS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arrateadjustmentsall-25162.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
