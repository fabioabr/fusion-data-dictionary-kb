---
id: DOC-AP-012
doc_type: system-doc
title: "AP_INVOICE_DISTRIBUTIONS_ALL — Distribuições Contábeis de Faturas"
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
  - distribuicoes
  - distributions
  - contabilidade
aliases:
  - AP_INVOICE_DISTRIBUTIONS_ALL
  - ap_invoice_distributions_all
  - distribuicoes-ap
  - invoice-distributions
  - distribuicoes-faturas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_INVOICE_DISTRIBUTIONS_ALL

## 📌 Visão Geral

Armazena as **distribuições contábeis** de cada fatura do módulo Accounts Payable. Cada linha representa uma alocação de valor a uma combinação de contas contábeis (code combination), definindo como o valor da fatura será contabilizado no General Ledger. Uma fatura pode ter múltiplas distribuições, permitindo rateio entre centros de custo, projetos ou contas diferentes.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Contabilização de faturas:** Define as contas contábeis de débito para cada parcela da fatura, gerando os lançamentos no GL.
- **Rateio de custos:** Permite distribuir o valor de uma fatura entre múltiplos centros de custo, projetos ou departamentos.
- **Three-way matching:** Vinculação com PO distributions e recebimentos para validação de matching.
- **Retenções fiscais:** Suporte a withholding tax com distribuições específicas de tipo TAX e AWT.
- **Auditoria contábil:** Rastreabilidade da alocação contábil de cada fatura até o nível de code combination.
- **Integração com projetos:** Distribuições podem ser vinculadas a projetos e tarefas para capitalização ou custeio.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INVOICE_DISTRIBUTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da distribuição | — | 🟢 100% |
| 2 | INVOICE_ID | NUMBER(18) | NOT NULL | FK | Fatura à qual pertence a distribuição | [[ap_invoices_all]] | 🟢 100% |
| 3 | INVOICE_LINE_NUMBER | NUMBER | NOT NULL | FK | Número da linha da fatura | [[ap_invoice_lines_all]] | 🟢 100% |
| 4 | DISTRIBUTION_LINE_NUMBER | NUMBER | NOT NULL | Identificação | Número sequencial da distribuição na linha | — | 🟢 100% |
| 5 | LINE_TYPE_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Classificação | Tipo da distribuição (ITEM/TAX/FREIGHT/MISCELLANEOUS/AWT) | [[ap_lookup_codes]] | 🟢 100% |
| 6 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor da distribuição na moeda da transação | — | 🟢 100% |
| 7 | BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda funcional (ledger) | — | 🟢 100% |
| 8 | DIST_CODE_COMBINATION_ID | NUMBER(18) | NOT NULL | Contabilidade | Conta contábil de débito (code combination) | [[gl_code_combinations]] | 🟢 100% |
| 9 | ACCOUNTING_DATE | DATE | NOT NULL | Contabilidade | Data contábil da distribuição | — | 🟢 100% |
| 10 | PERIOD_NAME | VARCHAR2(15) | NULL | Contabilidade | Nome do período contábil | [[gl_period_statuses]] | 🟢 100% |
| 11 | ACCRUAL_POSTED_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se accrual foi lançado (Y/N) | — | 🟢 100% |
| 12 | CASH_POSTED_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se cash basis foi lançado (Y/N) | — | 🟢 100% |
| 13 | POSTED_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se foi contabilizado no GL (Y/N) | — | 🟢 100% |
| 14 | MATCH_STATUS_FLAG | VARCHAR2(1) | NULL | Status | Status de matching (A=aprovado/T=testado/N=não testado) | — | 🟢 100% |
| 15 | QUANTITY_INVOICED | NUMBER | NULL | Quantidade | Quantidade faturada | — | 🟢 100% |
| 16 | UNIT_PRICE | NUMBER | NULL | Financeiro | Preço unitário | — | 🟢 100% |
| 17 | PO_DISTRIBUTION_ID | NUMBER(18) | NULL | Referência cruzada | Distribuição do PO vinculada (matching) | [[po_distributions_all]] | 🟢 100% |
| 18 | RCV_TRANSACTION_ID | NUMBER(18) | NULL | Referência cruzada | Transação de recebimento vinculada | [[rcv_transactions]] | 🟢 100% |
| 19 | ASSETS_TRACKING_FLAG | VARCHAR2(1) | NULL | Controle | Rastreamento de ativo fixo (Y/N) | — | 🟢 100% |
| 20 | ASSET_BOOK_TYPE_CODE | VARCHAR2(15) | NULL | Ativo fixo | Livro de ativos para capitalização | — | 🟡 75% |
| 21 | ASSET_CATEGORY_ID | NUMBER(18) | NULL | Ativo fixo | Categoria do ativo | — | 🟡 75% |
| 22 | PROJECT_ID | NUMBER(18) | NULL | Projetos | Projeto vinculado | [[pjf_projects_all_b]] | 🟢 100% |
| 23 | TASK_ID | NUMBER(18) | NULL | Projetos | Tarefa do projeto | [[pjf_tasks_b]] | 🟢 100% |
| 24 | EXPENDITURE_TYPE | VARCHAR2(30) | NULL | Projetos | Tipo de despesa do projeto | — | 🟢 100% |
| 25 | EXPENDITURE_ORGANIZATION_ID | NUMBER(18) | NULL | Projetos | Organização de despesa | — | 🟢 100% |
| 26 | PA_ADDITION_FLAG | VARCHAR2(1) | NULL | Projetos | Indica se foi transferido para Projects (Y/N/T/Z) | — | 🟢 100% |
| 27 | AWT_GROUP_ID | NUMBER(18) | NULL | Fiscal | Grupo de withholding tax | — | 🟡 75% |
| 28 | WITHHOLDING_TAX_CODE_ID | NUMBER(18) | NULL | Fiscal | Código de retenção fiscal | — | 🟡 75% |
| 29 | REVERSAL_FLAG | VARCHAR2(1) | NULL | Status | Indica se é distribuição de reversão (Y/N) | — | 🟢 100% |
| 30 | PARENT_REVERSAL_ID | NUMBER(18) | NULL | Referência cruzada | ID da distribuição original revertida | [[ap_invoice_distributions_all]] | 🟢 100% |
| 31 | CANCELLATION_FLAG | VARCHAR2(1) | NULL | Status | Indica se foi cancelada (Y/N) | — | 🟢 100% |
| 32 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 33 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 34 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 35 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 36 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 37 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 38 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 39 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ap_invoices_all]] — via `INVOICE_ID` (fatura à qual a distribuição contábil pertence)
- [[ap_invoice_lines_all]] — via `INVOICE_ID` + `INVOICE_LINE_NUMBER` (linha da fatura)
- [[gl_code_combinations]] — via `DIST_CODE_COMBINATION_ID` (conta contábil da distribuição da fatura)
- [[po_distributions_all]] — via `PO_DISTRIBUTION_ID` (distribuição do PO)
- [[rcv_transactions]] — via `RCV_TRANSACTION_ID` (transação de recebimento vinculada à distribuição)
- [[pjf_projects_all_b]] — via `PROJECT_ID` (projeto ao qual a despesa da distribuição é imputada)
- [[pjf_tasks_b]] — via `TASK_ID` (tarefa do projeto)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da distribuição da fatura)

### Tabelas-filha (FK de saída)
- [[ap_payment_hist_dists]] — via `INVOICE_DISTRIBUTION_ID` (distribuições de pagamento)
- [[ap_invoice_distributions_all]] — via `PARENT_REVERSAL_ID` (auto-referência para reversões)

---

## 📎 Uso Típico

### Distribuições de uma fatura
```sql
SELECT aid.DISTRIBUTION_LINE_NUMBER, aid.LINE_TYPE_LOOKUP_CODE,
       aid.AMOUNT, gcc.SEGMENT1 || '-' || gcc.SEGMENT2 AS conta
FROM   AP_INVOICE_DISTRIBUTIONS_ALL aid
JOIN   GL_CODE_COMBINATIONS gcc ON gcc.CODE_COMBINATION_ID = aid.DIST_CODE_COMBINATION_ID
WHERE  aid.INVOICE_ID = :p_invoice_id
ORDER BY aid.DISTRIBUTION_LINE_NUMBER;
```

### Total distribuído por conta contábil
```sql
SELECT gcc.SEGMENT1, gcc.SEGMENT2, gcc.SEGMENT3,
       SUM(aid.AMOUNT) AS total_distribuido
FROM   AP_INVOICE_DISTRIBUTIONS_ALL aid
JOIN   GL_CODE_COMBINATIONS gcc ON gcc.CODE_COMBINATION_ID = aid.DIST_CODE_COMBINATION_ID
WHERE  aid.ACCOUNTING_DATE BETWEEN :start_date AND :end_date
  AND  aid.ORG_ID = :p_org_id
  AND  aid.CANCELLATION_FLAG IS NULL
GROUP BY gcc.SEGMENT1, gcc.SEGMENT2, gcc.SEGMENT3;
```

### Filtros comuns
- `LINE_TYPE_LOOKUP_CODE = 'ITEM'` — Apenas distribuições de item
- `POSTED_FLAG = 'Y'` — Já contabilizadas no GL
- `MATCH_STATUS_FLAG = 'A'` — Aprovadas pelo matching
- `CANCELLATION_FLAG IS NULL` — Exclui canceladas

---

## 🔒 Observações

- O campo `LINE_TYPE_LOOKUP_CODE` classifica a distribuição: **ITEM** (valor do item), **TAX** (imposto), **FREIGHT** (frete), **MISCELLANEOUS** (diversos), **AWT** (withholding tax automático).
- Cada distribuição aponta para uma combinação de contas (`DIST_CODE_COMBINATION_ID`) que define onde o valor será debitado no GL.
- Distribuições vinculadas a PO (`PO_DISTRIBUTION_ID`) participam do processo de **matching** (2-way ou 3-way).
- O campo `REVERSAL_FLAG = 'Y'` indica uma distribuição de reversão, com `PARENT_REVERSAL_ID` apontando para a distribuição original.
- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.

---

## 🔗 PVOs Relacionados

### [[assetinvoicepvo|AssetInvoicePVO]] (OTHER · BICC: 2/176)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_DATE | InvDistAccountingDate | — |
| ACCOUNTING_EVENT_ID | InvDistAccountingEventId | — |
| ADJUSTMENT_REASON | InvDistAdjustmentReason | — |
| AMOUNT | InvDistAmount | — |
| AMOUNT_AT_PREPAY_PAY_XRATE | InvDistAmountAtPrepayPayXrate | — |
| AMOUNT_AT_PREPAY_XRATE | InvDistAmountAtPrepayXrate | — |
| AMOUNT_VARIANCE | InvDistAmountVariance | — |
| ASSET_BOOK_TYPE_CODE | InvDistAssetBookTypeCode | — |
| ASSET_CATEGORY_ID | InvDistAssetCategoryId | — |
| ASSETS_ADDITION_FLAG | InvDistAssetsAdditionFlag | — |
| ASSETS_TRACKING_FLAG | InvDistAssetsTrackingFlag | — |
| AWARD_ID | InvDistAwardId | — |
| AWT_FLAG | InvDistAwtFlag | — |
| AWT_GROSS_AMOUNT | InvDistAwtGrossAmount | — |
| AWT_GROUP_ID | InvDistAwtGroupId | — |
| AWT_INVOICE_ID | InvDistAwtInvoiceId | — |
| AWT_INVOICE_PAYMENT_ID | InvDistAwtInvoicePaymentId | — |
| AWT_ORIGIN_GROUP_ID | InvDistAwtOriginGroupId | — |
| AWT_RELATED_ID | InvDistAwtRelatedId | — |
| AWT_TAX_RATE_ID | InvDistAwtTaxRateId | — |
| BASE_AMOUNT | InvDistBaseAmount | — |
| BASE_AMOUNT_VARIANCE | InvDistBaseAmountVariance | — |
| BASE_QUANTITY_VARIANCE | InvDistBaseQuantityVariance | — |
| BATCH_ID | InvDistBatchId | — |
| BC_EVENT_ID | InvDistBcEventId | — |
| CANCELLATION_FLAG | InvDistCancellationFlag | — |
| CASH_BASIS_FINAL_APP_ROUNDING | InvDistCashBasisFinalAppRounding | — |
| CC_REVERSAL_FLAG | InvDistCcReversalFlag | — |
| CHARGE_APPLICABLE_TO_DIST_ID | InvDistChargeApplicableToDistId | — |
| COMPANY_PREPAID_INVOICE_ID | InvDistCompanyPrepaidInvoiceId | — |
| CORRECTED_INVOICE_DIST_ID | InvDistCorrectedInvoiceDistId | — |
| CORRECTED_QUANTITY | InvDistCorrectedQuantity | — |
| COUNTRY_OF_SUPPLY | InvDistCountryOfSupply | — |
| CREATED_BY | InvDistCreatedBy | — |
| CREATION_DATE | InvDistCreationDate | — |
| CREDIT_CARD_TRX_ID | InvDistCreditCardTrxId | — |
| DAILY_AMOUNT | InvDistDailyAmount | — |
| DESCRIPTION | InvDistDescription | — |
| DETAIL_TAX_DIST_ID | InvDistDetailTaxDistId | — |
| DIST_CODE_COMBINATION_ID | InvDistDistCodeCombinationId | — |
| DIST_MATCH_TYPE | InvDistDistMatchType | — |
| DISTRIBUTION_CLASS | InvDistDistributionClass | — |
| DISTRIBUTION_LINE_NUMBER | InvDistDistributionLineNumber | ✅ |
| ENCUMBERED_FLAG | InvDistEncumberedFlag | — |
| END_EXPENSE_DATE | InvDistEndExpenseDate | — |
| EXCHANGE_DATE | InvDistExchangeDate | — |
| EXCHANGE_RATE | InvDistExchangeRate | — |
| EXCHANGE_RATE_TYPE | InvDistExchangeRateType | — |
| EXPENDITURE_ITEM_DATE | InvDistExpenditureItemDate | — |
| EXPENDITURE_ORGANIZATION_ID | InvDistExpenditureOrganizationId | — |
| EXPENDITURE_TYPE | InvDistExpenditureType | — |
| EXPENSE_GROUP | InvDistExpenseGroup | — |
| EXTRA_PO_ERV | InvDistExtraPoErv | — |
| FINAL_APPLICATION_ROUNDING | InvDistFinalApplicationRounding | — |
| FINAL_MATCH_FLAG | InvDistFinalMatchFlag | — |
| FINAL_PAYMENT_ROUNDING | InvDistFinalPaymentRounding | — |
| FINAL_RELEASE_ROUNDING | InvDistFinalReleaseRounding | — |
| FULLY_PAID_ACCTD_FLAG | InvDistFullyPaidAcctdFlag | — |
| GMS_BURDENABLE_RAW_COST | InvDistGmsBurdenableRawCost | — |
| HISTORICAL_FLAG | InvDistHistoricalFlag | — |
| INCOME_TAX_REGION | InvDistIncomeTaxRegion | — |
| INTENDED_USE | InvDistIntendedUse | — |
| INVENTORY_TRANSFER_STATUS | InvDistInventoryTransferStatus | — |
| INVOICE_DISTRIBUTION_ID | InvDistInvoiceDistributionId | — |
| INVOICE_ID | InvDistInvoiceId | — |
| INVOICE_INCLUDES_PREPAY_FLAG | InvDistInvoiceIncludesPrepayFlag | — |
| INVOICE_LINE_NUMBER | InvDistInvoiceLineNumber | — |
| JUSTIFICATION | InvDistJustification | — |
| LAST_UPDATE_DATE | InvDistLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvDistLastUpdateLogin | — |
| LAST_UPDATED_BY | InvDistLastUpdatedBy | — |
| LINE_TYPE_LOOKUP_CODE | InvDistLineTypeLookupCode | — |
| MATCH_STATUS_FLAG | InvDistMatchStatusFlag | — |
| MATCHED_UOM_LOOKUP_CODE | InvDistMatchedUomLookupCode | — |
| MERCHANT_DOCUMENT_NUMBER | InvDistMerchantDocumentNumber | — |
| MERCHANT_NAME | InvDistMerchantName | — |
| MERCHANT_REFERENCE | InvDistMerchantReference | — |
| MERCHANT_TAX_REG_NUMBER | InvDistMerchantTaxRegNumber | — |
| MERCHANT_TAXPAYER_ID | InvDistMerchantTaxpayerId | — |
| OBJECT_VERSION_NUMBER | InvDistObjectVersionNumber | — |
| OLD_DIST_LINE_NUMBER | InvDistOldDistLineNumber | — |
| OLD_DISTRIBUTION_ID | InvDistOldDistributionId | — |
| ORG_ID | InvDistOrgId | — |
| PA_ADDITION_FLAG | InvDistPaAdditionFlag | — |
| PA_CMT_XFACE_FLAG | InvDistPaCmtXfaceFlag | — |
| PA_QUANTITY | InvDistPaQuantity | — |
| PARENT_INVOICE_ID | InvDistParentInvoiceId | — |
| PARENT_REVERSAL_ID | InvDistParentReversalId | — |
| PERIOD_NAME | InvDistPeriodName | — |
| PJC_BILLABLE_FLAG | InvDistPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | InvDistPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | InvDistPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | InvDistPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | InvDistPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | InvDistPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | InvDistPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | InvDistPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | InvDistPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | InvDistPJC_PROJECT_ID | — |
| PJC_RESERVED_ATTRIBUTE1 | InvDistPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_RESERVED_ATTRIBUTE10 | InvDistPJC_RESERVED_ATTRIBUTE10 | — |
| PJC_RESERVED_ATTRIBUTE2 | InvDistPJC_RESERVED_ATTRIBUTE2 | — |
| PJC_RESERVED_ATTRIBUTE3 | InvDistPJC_RESERVED_ATTRIBUTE3 | — |
| PJC_RESERVED_ATTRIBUTE4 | InvDistPJC_RESERVED_ATTRIBUTE4 | — |
| PJC_RESERVED_ATTRIBUTE5 | InvDistPJC_RESERVED_ATTRIBUTE5 | — |
| PJC_RESERVED_ATTRIBUTE6 | InvDistPJC_RESERVED_ATTRIBUTE6 | — |
| PJC_RESERVED_ATTRIBUTE7 | InvDistPJC_RESERVED_ATTRIBUTE7 | — |
| PJC_RESERVED_ATTRIBUTE8 | InvDistPJC_RESERVED_ATTRIBUTE8 | — |
| PJC_RESERVED_ATTRIBUTE9 | InvDistPJC_RESERVED_ATTRIBUTE9 | — |
| PJC_TASK_ID | InvDistPJC_TASK_ID | — |
| PJC_USER_DEF_ATTRIBUTE1 | InvDistPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | InvDistPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | InvDistPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | InvDistPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | InvDistPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | InvDistPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | InvDistPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | InvDistPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | InvDistPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | InvDistPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | InvDistPJC_WORK_TYPE_ID | — |
| PO_DISTRIBUTION_ID | InvDistPoDistributionId | — |
| POSTED_FLAG | InvDistPostedFlag | — |
| PREPAY_AMOUNT_REMAINING | InvDistPrepayAmountRemaining | — |
| PREPAY_DISTRIBUTION_ID | InvDistPrepayDistributionId | — |
| PREPAY_TAX_DIFF_AMOUNT | InvDistPrepayTaxDiffAmount | — |
| PROGRAM_APPLICATION_ID | InvDistProgramApplicationId | — |
| PROGRAM_ID | InvDistProgramId | — |
| PROGRAM_UPDATE_DATE | InvDistProgramUpdateDate | — |
| PROJECT_ID | InvDistProjectId | — |
| QUANTITY_INVOICED | InvDistQuantityInvoiced | — |
| QUANTITY_VARIANCE | InvDistQuantityVariance | — |
| RCV_CHARGE_ADDITION_FLAG | InvDistRcvChargeAdditionFlag | — |
| RCV_TRANSACTION_ID | InvDistRcvTransactionId | — |
| REC_NREC_RATE | InvDistRecNrecRate | — |
| RECEIPT_CONVERSION_RATE | InvDistReceiptConversionRate | — |
| RECEIPT_CURRENCY_AMOUNT | InvDistReceiptCurrencyAmount | — |
| RECEIPT_CURRENCY_CODE | InvDistReceiptCurrencyCode | — |
| RECEIPT_MISSING_FLAG | InvDistReceiptMissingFlag | — |
| RECEIPT_REQUIRED_FLAG | InvDistReceiptRequiredFlag | — |
| RECEIPT_VERIFIED_FLAG | InvDistReceiptVerifiedFlag | — |
| RECOVERY_RATE_CODE | InvDistRecoveryRateCode | — |
| RECOVERY_RATE_ID | InvDistRecoveryRateId | — |
| RECOVERY_RATE_NAME | InvDistRecoveryRateName | — |
| RECOVERY_TYPE_CODE | InvDistRecoveryTypeCode | — |
| RECURRING_PAYMENT_ID | InvDistRecurringPaymentId | — |
| REFERENCE_1 | InvDistReference1 | — |
| REFERENCE_2 | InvDistReference2 | — |
| RELATED_ID | InvDistRelatedId | — |
| RELATED_RETAINAGE_DIST_ID | InvDistRelatedRetainageDistId | — |
| RELEASE_INV_DIST_DERIVED_FROM | InvDistReleaseInvDistDerivedFrom | — |
| REQUEST_ID | InvDistRequestId | — |
| RETAINED_AMOUNT_REMAINING | InvDistRetainedAmountRemaining | — |
| RETAINED_INVOICE_DIST_ID | InvDistRetainedInvoiceDistId | — |
| REVERSAL_FLAG | InvDistReversalFlag | — |
| ROOT_DISTRIBUTION_ID | InvDistRootDistributionId | — |
| ROUNDING_AMT | InvDistRoundingAmt | — |
| SET_OF_BOOKS_ID | InvDistSetOfBooksId | — |
| START_EXPENSE_DATE | InvDistStartExpenseDate | — |
| STAT_AMOUNT | InvDistStatAmount | — |
| SUMMARY_TAX_LINE_ID | InvDistSummaryTaxLineId | — |
| TASK_ID | InvDistTaskId | — |
| TAX_ALREADY_DISTRIBUTED_FLAG | InvDistTaxAlreadyDistributedFlag | — |
| TAX_CODE_ID | InvDistTaxCodeId | — |
| TAX_RECOVERABLE_FLAG | InvDistTaxRecoverableFlag | — |
| TAXABLE_AMOUNT | InvDistTaxableAmount | — |
| TAXABLE_BASE_AMOUNT | InvDistTaxableBaseAmount | — |
| TOTAL_DIST_AMOUNT | InvDistTotalDistAmount | — |
| TOTAL_DIST_BASE_AMOUNT | InvDistTotalDistBaseAmount | — |
| TYPE_1099 | InvDistType1099 | — |
| UNIT_PRICE | InvDistUnitPrice | — |
| UPGRADE_BASE_POSTED_AMT | InvDistUpgradeBasePostedAmt | — |
| UPGRADE_POSTED_AMT | InvDistUpgradePostedAmt | — |
| WEB_PARAMETER_ID | InvDistWebParameterId | — |
| WITHHOLDING_TAX_CODE_ID | InvDistWithholdingTaxCodeId | — |
| XINV_PARENT_REVERSAL_ID | InvDistXinvParentReversalId | — |

### [[costaccountingtransactionspvo|CostAccountingTransactionsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | InvoiceDistributionPEOAmount | — |
| INVOICE_DISTRIBUTION_ID | InvoiceDistributionPEOInvoiceDistributionId | — |
| INVOICE_ID | InvoiceDistributionPEOInvoiceId | — |
| INVOICE_LINE_NUMBER | InvoiceDistributionPEOInvoiceLineNumber | — |
| LINE_TYPE_LOOKUP_CODE | InvoiceDistributionPEOLineTypeLookupCode | — |
| OBJECT_VERSION_NUMBER | InvoiceDistributionPEOObjectVersionNumber | — |

### [[costaccountingtransactionsrefpvo|CostAccountingTransactionsRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | InvoiceDistributionPEOAmount | — |
| INVOICE_DISTRIBUTION_ID | InvoiceDistributionPEOInvoiceDistributionId | — |
| INVOICE_ID | InvoiceDistributionPEOInvoiceId | — |
| INVOICE_LINE_NUMBER | InvoiceDistributionPEOInvoiceLineNumber | — |
| LINE_TYPE_LOOKUP_CODE | InvoiceDistributionPEOLineTypeLookupCode | — |
| OBJECT_VERSION_NUMBER | InvoiceDistributionPEOObjectVersionNumber | — |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 7/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISTRIBUTION_LINE_NUMBER | InvoiceDistributionDistributionLineNumber | ✅ |
| INVOICE_DISTRIBUTION_ID | AwtRelDistInvoiceDistributionId | — |
| INVOICE_DISTRIBUTION_ID | InvDistsInvoiceDistributionId | — |
| INVOICE_DISTRIBUTION_ID | InvoiceDistributionInvoiceDistributionId | — |
| LAST_UPDATE_DATE | AwtRelDistLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | InvDistsLastUpdateDate | ✅ |
| PJC_EXPENDITURE_TYPE_ID | InvDistsPJC_EXPENDITURE_TYPE_ID | ✅ |
| PJC_ORGANIZATION_ID | InvDistsPJC_ORGANIZATION_ID | ✅ |
| PJC_PROJECT_ID | InvDistsPJC_PROJECT_ID | ✅ |
| PJC_TASK_ID | InvDistsPJC_TASK_ID | ✅ |

### [[prepaymentappliationdistributionpvo|PrepaymentAppliationDistributionPVO]] (AP · BICC: 13/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_DATE | InvoiceDistributionAccountingDate | ✅ |
| ACCOUNTING_DATE | InvoiceDistributionPrepayDistAccountingDate | ✅ |
| DIST_CODE_COMBINATION_ID | InvoiceDistributionDistCodeCombinationId | — |
| DISTRIBUTION_LINE_NUMBER | InvoiceDistributionDistributionLineNumber | ✅ |
| DISTRIBUTION_LINE_NUMBER | InvoiceDistributionPrepayDistDistributionLineNumber | ✅ |
| DISTRIBUTION_LINE_NUMBER | PrepayAwtRelDistDistributionLineNumber | ✅ |
| INVOICE_DISTRIBUTION_ID | AwtRelDistInvoiceDistributionId | — |
| INVOICE_DISTRIBUTION_ID | InvParenRevIdInvoiceDistributionId | — |
| INVOICE_DISTRIBUTION_ID | InvoiceDistributionInvoiceDistributionId | ✅ |
| INVOICE_DISTRIBUTION_ID | InvoiceDistributionPrepayDistInvoiceDistributionId | — |
| INVOICE_DISTRIBUTION_ID | InvoiceDistributionPrepaymentInvoiceDistributionId | — |
| INVOICE_DISTRIBUTION_ID | PrepayAwtRelDistInvoiceDistributionId | — |
| INVOICE_DISTRIBUTION_ID | RelDistInvoiceDistributionId | — |
| INVOICE_ID | InvoiceDistributionInvoiceId | — |
| INVOICE_ID | InvoiceDistributionPrepaymentInvoiceId | — |
| INVOICE_LINE_NUMBER | InvoiceDistributionInvoiceLineNumber | — |
| INVOICE_LINE_NUMBER | InvoiceDistributionPrepayDistInvoiceLineNumber | ✅ |
| LAST_UPDATE_DATE | AwtRelDistLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | InvParenRevIdLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | InvoiceDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RelDistLastUpdateDate | ✅ |
| POSTED_FLAG | InvoiceDistributionPostedFlag | ✅ |
| POSTED_FLAG | InvoiceDistributionPrepayDistPostedFlag | ✅ |
| PREPAY_DISTRIBUTION_ID | InvoiceDistributionPrepayDistributionId | — |

### [[receiptaccountingtxnp1|ReceiptAccountingTxnP1]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_DATE | ApInvoiceDistributionsAllAccountingDate1 | — |
| ACCOUNTING_EVENT_ID | ApInvoiceDistributionsAllAccountingEventId4 | — |
| ADJUSTMENT_REASON | ApInvoiceDistributionsAllAdjustmentReason1 | — |
| AMOUNT | ApInvoiceDistributionsAllAmount5 | — |
| AMOUNT_AT_PREPAY_PAY_XRATE | ApInvoiceDistributionsAllAmountAtPrepayPayXrate | — |
| AMOUNT_AT_PREPAY_XRATE | ApInvoiceDistributionsAllAmountAtPrepayXrate | — |
| AMOUNT_VARIANCE | ApInvoiceDistributionsAllAmountVariance | — |
| ASSET_BOOK_TYPE_CODE | ApInvoiceDistributionsAllAssetBookTypeCode1 | — |
| ASSET_CATEGORY_ID | ApInvoiceDistributionsAllAssetCategoryId1 | — |
| ASSETS_ADDITION_FLAG | ApInvoiceDistributionsAllAssetsAdditionFlag | — |
| ASSETS_TRACKING_FLAG | ApInvoiceDistributionsAllAssetsTrackingFlag1 | — |
| ATTRIBUTE1 | ApInvoiceDistributionsAllAttribute130 | — |
| ATTRIBUTE10 | ApInvoiceDistributionsAllAttribute109 | — |
| ATTRIBUTE11 | ApInvoiceDistributionsAllAttribute1113 | — |
| ATTRIBUTE12 | ApInvoiceDistributionsAllAttribute1211 | — |
| ATTRIBUTE13 | ApInvoiceDistributionsAllAttribute139 | — |
| ATTRIBUTE14 | ApInvoiceDistributionsAllAttribute149 | — |
| ATTRIBUTE15 | ApInvoiceDistributionsAllAttribute159 | — |
| ATTRIBUTE2 | ApInvoiceDistributionsAllAttribute29 | — |
| ATTRIBUTE3 | ApInvoiceDistributionsAllAttribute39 | — |
| ATTRIBUTE4 | ApInvoiceDistributionsAllAttribute49 | — |
| ATTRIBUTE5 | ApInvoiceDistributionsAllAttribute59 | — |
| ATTRIBUTE6 | ApInvoiceDistributionsAllAttribute69 | — |
| ATTRIBUTE7 | ApInvoiceDistributionsAllAttribute79 | — |
| ATTRIBUTE8 | ApInvoiceDistributionsAllAttribute89 | — |
| ATTRIBUTE9 | ApInvoiceDistributionsAllAttribute99 | — |
| ATTRIBUTE_CATEGORY | ApInvoiceDistributionsAllAttributeCategory9 | — |
| ATTRIBUTE_DATE1 | ApInvoiceDistributionsAllAttributeDate19 | — |
| ATTRIBUTE_DATE2 | ApInvoiceDistributionsAllAttributeDate29 | — |
| ATTRIBUTE_DATE3 | ApInvoiceDistributionsAllAttributeDate39 | — |
| ATTRIBUTE_DATE4 | ApInvoiceDistributionsAllAttributeDate49 | — |
| ATTRIBUTE_DATE5 | ApInvoiceDistributionsAllAttributeDate59 | — |
| ATTRIBUTE_NUMBER1 | ApInvoiceDistributionsAllAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | ApInvoiceDistributionsAllAttributeNumber29 | — |
| ATTRIBUTE_NUMBER3 | ApInvoiceDistributionsAllAttributeNumber39 | — |
| ATTRIBUTE_NUMBER4 | ApInvoiceDistributionsAllAttributeNumber49 | — |
| ATTRIBUTE_NUMBER5 | ApInvoiceDistributionsAllAttributeNumber59 | — |
| AWARD_ID | ApInvoiceDistributionsAllAwardId3 | — |
| AWT_FLAG | ApInvoiceDistributionsAllAwtFlag1 | — |
| AWT_GROSS_AMOUNT | ApInvoiceDistributionsAllAwtGrossAmount | — |
| AWT_GROUP_ID | ApInvoiceDistributionsAllAwtGroupId2 | — |
| AWT_INVOICE_ID | ApInvoiceDistributionsAllAwtInvoiceId | — |
| AWT_INVOICE_PAYMENT_ID | ApInvoiceDistributionsAllAwtInvoicePaymentId | — |
| AWT_ORIGIN_GROUP_ID | ApInvoiceDistributionsAllAwtOriginGroupId | — |
| AWT_RELATED_ID | ApInvoiceDistributionsAllAwtRelatedId | — |
| AWT_TAX_RATE_ID | ApInvoiceDistributionsAllAwtTaxRateId | — |
| BASE_AMOUNT | ApInvoiceDistributionsAllBaseAmount2 | — |
| BASE_AMOUNT_VARIANCE | ApInvoiceDistributionsAllBaseAmountVariance | — |
| BASE_QUANTITY_VARIANCE | ApInvoiceDistributionsAllBaseQuantityVariance | — |
| BATCH_ID | ApInvoiceDistributionsAllBatchId1 | — |
| BC_EVENT_ID | ApInvoiceDistributionsAllBcEventId | — |
| BUDGET_DATE | ApInvoiceDistributionsAllBudgetDate3 | — |
| CANCELLATION_FLAG | ApInvoiceDistributionsAllCancellationFlag | — |
| CASH_BASIS_FINAL_APP_ROUNDING | ApInvoiceDistributionsAllCashBasisFinalAppRounding | — |
| CC_REVERSAL_FLAG | ApInvoiceDistributionsAllCcReversalFlag1 | — |
| CHARGE_APPLICABLE_TO_DIST_ID | ApInvoiceDistributionsAllChargeApplicableToDistId | — |
| COMPANY_PREPAID_INVOICE_ID | ApInvoiceDistributionsAllCompanyPrepaidInvoiceId1 | — |
| CONSUMPTION_ADVICE_HEADER_ID | ApInvoiceDistributionsAllConsumptionAdviceHeaderId2 | — |
| CONSUMPTION_ADVICE_LINE_ID | ApInvoiceDistributionsAllConsumptionAdviceLineId2 | — |
| CORRECTED_INVOICE_DIST_ID | ApInvoiceDistributionsAllCorrectedInvoiceDistId1 | — |
| CORRECTED_QUANTITY | ApInvoiceDistributionsAllCorrectedQuantity | — |
| COUNTRY_OF_SUPPLY | ApInvoiceDistributionsAllCountryOfSupply1 | — |
| CREATED_BY | ApInvoiceDistributionsAllCreatedBy12 | — |
| CREATION_DATE | ApInvoiceDistributionsAllCreationDate12 | — |
| CREDIT_CARD_TRX_ID | ApInvoiceDistributionsAllCreditCardTrxId1 | — |
| DAILY_AMOUNT | ApInvoiceDistributionsAllDailyAmount1 | — |
| DATA_SET_ID | ApInvoiceDistributionsAllDataSetId1 | — |
| DESCRIPTION | ApInvoiceDistributionsAllDescription3 | — |
| DETAIL_TAX_DIST_ID | ApInvoiceDistributionsAllDetailTaxDistId | — |
| DIST_CODE_COMBINATION_ID | ApInvoiceDistributionsAllDistCodeCombinationId | — |
| DIST_MATCH_TYPE | ApInvoiceDistributionsAllDistMatchType | — |
| DISTRIBUTION_CLASS | ApInvoiceDistributionsAllDistributionClass | — |
| DISTRIBUTION_LINE_NUMBER | ApInvoiceDistributionsAllDistributionLineNumber | — |
| ENCUMBERED_FLAG | ApInvoiceDistributionsAllEncumberedFlag2 | — |
| END_EXPENSE_DATE | ApInvoiceDistributionsAllEndExpenseDate1 | — |
| EXCHANGE_DATE | ApInvoiceDistributionsAllExchangeDate2 | — |
| EXCHANGE_RATE | ApInvoiceDistributionsAllExchangeRate2 | — |
| EXCHANGE_RATE_TYPE | ApInvoiceDistributionsAllExchangeRateType2 | — |
| EXPENDITURE_ITEM_DATE | ApInvoiceDistributionsAllExpenditureItemDate2 | — |
| EXPENDITURE_ORGANIZATION_ID | ApInvoiceDistributionsAllExpenditureOrganizationId2 | — |
| EXPENDITURE_TYPE | ApInvoiceDistributionsAllExpenditureType2 | — |
| EXPENSE_GROUP | ApInvoiceDistributionsAllExpenseGroup1 | — |
| EXTRA_PO_ERV | ApInvoiceDistributionsAllExtraPoErv | — |
| FINAL_APPLICATION_ROUNDING | ApInvoiceDistributionsAllFinalApplicationRounding | — |
| FINAL_MATCH_FLAG | ApInvoiceDistributionsAllFinalMatchFlag3 | — |
| FINAL_PAYMENT_ROUNDING | ApInvoiceDistributionsAllFinalPaymentRounding | — |
| FINAL_RELEASE_ROUNDING | ApInvoiceDistributionsAllFinalReleaseRounding | — |
| FULLY_PAID_ACCTD_FLAG | ApInvoiceDistributionsAllFullyPaidAcctdFlag | — |
| FUNDS_STATUS | ApInvoiceDistributionsAllFundsStatus6 | — |
| GLOBAL_ATTRIBUTE1 | ApInvoiceDistributionsAllGlobalAttribute118 | — |
| GLOBAL_ATTRIBUTE10 | ApInvoiceDistributionsAllGlobalAttribute105 | — |
| GLOBAL_ATTRIBUTE11 | ApInvoiceDistributionsAllGlobalAttribute119 | — |
| GLOBAL_ATTRIBUTE12 | ApInvoiceDistributionsAllGlobalAttribute125 | — |
| GLOBAL_ATTRIBUTE13 | ApInvoiceDistributionsAllGlobalAttribute135 | — |
| GLOBAL_ATTRIBUTE14 | ApInvoiceDistributionsAllGlobalAttribute145 | — |
| GLOBAL_ATTRIBUTE15 | ApInvoiceDistributionsAllGlobalAttribute155 | — |
| GLOBAL_ATTRIBUTE16 | ApInvoiceDistributionsAllGlobalAttribute165 | — |
| GLOBAL_ATTRIBUTE17 | ApInvoiceDistributionsAllGlobalAttribute175 | — |
| GLOBAL_ATTRIBUTE18 | ApInvoiceDistributionsAllGlobalAttribute185 | — |
| GLOBAL_ATTRIBUTE19 | ApInvoiceDistributionsAllGlobalAttribute195 | — |
| GLOBAL_ATTRIBUTE2 | ApInvoiceDistributionsAllGlobalAttribute25 | — |
| GLOBAL_ATTRIBUTE20 | ApInvoiceDistributionsAllGlobalAttribute205 | — |
| GLOBAL_ATTRIBUTE3 | ApInvoiceDistributionsAllGlobalAttribute35 | — |
| GLOBAL_ATTRIBUTE4 | ApInvoiceDistributionsAllGlobalAttribute45 | — |
| GLOBAL_ATTRIBUTE5 | ApInvoiceDistributionsAllGlobalAttribute55 | — |
| GLOBAL_ATTRIBUTE6 | ApInvoiceDistributionsAllGlobalAttribute65 | — |
| GLOBAL_ATTRIBUTE7 | ApInvoiceDistributionsAllGlobalAttribute75 | — |
| GLOBAL_ATTRIBUTE8 | ApInvoiceDistributionsAllGlobalAttribute85 | — |
| GLOBAL_ATTRIBUTE9 | ApInvoiceDistributionsAllGlobalAttribute95 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ApInvoiceDistributionsAllGlobalAttributeCategory5 | — |
| GLOBAL_ATTRIBUTE_DATE1 | ApInvoiceDistributionsAllGlobalAttributeDate12 | — |
| GLOBAL_ATTRIBUTE_DATE2 | ApInvoiceDistributionsAllGlobalAttributeDate22 | — |
| GLOBAL_ATTRIBUTE_DATE3 | ApInvoiceDistributionsAllGlobalAttributeDate32 | — |
| GLOBAL_ATTRIBUTE_DATE4 | ApInvoiceDistributionsAllGlobalAttributeDate42 | — |
| GLOBAL_ATTRIBUTE_DATE5 | ApInvoiceDistributionsAllGlobalAttributeDate52 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | ApInvoiceDistributionsAllGlobalAttributeNumber12 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | ApInvoiceDistributionsAllGlobalAttributeNumber22 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | ApInvoiceDistributionsAllGlobalAttributeNumber32 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | ApInvoiceDistributionsAllGlobalAttributeNumber42 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | ApInvoiceDistributionsAllGlobalAttributeNumber52 | — |
| GMS_BURDENABLE_RAW_COST | ApInvoiceDistributionsAllGmsBurdenableRawCost | — |
| HISTORICAL_FLAG | ApInvoiceDistributionsAllHistoricalFlag2 | — |
| INCOME_TAX_REGION | ApInvoiceDistributionsAllIncomeTaxRegion1 | — |
| INTENDED_USE | ApInvoiceDistributionsAllIntendedUse1 | — |
| INTENDED_USE_CLASSIF_ID | ApInvoiceDistributionsAllIntendedUseClassifId2 | — |
| INVENTORY_TRANSFER_STATUS | ApInvoiceDistributionsAllInventoryTransferStatus | — |
| INVOICE_DISTRIBUTION_ID | ApInvoiceDistributionsAllInvoiceDistributionId | — |
| INVOICE_ID | ApInvoiceDistributionsAllInvoiceId3 | — |
| INVOICE_INCLUDES_PREPAY_FLAG | ApInvoiceDistributionsAllInvoiceIncludesPrepayFlag1 | — |
| INVOICE_LINE_NUMBER | ApInvoiceDistributionsAllInvoiceLineNumber1 | — |
| JUSTIFICATION | ApInvoiceDistributionsAllJustification1 | — |
| LAST_UPDATE_DATE | ApInvoiceDistributionsAllLastUpdateDate12 | — |
| LAST_UPDATE_LOGIN | ApInvoiceDistributionsAllLastUpdateLogin12 | — |
| LAST_UPDATED_BY | ApInvoiceDistributionsAllLastUpdatedBy12 | — |
| LINE_TYPE_LOOKUP_CODE | ApInvoiceDistributionsAllLineTypeLookupCode1 | — |
| MATCH_STATUS_FLAG | ApInvoiceDistributionsAllMatchStatusFlag | — |
| MATCHED_UOM_LOOKUP_CODE | ApInvoiceDistributionsAllMatchedUomLookupCode | — |
| MERCHANT_DOCUMENT_NUMBER | ApInvoiceDistributionsAllMerchantDocumentNumber1 | — |
| MERCHANT_NAME | ApInvoiceDistributionsAllMerchantName1 | — |
| MERCHANT_REFERENCE | ApInvoiceDistributionsAllMerchantReference1 | — |
| MERCHANT_TAX_REG_NUMBER | ApInvoiceDistributionsAllMerchantTaxRegNumber1 | — |
| MERCHANT_TAXPAYER_ID | ApInvoiceDistributionsAllMerchantTaxpayerId1 | — |
| OBJECT_VERSION_NUMBER | ApInvoiceDistributionsAllObjectVersionNumber9 | — |
| OLD_DIST_LINE_NUMBER | ApInvoiceDistributionsAllOldDistLineNumber | — |
| OLD_DISTRIBUTION_ID | ApInvoiceDistributionsAllOldDistributionId | — |
| ORG_ID | ApInvoiceDistributionsAllOrgId2 | — |
| PA_ADDITION_FLAG | ApInvoiceDistributionsAllPaAdditionFlag1 | — |
| PA_CMT_XFACE_FLAG | ApInvoiceDistributionsAllPaCmtXfaceFlag | — |
| PA_QUANTITY | ApInvoiceDistributionsAllPaQuantity2 | — |
| PARENT_INVOICE_ID | ApInvoiceDistributionsAllParentInvoiceId | — |
| PARENT_REVERSAL_ID | ApInvoiceDistributionsAllParentReversalId | — |
| PERIOD_NAME | ApInvoiceDistributionsAllPeriodName1 | — |
| PJC_BILLABLE_FLAG | ApInvoiceDistributionsAllPJC_BILLABLE_FLAG3 | — |
| PJC_CAPITALIZABLE_FLAG | ApInvoiceDistributionsAllPJC_CAPITALIZABLE_FLAG3 | — |
| PJC_CONTEXT_CATEGORY | ApInvoiceDistributionsAllPJC_CONTEXT_CATEGORY3 | — |
| PJC_CONTRACT_ID | ApInvoiceDistributionsAllPJC_CONTRACT_ID3 | — |
| PJC_CONTRACT_LINE_ID | ApInvoiceDistributionsAllPJC_CONTRACT_LINE_ID3 | — |
| PJC_EXPENDITURE_ITEM_DATE | ApInvoiceDistributionsAllPJC_EXPENDITURE_ITEM_DATE3 | — |
| PJC_EXPENDITURE_TYPE_ID | ApInvoiceDistributionsAllPJC_EXPENDITURE_TYPE_ID3 | — |
| PJC_FUNDING_ALLOCATION_ID | ApInvoiceDistributionsAllPJC_FUNDING_ALLOCATION_ID3 | — |
| PJC_ORGANIZATION_ID | ApInvoiceDistributionsAllPJC_ORGANIZATION_ID3 | — |
| PJC_PROJECT_ID | ApInvoiceDistributionsAllPJC_PROJECT_ID3 | — |
| PJC_RESERVED_ATTRIBUTE1 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE13 | — |
| PJC_RESERVED_ATTRIBUTE10 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE103 | — |
| PJC_RESERVED_ATTRIBUTE2 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE23 | — |
| PJC_RESERVED_ATTRIBUTE3 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE33 | — |
| PJC_RESERVED_ATTRIBUTE4 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE43 | — |
| PJC_RESERVED_ATTRIBUTE5 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE53 | — |
| PJC_RESERVED_ATTRIBUTE6 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE63 | — |
| PJC_RESERVED_ATTRIBUTE7 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE73 | — |
| PJC_RESERVED_ATTRIBUTE8 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE83 | — |
| PJC_RESERVED_ATTRIBUTE9 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE93 | — |
| PJC_TASK_ID | ApInvoiceDistributionsAllPJC_TASK_ID3 | — |
| PJC_USER_DEF_ATTRIBUTE1 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE13 | — |
| PJC_USER_DEF_ATTRIBUTE10 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE103 | — |
| PJC_USER_DEF_ATTRIBUTE2 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE23 | — |
| PJC_USER_DEF_ATTRIBUTE3 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE33 | — |
| PJC_USER_DEF_ATTRIBUTE4 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE43 | — |
| PJC_USER_DEF_ATTRIBUTE5 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE53 | — |
| PJC_USER_DEF_ATTRIBUTE6 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE63 | — |
| PJC_USER_DEF_ATTRIBUTE7 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE73 | — |
| PJC_USER_DEF_ATTRIBUTE8 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE83 | — |
| PJC_USER_DEF_ATTRIBUTE9 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE93 | — |
| PJC_WORK_TYPE_ID | ApInvoiceDistributionsAllPJC_WORK_TYPE_ID3 | — |
| PO_DISTRIBUTION_ID | ApInvoiceDistributionsAllPoDistributionId5 | — |
| POSTED_FLAG | ApInvoiceDistributionsAllPostedFlag2 | — |
| PREPAY_AMOUNT_REMAINING | ApInvoiceDistributionsAllPrepayAmountRemaining | — |
| PREPAY_DISTRIBUTION_ID | ApInvoiceDistributionsAllPrepayDistributionId | — |
| PREPAY_TAX_DIFF_AMOUNT | ApInvoiceDistributionsAllPrepayTaxDiffAmount | — |
| PROGRAM_APPLICATION_ID | ApInvoiceDistributionsAllProgramApplicationId1 | — |
| PROGRAM_ID | ApInvoiceDistributionsAllProgramId1 | — |
| PROGRAM_UPDATE_DATE | ApInvoiceDistributionsAllProgramUpdateDate1 | — |
| PROJECT_ID | ApInvoiceDistributionsAllProjectId3 | — |
| QUANTITY_INVOICED | ApInvoiceDistributionsAllQuantityInvoiced1 | — |
| QUANTITY_VARIANCE | ApInvoiceDistributionsAllQuantityVariance | — |
| RCV_CHARGE_ADDITION_FLAG | ApInvoiceDistributionsAllRcvChargeAdditionFlag | — |
| RCV_TRANSACTION_ID | ApInvoiceDistributionsAllRcvTransactionId2 | — |
| REC_NREC_RATE | ApInvoiceDistributionsAllRecNrecRate | — |
| RECEIPT_CONVERSION_RATE | ApInvoiceDistributionsAllReceiptConversionRate1 | — |
| RECEIPT_CURRENCY_AMOUNT | ApInvoiceDistributionsAllReceiptCurrencyAmount1 | — |
| RECEIPT_CURRENCY_CODE | ApInvoiceDistributionsAllReceiptCurrencyCode1 | — |
| RECEIPT_MISSING_FLAG | ApInvoiceDistributionsAllReceiptMissingFlag1 | — |
| RECEIPT_REQUIRED_FLAG | ApInvoiceDistributionsAllReceiptRequiredFlag2 | — |
| RECEIPT_VERIFIED_FLAG | ApInvoiceDistributionsAllReceiptVerifiedFlag1 | — |
| RECOVERY_RATE_CODE | ApInvoiceDistributionsAllRecoveryRateCode | — |
| RECOVERY_RATE_ID | ApInvoiceDistributionsAllRecoveryRateId | — |
| RECOVERY_RATE_NAME | ApInvoiceDistributionsAllRecoveryRateName | — |
| RECOVERY_TYPE_CODE | ApInvoiceDistributionsAllRecoveryTypeCode | — |
| RECURRING_PAYMENT_ID | ApInvoiceDistributionsAllRecurringPaymentId1 | — |
| REFERENCE_1 | ApInvoiceDistributionsAllReference12 | — |
| REFERENCE_2 | ApInvoiceDistributionsAllReference22 | — |
| RELATED_ID | ApInvoiceDistributionsAllRelatedId | — |
| RELATED_RETAINAGE_DIST_ID | ApInvoiceDistributionsAllRelatedRetainageDistId | — |
| RELEASE_INV_DIST_DERIVED_FROM | ApInvoiceDistributionsAllReleaseInvDistDerivedFrom | — |
| REQUEST_ID | ApInvoiceDistributionsAllRequestId12 | — |
| RETAINED_AMOUNT_REMAINING | ApInvoiceDistributionsAllRetainedAmountRemaining1 | — |
| RETAINED_INVOICE_DIST_ID | ApInvoiceDistributionsAllRetainedInvoiceDistId | — |
| REVERSAL_FLAG | ApInvoiceDistributionsAllReversalFlag | — |
| ROOT_DISTRIBUTION_ID | ApInvoiceDistributionsAllRootDistributionId | — |
| ROUNDING_AMT | ApInvoiceDistributionsAllRoundingAmt1 | — |
| SET_OF_BOOKS_ID | ApInvoiceDistributionsAllSetOfBooksId3 | — |
| START_EXPENSE_DATE | ApInvoiceDistributionsAllStartExpenseDate1 | — |
| STAT_AMOUNT | ApInvoiceDistributionsAllStatAmount1 | — |
| SUMMARY_TAX_LINE_ID | ApInvoiceDistributionsAllSummaryTaxLineId1 | — |
| TASK_ID | ApInvoiceDistributionsAllTaskId3 | — |
| TAX_ALREADY_DISTRIBUTED_FLAG | ApInvoiceDistributionsAllTaxAlreadyDistributedFlag | — |
| TAX_CODE_ID | ApInvoiceDistributionsAllTaxCodeId3 | — |
| TAX_RECOVERABLE_FLAG | ApInvoiceDistributionsAllTaxRecoverableFlag | — |
| TAXABLE_AMOUNT | ApInvoiceDistributionsAllTaxableAmount | — |
| TAXABLE_BASE_AMOUNT | ApInvoiceDistributionsAllTaxableBaseAmount | — |
| TOTAL_DIST_AMOUNT | ApInvoiceDistributionsAllTotalDistAmount | — |
| TOTAL_DIST_BASE_AMOUNT | ApInvoiceDistributionsAllTotalDistBaseAmount | — |
| TYPE_1099 | ApInvoiceDistributionsAllType10992 | — |
| UNIT_PRICE | ApInvoiceDistributionsAllUnitPrice2 | — |
| UPGRADE_BASE_POSTED_AMT | ApInvoiceDistributionsAllUpgradeBasePostedAmt | — |
| UPGRADE_POSTED_AMT | ApInvoiceDistributionsAllUpgradePostedAmt | — |
| WEB_PARAMETER_ID | ApInvoiceDistributionsAllWebParameterId1 | — |
| WITHHOLDING_TAX_CODE_ID | ApInvoiceDistributionsAllWithholdingTaxCodeId | — |
| XINV_PARENT_REVERSAL_ID | ApInvoiceDistributionsAllXinvParentReversalId | — |

### [[receiptaccountingtxnrefpvo|ReceiptAccountingTxnRefPVO]] (AR · BICC: 39/239)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_DATE | ApInvoiceDistributionsAllAccountingDate1 | ✅ |
| ACCOUNTING_EVENT_ID | ApInvoiceDistributionsAllAccountingEventId4 | — |
| ADJUSTMENT_REASON | ApInvoiceDistributionsAllAdjustmentReason1 | ✅ |
| AMOUNT | ApInvoiceDistributionsAllAmount5 | — |
| AMOUNT_AT_PREPAY_PAY_XRATE | ApInvoiceDistributionsAllAmountAtPrepayPayXrate | — |
| AMOUNT_AT_PREPAY_XRATE | ApInvoiceDistributionsAllAmountAtPrepayXrate | — |
| AMOUNT_VARIANCE | ApInvoiceDistributionsAllAmountVariance | — |
| ASSET_BOOK_TYPE_CODE | ApInvoiceDistributionsAllAssetBookTypeCode1 | ✅ |
| ASSET_CATEGORY_ID | ApInvoiceDistributionsAllAssetCategoryId1 | — |
| ASSETS_ADDITION_FLAG | ApInvoiceDistributionsAllAssetsAdditionFlag | ✅ |
| ASSETS_TRACKING_FLAG | ApInvoiceDistributionsAllAssetsTrackingFlag1 | ✅ |
| ATTRIBUTE1 | ApInvoiceDistributionsAllAttribute130 | — |
| ATTRIBUTE10 | ApInvoiceDistributionsAllAttribute109 | — |
| ATTRIBUTE11 | ApInvoiceDistributionsAllAttribute1113 | — |
| ATTRIBUTE12 | ApInvoiceDistributionsAllAttribute1211 | — |
| ATTRIBUTE13 | ApInvoiceDistributionsAllAttribute139 | — |
| ATTRIBUTE14 | ApInvoiceDistributionsAllAttribute149 | — |
| ATTRIBUTE15 | ApInvoiceDistributionsAllAttribute159 | — |
| ATTRIBUTE2 | ApInvoiceDistributionsAllAttribute29 | — |
| ATTRIBUTE3 | ApInvoiceDistributionsAllAttribute39 | — |
| ATTRIBUTE4 | ApInvoiceDistributionsAllAttribute49 | — |
| ATTRIBUTE5 | ApInvoiceDistributionsAllAttribute59 | — |
| ATTRIBUTE6 | ApInvoiceDistributionsAllAttribute69 | — |
| ATTRIBUTE7 | ApInvoiceDistributionsAllAttribute79 | — |
| ATTRIBUTE8 | ApInvoiceDistributionsAllAttribute89 | — |
| ATTRIBUTE9 | ApInvoiceDistributionsAllAttribute99 | — |
| ATTRIBUTE_CATEGORY | ApInvoiceDistributionsAllAttributeCategory9 | — |
| ATTRIBUTE_DATE1 | ApInvoiceDistributionsAllAttributeDate19 | — |
| ATTRIBUTE_DATE2 | ApInvoiceDistributionsAllAttributeDate29 | — |
| ATTRIBUTE_DATE3 | ApInvoiceDistributionsAllAttributeDate39 | — |
| ATTRIBUTE_DATE4 | ApInvoiceDistributionsAllAttributeDate49 | — |
| ATTRIBUTE_DATE5 | ApInvoiceDistributionsAllAttributeDate59 | — |
| ATTRIBUTE_NUMBER1 | ApInvoiceDistributionsAllAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | ApInvoiceDistributionsAllAttributeNumber29 | — |
| ATTRIBUTE_NUMBER3 | ApInvoiceDistributionsAllAttributeNumber39 | — |
| ATTRIBUTE_NUMBER4 | ApInvoiceDistributionsAllAttributeNumber49 | — |
| ATTRIBUTE_NUMBER5 | ApInvoiceDistributionsAllAttributeNumber59 | — |
| AWARD_ID | ApInvoiceDistributionsAllAwardId3 | — |
| AWT_FLAG | ApInvoiceDistributionsAllAwtFlag1 | ✅ |
| AWT_GROSS_AMOUNT | ApInvoiceDistributionsAllAwtGrossAmount | — |
| AWT_GROUP_ID | ApInvoiceDistributionsAllAwtGroupId2 | — |
| AWT_INVOICE_ID | ApInvoiceDistributionsAllAwtInvoiceId | — |
| AWT_INVOICE_PAYMENT_ID | ApInvoiceDistributionsAllAwtInvoicePaymentId | — |
| AWT_ORIGIN_GROUP_ID | ApInvoiceDistributionsAllAwtOriginGroupId | — |
| AWT_RELATED_ID | ApInvoiceDistributionsAllAwtRelatedId | — |
| AWT_TAX_RATE_ID | ApInvoiceDistributionsAllAwtTaxRateId | — |
| BASE_AMOUNT | ApInvoiceDistributionsAllBaseAmount2 | — |
| BASE_AMOUNT_VARIANCE | ApInvoiceDistributionsAllBaseAmountVariance | — |
| BASE_QUANTITY_VARIANCE | ApInvoiceDistributionsAllBaseQuantityVariance | — |
| BATCH_ID | ApInvoiceDistributionsAllBatchId1 | — |
| BC_EVENT_ID | ApInvoiceDistributionsAllBcEventId | — |
| BUDGET_DATE | ApInvoiceDistributionsAllBudgetDate3 | ✅ |
| CANCELLATION_FLAG | ApInvoiceDistributionsAllCancellationFlag | ✅ |
| CASH_BASIS_FINAL_APP_ROUNDING | ApInvoiceDistributionsAllCashBasisFinalAppRounding | — |
| CC_REVERSAL_FLAG | ApInvoiceDistributionsAllCcReversalFlag1 | — |
| CHARGE_APPLICABLE_TO_DIST_ID | ApInvoiceDistributionsAllChargeApplicableToDistId | — |
| COMPANY_PREPAID_INVOICE_ID | ApInvoiceDistributionsAllCompanyPrepaidInvoiceId1 | — |
| CONSUMPTION_ADVICE_HEADER_ID | ApInvoiceDistributionsAllConsumptionAdviceHeaderId2 | — |
| CONSUMPTION_ADVICE_LINE_ID | ApInvoiceDistributionsAllConsumptionAdviceLineId2 | — |
| CORRECTED_INVOICE_DIST_ID | ApInvoiceDistributionsAllCorrectedInvoiceDistId1 | — |
| CORRECTED_QUANTITY | ApInvoiceDistributionsAllCorrectedQuantity | ✅ |
| COUNTRY_OF_SUPPLY | ApInvoiceDistributionsAllCountryOfSupply1 | — |
| CREATED_BY | ApInvoiceDistributionsAllCreatedBy12 | — |
| CREATION_DATE | ApInvoiceDistributionsAllCreationDate12 | — |
| CREDIT_CARD_TRX_ID | ApInvoiceDistributionsAllCreditCardTrxId1 | — |
| DAILY_AMOUNT | ApInvoiceDistributionsAllDailyAmount1 | — |
| DATA_SET_ID | ApInvoiceDistributionsAllDataSetId1 | — |
| DESCRIPTION | ApInvoiceDistributionsAllDescription3 | ✅ |
| DETAIL_TAX_DIST_ID | ApInvoiceDistributionsAllDetailTaxDistId | — |
| DIST_CODE_COMBINATION_ID | ApInvoiceDistributionsAllDistCodeCombinationId | — |
| DIST_MATCH_TYPE | ApInvoiceDistributionsAllDistMatchType | ✅ |
| DISTRIBUTION_CLASS | ApInvoiceDistributionsAllDistributionClass | — |
| DISTRIBUTION_LINE_NUMBER | ApInvoiceDistributionsAllDistributionLineNumber | ✅ |
| ENCUMBERED_FLAG | ApInvoiceDistributionsAllEncumberedFlag2 | — |
| END_EXPENSE_DATE | ApInvoiceDistributionsAllEndExpenseDate1 | — |
| EXCHANGE_DATE | ApInvoiceDistributionsAllExchangeDate2 | ✅ |
| EXCHANGE_RATE | ApInvoiceDistributionsAllExchangeRate2 | ✅ |
| EXCHANGE_RATE_TYPE | ApInvoiceDistributionsAllExchangeRateType2 | ✅ |
| EXPENDITURE_ITEM_DATE | ApInvoiceDistributionsAllExpenditureItemDate2 | — |
| EXPENDITURE_ORGANIZATION_ID | ApInvoiceDistributionsAllExpenditureOrganizationId2 | — |
| EXPENDITURE_TYPE | ApInvoiceDistributionsAllExpenditureType2 | — |
| EXPENSE_GROUP | ApInvoiceDistributionsAllExpenseGroup1 | — |
| EXTRA_PO_ERV | ApInvoiceDistributionsAllExtraPoErv | — |
| FINAL_APPLICATION_ROUNDING | ApInvoiceDistributionsAllFinalApplicationRounding | — |
| FINAL_MATCH_FLAG | ApInvoiceDistributionsAllFinalMatchFlag3 | ✅ |
| FINAL_PAYMENT_ROUNDING | ApInvoiceDistributionsAllFinalPaymentRounding | — |
| FINAL_RELEASE_ROUNDING | ApInvoiceDistributionsAllFinalReleaseRounding | — |
| FULLY_PAID_ACCTD_FLAG | ApInvoiceDistributionsAllFullyPaidAcctdFlag | — |
| FUNDS_STATUS | ApInvoiceDistributionsAllFundsStatus6 | ✅ |
| GLOBAL_ATTRIBUTE1 | ApInvoiceDistributionsAllGlobalAttribute118 | — |
| GLOBAL_ATTRIBUTE10 | ApInvoiceDistributionsAllGlobalAttribute105 | — |
| GLOBAL_ATTRIBUTE11 | ApInvoiceDistributionsAllGlobalAttribute119 | — |
| GLOBAL_ATTRIBUTE12 | ApInvoiceDistributionsAllGlobalAttribute125 | — |
| GLOBAL_ATTRIBUTE13 | ApInvoiceDistributionsAllGlobalAttribute135 | — |
| GLOBAL_ATTRIBUTE14 | ApInvoiceDistributionsAllGlobalAttribute145 | — |
| GLOBAL_ATTRIBUTE15 | ApInvoiceDistributionsAllGlobalAttribute155 | — |
| GLOBAL_ATTRIBUTE16 | ApInvoiceDistributionsAllGlobalAttribute165 | — |
| GLOBAL_ATTRIBUTE17 | ApInvoiceDistributionsAllGlobalAttribute175 | — |
| GLOBAL_ATTRIBUTE18 | ApInvoiceDistributionsAllGlobalAttribute185 | — |
| GLOBAL_ATTRIBUTE19 | ApInvoiceDistributionsAllGlobalAttribute195 | — |
| GLOBAL_ATTRIBUTE2 | ApInvoiceDistributionsAllGlobalAttribute25 | — |
| GLOBAL_ATTRIBUTE20 | ApInvoiceDistributionsAllGlobalAttribute205 | — |
| GLOBAL_ATTRIBUTE3 | ApInvoiceDistributionsAllGlobalAttribute35 | — |
| GLOBAL_ATTRIBUTE4 | ApInvoiceDistributionsAllGlobalAttribute45 | — |
| GLOBAL_ATTRIBUTE5 | ApInvoiceDistributionsAllGlobalAttribute55 | — |
| GLOBAL_ATTRIBUTE6 | ApInvoiceDistributionsAllGlobalAttribute65 | — |
| GLOBAL_ATTRIBUTE7 | ApInvoiceDistributionsAllGlobalAttribute75 | — |
| GLOBAL_ATTRIBUTE8 | ApInvoiceDistributionsAllGlobalAttribute85 | — |
| GLOBAL_ATTRIBUTE9 | ApInvoiceDistributionsAllGlobalAttribute95 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ApInvoiceDistributionsAllGlobalAttributeCategory5 | — |
| GLOBAL_ATTRIBUTE_DATE1 | ApInvoiceDistributionsAllGlobalAttributeDate12 | — |
| GLOBAL_ATTRIBUTE_DATE2 | ApInvoiceDistributionsAllGlobalAttributeDate22 | — |
| GLOBAL_ATTRIBUTE_DATE3 | ApInvoiceDistributionsAllGlobalAttributeDate32 | — |
| GLOBAL_ATTRIBUTE_DATE4 | ApInvoiceDistributionsAllGlobalAttributeDate42 | — |
| GLOBAL_ATTRIBUTE_DATE5 | ApInvoiceDistributionsAllGlobalAttributeDate52 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | ApInvoiceDistributionsAllGlobalAttributeNumber12 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | ApInvoiceDistributionsAllGlobalAttributeNumber22 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | ApInvoiceDistributionsAllGlobalAttributeNumber32 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | ApInvoiceDistributionsAllGlobalAttributeNumber42 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | ApInvoiceDistributionsAllGlobalAttributeNumber52 | — |
| GMS_BURDENABLE_RAW_COST | ApInvoiceDistributionsAllGmsBurdenableRawCost | — |
| HISTORICAL_FLAG | ApInvoiceDistributionsAllHistoricalFlag2 | — |
| INCOME_TAX_REGION | ApInvoiceDistributionsAllIncomeTaxRegion1 | — |
| INTENDED_USE | ApInvoiceDistributionsAllIntendedUse1 | ✅ |
| INTENDED_USE_CLASSIF_ID | ApInvoiceDistributionsAllIntendedUseClassifId2 | — |
| INVENTORY_TRANSFER_STATUS | ApInvoiceDistributionsAllInventoryTransferStatus | ✅ |
| INVOICE_DISTRIBUTION_ID | ApInvoiceDistributionsAllInvoiceDistributionId | ✅ |
| INVOICE_ID | ApInvoiceDistributionsAllInvoiceId3 | — |
| INVOICE_INCLUDES_PREPAY_FLAG | ApInvoiceDistributionsAllInvoiceIncludesPrepayFlag1 | ✅ |
| INVOICE_LINE_NUMBER | ApInvoiceDistributionsAllInvoiceLineNumber1 | ✅ |
| JUSTIFICATION | ApInvoiceDistributionsAllJustification1 | — |
| LAST_UPDATE_DATE | ApInvoiceDistributionsAllLastUpdateDate12 | ✅ |
| LAST_UPDATE_LOGIN | ApInvoiceDistributionsAllLastUpdateLogin12 | — |
| LAST_UPDATED_BY | ApInvoiceDistributionsAllLastUpdatedBy12 | — |
| LINE_TYPE_LOOKUP_CODE | ApInvoiceDistributionsAllLineTypeLookupCode1 | ✅ |
| MATCH_STATUS_FLAG | ApInvoiceDistributionsAllMatchStatusFlag | ✅ |
| MATCHED_UOM_LOOKUP_CODE | ApInvoiceDistributionsAllMatchedUomLookupCode | — |
| MERCHANT_DOCUMENT_NUMBER | ApInvoiceDistributionsAllMerchantDocumentNumber1 | — |
| MERCHANT_NAME | ApInvoiceDistributionsAllMerchantName1 | — |
| MERCHANT_REFERENCE | ApInvoiceDistributionsAllMerchantReference1 | — |
| MERCHANT_TAX_REG_NUMBER | ApInvoiceDistributionsAllMerchantTaxRegNumber1 | — |
| MERCHANT_TAXPAYER_ID | ApInvoiceDistributionsAllMerchantTaxpayerId1 | — |
| OBJECT_VERSION_NUMBER | ApInvoiceDistributionsAllObjectVersionNumber9 | — |
| OLD_DIST_LINE_NUMBER | ApInvoiceDistributionsAllOldDistLineNumber | — |
| OLD_DISTRIBUTION_ID | ApInvoiceDistributionsAllOldDistributionId | — |
| ORG_ID | ApInvoiceDistributionsAllOrgId2 | — |
| PA_ADDITION_FLAG | ApInvoiceDistributionsAllPaAdditionFlag1 | ✅ |
| PA_CMT_XFACE_FLAG | ApInvoiceDistributionsAllPaCmtXfaceFlag | ✅ |
| PA_QUANTITY | ApInvoiceDistributionsAllPaQuantity2 | — |
| PARENT_INVOICE_ID | ApInvoiceDistributionsAllParentInvoiceId | — |
| PARENT_REVERSAL_ID | ApInvoiceDistributionsAllParentReversalId | — |
| PERIOD_NAME | ApInvoiceDistributionsAllPeriodName1 | ✅ |
| PJC_BILLABLE_FLAG | ApInvoiceDistributionsAllPJC_BILLABLE_FLAG3 | — |
| PJC_CAPITALIZABLE_FLAG | ApInvoiceDistributionsAllPJC_CAPITALIZABLE_FLAG3 | — |
| PJC_CONTEXT_CATEGORY | ApInvoiceDistributionsAllPJC_CONTEXT_CATEGORY3 | — |
| PJC_CONTRACT_ID | ApInvoiceDistributionsAllPJC_CONTRACT_ID3 | — |
| PJC_CONTRACT_LINE_ID | ApInvoiceDistributionsAllPJC_CONTRACT_LINE_ID3 | — |
| PJC_EXPENDITURE_ITEM_DATE | ApInvoiceDistributionsAllPJC_EXPENDITURE_ITEM_DATE3 | ✅ |
| PJC_EXPENDITURE_TYPE_ID | ApInvoiceDistributionsAllPJC_EXPENDITURE_TYPE_ID3 | — |
| PJC_FUNDING_ALLOCATION_ID | ApInvoiceDistributionsAllPJC_FUNDING_ALLOCATION_ID3 | — |
| PJC_ORGANIZATION_ID | ApInvoiceDistributionsAllPJC_ORGANIZATION_ID3 | — |
| PJC_PROJECT_ID | ApInvoiceDistributionsAllPJC_PROJECT_ID3 | — |
| PJC_RESERVED_ATTRIBUTE1 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE13 | — |
| PJC_RESERVED_ATTRIBUTE10 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE103 | — |
| PJC_RESERVED_ATTRIBUTE2 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE23 | — |
| PJC_RESERVED_ATTRIBUTE3 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE33 | — |
| PJC_RESERVED_ATTRIBUTE4 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE43 | — |
| PJC_RESERVED_ATTRIBUTE5 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE53 | — |
| PJC_RESERVED_ATTRIBUTE6 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE63 | — |
| PJC_RESERVED_ATTRIBUTE7 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE73 | — |
| PJC_RESERVED_ATTRIBUTE8 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE83 | — |
| PJC_RESERVED_ATTRIBUTE9 | ApInvoiceDistributionsAllPJC_RESERVED_ATTRIBUTE93 | — |
| PJC_TASK_ID | ApInvoiceDistributionsAllPJC_TASK_ID3 | — |
| PJC_USER_DEF_ATTRIBUTE1 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE13 | — |
| PJC_USER_DEF_ATTRIBUTE10 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE103 | — |
| PJC_USER_DEF_ATTRIBUTE2 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE23 | — |
| PJC_USER_DEF_ATTRIBUTE3 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE33 | — |
| PJC_USER_DEF_ATTRIBUTE4 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE43 | — |
| PJC_USER_DEF_ATTRIBUTE5 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE53 | — |
| PJC_USER_DEF_ATTRIBUTE6 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE63 | — |
| PJC_USER_DEF_ATTRIBUTE7 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE73 | — |
| PJC_USER_DEF_ATTRIBUTE8 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE83 | — |
| PJC_USER_DEF_ATTRIBUTE9 | ApInvoiceDistributionsAllPJC_USER_DEF_ATTRIBUTE93 | — |
| PJC_WORK_TYPE_ID | ApInvoiceDistributionsAllPJC_WORK_TYPE_ID3 | — |
| PO_DISTRIBUTION_ID | ApInvoiceDistributionsAllPoDistributionId5 | — |
| POSTED_FLAG | ApInvoiceDistributionsAllPostedFlag2 | ✅ |
| PREPAY_AMOUNT_REMAINING | ApInvoiceDistributionsAllPrepayAmountRemaining | — |
| PREPAY_DISTRIBUTION_ID | ApInvoiceDistributionsAllPrepayDistributionId | — |
| PREPAY_TAX_DIFF_AMOUNT | ApInvoiceDistributionsAllPrepayTaxDiffAmount | — |
| PROGRAM_APPLICATION_ID | ApInvoiceDistributionsAllProgramApplicationId1 | — |
| PROGRAM_ID | ApInvoiceDistributionsAllProgramId1 | — |
| PROGRAM_UPDATE_DATE | ApInvoiceDistributionsAllProgramUpdateDate1 | — |
| PROJECT_ID | ApInvoiceDistributionsAllProjectId3 | — |
| QUANTITY_INVOICED | ApInvoiceDistributionsAllQuantityInvoiced1 | ✅ |
| QUANTITY_VARIANCE | ApInvoiceDistributionsAllQuantityVariance | — |
| RCV_CHARGE_ADDITION_FLAG | ApInvoiceDistributionsAllRcvChargeAdditionFlag | — |
| RCV_TRANSACTION_ID | ApInvoiceDistributionsAllRcvTransactionId2 | — |
| REC_NREC_RATE | ApInvoiceDistributionsAllRecNrecRate | ✅ |
| RECEIPT_CONVERSION_RATE | ApInvoiceDistributionsAllReceiptConversionRate1 | — |
| RECEIPT_CURRENCY_AMOUNT | ApInvoiceDistributionsAllReceiptCurrencyAmount1 | — |
| RECEIPT_CURRENCY_CODE | ApInvoiceDistributionsAllReceiptCurrencyCode1 | — |
| RECEIPT_MISSING_FLAG | ApInvoiceDistributionsAllReceiptMissingFlag1 | — |
| RECEIPT_REQUIRED_FLAG | ApInvoiceDistributionsAllReceiptRequiredFlag2 | — |
| RECEIPT_VERIFIED_FLAG | ApInvoiceDistributionsAllReceiptVerifiedFlag1 | — |
| RECOVERY_RATE_CODE | ApInvoiceDistributionsAllRecoveryRateCode | ✅ |
| RECOVERY_RATE_ID | ApInvoiceDistributionsAllRecoveryRateId | — |
| RECOVERY_RATE_NAME | ApInvoiceDistributionsAllRecoveryRateName | ✅ |
| RECOVERY_TYPE_CODE | ApInvoiceDistributionsAllRecoveryTypeCode | ✅ |
| RECURRING_PAYMENT_ID | ApInvoiceDistributionsAllRecurringPaymentId1 | — |
| REFERENCE_1 | ApInvoiceDistributionsAllReference12 | — |
| REFERENCE_2 | ApInvoiceDistributionsAllReference22 | — |
| RELATED_ID | ApInvoiceDistributionsAllRelatedId | — |
| RELATED_RETAINAGE_DIST_ID | ApInvoiceDistributionsAllRelatedRetainageDistId | — |
| RELEASE_INV_DIST_DERIVED_FROM | ApInvoiceDistributionsAllReleaseInvDistDerivedFrom | — |
| REQUEST_ID | ApInvoiceDistributionsAllRequestId12 | — |
| RETAINED_AMOUNT_REMAINING | ApInvoiceDistributionsAllRetainedAmountRemaining1 | — |
| RETAINED_INVOICE_DIST_ID | ApInvoiceDistributionsAllRetainedInvoiceDistId | — |
| REVERSAL_FLAG | ApInvoiceDistributionsAllReversalFlag | ✅ |
| ROOT_DISTRIBUTION_ID | ApInvoiceDistributionsAllRootDistributionId | — |
| ROUNDING_AMT | ApInvoiceDistributionsAllRoundingAmt1 | — |
| SET_OF_BOOKS_ID | ApInvoiceDistributionsAllSetOfBooksId3 | — |
| START_EXPENSE_DATE | ApInvoiceDistributionsAllStartExpenseDate1 | — |
| STAT_AMOUNT | ApInvoiceDistributionsAllStatAmount1 | — |
| SUMMARY_TAX_LINE_ID | ApInvoiceDistributionsAllSummaryTaxLineId1 | — |
| TASK_ID | ApInvoiceDistributionsAllTaskId3 | — |
| TAX_ALREADY_DISTRIBUTED_FLAG | ApInvoiceDistributionsAllTaxAlreadyDistributedFlag | ✅ |
| TAX_CODE_ID | ApInvoiceDistributionsAllTaxCodeId3 | — |
| TAX_RECOVERABLE_FLAG | ApInvoiceDistributionsAllTaxRecoverableFlag | ✅ |
| TAXABLE_AMOUNT | ApInvoiceDistributionsAllTaxableAmount | — |
| TAXABLE_BASE_AMOUNT | ApInvoiceDistributionsAllTaxableBaseAmount | — |
| TOTAL_DIST_AMOUNT | ApInvoiceDistributionsAllTotalDistAmount | — |
| TOTAL_DIST_BASE_AMOUNT | ApInvoiceDistributionsAllTotalDistBaseAmount | — |
| TYPE_1099 | ApInvoiceDistributionsAllType10992 | — |
| UNIT_PRICE | ApInvoiceDistributionsAllUnitPrice2 | ✅ |
| UPGRADE_BASE_POSTED_AMT | ApInvoiceDistributionsAllUpgradeBasePostedAmt | — |
| UPGRADE_POSTED_AMT | ApInvoiceDistributionsAllUpgradePostedAmt | — |
| WEB_PARAMETER_ID | ApInvoiceDistributionsAllWebParameterId1 | — |
| WITHHOLDING_TAX_CODE_ID | ApInvoiceDistributionsAllWithholdingTaxCodeId | — |
| XINV_PARENT_REVERSAL_ID | ApInvoiceDistributionsAllXinvParentReversalId | — |

---

## 📚 Referências

- [Oracle Docs — AP_INVOICE_DISTRIBUTIONS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/apinvoicedistributionsall-10003.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
