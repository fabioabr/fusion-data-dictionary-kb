---
id: DOC-AR-026
doc_type: system-doc
title: "AR_REVENUE_ADJUSTMENTS_ALL — Ajustes de Reconhecimento de Receita"
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
  - revenue-adjustment
  - reconhecimento-receita
  - revenue-recognition
aliases:
  - AR_REVENUE_ADJUSTMENTS_ALL
  - ar_revenue_adjustments_all
  - ajuste-receita-ar
  - revenue-adjustments
  - reconhecimento-receita-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_REVENUE_ADJUSTMENTS_ALL

## 📌 Visão Geral

Armazena os **ajustes de reconhecimento de receita** do módulo Accounts Receivable. Cada registro representa um ajuste que altera a distribuição de receita de uma transação — reclassificação entre categorias contábeis, diferimento ou aceleração de reconhecimento. Utilizada em cenários onde a receita precisa ser redistribuída entre contas contábeis (e.g., mudança de categoria de receita, correção de alocação).

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Reclassificação de receita:** Transferência de valores entre categorias contábeis de receita.
- **Diferimento de receita:** Postergação do reconhecimento de receita para períodos futuros.
- **Aceleração de receita:** Antecipação do reconhecimento de receita.
- **Compliance ASC 606/IFRS 15:** Suporte a regras de reconhecimento de receita conforme normas contábeis.
- **Auditoria contábil:** Rastreabilidade de alterações na alocação de receita.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REVENUE_ADJUSTMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do ajuste de receita | — | 🟢 100% |
| 2 | CUSTOMER_TRX_ID | NUMBER(18) | NOT NULL | FK | Transação associada | [[ra_customer_trx_all]] | 🟢 100% |
| 3 | CUSTOMER_TRX_LINE_ID | NUMBER(18) | NULL | FK | Linha específica da transação | [[ra_customer_trx_lines_all]] | 🟢 100% |
| 4 | FROM_CATEGORY_ID | NUMBER(18) | NULL | Classificação | Categoria contábil de origem da receita | — | 🟢 100% |
| 5 | TO_CATEGORY_ID | NUMBER(18) | NULL | Classificação | Categoria contábil de destino da receita | — | 🟢 100% |
| 6 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor do ajuste de receita | — | 🟢 100% |
| 7 | AMOUNT_DR | NUMBER | NULL | Financeiro | Valor a débito | — | 🟢 100% |
| 8 | AMOUNT_CR | NUMBER | NULL | Financeiro | Valor a crédito | — | 🟢 100% |
| 9 | ACCTD_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda funcional | — | 🟢 100% |
| 10 | GL_DATE | DATE | NOT NULL | Contabilidade | Data contábil (General Ledger) | — | 🟢 100% |
| 11 | GL_POSTED_DATE | DATE | NULL | Contabilidade | Data em que foi contabilizado no GL | — | 🟡 75% |
| 12 | TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do ajuste (DEFERRAL/ACCELERATION/RECLASS) | — | 🟢 100% |
| 13 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status do ajuste (A=aprovado, P=pendente) | — | 🟢 100% |
| 14 | REASON_CODE | VARCHAR2(30) | NULL | Classificação | Código do motivo do ajuste | — | 🟢 100% |
| 15 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Comentários sobre o ajuste | — | 🟢 100% |
| 16 | CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | CCID da conta de receita afetada | [[gl_code_combinations]] | 🟢 100% |
| 17 | FROM_CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | CCID da conta de origem | [[gl_code_combinations]] | 🟡 75% |
| 18 | TO_CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | CCID da conta de destino | [[gl_code_combinations]] | 🟡 75% |
| 19 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 20 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 21 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 22 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 23 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 24 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_customer_trx_all]] — via `CUSTOMER_TRX_ID` (transação de cliente objeto do ajuste de receita)
- [[ra_customer_trx_lines_all]] — via `CUSTOMER_TRX_LINE_ID` (linha da transação)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID`, `FROM_CODE_COMBINATION_ID`, `TO_CODE_COMBINATION_ID` (conta contábil do ajuste de receita)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do ajuste de receita)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Ajustes de receita por transação
```sql
SELECT ra.REVENUE_ADJUSTMENT_ID, ra.AMOUNT, ra.TYPE, ra.STATUS,
       ra.GL_DATE, ra.FROM_CATEGORY_ID, ra.TO_CATEGORY_ID
FROM   AR_REVENUE_ADJUSTMENTS_ALL ra
WHERE  ra.CUSTOMER_TRX_ID = :p_customer_trx_id
ORDER BY ra.GL_DATE;
```

### Total de ajustes de receita por período
```sql
SELECT ra.TYPE, SUM(ra.AMOUNT) AS total_ajuste, COUNT(*) AS qtd
FROM   AR_REVENUE_ADJUSTMENTS_ALL ra
WHERE  ra.STATUS = 'A'
  AND  ra.GL_DATE BETWEEN :start_date AND :end_date
  AND  ra.ORG_ID = :p_org_id
GROUP BY ra.TYPE;
```

---

## 🔒 Observações

- O `TYPE` indica o tipo de ajuste: **DEFERRAL** (diferimento), **ACCELERATION** (aceleração), **RECLASS** (reclassificação entre categorias).
- Os campos `FROM_CATEGORY_ID` e `TO_CATEGORY_ID` identificam a movimentação entre categorias contábeis.
- Ajustes de receita diferem de ajustes de fatura ([[ar_adjustments_all]]): aqui o saldo do cliente **não é alterado** — apenas a alocação contábil da receita.
- Compliance com **ASC 606** e **IFRS 15** frequentemente gera ajustes de receita para realocação de preço de transação.

---

## 📚 Referências

- [Oracle Docs — AR_REVENUE_ADJUSTMENTS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arrevenueadjustmentsall-25164.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
