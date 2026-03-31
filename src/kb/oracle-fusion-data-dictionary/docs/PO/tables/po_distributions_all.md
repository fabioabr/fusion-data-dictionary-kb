---
id: DOC-PO-116
doc_type: system-doc
title: "PO_DISTRIBUTIONS_ALL — Distribuicoes de Ordens de Compra"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - purchase-orders
  - po-transactions
  - compras
aliases:
  - PO_DISTRIBUTIONS_ALL
  - po_distributions_all
  - po-distributions-all
  - po-distributions
  - distribuicoes-de-ordens-de-compra
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_DISTRIBUTIONS_ALL

## 📌 Visão Geral

Armazena as **distribuicoes contabeis de linhas de ordens de compra**. Cada distribuicao define alocacao contabil — conta, centro de custo, projeto, percentual, quantidade e valores recebidos/faturados.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Contabilizacao:** Definicao de contas contabeis (CCID) para cada item.
- **Projetos:** Associacao de gastos a projetos e tarefas.
- **Encumbrances:** Reserva orcamentaria na aprovacao.
- **Matching:** Reconciliacao PO x Recebimento x Fatura (3-way match).
- **Relatorios financeiros:** Analise por conta, centro de custo, projeto.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PO_DISTRIBUTION_ID | NUMBER(18) | NOT NULL | PK | ID da distribuicao | — | 🟢 100% |
| 2 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho do PO | [[po_headers_all]] | 🟢 100% |
| 3 | PO_LINE_ID | NUMBER(18) | NOT NULL | FK | Linha do PO | [[po_lines_all]] | 🟢 100% |
| 4 | LINE_LOCATION_ID | NUMBER(18) | NOT NULL | FK | Schedule (entrega) | [[po_line_locations_all]] | 🟢 100% |
| 5 | DISTRIBUTION_NUM | NUMBER | NOT NULL | Identificacao | Numero da distribuicao | — | 🟢 100% |
| 6 | QUANTITY_ORDERED | NUMBER | NULL | Quantidade | Quantidade ordenada | — | 🟢 100% |
| 7 | QUANTITY_DELIVERED | NUMBER | NULL | Quantidade | Quantidade recebida | — | 🟢 100% |
| 8 | QUANTITY_BILLED | NUMBER | NULL | Quantidade | Quantidade faturada | — | 🟢 100% |
| 9 | QUANTITY_CANCELLED | NUMBER | NULL | Quantidade | Quantidade cancelada | — | 🟢 100% |
| 10 | CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | CCID — conta contabil | [[gl_code_combinations]] | 🟢 100% |
| 11 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | Contabilidade | Ledger | [[gl_ledgers]] | 🟢 95% |
| 12 | PROJECT_ID | NUMBER(18) | NULL | FK | Projeto | [[pjf_projects_all_b]] | 🟢 90% |
| 13 | TASK_ID | NUMBER(18) | NULL | FK | Tarefa do projeto | [[pjf_tasks_b]] | 🟢 90% |
| 14 | ENCUMBERED_FLAG | VARCHAR2(1) | NULL | Flag | Reserva orcamentaria (Y/N) | — | 🟢 90% |
| 15 | ENCUMBERED_AMOUNT | NUMBER | NULL | Financeiro | Valor da reserva | — | 🟢 90% |
| 16 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 100% |
| 17 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 18 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 19 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 20 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra ao qual a distribuição pertence)
- [[po_lines_all]] — via `PO_LINE_ID` (linha do PO à qual a distribuição pertence)
- [[po_line_locations_all]] — via `LINE_LOCATION_ID` (shipment do PO ao qual a distribuição pertence)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (conta contábil de encargo da distribuição do PO)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil da distribuição do PO)
- [[pjf_projects_all_b]] — via `PROJECT_ID` (projeto ao qual a distribuição do PO é imputada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Distribuicoes de um PO
```sql
SELECT PO_DISTRIBUTION_ID, DISTRIBUTION_NUM, QUANTITY_ORDERED,
       QUANTITY_DELIVERED, QUANTITY_BILLED, CODE_COMBINATION_ID
FROM   PO_DISTRIBUTIONS_ALL
WHERE  PO_HEADER_ID = :p_po_header_id
ORDER BY PO_LINE_ID, DISTRIBUTION_NUM;
```

---

## 🔒 Observações

- Tabela central para 3-way matching.
- `ENCUMBERED_FLAG = 'Y'` indica reserva orcamentaria ativa.
- Cada linha pode ter multiplas distribuicoes (rateio contabil).
- Filtrar por `ORG_ID` em consultas multi-org.

---

## 🔗 PVOs Relacionados

### [[assetinvoicepvo|AssetInvoicePVO]] (OTHER · BICC: 2/118)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PODistributionAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | PODistributionAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | PODistributionAccruedFlag | — |
| AMOUNT_BILLED | PODistributionAmountBilled | — |
| AMOUNT_CANCELLED | PODistributionAmountCancelled | — |
| AMOUNT_DELIVERED | PODistributionAmountDelivered | — |
| AMOUNT_FINANCED | PODistributionAmountFinanced | — |
| AMOUNT_ORDERED | PODistributionAmountOrdered | — |
| AMOUNT_RECOUPED | PODistributionAmountRecouped | — |
| AMOUNT_TO_ENCUMBER | PODistributionAmountToEncumber | — |
| AWARD_ID | PODistributionAwardId | — |
| BOM_RESOURCE_ID | PODistributionBomResourceId | — |
| BUDGET_ACCOUNT_ID | PODistributionBudgetAccountId | — |
| CODE_COMBINATION_ID | PODistributionCodeCombinationId | — |
| CREATED_BY | PODistributionCreatedBy | — |
| CREATION_DATE | PODistributionCreationDate | — |
| DELIVER_TO_LOCATION_ID | PODistributionDeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | PODistributionDeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | PODistributionDestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PODistributionDestVarianceAccountId | — |
| DESTINATION_CONTEXT | PODistributionDestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PODistributionDestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | PODistributionDestinationSubinventory | — |
| DESTINATION_TYPE_CODE | PODistributionDestinationTypeCode | — |
| DIST_INTENDED_USE | PODistributionDistIntendedUse | — |
| DISTRIBUTION_NUM | PODistributionDistributionNum | ✅ |
| DISTRIBUTION_TYPE | PODistributionDistributionType | — |
| ENCUMBERED_AMOUNT | PODistributionEncumberedAmount | — |
| ENCUMBERED_FLAG | PODistributionEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PODistributionEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PODistributionFailedFundsLookupCode | — |
| GL_CANCELLED_DATE | PODistributionGlCancelledDate | — |
| GL_CLOSED_DATE | PODistributionGlClosedDate | — |
| GL_ENCUMBERED_DATE | PODistributionGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PODistributionGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PODistributionGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PODistributionInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PODistributionInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PODistributionInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PODistributionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PODistributionJobDefinitionPackage | — |
| KANBAN_CARD_ID | PODistributionKanbanCardId | — |
| LAST_UPDATE_DATE | PODistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PODistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | PODistributionLastUpdatedBy | — |
| LINE_LOCATION_ID | PODistributionLineLocationId | — |
| NONRECOVERABLE_TAX | PODistributionNonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | PODistributionObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PODistributionOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PODistributionOkeContractLineId | — |
| PJC_BILLABLE_FLAG | PODistributionPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | PODistributionPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | PODistributionPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | PODistributionPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | PODistributionPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | PODistributionPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | PODistributionPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | PODistributionPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | PODistributionPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | PODistributionPJC_PROJECT_ID | — |
| PJC_RESERVED_ATTRIBUTE1 | PODistributionPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_RESERVED_ATTRIBUTE10 | PODistributionPJC_RESERVED_ATTRIBUTE10 | — |
| PJC_RESERVED_ATTRIBUTE2 | PODistributionPJC_RESERVED_ATTRIBUTE2 | — |
| PJC_RESERVED_ATTRIBUTE3 | PODistributionPJC_RESERVED_ATTRIBUTE3 | — |
| PJC_RESERVED_ATTRIBUTE4 | PODistributionPJC_RESERVED_ATTRIBUTE4 | — |
| PJC_RESERVED_ATTRIBUTE5 | PODistributionPJC_RESERVED_ATTRIBUTE5 | — |
| PJC_RESERVED_ATTRIBUTE6 | PODistributionPJC_RESERVED_ATTRIBUTE6 | — |
| PJC_RESERVED_ATTRIBUTE7 | PODistributionPJC_RESERVED_ATTRIBUTE7 | — |
| PJC_RESERVED_ATTRIBUTE8 | PODistributionPJC_RESERVED_ATTRIBUTE8 | — |
| PJC_RESERVED_ATTRIBUTE9 | PODistributionPJC_RESERVED_ATTRIBUTE9 | — |
| PJC_TASK_ID | PODistributionPJC_TASK_ID | — |
| PJC_USER_DEF_ATTRIBUTE1 | PODistributionPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | PODistributionPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | PODistributionPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | PODistributionPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | PODistributionPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | PODistributionPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | PODistributionPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | PODistributionPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | PODistributionPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | PODistributionPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | PODistributionPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | PODistributionPoDistributionId | — |
| PO_HEADER_ID | PODistributionPoHeaderId | — |
| PO_LINE_ID | PODistributionPoLineId | — |
| PRC_BU_ID | PODistributionPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PODistributionPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PODistributionProgramAppName | — |
| PROGRAM_NAME | PODistributionProgramName | — |
| QUANTITY_BILLED | PODistributionQuantityBilled | — |
| QUANTITY_CANCELLED | PODistributionQuantityCancelled | — |
| QUANTITY_DELIVERED | PODistributionQuantityDelivered | — |
| QUANTITY_FINANCED | PODistributionQuantityFinanced | — |
| QUANTITY_ORDERED | PODistributionQuantityOrdered | — |
| QUANTITY_RECOUPED | PODistributionQuantityRecouped | — |
| RATE | PODistributionRate | — |
| RATE_DATE | PODistributionRateDate | — |
| RECOVERABLE_TAX | PODistributionRecoverableTax | — |
| RECOVERY_RATE | PODistributionRecoveryRate | — |
| REQ_BU_ID | PODistributionReqBuId | — |
| REQ_DISTRIBUTION_ID | PODistributionReqDistributionId | — |
| REQ_HEADER_REFERENCE_NUM | PODistributionReqHeaderReferenceNum | — |
| REQ_LINE_REFERENCE_NUM | PODistributionReqLineReferenceNum | — |
| REQUEST_ID | PODistributionRequestId | — |
| RETAINAGE_RELEASED_AMOUNT | PODistributionRetainageReleasedAmount | — |
| RETAINAGE_WITHHELD_AMOUNT | PODistributionRetainageWithheldAmount | — |
| SET_OF_BOOKS_ID | PODistributionSetOfBooksId | — |
| SOURCE_DISTRIBUTION_ID | PODistributionSourceDistributionId | — |
| TAX_ATTRIBUTE_UPDATE_CODE | PODistributionTaxAttributeUpdateCode | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PODistributionTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PODistributionUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PODistributionUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PODistributionVarianceAccountId | — |
| WIP_ENTITY_ID | PODistributionWipEntityId | — |
| WIP_LINE_ID | PODistributionWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PODistributionWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PODistributionWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PODistributionWipResourceSeqNum | — |

### [[draftpurchaseorderdistributionpvo|DraftPurchaseOrderDistributionPVO]] (PO · BICC: 2/122)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PurchaseOrderDistributionAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | PurchaseOrderDistributionAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | PurchaseOrderDistributionAccruedFlag | — |
| AMOUNT_BILLED | PurchaseOrderDistributionAmountBilled | — |
| AMOUNT_CANCELLED | PurchaseOrderDistributionAmountCancelled | — |
| AMOUNT_DELIVERED | PurchaseOrderDistributionAmountDelivered | — |
| AMOUNT_FINANCED | PurchaseOrderDistributionAmountFinanced | — |
| AMOUNT_ORDERED | PurchaseOrderDistributionAmountOrdered | — |
| AMOUNT_RECOUPED | PurchaseOrderDistributionAmountRecouped | — |
| AMOUNT_TO_ENCUMBER | PurchaseOrderDistributionAmountToEncumber | — |
| AWARD_ID | PurchaseOrderDistributionAwardId | — |
| BOM_RESOURCE_ID | PurchaseOrderDistributionBomResourceId | — |
| BUDGET_ACCOUNT_ID | PurchaseOrderDistributionBudgetAccountId | — |
| CODE_COMBINATION_ID | PurchaseOrderDistributionCodeCombinationId | — |
| CREATED_BY | PurchaseOrderDistributionCreatedBy | — |
| CREATION_DATE | PurchaseOrderDistributionCreationDate | — |
| DELIVER_TO_CUST_CONTACT_ID | PurchaseOrderDistributionDeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | PurchaseOrderDistributionDeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | PurchaseOrderDistributionDeliverToCustLocationId | ✅ |
| DELIVER_TO_LOCATION_ID | PurchaseOrderDistributionDeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | PurchaseOrderDistributionDeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | PurchaseOrderDistributionDestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionDestVarianceAccountId | — |
| DESTINATION_CONTEXT | PurchaseOrderDistributionDestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PurchaseOrderDistributionDestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | PurchaseOrderDistributionDestinationSubinventory | — |
| DESTINATION_TYPE_CODE | PurchaseOrderDistributionDestinationTypeCode | — |
| DIST_INTENDED_USE | PurchaseOrderDistributionDistIntendedUse | — |
| DISTRIBUTION_NUM | PurchaseOrderDistributionDistributionNum | — |
| DISTRIBUTION_TYPE | PurchaseOrderDistributionDistributionType | — |
| ENCUMBERED_AMOUNT | PurchaseOrderDistributionEncumberedAmount | — |
| ENCUMBERED_FLAG | PurchaseOrderDistributionEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PurchaseOrderDistributionEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PurchaseOrderDistributionFailedFundsLookupCode | — |
| FUNDS_STATUS | PurchaseOrderDistributionFundsStatus | — |
| GL_CANCELLED_DATE | PurchaseOrderDistributionGlCancelledDate | — |
| GL_CLOSED_DATE | PurchaseOrderDistributionGlClosedDate | — |
| GL_ENCUMBERED_DATE | PurchaseOrderDistributionGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PurchaseOrderDistributionGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PurchaseOrderDistributionGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PurchaseOrderDistributionInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PurchaseOrderDistributionInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PurchaseOrderDistributionInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PurchaseOrderDistributionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderDistributionJobDefinitionPackage | — |
| KANBAN_CARD_ID | PurchaseOrderDistributionKanbanCardId | — |
| LAST_UPDATE_DATE | PurchaseOrderDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchaseOrderDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchaseOrderDistributionLastUpdatedBy | — |
| LINE_LOCATION_ID | PurchaseOrderDistributionLineLocationId | — |
| NONRECOVERABLE_TAX | PurchaseOrderDistributionNonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PurchaseOrderDistributionOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PurchaseOrderDistributionOkeContractLineId | — |
| PJC_BILLABLE_FLAG | PurchaseOrderDistributionPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | PurchaseOrderDistributionPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | PurchaseOrderDistributionPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | PurchaseOrderDistributionPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | PurchaseOrderDistributionPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPJC_PROJECT_ID | — |
| PJC_RESERVED_ATTRIBUTE1 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_RESERVED_ATTRIBUTE10 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE10 | — |
| PJC_RESERVED_ATTRIBUTE2 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE2 | — |
| PJC_RESERVED_ATTRIBUTE3 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE3 | — |
| PJC_RESERVED_ATTRIBUTE4 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE4 | — |
| PJC_RESERVED_ATTRIBUTE5 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE5 | — |
| PJC_RESERVED_ATTRIBUTE6 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE6 | — |
| PJC_RESERVED_ATTRIBUTE7 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE7 | — |
| PJC_RESERVED_ATTRIBUTE8 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE8 | — |
| PJC_RESERVED_ATTRIBUTE9 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE9 | — |
| PJC_TASK_ID | PurchaseOrderDistributionPJC_TASK_ID | — |
| PJC_USER_DEF_ATTRIBUTE1 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | PurchaseOrderDistributionPoDistributionId | — |
| PO_HEADER_ID | PurchaseOrderDistributionPoHeaderId | — |
| PO_LINE_ID | PurchaseOrderDistributionPoLineId | — |
| PRC_BU_ID | PurchaseOrderDistributionPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PurchaseOrderDistributionPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PurchaseOrderDistributionProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderDistributionProgramName | — |
| QUANTITY_BILLED | PurchaseOrderDistributionQuantityBilled | — |
| QUANTITY_CANCELLED | PurchaseOrderDistributionQuantityCancelled | — |
| QUANTITY_DELIVERED | PurchaseOrderDistributionQuantityDelivered | — |
| QUANTITY_FINANCED | PurchaseOrderDistributionQuantityFinanced | — |
| QUANTITY_ORDERED | PurchaseOrderDistributionQuantityOrdered | — |
| QUANTITY_RECOUPED | PurchaseOrderDistributionQuantityRecouped | — |
| RATE | PurchaseOrderDistributionRate | — |
| RATE_DATE | PurchaseOrderDistributionRateDate | — |
| RECOVERABLE_TAX | PurchaseOrderDistributionRecoverableTax | — |
| RECOVERY_RATE | PurchaseOrderDistributionRecoveryRate | — |
| REQ_BU_ID | PurchaseOrderDistributionReqBuId | — |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionReqDistributionId | — |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionReqHeaderReferenceNum | — |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionReqLineReferenceNum | — |
| REQUEST_ID | PurchaseOrderDistributionRequestId | — |
| RETAINAGE_RELEASED_AMOUNT | PurchaseOrderDistributionRetainageReleasedAmount | — |
| RETAINAGE_WITHHELD_AMOUNT | PurchaseOrderDistributionRetainageWithheldAmount | — |
| SET_OF_BOOKS_ID | PurchaseOrderDistributionSetOfBooksId | — |
| SOURCE_DISTRIBUTION_ID | PurchaseOrderDistributionSourceDistributionId | — |
| TAX_ATTRIBUTE_UPDATE_CODE | PurchaseOrderDistributionTaxAttributeUpdateCode | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PurchaseOrderDistributionTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PurchaseOrderDistributionUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PurchaseOrderDistributionUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionVarianceAccountId | — |
| WIP_ENTITY_ID | PurchaseOrderDistributionWipEntityId | — |
| WIP_LINE_ID | PurchaseOrderDistributionWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PurchaseOrderDistributionWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PurchaseOrderDistributionWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PurchaseOrderDistributionWipResourceSeqNum | — |

### [[draftpurchaseorderdistributionrefpvo|DraftPurchaseOrderDistributionRefPVO]] (PO · BICC: 12/122)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PurchaseOrderDistributionAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | PurchaseOrderDistributionAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | PurchaseOrderDistributionAccruedFlag | — |
| AMOUNT_BILLED | PurchaseOrderDistributionAmountBilled | — |
| AMOUNT_CANCELLED | PurchaseOrderDistributionAmountCancelled | — |
| AMOUNT_DELIVERED | PurchaseOrderDistributionAmountDelivered | — |
| AMOUNT_FINANCED | PurchaseOrderDistributionAmountFinanced | — |
| AMOUNT_ORDERED | PurchaseOrderDistributionAmountOrdered | — |
| AMOUNT_RECOUPED | PurchaseOrderDistributionAmountRecouped | — |
| AMOUNT_TO_ENCUMBER | PurchaseOrderDistributionAmountToEncumber | — |
| AWARD_ID | PurchaseOrderDistributionAwardId | — |
| BOM_RESOURCE_ID | PurchaseOrderDistributionBomResourceId | — |
| BUDGET_ACCOUNT_ID | PurchaseOrderDistributionBudgetAccountId | — |
| CODE_COMBINATION_ID | PurchaseOrderDistributionCodeCombinationId | — |
| CREATED_BY | PurchaseOrderDistributionCreatedBy | — |
| CREATION_DATE | PurchaseOrderDistributionCreationDate | — |
| DELIVER_TO_CUST_CONTACT_ID | PurchaseOrderDistributionDeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | PurchaseOrderDistributionDeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | PurchaseOrderDistributionDeliverToCustLocationId | — |
| DELIVER_TO_LOCATION_ID | PurchaseOrderDistributionDeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | PurchaseOrderDistributionDeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | PurchaseOrderDistributionDestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionDestVarianceAccountId | — |
| DESTINATION_CONTEXT | PurchaseOrderDistributionDestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PurchaseOrderDistributionDestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | PurchaseOrderDistributionDestinationSubinventory | — |
| DESTINATION_TYPE_CODE | PurchaseOrderDistributionDestinationTypeCode | ✅ |
| DIST_INTENDED_USE | PurchaseOrderDistributionDistIntendedUse | — |
| DISTRIBUTION_NUM | PurchaseOrderDistributionDistributionNum | ✅ |
| DISTRIBUTION_TYPE | PurchaseOrderDistributionDistributionType | — |
| ENCUMBERED_AMOUNT | PurchaseOrderDistributionEncumberedAmount | — |
| ENCUMBERED_FLAG | PurchaseOrderDistributionEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PurchaseOrderDistributionEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PurchaseOrderDistributionFailedFundsLookupCode | — |
| FUNDS_STATUS | PurchaseOrderDistributionFundsStatus | ✅ |
| GL_CANCELLED_DATE | PurchaseOrderDistributionGlCancelledDate | ✅ |
| GL_CLOSED_DATE | PurchaseOrderDistributionGlClosedDate | — |
| GL_ENCUMBERED_DATE | PurchaseOrderDistributionGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PurchaseOrderDistributionGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PurchaseOrderDistributionGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PurchaseOrderDistributionInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PurchaseOrderDistributionInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PurchaseOrderDistributionInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PurchaseOrderDistributionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderDistributionJobDefinitionPackage | — |
| KANBAN_CARD_ID | PurchaseOrderDistributionKanbanCardId | — |
| LAST_UPDATE_DATE | PurchaseOrderDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchaseOrderDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchaseOrderDistributionLastUpdatedBy | — |
| LINE_LOCATION_ID | PurchaseOrderDistributionLineLocationId | — |
| NONRECOVERABLE_TAX | PurchaseOrderDistributionNonrecoverableTax | ✅ |
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PurchaseOrderDistributionOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PurchaseOrderDistributionOkeContractLineId | — |
| PJC_BILLABLE_FLAG | PurchaseOrderDistributionPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | PurchaseOrderDistributionPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | PurchaseOrderDistributionPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | PurchaseOrderDistributionPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | PurchaseOrderDistributionPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPJC_PROJECT_ID | — |
| PJC_RESERVED_ATTRIBUTE1 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_RESERVED_ATTRIBUTE10 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE10 | — |
| PJC_RESERVED_ATTRIBUTE2 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE2 | — |
| PJC_RESERVED_ATTRIBUTE3 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE3 | — |
| PJC_RESERVED_ATTRIBUTE4 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE4 | — |
| PJC_RESERVED_ATTRIBUTE5 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE5 | — |
| PJC_RESERVED_ATTRIBUTE6 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE6 | — |
| PJC_RESERVED_ATTRIBUTE7 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE7 | — |
| PJC_RESERVED_ATTRIBUTE8 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE8 | — |
| PJC_RESERVED_ATTRIBUTE9 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE9 | — |
| PJC_TASK_ID | PurchaseOrderDistributionPJC_TASK_ID | — |
| PJC_USER_DEF_ATTRIBUTE1 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | PurchaseOrderDistributionPoDistributionId | — |
| PO_HEADER_ID | PurchaseOrderDistributionPoHeaderId | — |
| PO_LINE_ID | PurchaseOrderDistributionPoLineId | — |
| PRC_BU_ID | PurchaseOrderDistributionPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PurchaseOrderDistributionPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PurchaseOrderDistributionProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderDistributionProgramName | — |
| QUANTITY_BILLED | PurchaseOrderDistributionQuantityBilled | — |
| QUANTITY_CANCELLED | PurchaseOrderDistributionQuantityCancelled | ✅ |
| QUANTITY_DELIVERED | PurchaseOrderDistributionQuantityDelivered | — |
| QUANTITY_FINANCED | PurchaseOrderDistributionQuantityFinanced | — |
| QUANTITY_ORDERED | PurchaseOrderDistributionQuantityOrdered | ✅ |
| QUANTITY_RECOUPED | PurchaseOrderDistributionQuantityRecouped | — |
| RATE | PurchaseOrderDistributionRate | ✅ |
| RATE_DATE | PurchaseOrderDistributionRateDate | — |
| RECOVERABLE_TAX | PurchaseOrderDistributionRecoverableTax | ✅ |
| RECOVERY_RATE | PurchaseOrderDistributionRecoveryRate | — |
| REQ_BU_ID | PurchaseOrderDistributionReqBuId | — |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionReqDistributionId | ✅ |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionReqHeaderReferenceNum | ✅ |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionReqLineReferenceNum | — |
| REQUEST_ID | PurchaseOrderDistributionRequestId | — |
| RETAINAGE_RELEASED_AMOUNT | PurchaseOrderDistributionRetainageReleasedAmount | — |
| RETAINAGE_WITHHELD_AMOUNT | PurchaseOrderDistributionRetainageWithheldAmount | — |
| SET_OF_BOOKS_ID | PurchaseOrderDistributionSetOfBooksId | — |
| SOURCE_DISTRIBUTION_ID | PurchaseOrderDistributionSourceDistributionId | — |
| TAX_ATTRIBUTE_UPDATE_CODE | PurchaseOrderDistributionTaxAttributeUpdateCode | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PurchaseOrderDistributionTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PurchaseOrderDistributionUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PurchaseOrderDistributionUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionVarianceAccountId | — |
| WIP_ENTITY_ID | PurchaseOrderDistributionWipEntityId | — |
| WIP_LINE_ID | PurchaseOrderDistributionWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PurchaseOrderDistributionWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PurchaseOrderDistributionWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PurchaseOrderDistributionWipResourceSeqNum | — |

### [[inventorysupplypvo|InventorySupplyPVO]] (OTHER · BICC: 6/101)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PurchaseOrderDistributionPEOAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | PurchaseOrderDistributionPEOAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | PurchaseOrderDistributionPEOAccruedFlag | — |
| AMOUNT_BILLED | PurchaseOrderDistributionPEOAmountBilled | — |
| AMOUNT_CANCELLED | PurchaseOrderDistributionPEOAmountCancelled | — |
| AMOUNT_DELIVERED | PurchaseOrderDistributionPEOAmountDelivered | — |
| AMOUNT_FINANCED | PurchaseOrderDistributionPEOAmountFinanced | — |
| AMOUNT_ORDERED | PurchaseOrderDistributionPEOAmountOrdered | — |
| AMOUNT_RECOUPED | PurchaseOrderDistributionPEOAmountRecouped | — |
| AMOUNT_TO_ENCUMBER | PurchaseOrderDistributionPEOAmountToEncumber | — |
| AWARD_ID | PurchaseOrderDistributionPEOAwardId | — |
| BOM_RESOURCE_ID | PurchaseOrderDistributionPEOBomResourceId | — |
| BUDGET_ACCOUNT_ID | PurchaseOrderDistributionPEOBudgetAccountId | — |
| BUDGET_DATE | PurchaseOrderDistributionPEOBudgetDate | — |
| CLOSE_BUDGET_DATE | PurchaseOrderDistributionPEOCloseBudgetDate | — |
| CODE_COMBINATION_ID | PurchaseOrderDistributionPEOCodeCombinationId | — |
| CONSIGNMENT_QUANTITY | PurchaseOrderDistributionPEOConsignmentQuantity | — |
| CREATED_BY | PurchaseOrderDistributionPEOCreatedBy | — |
| CREATION_DATE | PurchaseOrderDistributionPEOCreationDate | — |
| DELIVER_TO_CUST_CONTACT_ID | PurchaseOrderDistributionPEODeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | PurchaseOrderDistributionPEODeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | PurchaseOrderDistributionPEODeliverToCustLocationId | — |
| DELIVER_TO_LOCATION_ID | PurchaseOrderDistributionPEODeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | PurchaseOrderDistributionPEODeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | PurchaseOrderDistributionPEODestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEODestVarianceAccountId | — |
| DESTINATION_CONTEXT | PurchaseOrderDistributionPEODestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PurchaseOrderDistributionPEODestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | PurchaseOrderDistributionPEODestinationSubinventory | — |
| DESTINATION_TYPE_CODE | PurchaseOrderDistributionPEODestinationTypeCode | — |
| DIST_INTENDED_USE | PurchaseOrderDistributionPEODistIntendedUse | — |
| DISTRIBUTION_NUM | PurchaseOrderDistributionPEODistributionNum | ✅ |
| DISTRIBUTION_TYPE | PurchaseOrderDistributionPEODistributionType | — |
| ENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOEncumberedAmount | — |
| ENCUMBERED_FLAG | PurchaseOrderDistributionPEOEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PurchaseOrderDistributionPEOEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PurchaseOrderDistributionPEOFailedFundsLookupCode | — |
| FUNDS_STATUS | PurchaseOrderDistributionPEOFundsStatus | — |
| GL_CANCELLED_DATE | PurchaseOrderDistributionPEOGlCancelledDate | — |
| GL_CLOSED_DATE | PurchaseOrderDistributionPEOGlClosedDate | — |
| GL_ENCUMBERED_DATE | PurchaseOrderDistributionPEOGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PurchaseOrderDistributionPEOGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PurchaseOrderDistributionPEOGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PurchaseOrderDistributionPEOInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PurchaseOrderDistributionPEOInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PurchaseOrderDistributionPEOInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PurchaseOrderDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderDistributionPEOJobDefinitionPackage | — |
| KANBAN_CARD_ID | PurchaseOrderDistributionPEOKanbanCardId | — |
| LAST_UPDATE_DATE | PurchaseOrderDistributionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchaseOrderDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchaseOrderDistributionPEOLastUpdatedBy | — |
| LINE_LOCATION_ID | PurchaseOrderDistributionPEOLineLocationId | — |
| NONRECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEONonrecoverableInclusiveTax | — |
| NONRECOVERABLE_TAX | PurchaseOrderDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionPEOObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PurchaseOrderDistributionPEOOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOOkeContractLineId | — |
| ORIGINAL_DISTRIBUTION_ID | PurchaseOrderDistributionPEOOriginalDistributionId | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPEOPjcProjectId | — |
| PJC_TASK_ID | PurchaseOrderDistributionPEOPjcTaskId | — |
| PO_DISTRIBUTION_ID | PurchaseOrderDistributionPEOPoDistributionId | — |
| PO_HEADER_ID | PurchaseOrderDistributionPEOPoHeaderId | — |
| PO_LINE_ID | PurchaseOrderDistributionPEOPoLineId | — |
| PRC_BU_ID | PurchaseOrderDistributionPEOPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PurchaseOrderDistributionPEOPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PurchaseOrderDistributionPEOProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderDistributionPEOProgramName | — |
| QUANTITY_BILLED | PurchaseOrderDistributionPEOQuantityBilled | — |
| QUANTITY_CANCELLED | PurchaseOrderDistributionPEOQuantityCancelled | — |
| QUANTITY_DELIVERED | PurchaseOrderDistributionPEOQuantityDelivered | ✅ |
| QUANTITY_FINANCED | PurchaseOrderDistributionPEOQuantityFinanced | — |
| QUANTITY_ORDERED | PurchaseOrderDistributionPEOQuantityOrdered | ✅ |
| QUANTITY_RECOUPED | PurchaseOrderDistributionPEOQuantityRecouped | — |
| RATE | PurchaseOrderDistributionPEORate | — |
| RATE_DATE | PurchaseOrderDistributionPEORateDate | — |
| RECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEORecoverableInclusiveTax | — |
| RECOVERABLE_TAX | PurchaseOrderDistributionPEORecoverableTax | — |
| RECOVERY_RATE | PurchaseOrderDistributionPEORecoveryRate | — |
| REQ_BU_ID | PurchaseOrderDistributionPEOReqBuId | — |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionPEOReqDistributionId | — |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionPEOReqHeaderReferenceNum | — |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionPEOReqLineReferenceNum | — |
| REQUEST_ID | PurchaseOrderDistributionPEORequestId | — |
| RETAINAGE_RELEASED_AMOUNT | PurchaseOrderDistributionPEORetainageReleasedAmount | — |
| RETAINAGE_WITHHELD_AMOUNT | PurchaseOrderDistributionPEORetainageWithheldAmount | — |
| SET_OF_BOOKS_ID | PurchaseOrderDistributionPEOSetOfBooksId | — |
| SHIPPING_UOM_QTY_DELIVERED | PurchaseOrderDistributionPEOShippingUomQtyDelivered | ✅ |
| SHIPPING_UOM_QUANTITY | PurchaseOrderDistributionPEOShippingUomQuantity | ✅ |
| SOURCE_DISTRIBUTION_ID | PurchaseOrderDistributionPEOSourceDistributionId | — |
| TAX_ATTRIBUTE_UPDATE_CODE | PurchaseOrderDistributionPEOTaxAttributeUpdateCode | — |
| TAX_EXCLUSIVE_AMOUNT | PurchaseOrderDistributionPEOTaxExclusiveAmount | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PurchaseOrderDistributionPEOTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PurchaseOrderDistributionPEOUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEOVarianceAccountId | — |
| WIP_ENTITY_ID | PurchaseOrderDistributionPEOWipEntityId | — |
| WIP_LINE_ID | PurchaseOrderDistributionPEOWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PurchaseOrderDistributionPEOWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PurchaseOrderDistributionPEOWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PurchaseOrderDistributionPEOWipResourceSeqNum | — |

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISTRIBUTION_NUM | PoDistributionDistributionNum | ✅ |
| PO_DISTRIBUTION_ID | PoDistributionPoDistributionId | — |

### [[maintenancewooperationspvo|MaintenanceWOOperationsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PurchaseOrderDistributionPEOAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | PurchaseOrderDistributionPEOAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | PurchaseOrderDistributionPEOAccruedFlag | — |
| AMOUNT_BILLED | PurchaseOrderDistributionPEOAmountBilled | — |
| AMOUNT_CANCELLED | PurchaseOrderDistributionPEOAmountCancelled | — |
| AMOUNT_DELIVERED | PurchaseOrderDistributionPEOAmountDelivered | — |
| AMOUNT_FINANCED | PurchaseOrderDistributionPEOAmountFinanced | — |
| AMOUNT_ORDERED | PurchaseOrderDistributionPEOAmountOrdered | — |
| AMOUNT_RECOUPED | PurchaseOrderDistributionPEOAmountRecouped | — |
| AMOUNT_TO_ENCUMBER | PurchaseOrderDistributionPEOAmountToEncumber | — |
| AWARD_ID | PurchaseOrderDistributionPEOAwardId | — |
| BOM_RESOURCE_ID | PurchaseOrderDistributionPEOBomResourceId | — |
| BUDGET_ACCOUNT_ID | PurchaseOrderDistributionPEOBudgetAccountId | — |
| BUDGET_DATE | PurchaseOrderDistributionPEOBudgetDate | — |
| CLOSE_BUDGET_DATE | PurchaseOrderDistributionPEOCloseBudgetDate | — |
| CODE_COMBINATION_ID | PurchaseOrderDistributionPEOCodeCombinationId | — |
| CONSIGNMENT_QUANTITY | PurchaseOrderDistributionPEOConsignmentQuantity | — |
| CREATED_BY | PurchaseOrderDistributionPEOCreatedBy | — |
| CREATION_DATE | PurchaseOrderDistributionPEOCreationDate | — |
| DELIVER_TO_CUST_CONTACT_ID | PurchaseOrderDistributionPEODeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | PurchaseOrderDistributionPEODeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | PurchaseOrderDistributionPEODeliverToCustLocationId | — |
| DELIVER_TO_LOCATION_ID | PurchaseOrderDistributionPEODeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | PurchaseOrderDistributionPEODeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | PurchaseOrderDistributionPEODestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEODestVarianceAccountId | — |
| DESTINATION_CONTEXT | PurchaseOrderDistributionPEODestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PurchaseOrderDistributionPEODestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | PurchaseOrderDistributionPEODestinationSubinventory | — |
| DESTINATION_TYPE_CODE | PurchaseOrderDistributionPEODestinationTypeCode | — |
| DIST_INTENDED_USE | PurchaseOrderDistributionPEODistIntendedUse | — |
| DISTRIBUTION_NUM | PurchaseOrderDistributionPEODistributionNum | — |
| DISTRIBUTION_TYPE | PurchaseOrderDistributionPEODistributionType | — |
| ENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOEncumberedAmount | — |
| ENCUMBERED_FLAG | PurchaseOrderDistributionPEOEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PurchaseOrderDistributionPEOEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PurchaseOrderDistributionPEOFailedFundsLookupCode | — |
| FUNDS_STATUS | PurchaseOrderDistributionPEOFundsStatus | — |
| GL_CANCELLED_DATE | PurchaseOrderDistributionPEOGlCancelledDate | — |
| GL_CLOSED_DATE | PurchaseOrderDistributionPEOGlClosedDate | — |
| GL_ENCUMBERED_DATE | PurchaseOrderDistributionPEOGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PurchaseOrderDistributionPEOGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PurchaseOrderDistributionPEOGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PurchaseOrderDistributionPEOInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PurchaseOrderDistributionPEOInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PurchaseOrderDistributionPEOInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PurchaseOrderDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderDistributionPEOJobDefinitionPackage | — |
| KANBAN_CARD_ID | PurchaseOrderDistributionPEOKanbanCardId | — |
| LAST_UPDATE_DATE | PurchaseOrderDistributionPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | PurchaseOrderDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchaseOrderDistributionPEOLastUpdatedBy | — |
| LINE_LOCATION_ID | PurchaseOrderDistributionPEOLineLocationId | — |
| NONRECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEONonrecoverableInclusiveTax | — |
| NONRECOVERABLE_TAX | PurchaseOrderDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionPEOObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PurchaseOrderDistributionPEOOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOOkeContractLineId | — |
| ORIGINAL_DISTRIBUTION_ID | PurchaseOrderDistributionPEOOriginalDistributionId | — |
| PJC_BILLABLE_FLAG | PurchaseOrderDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | PurchaseOrderDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | PurchaseOrderDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | PurchaseOrderDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPEOPJC_PROJECT_ID | — |
| PJC_RESERVED_ATTRIBUTE1 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_RESERVED_ATTRIBUTE10 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE10 | — |
| PJC_RESERVED_ATTRIBUTE2 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE2 | — |
| PJC_RESERVED_ATTRIBUTE3 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE3 | — |
| PJC_RESERVED_ATTRIBUTE4 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE4 | — |
| PJC_RESERVED_ATTRIBUTE5 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE5 | — |
| PJC_RESERVED_ATTRIBUTE6 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE6 | — |
| PJC_RESERVED_ATTRIBUTE7 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE7 | — |
| PJC_RESERVED_ATTRIBUTE8 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE8 | — |
| PJC_RESERVED_ATTRIBUTE9 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE9 | — |
| PJC_TASK_ID | PurchaseOrderDistributionPEOPJC_TASK_ID | — |
| PJC_USER_DEF_ATTRIBUTE1 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPEOPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | PurchaseOrderDistributionPEOPoDistributionId | — |
| PO_HEADER_ID | PurchaseOrderDistributionPEOPoHeaderId | — |
| PO_LINE_ID | PurchaseOrderDistributionPEOPoLineId | — |
| PRC_BU_ID | PurchaseOrderDistributionPEOPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PurchaseOrderDistributionPEOPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PurchaseOrderDistributionPEOProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderDistributionPEOProgramName | — |
| QUANTITY_BILLED | PurchaseOrderDistributionPEOQuantityBilled | — |
| QUANTITY_CANCELLED | PurchaseOrderDistributionPEOQuantityCancelled | — |
| QUANTITY_DELIVERED | PurchaseOrderDistributionPEOQuantityDelivered | — |
| QUANTITY_FINANCED | PurchaseOrderDistributionPEOQuantityFinanced | — |
| QUANTITY_ORDERED | PurchaseOrderDistributionPEOQuantityOrdered | — |
| QUANTITY_RECOUPED | PurchaseOrderDistributionPEOQuantityRecouped | — |
| RATE | PurchaseOrderDistributionPEORate | — |
| RATE_DATE | PurchaseOrderDistributionPEORateDate | — |
| RECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEORecoverableInclusiveTax | — |
| RECOVERABLE_TAX | PurchaseOrderDistributionPEORecoverableTax | — |
| RECOVERY_RATE | PurchaseOrderDistributionPEORecoveryRate | — |
| REQ_BU_ID | PurchaseOrderDistributionPEOReqBuId | — |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionPEOReqDistributionId | — |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionPEOReqHeaderReferenceNum | — |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionPEOReqLineReferenceNum | — |
| REQUEST_ID | PurchaseOrderDistributionPEORequestId | — |
| RETAINAGE_RELEASED_AMOUNT | PurchaseOrderDistributionPEORetainageReleasedAmount | — |
| RETAINAGE_WITHHELD_AMOUNT | PurchaseOrderDistributionPEORetainageWithheldAmount | — |
| SET_OF_BOOKS_ID | PurchaseOrderDistributionPEOSetOfBooksId | — |
| SOURCE_DISTRIBUTION_ID | PurchaseOrderDistributionPEOSourceDistributionId | — |
| TAX_ATTRIBUTE_UPDATE_CODE | PurchaseOrderDistributionPEOTaxAttributeUpdateCode | — |
| TAX_EXCLUSIVE_AMOUNT | PurchaseOrderDistributionPEOTaxExclusiveAmount | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PurchaseOrderDistributionPEOTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PurchaseOrderDistributionPEOUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEOVarianceAccountId | — |
| WIP_ENTITY_ID | PurchaseOrderDistributionPEOWipEntityId | — |
| WIP_LINE_ID | PurchaseOrderDistributionPEOWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PurchaseOrderDistributionPEOWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PurchaseOrderDistributionPEOWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PurchaseOrderDistributionPEOWipResourceSeqNum | — |

### [[maintenancewoprocurementpopvo|MaintenanceWOProcurementPOPVO]] (OTHER · BICC: 10/110)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PurchaseOrderDistributionPEOAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | PurchaseOrderDistributionPEOAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | PurchaseOrderDistributionPEOAccruedFlag | — |
| AMOUNT_BILLED | PurchaseOrderDistributionPEOAmountBilled | — |
| AMOUNT_CANCELLED | PurchaseOrderDistributionPEOAmountCancelled | ✅ |
| AMOUNT_DELIVERED | PurchaseOrderDistributionPEOAmountDelivered | — |
| AMOUNT_FINANCED | PurchaseOrderDistributionPEOAmountFinanced | — |
| AMOUNT_ORDERED | PurchaseOrderDistributionPEOAmountOrdered | ✅ |
| AMOUNT_RECOUPED | PurchaseOrderDistributionPEOAmountRecouped | — |
| AMOUNT_TO_ENCUMBER | PurchaseOrderDistributionPEOAmountToEncumber | — |
| AWARD_ID | PurchaseOrderDistributionPEOAwardId | — |
| BOM_RESOURCE_ID | PurchaseOrderDistributionPEOBomResourceId | — |
| BUDGET_ACCOUNT_ID | PurchaseOrderDistributionPEOBudgetAccountId | — |
| BUDGET_DATE | PurchaseOrderDistributionPEOBudgetDate | — |
| CLOSE_BUDGET_DATE | PurchaseOrderDistributionPEOCloseBudgetDate | — |
| CODE_COMBINATION_ID | PurchaseOrderDistributionPEOCodeCombinationId | — |
| CONSIGNMENT_QUANTITY | PurchaseOrderDistributionPEOConsignmentQuantity | — |
| CREATED_BY | PurchaseOrderDistributionPEOCreatedBy | — |
| CREATION_DATE | PurchaseOrderDistributionPEOCreationDate | — |
| DELIVER_TO_CUST_CONTACT_ID | PurchaseOrderDistributionPEODeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | PurchaseOrderDistributionPEODeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | PurchaseOrderDistributionPEODeliverToCustLocationId | — |
| DELIVER_TO_LOCATION_ID | PurchaseOrderDistributionPEODeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | PurchaseOrderDistributionPEODeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | PurchaseOrderDistributionPEODestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEODestVarianceAccountId | — |
| DESTINATION_CONTEXT | PurchaseOrderDistributionPEODestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PurchaseOrderDistributionPEODestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | PurchaseOrderDistributionPEODestinationSubinventory | — |
| DESTINATION_TYPE_CODE | PurchaseOrderDistributionPEODestinationTypeCode | ✅ |
| DIST_INTENDED_USE | PurchaseOrderDistributionPEODistIntendedUse | — |
| DISTRIBUTION_NUM | PurchaseOrderDistributionPEODistributionNum | ✅ |
| DISTRIBUTION_TYPE | PurchaseOrderDistributionPEODistributionType | — |
| ENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOEncumberedAmount | — |
| ENCUMBERED_FLAG | PurchaseOrderDistributionPEOEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PurchaseOrderDistributionPEOEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PurchaseOrderDistributionPEOFailedFundsLookupCode | — |
| FUNDS_STATUS | PurchaseOrderDistributionPEOFundsStatus | — |
| GL_CANCELLED_DATE | PurchaseOrderDistributionPEOGlCancelledDate | — |
| GL_CLOSED_DATE | PurchaseOrderDistributionPEOGlClosedDate | — |
| GL_ENCUMBERED_DATE | PurchaseOrderDistributionPEOGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PurchaseOrderDistributionPEOGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PurchaseOrderDistributionPEOGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PurchaseOrderDistributionPEOInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PurchaseOrderDistributionPEOInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PurchaseOrderDistributionPEOInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PurchaseOrderDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderDistributionPEOJobDefinitionPackage | — |
| KANBAN_CARD_ID | PurchaseOrderDistributionPEOKanbanCardId | — |
| LAST_UPDATE_DATE | PurchaseOrderDistributionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchaseOrderDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchaseOrderDistributionPEOLastUpdatedBy | — |
| LINE_LOCATION_ID | PurchaseOrderDistributionPEOLineLocationId | — |
| NONRECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEONonrecoverableInclusiveTax | — |
| NONRECOVERABLE_TAX | PurchaseOrderDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionPEOObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PurchaseOrderDistributionPEOOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOOkeContractLineId | — |
| ORIGINAL_DISTRIBUTION_ID | PurchaseOrderDistributionPEOOriginalDistributionId | — |
| PJC_BILLABLE_FLAG | PurchaseOrderDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | PurchaseOrderDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | PurchaseOrderDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | PurchaseOrderDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPEOPJC_PROJECT_ID | — |
| PJC_TASK_ID | PurchaseOrderDistributionPEOPJC_TASK_ID | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPEOPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | PoDistributionId | ✅ |
| PO_HEADER_ID | PurchaseOrderDistributionPEOPoHeaderId | — |
| PO_LINE_ID | PurchaseOrderDistributionPEOPoLineId | — |
| PRC_BU_ID | PurchaseOrderDistributionPEOPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PurchaseOrderDistributionPEOPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PurchaseOrderDistributionPEOProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderDistributionPEOProgramName | — |
| QUANTITY_BILLED | PurchaseOrderDistributionPEOQuantityBilled | — |
| QUANTITY_CANCELLED | PurchaseOrderDistributionPEOQuantityCancelled | ✅ |
| QUANTITY_DELIVERED | PurchaseOrderDistributionPEOQuantityDelivered | — |
| QUANTITY_FINANCED | PurchaseOrderDistributionPEOQuantityFinanced | — |
| QUANTITY_ORDERED | PurchaseOrderDistributionPEOQuantityOrdered | ✅ |
| QUANTITY_RECOUPED | PurchaseOrderDistributionPEOQuantityRecouped | — |
| RATE | PurchaseOrderDistributionPEORate | — |
| RATE_DATE | PurchaseOrderDistributionPEORateDate | — |
| RECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEORecoverableInclusiveTax | — |
| RECOVERABLE_TAX | PurchaseOrderDistributionPEORecoverableTax | — |
| RECOVERY_RATE | PurchaseOrderDistributionPEORecoveryRate | — |
| REQ_BU_ID | PurchaseOrderDistributionPEOReqBuId | — |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionPEOReqDistributionId | ✅ |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionPEOReqHeaderReferenceNum | — |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionPEOReqLineReferenceNum | ✅ |
| REQUEST_ID | PurchaseOrderDistributionPEORequestId | — |
| RETAINAGE_RELEASED_AMOUNT | PurchaseOrderDistributionPEORetainageReleasedAmount | — |
| RETAINAGE_WITHHELD_AMOUNT | PurchaseOrderDistributionPEORetainageWithheldAmount | — |
| SET_OF_BOOKS_ID | PurchaseOrderDistributionPEOSetOfBooksId | — |
| SHIPPING_UOM_QUANTITY | PurchaseOrderDistributionPEOShippingUomQuantity | — |
| SHIPPING_UOM_QUANTITY_CANCELED | PurchaseOrderDistributionPEOShippingUomQuantityCanceled | — |
| SOURCE_DISTRIBUTION_ID | PurchaseOrderDistributionPEOSourceDistributionId | — |
| TAX_EXCLUSIVE_AMOUNT | PurchaseOrderDistributionPEOTaxExclusiveAmount | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PurchaseOrderDistributionPEOTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PurchaseOrderDistributionPEOUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEOVarianceAccountId | — |
| WIP_ENTITY_ID | PurchaseOrderDistributionPEOWipEntityId | — |
| WIP_LINE_ID | PurchaseOrderDistributionPEOWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PurchaseOrderDistributionPEOWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PurchaseOrderDistributionPEOWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PurchaseOrderDistributionPEOWipResourceSeqNum | — |

### [[maintenancewoprocurementreceiptpvo|MaintenanceWOProcurementReceiptPVO]] (OTHER · BICC: 8/108)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PurchaseOrderDistributionPEOAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | PurchaseOrderDistributionPEOAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | PurchaseOrderDistributionPEOAccruedFlag | — |
| AMOUNT_BILLED | PurchaseOrderDistributionPEOAmountBilled | — |
| AMOUNT_CANCELLED | PurchaseOrderDistributionPEOAmountCancelled | — |
| AMOUNT_DELIVERED | PurchaseOrderDistributionPEOAmountDelivered | — |
| AMOUNT_FINANCED | PurchaseOrderDistributionPEOAmountFinanced | — |
| AMOUNT_ORDERED | PurchaseOrderDistributionPEOAmountOrdered | ✅ |
| AMOUNT_RECOUPED | PurchaseOrderDistributionPEOAmountRecouped | — |
| AMOUNT_TO_ENCUMBER | PurchaseOrderDistributionPEOAmountToEncumber | — |
| AWARD_ID | PurchaseOrderDistributionPEOAwardId | — |
| BOM_RESOURCE_ID | PurchaseOrderDistributionPEOBomResourceId | — |
| BUDGET_ACCOUNT_ID | PurchaseOrderDistributionPEOBudgetAccountId | — |
| BUDGET_DATE | PurchaseOrderDistributionPEOBudgetDate | — |
| CLOSE_BUDGET_DATE | PurchaseOrderDistributionPEOCloseBudgetDate | — |
| CODE_COMBINATION_ID | PurchaseOrderDistributionPEOCodeCombinationId | — |
| CONSIGNMENT_QUANTITY | PurchaseOrderDistributionPEOConsignmentQuantity | — |
| CREATED_BY | PurchaseOrderDistributionPEOCreatedBy | — |
| CREATION_DATE | PurchaseOrderDistributionPEOCreationDate | — |
| DELIVER_TO_CUST_CONTACT_ID | PurchaseOrderDistributionPEODeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | PurchaseOrderDistributionPEODeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | PurchaseOrderDistributionPEODeliverToCustLocationId | — |
| DELIVER_TO_LOCATION_ID | PurchaseOrderDistributionPEODeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | PurchaseOrderDistributionPEODeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | PurchaseOrderDistributionPEODestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEODestVarianceAccountId | — |
| DESTINATION_CONTEXT | PurchaseOrderDistributionPEODestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PurchaseOrderDistributionPEODestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | PurchaseOrderDistributionPEODestinationSubinventory | — |
| DESTINATION_TYPE_CODE | PurchaseOrderDistributionPEODestinationTypeCode | ✅ |
| DIST_INTENDED_USE | PurchaseOrderDistributionPEODistIntendedUse | — |
| DISTRIBUTION_NUM | PurchaseOrderDistributionPEODistributionNum | ✅ |
| DISTRIBUTION_TYPE | PurchaseOrderDistributionPEODistributionType | — |
| ENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOEncumberedAmount | — |
| ENCUMBERED_FLAG | PurchaseOrderDistributionPEOEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PurchaseOrderDistributionPEOEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PurchaseOrderDistributionPEOFailedFundsLookupCode | — |
| FUNDS_STATUS | PurchaseOrderDistributionPEOFundsStatus | — |
| GL_CANCELLED_DATE | PurchaseOrderDistributionPEOGlCancelledDate | — |
| GL_CLOSED_DATE | PurchaseOrderDistributionPEOGlClosedDate | — |
| GL_ENCUMBERED_DATE | PurchaseOrderDistributionPEOGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PurchaseOrderDistributionPEOGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PurchaseOrderDistributionPEOGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PurchaseOrderDistributionPEOInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PurchaseOrderDistributionPEOInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PurchaseOrderDistributionPEOInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PurchaseOrderDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderDistributionPEOJobDefinitionPackage | — |
| KANBAN_CARD_ID | PurchaseOrderDistributionPEOKanbanCardId | — |
| LAST_UPDATE_DATE | PurchaseOrderDistributionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchaseOrderDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchaseOrderDistributionPEOLastUpdatedBy | — |
| LINE_LOCATION_ID | PurchaseOrderDistributionPEOLineLocationId | — |
| NONRECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEONonrecoverableInclusiveTax | — |
| NONRECOVERABLE_TAX | PurchaseOrderDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionPEOObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PurchaseOrderDistributionPEOOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOOkeContractLineId | — |
| ORIGINAL_DISTRIBUTION_ID | PurchaseOrderDistributionPEOOriginalDistributionId | — |
| PJC_BILLABLE_FLAG | PurchaseOrderDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | PurchaseOrderDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | PurchaseOrderDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | PurchaseOrderDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPEOPJC_PROJECT_ID | — |
| PJC_TASK_ID | PurchaseOrderDistributionPEOPJC_TASK_ID | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPEOPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | PurchaseOrderDistributionPEOPoDistributionId | ✅ |
| PO_HEADER_ID | PurchaseOrderDistributionPEOPoHeaderId | — |
| PO_LINE_ID | PurchaseOrderDistributionPEOPoLineId | — |
| PRC_BU_ID | PurchaseOrderDistributionPEOPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PurchaseOrderDistributionPEOPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PurchaseOrderDistributionPEOProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderDistributionPEOProgramName | — |
| QUANTITY_BILLED | PurchaseOrderDistributionPEOQuantityBilled | — |
| QUANTITY_CANCELLED | PurchaseOrderDistributionPEOQuantityCancelled | — |
| QUANTITY_DELIVERED | PurchaseOrderDistributionPEOQuantityDelivered | — |
| QUANTITY_FINANCED | PurchaseOrderDistributionPEOQuantityFinanced | — |
| QUANTITY_ORDERED | PurchaseOrderDistributionPEOQuantityOrdered | ✅ |
| QUANTITY_RECOUPED | PurchaseOrderDistributionPEOQuantityRecouped | — |
| RATE | PurchaseOrderDistributionPEORate | — |
| RATE_DATE | PurchaseOrderDistributionPEORateDate | — |
| RECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEORecoverableInclusiveTax | — |
| RECOVERABLE_TAX | PurchaseOrderDistributionPEORecoverableTax | — |
| RECOVERY_RATE | PurchaseOrderDistributionPEORecoveryRate | — |
| REQ_BU_ID | PurchaseOrderDistributionPEOReqBuId | — |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionPEOReqDistributionId | ✅ |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionPEOReqHeaderReferenceNum | — |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionPEOReqLineReferenceNum | ✅ |
| REQUEST_ID | PurchaseOrderDistributionPEORequestId | — |
| RETAINAGE_RELEASED_AMOUNT | PurchaseOrderDistributionPEORetainageReleasedAmount | — |
| RETAINAGE_WITHHELD_AMOUNT | PurchaseOrderDistributionPEORetainageWithheldAmount | — |
| SET_OF_BOOKS_ID | PurchaseOrderDistributionPEOSetOfBooksId | — |
| SOURCE_DISTRIBUTION_ID | PurchaseOrderDistributionPEOSourceDistributionId | — |
| TAX_EXCLUSIVE_AMOUNT | PurchaseOrderDistributionPEOTaxExclusiveAmount | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PurchaseOrderDistributionPEOTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PurchaseOrderDistributionPEOUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEOVarianceAccountId | — |
| WIP_ENTITY_ID | PurchaseOrderDistributionPEOWipEntityId | — |
| WIP_LINE_ID | PurchaseOrderDistributionPEOWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PurchaseOrderDistributionPEOWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PurchaseOrderDistributionPEOWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PurchaseOrderDistributionPEOWipResourceSeqNum | — |

### [[prepaymentappliationdistributionpvo|PrepaymentAppliationDistributionPVO]] (AP · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | PoDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PurchaseOrderDistLastUpdateDate | ✅ |
| PO_DISTRIBUTION_ID | PoDistributionPoDistributionId | — |
| PO_DISTRIBUTION_ID | PurchaseOrderDistPoDistributionId | — |

### [[purchasingdocumentdistributionextractpvo|PurchasingDocumentDistributionExtractPVO]] (PO · BICC: 63/64)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | AccrualAccountId | ✅ |
| ACCRUE_ON_RECEIPT_FLAG | AccrueOnReceiptFlag | ✅ |
| ACCRUED_FLAG | AccruedFlag | ✅ |
| AMOUNT_BILLED | AmountBilled | ✅ |
| AMOUNT_CANCELLED | AmountCancelled | ✅ |
| AMOUNT_DELIVERED | AmountDelivered | ✅ |
| AMOUNT_ORDERED | AmountOrdered | ✅ |
| BUDGET_DATE | BudgetDate | ✅ |
| CODE_COMBINATION_ID | CodeCombinationId | ✅ |
| CONSIGNMENT_QUANTITY | ConsignmentQuantity | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DELIVER_TO_CUST_CONTACT_ID | DeliverToCustContactId | ✅ |
| DELIVER_TO_CUST_ID | DeliverToCustId | ✅ |
| DELIVER_TO_CUST_LOCATION_ID | DeliverToCustLocationId | ✅ |
| DELIVER_TO_LOCATION_ID | DeliverToLocationId | ✅ |
| DELIVER_TO_PERSON_ID | DeliverToPersonId | ✅ |
| DEST_CHARGE_ACCOUNT_ID | DestChargeAccountId | ✅ |
| DEST_VARIANCE_ACCOUNT_ID | DestVarianceAccountId | ✅ |
| DESTINATION_ORGANIZATION_ID | DestinationOrganizationId | ✅ |
| DESTINATION_SUBINVENTORY | DestinationSubinventory | ✅ |
| DESTINATION_TYPE_CODE | DestinationTypeCode | ✅ |
| DIST_INTENDED_USE | DistIntendedUse | — |
| DISTRIBUTION_NUM | DistributionNum | ✅ |
| FUNDS_STATUS | FundsStatus | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LINE_LOCATION_ID | LineLocationId | ✅ |
| NONRECOVERABLE_INCLUSIVE_TAX | NonrecoverableInclusiveTax | ✅ |
| NONRECOVERABLE_TAX | NonrecoverableTax | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORIGINAL_DISTRIBUTION_ID | OriginalDistributionId | ✅ |
| PJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | ✅ |
| PJC_EXPENDITURE_TYPE_ID | PJC_EXPENDITURE_TYPE_ID | ✅ |
| PJC_ORGANIZATION_ID | PJC_ORGANIZATION_ID | ✅ |
| PJC_PROJECT_ID | PJC_PROJECT_ID | ✅ |
| PJC_TASK_ID | PJC_TASK_ID | ✅ |
| PO_DISTRIBUTION_ID | PoDistributionId | ✅ |
| PO_HEADER_ID | PoHeaderId | ✅ |
| PO_LINE_ID | PoLineId | ✅ |
| QUANTITY_BILLED | QuantityBilled | ✅ |
| QUANTITY_CANCELLED | QuantityCancelled | ✅ |
| QUANTITY_DELIVERED | QuantityDelivered | ✅ |
| QUANTITY_ORDERED | QuantityOrdered | ✅ |
| RATE | Rate | ✅ |
| RATE_DATE | RateDate | ✅ |
| RECOVERABLE_INCLUSIVE_TAX | RecoverableInclusiveTax | ✅ |
| RECOVERABLE_TAX | RecoverableTax | ✅ |
| RECOVERY_RATE | RecoveryRate | ✅ |
| REQ_BU_ID | ReqBuId | ✅ |
| REQ_DISTRIBUTION_ID | ReqDistributionId | ✅ |
| REQ_HEADER_REFERENCE_NUM | ReqHeaderReferenceNum | ✅ |
| REQ_LINE_REFERENCE_NUM | ReqLineReferenceNum | ✅ |
| RETAINAGE_RELEASED_AMOUNT | RetainageReleasedAmount | ✅ |
| RETAINAGE_WITHHELD_AMOUNT | RetainageWithheldAmount | ✅ |
| SET_OF_BOOKS_ID | SetOfBooksId | ✅ |
| SHIPPING_UOM_QTY_DELIVERED | ShippingUomQtyDelivered | ✅ |
| SHIPPING_UOM_QUANTITY | ShippingUomQuantity | ✅ |
| SHIPPING_UOM_QUANTITY_CANCELED | ShippingUomQtyCanceled | ✅ |
| TAX_ATTRIBUTE_UPDATE_CODE | TaxAttributeUpdateCode | ✅ |
| TAX_EXCLUSIVE_AMOUNT | TaxExclusiveAmount | ✅ |
| TAX_RECOVERY_OVERRIDE_FLAG | TaxRecoveryOverrideFlag | ✅ |
| UNENCUMBERED_AMOUNT | UnencumberedAmount | ✅ |
| VARIANCE_ACCOUNT_ID | VarianceAccountId | ✅ |

### [[receiptaccountingpvo|ReceiptAccountingPVO]] (AR · BICC: 6/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISTRIBUTION_NUM | PurchaseOrderDistributionDistributionNum | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| PO_DISTRIBUTION_ID | PoDistributionId | — |
| RATE | PurchaseOrderDistributionRate | ✅ |
| RATE_DATE | PurchaseOrderDistributionRateDate | ✅ |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionReqDistributionId | ✅ |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionReqHeaderReferenceNum | ✅ |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionReqLineReferenceNum | ✅ |

### [[receiptaccountingtxnp1|ReceiptAccountingTxnP1]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PurchaseOrderDistributionPEOAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | PurchaseOrderDistributionPEOAccrueOnReceiptFlag1 | — |
| ACCRUED_FLAG | PurchaseOrderDistributionPEOAccruedFlag | — |
| AMOUNT_BILLED | PurchaseOrderDistributionPEOAmountBilled | — |
| AMOUNT_CANCELLED | PurchaseOrderDistributionPEOAmountCancelled | — |
| AMOUNT_DELIVERED | PurchaseOrderDistributionPEOAmountDelivered | — |
| AMOUNT_FINANCED | PurchaseOrderDistributionPEOAmountFinanced | — |
| AMOUNT_ORDERED | PurchaseOrderDistributionPEOAmountOrdered | — |
| AMOUNT_RECOUPED | PurchaseOrderDistributionPEOAmountRecouped | — |
| AMOUNT_TO_ENCUMBER | PurchaseOrderDistributionPEOAmountToEncumber | — |
| ATTRIBUTE1 | PurchaseOrderDistributionPEOAttribute1 | — |
| ATTRIBUTE10 | PurchaseOrderDistributionPEOAttribute10 | — |
| ATTRIBUTE11 | PurchaseOrderDistributionPEOAttribute11 | — |
| ATTRIBUTE12 | PurchaseOrderDistributionPEOAttribute12 | — |
| ATTRIBUTE13 | PurchaseOrderDistributionPEOAttribute13 | — |
| ATTRIBUTE14 | PurchaseOrderDistributionPEOAttribute14 | — |
| ATTRIBUTE15 | PurchaseOrderDistributionPEOAttribute15 | — |
| ATTRIBUTE16 | PurchaseOrderDistributionPEOAttribute16 | — |
| ATTRIBUTE17 | PurchaseOrderDistributionPEOAttribute17 | — |
| ATTRIBUTE18 | PurchaseOrderDistributionPEOAttribute18 | — |
| ATTRIBUTE19 | PurchaseOrderDistributionPEOAttribute19 | — |
| ATTRIBUTE2 | PurchaseOrderDistributionPEOAttribute2 | — |
| ATTRIBUTE20 | PurchaseOrderDistributionPEOAttribute20 | — |
| ATTRIBUTE3 | PurchaseOrderDistributionPEOAttribute3 | — |
| ATTRIBUTE4 | PurchaseOrderDistributionPEOAttribute4 | — |
| ATTRIBUTE5 | PurchaseOrderDistributionPEOAttribute5 | — |
| ATTRIBUTE6 | PurchaseOrderDistributionPEOAttribute6 | — |
| ATTRIBUTE7 | PurchaseOrderDistributionPEOAttribute7 | — |
| ATTRIBUTE8 | PurchaseOrderDistributionPEOAttribute8 | — |
| ATTRIBUTE9 | PurchaseOrderDistributionPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | PurchaseOrderDistributionPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | PurchaseOrderDistributionPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | PurchaseOrderDistributionPEOAttributeDate10 | — |
| ATTRIBUTE_DATE2 | PurchaseOrderDistributionPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | PurchaseOrderDistributionPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | PurchaseOrderDistributionPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | PurchaseOrderDistributionPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | PurchaseOrderDistributionPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | PurchaseOrderDistributionPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | PurchaseOrderDistributionPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | PurchaseOrderDistributionPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | PurchaseOrderDistributionPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | PurchaseOrderDistributionPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER2 | PurchaseOrderDistributionPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | PurchaseOrderDistributionPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | PurchaseOrderDistributionPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | PurchaseOrderDistributionPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | PurchaseOrderDistributionPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | PurchaseOrderDistributionPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | PurchaseOrderDistributionPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | PurchaseOrderDistributionPEOAttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | PurchaseOrderDistributionPEOAttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | PurchaseOrderDistributionPEOAttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | PurchaseOrderDistributionPEOAttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | PurchaseOrderDistributionPEOAttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | PurchaseOrderDistributionPEOAttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | PurchaseOrderDistributionPEOAttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | PurchaseOrderDistributionPEOAttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | PurchaseOrderDistributionPEOAttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | PurchaseOrderDistributionPEOAttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | PurchaseOrderDistributionPEOAttributeTimestamp9 | — |
| AWARD_ID | PurchaseOrderDistributionPEOAwardId | — |
| BOM_RESOURCE_ID | PurchaseOrderDistributionPEOBomResourceId | — |
| BUDGET_ACCOUNT_ID | PurchaseOrderDistributionPEOBudgetAccountId | — |
| BUDGET_DATE | PurchaseOrderDistributionPEOBudgetDate | — |
| CLOSE_BUDGET_DATE | PurchaseOrderDistributionPEOCloseBudgetDate | — |
| CODE_COMBINATION_ID | PurchaseOrderDistributionPEOCodeCombinationId2 | — |
| CONSIGNMENT_QUANTITY | PurchaseOrderDistributionPEOConsignmentQuantity | — |
| CREATED_BY | PurchaseOrderDistributionPEOCreatedBy3 | — |
| CREATION_DATE | PurchaseOrderDistributionPEOCreationDate3 | — |
| DELIVER_TO_CUST_CONTACT_ID | PurchaseOrderDistributionPEODeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | PurchaseOrderDistributionPEODeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | PurchaseOrderDistributionPEODeliverToCustLocationId | — |
| DELIVER_TO_LOCATION_ID | PurchaseOrderDistributionPEODeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | PurchaseOrderDistributionPEODeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | PurchaseOrderDistributionPEODestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEODestVarianceAccountId | — |
| DESTINATION_CONTEXT | PurchaseOrderDistributionPEODestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PurchaseOrderDistributionPEODestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | PurchaseOrderDistributionPEODestinationSubinventory | — |
| DESTINATION_TYPE_CODE | PurchaseOrderDistributionPEODestinationTypeCode4 | — |
| DIST_INTENDED_USE | PurchaseOrderDistributionPEODistIntendedUse | — |
| DISTRIBUTION_NUM | PurchaseOrderDistributionPEODistributionNum | — |
| DISTRIBUTION_TYPE | PurchaseOrderDistributionPEODistributionType | — |
| ENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOEncumberedAmount | — |
| ENCUMBERED_FLAG | PurchaseOrderDistributionPEOEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PurchaseOrderDistributionPEOEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PurchaseOrderDistributionPEOFailedFundsLookupCode | — |
| FUNDS_STATUS | PurchaseOrderDistributionPEOFundsStatus | — |
| GL_CANCELLED_DATE | PurchaseOrderDistributionPEOGlCancelledDate | — |
| GL_CLOSED_DATE | PurchaseOrderDistributionPEOGlClosedDate | — |
| GL_ENCUMBERED_DATE | PurchaseOrderDistributionPEOGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PurchaseOrderDistributionPEOGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PurchaseOrderDistributionPEOGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PurchaseOrderDistributionPEOInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PurchaseOrderDistributionPEOInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PurchaseOrderDistributionPEOInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PurchaseOrderDistributionPEOJobDefinitionName3 | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderDistributionPEOJobDefinitionPackage3 | — |
| KANBAN_CARD_ID | PurchaseOrderDistributionPEOKanbanCardId | — |
| LAST_UPDATE_DATE | PurchaseOrderDistributionPEOLastUpdateDate3 | — |
| LAST_UPDATE_LOGIN | PurchaseOrderDistributionPEOLastUpdateLogin3 | — |
| LAST_UPDATED_BY | PurchaseOrderDistributionPEOLastUpdatedBy3 | — |
| LINE_LOCATION_ID | PurchaseOrderDistributionPEOLineLocationId | — |
| NONRECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEONonrecoverableInclusiveTax | — |
| NONRECOVERABLE_TAX | PurchaseOrderDistributionPEONonrecoverableTax2 | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionPEOObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PurchaseOrderDistributionPEOOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOOkeContractLineId | — |
| ORIGINAL_DISTRIBUTION_ID | PurchaseOrderDistributionPEOOriginalDistributionId | — |
| PJC_BILLABLE_FLAG | PurchaseOrderDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | PurchaseOrderDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | PurchaseOrderDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | PurchaseOrderDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPEOPJC_PROJECT_ID | — |
| PJC_RESERVED_ATTRIBUTE1 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_RESERVED_ATTRIBUTE10 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE10 | — |
| PJC_RESERVED_ATTRIBUTE2 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE2 | — |
| PJC_RESERVED_ATTRIBUTE3 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE3 | — |
| PJC_RESERVED_ATTRIBUTE4 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE4 | — |
| PJC_RESERVED_ATTRIBUTE5 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE5 | — |
| PJC_RESERVED_ATTRIBUTE6 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE6 | — |
| PJC_RESERVED_ATTRIBUTE7 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE7 | — |
| PJC_RESERVED_ATTRIBUTE8 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE8 | — |
| PJC_RESERVED_ATTRIBUTE9 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE9 | — |
| PJC_TASK_ID | PurchaseOrderDistributionPEOPJC_TASK_ID | — |
| PJC_USER_DEF_ATTRIBUTE1 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPEOPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | PurchaseOrderDistributionPEOPoDistributionId1 | — |
| PO_HEADER_ID | PurchaseOrderDistributionPEOPoHeaderId | — |
| PO_LINE_ID | PurchaseOrderDistributionPEOPoLineId | — |
| PRC_BU_ID | PurchaseOrderDistributionPEOPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PurchaseOrderDistributionPEOPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PurchaseOrderDistributionPEOProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderDistributionPEOProgramName | — |
| QUANTITY_BILLED | PurchaseOrderDistributionPEOQuantityBilled | — |
| QUANTITY_CANCELLED | PurchaseOrderDistributionPEOQuantityCancelled | — |
| QUANTITY_DELIVERED | PurchaseOrderDistributionPEOQuantityDelivered | — |
| QUANTITY_FINANCED | PurchaseOrderDistributionPEOQuantityFinanced | — |
| QUANTITY_ORDERED | PurchaseOrderDistributionPEOQuantityOrdered1 | — |
| QUANTITY_RECOUPED | PurchaseOrderDistributionPEOQuantityRecouped | — |
| RATE | PurchaseOrderDistributionPEORate | — |
| RATE_DATE | PurchaseOrderDistributionPEORateDate | — |
| RECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEORecoverableInclusiveTax | — |
| RECOVERABLE_TAX | PurchaseOrderDistributionPEORecoverableTax | — |
| RECOVERY_RATE | PurchaseOrderDistributionPEORecoveryRate | — |
| REQ_BU_ID | PurchaseOrderDistributionPEOReqBuId | — |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionPEOReqDistributionId | — |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionPEOReqHeaderReferenceNum | — |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionPEOReqLineReferenceNum | — |
| REQUEST_ID | PurchaseOrderDistributionPEORequestId3 | — |
| RETAINAGE_RELEASED_AMOUNT | PurchaseOrderDistributionPEORetainageReleasedAmount | — |
| RETAINAGE_WITHHELD_AMOUNT | PurchaseOrderDistributionPEORetainageWithheldAmount | — |
| SET_OF_BOOKS_ID | PurchaseOrderDistributionPEOSetOfBooksId | — |
| SOURCE_DISTRIBUTION_ID | PurchaseOrderDistributionPEOSourceDistributionId | — |
| TAX_ATTRIBUTE_UPDATE_CODE | PurchaseOrderDistributionPEOTaxAttributeUpdateCode | — |
| TAX_EXCLUSIVE_AMOUNT | PurchaseOrderDistributionPEOTaxExclusiveAmount | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PurchaseOrderDistributionPEOTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PurchaseOrderDistributionPEOUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEOVarianceAccountId | — |
| WIP_ENTITY_ID | PurchaseOrderDistributionPEOWipEntityId | — |
| WIP_LINE_ID | PurchaseOrderDistributionPEOWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PurchaseOrderDistributionPEOWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PurchaseOrderDistributionPEOWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PurchaseOrderDistributionPEOWipResourceSeqNum | — |

### [[receiptaccountingtxnrefpvo|ReceiptAccountingTxnRefPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PurchaseOrderDistributionPEOAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | PurchaseOrderDistributionPEOAccrueOnReceiptFlag1 | — |
| ACCRUED_FLAG | PurchaseOrderDistributionPEOAccruedFlag | — |
| AMOUNT_BILLED | PurchaseOrderDistributionPEOAmountBilled | — |
| AMOUNT_CANCELLED | PurchaseOrderDistributionPEOAmountCancelled | — |
| AMOUNT_DELIVERED | PurchaseOrderDistributionPEOAmountDelivered | — |
| AMOUNT_FINANCED | PurchaseOrderDistributionPEOAmountFinanced | — |
| AMOUNT_ORDERED | PurchaseOrderDistributionPEOAmountOrdered | — |
| AMOUNT_RECOUPED | PurchaseOrderDistributionPEOAmountRecouped | — |
| AMOUNT_TO_ENCUMBER | PurchaseOrderDistributionPEOAmountToEncumber | — |
| ATTRIBUTE1 | PurchaseOrderDistributionPEOAttribute1 | — |
| ATTRIBUTE10 | PurchaseOrderDistributionPEOAttribute10 | — |
| ATTRIBUTE11 | PurchaseOrderDistributionPEOAttribute11 | — |
| ATTRIBUTE12 | PurchaseOrderDistributionPEOAttribute12 | — |
| ATTRIBUTE13 | PurchaseOrderDistributionPEOAttribute13 | — |
| ATTRIBUTE14 | PurchaseOrderDistributionPEOAttribute14 | — |
| ATTRIBUTE15 | PurchaseOrderDistributionPEOAttribute15 | — |
| ATTRIBUTE16 | PurchaseOrderDistributionPEOAttribute16 | — |
| ATTRIBUTE17 | PurchaseOrderDistributionPEOAttribute17 | — |
| ATTRIBUTE18 | PurchaseOrderDistributionPEOAttribute18 | — |
| ATTRIBUTE19 | PurchaseOrderDistributionPEOAttribute19 | — |
| ATTRIBUTE2 | PurchaseOrderDistributionPEOAttribute2 | — |
| ATTRIBUTE20 | PurchaseOrderDistributionPEOAttribute20 | — |
| ATTRIBUTE3 | PurchaseOrderDistributionPEOAttribute3 | — |
| ATTRIBUTE4 | PurchaseOrderDistributionPEOAttribute4 | — |
| ATTRIBUTE5 | PurchaseOrderDistributionPEOAttribute5 | — |
| ATTRIBUTE6 | PurchaseOrderDistributionPEOAttribute6 | — |
| ATTRIBUTE7 | PurchaseOrderDistributionPEOAttribute7 | — |
| ATTRIBUTE8 | PurchaseOrderDistributionPEOAttribute8 | — |
| ATTRIBUTE9 | PurchaseOrderDistributionPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | PurchaseOrderDistributionPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | PurchaseOrderDistributionPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | PurchaseOrderDistributionPEOAttributeDate10 | — |
| ATTRIBUTE_DATE2 | PurchaseOrderDistributionPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | PurchaseOrderDistributionPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | PurchaseOrderDistributionPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | PurchaseOrderDistributionPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | PurchaseOrderDistributionPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | PurchaseOrderDistributionPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | PurchaseOrderDistributionPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | PurchaseOrderDistributionPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | PurchaseOrderDistributionPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | PurchaseOrderDistributionPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER2 | PurchaseOrderDistributionPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | PurchaseOrderDistributionPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | PurchaseOrderDistributionPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | PurchaseOrderDistributionPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | PurchaseOrderDistributionPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | PurchaseOrderDistributionPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | PurchaseOrderDistributionPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | PurchaseOrderDistributionPEOAttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | PurchaseOrderDistributionPEOAttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | PurchaseOrderDistributionPEOAttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | PurchaseOrderDistributionPEOAttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | PurchaseOrderDistributionPEOAttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | PurchaseOrderDistributionPEOAttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | PurchaseOrderDistributionPEOAttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | PurchaseOrderDistributionPEOAttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | PurchaseOrderDistributionPEOAttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | PurchaseOrderDistributionPEOAttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | PurchaseOrderDistributionPEOAttributeTimestamp9 | — |
| AWARD_ID | PurchaseOrderDistributionPEOAwardId | — |
| BOM_RESOURCE_ID | PurchaseOrderDistributionPEOBomResourceId | — |
| BUDGET_ACCOUNT_ID | PurchaseOrderDistributionPEOBudgetAccountId | — |
| BUDGET_DATE | PurchaseOrderDistributionPEOBudgetDate | — |
| CLOSE_BUDGET_DATE | PurchaseOrderDistributionPEOCloseBudgetDate | — |
| CODE_COMBINATION_ID | PurchaseOrderDistributionPEOCodeCombinationId2 | — |
| CONSIGNMENT_QUANTITY | PurchaseOrderDistributionPEOConsignmentQuantity | — |
| CREATED_BY | PurchaseOrderDistributionPEOCreatedBy3 | — |
| CREATION_DATE | PurchaseOrderDistributionPEOCreationDate3 | — |
| DELIVER_TO_CUST_CONTACT_ID | PurchaseOrderDistributionPEODeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | PurchaseOrderDistributionPEODeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | PurchaseOrderDistributionPEODeliverToCustLocationId | — |
| DELIVER_TO_LOCATION_ID | PurchaseOrderDistributionPEODeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | PurchaseOrderDistributionPEODeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | PurchaseOrderDistributionPEODestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEODestVarianceAccountId | — |
| DESTINATION_CONTEXT | PurchaseOrderDistributionPEODestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PurchaseOrderDistributionPEODestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | PurchaseOrderDistributionPEODestinationSubinventory | — |
| DESTINATION_TYPE_CODE | PurchaseOrderDistributionPEODestinationTypeCode4 | — |
| DIST_INTENDED_USE | PurchaseOrderDistributionPEODistIntendedUse | — |
| DISTRIBUTION_NUM | PurchaseOrderDistributionPEODistributionNum | — |
| DISTRIBUTION_TYPE | PurchaseOrderDistributionPEODistributionType | — |
| ENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOEncumberedAmount | — |
| ENCUMBERED_FLAG | PurchaseOrderDistributionPEOEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PurchaseOrderDistributionPEOEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PurchaseOrderDistributionPEOFailedFundsLookupCode | — |
| FUNDS_STATUS | PurchaseOrderDistributionPEOFundsStatus | — |
| GL_CANCELLED_DATE | PurchaseOrderDistributionPEOGlCancelledDate | — |
| GL_CLOSED_DATE | PurchaseOrderDistributionPEOGlClosedDate | — |
| GL_ENCUMBERED_DATE | PurchaseOrderDistributionPEOGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PurchaseOrderDistributionPEOGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PurchaseOrderDistributionPEOGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PurchaseOrderDistributionPEOInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PurchaseOrderDistributionPEOInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PurchaseOrderDistributionPEOInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PurchaseOrderDistributionPEOJobDefinitionName3 | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderDistributionPEOJobDefinitionPackage3 | — |
| KANBAN_CARD_ID | PurchaseOrderDistributionPEOKanbanCardId | — |
| LAST_UPDATE_DATE | PurchaseOrderDistributionPEOLastUpdateDate3 | — |
| LAST_UPDATE_LOGIN | PurchaseOrderDistributionPEOLastUpdateLogin3 | — |
| LAST_UPDATED_BY | PurchaseOrderDistributionPEOLastUpdatedBy3 | — |
| LINE_LOCATION_ID | PurchaseOrderDistributionPEOLineLocationId | — |
| NONRECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEONonrecoverableInclusiveTax | — |
| NONRECOVERABLE_TAX | PurchaseOrderDistributionPEONonrecoverableTax2 | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionPEOObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PurchaseOrderDistributionPEOOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOOkeContractLineId | — |
| ORIGINAL_DISTRIBUTION_ID | PurchaseOrderDistributionPEOOriginalDistributionId | — |
| PJC_BILLABLE_FLAG | PurchaseOrderDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | PurchaseOrderDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | PurchaseOrderDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | PurchaseOrderDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPEOPJC_PROJECT_ID | — |
| PJC_RESERVED_ATTRIBUTE1 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_RESERVED_ATTRIBUTE10 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE10 | — |
| PJC_RESERVED_ATTRIBUTE2 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE2 | — |
| PJC_RESERVED_ATTRIBUTE3 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE3 | — |
| PJC_RESERVED_ATTRIBUTE4 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE4 | — |
| PJC_RESERVED_ATTRIBUTE5 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE5 | — |
| PJC_RESERVED_ATTRIBUTE6 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE6 | — |
| PJC_RESERVED_ATTRIBUTE7 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE7 | — |
| PJC_RESERVED_ATTRIBUTE8 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE8 | — |
| PJC_RESERVED_ATTRIBUTE9 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE9 | — |
| PJC_TASK_ID | PurchaseOrderDistributionPEOPJC_TASK_ID | — |
| PJC_USER_DEF_ATTRIBUTE1 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPEOPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | PurchaseOrderDistributionPEOPoDistributionId1 | — |
| PO_HEADER_ID | PurchaseOrderDistributionPEOPoHeaderId | — |
| PO_LINE_ID | PurchaseOrderDistributionPEOPoLineId | — |
| PRC_BU_ID | PurchaseOrderDistributionPEOPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PurchaseOrderDistributionPEOPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PurchaseOrderDistributionPEOProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderDistributionPEOProgramName | — |
| QUANTITY_BILLED | PurchaseOrderDistributionPEOQuantityBilled | — |
| QUANTITY_CANCELLED | PurchaseOrderDistributionPEOQuantityCancelled | — |
| QUANTITY_DELIVERED | PurchaseOrderDistributionPEOQuantityDelivered | — |
| QUANTITY_FINANCED | PurchaseOrderDistributionPEOQuantityFinanced | — |
| QUANTITY_ORDERED | PurchaseOrderDistributionPEOQuantityOrdered1 | — |
| QUANTITY_RECOUPED | PurchaseOrderDistributionPEOQuantityRecouped | — |
| RATE | PurchaseOrderDistributionPEORate | — |
| RATE_DATE | PurchaseOrderDistributionPEORateDate | — |
| RECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEORecoverableInclusiveTax | — |
| RECOVERABLE_TAX | PurchaseOrderDistributionPEORecoverableTax | — |
| RECOVERY_RATE | PurchaseOrderDistributionPEORecoveryRate | — |
| REQ_BU_ID | PurchaseOrderDistributionPEOReqBuId | — |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionPEOReqDistributionId | — |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionPEOReqHeaderReferenceNum | — |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionPEOReqLineReferenceNum | — |
| REQUEST_ID | PurchaseOrderDistributionPEORequestId3 | — |
| RETAINAGE_RELEASED_AMOUNT | PurchaseOrderDistributionPEORetainageReleasedAmount | — |
| RETAINAGE_WITHHELD_AMOUNT | PurchaseOrderDistributionPEORetainageWithheldAmount | — |
| SET_OF_BOOKS_ID | PurchaseOrderDistributionPEOSetOfBooksId | — |
| SOURCE_DISTRIBUTION_ID | PurchaseOrderDistributionPEOSourceDistributionId | — |
| TAX_ATTRIBUTE_UPDATE_CODE | PurchaseOrderDistributionPEOTaxAttributeUpdateCode | — |
| TAX_EXCLUSIVE_AMOUNT | PurchaseOrderDistributionPEOTaxExclusiveAmount | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PurchaseOrderDistributionPEOTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PurchaseOrderDistributionPEOUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEOVarianceAccountId | — |
| WIP_ENTITY_ID | PurchaseOrderDistributionPEOWipEntityId | — |
| WIP_LINE_ID | PurchaseOrderDistributionPEOWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PurchaseOrderDistributionPEOWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PurchaseOrderDistributionPEOWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PurchaseOrderDistributionPEOWipResourceSeqNum | — |

### [[receivingreceiptp2ptransactionpvo|ReceivingReceiptP2PTransactionPVO]] (AR · BICC: 1/180)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PurchaseOrderDistributionPEOAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | PurchaseOrderDistributionPEOAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | PurchaseOrderDistributionPEOAccruedFlag | — |
| AMOUNT_BILLED | PurchaseOrderDistributionPEOAmountBilled | — |
| AMOUNT_CANCELLED | PurchaseOrderDistributionPEOAmountCancelled | — |
| AMOUNT_DELIVERED | PurchaseOrderDistributionPEOAmountDelivered | — |
| AMOUNT_FINANCED | PurchaseOrderDistributionPEOAmountFinanced | — |
| AMOUNT_ORDERED | PurchaseOrderDistributionPEOAmountOrdered | — |
| AMOUNT_RECOUPED | PurchaseOrderDistributionPEOAmountRecouped | — |
| AMOUNT_TO_ENCUMBER | PurchaseOrderDistributionPEOAmountToEncumber | — |
| ATTRIBUTE1 | PurchaseOrderDistributionPEOAttribute1 | — |
| ATTRIBUTE10 | PurchaseOrderDistributionPEOAttribute10 | — |
| ATTRIBUTE11 | PurchaseOrderDistributionPEOAttribute11 | — |
| ATTRIBUTE12 | PurchaseOrderDistributionPEOAttribute12 | — |
| ATTRIBUTE13 | PurchaseOrderDistributionPEOAttribute13 | — |
| ATTRIBUTE14 | PurchaseOrderDistributionPEOAttribute14 | — |
| ATTRIBUTE15 | PurchaseOrderDistributionPEOAttribute15 | — |
| ATTRIBUTE16 | PurchaseOrderDistributionPEOAttribute16 | — |
| ATTRIBUTE17 | PurchaseOrderDistributionPEOAttribute17 | — |
| ATTRIBUTE18 | PurchaseOrderDistributionPEOAttribute18 | — |
| ATTRIBUTE19 | PurchaseOrderDistributionPEOAttribute19 | — |
| ATTRIBUTE2 | PurchaseOrderDistributionPEOAttribute2 | — |
| ATTRIBUTE20 | PurchaseOrderDistributionPEOAttribute20 | — |
| ATTRIBUTE3 | PurchaseOrderDistributionPEOAttribute3 | — |
| ATTRIBUTE4 | PurchaseOrderDistributionPEOAttribute4 | — |
| ATTRIBUTE5 | PurchaseOrderDistributionPEOAttribute5 | — |
| ATTRIBUTE6 | PurchaseOrderDistributionPEOAttribute6 | — |
| ATTRIBUTE7 | PurchaseOrderDistributionPEOAttribute7 | — |
| ATTRIBUTE8 | PurchaseOrderDistributionPEOAttribute8 | — |
| ATTRIBUTE9 | PurchaseOrderDistributionPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | PurchaseOrderDistributionPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | PurchaseOrderDistributionPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | PurchaseOrderDistributionPEOAttributeDate10 | — |
| ATTRIBUTE_DATE2 | PurchaseOrderDistributionPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | PurchaseOrderDistributionPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | PurchaseOrderDistributionPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | PurchaseOrderDistributionPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | PurchaseOrderDistributionPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | PurchaseOrderDistributionPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | PurchaseOrderDistributionPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | PurchaseOrderDistributionPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | PurchaseOrderDistributionPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | PurchaseOrderDistributionPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER2 | PurchaseOrderDistributionPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | PurchaseOrderDistributionPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | PurchaseOrderDistributionPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | PurchaseOrderDistributionPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | PurchaseOrderDistributionPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | PurchaseOrderDistributionPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | PurchaseOrderDistributionPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | PurchaseOrderDistributionPEOAttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | PurchaseOrderDistributionPEOAttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | PurchaseOrderDistributionPEOAttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | PurchaseOrderDistributionPEOAttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | PurchaseOrderDistributionPEOAttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | PurchaseOrderDistributionPEOAttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | PurchaseOrderDistributionPEOAttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | PurchaseOrderDistributionPEOAttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | PurchaseOrderDistributionPEOAttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | PurchaseOrderDistributionPEOAttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | PurchaseOrderDistributionPEOAttributeTimestamp9 | — |
| AWARD_ID | PurchaseOrderDistributionPEOAwardId | — |
| BOM_RESOURCE_ID | PurchaseOrderDistributionPEOBomResourceId | — |
| BUDGET_ACCOUNT_ID | PurchaseOrderDistributionPEOBudgetAccountId | — |
| BUDGET_DATE | PurchaseOrderDistributionPEOBudgetDate | — |
| CLOSE_BUDGET_DATE | PurchaseOrderDistributionPEOCloseBudgetDate | — |
| CODE_COMBINATION_ID | PurchaseOrderDistributionPEOCodeCombinationId | — |
| CONSIGNMENT_QUANTITY | PurchaseOrderDistributionPEOConsignmentQuantity | — |
| CREATED_BY | PurchaseOrderDistributionPEOCreatedBy | — |
| CREATION_DATE | PurchaseOrderDistributionPEOCreationDate | — |
| DELIVER_TO_CUST_CONTACT_ID | PurchaseOrderDistributionPEODeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | PurchaseOrderDistributionPEODeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | PurchaseOrderDistributionPEODeliverToCustLocationId | — |
| DELIVER_TO_LOCATION_ID | PurchaseOrderDistributionPEODeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | PurchaseOrderDistributionPEODeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | PurchaseOrderDistributionPEODestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEODestVarianceAccountId | — |
| DESTINATION_CONTEXT | PurchaseOrderDistributionPEODestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PurchaseOrderDistributionPEODestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | PurchaseOrderDistributionPEODestinationSubinventory | — |
| DESTINATION_TYPE_CODE | PurchaseOrderDistributionPEODestinationTypeCode | ✅ |
| DIST_INTENDED_USE | PurchaseOrderDistributionPEODistIntendedUse | — |
| DISTRIBUTION_NUM | PurchaseOrderDistributionPEODistributionNum | — |
| DISTRIBUTION_TYPE | PurchaseOrderDistributionPEODistributionType | — |
| ENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOEncumberedAmount | — |
| ENCUMBERED_FLAG | PurchaseOrderDistributionPEOEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PurchaseOrderDistributionPEOEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PurchaseOrderDistributionPEOFailedFundsLookupCode | — |
| FUNDS_STATUS | PurchaseOrderDistributionPEOFundsStatus | — |
| GL_CANCELLED_DATE | PurchaseOrderDistributionPEOGlCancelledDate | — |
| GL_CLOSED_DATE | PurchaseOrderDistributionPEOGlClosedDate | — |
| GL_ENCUMBERED_DATE | PurchaseOrderDistributionPEOGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PurchaseOrderDistributionPEOGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PurchaseOrderDistributionPEOGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PurchaseOrderDistributionPEOInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PurchaseOrderDistributionPEOInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PurchaseOrderDistributionPEOInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PurchaseOrderDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderDistributionPEOJobDefinitionPackage | — |
| KANBAN_CARD_ID | PurchaseOrderDistributionPEOKanbanCardId | — |
| LAST_UPDATE_DATE | PurchaseOrderDistributionPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | PurchaseOrderDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchaseOrderDistributionPEOLastUpdatedBy | — |
| LINE_LOCATION_ID | PurchaseOrderDistributionPEOLineLocationId | — |
| NONRECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEONonrecoverableInclusiveTax | — |
| NONRECOVERABLE_TAX | PurchaseOrderDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionPEOObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PurchaseOrderDistributionPEOOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOOkeContractLineId | — |
| ORIGINAL_DISTRIBUTION_ID | PurchaseOrderDistributionPEOOriginalDistributionId | — |
| PJC_BILLABLE_FLAG | PurchaseOrderDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | PurchaseOrderDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | PurchaseOrderDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | PurchaseOrderDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPEOPJC_PROJECT_ID | — |
| PJC_RESERVED_ATTRIBUTE1 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_RESERVED_ATTRIBUTE10 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE10 | — |
| PJC_RESERVED_ATTRIBUTE2 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE2 | — |
| PJC_RESERVED_ATTRIBUTE3 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE3 | — |
| PJC_RESERVED_ATTRIBUTE4 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE4 | — |
| PJC_RESERVED_ATTRIBUTE5 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE5 | — |
| PJC_RESERVED_ATTRIBUTE6 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE6 | — |
| PJC_RESERVED_ATTRIBUTE7 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE7 | — |
| PJC_RESERVED_ATTRIBUTE8 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE8 | — |
| PJC_RESERVED_ATTRIBUTE9 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE9 | — |
| PJC_TASK_ID | PurchaseOrderDistributionPEOPJC_TASK_ID | — |
| PJC_USER_DEF_ATTRIBUTE1 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPEOPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | PurchaseOrderDistributionPEOPoDistributionId | — |
| PO_HEADER_ID | PurchaseOrderDistributionPEOPoHeaderId | — |
| PO_LINE_ID | PurchaseOrderDistributionPEOPoLineId | — |
| PRC_BU_ID | PurchaseOrderDistributionPEOPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PurchaseOrderDistributionPEOPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PurchaseOrderDistributionPEOProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderDistributionPEOProgramName | — |
| QUANTITY_BILLED | PurchaseOrderDistributionPEOQuantityBilled | — |
| QUANTITY_CANCELLED | PurchaseOrderDistributionPEOQuantityCancelled | — |
| QUANTITY_DELIVERED | PurchaseOrderDistributionPEOQuantityDelivered | — |
| QUANTITY_FINANCED | PurchaseOrderDistributionPEOQuantityFinanced | — |
| QUANTITY_ORDERED | PurchaseOrderDistributionPEOQuantityOrdered | — |
| QUANTITY_RECOUPED | PurchaseOrderDistributionPEOQuantityRecouped | — |
| RATE | PurchaseOrderDistributionPEORate | — |
| RATE_DATE | PurchaseOrderDistributionPEORateDate | — |
| RECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEORecoverableInclusiveTax | — |
| RECOVERABLE_TAX | PurchaseOrderDistributionPEORecoverableTax | — |
| RECOVERY_RATE | PurchaseOrderDistributionPEORecoveryRate | — |
| REQ_BU_ID | PurchaseOrderDistributionPEOReqBuId | — |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionPEOReqDistributionId | — |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionPEOReqHeaderReferenceNum | — |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionPEOReqLineReferenceNum | — |
| REQUEST_ID | PurchaseOrderDistributionPEORequestId | — |
| RETAINAGE_RELEASED_AMOUNT | PurchaseOrderDistributionPEORetainageReleasedAmount | — |
| RETAINAGE_WITHHELD_AMOUNT | PurchaseOrderDistributionPEORetainageWithheldAmount | — |
| SET_OF_BOOKS_ID | PurchaseOrderDistributionPEOSetOfBooksId | — |
| SOURCE_DISTRIBUTION_ID | PurchaseOrderDistributionPEOSourceDistributionId | — |
| TAX_ATTRIBUTE_UPDATE_CODE | PurchaseOrderDistributionPEOTaxAttributeUpdateCode | — |
| TAX_EXCLUSIVE_AMOUNT | PurchaseOrderDistributionPEOTaxExclusiveAmount | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PurchaseOrderDistributionPEOTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PurchaseOrderDistributionPEOUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEOVarianceAccountId | — |
| WIP_ENTITY_ID | PurchaseOrderDistributionPEOWipEntityId | — |
| WIP_LINE_ID | PurchaseOrderDistributionPEOWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PurchaseOrderDistributionPEOWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PurchaseOrderDistributionPEOWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PurchaseOrderDistributionPEOWipResourceSeqNum | — |

### [[receivingreceipttransactionpvo|ReceivingReceiptTransactionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionPEOObjectVersionNumber | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPEOPjcContractId | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPEOPjcExpenditureItemDate | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPEOPjcExpenditureTypeId | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPEOPjcOrganizationId | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPEOPjcProjectId | — |
| PJC_RESERVED_ATTRIBUTE1 | PurchaseOrderDistributionPEOPjcReservedAttribute1 | — |
| PJC_TASK_ID | PurchaseOrderDistributionPEOPjcTaskId | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPEOPjcWorkTypeId | — |
| PO_DISTRIBUTION_ID | PurchaseOrderDistributionPEOPoDistributionId | — |

### [[receivingreceipttransactionrefpvo|ReceivingReceiptTransactionRefPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionPEOObjectVersionNumber | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPEOPjcContractId | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPEOPjcExpenditureItemDate | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPEOPjcExpenditureTypeId | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPEOPjcOrganizationId | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPEOPjcProjectId | — |
| PJC_RESERVED_ATTRIBUTE1 | PurchaseOrderDistributionPEOPjcReservedAttribute1 | — |
| PJC_TASK_ID | PurchaseOrderDistributionPEOPjcTaskId | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPEOPjcWorkTypeId | — |
| PO_DISTRIBUTION_ID | PurchaseOrderDistributionPEOPoDistributionId | — |

### [[standarddistributionpvo|StandardDistributionPVO]] (PO · BICC: 43/118)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PurchaseOrderDistributionAccrualAccountId | ✅ |
| ACCRUE_ON_RECEIPT_FLAG | PurchaseOrderDistributionAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | PurchaseOrderDistributionAccruedFlag | — |
| AMOUNT_BILLED | PurchaseOrderDistributionAmountBilled | ✅ |
| AMOUNT_CANCELLED | PurchaseOrderDistributionAmountCancelled | ✅ |
| AMOUNT_DELIVERED | PurchaseOrderDistributionAmountDelivered | ✅ |
| AMOUNT_FINANCED | PurchaseOrderDistributionAmountFinanced | ✅ |
| AMOUNT_ORDERED | PurchaseOrderDistributionAmountOrdered | ✅ |
| AMOUNT_RECOUPED | PurchaseOrderDistributionAmountRecouped | ✅ |
| AMOUNT_TO_ENCUMBER | PurchaseOrderDistributionAmountToEncumber | — |
| AWARD_ID | PurchaseOrderDistributionAwardId | — |
| BOM_RESOURCE_ID | PurchaseOrderDistributionBomResourceId | — |
| BUDGET_ACCOUNT_ID | PurchaseOrderDistributionBudgetAccountId | ✅ |
| BUDGET_DATE | PurchaseOrderDistributionBudgetDate | — |
| CLOSE_BUDGET_DATE | PurchaseOrderDistributionCloseBudgetDate | — |
| CODE_COMBINATION_ID | PurchaseOrderDistributionCodeCombinationId | ✅ |
| CONSIGNMENT_QUANTITY | PurchaseOrderDistributionConsignmentQuantity | — |
| CREATED_BY | PurchaseOrderDistributionCreatedBy | ✅ |
| CREATION_DATE | PurchaseOrderDistributionCreationDate | ✅ |
| DELIVER_TO_CUST_CONTACT_ID | PurchaseOrderDistributionDeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | PurchaseOrderDistributionDeliverToCustId | ✅ |
| DELIVER_TO_CUST_LOCATION_ID | PurchaseOrderDistributionDeliverToCustLocationId | ✅ |
| DELIVER_TO_LOCATION_ID | PurchaseOrderDistributionDeliverToLocationId | ✅ |
| DELIVER_TO_PERSON_ID | PurchaseOrderDistributionDeliverToPersonId | ✅ |
| DEST_CHARGE_ACCOUNT_ID | PurchaseOrderDistributionDestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionDestVarianceAccountId | — |
| DESTINATION_CONTEXT | PurchaseOrderDistributionDestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PurchaseOrderDistributionDestinationOrganizationId | ✅ |
| DESTINATION_SUBINVENTORY | PurchaseOrderDistributionDestinationSubinventory | ✅ |
| DESTINATION_TYPE_CODE | PurchaseOrderDistributionDestinationTypeCode | ✅ |
| DIST_INTENDED_USE | PurchaseOrderDistributionDistIntendedUse | — |
| DISTRIBUTION_NUM | PurchaseOrderDistributionDistributionNum | ✅ |
| DISTRIBUTION_TYPE | PurchaseOrderDistributionDistributionType | — |
| ENCUMBERED_AMOUNT | PurchaseOrderDistributionEncumberedAmount | — |
| ENCUMBERED_FLAG | PurchaseOrderDistributionEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PurchaseOrderDistributionEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PurchaseOrderDistributionFailedFundsLookupCode | — |
| FUNDS_STATUS | PurchaseOrderDistributionFundsStatus | — |
| GL_CANCELLED_DATE | PurchaseOrderDistributionGlCancelledDate | — |
| GL_CLOSED_DATE | PurchaseOrderDistributionGlClosedDate | — |
| GL_ENCUMBERED_DATE | PurchaseOrderDistributionGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PurchaseOrderDistributionGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PurchaseOrderDistributionGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PurchaseOrderDistributionInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PurchaseOrderDistributionInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PurchaseOrderDistributionInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PurchaseOrderDistributionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderDistributionJobDefinitionPackage | — |
| KANBAN_CARD_ID | PurchaseOrderDistributionKanbanCardId | — |
| LAST_UPDATE_DATE | PurchaseOrderDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchaseOrderDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchaseOrderDistributionLastUpdatedBy | ✅ |
| LINE_LOCATION_ID | PurchaseOrderDistributionLineLocationId | — |
| NONRECOVERABLE_TAX | PurchaseOrderDistributionNonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PurchaseOrderDistributionOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PurchaseOrderDistributionOkeContractLineId | — |
| PJC_BILLABLE_FLAG | PurchaseOrderDistributionPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | PurchaseOrderDistributionPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | PurchaseOrderDistributionPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | PurchaseOrderDistributionPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPJC_PROJECT_ID | ✅ |
| PJC_RESERVED_ATTRIBUTE1 | PurchaseOrderDistributionPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_TASK_ID | PurchaseOrderDistributionPJC_TASK_ID | ✅ |
| PJC_USER_DEF_ATTRIBUTE1 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | PurchaseOrderDistributionPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | PoDistributionId | ✅ |
| PO_HEADER_ID | PurchaseOrderDistributionPoHeaderId | — |
| PO_LINE_ID | PurchaseOrderDistributionPoLineId | — |
| PRC_BU_ID | PurchaseOrderDistributionPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PurchaseOrderDistributionPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PurchaseOrderDistributionProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderDistributionProgramName | — |
| QUANTITY_BILLED | PurchaseOrderDistributionQuantityBilled | ✅ |
| QUANTITY_CANCELLED | PurchaseOrderDistributionQuantityCancelled | ✅ |
| QUANTITY_DELIVERED | PurchaseOrderDistributionQuantityDelivered | ✅ |
| QUANTITY_FINANCED | PurchaseOrderDistributionQuantityFinanced | ✅ |
| QUANTITY_ORDERED | PurchaseOrderDistributionQuantityOrdered | ✅ |
| QUANTITY_RECOUPED | PurchaseOrderDistributionQuantityRecouped | ✅ |
| RATE | PurchaseOrderDistributionRate | ✅ |
| RATE_DATE | PurchaseOrderDistributionRateDate | ✅ |
| RECOVERABLE_TAX | PurchaseOrderDistributionRecoverableTax | — |
| RECOVERY_RATE | PurchaseOrderDistributionRecoveryRate | — |
| REQ_BU_ID | PurchaseOrderDistributionReqBuId | ✅ |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionReqDistributionId | ✅ |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionReqHeaderReferenceNum | ✅ |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionReqLineReferenceNum | ✅ |
| REQUEST_ID | PurchaseOrderDistributionRequestId | — |
| RETAINAGE_RELEASED_AMOUNT | PurchaseOrderDistributionRetainageReleasedAmount | ✅ |
| RETAINAGE_WITHHELD_AMOUNT | PurchaseOrderDistributionRetainageWithheldAmount | ✅ |
| SET_OF_BOOKS_ID | PurchaseOrderDistributionSetOfBooksId | ✅ |
| SHIPPING_UOM_QTY_DELIVERED | PurchaseOrderDistributionShippingUomQtyDelivered | ✅ |
| SHIPPING_UOM_QUANTITY | PurchaseOrderDistributionShippingUomQuantity | ✅ |
| SHIPPING_UOM_QUANTITY_CANCELED | PurchaseOrderDistributionShippingUomQtyCanceled | ✅ |
| SOURCE_DISTRIBUTION_ID | PurchaseOrderDistributionSourceDistributionId | — |
| TAX_ATTRIBUTE_UPDATE_CODE | PurchaseOrderDistributionTaxAttributeUpdateCode | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PurchaseOrderDistributionTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PurchaseOrderDistributionUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PurchaseOrderDistributionUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionVarianceAccountId | ✅ |
| WIP_ENTITY_ID | PurchaseOrderDistributionWipEntityId | — |
| WIP_LINE_ID | PurchaseOrderDistributionWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PurchaseOrderDistributionWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PurchaseOrderDistributionWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PurchaseOrderDistributionWipResourceSeqNum | — |

### [[wooperationspvo|WOOperationsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PurchaseOrderDistributionPEOAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | PurchaseOrderDistributionPEOAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | PurchaseOrderDistributionPEOAccruedFlag | — |
| AMOUNT_BILLED | PurchaseOrderDistributionPEOAmountBilled | — |
| AMOUNT_CANCELLED | PurchaseOrderDistributionPEOAmountCancelled | — |
| AMOUNT_DELIVERED | PurchaseOrderDistributionPEOAmountDelivered | — |
| AMOUNT_FINANCED | PurchaseOrderDistributionPEOAmountFinanced | — |
| AMOUNT_ORDERED | PurchaseOrderDistributionPEOAmountOrdered | — |
| AMOUNT_RECOUPED | PurchaseOrderDistributionPEOAmountRecouped | — |
| AMOUNT_TO_ENCUMBER | PurchaseOrderDistributionPEOAmountToEncumber | — |
| AWARD_ID | PurchaseOrderDistributionPEOAwardId | — |
| BOM_RESOURCE_ID | PurchaseOrderDistributionPEOBomResourceId | — |
| BUDGET_ACCOUNT_ID | PurchaseOrderDistributionPEOBudgetAccountId | — |
| BUDGET_DATE | PurchaseOrderDistributionPEOBudgetDate | — |
| CLOSE_BUDGET_DATE | PurchaseOrderDistributionPEOCloseBudgetDate | — |
| CODE_COMBINATION_ID | PurchaseOrderDistributionPEOCodeCombinationId | — |
| CONSIGNMENT_QUANTITY | PurchaseOrderDistributionPEOConsignmentQuantity | — |
| CREATED_BY | PurchaseOrderDistributionPEOCreatedBy | — |
| CREATION_DATE | PurchaseOrderDistributionPEOCreationDate | — |
| DELIVER_TO_CUST_CONTACT_ID | PurchaseOrderDistributionPEODeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | PurchaseOrderDistributionPEODeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | PurchaseOrderDistributionPEODeliverToCustLocationId | — |
| DELIVER_TO_LOCATION_ID | PurchaseOrderDistributionPEODeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | PurchaseOrderDistributionPEODeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | PurchaseOrderDistributionPEODestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEODestVarianceAccountId | — |
| DESTINATION_CONTEXT | PurchaseOrderDistributionPEODestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PurchaseOrderDistributionPEODestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | PurchaseOrderDistributionPEODestinationSubinventory | — |
| DESTINATION_TYPE_CODE | PurchaseOrderDistributionPEODestinationTypeCode | — |
| DIST_INTENDED_USE | PurchaseOrderDistributionPEODistIntendedUse | — |
| DISTRIBUTION_NUM | PurchaseOrderDistributionPEODistributionNum | — |
| DISTRIBUTION_TYPE | PurchaseOrderDistributionPEODistributionType | — |
| ENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOEncumberedAmount | — |
| ENCUMBERED_FLAG | PurchaseOrderDistributionPEOEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PurchaseOrderDistributionPEOEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PurchaseOrderDistributionPEOFailedFundsLookupCode | — |
| FUNDS_STATUS | PurchaseOrderDistributionPEOFundsStatus | — |
| GL_CANCELLED_DATE | PurchaseOrderDistributionPEOGlCancelledDate | — |
| GL_CLOSED_DATE | PurchaseOrderDistributionPEOGlClosedDate | — |
| GL_ENCUMBERED_DATE | PurchaseOrderDistributionPEOGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PurchaseOrderDistributionPEOGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PurchaseOrderDistributionPEOGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PurchaseOrderDistributionPEOInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PurchaseOrderDistributionPEOInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PurchaseOrderDistributionPEOInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PurchaseOrderDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderDistributionPEOJobDefinitionPackage | — |
| KANBAN_CARD_ID | PurchaseOrderDistributionPEOKanbanCardId | — |
| LAST_UPDATE_DATE | PurchaseOrderDistributionPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | PurchaseOrderDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchaseOrderDistributionPEOLastUpdatedBy | — |
| LINE_LOCATION_ID | PurchaseOrderDistributionPEOLineLocationId | — |
| NONRECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEONonrecoverableInclusiveTax | — |
| NONRECOVERABLE_TAX | PurchaseOrderDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionPEOObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PurchaseOrderDistributionPEOOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOOkeContractLineId | — |
| ORIGINAL_DISTRIBUTION_ID | PurchaseOrderDistributionPEOOriginalDistributionId | — |
| PJC_BILLABLE_FLAG | PurchaseOrderDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | PurchaseOrderDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | PurchaseOrderDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | PurchaseOrderDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPEOPJC_PROJECT_ID | — |
| PJC_RESERVED_ATTRIBUTE1 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_RESERVED_ATTRIBUTE10 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE10 | — |
| PJC_RESERVED_ATTRIBUTE2 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE2 | — |
| PJC_RESERVED_ATTRIBUTE3 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE3 | — |
| PJC_RESERVED_ATTRIBUTE4 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE4 | — |
| PJC_RESERVED_ATTRIBUTE5 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE5 | — |
| PJC_RESERVED_ATTRIBUTE6 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE6 | — |
| PJC_RESERVED_ATTRIBUTE7 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE7 | — |
| PJC_RESERVED_ATTRIBUTE8 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE8 | — |
| PJC_RESERVED_ATTRIBUTE9 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE9 | — |
| PJC_TASK_ID | PurchaseOrderDistributionPEOPJC_TASK_ID | — |
| PJC_USER_DEF_ATTRIBUTE1 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPEOPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | PurchaseOrderDistributionPEOPoDistributionId | — |
| PO_HEADER_ID | PurchaseOrderDistributionPEOPoHeaderId | — |
| PO_LINE_ID | PurchaseOrderDistributionPEOPoLineId | — |
| PRC_BU_ID | PurchaseOrderDistributionPEOPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PurchaseOrderDistributionPEOPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PurchaseOrderDistributionPEOProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderDistributionPEOProgramName | — |
| QUANTITY_BILLED | PurchaseOrderDistributionPEOQuantityBilled | — |
| QUANTITY_CANCELLED | PurchaseOrderDistributionPEOQuantityCancelled | — |
| QUANTITY_DELIVERED | PurchaseOrderDistributionPEOQuantityDelivered | — |
| QUANTITY_FINANCED | PurchaseOrderDistributionPEOQuantityFinanced | — |
| QUANTITY_ORDERED | PurchaseOrderDistributionPEOQuantityOrdered | — |
| QUANTITY_RECOUPED | PurchaseOrderDistributionPEOQuantityRecouped | — |
| RATE | PurchaseOrderDistributionPEORate | — |
| RATE_DATE | PurchaseOrderDistributionPEORateDate | — |
| RECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEORecoverableInclusiveTax | — |
| RECOVERABLE_TAX | PurchaseOrderDistributionPEORecoverableTax | — |
| RECOVERY_RATE | PurchaseOrderDistributionPEORecoveryRate | — |
| REQ_BU_ID | PurchaseOrderDistributionPEOReqBuId | — |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionPEOReqDistributionId | — |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionPEOReqHeaderReferenceNum | — |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionPEOReqLineReferenceNum | — |
| REQUEST_ID | PurchaseOrderDistributionPEORequestId | — |
| RETAINAGE_RELEASED_AMOUNT | PurchaseOrderDistributionPEORetainageReleasedAmount | — |
| RETAINAGE_WITHHELD_AMOUNT | PurchaseOrderDistributionPEORetainageWithheldAmount | — |
| SET_OF_BOOKS_ID | PurchaseOrderDistributionPEOSetOfBooksId | — |
| SOURCE_DISTRIBUTION_ID | PurchaseOrderDistributionPEOSourceDistributionId | — |
| TAX_ATTRIBUTE_UPDATE_CODE | PurchaseOrderDistributionPEOTaxAttributeUpdateCode | — |
| TAX_EXCLUSIVE_AMOUNT | PurchaseOrderDistributionPEOTaxExclusiveAmount | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PurchaseOrderDistributionPEOTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PurchaseOrderDistributionPEOUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEOVarianceAccountId | — |
| WIP_ENTITY_ID | PurchaseOrderDistributionPEOWipEntityId | — |
| WIP_LINE_ID | PurchaseOrderDistributionPEOWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PurchaseOrderDistributionPEOWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PurchaseOrderDistributionPEOWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PurchaseOrderDistributionPEOWipResourceSeqNum | — |

### [[wooperationsrefpvo|WOOperationsRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PurchaseOrderDistributionPEOAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | PurchaseOrderDistributionPEOAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | PurchaseOrderDistributionPEOAccruedFlag | — |
| AMOUNT_BILLED | PurchaseOrderDistributionPEOAmountBilled | — |
| AMOUNT_CANCELLED | PurchaseOrderDistributionPEOAmountCancelled | — |
| AMOUNT_DELIVERED | PurchaseOrderDistributionPEOAmountDelivered | — |
| AMOUNT_FINANCED | PurchaseOrderDistributionPEOAmountFinanced | — |
| AMOUNT_ORDERED | PurchaseOrderDistributionPEOAmountOrdered | — |
| AMOUNT_RECOUPED | PurchaseOrderDistributionPEOAmountRecouped | — |
| AMOUNT_TO_ENCUMBER | PurchaseOrderDistributionPEOAmountToEncumber | — |
| AWARD_ID | PurchaseOrderDistributionPEOAwardId | — |
| BOM_RESOURCE_ID | PurchaseOrderDistributionPEOBomResourceId | — |
| BUDGET_ACCOUNT_ID | PurchaseOrderDistributionPEOBudgetAccountId | — |
| BUDGET_DATE | PurchaseOrderDistributionPEOBudgetDate | — |
| CLOSE_BUDGET_DATE | PurchaseOrderDistributionPEOCloseBudgetDate | — |
| CODE_COMBINATION_ID | PurchaseOrderDistributionPEOCodeCombinationId | — |
| CONSIGNMENT_QUANTITY | PurchaseOrderDistributionPEOConsignmentQuantity | — |
| CREATED_BY | PurchaseOrderDistributionPEOCreatedBy | — |
| CREATION_DATE | PurchaseOrderDistributionPEOCreationDate | — |
| DELIVER_TO_CUST_CONTACT_ID | PurchaseOrderDistributionPEODeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | PurchaseOrderDistributionPEODeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | PurchaseOrderDistributionPEODeliverToCustLocationId | — |
| DELIVER_TO_LOCATION_ID | PurchaseOrderDistributionPEODeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | PurchaseOrderDistributionPEODeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | PurchaseOrderDistributionPEODestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEODestVarianceAccountId | — |
| DESTINATION_CONTEXT | PurchaseOrderDistributionPEODestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PurchaseOrderDistributionPEODestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | PurchaseOrderDistributionPEODestinationSubinventory | — |
| DESTINATION_TYPE_CODE | PurchaseOrderDistributionPEODestinationTypeCode | — |
| DIST_INTENDED_USE | PurchaseOrderDistributionPEODistIntendedUse | — |
| DISTRIBUTION_NUM | PurchaseOrderDistributionPEODistributionNum | — |
| DISTRIBUTION_TYPE | PurchaseOrderDistributionPEODistributionType | — |
| ENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOEncumberedAmount | — |
| ENCUMBERED_FLAG | PurchaseOrderDistributionPEOEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PurchaseOrderDistributionPEOEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PurchaseOrderDistributionPEOFailedFundsLookupCode | — |
| FUNDS_STATUS | PurchaseOrderDistributionPEOFundsStatus | — |
| GL_CANCELLED_DATE | PurchaseOrderDistributionPEOGlCancelledDate | — |
| GL_CLOSED_DATE | PurchaseOrderDistributionPEOGlClosedDate | — |
| GL_ENCUMBERED_DATE | PurchaseOrderDistributionPEOGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PurchaseOrderDistributionPEOGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PurchaseOrderDistributionPEOGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PurchaseOrderDistributionPEOInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PurchaseOrderDistributionPEOInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PurchaseOrderDistributionPEOInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PurchaseOrderDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderDistributionPEOJobDefinitionPackage | — |
| KANBAN_CARD_ID | PurchaseOrderDistributionPEOKanbanCardId | — |
| LAST_UPDATE_DATE | PurchaseOrderDistributionPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | PurchaseOrderDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchaseOrderDistributionPEOLastUpdatedBy | — |
| LINE_LOCATION_ID | PurchaseOrderDistributionPEOLineLocationId | — |
| NONRECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEONonrecoverableInclusiveTax | — |
| NONRECOVERABLE_TAX | PurchaseOrderDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionPEOObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PurchaseOrderDistributionPEOOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOOkeContractLineId | — |
| ORIGINAL_DISTRIBUTION_ID | PurchaseOrderDistributionPEOOriginalDistributionId | — |
| PJC_BILLABLE_FLAG | PurchaseOrderDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | PurchaseOrderDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | PurchaseOrderDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | PurchaseOrderDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPEOPJC_PROJECT_ID | — |
| PJC_RESERVED_ATTRIBUTE1 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_RESERVED_ATTRIBUTE10 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE10 | — |
| PJC_RESERVED_ATTRIBUTE2 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE2 | — |
| PJC_RESERVED_ATTRIBUTE3 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE3 | — |
| PJC_RESERVED_ATTRIBUTE4 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE4 | — |
| PJC_RESERVED_ATTRIBUTE5 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE5 | — |
| PJC_RESERVED_ATTRIBUTE6 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE6 | — |
| PJC_RESERVED_ATTRIBUTE7 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE7 | — |
| PJC_RESERVED_ATTRIBUTE8 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE8 | — |
| PJC_RESERVED_ATTRIBUTE9 | PurchaseOrderDistributionPEOPJC_RESERVED_ATTRIBUTE9 | — |
| PJC_TASK_ID | PurchaseOrderDistributionPEOPJC_TASK_ID | — |
| PJC_USER_DEF_ATTRIBUTE1 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | PurchaseOrderDistributionPEOPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPEOPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | PurchaseOrderDistributionPEOPoDistributionId | — |
| PO_HEADER_ID | PurchaseOrderDistributionPEOPoHeaderId | — |
| PO_LINE_ID | PurchaseOrderDistributionPEOPoLineId | — |
| PRC_BU_ID | PurchaseOrderDistributionPEOPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PurchaseOrderDistributionPEOPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PurchaseOrderDistributionPEOProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderDistributionPEOProgramName | — |
| QUANTITY_BILLED | PurchaseOrderDistributionPEOQuantityBilled | — |
| QUANTITY_CANCELLED | PurchaseOrderDistributionPEOQuantityCancelled | — |
| QUANTITY_DELIVERED | PurchaseOrderDistributionPEOQuantityDelivered | — |
| QUANTITY_FINANCED | PurchaseOrderDistributionPEOQuantityFinanced | — |
| QUANTITY_ORDERED | PurchaseOrderDistributionPEOQuantityOrdered | — |
| QUANTITY_RECOUPED | PurchaseOrderDistributionPEOQuantityRecouped | — |
| RATE | PurchaseOrderDistributionPEORate | — |
| RATE_DATE | PurchaseOrderDistributionPEORateDate | — |
| RECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEORecoverableInclusiveTax | — |
| RECOVERABLE_TAX | PurchaseOrderDistributionPEORecoverableTax | — |
| RECOVERY_RATE | PurchaseOrderDistributionPEORecoveryRate | — |
| REQ_BU_ID | PurchaseOrderDistributionPEOReqBuId | — |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionPEOReqDistributionId | — |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionPEOReqHeaderReferenceNum | — |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionPEOReqLineReferenceNum | — |
| REQUEST_ID | PurchaseOrderDistributionPEORequestId | — |
| RETAINAGE_RELEASED_AMOUNT | PurchaseOrderDistributionPEORetainageReleasedAmount | — |
| RETAINAGE_WITHHELD_AMOUNT | PurchaseOrderDistributionPEORetainageWithheldAmount | — |
| SET_OF_BOOKS_ID | PurchaseOrderDistributionPEOSetOfBooksId | — |
| SOURCE_DISTRIBUTION_ID | PurchaseOrderDistributionPEOSourceDistributionId | — |
| TAX_ATTRIBUTE_UPDATE_CODE | PurchaseOrderDistributionPEOTaxAttributeUpdateCode | — |
| TAX_EXCLUSIVE_AMOUNT | PurchaseOrderDistributionPEOTaxExclusiveAmount | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PurchaseOrderDistributionPEOTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PurchaseOrderDistributionPEOUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEOVarianceAccountId | — |
| WIP_ENTITY_ID | PurchaseOrderDistributionPEOWipEntityId | — |
| WIP_LINE_ID | PurchaseOrderDistributionPEOWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PurchaseOrderDistributionPEOWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PurchaseOrderDistributionPEOWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PurchaseOrderDistributionPEOWipResourceSeqNum | — |

### [[woprocurementpopvo|WOProcurementPOPVO]] (OTHER · BICC: 13/110)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PurchaseOrderDistributionPEOAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | PurchaseOrderDistributionPEOAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | PurchaseOrderDistributionPEOAccruedFlag | — |
| AMOUNT_BILLED | PurchaseOrderDistributionPEOAmountBilled | — |
| AMOUNT_CANCELLED | PurchaseOrderDistributionPEOAmountCancelled | ✅ |
| AMOUNT_DELIVERED | PurchaseOrderDistributionPEOAmountDelivered | — |
| AMOUNT_FINANCED | PurchaseOrderDistributionPEOAmountFinanced | — |
| AMOUNT_ORDERED | PurchaseOrderDistributionPEOAmountOrdered | ✅ |
| AMOUNT_RECOUPED | PurchaseOrderDistributionPEOAmountRecouped | — |
| AMOUNT_TO_ENCUMBER | PurchaseOrderDistributionPEOAmountToEncumber | — |
| AWARD_ID | PurchaseOrderDistributionPEOAwardId | — |
| BOM_RESOURCE_ID | PurchaseOrderDistributionPEOBomResourceId | — |
| BUDGET_ACCOUNT_ID | PurchaseOrderDistributionPEOBudgetAccountId | — |
| BUDGET_DATE | PurchaseOrderDistributionPEOBudgetDate | — |
| CLOSE_BUDGET_DATE | PurchaseOrderDistributionPEOCloseBudgetDate | — |
| CODE_COMBINATION_ID | PurchaseOrderDistributionPEOCodeCombinationId | — |
| CONSIGNMENT_QUANTITY | PurchaseOrderDistributionPEOConsignmentQuantity | — |
| CREATED_BY | PurchaseOrderDistributionPEOCreatedBy | — |
| CREATION_DATE | PurchaseOrderDistributionPEOCreationDate | ✅ |
| DELIVER_TO_CUST_CONTACT_ID | PurchaseOrderDistributionPEODeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | PurchaseOrderDistributionPEODeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | PurchaseOrderDistributionPEODeliverToCustLocationId | — |
| DELIVER_TO_LOCATION_ID | PurchaseOrderDistributionPEODeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | PurchaseOrderDistributionPEODeliverToPersonId | ✅ |
| DEST_CHARGE_ACCOUNT_ID | PurchaseOrderDistributionPEODestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEODestVarianceAccountId | — |
| DESTINATION_CONTEXT | PurchaseOrderDistributionPEODestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PurchaseOrderDistributionPEODestinationOrganizationId | ✅ |
| DESTINATION_SUBINVENTORY | PurchaseOrderDistributionPEODestinationSubinventory | — |
| DESTINATION_TYPE_CODE | PurchaseOrderDistributionPEODestinationTypeCode | ✅ |
| DIST_INTENDED_USE | PurchaseOrderDistributionPEODistIntendedUse | — |
| DISTRIBUTION_NUM | PurchaseOrderDistributionPEODistributionNum | ✅ |
| DISTRIBUTION_TYPE | PurchaseOrderDistributionPEODistributionType | — |
| ENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOEncumberedAmount | — |
| ENCUMBERED_FLAG | PurchaseOrderDistributionPEOEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PurchaseOrderDistributionPEOEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PurchaseOrderDistributionPEOFailedFundsLookupCode | — |
| FUNDS_STATUS | PurchaseOrderDistributionPEOFundsStatus | — |
| GL_CANCELLED_DATE | PurchaseOrderDistributionPEOGlCancelledDate | — |
| GL_CLOSED_DATE | PurchaseOrderDistributionPEOGlClosedDate | — |
| GL_ENCUMBERED_DATE | PurchaseOrderDistributionPEOGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PurchaseOrderDistributionPEOGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PurchaseOrderDistributionPEOGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PurchaseOrderDistributionPEOInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PurchaseOrderDistributionPEOInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PurchaseOrderDistributionPEOInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PurchaseOrderDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderDistributionPEOJobDefinitionPackage | — |
| KANBAN_CARD_ID | PurchaseOrderDistributionPEOKanbanCardId | — |
| LAST_UPDATE_DATE | PurchaseOrderDistributionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchaseOrderDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchaseOrderDistributionPEOLastUpdatedBy | — |
| LINE_LOCATION_ID | PurchaseOrderDistributionPEOLineLocationId | — |
| NONRECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEONonrecoverableInclusiveTax | — |
| NONRECOVERABLE_TAX | PurchaseOrderDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionPEOObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PurchaseOrderDistributionPEOOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOOkeContractLineId | — |
| ORIGINAL_DISTRIBUTION_ID | PurchaseOrderDistributionPEOOriginalDistributionId | — |
| PJC_BILLABLE_FLAG | PurchaseOrderDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | PurchaseOrderDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | PurchaseOrderDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | PurchaseOrderDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPEOPJC_PROJECT_ID | — |
| PJC_TASK_ID | PurchaseOrderDistributionPEOPJC_TASK_ID | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPEOPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | PoDistributionId | ✅ |
| PO_HEADER_ID | PurchaseOrderDistributionPEOPoHeaderId | — |
| PO_LINE_ID | PurchaseOrderDistributionPEOPoLineId | — |
| PRC_BU_ID | PurchaseOrderDistributionPEOPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PurchaseOrderDistributionPEOPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PurchaseOrderDistributionPEOProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderDistributionPEOProgramName | — |
| QUANTITY_BILLED | PurchaseOrderDistributionPEOQuantityBilled | — |
| QUANTITY_CANCELLED | PurchaseOrderDistributionPEOQuantityCancelled | ✅ |
| QUANTITY_DELIVERED | PurchaseOrderDistributionPEOQuantityDelivered | — |
| QUANTITY_FINANCED | PurchaseOrderDistributionPEOQuantityFinanced | — |
| QUANTITY_ORDERED | PurchaseOrderDistributionPEOQuantityOrdered | ✅ |
| QUANTITY_RECOUPED | PurchaseOrderDistributionPEOQuantityRecouped | — |
| RATE | PurchaseOrderDistributionPEORate | — |
| RATE_DATE | PurchaseOrderDistributionPEORateDate | — |
| RECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEORecoverableInclusiveTax | — |
| RECOVERABLE_TAX | PurchaseOrderDistributionPEORecoverableTax | — |
| RECOVERY_RATE | PurchaseOrderDistributionPEORecoveryRate | — |
| REQ_BU_ID | PurchaseOrderDistributionPEOReqBuId | — |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionPEOReqDistributionId | ✅ |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionPEOReqHeaderReferenceNum | — |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionPEOReqLineReferenceNum | ✅ |
| REQUEST_ID | PurchaseOrderDistributionPEORequestId | — |
| RETAINAGE_RELEASED_AMOUNT | PurchaseOrderDistributionPEORetainageReleasedAmount | — |
| RETAINAGE_WITHHELD_AMOUNT | PurchaseOrderDistributionPEORetainageWithheldAmount | — |
| SET_OF_BOOKS_ID | PurchaseOrderDistributionPEOSetOfBooksId | — |
| SHIPPING_UOM_QUANTITY | PurchaseOrderDistributionPEOShippingUomQuantity | — |
| SHIPPING_UOM_QUANTITY_CANCELED | PurchaseOrderDistributionPEOShippingUomQuantityCanceled | — |
| SOURCE_DISTRIBUTION_ID | PurchaseOrderDistributionPEOSourceDistributionId | — |
| TAX_EXCLUSIVE_AMOUNT | PurchaseOrderDistributionPEOTaxExclusiveAmount | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PurchaseOrderDistributionPEOTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PurchaseOrderDistributionPEOUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEOVarianceAccountId | — |
| WIP_ENTITY_ID | PurchaseOrderDistributionPEOWipEntityId | — |
| WIP_LINE_ID | PurchaseOrderDistributionPEOWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PurchaseOrderDistributionPEOWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PurchaseOrderDistributionPEOWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PurchaseOrderDistributionPEOWipResourceSeqNum | — |

### [[woprocurementreceiptpvo|WOProcurementReceiptPVO]] (OTHER · BICC: 8/108)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | PurchaseOrderDistributionPEOAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | PurchaseOrderDistributionPEOAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | PurchaseOrderDistributionPEOAccruedFlag | — |
| AMOUNT_BILLED | PurchaseOrderDistributionPEOAmountBilled | — |
| AMOUNT_CANCELLED | PurchaseOrderDistributionPEOAmountCancelled | — |
| AMOUNT_DELIVERED | PurchaseOrderDistributionPEOAmountDelivered | — |
| AMOUNT_FINANCED | PurchaseOrderDistributionPEOAmountFinanced | — |
| AMOUNT_ORDERED | PurchaseOrderDistributionPEOAmountOrdered | ✅ |
| AMOUNT_RECOUPED | PurchaseOrderDistributionPEOAmountRecouped | — |
| AMOUNT_TO_ENCUMBER | PurchaseOrderDistributionPEOAmountToEncumber | — |
| AWARD_ID | PurchaseOrderDistributionPEOAwardId | — |
| BOM_RESOURCE_ID | PurchaseOrderDistributionPEOBomResourceId | — |
| BUDGET_ACCOUNT_ID | PurchaseOrderDistributionPEOBudgetAccountId | — |
| BUDGET_DATE | PurchaseOrderDistributionPEOBudgetDate | — |
| CLOSE_BUDGET_DATE | PurchaseOrderDistributionPEOCloseBudgetDate | — |
| CODE_COMBINATION_ID | PurchaseOrderDistributionPEOCodeCombinationId | — |
| CONSIGNMENT_QUANTITY | PurchaseOrderDistributionPEOConsignmentQuantity | — |
| CREATED_BY | PurchaseOrderDistributionPEOCreatedBy | — |
| CREATION_DATE | PurchaseOrderDistributionPEOCreationDate | — |
| DELIVER_TO_CUST_CONTACT_ID | PurchaseOrderDistributionPEODeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | PurchaseOrderDistributionPEODeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | PurchaseOrderDistributionPEODeliverToCustLocationId | — |
| DELIVER_TO_LOCATION_ID | PurchaseOrderDistributionPEODeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | PurchaseOrderDistributionPEODeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | PurchaseOrderDistributionPEODestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEODestVarianceAccountId | — |
| DESTINATION_CONTEXT | PurchaseOrderDistributionPEODestinationContext | — |
| DESTINATION_ORGANIZATION_ID | PurchaseOrderDistributionPEODestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | PurchaseOrderDistributionPEODestinationSubinventory | — |
| DESTINATION_TYPE_CODE | PurchaseOrderDistributionPEODestinationTypeCode | ✅ |
| DIST_INTENDED_USE | PurchaseOrderDistributionPEODistIntendedUse | — |
| DISTRIBUTION_NUM | PurchaseOrderDistributionPEODistributionNum | ✅ |
| DISTRIBUTION_TYPE | PurchaseOrderDistributionPEODistributionType | — |
| ENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOEncumberedAmount | — |
| ENCUMBERED_FLAG | PurchaseOrderDistributionPEOEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | PurchaseOrderDistributionPEOEndItemUnitNumber | — |
| FAILED_FUNDS_LOOKUP_CODE | PurchaseOrderDistributionPEOFailedFundsLookupCode | — |
| FUNDS_STATUS | PurchaseOrderDistributionPEOFundsStatus | — |
| GL_CANCELLED_DATE | PurchaseOrderDistributionPEOGlCancelledDate | — |
| GL_CLOSED_DATE | PurchaseOrderDistributionPEOGlClosedDate | — |
| GL_ENCUMBERED_DATE | PurchaseOrderDistributionPEOGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | PurchaseOrderDistributionPEOGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | PurchaseOrderDistributionPEOGovernmentContext | — |
| INTERFACE_DISTRIBUTION_REF | PurchaseOrderDistributionPEOInterfaceDistributionRef | — |
| INVOICE_ADJUSTMENT_FLAG | PurchaseOrderDistributionPEOInvoiceAdjustmentFlag | — |
| INVOICED_VAL_IN_NTFN | PurchaseOrderDistributionPEOInvoicedValInNtfn | — |
| JOB_DEFINITION_NAME | PurchaseOrderDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderDistributionPEOJobDefinitionPackage | — |
| KANBAN_CARD_ID | PurchaseOrderDistributionPEOKanbanCardId | — |
| LAST_UPDATE_DATE | PurchaseOrderDistributionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchaseOrderDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchaseOrderDistributionPEOLastUpdatedBy | — |
| LINE_LOCATION_ID | PurchaseOrderDistributionPEOLineLocationId | — |
| NONRECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEONonrecoverableInclusiveTax | — |
| NONRECOVERABLE_TAX | PurchaseOrderDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderDistributionPEOObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | PurchaseOrderDistributionPEOOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOOkeContractLineId | — |
| ORIGINAL_DISTRIBUTION_ID | PurchaseOrderDistributionPEOOriginalDistributionId | — |
| PJC_BILLABLE_FLAG | PurchaseOrderDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | PurchaseOrderDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | PurchaseOrderDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | PurchaseOrderDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | PurchaseOrderDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | PurchaseOrderDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | PurchaseOrderDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | PurchaseOrderDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | PurchaseOrderDistributionPEOPJC_PROJECT_ID | — |
| PJC_TASK_ID | PurchaseOrderDistributionPEOPJC_TASK_ID | — |
| PJC_WORK_TYPE_ID | PurchaseOrderDistributionPEOPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | PurchaseOrderDistributionPEOPoDistributionId | ✅ |
| PO_HEADER_ID | PurchaseOrderDistributionPEOPoHeaderId | — |
| PO_LINE_ID | PurchaseOrderDistributionPEOPoLineId | — |
| PRC_BU_ID | PurchaseOrderDistributionPEOPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | PurchaseOrderDistributionPEOPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | PurchaseOrderDistributionPEOProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderDistributionPEOProgramName | — |
| QUANTITY_BILLED | PurchaseOrderDistributionPEOQuantityBilled | — |
| QUANTITY_CANCELLED | PurchaseOrderDistributionPEOQuantityCancelled | — |
| QUANTITY_DELIVERED | PurchaseOrderDistributionPEOQuantityDelivered | — |
| QUANTITY_FINANCED | PurchaseOrderDistributionPEOQuantityFinanced | — |
| QUANTITY_ORDERED | PurchaseOrderDistributionPEOQuantityOrdered | ✅ |
| QUANTITY_RECOUPED | PurchaseOrderDistributionPEOQuantityRecouped | — |
| RATE | PurchaseOrderDistributionPEORate | — |
| RATE_DATE | PurchaseOrderDistributionPEORateDate | — |
| RECOVERABLE_INCLUSIVE_TAX | PurchaseOrderDistributionPEORecoverableInclusiveTax | — |
| RECOVERABLE_TAX | PurchaseOrderDistributionPEORecoverableTax | — |
| RECOVERY_RATE | PurchaseOrderDistributionPEORecoveryRate | — |
| REQ_BU_ID | PurchaseOrderDistributionPEOReqBuId | — |
| REQ_DISTRIBUTION_ID | PurchaseOrderDistributionPEOReqDistributionId | ✅ |
| REQ_HEADER_REFERENCE_NUM | PurchaseOrderDistributionPEOReqHeaderReferenceNum | — |
| REQ_LINE_REFERENCE_NUM | PurchaseOrderDistributionPEOReqLineReferenceNum | ✅ |
| REQUEST_ID | PurchaseOrderDistributionPEORequestId | — |
| RETAINAGE_RELEASED_AMOUNT | PurchaseOrderDistributionPEORetainageReleasedAmount | — |
| RETAINAGE_WITHHELD_AMOUNT | PurchaseOrderDistributionPEORetainageWithheldAmount | — |
| SET_OF_BOOKS_ID | PurchaseOrderDistributionPEOSetOfBooksId | — |
| SOURCE_DISTRIBUTION_ID | PurchaseOrderDistributionPEOSourceDistributionId | — |
| TAX_EXCLUSIVE_AMOUNT | PurchaseOrderDistributionPEOTaxExclusiveAmount | — |
| TAX_RECOVERY_OVERRIDE_FLAG | PurchaseOrderDistributionPEOTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | PurchaseOrderDistributionPEOUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | PurchaseOrderDistributionPEOUnencumberedQuantity | — |
| VARIANCE_ACCOUNT_ID | PurchaseOrderDistributionPEOVarianceAccountId | — |
| WIP_ENTITY_ID | PurchaseOrderDistributionPEOWipEntityId | — |
| WIP_LINE_ID | PurchaseOrderDistributionPEOWipLineId | — |
| WIP_OPERATION_SEQ_NUM | PurchaseOrderDistributionPEOWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | PurchaseOrderDistributionPEOWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | PurchaseOrderDistributionPEOWipResourceSeqNum | — |

---

## 📚 Referências

- [Oracle Docs — PO_DISTRIBUTIONS_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/podistributionsall-10187.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
