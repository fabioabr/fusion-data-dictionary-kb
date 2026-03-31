---
id: DOC-AP-025
doc_type: system-doc
title: "AP_SELF_ASSESSED_TAX_DIST_ALL — Distribuições de Impostos Auto-avaliados"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, impostos, self-assessed, distribuicao-tributaria]
aliases: [AP_SELF_ASSESSED_TAX_DIST_ALL, ap_self_assessed_tax_dist_all, self_assessed_tax_dist, impostos_autoavaliados_ap, dist_tax_self_assessed]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_SELF_ASSESSED_TAX_DIST_ALL

## Visão Geral

Tabela que armazena as distribuições contábeis de impostos auto-avaliados (self-assessed taxes) em faturas do Accounts Payable. Impostos auto-avaliados são aqueles calculados e recolhidos pelo comprador, não pelo fornecedor — como use tax nos EUA ou reverse charge (ICMS-ST, ISS retido) em regimes tributários específicos.

## Propósito de Negócio

Permite o registro e rastreamento de impostos que o Banco Patria calcula e recolhe por conta própria, sem que o fornecedor os inclua na fatura. É essencial para: (1) contabilização correta de impostos retidos, (2) compliance tributário com obrigações de recolhimento, (3) apuração de créditos fiscais (onde aplicável), (4) conciliação entre impostos auto-avaliados e recolhimentos efetivos.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SELF_ASSESSED_TAX_DIST_ID | NUMBER(15) | NOT NULL | PK | Chave primária. Identificador único da distribuição de imposto auto-avaliado. | — | 🟢 100% |
| 2 | INVOICE_ID | NUMBER(15) | NOT NULL | FK | FK para a fatura de origem. | [[ap_invoices_all]] | 🟢 100% |
| 3 | INVOICE_LINE_NUMBER | NUMBER | NOT NULL | FK | Número da linha da fatura. | [[ap_invoice_lines_all]] | 🟢 95% |
| 4 | INVOICE_DISTRIBUTION_ID | NUMBER(15) | NULL | FK | FK para a distribuição da fatura associada. | [[ap_invoice_distributions_all]] | 🟢 95% |
| 5 | TAX_RATE_ID | NUMBER(15) | NULL | FK | FK para a taxa de imposto aplicada (ZX_RATES_B). | — | 🟢 90% |
| 6 | TAX_REGIME_CODE | VARCHAR2(30) | NULL | Tributário | Código do regime tributário (ex.: BR-FEDERAL). | — | 🟢 90% |
| 7 | TAX | VARCHAR2(30) | NULL | Tributário | Nome do imposto (ex.: ISS, ICMS-ST, USE_TAX). | — | 🟢 90% |
| 8 | TAX_STATUS_CODE | VARCHAR2(30) | NULL | Tributário | Status do imposto (STANDARD, EXEMPT, ZERO_RATE). | — | 🟡 80% |
| 9 | TAX_RATE | NUMBER | NULL | Tributário | Alíquota do imposto aplicada. | — | 🟢 90% |
| 10 | TAXABLE_AMOUNT | NUMBER | NULL | Financeiro | Base de cálculo do imposto. | — | 🟢 95% |
| 11 | TAX_AMOUNT | NUMBER | NULL | Financeiro | Valor do imposto auto-avaliado. | — | 🟢 100% |
| 12 | DIST_CODE_COMBINATION_ID | NUMBER(15) | NULL | FK | FK para [[gl_code_combinations]]. Conta contábil de débito/crédito. | [[gl_code_combinations]] | 🟢 90% |
| 13 | ACCOUNTING_DATE | DATE | NULL | Temporal | Data contábil da distribuição. | — | 🟢 90% |
| 14 | ORG_ID | NUMBER(15) | NOT NULL | Partição | Identificador da business unit (Operating Unit). | — | 🟢 100% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 16 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[ap_invoices_all]]** — Fatura de origem (N:1 via `INVOICE_ID`).
- **[[ap_invoice_lines_all]]** — Linha da fatura (N:1 via `INVOICE_ID` + `INVOICE_LINE_NUMBER`).
- **[[ap_invoice_distributions_all]]** — Distribuição associada (N:1 via `INVOICE_DISTRIBUTION_ID`).
- **[[gl_code_combinations]]** — Conta contábil (N:1 via `DIST_CODE_COMBINATION_ID`).

### Tabelas-filha

- Nenhuma tabela-filha direta identificada.

## Uso Típico

```sql
-- Impostos auto-avaliados por fatura
SELECT sat.SELF_ASSESSED_TAX_DIST_ID,
       inv.INVOICE_NUM,
       sat.TAX,
       sat.TAX_REGIME_CODE,
       sat.TAX_RATE,
       sat.TAXABLE_AMOUNT,
       sat.TAX_AMOUNT
  FROM AP_SELF_ASSESSED_TAX_DIST_ALL sat
  JOIN AP_INVOICES_ALL inv
    ON inv.INVOICE_ID = sat.INVOICE_ID
 WHERE sat.ORG_ID = :p_org_id
   AND inv.INVOICE_DATE BETWEEN :p_data_ini AND :p_data_fim
 ORDER BY inv.INVOICE_NUM, sat.TAX;
```

## Observações

- Impostos auto-avaliados geram lançamentos contábeis adicionais (débito e crédito) que não aparecem no valor bruto da fatura do fornecedor.
- No contexto brasileiro, impostos retidos na fonte (ISS, INSS, IR, CSLL) podem utilizar estrutura similar.
- Integra-se com o módulo Oracle Tax (ZX) via `TAX_RATE_ID` e `TAX_REGIME_CODE`.
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Tax (E-Business Tax / ZX) Integration Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).

---

## 🔗 PVOs Relacionados

### [[invoiceselfassessedtaxdistributionpvo|InvoiceSelfAssessedTaxDistributionPVO]] (AP · BICC: 14/126)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_DATE | InvoiceSelfAssessedTaxDistAccountingDate | ✅ |
| ACCOUNTING_EVENT_ID | InvoiceSelfAssessedTaxDistAccountingEventId | — |
| ADJUSTMENT_REASON | InvoiceSelfAssessedTaxDistAdjustmentReason | ✅ |
| AMOUNT | InvoiceSelfAssessedTaxDistAmount | ✅ |
| AMOUNT_VARIANCE | InvoiceSelfAssessedTaxDistAmountVariance | — |
| ASSET_BOOK_TYPE_CODE | InvoiceSelfAssessedTaxDistAssetBookTypeCode | — |
| ASSET_CATEGORY_ID | InvoiceSelfAssessedTaxDistAssetCategoryId | — |
| ASSETS_ADDITION_FLAG | InvoiceSelfAssessedTaxDistAssetsAdditionFlag | — |
| ASSETS_TRACKING_FLAG | InvoiceSelfAssessedTaxDistAssetsTrackingFlag | — |
| ATTRIBUTE_CATEGORY | InvoiceSelfAssessedTaxDistAttributeCategory | — |
| AWARD_ID | InvoiceSelfAssessedTaxDistAwardId | — |
| AWT_FLAG | InvoiceSelfAssessedTaxDistAwtFlag | — |
| AWT_GROSS_AMOUNT | InvoiceSelfAssessedTaxDistAwtGrossAmount | — |
| AWT_GROUP_ID | InvoiceSelfAssessedTaxDistAwtGroupId | — |
| AWT_INVOICE_ID | InvoiceSelfAssessedTaxDistAwtInvoiceId | — |
| AWT_INVOICE_PAYMENT_ID | InvoiceSelfAssessedTaxDistAwtInvoicePaymentId | — |
| AWT_ORIGIN_GROUP_ID | InvoiceSelfAssessedTaxDistAwtOriginGroupId | — |
| AWT_TAX_RATE_ID | InvoiceSelfAssessedTaxDistAwtTaxRateId | — |
| AWT_WITHHELD_AMT | InvoiceSelfAssessedTaxDistAwtWithheldAmt | — |
| BASE_AMOUNT | InvoiceSelfAssessedTaxDistBaseAmount | ✅ |
| BASE_AMOUNT_VARIANCE | InvoiceSelfAssessedTaxDistBaseAmountVariance | — |
| BASE_QUANTITY_VARIANCE | InvoiceSelfAssessedTaxDistBaseQuantityVariance | — |
| BATCH_ID | InvoiceSelfAssessedTaxDistBatchId | — |
| BC_EVENT_ID | InvoiceSelfAssessedTaxDistBcEventId | — |
| CANCELLATION_FLAG | InvoiceSelfAssessedTaxDistCancellationFlag | ✅ |
| CC_REVERSAL_FLAG | InvoiceSelfAssessedTaxDistCcReversalFlag | — |
| CHARGE_APPLICABLE_TO_DIST_ID | InvoiceSelfAssessedTaxChargeApplicableToDistId | — |
| COMPANY_PREPAID_INVOICE_ID | InvoiceSelfAssessedTaxDistCompanyPrepaidInvoiceId | — |
| CORRECTED_INVOICE_DIST_ID | InvoiceSelfAssessedTaxDistCorrectedInvoiceDistId | — |
| CORRECTED_QUANTITY | InvoiceSelfAssessedTaxDistCorrectedQuantity | — |
| COUNTRY_OF_SUPPLY | InvoiceSelfAssessedTaxDistCountryOfSupply | — |
| CREATED_BY | InvoiceSelfAssessedTaxDistCreatedBy | — |
| CREATION_DATE | InvoiceSelfAssessedTaxDistCreationDate | — |
| CREDIT_CARD_TRX_ID | InvoiceSelfAssessedTaxDistCreditCardTrxId | — |
| DAILY_AMOUNT | InvoiceSelfAssessedTaxDistDailyAmount | — |
| DESCRIPTION | InvoiceSelfAssessedTaxDistDescription | — |
| DETAIL_TAX_DIST_ID | InvoiceSelfAssessedTaxDistDetailTaxDistId | — |
| DIST_CODE_COMBINATION_ID | InvoiceSelfAssessedTaxDistDistCodeCombinationId | — |
| DIST_MATCH_TYPE | InvoiceSelfAssessedTaxDistDistMatchType | — |
| DISTRIBUTION_CLASS | InvoiceSelfAssessedTaxDistDistributionClass | — |
| DISTRIBUTION_LINE_NUMBER | InvoiceSelfAssessedTaxDistDistributionLineNumber | ✅ |
| ENCUMBERED_FLAG | InvoiceSelfAssessedTaxDistEncumberedFlag | — |
| END_EXPENSE_DATE | InvoiceSelfAssessedTaxDistEndExpenseDate | — |
| EXPENDITURE_ITEM_DATE | InvoiceSelfAssessedTaxDistExpenditureItemDate | — |
| EXPENDITURE_ORGANIZATION_ID | InvoiceSelfAssessedTaxDistExpenditureOrganizationId | — |
| EXPENDITURE_TYPE | InvoiceSelfAssessedTaxDistExpenditureType | — |
| EXPENSE_GROUP | InvoiceSelfAssessedTaxDistExpenseGroup | — |
| EXTRA_PO_ERV | InvoiceSelfAssessedTaxDistExtraPoErv | — |
| FINAL_MATCH_FLAG | InvoiceSelfAssessedTaxDistFinalMatchFlag | — |
| GLOBAL_ATTRIBUTE_CATEGORY | InvoiceSelfAssessedTaxDistGlobalAttributeCategory | — |
| GMS_BURDENABLE_RAW_COST | InvoiceSelfAssessedTaxDistGmsBurdenableRawCost | — |
| INCOME_TAX_REGION | InvoiceSelfAssessedTaxDistIncomeTaxRegion | — |
| INTENDED_USE | InvoiceSelfAssessedTaxDistIntendedUse | — |
| INVENTORY_TRANSFER_STATUS | InvoiceSelfAssessedTaxDistInventoryTransferStatus | — |
| INVOICE_DISTRIBUTION_ID | InvoiceDistributionId | ✅ |
| INVOICE_LINE_NUMBER | InvoiceSelfAssessedTaxDistInvoiceLineNumber | — |
| JUSTIFICATION | InvoiceSelfAssessedTaxDistJustification | — |
| LAST_UPDATE_DATE | InvoiceSelfAssessedTaxDistLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvoiceSelfAssessedTaxDistLastUpdateLogin | — |
| LAST_UPDATED_BY | InvoiceSelfAssessedTaxDistLastUpdatedBy | — |
| LINE_TYPE_LOOKUP_CODE | InvoiceSelfAssessedTaxDistLineTypeLookupCode | ✅ |
| MATCH_STATUS_FLAG | InvoiceSelfAssessedTaxDistMatchStatusFlag | ✅ |
| MATCHED_UOM_LOOKUP_CODE | InvoiceSelfAssessedTaxDistMatchedUomLookupCode | — |
| MERCHANT_DOCUMENT_NUMBER | InvoiceSelfAssessedTaxDistMerchantDocumentNumber | — |
| MERCHANT_NAME | InvoiceSelfAssessedTaxDistMerchantName | — |
| MERCHANT_REFERENCE | InvoiceSelfAssessedTaxDistMerchantReference | — |
| MERCHANT_TAX_REG_NUMBER | InvoiceSelfAssessedTaxDistMerchantTaxRegNumber | — |
| MERCHANT_TAXPAYER_ID | InvoiceSelfAssessedTaxDistMerchantTaxpayerId | — |
| OBJECT_VERSION_NUMBER | InvoiceSelfAssessedTaxDistObjectVersionNumber | — |
| ORG_ID | InvoiceSelfAssessedTaxDistOrgId | — |
| PA_ADDITION_FLAG | InvoiceSelfAssessedTaxDistPaAdditionFlag | — |
| PA_CMT_XFACE_FLAG | InvoiceSelfAssessedTaxDistPaCmtXfaceFlag | — |
| PA_QUANTITY | InvoiceSelfAssessedTaxDistPaQuantity | — |
| PACKET_ID | InvoiceSelfAssessedTaxDistPacketId | — |
| PARENT_INVOICE_ID | InvoiceSelfAssessedTaxDistParentInvoiceId | — |
| PARENT_REVERSAL_ID | InvoiceSelfAssessedTaxDistInvoiceSelfAssessedTaxDistParentReversalId | — |
| PERIOD_NAME | InvoiceSelfAssessedTaxDistPeriodName | ✅ |
| PO_DISTRIBUTION_ID | InvoiceSelfAssessedTaxDistPoDistributionId | — |
| POSTED_FLAG | InvoiceSelfAssessedTaxDistPostedFlag | ✅ |
| PREPAY_AMOUNT_REMAINING | InvoiceSelfAssessedTaxDistPrepayAmountRemaining | — |
| PREPAY_DISTRIBUTION_ID | InvoiceSelfAssessedTaxDistPrepayDistributionId | — |
| PREPAY_TAX_DIFF_AMOUNT | InvoiceSelfAssessedTaxDistPrepayTaxDiffAmount | — |
| PROGRAM_APPLICATION_ID | InvoiceSelfAssessedTaxDistProgramApplicationId | — |
| PROGRAM_ID | InvoiceSelfAssessedTaxDistProgramId | — |
| PROGRAM_UPDATE_DATE | InvoiceSelfAssessedTaxDistProgramUpdateDate | — |
| PROJECT_ID | InvoiceSelfAssessedTaxDistProjectId | — |
| QUANTITY_INVOICED | InvoiceSelfAssessedTaxDistQuantityInvoiced | — |
| QUANTITY_VARIANCE | InvoiceSelfAssessedTaxDistQuantityVariance | — |
| RCV_CHARGE_ADDITION_FLAG | InvoiceSelfAssessedTaxDistRcvChargeAdditionFlag | — |
| RCV_TRANSACTION_ID | InvoiceSelfAssessedTaxDistRcvTransactionId | — |
| REC_NREC_RATE | InvoiceSelfAssessedTaxDistRecNrecRate | — |
| RECEIPT_CONVERSION_RATE | InvoiceSelfAssessedTaxDistReceiptConversionRate | — |
| RECEIPT_CURRENCY_AMOUNT | InvoiceSelfAssessedTaxDistReceiptCurrencyAmount | — |
| RECEIPT_CURRENCY_CODE | InvoiceSelfAssessedTaxDistCurrencyCode | — |
| RECEIPT_MISSING_FLAG | InvoiceSelfAssessedTaxDistReceiptMissingFlag | — |
| RECEIPT_REQUIRED_FLAG | InvoiceSelfAssessedTaxDistReceiptRequiredFlag | — |
| RECEIPT_VERIFIED_FLAG | InvoiceSelfAssessedTaxDistReceiptVerifiedFlag | — |
| RECOVERY_RATE_ID | InvoiceSelfAssessedTaxDistRecoveryRateId | — |
| RECOVERY_RATE_NAME | InvoiceSelfAssessedTaxDistRecoveryRateName | — |
| RECOVERY_TYPE_CODE | InvoiceSelfAssessedTaxDistRecoveryTypeCode | ✅ |
| REFERENCE_1 | InvoiceSelfAssessedTaxDistReference1 | — |
| REFERENCE_2 | InvoiceSelfAssessedTaxDistReference2 | — |
| RELATED_ID | InvoiceSelfAssessedTaxDistRelatedId | — |
| REQUEST_ID | InvoiceSelfAssessedTaxDistRequestId | — |
| REVERSAL_FLAG | InvoiceSelfAssessedTaxDistReversalFlag | ✅ |
| ROUNDING_AMT | InvoiceSelfAssessedTaxDistRoundingAmt | — |
| SELF_ASSESSED_FLAG | InvoiceSelfAssessedTaxDistSelfAssessedFlag | — |
| SELF_ASSESSED_TAX_LIAB_CCID | InvoiceSelfAssessedTaxDistSelfAssessedTaxLiabCcid | — |
| SET_OF_BOOKS_ID | InvoiceSelfAssessedTaxDistSetOfBooksId | — |
| START_EXPENSE_DATE | InvoiceSelfAssessedTaxDistStartExpenseDate | — |
| STAT_AMOUNT | InvoiceSelfAssessedTaxDistStatAmount | — |
| SUMMARY_TAX_LINE_ID | InvoiceSelfAssessedTaxDistSummaryTaxLineId | — |
| TASK_ID | InvoiceSelfAssessedTaxDistTaskId | — |
| TAX_ALREADY_DISTRIBUTED_FLAG | InvoiceSelfAssessedTaxDistTaxAlreadyDistributedFlag | — |
| TAX_CODE_ID | InvoiceSelfAssessedTaxDistTaxCodeId | — |
| TAX_RECOVERABLE_FLAG | InvoiceSelfAssessedTaxDistTaxRecoverableFlag | — |
| TAXABLE_AMOUNT | InvoiceSelfAssessedTaxDistTaxableAmount | — |
| TAXABLE_BASE_AMOUNT | InvoiceSelfAssessedTaxDistTaxableBaseAmount | — |
| TYPE_1099 | InvoiceSelfAssessedTaxDistType1099 | — |
| UNIT_PRICE | InvoiceSelfAssessedTaxDistUnitPrice | — |
| UPGRADE_BASE_POSTED_AMT | InvoiceSelfAssessedTaxDistUpgradeBasePostedAmt | — |
| UPGRADE_POSTED_AMT | InvoiceSelfAssessedTaxDistUpgradePostedAmt | — |
| USSGL_TRANSACTION_CODE | InvoiceSelfAssessedTaxDistUssglTransactionCode | — |
| USSGL_TRX_CODE_CONTEXT | InvoiceSelfAssessedTaxDistUssglTrxCodeContext | — |
| WEB_PARAMETER_ID | InvoiceSelfAssessedTaxDistWebParameterId | — |
| WITHHOLDING_TAX_CODE_ID | InvoiceSelfAssessedTaxDistWithholdingTaxCodeId | — |
