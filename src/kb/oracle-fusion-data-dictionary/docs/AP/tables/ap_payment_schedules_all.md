---
id: DOC-AP-020
doc_type: system-doc
title: "AP_PAYMENT_SCHEDULES_ALL — Parcelas e Vencimentos de Faturas"
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
  - parcelas
  - vencimentos
  - payment-schedules
aliases:
  - AP_PAYMENT_SCHEDULES_ALL
  - ap_payment_schedules_all
  - parcelas-ap
  - vencimentos-ap
  - payment-schedules-ap
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_PAYMENT_SCHEDULES_ALL

## 📌 Visão Geral

Armazena as **parcelas de pagamento** (payment schedules) de cada fatura do módulo Accounts Payable. Cada registro representa um vencimento (due date) com valor bruto, valor remanescente, descontos disponíveis e status de pagamento. Uma fatura pode ter uma ou mais parcelas, conforme a condição de pagamento (payment terms) aplicada. É a tabela central para gestão de vencimentos e seleção de faturas para pagamento.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de vencimentos:** Cada parcela contém a data de vencimento calculada a partir da condição de pagamento.
- **Seleção de pagamento (PPR):** O Payment Process Request consulta esta tabela para identificar parcelas elegíveis.
- **Aging de contas a pagar:** Base para relatórios de aging (30/60/90/120 dias) por data de vencimento.
- **Descontos financeiros:** Armazena datas e percentuais de desconto por pagamento antecipado.
- **Controle de saldo:** O campo `AMOUNT_REMAINING` é atualizado a cada pagamento parcial ou total.
- **Fluxo de caixa:** Base para projeção de desembolsos futuros por data de vencimento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INVOICE_ID | NUMBER(18) | NOT NULL | PK/FK | Fatura à qual pertence a parcela | [[ap_invoices_all]] | 🟢 100% |
| 2 | PAYMENT_NUM | NUMBER | NOT NULL | PK | Número sequencial da parcela | — | 🟢 100% |
| 3 | DUE_DATE | DATE | NOT NULL | Data | Data de vencimento da parcela | — | 🟢 100% |
| 4 | GROSS_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor bruto da parcela | — | 🟢 100% |
| 5 | AMOUNT_REMAINING | NUMBER | NULL | Financeiro | Valor remanescente (não pago) | — | 🟢 100% |
| 6 | PAYMENT_STATUS_FLAG | VARCHAR2(1) | NULL | Status | Status do pagamento (Y=pago/N=pendente/P=parcial) | — | 🟢 100% |
| 7 | PAYMENT_METHOD_CODE | VARCHAR2(30) | NULL | Pagamento | Método de pagamento | [[iby_payment_methods_b]] | 🟢 100% |
| 8 | PAYMENT_PRIORITY | NUMBER | NULL | Pagamento | Prioridade de pagamento (1=alta, 99=baixa) | — | 🟢 100% |
| 9 | HOLD_FLAG | VARCHAR2(1) | NULL | Controle | Indica se a parcela está em hold (Y/N) | — | 🟢 100% |
| 10 | DISCOUNT_DATE | DATE | NULL | Desconto | Data limite para desconto (1o nível) | — | 🟢 100% |
| 11 | DISCOUNT_AMOUNT_AVAILABLE | NUMBER | NULL | Desconto | Valor de desconto disponível (1o nível) | — | 🟢 100% |
| 12 | SECOND_DISCOUNT_DATE | DATE | NULL | Desconto | Data limite para desconto (2o nível) | — | 🟢 100% |
| 13 | SECOND_DISC_AMT_AVAILABLE | NUMBER | NULL | Desconto | Valor de desconto disponível (2o nível) | — | 🟢 100% |
| 14 | THIRD_DISCOUNT_DATE | DATE | NULL | Desconto | Data limite para desconto (3o nível) | — | 🟢 100% |
| 15 | THIRD_DISC_AMT_AVAILABLE | NUMBER | NULL | Desconto | Valor de desconto disponível (3o nível) | — | 🟢 100% |
| 16 | DISCOUNT_AMOUNT_REMAINING | NUMBER | NULL | Desconto | Valor de desconto remanescente | — | 🟢 100% |
| 17 | INV_CURR_GROSS_AMOUNT | NUMBER | NULL | Financeiro | Valor bruto na moeda da fatura | — | 🟢 100% |
| 18 | PAYMENT_CROSS_RATE | NUMBER | NULL | Financeiro | Taxa de conversão entre moeda da fatura e pagamento | — | 🟡 75% |
| 19 | FUTURE_PAY_DUE_DATE | DATE | NULL | Data | Data de vencimento para future-dated payment | — | 🟡 75% |
| 20 | EXTERNAL_BANK_ACCOUNT_ID | NUMBER(18) | NULL | Bancário | Conta bancária do fornecedor (para EFT) | [[iby_ext_bank_accounts]] | 🟢 100% |
| 21 | IBY_HOLD_REASON | VARCHAR2(2000) | NULL | Controle | Motivo de hold do Oracle Payments | — | 🟡 75% |
| 22 | REMIT_TO_SUPPLIER_NAME | VARCHAR2(240) | NULL | Fornecedor | Nome do fornecedor de remessa | — | 🟡 70% |
| 23 | REMIT_TO_SUPPLIER_SITE | VARCHAR2(15) | NULL | Fornecedor | Site do fornecedor de remessa | — | 🟡 70% |
| 24 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 25 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 26 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 27 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 28 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 29 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 30 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 31 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ap_invoices_all]] — via `INVOICE_ID` (fatura à qual a parcela de pagamento pertence)
- [[iby_payment_methods_b]] — via `PAYMENT_METHOD_CODE` (método de pagamento)
- [[iby_ext_bank_accounts]] — via `EXTERNAL_BANK_ACCOUNT_ID` (conta bancária do fornecedor)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da parcela de pagamento)

### Tabelas-filha (FK de saída)
- [[ap_invoice_payments_all]] — via `INVOICE_ID` + `PAYMENT_NUM` (pagamentos aplicados à parcela)

---

## 📎 Uso Típico

### Parcelas pendentes por data de vencimento
```sql
SELECT ai.INVOICE_NUM, aps.PAYMENT_NUM, aps.DUE_DATE,
       aps.GROSS_AMOUNT, aps.AMOUNT_REMAINING
FROM   AP_PAYMENT_SCHEDULES_ALL aps
JOIN   AP_INVOICES_ALL ai ON ai.INVOICE_ID = aps.INVOICE_ID
WHERE  aps.PAYMENT_STATUS_FLAG <> 'Y'
  AND  aps.DUE_DATE <= :p_thru_date
  AND  aps.ORG_ID = :p_org_id
ORDER BY aps.DUE_DATE;
```

### Aging de contas a pagar
```sql
SELECT CASE
         WHEN aps.DUE_DATE >= TRUNC(SYSDATE) THEN 'A Vencer'
         WHEN TRUNC(SYSDATE) - aps.DUE_DATE <= 30 THEN '1-30 dias'
         WHEN TRUNC(SYSDATE) - aps.DUE_DATE <= 60 THEN '31-60 dias'
         WHEN TRUNC(SYSDATE) - aps.DUE_DATE <= 90 THEN '61-90 dias'
         ELSE '90+ dias'
       END AS faixa_aging,
       SUM(aps.AMOUNT_REMAINING) AS total_pendente
FROM   AP_PAYMENT_SCHEDULES_ALL aps
WHERE  aps.PAYMENT_STATUS_FLAG <> 'Y'
  AND  aps.ORG_ID = :p_org_id
GROUP BY CASE
           WHEN aps.DUE_DATE >= TRUNC(SYSDATE) THEN 'A Vencer'
           WHEN TRUNC(SYSDATE) - aps.DUE_DATE <= 30 THEN '1-30 dias'
           WHEN TRUNC(SYSDATE) - aps.DUE_DATE <= 60 THEN '31-60 dias'
           WHEN TRUNC(SYSDATE) - aps.DUE_DATE <= 90 THEN '61-90 dias'
           ELSE '90+ dias'
         END;
```

### Filtros comuns
- `PAYMENT_STATUS_FLAG = 'N'` — Parcelas não pagas
- `PAYMENT_STATUS_FLAG <> 'Y'` — Pendentes (inclui parcial)
- `DUE_DATE <= SYSDATE` — Vencidas
- `HOLD_FLAG IS NULL OR HOLD_FLAG = 'N'` — Sem hold

---

## 🔒 Observações

- A PK composta é `INVOICE_ID` + `PAYMENT_NUM`.
- O campo `AMOUNT_REMAINING` é atualizado automaticamente a cada pagamento parcial ou total, refletindo o saldo em aberto.
- A tabela suporta até **três níveis de desconto** financeiro com datas e valores específicos (`DISCOUNT_DATE`, `SECOND_DISCOUNT_DATE`, `THIRD_DISCOUNT_DATE`).
- O campo `HOLD_FLAG = 'Y'` impede que a parcela seja selecionada no Payment Process Request.
- A coluna `PAYMENT_PRIORITY` influencia a ordem de seleção no PPR — valores menores = prioridade maior.
- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.

---

## 📚 Referências

- [Oracle Docs — AP_PAYMENT_SCHEDULES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/appaymentschedulesall-10047.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
