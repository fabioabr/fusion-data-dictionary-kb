---
id: DOC-PO-117
doc_type: system-doc
title: "PO_DISTRIBUTIONS_DRAFT_ALL — Distribuicoes de PO em Rascunho"
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
  - PO_DISTRIBUTIONS_DRAFT_ALL
  - po_distributions_draft_all
  - po-distributions-draft-all
  - po-distributions
  - distribuicoes-de-po-em-rascunho
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_DISTRIBUTIONS_DRAFT_ALL

## 📌 Visão Geral

Armazena as **distribuicoes contabeis de POs em fase de rascunho**. Estrutura identica a `PO_DISTRIBUTIONS_ALL` para POs em elaboracao.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Edicao:** Distribuicoes de POs antes da submissao.
- **Amendments:** Distribuicoes alteradas durante emendas.
- **Validacao:** Verificacao antes da aprovacao.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PO_DISTRIBUTION_ID | NUMBER(18) | NOT NULL | PK | ID da distribuicao | — | 🟢 95% |
| 2 | DRAFT_ID | NUMBER(18) | NOT NULL | FK | ID do rascunho | [[po_headers_draft_all]] | 🟢 95% |
| 3 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho | [[po_headers_draft_all]] | 🟢 95% |
| 4 | PO_LINE_ID | NUMBER(18) | NOT NULL | FK | Linha | [[po_lines_draft_all]] | 🟢 95% |
| 5 | LINE_LOCATION_ID | NUMBER(18) | NOT NULL | FK | Schedule | [[po_line_locations_draft_all]] | 🟢 95% |
| 6 | DISTRIBUTION_NUM | NUMBER | NOT NULL | Identificacao | Numero da distribuicao | — | 🟢 100% |
| 7 | QUANTITY_ORDERED | NUMBER | NULL | Quantidade | Quantidade | — | 🟢 100% |
| 8 | CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | CCID | [[gl_code_combinations]] | 🟢 100% |
| 9 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 100% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_draft_all]] — via `PO_HEADER_ID`/`DRAFT_ID` (rascunho do PO ao qual a distribuição draft pertence)
- [[po_lines_draft_all]] — via `PO_LINE_ID` (linha draft do PO da distribuição em rascunho)
- [[po_line_locations_draft_all]] — via `LINE_LOCATION_ID` (shipment draft ao qual a distribuição draft pertence)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (conta contábil da distribuição draft do PO)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Distribuicoes de um draft
```sql
SELECT PO_DISTRIBUTION_ID, DISTRIBUTION_NUM, QUANTITY_ORDERED, CODE_COMBINATION_ID
FROM   PO_DISTRIBUTIONS_DRAFT_ALL
WHERE  PO_HEADER_ID = :p_header_id AND DRAFT_ID = :p_draft_id;
```

---

## 🔒 Observações

- Dados migram para `PO_DISTRIBUTIONS_ALL` apos aprovacao.
- O `DRAFT_ID` identifica a versao em edicao.
- Estrutura espelha `PO_DISTRIBUTIONS_ALL`.

---

## 🔗 PVOs Relacionados

### [[draftpurchaseorderdistributionpvo|DraftPurchaseOrderDistributionPVO]] (PO · BICC: 15/115)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | DraftDistributionAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | DraftDistributionAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | DraftDistributionAccruedFlag | — |
| AMOUNT_ORDERED | DraftDistributionAmountOrdered | ✅ |
| AMOUNT_TO_ENCUMBER | DraftDistributionAmountToEncumber | — |
| AWARD_ID | DraftDistributionAwardId | — |
| BOM_RESOURCE_ID | DraftDistributionBomResourceId | — |
| BUDGET_ACCOUNT_ID | DraftDistributionBudgetAccountId | — |
| BUDGET_DATE | DraftDistributionBudgetDate | ✅ |
| CHANGE_ACCEPTED_FLAG | DraftDistributionChangeAcceptedFlag | — |
| CO_AMOUNT_CANCELLED | DraftDistributionCoAmountCancelled | ✅ |
| CO_QUANTITY_CANCELLED | DraftDistributionCoQuantityCancelled | ✅ |
| CODE_COMBINATION_ID | DraftDistributionCodeCombinationId | — |
| CREATED_BY | DraftDistributionCreatedBy | — |
| CREATION_DATE | DraftDistributionCreationDate | — |
| DELIVER_TO_CUST_CONTACT_ID | DraftDistributionDeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | DraftDistributionDeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | DraftDistributionDeliverToCustLocationId | ✅ |
| DELIVER_TO_LOCATION_ID | DraftDistributionDeliverToLocationId | ✅ |
| DELIVER_TO_PERSON_ID | DraftDistributionDeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | DraftDistributionDestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | DraftDistributionDestVarianceAccountId | — |
| DESTINATION_CONTEXT | DraftDistributionDestinationContext | — |
| DESTINATION_ORGANIZATION_ID | DraftDistributionDestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | DraftDistributionDestinationSubinventory | — |
| DESTINATION_TYPE_CODE | DraftDistributionDestinationTypeCode | — |
| DIST_INTENDED_USE | DraftDistributionDistIntendedUse | — |
| DISTRIBUTION_NUM | DraftDistributionDistributionNum | ✅ |
| DISTRIBUTION_TYPE | DraftDistributionDistributionType | — |
| ENCUMBERED_AMOUNT | DraftDistributionEncumberedAmount | — |
| ENCUMBERED_FLAG | DraftDistributionEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | DraftDistributionEndItemUnitNumber | — |
| ENTITY_CHANGE_TYPE_CODE | DraftDistributionEntityChangeTypeCode | — |
| EXTERNAL_CHANGE_FLAG | DraftDistributionExternalChangeFlag | — |
| FAILED_FUNDS_LOOKUP_CODE | DraftDistributionFailedFundsLookupCode | — |
| FUNDS_STATUS | DraftDistributionFundsStatus | ✅ |
| GL_CANCELLED_DATE | DraftDistributionGlCancelledDate | — |
| GL_ENCUMBERED_DATE | DraftDistributionGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | DraftDistributionGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | DraftDistributionGovernmentContext | — |
| JOB_DEFINITION_NAME | DraftDistributionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | DraftDistributionJobDefinitionPackage | — |
| KANBAN_CARD_ID | DraftDistributionKanbanCardId | — |
| LAST_UPDATE_DATE | DraftDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DraftDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | DraftDistributionLastUpdatedBy | — |
| LINE_LOCATION_ID | DraftDistributionLineLocationId | — |
| NONRECOVERABLE_TAX | DraftDistributionNonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | DraftDistributionObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | DraftDistributionOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | DraftDistributionOkeContractLineId | — |
| PJC_BILLABLE_FLAG | DraftDistributionPjcBillableFlag | — |
| PJC_CAPITALIZABLE_FLAG | DraftDistributionPjcCapitalizableFlag | — |
| PJC_CONTEXT_CATEGORY | DraftDistributionPjcContextCategory | — |
| PJC_CONTRACT_ID | DraftDistributionPjcContractId | — |
| PJC_CONTRACT_LINE_ID | DraftDistributionPjcContractLineId | — |
| PJC_EXPENDITURE_ITEM_DATE | DraftDistributionPjcExpenditureItemDate | — |
| PJC_EXPENDITURE_TYPE_ID | DraftDistributionPjcExpenditureTypeId | — |
| PJC_FUNDING_ALLOCATION_ID | DraftDistributionPjcFundingAllocationId | — |
| PJC_ORGANIZATION_ID | DraftDistributionPjcOrganizationId | — |
| PJC_PROJECT_ID | DraftDistributionPjcProjectId | — |
| PJC_RESERVED_ATTRIBUTE1 | DraftDistributionPjcReservedAttribute1 | — |
| PJC_RESERVED_ATTRIBUTE10 | DraftDistributionPjcReservedAttribute10 | — |
| PJC_RESERVED_ATTRIBUTE2 | DraftDistributionPjcReservedAttribute2 | — |
| PJC_RESERVED_ATTRIBUTE3 | DraftDistributionPjcReservedAttribute3 | — |
| PJC_RESERVED_ATTRIBUTE4 | DraftDistributionPjcReservedAttribute4 | — |
| PJC_RESERVED_ATTRIBUTE5 | DraftDistributionPjcReservedAttribute5 | — |
| PJC_RESERVED_ATTRIBUTE6 | DraftDistributionPjcReservedAttribute6 | — |
| PJC_RESERVED_ATTRIBUTE7 | DraftDistributionPjcReservedAttribute7 | — |
| PJC_RESERVED_ATTRIBUTE8 | DraftDistributionPjcReservedAttribute8 | — |
| PJC_RESERVED_ATTRIBUTE9 | DraftDistributionPjcReservedAttribute9 | — |
| PJC_TASK_ID | DraftDistributionPjcTaskId | — |
| PJC_USER_DEF_ATTRIBUTE1 | DraftDistributionPjcUserDefAttribute1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | DraftDistributionPjcUserDefAttribute10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | DraftDistributionPjcUserDefAttribute2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | DraftDistributionPjcUserDefAttribute3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | DraftDistributionPjcUserDefAttribute4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | DraftDistributionPjcUserDefAttribute5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | DraftDistributionPjcUserDefAttribute6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | DraftDistributionPjcUserDefAttribute7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | DraftDistributionPjcUserDefAttribute8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | DraftDistributionPjcUserDefAttribute9 | — |
| PJC_WORK_TYPE_ID | DraftDistributionPjcWorkTypeId | — |
| PO_DISTRIBUTION_ID | PoDistributionId | ✅ |
| PO_HEADER_ID | DraftDistributionPoHeaderId | — |
| PO_LINE_ID | DraftDistributionPoLineId | — |
| PRC_BU_ID | DraftDistributionPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | DraftDistributionPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | DraftDistributionProgramAppName | — |
| PROGRAM_NAME | DraftDistributionProgramName | — |
| QUANTITY_ORDERED | DraftDistributionQuantityOrdered | ✅ |
| RATE | DraftDistributionRate | ✅ |
| RATE_DATE | DraftDistributionRateDate | — |
| REASON_FOR_CHANGE | DraftDistributionReasonForChange | ✅ |
| RECOVERABLE_TAX | DraftDistributionRecoverableTax | — |
| RECOVERY_RATE | DraftDistributionRecoveryRate | — |
| REQ_BU_ID | DraftDistributionReqBuId | — |
| REQ_DISTRIBUTION_ID | DraftDistributionReqDistributionId | — |
| REQ_HEADER_REFERENCE_NUM | DraftDistributionReqHeaderReferenceNum | ✅ |
| REQ_LINE_REFERENCE_NUM | DraftDistributionReqLineReferenceNum | ✅ |
| REQUEST_ID | DraftDistributionRequestId | — |
| SET_OF_BOOKS_ID | DraftDistributionSetOfBooksId | — |
| SHIPPING_UOM_QUANTITY | DraftDistributionShippingUomQuantity | — |
| SOURCE_DISTRIBUTION_ID | DraftDistributionSourceDistributionId | — |
| TAX_ATTRIBUTE_UPDATE_CODE | DraftDistributionTaxAttributeUpdateCode | — |
| TAX_RECOVERY_OVERRIDE_FLAG | DraftDistributionTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | DraftDistributionUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | DraftDistributionUnencumberedQuantity | — |
| USER_PO_CHRG_ACCT_CHG_FLAG | DraftDistributionUserPoChrgAcctChgFlag | — |
| VARIANCE_ACCOUNT_ID | DraftDistributionVarianceAccountId | — |
| WIP_ENTITY_ID | DraftDistributionWipEntityId | — |
| WIP_LINE_ID | DraftDistributionWipLineId | — |
| WIP_OPERATION_SEQ_NUM | DraftDistributionWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | DraftDistributionWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | DraftDistributionWipResourceSeqNum | — |

### [[draftpurchaseorderdistributionrefpvo|DraftPurchaseOrderDistributionRefPVO]] (PO · BICC: 5/115)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | DraftDistributionAccrualAccountId | — |
| ACCRUE_ON_RECEIPT_FLAG | DraftDistributionAccrueOnReceiptFlag | — |
| ACCRUED_FLAG | DraftDistributionAccruedFlag | — |
| AMOUNT_ORDERED | DraftDistributionAmountOrdered | — |
| AMOUNT_TO_ENCUMBER | DraftDistributionAmountToEncumber | — |
| AWARD_ID | DraftDistributionAwardId | — |
| BOM_RESOURCE_ID | DraftDistributionBomResourceId | — |
| BUDGET_ACCOUNT_ID | DraftDistributionBudgetAccountId | — |
| BUDGET_DATE | DraftDistributionBudgetDate | ✅ |
| CHANGE_ACCEPTED_FLAG | DraftDistributionChangeAcceptedFlag | — |
| CO_AMOUNT_CANCELLED | DraftDistributionCoAmountCancelled | — |
| CO_QUANTITY_CANCELLED | DraftDistributionCoQuantityCancelled | — |
| CODE_COMBINATION_ID | DraftDistributionCodeCombinationId | — |
| CREATED_BY | DraftDistributionCreatedBy | — |
| CREATION_DATE | DraftDistributionCreationDate | — |
| DELIVER_TO_CUST_CONTACT_ID | DraftDistributionDeliverToCustContactId | — |
| DELIVER_TO_CUST_ID | DraftDistributionDeliverToCustId | — |
| DELIVER_TO_CUST_LOCATION_ID | DraftDistributionDeliverToCustLocationId | — |
| DELIVER_TO_LOCATION_ID | DraftDistributionDeliverToLocationId | — |
| DELIVER_TO_PERSON_ID | DraftDistributionDeliverToPersonId | — |
| DEST_CHARGE_ACCOUNT_ID | DraftDistributionDestChargeAccountId | — |
| DEST_VARIANCE_ACCOUNT_ID | DraftDistributionDestVarianceAccountId | — |
| DESTINATION_CONTEXT | DraftDistributionDestinationContext | — |
| DESTINATION_ORGANIZATION_ID | DraftDistributionDestinationOrganizationId | — |
| DESTINATION_SUBINVENTORY | DraftDistributionDestinationSubinventory | — |
| DESTINATION_TYPE_CODE | DraftDistributionDestinationTypeCode | — |
| DIST_INTENDED_USE | DraftDistributionDistIntendedUse | — |
| DISTRIBUTION_NUM | DraftDistributionDistributionNum | — |
| DISTRIBUTION_TYPE | DraftDistributionDistributionType | — |
| ENCUMBERED_AMOUNT | DraftDistributionEncumberedAmount | — |
| ENCUMBERED_FLAG | DraftDistributionEncumberedFlag | — |
| END_ITEM_UNIT_NUMBER | DraftDistributionEndItemUnitNumber | — |
| ENTITY_CHANGE_TYPE_CODE | DraftDistributionEntityChangeTypeCode | — |
| EXTERNAL_CHANGE_FLAG | DraftDistributionExternalChangeFlag | — |
| FAILED_FUNDS_LOOKUP_CODE | DraftDistributionFailedFundsLookupCode | — |
| FUNDS_STATUS | DraftDistributionFundsStatus | — |
| GL_CANCELLED_DATE | DraftDistributionGlCancelledDate | — |
| GL_ENCUMBERED_DATE | DraftDistributionGlEncumberedDate | — |
| GL_ENCUMBERED_PERIOD_NAME | DraftDistributionGlEncumberedPeriodName | — |
| GOVERNMENT_CONTEXT | DraftDistributionGovernmentContext | — |
| JOB_DEFINITION_NAME | DraftDistributionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | DraftDistributionJobDefinitionPackage | — |
| KANBAN_CARD_ID | DraftDistributionKanbanCardId | — |
| LAST_UPDATE_DATE | DraftDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DraftDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | DraftDistributionLastUpdatedBy | — |
| LINE_LOCATION_ID | DraftDistributionLineLocationId | — |
| NONRECOVERABLE_TAX | DraftDistributionNonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | DraftDistributionObjectVersionNumber | — |
| OKE_CONTRACT_DELIVERABLE_ID | DraftDistributionOkeContractDeliverableId | — |
| OKE_CONTRACT_LINE_ID | DraftDistributionOkeContractLineId | — |
| PJC_BILLABLE_FLAG | DraftDistributionPjcBillableFlag | — |
| PJC_CAPITALIZABLE_FLAG | DraftDistributionPjcCapitalizableFlag | ✅ |
| PJC_CONTEXT_CATEGORY | DraftDistributionPjcContextCategory | — |
| PJC_CONTRACT_ID | DraftDistributionPjcContractId | — |
| PJC_CONTRACT_LINE_ID | DraftDistributionPjcContractLineId | — |
| PJC_EXPENDITURE_ITEM_DATE | DraftDistributionPjcExpenditureItemDate | ✅ |
| PJC_EXPENDITURE_TYPE_ID | DraftDistributionPjcExpenditureTypeId | — |
| PJC_FUNDING_ALLOCATION_ID | DraftDistributionPjcFundingAllocationId | — |
| PJC_ORGANIZATION_ID | DraftDistributionPjcOrganizationId | — |
| PJC_PROJECT_ID | DraftDistributionPjcProjectId | — |
| PJC_RESERVED_ATTRIBUTE1 | DraftDistributionPjcReservedAttribute1 | — |
| PJC_RESERVED_ATTRIBUTE10 | DraftDistributionPjcReservedAttribute10 | — |
| PJC_RESERVED_ATTRIBUTE2 | DraftDistributionPjcReservedAttribute2 | — |
| PJC_RESERVED_ATTRIBUTE3 | DraftDistributionPjcReservedAttribute3 | — |
| PJC_RESERVED_ATTRIBUTE4 | DraftDistributionPjcReservedAttribute4 | — |
| PJC_RESERVED_ATTRIBUTE5 | DraftDistributionPjcReservedAttribute5 | — |
| PJC_RESERVED_ATTRIBUTE6 | DraftDistributionPjcReservedAttribute6 | — |
| PJC_RESERVED_ATTRIBUTE7 | DraftDistributionPjcReservedAttribute7 | — |
| PJC_RESERVED_ATTRIBUTE8 | DraftDistributionPjcReservedAttribute8 | — |
| PJC_RESERVED_ATTRIBUTE9 | DraftDistributionPjcReservedAttribute9 | — |
| PJC_TASK_ID | DraftDistributionPjcTaskId | — |
| PJC_USER_DEF_ATTRIBUTE1 | DraftDistributionPjcUserDefAttribute1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | DraftDistributionPjcUserDefAttribute10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | DraftDistributionPjcUserDefAttribute2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | DraftDistributionPjcUserDefAttribute3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | DraftDistributionPjcUserDefAttribute4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | DraftDistributionPjcUserDefAttribute5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | DraftDistributionPjcUserDefAttribute6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | DraftDistributionPjcUserDefAttribute7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | DraftDistributionPjcUserDefAttribute8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | DraftDistributionPjcUserDefAttribute9 | — |
| PJC_WORK_TYPE_ID | DraftDistributionPjcWorkTypeId | — |
| PO_DISTRIBUTION_ID | PoDistributionId | ✅ |
| PO_HEADER_ID | DraftDistributionPoHeaderId | — |
| PO_LINE_ID | DraftDistributionPoLineId | — |
| PRC_BU_ID | DraftDistributionPrcBuId | — |
| PREVENT_ENCUMBRANCE_FLAG | DraftDistributionPreventEncumbranceFlag | — |
| PROGRAM_APP_NAME | DraftDistributionProgramAppName | — |
| PROGRAM_NAME | DraftDistributionProgramName | — |
| QUANTITY_ORDERED | DraftDistributionQuantityOrdered | — |
| RATE | DraftDistributionRate | — |
| RATE_DATE | DraftDistributionRateDate | — |
| REASON_FOR_CHANGE | DraftDistributionReasonForChange | — |
| RECOVERABLE_TAX | DraftDistributionRecoverableTax | — |
| RECOVERY_RATE | DraftDistributionRecoveryRate | — |
| REQ_BU_ID | DraftDistributionReqBuId | — |
| REQ_DISTRIBUTION_ID | DraftDistributionReqDistributionId | — |
| REQ_HEADER_REFERENCE_NUM | DraftDistributionReqHeaderReferenceNum | — |
| REQ_LINE_REFERENCE_NUM | DraftDistributionReqLineReferenceNum | — |
| REQUEST_ID | DraftDistributionRequestId | — |
| SET_OF_BOOKS_ID | DraftDistributionSetOfBooksId | — |
| SHIPPING_UOM_QUANTITY | DraftDistributionShippingUomQuantity | — |
| SOURCE_DISTRIBUTION_ID | DraftDistributionSourceDistributionId | — |
| TAX_ATTRIBUTE_UPDATE_CODE | DraftDistributionTaxAttributeUpdateCode | — |
| TAX_RECOVERY_OVERRIDE_FLAG | DraftDistributionTaxRecoveryOverrideFlag | — |
| UNENCUMBERED_AMOUNT | DraftDistributionUnencumberedAmount | — |
| UNENCUMBERED_QUANTITY | DraftDistributionUnencumberedQuantity | — |
| USER_PO_CHRG_ACCT_CHG_FLAG | DraftDistributionUserPoChrgAcctChgFlag | — |
| VARIANCE_ACCOUNT_ID | DraftDistributionVarianceAccountId | — |
| WIP_ENTITY_ID | DraftDistributionWipEntityId | — |
| WIP_LINE_ID | DraftDistributionWipLineId | — |
| WIP_OPERATION_SEQ_NUM | DraftDistributionWipOperationSeqNum | — |
| WIP_REPETITIVE_SCHEDULE_ID | DraftDistributionWipRepetitiveScheduleId | — |
| WIP_RESOURCE_SEQ_NUM | DraftDistributionWipResourceSeqNum | — |

### [[draftpurchasingdocumentdistributionextractpvo|DraftPurchasingDocumentDistributionExtractPVO]] (PO · BICC: 68/69)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_ACCOUNT_ID | AccrualAccountId | ✅ |
| ACCRUE_ON_RECEIPT_FLAG | AccrueOnReceiptFlag | ✅ |
| ACCRUED_FLAG | AccruedFlag | ✅ |
| AMOUNT_ORDERED | AmountOrdered | ✅ |
| BUDGET_DATE | BudgetDate | ✅ |
| CHANGE_ACCEPTED_FLAG | ChangeAcceptedFlag | ✅ |
| CO_AMOUNT_CANCELLED | CoAmountCancelled | ✅ |
| CO_QUANTITY_CANCELLED | CoQuantityCancelled | ✅ |
| CODE_COMBINATION_ID | CodeCombinationId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DELIVER_TO_CUST_CONTACT_ID | DeliverToCustContactId | ✅ |
| DELIVER_TO_CUST_ID | DeliverToCustId | ✅ |
| DELIVER_TO_CUST_LOCATION_ID | DeliverToCustLocationId | ✅ |
| DELIVER_TO_LOCATION_ID | DeliverToLocationId | ✅ |
| DELIVER_TO_PERSON_ID | DeliverToPersonId | ✅ |
| DEST_CHARGE_ACCOUNT_ID | DestChargeAccountId | ✅ |
| DEST_VARIANCE_ACCOUNT_ID | DestVarianceAccountId | ✅ |
| DESTINATION_CONTEXT | DestinationContext | ✅ |
| DESTINATION_ORGANIZATION_ID | DestinationOrganizationId | ✅ |
| DESTINATION_SUBINVENTORY | DestinationSubinventory | ✅ |
| DESTINATION_TYPE_CODE | DestinationTypeCode | ✅ |
| DIST_INTENDED_USE | DistIntendedUse | — |
| DISTRIBUTION_NUM | DistributionNum | ✅ |
| ENTITY_CHANGE_TYPE_CODE | EntityChangeTypeCode | ✅ |
| EXTERNAL_CHANGE_FLAG | ExternalChangeFlag | ✅ |
| FUNDS_STATUS | FundsStatus | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | ✅ |
| KANBAN_CARD_ID | KanbanCardId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LINE_LOCATION_ID | LineLocationId | ✅ |
| NONRECOVERABLE_INCLUSIVE_TAX | NonrecoverableInclusiveTax | ✅ |
| NONRECOVERABLE_TAX | NonrecoverableTax | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORIGINAL_DISTRIBUTION_ID | OriginalDistributionId | ✅ |
| PJC_CONTEXT_CATEGORY | PjcContextCategory | ✅ |
| PJC_EXPENDITURE_TYPE_ID | PjcExpenditureTypeId | ✅ |
| PJC_ORGANIZATION_ID | PjcOrganizationId | ✅ |
| PJC_PROJECT_ID | PjcProjectId | ✅ |
| PJC_TASK_ID | PjcTaskId | ✅ |
| PO_DISTRIBUTION_ID | PoDistributionId | ✅ |
| PO_HEADER_ID | PoHeaderId | ✅ |
| PO_LINE_ID | PoLineId | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| PROGRAM_APP_NAME | ProgramAppName | ✅ |
| PROGRAM_NAME | ProgramName | ✅ |
| QUANTITY_ORDERED | QuantityOrdered | ✅ |
| RATE | Rate | ✅ |
| RATE_DATE | RateDate | ✅ |
| REASON_FOR_CHANGE | ReasonForChange | ✅ |
| RECOVERABLE_INCLUSIVE_TAX | RecoverableInclusiveTax | ✅ |
| RECOVERABLE_TAX | RecoverableTax | ✅ |
| RECOVERY_RATE | RecoveryRate | ✅ |
| REQ_BU_ID | ReqBuId | ✅ |
| REQ_DISTRIBUTION_ID | ReqDistributionId | ✅ |
| REQ_HEADER_REFERENCE_NUM | ReqHeaderReferenceNum | ✅ |
| REQ_LINE_REFERENCE_NUM | ReqLineReferenceNum | ✅ |
| REQUEST_ID | RequestId | ✅ |
| SET_OF_BOOKS_ID | SetOfBooksId | ✅ |
| SHIPPING_UOM_QUANTITY | ShippingUomQuantity | ✅ |
| TAX_ATTRIBUTE_UPDATE_CODE | TaxAttributeUpdateCode | ✅ |
| TAX_EXCLUSIVE_AMOUNT | TaxExclusiveAmount | ✅ |
| TAX_RECOVERY_OVERRIDE_FLAG | TaxRecoveryOverrideFlag | ✅ |
| UNENCUMBERED_AMOUNT | UnencumberedAmount | ✅ |
| USER_PO_CHRG_ACCT_CHG_FLAG | UserPoChrgAcctChgFlag | ✅ |
| VARIANCE_ACCOUNT_ID | VarianceAccountId | ✅ |

---

## 📚 Referências

- [Oracle Docs — PO_DISTRIBUTIONS_DRAFT_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
