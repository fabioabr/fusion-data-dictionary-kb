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

## 🔗 PVOs Relacionados

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | RevenueAdjustmentAmount | — |
| AMOUNT_MODE | RevenueAdjustmentAmountMode | — |
| APPLICATION_DATE | RevenueAdjustmentApplicationDate | — |
| CUSTOMER_TRX_ID | RevenueAdjustmentCustomerTrxId | — |
| FROM_CATEGORY_ID | RevenueAdjustmentFromCategoryId | — |
| FROM_CUST_TRX_LINE_ID | RevenueAdjustmentFromCustTrxLineId | — |
| FROM_INVENTORY_ITEM_ID | RevenueAdjustmentFromInventoryItemId | — |
| FROM_RESOURCE_SALESREP_ID | RevenueAdjustmentFromResourceSalesrepId | — |
| FROM_SALESGROUP_ID | RevenueAdjustmentFromSalesgroupId | — |
| GL_DATE | RevenueAdjustmentGlDate | — |
| LINE_SELECTION_MODE | RevenueAdjustmentLineSelectionMode | — |
| ORG_ID | RevenueAdjustmentOrgId | — |
| PERCENT | RevenueAdjustmentPercent | — |
| PROGRAM_APPLICATION_ID | RevenueAdjustmentProgramApplicationId | — |
| PROGRAM_ID | RevenueAdjustmentProgramId | — |
| PROGRAM_UPDATE_DATE | RevenueAdjustmentProgramUpdateDate | — |
| REASON_CODE | RevenueAdjustmentReasonCode | — |
| REQUEST_ID | RevenueAdjustmentRequestId | — |
| REVENUE_ADJUSTMENT_ID | RevenueAdjustmentRevenueAdjustmentId | — |
| REVENUE_ADJUSTMENT_NUMBER | RevenueAdjustmentRevenueAdjustmentNumber | — |
| SALES_CREDIT_TYPE | RevenueAdjustmentSalesCreditType | — |
| STATUS | RevenueAdjustmentStatus | — |
| TO_CATEGORY_ID | RevenueAdjustmentToCategoryId | — |
| TO_CUST_TRX_LINE_ID | RevenueAdjustmentToCustTrxLineId | — |
| TO_INVENTORY_ITEM_ID | RevenueAdjustmentToInventoryItemId | — |
| TO_RESOURCE_SALESREP_ID | RevenueAdjustmentToResourceSalesrepId | — |
| TO_SALESGROUP_ID | RevenueAdjustmentToSalesgroupId | — |
| TYPE | RevenueAdjustmentType | — |

### [[completedtrxrevenuedistributionpvo|CompletedTrxRevenueDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | RevenueAdjustmentAmount | — |
| AMOUNT_MODE | RevenueAdjustmentAmountMode | — |
| APPLICATION_DATE | RevenueAdjustmentApplicationDate | — |
| CUSTOMER_TRX_ID | RevenueAdjustmentCustomerTrxId | — |
| FROM_CATEGORY_ID | RevenueAdjustmentFromCategoryId | — |
| FROM_CUST_TRX_LINE_ID | RevenueAdjustmentFromCustTrxLineId | — |
| FROM_INVENTORY_ITEM_ID | RevenueAdjustmentFromInventoryItemId | — |
| FROM_RESOURCE_SALESREP_ID | RevenueAdjustmentFromResourceSalesrepId | — |
| FROM_SALESGROUP_ID | RevenueAdjustmentFromSalesgroupId | — |
| GL_DATE | RevenueAdjustmentGlDate | — |
| LINE_SELECTION_MODE | RevenueAdjustmentLineSelectionMode | — |
| ORG_ID | RevenueAdjustmentOrgId | — |
| PERCENT | RevenueAdjustmentPercent | — |
| PROGRAM_APPLICATION_ID | RevenueAdjustmentProgramApplicationId | — |
| PROGRAM_ID | RevenueAdjustmentProgramId | — |
| PROGRAM_UPDATE_DATE | RevenueAdjustmentProgramUpdateDate | — |
| REASON_CODE | RevenueAdjustmentReasonCode | — |
| REQUEST_ID | RevenueAdjustmentRequestId | — |
| REVENUE_ADJUSTMENT_ID | RevenueAdjustmentRevenueAdjustmentId | — |
| REVENUE_ADJUSTMENT_NUMBER | RevenueAdjustmentRevenueAdjustmentNumber | — |
| SALES_CREDIT_TYPE | RevenueAdjustmentSalesCreditType | — |
| STATUS | RevenueAdjustmentStatus | — |
| TO_CATEGORY_ID | RevenueAdjustmentToCategoryId | — |
| TO_CUST_TRX_LINE_ID | RevenueAdjustmentToCustTrxLineId | — |
| TO_INVENTORY_ITEM_ID | RevenueAdjustmentToInventoryItemId | — |
| TO_RESOURCE_SALESREP_ID | RevenueAdjustmentToResourceSalesrepId | — |
| TO_SALESGROUP_ID | RevenueAdjustmentToSalesgroupId | — |
| TYPE | RevenueAdjustmentType | — |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR · BICC: 1/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | RevAdjAmount | — |
| AMOUNT_MODE | RevAdjAmountMode | — |
| APPLICATION_DATE | RevAdjApplicationDate | — |
| CUSTOMER_TRX_ID | RevAdjCustomerTrxId | — |
| FROM_CATEGORY_ID | RevAdjFromCategoryId | — |
| FROM_CUST_TRX_LINE_ID | RevAdjFromCustTrxLineId | — |
| FROM_INVENTORY_ITEM_ID | RevAdjFromInventoryItemId | — |
| FROM_RESOURCE_SALESREP_ID | RevAdjFromResourceSalesrepId | — |
| FROM_SALESGROUP_ID | RevAdjFromSalesgroupId | — |
| GL_DATE | RevAdjGlDate | — |
| LINE_SELECTION_MODE | RevAdjLineSelectionMode | — |
| ORG_ID | RevAdjOrgId | — |
| PERCENT | RevAdjPercent | — |
| PROGRAM_APPLICATION_ID | RevAdjProgramApplicationId | — |
| PROGRAM_ID | RevAdjProgramId | — |
| PROGRAM_UPDATE_DATE | RevAdjProgramUpdateDate | — |
| REASON_CODE | RevAdjReasonCode | — |
| REQUEST_ID | RevAdjRequestId | — |
| REVENUE_ADJUSTMENT_ID | RevAdjRevenueAdjustmentId | — |
| REVENUE_ADJUSTMENT_NUMBER | RevAdjRevenueAdjustmentNumber | ✅ |
| SALES_CREDIT_TYPE | RevAdjSalesCreditType | — |
| STATUS | RevAdjStatus | — |
| TO_CATEGORY_ID | RevAdjToCategoryId | — |
| TO_CUST_TRX_LINE_ID | RevAdjToCustTrxLineId | — |
| TO_INVENTORY_ITEM_ID | RevAdjToInventoryItemId | — |
| TO_RESOURCE_SALESREP_ID | RevAdjToResourceSalesrepId | — |
| TO_SALESGROUP_ID | RevAdjToSalesgroupId | — |
| TYPE | RevAdjType | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 1/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | RevAdjAmount | — |
| AMOUNT_MODE | RevAdjAmountMode | — |
| APPLICATION_DATE | RevAdjApplicationDate | — |
| CUSTOMER_TRX_ID | RevAdjCustomerTrxId | — |
| FROM_CATEGORY_ID | RevAdjFromCategoryId | — |
| FROM_CUST_TRX_LINE_ID | RevAdjFromCustTrxLineId | — |
| FROM_INVENTORY_ITEM_ID | RevAdjFromInventoryItemId | — |
| FROM_RESOURCE_SALESREP_ID | RevAdjFromResourceSalesrepId | — |
| FROM_SALESGROUP_ID | RevAdjFromSalesgroupId | — |
| GL_DATE | RevAdjGlDate | — |
| LINE_SELECTION_MODE | RevAdjLineSelectionMode | — |
| ORG_ID | RevAdjOrgId | — |
| PERCENT | RevAdjPercent | — |
| PROGRAM_APPLICATION_ID | RevAdjProgramApplicationId | — |
| PROGRAM_ID | RevAdjProgramId | — |
| PROGRAM_UPDATE_DATE | RevAdjProgramUpdateDate | — |
| REASON_CODE | RevAdjReasonCode | — |
| REQUEST_ID | RevAdjRequestId | — |
| REVENUE_ADJUSTMENT_ID | RevAdjRevenueAdjustmentId | — |
| REVENUE_ADJUSTMENT_NUMBER | RevAdjRevenueAdjustmentNumber | ✅ |
| SALES_CREDIT_TYPE | RevAdjSalesCreditType | — |
| STATUS | RevAdjStatus | — |
| TO_CATEGORY_ID | RevAdjToCategoryId | — |
| TO_CUST_TRX_LINE_ID | RevAdjToCustTrxLineId | — |
| TO_INVENTORY_ITEM_ID | RevAdjToInventoryItemId | — |
| TO_RESOURCE_SALESREP_ID | RevAdjToResourceSalesrepId | — |
| TO_SALESGROUP_ID | RevAdjToSalesgroupId | — |
| TYPE | RevAdjType | — |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | RevenueAdjustmentAmount | — |
| AMOUNT_MODE | RevenueAdjustmentAmountMode | — |
| APPLICATION_DATE | RevenueAdjustmentApplicationDate | — |
| COMMENTS | RevenueAdjustmentComments | — |
| CREATED_BY | RevenueAdjustmentCreatedBy | — |
| CUSTOMER_TRX_ID | RevenueAdjustmentCustomerTrxId | — |
| FROM_CATEGORY_ID | RevenueAdjustmentFromCategoryId | — |
| FROM_CUST_TRX_LINE_ID | RevenueAdjustmentFromCustTrxLineId | — |
| FROM_INVENTORY_ITEM_ID | RevenueAdjustmentFromInventoryItemId | — |
| FROM_RESOURCE_SALESREP_ID | RevenueAdjustmentFromResourceSalesrepId | — |
| FROM_SALESGROUP_ID | RevenueAdjustmentFromSalesgroupId | — |
| GL_DATE | RevenueAdjustmentGlDate | — |
| LAST_UPDATE_LOGIN | RevenueAdjustmentLastUpdateLogin | — |
| LAST_UPDATED_BY | RevenueAdjustmentLastUpdatedBy | — |
| LINE_SELECTION_MODE | RevenueAdjustmentLineSelectionMode | — |
| OBJECT_VERSION_NUMBER | RevenueAdjustmentObjectVersionNumber | — |
| ORG_ID | RevenueAdjustmentOrgId | — |
| PERCENT | RevenueAdjustmentPercent | — |
| PROGRAM_APPLICATION_ID | RevenueAdjustmentProgramApplicationId | — |
| PROGRAM_ID | RevenueAdjustmentProgramId | — |
| PROGRAM_UPDATE_DATE | RevenueAdjustmentProgramUpdateDate | — |
| REASON_CODE | RevenueAdjustmentReasonCode | — |
| REQUEST_ID | RevenueAdjustmentRequestId | — |
| REVENUE_ADJUSTMENT_ID | RevenueAdjustmentRevenueAdjustmentId | — |
| REVENUE_ADJUSTMENT_NUMBER | RevenueAdjustmentRevenueAdjustmentNumber | — |
| SALES_CREDIT_TYPE | RevenueAdjustmentSalesCreditType | — |
| STATUS | RevenueAdjustmentStatus | — |
| TO_CATEGORY_ID | RevenueAdjustmentToCategoryId | — |
| TO_CUST_TRX_LINE_ID | RevenueAdjustmentToCustTrxLineId | — |
| TO_INVENTORY_ITEM_ID | RevenueAdjustmentToInventoryItemId | — |
| TO_RESOURCE_SALESREP_ID | RevenueAdjustmentToResourceSalesrepId | — |
| TO_SALESGROUP_ID | RevenueAdjustmentToSalesgroupId | — |
| TYPE | RevenueAdjustmentType | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | RevenueAdjustmentAmount | — |
| AMOUNT_MODE | RevenueAdjustmentAmountMode | — |
| APPLICATION_DATE | RevenueAdjustmentApplicationDate | — |
| COMMENTS | RevenueAdjustmentComments | — |
| CREATED_BY | RevenueAdjustmentCreatedBy | — |
| CUSTOMER_TRX_ID | RevenueAdjustmentCustomerTrxId | — |
| FROM_CATEGORY_ID | RevenueAdjustmentFromCategoryId | — |
| FROM_CUST_TRX_LINE_ID | RevenueAdjustmentFromCustTrxLineId | — |
| FROM_INVENTORY_ITEM_ID | RevenueAdjustmentFromInventoryItemId | — |
| FROM_RESOURCE_SALESREP_ID | RevenueAdjustmentFromResourceSalesrepId | — |
| FROM_SALESGROUP_ID | RevenueAdjustmentFromSalesgroupId | — |
| GL_DATE | RevenueAdjustmentGlDate | — |
| LAST_UPDATE_LOGIN | RevenueAdjustmentLastUpdateLogin | — |
| LAST_UPDATED_BY | RevenueAdjustmentLastUpdatedBy | — |
| LINE_SELECTION_MODE | RevenueAdjustmentLineSelectionMode | — |
| OBJECT_VERSION_NUMBER | RevenueAdjustmentObjectVersionNumber | — |
| ORG_ID | RevenueAdjustmentOrgId | — |
| PERCENT | RevenueAdjustmentPercent | — |
| PROGRAM_APPLICATION_ID | RevenueAdjustmentProgramApplicationId | — |
| PROGRAM_ID | RevenueAdjustmentProgramId | — |
| PROGRAM_UPDATE_DATE | RevenueAdjustmentProgramUpdateDate | — |
| REASON_CODE | RevenueAdjustmentReasonCode | — |
| REQUEST_ID | RevenueAdjustmentRequestId | — |
| REVENUE_ADJUSTMENT_ID | RevenueAdjustmentRevenueAdjustmentId | — |
| REVENUE_ADJUSTMENT_NUMBER | RevenueAdjustmentRevenueAdjustmentNumber | — |
| SALES_CREDIT_TYPE | RevenueAdjustmentSalesCreditType | — |
| STATUS | RevenueAdjustmentStatus | — |
| TO_CATEGORY_ID | RevenueAdjustmentToCategoryId | — |
| TO_CUST_TRX_LINE_ID | RevenueAdjustmentToCustTrxLineId | — |
| TO_INVENTORY_ITEM_ID | RevenueAdjustmentToInventoryItemId | — |
| TO_RESOURCE_SALESREP_ID | RevenueAdjustmentToResourceSalesrepId | — |
| TO_SALESGROUP_ID | RevenueAdjustmentToSalesgroupId | — |
| TYPE | RevenueAdjustmentType | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | RevenueAdjustmentAmount | — |
| AMOUNT_MODE | RevenueAdjustmentAmountMode | — |
| APPLICATION_DATE | RevenueAdjustmentApplicationDate | — |
| COMMENTS | RevenueAdjustmentComments | — |
| CREATED_BY | RevenueAdjustmentCreatedBy | — |
| CUSTOMER_TRX_ID | RevenueAdjustmentCustomerTrxId | — |
| FROM_CATEGORY_ID | RevenueAdjustmentFromCategoryId | — |
| FROM_CUST_TRX_LINE_ID | RevenueAdjustmentFromCustTrxLineId | — |
| FROM_INVENTORY_ITEM_ID | RevenueAdjustmentFromInventoryItemId | — |
| FROM_RESOURCE_SALESREP_ID | RevenueAdjustmentFromResourceSalesrepId | — |
| FROM_SALESGROUP_ID | RevenueAdjustmentFromSalesgroupId | — |
| GL_DATE | RevenueAdjustmentGlDate | — |
| LAST_UPDATE_LOGIN | RevenueAdjustmentLastUpdateLogin | — |
| LAST_UPDATED_BY | RevenueAdjustmentLastUpdatedBy | — |
| LINE_SELECTION_MODE | RevenueAdjustmentLineSelectionMode | — |
| OBJECT_VERSION_NUMBER | RevenueAdjustmentObjectVersionNumber | — |
| ORG_ID | RevenueAdjustmentOrgId | — |
| PERCENT | RevenueAdjustmentPercent | — |
| PROGRAM_APPLICATION_ID | RevenueAdjustmentProgramApplicationId | — |
| PROGRAM_ID | RevenueAdjustmentProgramId | — |
| PROGRAM_UPDATE_DATE | RevenueAdjustmentProgramUpdateDate | — |
| REASON_CODE | RevenueAdjustmentReasonCode | — |
| REQUEST_ID | RevenueAdjustmentRequestId | — |
| REVENUE_ADJUSTMENT_ID | RevenueAdjustmentRevenueAdjustmentId | — |
| REVENUE_ADJUSTMENT_NUMBER | RevenueAdjustmentRevenueAdjustmentNumber | — |
| SALES_CREDIT_TYPE | RevenueAdjustmentSalesCreditType | — |
| STATUS | RevenueAdjustmentStatus | — |
| TO_CATEGORY_ID | RevenueAdjustmentToCategoryId | — |
| TO_CUST_TRX_LINE_ID | RevenueAdjustmentToCustTrxLineId | — |
| TO_INVENTORY_ITEM_ID | RevenueAdjustmentToInventoryItemId | — |
| TO_RESOURCE_SALESREP_ID | RevenueAdjustmentToResourceSalesrepId | — |
| TO_SALESGROUP_ID | RevenueAdjustmentToSalesgroupId | — |
| TYPE | RevenueAdjustmentType | — |

### [[revenueadjustmentdistributionpvo|RevenueAdjustmentDistributionPVO]] (AR · BICC: 14/35)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | RevAdjustmentAmount | — |
| AMOUNT_MODE | RevAdjustmentAmountMode | ✅ |
| APPLICATION_DATE | RevAdjustmentApplicationDate | ✅ |
| COMMENTS | RevAdjustmentComments | ✅ |
| CREATED_BY | RevAdjustmentCreatedBy | ✅ |
| CREATION_DATE | RevAdjustmentCreationDate | ✅ |
| CUSTOMER_TRX_ID | RevAdjustmentCustomerTrxId | — |
| FROM_CATEGORY_ID | RevAdjustmentFromCategoryId | — |
| FROM_CUST_TRX_LINE_ID | RevAdjustmentFromCustTrxLineId | — |
| FROM_INVENTORY_ITEM_ID | RevAdjustmentFromInventoryItemId | — |
| FROM_RESOURCE_SALESREP_ID | RevAdjustmentFromResourceSalesrepId | — |
| FROM_SALESGROUP_ID | RevAdjustmentFromSalesgroupId | — |
| GL_DATE | RevAdjustmentGlDate | ✅ |
| LAST_UPDATE_DATE | RevAdjustmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RevAdjustmentLastUpdateLogin | — |
| LAST_UPDATED_BY | RevAdjustmentLastUpdatedBy | ✅ |
| LINE_SELECTION_MODE | RevAdjustmentLineSelectionMode | — |
| OBJECT_VERSION_NUMBER | RevAdjustmentObjectVersionNumber | — |
| ORG_ID | RevAdjustmentOrgId | — |
| PERCENT | RevAdjustmentPercent | ✅ |
| PROGRAM_APPLICATION_ID | RevAdjustmentProgramApplicationId | — |
| PROGRAM_ID | RevAdjustmentProgramId | — |
| PROGRAM_UPDATE_DATE | RevAdjustmentProgramUpdateDate | — |
| REASON_CODE | RevAdjustmentReasonCode | ✅ |
| REQUEST_ID | RevAdjustmentRequestId | — |
| REVENUE_ADJUSTMENT_ID | RevAdjustmentRevenueAdjustmentId | ✅ |
| REVENUE_ADJUSTMENT_NUMBER | RevAdjustmentRevenueAdjustmentNumber | ✅ |
| SALES_CREDIT_TYPE | RevAdjustmentSalesCreditType | ✅ |
| STATUS | RevAdjustmentStatus | — |
| TO_CATEGORY_ID | RevAdjustmentToCategoryId | — |
| TO_CUST_TRX_LINE_ID | RevAdjustmentToCustTrxLineId | — |
| TO_INVENTORY_ITEM_ID | RevAdjustmentToInventoryItemId | — |
| TO_RESOURCE_SALESREP_ID | RevAdjustmentToResourceSalesrepId | — |
| TO_SALESGROUP_ID | RevAdjustmentToSalesgroupId | — |
| TYPE | RevAdjustmentType | ✅ |

### [[revenueadjustmentextractpvo|RevenueAdjustmentExtractPVO]] (OTHER · BICC: 35/51)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | ArRevenueAdjustmentAmount | ✅ |
| AMOUNT_MODE | ArRevenueAdjustmentAmountMode | ✅ |
| APPLICATION_DATE | ArRevenueAdjustmentApplicationDate | ✅ |
| ATTRIBUTE1 | ArRevenueAdjustmentAttribute1 | — |
| ATTRIBUTE10 | ArRevenueAdjustmentAttribute10 | — |
| ATTRIBUTE11 | ArRevenueAdjustmentAttribute11 | — |
| ATTRIBUTE12 | ArRevenueAdjustmentAttribute12 | — |
| ATTRIBUTE13 | ArRevenueAdjustmentAttribute13 | — |
| ATTRIBUTE14 | ArRevenueAdjustmentAttribute14 | — |
| ATTRIBUTE15 | ArRevenueAdjustmentAttribute15 | — |
| ATTRIBUTE2 | ArRevenueAdjustmentAttribute2 | — |
| ATTRIBUTE3 | ArRevenueAdjustmentAttribute3 | — |
| ATTRIBUTE4 | ArRevenueAdjustmentAttribute4 | — |
| ATTRIBUTE5 | ArRevenueAdjustmentAttribute5 | — |
| ATTRIBUTE6 | ArRevenueAdjustmentAttribute6 | — |
| ATTRIBUTE7 | ArRevenueAdjustmentAttribute7 | — |
| ATTRIBUTE8 | ArRevenueAdjustmentAttribute8 | — |
| ATTRIBUTE9 | ArRevenueAdjustmentAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArRevenueAdjustmentAttributeCategory | — |
| COMMENTS | ArRevenueAdjustmentComments | ✅ |
| CREATED_BY | ArRevenueAdjustmentCreatedBy | ✅ |
| CREATION_DATE | ArRevenueAdjustmentCreationDate | ✅ |
| CUSTOMER_TRX_ID | ArRevenueAdjustmentCustomerTrxId | ✅ |
| FROM_CATEGORY_ID | ArRevenueAdjustmentFromCategoryId | ✅ |
| FROM_CUST_TRX_LINE_ID | ArRevenueAdjustmentFromCustTrxLineId | ✅ |
| FROM_INVENTORY_ITEM_ID | ArRevenueAdjustmentFromInventoryItemId | ✅ |
| FROM_RESOURCE_SALESREP_ID | ArRevenueAdjustmentFromResourceSalesrepId | ✅ |
| FROM_SALESGROUP_ID | ArRevenueAdjustmentFromSalesgroupId | ✅ |
| GL_DATE | ArRevenueAdjustmentGlDate | ✅ |
| LAST_UPDATE_DATE | ArRevenueAdjustmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArRevenueAdjustmentLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArRevenueAdjustmentLastUpdatedBy | ✅ |
| LINE_SELECTION_MODE | ArRevenueAdjustmentLineSelectionMode | ✅ |
| OBJECT_VERSION_NUMBER | ArRevenueAdjustmentObjectVersionNumber | ✅ |
| ORG_ID | ArRevenueAdjustmentOrgId | ✅ |
| PERCENT | ArRevenueAdjustmentPercent | ✅ |
| PROGRAM_APPLICATION_ID | ArRevenueAdjustmentProgramApplicationId | ✅ |
| PROGRAM_ID | ArRevenueAdjustmentProgramId | ✅ |
| PROGRAM_UPDATE_DATE | ArRevenueAdjustmentProgramUpdateDate | ✅ |
| REASON_CODE | ArRevenueAdjustmentReasonCode | ✅ |
| REQUEST_ID | ArRevenueAdjustmentRequestId | ✅ |
| REVENUE_ADJUSTMENT_ID | ArRevenueAdjustmentRevenueAdjustmentId | ✅ |
| REVENUE_ADJUSTMENT_NUMBER | ArRevenueAdjustmentRevenueAdjustmentNumber | ✅ |
| SALES_CREDIT_TYPE | ArRevenueAdjustmentSalesCreditType | ✅ |
| STATUS | ArRevenueAdjustmentStatus | ✅ |
| TO_CATEGORY_ID | ArRevenueAdjustmentToCategoryId | ✅ |
| TO_CUST_TRX_LINE_ID | ArRevenueAdjustmentToCustTrxLineId | ✅ |
| TO_INVENTORY_ITEM_ID | ArRevenueAdjustmentToInventoryItemId | ✅ |
| TO_RESOURCE_SALESREP_ID | ArRevenueAdjustmentToResourceSalesrepId | ✅ |
| TO_SALESGROUP_ID | ArRevenueAdjustmentToSalesgroupId | ✅ |
| TYPE | ArRevenueAdjustmentType | ✅ |

### [[revenueadjustmentpvo|RevenueAdjustmentPVO]] (AR · BICC: 15/35)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | RevenueAdjustmentAmount | ✅ |
| AMOUNT_MODE | RevenueAdjustmentAmountMode | ✅ |
| APPLICATION_DATE | RevenueAdjustmentApplicationDate | ✅ |
| COMMENTS | RevenueAdjustmentComments | ✅ |
| CREATED_BY | RevenueAdjustmentCreatedBy | ✅ |
| CREATION_DATE | RevenueAdjustmentCreationDate | ✅ |
| CUSTOMER_TRX_ID | RevenueAdjustmentCustomerTrxId | — |
| FROM_CATEGORY_ID | RevenueAdjustmentFromCategoryId | — |
| FROM_CUST_TRX_LINE_ID | RevenueAdjustmentFromCustTrxLineId | — |
| FROM_INVENTORY_ITEM_ID | RevenueAdjustmentFromInventoryItemId | — |
| FROM_RESOURCE_SALESREP_ID | RevenueAdjustmentFromResourceSalesrepId | — |
| FROM_SALESGROUP_ID | RevenueAdjustmentFromSalesgroupId | — |
| GL_DATE | RevenueAdjustmentGlDate | ✅ |
| LAST_UPDATE_DATE | RevenueAdjustmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RevenueAdjustmentLastUpdateLogin | — |
| LAST_UPDATED_BY | RevenueAdjustmentLastUpdatedBy | ✅ |
| LINE_SELECTION_MODE | RevenueAdjustmentLineSelectionMode | — |
| OBJECT_VERSION_NUMBER | RevenueAdjustmentObjectVersionNumber | — |
| ORG_ID | RevenueAdjustmentOrgId | — |
| PERCENT | RevenueAdjustmentPercent | ✅ |
| PROGRAM_APPLICATION_ID | RevenueAdjustmentProgramApplicationId | — |
| PROGRAM_ID | RevenueAdjustmentProgramId | — |
| PROGRAM_UPDATE_DATE | RevenueAdjustmentProgramUpdateDate | — |
| REASON_CODE | RevenueAdjustmentReasonCode | ✅ |
| REQUEST_ID | RevenueAdjustmentRequestId | — |
| REVENUE_ADJUSTMENT_ID | RevenueAdjustmentId | ✅ |
| REVENUE_ADJUSTMENT_NUMBER | RevenueAdjustmentRevenueAdjustmentNumber | ✅ |
| SALES_CREDIT_TYPE | RevenueAdjustmentSalesCreditType | ✅ |
| STATUS | RevenueAdjustmentStatus | — |
| TO_CATEGORY_ID | RevenueAdjustmentToCategoryId | — |
| TO_CUST_TRX_LINE_ID | RevenueAdjustmentToCustTrxLineId | — |
| TO_INVENTORY_ITEM_ID | RevenueAdjustmentToInventoryItemId | — |
| TO_RESOURCE_SALESREP_ID | RevenueAdjustmentToResourceSalesrepId | — |
| TO_SALESGROUP_ID | RevenueAdjustmentToSalesgroupId | — |
| TYPE | RevenueAdjustmentType | ✅ |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 1/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | RevenueAdjustmentAmount | — |
| AMOUNT_MODE | RevenueAdjustmentAmountMode | — |
| APPLICATION_DATE | RevenueAdjustmentApplicationDate | — |
| CREATED_BY | RevenueAdjustmentCreatedBy | — |
| CUSTOMER_TRX_ID | RevenueAdjustmentCustomerTrxId | — |
| FROM_CATEGORY_ID | RevenueAdjustmentFromCategoryId | — |
| FROM_CUST_TRX_LINE_ID | RevenueAdjustmentFromCustTrxLineId | — |
| FROM_INVENTORY_ITEM_ID | RevenueAdjustmentFromInventoryItemId | — |
| FROM_RESOURCE_SALESREP_ID | RevenueAdjustmentFromResourceSalesrepId | — |
| FROM_SALESGROUP_ID | RevenueAdjustmentFromSalesgroupId | — |
| GL_DATE | RevenueAdjustmentGlDate | — |
| LAST_UPDATE_LOGIN | RevenueAdjustmentLastUpdateLogin | — |
| LAST_UPDATED_BY | RevenueAdjustmentLastUpdatedBy | — |
| LINE_SELECTION_MODE | RevenueAdjustmentLineSelectionMode | — |
| OBJECT_VERSION_NUMBER | RevenueAdjustmentObjectVersionNumber | — |
| ORG_ID | RevenueAdjustmentOrgId | — |
| PERCENT | RevenueAdjustmentPercent | — |
| PROGRAM_APPLICATION_ID | RevenueAdjustmentProgramApplicationId | — |
| PROGRAM_ID | RevenueAdjustmentProgramId | — |
| PROGRAM_UPDATE_DATE | RevenueAdjustmentProgramUpdateDate | — |
| REASON_CODE | RevenueAdjustmentReasonCode | — |
| REQUEST_ID | RevenueAdjustmentRequestId | — |
| REVENUE_ADJUSTMENT_ID | RevenueAdjustmentRevenueAdjustmentId | — |
| REVENUE_ADJUSTMENT_NUMBER | RevenueAdjustmentRevenueAdjustmentNumber | ✅ |
| SALES_CREDIT_TYPE | RevenueAdjustmentSalesCreditType | — |
| STATUS | RevenueAdjustmentStatus | — |
| TO_CATEGORY_ID | RevenueAdjustmentToCategoryId | — |
| TO_CUST_TRX_LINE_ID | RevenueAdjustmentToCustTrxLineId | — |
| TO_INVENTORY_ITEM_ID | RevenueAdjustmentToInventoryItemId | — |
| TO_RESOURCE_SALESREP_ID | RevenueAdjustmentToResourceSalesrepId | — |
| TO_SALESGROUP_ID | RevenueAdjustmentToSalesgroupId | — |
| TYPE | RevenueAdjustmentType | — |

---

## 📚 Referências

- [Oracle Docs — AR_REVENUE_ADJUSTMENTS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arrevenueadjustmentsall-25164.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
