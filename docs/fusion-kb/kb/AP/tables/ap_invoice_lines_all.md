---
id: DOC-AP-013
doc_type: system-doc
title: "AP_INVOICE_LINES_ALL — Linhas de Faturas de Fornecedores"
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
  - linhas-fatura
  - invoice-lines
  - ap-lines
aliases:
  - AP_INVOICE_LINES_ALL
  - ap_invoice_lines_all
  - linhas-fatura-ap
  - invoice-lines-ap
  - linhas-faturas-fornecedores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_INVOICE_LINES_ALL

## 📌 Visão Geral

Armazena as **linhas** de cada fatura do módulo Accounts Payable. Cada linha representa um item, imposto, frete ou encargo dentro da fatura, contendo descrição, quantidade, valor unitário, valor total e referência a pedido de compra. Atua como nível intermediário entre o cabeçalho da fatura ([[ap_invoices_all]]) e as distribuições contábeis ([[ap_invoice_distributions_all]]).

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhamento da fatura:** Cada item, serviço, imposto ou frete recebido é registrado como uma linha separada.
- **Matching com PO:** Linhas do tipo ITEM podem ser vinculadas a linhas de pedido de compra para validação de preço e quantidade.
- **Cálculo de impostos:** Linhas do tipo TAX armazenam os impostos calculados automaticamente ou informados manualmente.
- **Geração de distribuições:** Cada linha gera uma ou mais distribuições contábeis em [[ap_invoice_distributions_all]].
- **Retenções fiscais:** Suporte a linhas de withholding tax (AWT) geradas automaticamente.
- **Rastreabilidade:** Vinculação de cada item da fatura ao respectivo PO line e shipment para auditoria.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INVOICE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da fatura (parte da PK composta) | [[ap_invoices_all]] | 🟢 100% |
| 2 | LINE_NUMBER | NUMBER | NOT NULL | PK | Número sequencial da linha na fatura | — | 🟢 100% |
| 3 | LINE_TYPE_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Classificação | Tipo da linha (ITEM/TAX/FREIGHT/MISCELLANEOUS/AWT) | [[ap_lookup_codes]] | 🟢 100% |
| 4 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor da linha na moeda da transação | — | 🟢 100% |
| 5 | BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda funcional (ledger) | — | 🟢 100% |
| 6 | QUANTITY_INVOICED | NUMBER | NULL | Quantidade | Quantidade faturada | — | 🟢 100% |
| 7 | UNIT_PRICE | NUMBER | NULL | Financeiro | Preço unitário | — | 🟢 100% |
| 8 | UNIT_MEAS_LOOKUP_CODE | VARCHAR2(25) | NULL | Quantidade | Unidade de medida | — | 🟢 100% |
| 9 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição da linha | — | 🟢 100% |
| 10 | ACCOUNTING_DATE | DATE | NULL | Contabilidade | Data contábil da linha | — | 🟢 100% |
| 11 | DIST_CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Conta contábil padrão | [[gl_code_combinations]] | 🟢 100% |
| 12 | PO_HEADER_ID | NUMBER(18) | NULL | Referência cruzada | Cabeçalho do PO vinculado | [[po_headers_all]] | 🟢 100% |
| 13 | PO_LINE_ID | NUMBER(18) | NULL | Referência cruzada | Linha do PO vinculada | [[po_lines_all]] | 🟢 100% |
| 14 | PO_LINE_LOCATION_ID | NUMBER(18) | NULL | Referência cruzada | Shipment do PO vinculado | [[po_line_locations_all]] | 🟢 100% |
| 15 | PO_DISTRIBUTION_ID | NUMBER(18) | NULL | Referência cruzada | Distribuição do PO vinculada | [[po_distributions_all]] | 🟢 100% |
| 16 | RCV_TRANSACTION_ID | NUMBER(18) | NULL | Referência cruzada | Transação de recebimento vinculada | [[rcv_transactions]] | 🟢 100% |
| 17 | RCV_SHIPMENT_LINE_ID | NUMBER(18) | NULL | Referência cruzada | Linha de shipment de recebimento | [[rcv_shipment_lines]] | 🟡 75% |
| 18 | MATCH_TYPE | VARCHAR2(25) | NULL | Classificação | Tipo de matching (ITEM_TO_PO/ITEM_TO_RECEIPT/etc.) | — | 🟢 100% |
| 19 | TAX_CLASSIFICATION_CODE | VARCHAR2(30) | NULL | Fiscal | Código de classificação fiscal | — | 🟢 100% |
| 20 | TAX_RATE_ID | NUMBER(18) | NULL | Fiscal | ID da taxa de imposto | — | 🟡 75% |
| 21 | TAX_RATE | NUMBER | NULL | Fiscal | Percentual do imposto | — | 🟢 100% |
| 22 | INCOME_TAX_REGION | VARCHAR2(10) | NULL | Fiscal | Região fiscal (imposto de renda) | — | 🟡 75% |
| 23 | TYPE_1099 | VARCHAR2(10) | NULL | Fiscal | Tipo 1099 (reporting fiscal US) | — | 🟡 70% |
| 24 | DISCARDED_FLAG | VARCHAR2(1) | NULL | Status | Indica se a linha foi descartada (Y/N) | — | 🟢 100% |
| 25 | CANCELLED_FLAG | VARCHAR2(1) | NULL | Status | Indica se a linha foi cancelada (Y/N) | — | 🟢 100% |
| 26 | GENERATE_DISTS | VARCHAR2(1) | NULL | Controle | Indica se distribuições foram geradas (Y/D/N) | — | 🟢 100% |
| 27 | ASSETS_TRACKING_FLAG | VARCHAR2(1) | NULL | Controle | Rastreamento de ativo fixo (Y/N) | — | 🟢 100% |
| 28 | PROJECT_ID | NUMBER(18) | NULL | Projetos | Projeto vinculado | [[pjf_projects_all_b]] | 🟢 100% |
| 29 | TASK_ID | NUMBER(18) | NULL | Projetos | Tarefa do projeto | [[pjf_tasks_b]] | 🟢 100% |
| 30 | ITEM_ID | NUMBER(18) | NULL | Item | Item do inventário | [[egp_system_items_b]] | 🟡 75% |
| 31 | ITEM_DESCRIPTION | VARCHAR2(240) | NULL | Item | Descrição do item | — | 🟢 100% |
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
- [[ap_invoices_all]] — via `INVOICE_ID` (fatura-cabeçalho)
- [[gl_code_combinations]] — via `DIST_CODE_COMBINATION_ID` (conta contábil padrão)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra)
- [[po_lines_all]] — via `PO_LINE_ID` (linha do pedido de compra vinculada à linha da fatura)
- [[po_line_locations_all]] — via `PO_LINE_LOCATION_ID` (shipment do PO referenciado na linha da fatura)
- [[po_distributions_all]] — via `PO_DISTRIBUTION_ID` (distribuição do PO)
- [[rcv_transactions]] — via `RCV_TRANSACTION_ID` (recebimento físico vinculado à linha da fatura)
- [[pjf_projects_all_b]] — via `PROJECT_ID` (projeto associado à linha da fatura)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da linha da fatura)

### Tabelas-filha (FK de saída)
- [[ap_invoice_distributions_all]] — via `INVOICE_ID` + `LINE_NUMBER` (distribuições contábeis)

---

## 📎 Uso Típico

### Linhas de uma fatura
```sql
SELECT ail.LINE_NUMBER, ail.LINE_TYPE_LOOKUP_CODE,
       ail.DESCRIPTION, ail.QUANTITY_INVOICED,
       ail.UNIT_PRICE, ail.AMOUNT
FROM   AP_INVOICE_LINES_ALL ail
WHERE  ail.INVOICE_ID = :p_invoice_id
ORDER BY ail.LINE_NUMBER;
```

### Linhas com matching a PO
```sql
SELECT ail.LINE_NUMBER, ail.AMOUNT, ail.MATCH_TYPE,
       ph.SEGMENT1 AS po_number, pl.LINE_NUM AS po_line
FROM   AP_INVOICE_LINES_ALL ail
JOIN   PO_HEADERS_ALL ph ON ph.PO_HEADER_ID = ail.PO_HEADER_ID
JOIN   PO_LINES_ALL pl ON pl.PO_LINE_ID = ail.PO_LINE_ID
WHERE  ail.INVOICE_ID = :p_invoice_id
  AND  ail.LINE_TYPE_LOOKUP_CODE = 'ITEM';
```

### Filtros comuns
- `LINE_TYPE_LOOKUP_CODE = 'ITEM'` — Apenas linhas de item
- `DISCARDED_FLAG IS NULL OR DISCARDED_FLAG = 'N'` — Exclui descartadas
- `CANCELLED_FLAG IS NULL OR CANCELLED_FLAG = 'N'` — Exclui canceladas

---

## 🔒 Observações

- O campo `LINE_TYPE_LOOKUP_CODE` classifica a linha: **ITEM** (item/serviço), **TAX** (imposto), **FREIGHT** (frete), **MISCELLANEOUS** (diversos), **AWT** (withholding tax).
- Linhas do tipo **ITEM** podem ser vinculadas a PO lines/shipments para matching. O campo `MATCH_TYPE` indica o tipo de matching realizado.
- A PK composta é `INVOICE_ID` + `LINE_NUMBER`.
- O campo `GENERATE_DISTS` controla a geração de distribuições: **Y** (gerar), **D** (já gerado), **N** (não gerar).
- Linhas descartadas (`DISCARDED_FLAG = 'Y'`) permanecem na tabela mas são ignoradas nos processos de negócio.

---

## 🔗 PVOs Relacionados

### [[costaccountingtransactionspvo|CostAccountingTransactionsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INVOICE_ID | InvoiceLinePEOInvoiceId | — |
| LINE_NUMBER | InvoiceLinePEOLineNumber | — |
| OBJECT_VERSION_NUMBER | InvoiceLinesPEOObjectVersionNumber | — |

### [[costaccountingtransactionsrefpvo|CostAccountingTransactionsRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INVOICE_ID | InvoiceLinePEOInvoiceId | — |
| LINE_NUMBER | InvoiceLinePEOLineNumber | — |
| OBJECT_VERSION_NUMBER | InvoiceLinesPEOObjectVersionNumber | — |

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 76/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_DATE | InvoiceLineAccountingDate | ✅ |
| ADJUSTMENT_REASON | InvoiceLineAdjustmentReason | ✅ |
| AMOUNT | InvoiceLineAmount | ✅ |
| ASSESSABLE_VALUE | InvoiceLineAssessableValue | ✅ |
| ASSET_BOOK_TYPE_CODE | InvoiceLineAssetBookTypeCode | ✅ |
| ASSETS_TRACKING_FLAG | InvoiceLineAssetsTrackingFlag | ✅ |
| BASE_AMOUNT | InvoiceLineBaseAmount | ✅ |
| BUDGET_DATE | InvoiceLineBudgetDate | ✅ |
| CANCELLED_FLAG | InvoiceLineCancelledFlag | ✅ |
| CONTROL_AMOUNT | InvoiceLineControlAmount | ✅ |
| CORRECTED_INV_ID | InvoiceLineCorrectedInvId | — |
| CORRECTED_LINE_NUMBER | InvoiceLineCorrectedLineNumber | ✅ |
| CREATED_BY | InvoiceLineCreatedBy | ✅ |
| CREATION_DATE | InvoiceLineCreationDate | ✅ |
| DEF_ACCTG_ACCRUAL_CCID | InvoiceLineDefAcctgAclCcid | ✅ |
| DEF_ACCTG_END_DATE | InvoiceLineDefAcctgEndDate | ✅ |
| DEF_ACCTG_NUMBER_OF_PERIODS | InvoiceLineDefAcctgNumberOfPeriods | ✅ |
| DEF_ACCTG_PERIOD_TYPE | InvoiceLineDefAcctgPeriodType | ✅ |
| DEF_ACCTG_START_DATE | InvoiceLineDefAcctgStartDate | ✅ |
| DEFAULT_DIST_CCID | InvoiceLineDefaultDistCcid | ✅ |
| DEFERRED_ACCTG_FLAG | InvoiceLineDeferredAcctgFlag | ✅ |
| DESCRIPTION | InvoiceLineDescription | ✅ |
| DISCARDED_FLAG | InvoiceLineDiscardedFlag | ✅ |
| EXPENDITURE_ITEM_DATE | InvoiceLineExpenditureItemDate | ✅ |
| FINAL_MATCH_FLAG | InvoiceLineFinalMatchFlag | ✅ |
| FUNDS_STATUS | InvoiceLineFundsStatus | ✅ |
| INCLUDED_TAX_AMOUNT | InvoiceLineIncludedTaxAmount | ✅ |
| INCOME_TAX_REGION | InvoiceLineIncomeTaxRegion | ✅ |
| INVENTORY_ITEM_ID | InvoiceLineInventoryItemId | — |
| INVOICE_ID | AppliedInvoiceLineInvoiceId | — |
| INVOICE_ID | InvoiceId | ✅ |
| INVOICE_INCLUDES_PREPAY_FLAG | InvoiceLineInvoiceIncludesPrepayFlag | ✅ |
| ITEM_DESCRIPTION | InvoiceLineItemDescription | ✅ |
| LAST_UPDATE_DATE | InvoiceLineLastUpdateDate | ✅ |
| LAST_UPDATED_BY | InvoiceLineLastUpdatedBy | ✅ |
| LCM_ENABLED_FLAG | InvoiceLineLCMEnabledLookupCode | ✅ |
| LINE_GROUP_NUMBER | InvoiceLineLineGroupNumber | ✅ |
| LINE_NUMBER | AppliedInvoiceLineLineNumber | — |
| LINE_NUMBER | LineNumber | ✅ |
| LINE_SOURCE | InvoiceLineLineSource | — |
| LINE_TYPE_LOOKUP_CODE | InvoiceLineLineTypeLookupCode | ✅ |
| MANUFACTURER | InvoiceLineManufacturer | ✅ |
| MATCH_TYPE | InvoiceLineMatchType | ✅ |
| MODEL_NUMBER | InvoiceLineModelNumber | ✅ |
| OBJECT_VERSION_NUMBER | AppliedInvoiceLineObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | InvoiceLineObjectVersionNumber | — |
| ORG_ID | InvoiceLineOrgId | ✅ |
| ORIGINAL_AMOUNT | InvoiceLineOriginalAmount | ✅ |
| ORIGINAL_BASE_AMOUNT | InvoiceLineOriginalBaseAmount | ✅ |
| ORIGINAL_ROUNDING_AMT | InvoiceLineOriginalRoundingAmt | ✅ |
| PA_CC_AR_INVOICE_LINE_NUM | InvoiceLinePaCcArInvoiceLineNum | ✅ |
| PA_CC_PROCESSED_CODE | InvoiceLinePaCcProcessedCode | ✅ |
| PERIOD_NAME | InvoiceLinePeriodName | ✅ |
| PJC_EXPENDITURE_ITEM_DATE | InvoiceLinePjcExpenditureItemDate | ✅ |
| PREPAY_INVOICE_ID | InvoiceLinePrepayInvoiceId | — |
| PREPAY_LINE_NUMBER | InvoiceLinePrepayLineNumber | ✅ |
| PRODUCT_CATEGORY | InvoiceLineProductCategory | ✅ |
| PRODUCT_FISC_CLASSIFICATION | InvoiceLineProductFiscClassification | ✅ |
| PRODUCT_TYPE | InvoiceLineProductType | ✅ |
| PRORATE_ACROSS_ALL_ITEMS | InvoiceLineProrateAcrossAllItems | ✅ |
| QUANTITY_INVOICED | InvoiceLineQuantityInvoiced | ✅ |
| REFERENCE_KEY1 | InvoiceLineReferenceKey1 | — |
| RETAINED_AMOUNT | InvoiceLineRetainedAmount | ✅ |
| RETAINED_AMOUNT_REMAINING | InvoiceLineRetainedAmountRemaining | ✅ |
| RETAINED_INVOICE_ID | InvoiceLineRetainedInvoiceId | — |
| RETAINED_LINE_NUMBER | InvoiceLineRetainedLineNumber | ✅ |
| ROUNDING_AMT | InvoiceLineRoundingAmt | ✅ |
| SERIAL_NUMBER | InvoiceLineSerialNumber | ✅ |
| SHIP_TO_LOCATION_ID | InvoiceLineShipToLocationId | — |
| TAX | InvoiceLineTax | ✅ |
| TAX_ALREADY_CALCULATED_FLAG | InvoiceLineTaxAlreadyCalculatedFlag | ✅ |
| TAX_CLASSIFICATION_CODE | InvoiceLineTaxClassificationCode | ✅ |
| TAX_JURISDICTION_CODE | InvoiceLineTaxJurisdictionCode | ✅ |
| TAX_RATE | InvoiceLineTaxRate | ✅ |
| TAX_RATE_CODE | InvoiceLineTaxRateCode | ✅ |
| TAX_REGIME_CODE | InvoiceLineTaxRegimeCode | ✅ |
| TAX_STATUS_CODE | InvoiceLineTaxStatusCode | — |
| TOTAL_NREC_TAX_AMOUNT | InvoiceLineTotalNrecTaxAmount | ✅ |
| TOTAL_NREC_TAX_AMT_FUNCL_CURR | InvoiceLineTotalNrecTaxAmtFunclCurr | ✅ |
| TOTAL_REC_TAX_AMOUNT | InvoiceLineTotalRecTaxAmount | ✅ |
| TOTAL_REC_TAX_AMT_FUNCL_CURR | InvoiceLineTotalRecTaxAmtFunclCurr | ✅ |
| TRX_BUSINESS_CATEGORY | InvoiceLineTrxBusinessCategory | ✅ |
| TYPE_1099 | InvoiceLineType1099 | ✅ |
| UNIT_MEAS_LOOKUP_CODE | InvoiceLineUnitMeasLookupCode | ✅ |
| UNIT_PRICE | InvoiceLineUnitPrice | ✅ |
| USER_DEFINED_FISC_CLASS | InvoiceLineUserDefinedFiscClass | ✅ |
| WARRANTY_NUMBER | InvoiceLineWarrantyNumber | ✅ |
| WFAPPROVAL_STATUS | InvoiceLineWfapprovalStatus | ✅ |

### [[prepaymentappliationdistributionpvo|PrepaymentAppliationDistributionPVO]] (AP · BICC: 8/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | InvoiceLineAmount | ✅ |
| BASE_AMOUNT | InvoiceLineBaseAmount | ✅ |
| INCLUDED_TAX_AMOUNT | InvoiceLineIncludedTaxAmount | ✅ |
| INVOICE_ID | InvoiceLineInvoiceId | — |
| INVOICE_INCLUDES_PREPAY_FLAG | InvoiceLineInvoiceIncludesPrepayFlag | ✅ |
| LAST_UPDATE_DATE | InvoiceLineLastUpdateDate | ✅ |
| LINE_NUMBER | InvoiceLineLineNumber | ✅ |
| LINE_TYPE_LOOKUP_CODE | InvoiceLineLineTypeLookupCode | ✅ |
| PREPAY_INVOICE_ID | InvoiceLinePrepayInvoiceId | — |
| PREPAY_LINE_NUMBER | InvoiceLinePrepayLineNumber | ✅ |

### [[receiptaccountingtxnp1|ReceiptAccountingTxnP1]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_SEGMENT | ApInvoiceLinesAllAccountSegment | — |
| ACCOUNTING_DATE | ApInvoiceLinesAllAccountingDate | — |
| ADJUSTMENT_REASON | ApInvoiceLinesAllAdjustmentReason | — |
| AMOUNT | ApInvoiceLinesAllAmount4 | — |
| APPLICATION_ID | ApInvoiceLinesAllApplicationId1 | — |
| ASSESSABLE_VALUE | ApInvoiceLinesAllAssessableValue3 | — |
| ASSET_BOOK_TYPE_CODE | ApInvoiceLinesAllAssetBookTypeCode | — |
| ASSET_CATEGORY_ID | ApInvoiceLinesAllAssetCategoryId | — |
| ASSETS_TRACKING_FLAG | ApInvoiceLinesAllAssetsTrackingFlag | — |
| ATTRIBUTE1 | ApInvoiceLinesAllAttribute129 | — |
| ATTRIBUTE10 | ApInvoiceLinesAllAttribute108 | — |
| ATTRIBUTE11 | ApInvoiceLinesAllAttribute1112 | — |
| ATTRIBUTE12 | ApInvoiceLinesAllAttribute1210 | — |
| ATTRIBUTE13 | ApInvoiceLinesAllAttribute138 | — |
| ATTRIBUTE14 | ApInvoiceLinesAllAttribute148 | — |
| ATTRIBUTE15 | ApInvoiceLinesAllAttribute158 | — |
| ATTRIBUTE2 | ApInvoiceLinesAllAttribute28 | — |
| ATTRIBUTE3 | ApInvoiceLinesAllAttribute38 | — |
| ATTRIBUTE4 | ApInvoiceLinesAllAttribute48 | — |
| ATTRIBUTE5 | ApInvoiceLinesAllAttribute58 | — |
| ATTRIBUTE6 | ApInvoiceLinesAllAttribute68 | — |
| ATTRIBUTE7 | ApInvoiceLinesAllAttribute78 | — |
| ATTRIBUTE8 | ApInvoiceLinesAllAttribute88 | — |
| ATTRIBUTE9 | ApInvoiceLinesAllAttribute98 | — |
| ATTRIBUTE_CATEGORY | ApInvoiceLinesAllAttributeCategory8 | — |
| ATTRIBUTE_DATE1 | ApInvoiceLinesAllAttributeDate18 | — |
| ATTRIBUTE_DATE2 | ApInvoiceLinesAllAttributeDate28 | — |
| ATTRIBUTE_DATE3 | ApInvoiceLinesAllAttributeDate38 | — |
| ATTRIBUTE_DATE4 | ApInvoiceLinesAllAttributeDate48 | — |
| ATTRIBUTE_DATE5 | ApInvoiceLinesAllAttributeDate58 | — |
| ATTRIBUTE_NUMBER1 | ApInvoiceLinesAllAttributeNumber18 | — |
| ATTRIBUTE_NUMBER2 | ApInvoiceLinesAllAttributeNumber28 | — |
| ATTRIBUTE_NUMBER3 | ApInvoiceLinesAllAttributeNumber38 | — |
| ATTRIBUTE_NUMBER4 | ApInvoiceLinesAllAttributeNumber48 | — |
| ATTRIBUTE_NUMBER5 | ApInvoiceLinesAllAttributeNumber58 | — |
| AWARD_ID | ApInvoiceLinesAllAwardId2 | — |
| AWT_GROUP_ID | ApInvoiceLinesAllAwtGroupId1 | — |
| BALANCING_SEGMENT | ApInvoiceLinesAllBalancingSegment | — |
| BASE_AMOUNT | ApInvoiceLinesAllBaseAmount1 | — |
| BUDGET_DATE | ApInvoiceLinesAllBudgetDate2 | — |
| CANCELLED_FLAG | ApInvoiceLinesAllCancelledFlag | — |
| CC_REVERSAL_FLAG | ApInvoiceLinesAllCcReversalFlag | — |
| COMPANY_PREPAID_INVOICE_ID | ApInvoiceLinesAllCompanyPrepaidInvoiceId | — |
| CONSUMPTION_ADVICE_HEADER_ID | ApInvoiceLinesAllConsumptionAdviceHeaderId1 | — |
| CONSUMPTION_ADVICE_LINE_ID | ApInvoiceLinesAllConsumptionAdviceLineId1 | — |
| CONTROL_AMOUNT | ApInvoiceLinesAllControlAmount1 | — |
| CORRECTED_INV_ID | ApInvoiceLinesAllCorrectedInvId | — |
| CORRECTED_LINE_NUMBER | ApInvoiceLinesAllCorrectedLineNumber | — |
| COST_CENTER_SEGMENT | ApInvoiceLinesAllCostCenterSegment | — |
| COST_FACTOR_ID | ApInvoiceLinesAllCostFactorId | — |
| COUNTRY_OF_SUPPLY | ApInvoiceLinesAllCountryOfSupply | — |
| CREATED_BY | ApInvoiceLinesAllCreatedBy11 | — |
| CREATION_DATE | ApInvoiceLinesAllCreationDate11 | — |
| CREDIT_CARD_TRX_ID | ApInvoiceLinesAllCreditCardTrxId | — |
| DAILY_AMOUNT | ApInvoiceLinesAllDailyAmount | — |
| DEF_ACCTG_END_DATE | ApInvoiceLinesAllDefAcctgEndDate | — |
| DEF_ACCTG_NUMBER_OF_PERIODS | ApInvoiceLinesAllDefAcctgNumberOfPeriods | — |
| DEF_ACCTG_PERIOD_TYPE | ApInvoiceLinesAllDefAcctgPeriodType | — |
| DEF_ACCTG_START_DATE | ApInvoiceLinesAllDefAcctgStartDate | — |
| DEFAULT_DIST_CCID | ApInvoiceLinesAllDefaultDistCcid | — |
| DEFERRED_ACCTG_FLAG | ApInvoiceLinesAllDeferredAcctgFlag | — |
| DESCRIPTION | ApInvoiceLinesAllDescription2 | — |
| DISCARDED_FLAG | ApInvoiceLinesAllDiscardedFlag | — |
| DISPUTABLE_FLAG | ApInvoiceLinesAllDisputableFlag | — |
| DISTRIBUTION_SET_ID | ApInvoiceLinesAllDistributionSetId1 | — |
| END_EXPENSE_DATE | ApInvoiceLinesAllEndExpenseDate | — |
| EXPENDITURE_ITEM_DATE | ApInvoiceLinesAllExpenditureItemDate1 | — |
| EXPENDITURE_ORGANIZATION_ID | ApInvoiceLinesAllExpenditureOrganizationId1 | — |
| EXPENDITURE_TYPE | ApInvoiceLinesAllExpenditureType1 | — |
| EXPENSE_GROUP | ApInvoiceLinesAllExpenseGroup | — |
| FINAL_DISCHARGE_LOCATION_ID | ApInvoiceLinesAllFinalDischargeLocationId3 | — |
| FINAL_MATCH_FLAG | ApInvoiceLinesAllFinalMatchFlag2 | — |
| FOS_XFACE_FLAG | ApInvoiceLinesAllFosXfaceFlag | — |
| FUNDS_STATUS | ApInvoiceLinesAllFundsStatus5 | — |
| GENERATE_DISTS | ApInvoiceLinesAllGenerateDists | — |
| GLOBAL_ATTRIBUTE1 | ApInvoiceLinesAllGlobalAttribute116 | — |
| GLOBAL_ATTRIBUTE10 | ApInvoiceLinesAllGlobalAttribute104 | — |
| GLOBAL_ATTRIBUTE11 | ApInvoiceLinesAllGlobalAttribute117 | — |
| GLOBAL_ATTRIBUTE12 | ApInvoiceLinesAllGlobalAttribute124 | — |
| GLOBAL_ATTRIBUTE13 | ApInvoiceLinesAllGlobalAttribute134 | — |
| GLOBAL_ATTRIBUTE14 | ApInvoiceLinesAllGlobalAttribute144 | — |
| GLOBAL_ATTRIBUTE15 | ApInvoiceLinesAllGlobalAttribute154 | — |
| GLOBAL_ATTRIBUTE16 | ApInvoiceLinesAllGlobalAttribute164 | — |
| GLOBAL_ATTRIBUTE17 | ApInvoiceLinesAllGlobalAttribute174 | — |
| GLOBAL_ATTRIBUTE18 | ApInvoiceLinesAllGlobalAttribute184 | — |
| GLOBAL_ATTRIBUTE19 | ApInvoiceLinesAllGlobalAttribute194 | — |
| GLOBAL_ATTRIBUTE2 | ApInvoiceLinesAllGlobalAttribute24 | — |
| GLOBAL_ATTRIBUTE20 | ApInvoiceLinesAllGlobalAttribute204 | — |
| GLOBAL_ATTRIBUTE3 | ApInvoiceLinesAllGlobalAttribute34 | — |
| GLOBAL_ATTRIBUTE4 | ApInvoiceLinesAllGlobalAttribute44 | — |
| GLOBAL_ATTRIBUTE5 | ApInvoiceLinesAllGlobalAttribute54 | — |
| GLOBAL_ATTRIBUTE6 | ApInvoiceLinesAllGlobalAttribute64 | — |
| GLOBAL_ATTRIBUTE7 | ApInvoiceLinesAllGlobalAttribute74 | — |
| GLOBAL_ATTRIBUTE8 | ApInvoiceLinesAllGlobalAttribute84 | — |
| GLOBAL_ATTRIBUTE9 | ApInvoiceLinesAllGlobalAttribute94 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ApInvoiceLinesAllGlobalAttributeCategory4 | — |
| GLOBAL_ATTRIBUTE_DATE1 | ApInvoiceLinesAllGlobalAttributeDate11 | — |
| GLOBAL_ATTRIBUTE_DATE2 | ApInvoiceLinesAllGlobalAttributeDate21 | — |
| GLOBAL_ATTRIBUTE_DATE3 | ApInvoiceLinesAllGlobalAttributeDate31 | — |
| GLOBAL_ATTRIBUTE_DATE4 | ApInvoiceLinesAllGlobalAttributeDate41 | — |
| GLOBAL_ATTRIBUTE_DATE5 | ApInvoiceLinesAllGlobalAttributeDate51 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | ApInvoiceLinesAllGlobalAttributeNumber11 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | ApInvoiceLinesAllGlobalAttributeNumber21 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | ApInvoiceLinesAllGlobalAttributeNumber31 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | ApInvoiceLinesAllGlobalAttributeNumber41 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | ApInvoiceLinesAllGlobalAttributeNumber51 | — |
| HISTORICAL_FLAG | ApInvoiceLinesAllHistoricalFlag1 | — |
| INCLUDED_TAX_AMOUNT | ApInvoiceLinesAllIncludedTaxAmount | — |
| INCOME_TAX_REGION | ApInvoiceLinesAllIncomeTaxRegion | — |
| INTENDED_USE_CLASSIF_ID | ApInvoiceLinesAllIntendedUseClassifId1 | — |
| INVENTORY_ITEM_ID | ApInvoiceLinesAllInventoryItemId2 | — |
| INVOICE_ID | ApInvoiceLinesAllInvoiceId2 | — |
| INVOICE_INCLUDES_PREPAY_FLAG | ApInvoiceLinesAllInvoiceIncludesPrepayFlag | — |
| ITEM_DESCRIPTION | ApInvoiceLinesAllItemDescription3 | — |
| JUSTIFICATION | ApInvoiceLinesAllJustification | — |
| LAST_UPDATE_DATE | ApInvoiceLinesAllLastUpdateDate11 | — |
| LAST_UPDATE_LOGIN | ApInvoiceLinesAllLastUpdateLogin11 | — |
| LAST_UPDATED_BY | ApInvoiceLinesAllLastUpdatedBy11 | — |
| LCM_ENABLED_FLAG | ApInvoiceLinesAllLcmEnabledFlag1 | — |
| LINE_GROUP_NUMBER | ApInvoiceLinesAllLineGroupNumber | — |
| LINE_NUMBER | ApInvoiceLinesAllLineNumber2 | — |
| LINE_OWNER_ROLE | ApInvoiceLinesAllLineOwnerRole | — |
| LINE_SELECTED_FOR_APPL_FLAG | ApInvoiceLinesAllLineSelectedForApplFlag | — |
| LINE_SELECTED_FOR_RELEASE_FLAG | ApInvoiceLinesAllLineSelectedForReleaseFlag | — |
| LINE_SOURCE | ApInvoiceLinesAllLineSource | — |
| LINE_TYPE_LOOKUP_CODE | ApInvoiceLinesAllLineTypeLookupCode | — |
| MANUFACTURER | ApInvoiceLinesAllManufacturer | — |
| MATCH_TYPE | ApInvoiceLinesAllMatchType | — |
| MERCHANT_DOCUMENT_NUMBER | ApInvoiceLinesAllMerchantDocumentNumber | — |
| MERCHANT_NAME | ApInvoiceLinesAllMerchantName | — |
| MERCHANT_REFERENCE | ApInvoiceLinesAllMerchantReference | — |
| MERCHANT_TAX_REG_NUMBER | ApInvoiceLinesAllMerchantTaxRegNumber | — |
| MERCHANT_TAXPAYER_ID | ApInvoiceLinesAllMerchantTaxpayerId | — |
| MODEL_NUMBER | ApInvoiceLinesAllModelNumber | — |
| OBJECT_VERSION_NUMBER | ApInvoiceLinesAllObjectVersionNumber8 | — |
| ORG_ID | ApInvoiceLinesAllOrgId1 | — |
| ORIGINAL_AMOUNT | ApInvoiceLinesAllOriginalAmount | — |
| ORIGINAL_BASE_AMOUNT | ApInvoiceLinesAllOriginalBaseAmount | — |
| ORIGINAL_ROUNDING_AMT | ApInvoiceLinesAllOriginalRoundingAmt | — |
| OVERLAY_DIST_CODE_CONCAT | ApInvoiceLinesAllOverlayDistCodeConcat | — |
| PA_CC_AR_INVOICE_ID | ApInvoiceLinesAllPaCcArInvoiceId | — |
| PA_CC_AR_INVOICE_LINE_NUM | ApInvoiceLinesAllPaCcArInvoiceLineNum | — |
| PA_CC_PROCESSED_CODE | ApInvoiceLinesAllPaCcProcessedCode | — |
| PA_QUANTITY | ApInvoiceLinesAllPaQuantity1 | — |
| PERIOD_NAME | ApInvoiceLinesAllPeriodName | — |
| PJC_BILLABLE_FLAG | ApInvoiceLinesAllPjcBillableFlag | — |
| PJC_CAPITALIZABLE_FLAG | ApInvoiceLinesAllPjcCapitalizableFlag | — |
| PJC_CONTEXT_CATEGORY | ApInvoiceLinesAllPjcContextCategory | — |
| PJC_CONTRACT_ID | ApInvoiceLinesAllPjcContractId | — |
| PJC_CONTRACT_LINE_ID | ApInvoiceLinesAllPjcContractLineId | — |
| PJC_EXPENDITURE_ITEM_DATE | ApInvoiceLinesAllPjcExpenditureItemDate | — |
| PJC_EXPENDITURE_TYPE_ID | ApInvoiceLinesAllPjcExpenditureTypeId | — |
| PJC_FUNDING_ALLOCATION_ID | ApInvoiceLinesAllPjcFundingAllocationId | — |
| PJC_ORGANIZATION_ID | ApInvoiceLinesAllPjcOrganizationId | — |
| PJC_PROJECT_ID | ApInvoiceLinesAllPjcProjectId | — |
| PJC_RESERVED_ATTRIBUTE1 | ApInvoiceLinesAllPjcReservedAttribute1 | — |
| PJC_RESERVED_ATTRIBUTE10 | ApInvoiceLinesAllPjcReservedAttribute10 | — |
| PJC_RESERVED_ATTRIBUTE2 | ApInvoiceLinesAllPjcReservedAttribute2 | — |
| PJC_RESERVED_ATTRIBUTE3 | ApInvoiceLinesAllPjcReservedAttribute3 | — |
| PJC_RESERVED_ATTRIBUTE4 | ApInvoiceLinesAllPjcReservedAttribute4 | — |
| PJC_RESERVED_ATTRIBUTE5 | ApInvoiceLinesAllPjcReservedAttribute5 | — |
| PJC_RESERVED_ATTRIBUTE6 | ApInvoiceLinesAllPjcReservedAttribute6 | — |
| PJC_RESERVED_ATTRIBUTE7 | ApInvoiceLinesAllPjcReservedAttribute7 | — |
| PJC_RESERVED_ATTRIBUTE8 | ApInvoiceLinesAllPjcReservedAttribute8 | — |
| PJC_RESERVED_ATTRIBUTE9 | ApInvoiceLinesAllPjcReservedAttribute9 | — |
| PJC_TASK_ID | ApInvoiceLinesAllPjcTaskId | — |
| PJC_USER_DEF_ATTRIBUTE1 | ApInvoiceLinesAllPjcUserDefAttribute1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | ApInvoiceLinesAllPjcUserDefAttribute10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | ApInvoiceLinesAllPjcUserDefAttribute2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | ApInvoiceLinesAllPjcUserDefAttribute3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | ApInvoiceLinesAllPjcUserDefAttribute4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | ApInvoiceLinesAllPjcUserDefAttribute5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | ApInvoiceLinesAllPjcUserDefAttribute6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | ApInvoiceLinesAllPjcUserDefAttribute7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | ApInvoiceLinesAllPjcUserDefAttribute8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | ApInvoiceLinesAllPjcUserDefAttribute9 | — |
| PJC_WORK_TYPE_ID | ApInvoiceLinesAllPjcWorkTypeId | — |
| PO_DISTRIBUTION_ID | ApInvoiceLinesAllPoDistributionId4 | — |
| PO_HEADER_ID | ApInvoiceLinesAllPoHeaderId7 | — |
| PO_LINE_ID | ApInvoiceLinesAllPoLineId5 | — |
| PO_LINE_LOCATION_ID | ApInvoiceLinesAllPoLineLocationId4 | — |
| PO_RELEASE_ID | ApInvoiceLinesAllPoReleaseId | — |
| PREPAY_APPL_REQUEST_ID | ApInvoiceLinesAllPrepayApplRequestId | — |
| PREPAY_INVOICE_ID | ApInvoiceLinesAllPrepayInvoiceId | — |
| PREPAY_LINE_NUMBER | ApInvoiceLinesAllPrepayLineNumber | — |
| PRIMARY_INTENDED_USE | ApInvoiceLinesAllPrimaryIntendedUse | — |
| PROD_FC_CATEG_ID | ApInvoiceLinesAllProdFcCategId | — |
| PRODUCT_CATEGORY | ApInvoiceLinesAllProductCategory3 | — |
| PRODUCT_FISC_CLASSIFICATION | ApInvoiceLinesAllProductFiscClassification1 | — |
| PRODUCT_TABLE | ApInvoiceLinesAllProductTable1 | — |
| PRODUCT_TYPE | ApInvoiceLinesAllProductType3 | — |
| PROGRAM_APPLICATION_ID | ApInvoiceLinesAllProgramApplicationId | — |
| PROGRAM_ID | ApInvoiceLinesAllProgramId | — |
| PROGRAM_UPDATE_DATE | ApInvoiceLinesAllProgramUpdateDate | — |
| PROJECT_ID | ApInvoiceLinesAllProjectId2 | — |
| PRORATE_ACROSS_ALL_ITEMS | ApInvoiceLinesAllProrateAcrossAllItems | — |
| PURCHASING_CATEGORY_ID | ApInvoiceLinesAllPurchasingCategoryId | — |
| QUANTITY_INVOICED | ApInvoiceLinesAllQuantityInvoiced | — |
| RCV_SHIPMENT_LINE_ID | ApInvoiceLinesAllRcvShipmentLineId | — |
| RCV_TRANSACTION_ID | ApInvoiceLinesAllRcvTransactionId1 | — |
| RECEIPT_CONVERSION_RATE | ApInvoiceLinesAllReceiptConversionRate | — |
| RECEIPT_CURRENCY_AMOUNT | ApInvoiceLinesAllReceiptCurrencyAmount | — |
| RECEIPT_CURRENCY_CODE | ApInvoiceLinesAllReceiptCurrencyCode | — |
| RECEIPT_MISSING_FLAG | ApInvoiceLinesAllReceiptMissingFlag | — |
| RECEIPT_REQUIRED_FLAG | ApInvoiceLinesAllReceiptRequiredFlag1 | — |
| RECEIPT_VERIFIED_FLAG | ApInvoiceLinesAllReceiptVerifiedFlag | — |
| REFERENCE_1 | ApInvoiceLinesAllReference11 | — |
| REFERENCE_2 | ApInvoiceLinesAllReference21 | — |
| REFERENCE_KEY1 | ApInvoiceLinesAllReferenceKey11 | — |
| REFERENCE_KEY2 | ApInvoiceLinesAllReferenceKey21 | — |
| REFERENCE_KEY3 | ApInvoiceLinesAllReferenceKey31 | — |
| REFERENCE_KEY4 | ApInvoiceLinesAllReferenceKey41 | — |
| REFERENCE_KEY5 | ApInvoiceLinesAllReferenceKey51 | — |
| REQUEST_ID | ApInvoiceLinesAllRequestId11 | — |
| REQUESTER_ID | ApInvoiceLinesAllRequesterId1 | — |
| RETAINED_AMOUNT | ApInvoiceLinesAllRetainedAmount | — |
| RETAINED_AMOUNT_REMAINING | ApInvoiceLinesAllRetainedAmountRemaining | — |
| RETAINED_INVOICE_ID | ApInvoiceLinesAllRetainedInvoiceId | — |
| RETAINED_LINE_NUMBER | ApInvoiceLinesAllRetainedLineNumber | — |
| ROUNDING_AMT | ApInvoiceLinesAllRoundingAmt | — |
| SERIAL_NUMBER | ApInvoiceLinesAllSerialNumber | — |
| SET_OF_BOOKS_ID | ApInvoiceLinesAllSetOfBooksId2 | — |
| SHIP_FROM_LOCATION_ID | ApInvoiceLinesAllShipFromLocationId3 | — |
| SHIP_TO_LOCATION_ID | ApInvoiceLinesAllShipToLocationId4 | — |
| SOURCE_APPLICATION_ID | ApInvoiceLinesAllSourceApplicationId | — |
| SOURCE_ENTITY_CODE | ApInvoiceLinesAllSourceEntityCode | — |
| SOURCE_EVENT_CLASS_CODE | ApInvoiceLinesAllSourceEventClassCode | — |
| SOURCE_LINE_ID | ApInvoiceLinesAllSourceLineId | — |
| SOURCE_TRX_ID | ApInvoiceLinesAllSourceTrxId | — |
| SOURCE_TRX_LEVEL_TYPE | ApInvoiceLinesAllSourceTrxLevelType | — |
| START_EXPENSE_DATE | ApInvoiceLinesAllStartExpenseDate | — |
| STAT_AMOUNT | ApInvoiceLinesAllStatAmount | — |
| SUMMARY_TAX_LINE_ID | ApInvoiceLinesAllSummaryTaxLineId | — |
| TASK_ID | ApInvoiceLinesAllTaskId2 | — |
| TAX | ApInvoiceLinesAllTax | — |
| TAX_ALREADY_CALCULATED_FLAG | ApInvoiceLinesAllTaxAlreadyCalculatedFlag | — |
| TAX_CLASSIFICATION_CODE | ApInvoiceLinesAllTaxClassificationCode2 | — |
| TAX_CODE_ID | ApInvoiceLinesAllTaxCodeId2 | — |
| TAX_JURISDICTION_CODE | ApInvoiceLinesAllTaxJurisdictionCode | — |
| TAX_RATE | ApInvoiceLinesAllTaxRate | — |
| TAX_RATE_CODE | ApInvoiceLinesAllTaxRateCode | — |
| TAX_RATE_ID | ApInvoiceLinesAllTaxRateId | — |
| TAX_REGIME_CODE | ApInvoiceLinesAllTaxRegimeCode | — |
| TAX_STATUS_CODE | ApInvoiceLinesAllTaxStatusCode | — |
| TOTAL_NREC_TAX_AMOUNT | ApInvoiceLinesAllTotalNrecTaxAmount | — |
| TOTAL_NREC_TAX_AMT_FUNCL_CURR | ApInvoiceLinesAllTotalNrecTaxAmtFunclCurr | — |
| TOTAL_REC_TAX_AMOUNT | ApInvoiceLinesAllTotalRecTaxAmount | — |
| TOTAL_REC_TAX_AMT_FUNCL_CURR | ApInvoiceLinesAllTotalRecTaxAmtFunclCurr | — |
| TRX_BUSINESS_CATEGORY | ApInvoiceLinesAllTrxBusinessCategory4 | — |
| TYPE_1099 | ApInvoiceLinesAllType10991 | — |
| UNIT_MEAS_LOOKUP_CODE | ApInvoiceLinesAllUnitMeasLookupCode | — |
| UNIT_PRICE | ApInvoiceLinesAllUnitPrice1 | — |
| USER_DEFINED_FISC_CLASS | ApInvoiceLinesAllUserDefinedFiscClass4 | — |
| USSGL_TRANSACTION_CODE | ApInvoiceLinesAllUssglTransactionCode1 | — |
| WARRANTY_NUMBER | ApInvoiceLinesAllWarrantyNumber | — |
| WEB_PARAMETER_ID | ApInvoiceLinesAllWebParameterId | — |
| WFAPPROVAL_STATUS | ApInvoiceLinesAllWfapprovalStatus1 | — |

### [[receiptaccountingtxnrefpvo|ReceiptAccountingTxnRefPVO]] (AR · BICC: 47/257)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_SEGMENT | ApInvoiceLinesAllAccountSegment | — |
| ACCOUNTING_DATE | ApInvoiceLinesAllAccountingDate | ✅ |
| ADJUSTMENT_REASON | ApInvoiceLinesAllAdjustmentReason | ✅ |
| AMOUNT | ApInvoiceLinesAllAmount4 | — |
| APPLICATION_ID | ApInvoiceLinesAllApplicationId1 | — |
| ASSESSABLE_VALUE | ApInvoiceLinesAllAssessableValue3 | ✅ |
| ASSET_BOOK_TYPE_CODE | ApInvoiceLinesAllAssetBookTypeCode | ✅ |
| ASSET_CATEGORY_ID | ApInvoiceLinesAllAssetCategoryId | — |
| ASSETS_TRACKING_FLAG | ApInvoiceLinesAllAssetsTrackingFlag | ✅ |
| ATTRIBUTE1 | ApInvoiceLinesAllAttribute129 | — |
| ATTRIBUTE10 | ApInvoiceLinesAllAttribute108 | — |
| ATTRIBUTE11 | ApInvoiceLinesAllAttribute1112 | — |
| ATTRIBUTE12 | ApInvoiceLinesAllAttribute1210 | — |
| ATTRIBUTE13 | ApInvoiceLinesAllAttribute138 | — |
| ATTRIBUTE14 | ApInvoiceLinesAllAttribute148 | — |
| ATTRIBUTE15 | ApInvoiceLinesAllAttribute158 | — |
| ATTRIBUTE2 | ApInvoiceLinesAllAttribute28 | — |
| ATTRIBUTE3 | ApInvoiceLinesAllAttribute38 | — |
| ATTRIBUTE4 | ApInvoiceLinesAllAttribute48 | — |
| ATTRIBUTE5 | ApInvoiceLinesAllAttribute58 | — |
| ATTRIBUTE6 | ApInvoiceLinesAllAttribute68 | — |
| ATTRIBUTE7 | ApInvoiceLinesAllAttribute78 | — |
| ATTRIBUTE8 | ApInvoiceLinesAllAttribute88 | — |
| ATTRIBUTE9 | ApInvoiceLinesAllAttribute98 | — |
| ATTRIBUTE_CATEGORY | ApInvoiceLinesAllAttributeCategory8 | — |
| ATTRIBUTE_DATE1 | ApInvoiceLinesAllAttributeDate18 | — |
| ATTRIBUTE_DATE2 | ApInvoiceLinesAllAttributeDate28 | — |
| ATTRIBUTE_DATE3 | ApInvoiceLinesAllAttributeDate38 | — |
| ATTRIBUTE_DATE4 | ApInvoiceLinesAllAttributeDate48 | — |
| ATTRIBUTE_DATE5 | ApInvoiceLinesAllAttributeDate58 | — |
| ATTRIBUTE_NUMBER1 | ApInvoiceLinesAllAttributeNumber18 | — |
| ATTRIBUTE_NUMBER2 | ApInvoiceLinesAllAttributeNumber28 | — |
| ATTRIBUTE_NUMBER3 | ApInvoiceLinesAllAttributeNumber38 | — |
| ATTRIBUTE_NUMBER4 | ApInvoiceLinesAllAttributeNumber48 | — |
| ATTRIBUTE_NUMBER5 | ApInvoiceLinesAllAttributeNumber58 | — |
| AWARD_ID | ApInvoiceLinesAllAwardId2 | — |
| AWT_GROUP_ID | ApInvoiceLinesAllAwtGroupId1 | — |
| BALANCING_SEGMENT | ApInvoiceLinesAllBalancingSegment | — |
| BASE_AMOUNT | ApInvoiceLinesAllBaseAmount1 | — |
| BUDGET_DATE | ApInvoiceLinesAllBudgetDate2 | ✅ |
| CANCELLED_FLAG | ApInvoiceLinesAllCancelledFlag | ✅ |
| CC_REVERSAL_FLAG | ApInvoiceLinesAllCcReversalFlag | — |
| COMPANY_PREPAID_INVOICE_ID | ApInvoiceLinesAllCompanyPrepaidInvoiceId | — |
| CONSUMPTION_ADVICE_HEADER_ID | ApInvoiceLinesAllConsumptionAdviceHeaderId1 | — |
| CONSUMPTION_ADVICE_LINE_ID | ApInvoiceLinesAllConsumptionAdviceLineId1 | — |
| CONTROL_AMOUNT | ApInvoiceLinesAllControlAmount1 | ✅ |
| CORRECTED_INV_ID | ApInvoiceLinesAllCorrectedInvId | — |
| CORRECTED_LINE_NUMBER | ApInvoiceLinesAllCorrectedLineNumber | ✅ |
| COST_CENTER_SEGMENT | ApInvoiceLinesAllCostCenterSegment | — |
| COST_FACTOR_ID | ApInvoiceLinesAllCostFactorId | — |
| COUNTRY_OF_SUPPLY | ApInvoiceLinesAllCountryOfSupply | — |
| CREATED_BY | ApInvoiceLinesAllCreatedBy11 | — |
| CREATION_DATE | ApInvoiceLinesAllCreationDate11 | — |
| CREDIT_CARD_TRX_ID | ApInvoiceLinesAllCreditCardTrxId | — |
| DAILY_AMOUNT | ApInvoiceLinesAllDailyAmount | — |
| DEF_ACCTG_END_DATE | ApInvoiceLinesAllDefAcctgEndDate | — |
| DEF_ACCTG_NUMBER_OF_PERIODS | ApInvoiceLinesAllDefAcctgNumberOfPeriods | — |
| DEF_ACCTG_PERIOD_TYPE | ApInvoiceLinesAllDefAcctgPeriodType | — |
| DEF_ACCTG_START_DATE | ApInvoiceLinesAllDefAcctgStartDate | — |
| DEFAULT_DIST_CCID | ApInvoiceLinesAllDefaultDistCcid | — |
| DEFERRED_ACCTG_FLAG | ApInvoiceLinesAllDeferredAcctgFlag | — |
| DESCRIPTION | ApInvoiceLinesAllDescription2 | ✅ |
| DISCARDED_FLAG | ApInvoiceLinesAllDiscardedFlag | ✅ |
| DISPUTABLE_FLAG | ApInvoiceLinesAllDisputableFlag | — |
| DISTRIBUTION_SET_ID | ApInvoiceLinesAllDistributionSetId1 | — |
| END_EXPENSE_DATE | ApInvoiceLinesAllEndExpenseDate | — |
| EXPENDITURE_ITEM_DATE | ApInvoiceLinesAllExpenditureItemDate1 | ✅ |
| EXPENDITURE_ORGANIZATION_ID | ApInvoiceLinesAllExpenditureOrganizationId1 | — |
| EXPENDITURE_TYPE | ApInvoiceLinesAllExpenditureType1 | — |
| EXPENSE_GROUP | ApInvoiceLinesAllExpenseGroup | — |
| FINAL_DISCHARGE_LOCATION_ID | ApInvoiceLinesAllFinalDischargeLocationId3 | — |
| FINAL_MATCH_FLAG | ApInvoiceLinesAllFinalMatchFlag2 | ✅ |
| FOS_XFACE_FLAG | ApInvoiceLinesAllFosXfaceFlag | — |
| FUNDS_STATUS | ApInvoiceLinesAllFundsStatus5 | ✅ |
| GENERATE_DISTS | ApInvoiceLinesAllGenerateDists | — |
| GLOBAL_ATTRIBUTE1 | ApInvoiceLinesAllGlobalAttribute116 | — |
| GLOBAL_ATTRIBUTE10 | ApInvoiceLinesAllGlobalAttribute104 | — |
| GLOBAL_ATTRIBUTE11 | ApInvoiceLinesAllGlobalAttribute117 | — |
| GLOBAL_ATTRIBUTE12 | ApInvoiceLinesAllGlobalAttribute124 | — |
| GLOBAL_ATTRIBUTE13 | ApInvoiceLinesAllGlobalAttribute134 | — |
| GLOBAL_ATTRIBUTE14 | ApInvoiceLinesAllGlobalAttribute144 | — |
| GLOBAL_ATTRIBUTE15 | ApInvoiceLinesAllGlobalAttribute154 | — |
| GLOBAL_ATTRIBUTE16 | ApInvoiceLinesAllGlobalAttribute164 | — |
| GLOBAL_ATTRIBUTE17 | ApInvoiceLinesAllGlobalAttribute174 | — |
| GLOBAL_ATTRIBUTE18 | ApInvoiceLinesAllGlobalAttribute184 | — |
| GLOBAL_ATTRIBUTE19 | ApInvoiceLinesAllGlobalAttribute194 | — |
| GLOBAL_ATTRIBUTE2 | ApInvoiceLinesAllGlobalAttribute24 | — |
| GLOBAL_ATTRIBUTE20 | ApInvoiceLinesAllGlobalAttribute204 | — |
| GLOBAL_ATTRIBUTE3 | ApInvoiceLinesAllGlobalAttribute34 | — |
| GLOBAL_ATTRIBUTE4 | ApInvoiceLinesAllGlobalAttribute44 | — |
| GLOBAL_ATTRIBUTE5 | ApInvoiceLinesAllGlobalAttribute54 | — |
| GLOBAL_ATTRIBUTE6 | ApInvoiceLinesAllGlobalAttribute64 | — |
| GLOBAL_ATTRIBUTE7 | ApInvoiceLinesAllGlobalAttribute74 | — |
| GLOBAL_ATTRIBUTE8 | ApInvoiceLinesAllGlobalAttribute84 | — |
| GLOBAL_ATTRIBUTE9 | ApInvoiceLinesAllGlobalAttribute94 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ApInvoiceLinesAllGlobalAttributeCategory4 | — |
| GLOBAL_ATTRIBUTE_DATE1 | ApInvoiceLinesAllGlobalAttributeDate11 | — |
| GLOBAL_ATTRIBUTE_DATE2 | ApInvoiceLinesAllGlobalAttributeDate21 | — |
| GLOBAL_ATTRIBUTE_DATE3 | ApInvoiceLinesAllGlobalAttributeDate31 | — |
| GLOBAL_ATTRIBUTE_DATE4 | ApInvoiceLinesAllGlobalAttributeDate41 | — |
| GLOBAL_ATTRIBUTE_DATE5 | ApInvoiceLinesAllGlobalAttributeDate51 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | ApInvoiceLinesAllGlobalAttributeNumber11 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | ApInvoiceLinesAllGlobalAttributeNumber21 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | ApInvoiceLinesAllGlobalAttributeNumber31 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | ApInvoiceLinesAllGlobalAttributeNumber41 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | ApInvoiceLinesAllGlobalAttributeNumber51 | — |
| HISTORICAL_FLAG | ApInvoiceLinesAllHistoricalFlag1 | — |
| INCLUDED_TAX_AMOUNT | ApInvoiceLinesAllIncludedTaxAmount | — |
| INCOME_TAX_REGION | ApInvoiceLinesAllIncomeTaxRegion | ✅ |
| INTENDED_USE_CLASSIF_ID | ApInvoiceLinesAllIntendedUseClassifId1 | — |
| INVENTORY_ITEM_ID | ApInvoiceLinesAllInventoryItemId2 | — |
| INVOICE_ID | ApInvoiceLinesAllInvoiceId2 | — |
| INVOICE_INCLUDES_PREPAY_FLAG | ApInvoiceLinesAllInvoiceIncludesPrepayFlag | ✅ |
| ITEM_DESCRIPTION | ApInvoiceLinesAllItemDescription3 | — |
| JUSTIFICATION | ApInvoiceLinesAllJustification | — |
| LAST_UPDATE_DATE | ApInvoiceLinesAllLastUpdateDate11 | ✅ |
| LAST_UPDATE_LOGIN | ApInvoiceLinesAllLastUpdateLogin11 | — |
| LAST_UPDATED_BY | ApInvoiceLinesAllLastUpdatedBy11 | — |
| LCM_ENABLED_FLAG | ApInvoiceLinesAllLcmEnabledFlag1 | — |
| LINE_GROUP_NUMBER | ApInvoiceLinesAllLineGroupNumber | ✅ |
| LINE_NUMBER | ApInvoiceLinesAllLineNumber2 | ✅ |
| LINE_OWNER_ROLE | ApInvoiceLinesAllLineOwnerRole | — |
| LINE_SELECTED_FOR_APPL_FLAG | ApInvoiceLinesAllLineSelectedForApplFlag | — |
| LINE_SELECTED_FOR_RELEASE_FLAG | ApInvoiceLinesAllLineSelectedForReleaseFlag | — |
| LINE_SOURCE | ApInvoiceLinesAllLineSource | — |
| LINE_TYPE_LOOKUP_CODE | ApInvoiceLinesAllLineTypeLookupCode | ✅ |
| MANUFACTURER | ApInvoiceLinesAllManufacturer | ✅ |
| MATCH_TYPE | ApInvoiceLinesAllMatchType | ✅ |
| MERCHANT_DOCUMENT_NUMBER | ApInvoiceLinesAllMerchantDocumentNumber | — |
| MERCHANT_NAME | ApInvoiceLinesAllMerchantName | — |
| MERCHANT_REFERENCE | ApInvoiceLinesAllMerchantReference | — |
| MERCHANT_TAX_REG_NUMBER | ApInvoiceLinesAllMerchantTaxRegNumber | — |
| MERCHANT_TAXPAYER_ID | ApInvoiceLinesAllMerchantTaxpayerId | — |
| MODEL_NUMBER | ApInvoiceLinesAllModelNumber | ✅ |
| OBJECT_VERSION_NUMBER | ApInvoiceLinesAllObjectVersionNumber8 | — |
| ORG_ID | ApInvoiceLinesAllOrgId1 | — |
| ORIGINAL_AMOUNT | ApInvoiceLinesAllOriginalAmount | — |
| ORIGINAL_BASE_AMOUNT | ApInvoiceLinesAllOriginalBaseAmount | — |
| ORIGINAL_ROUNDING_AMT | ApInvoiceLinesAllOriginalRoundingAmt | — |
| OVERLAY_DIST_CODE_CONCAT | ApInvoiceLinesAllOverlayDistCodeConcat | — |
| PA_CC_AR_INVOICE_ID | ApInvoiceLinesAllPaCcArInvoiceId | — |
| PA_CC_AR_INVOICE_LINE_NUM | ApInvoiceLinesAllPaCcArInvoiceLineNum | ✅ |
| PA_CC_PROCESSED_CODE | ApInvoiceLinesAllPaCcProcessedCode | ✅ |
| PA_QUANTITY | ApInvoiceLinesAllPaQuantity1 | — |
| PERIOD_NAME | ApInvoiceLinesAllPeriodName | ✅ |
| PJC_BILLABLE_FLAG | ApInvoiceLinesAllPjcBillableFlag | — |
| PJC_CAPITALIZABLE_FLAG | ApInvoiceLinesAllPjcCapitalizableFlag | — |
| PJC_CONTEXT_CATEGORY | ApInvoiceLinesAllPjcContextCategory | — |
| PJC_CONTRACT_ID | ApInvoiceLinesAllPjcContractId | — |
| PJC_CONTRACT_LINE_ID | ApInvoiceLinesAllPjcContractLineId | — |
| PJC_EXPENDITURE_ITEM_DATE | ApInvoiceLinesAllPjcExpenditureItemDate | ✅ |
| PJC_EXPENDITURE_TYPE_ID | ApInvoiceLinesAllPjcExpenditureTypeId | — |
| PJC_FUNDING_ALLOCATION_ID | ApInvoiceLinesAllPjcFundingAllocationId | — |
| PJC_ORGANIZATION_ID | ApInvoiceLinesAllPjcOrganizationId | — |
| PJC_PROJECT_ID | ApInvoiceLinesAllPjcProjectId | — |
| PJC_RESERVED_ATTRIBUTE1 | ApInvoiceLinesAllPjcReservedAttribute1 | — |
| PJC_RESERVED_ATTRIBUTE10 | ApInvoiceLinesAllPjcReservedAttribute10 | — |
| PJC_RESERVED_ATTRIBUTE2 | ApInvoiceLinesAllPjcReservedAttribute2 | — |
| PJC_RESERVED_ATTRIBUTE3 | ApInvoiceLinesAllPjcReservedAttribute3 | — |
| PJC_RESERVED_ATTRIBUTE4 | ApInvoiceLinesAllPjcReservedAttribute4 | — |
| PJC_RESERVED_ATTRIBUTE5 | ApInvoiceLinesAllPjcReservedAttribute5 | — |
| PJC_RESERVED_ATTRIBUTE6 | ApInvoiceLinesAllPjcReservedAttribute6 | — |
| PJC_RESERVED_ATTRIBUTE7 | ApInvoiceLinesAllPjcReservedAttribute7 | — |
| PJC_RESERVED_ATTRIBUTE8 | ApInvoiceLinesAllPjcReservedAttribute8 | — |
| PJC_RESERVED_ATTRIBUTE9 | ApInvoiceLinesAllPjcReservedAttribute9 | — |
| PJC_TASK_ID | ApInvoiceLinesAllPjcTaskId | — |
| PJC_USER_DEF_ATTRIBUTE1 | ApInvoiceLinesAllPjcUserDefAttribute1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | ApInvoiceLinesAllPjcUserDefAttribute10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | ApInvoiceLinesAllPjcUserDefAttribute2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | ApInvoiceLinesAllPjcUserDefAttribute3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | ApInvoiceLinesAllPjcUserDefAttribute4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | ApInvoiceLinesAllPjcUserDefAttribute5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | ApInvoiceLinesAllPjcUserDefAttribute6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | ApInvoiceLinesAllPjcUserDefAttribute7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | ApInvoiceLinesAllPjcUserDefAttribute8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | ApInvoiceLinesAllPjcUserDefAttribute9 | — |
| PJC_WORK_TYPE_ID | ApInvoiceLinesAllPjcWorkTypeId | — |
| PO_DISTRIBUTION_ID | ApInvoiceLinesAllPoDistributionId4 | — |
| PO_HEADER_ID | ApInvoiceLinesAllPoHeaderId7 | — |
| PO_LINE_ID | ApInvoiceLinesAllPoLineId5 | — |
| PO_LINE_LOCATION_ID | ApInvoiceLinesAllPoLineLocationId4 | — |
| PO_RELEASE_ID | ApInvoiceLinesAllPoReleaseId | — |
| PREPAY_APPL_REQUEST_ID | ApInvoiceLinesAllPrepayApplRequestId | — |
| PREPAY_INVOICE_ID | ApInvoiceLinesAllPrepayInvoiceId | — |
| PREPAY_LINE_NUMBER | ApInvoiceLinesAllPrepayLineNumber | ✅ |
| PRIMARY_INTENDED_USE | ApInvoiceLinesAllPrimaryIntendedUse | ✅ |
| PROD_FC_CATEG_ID | ApInvoiceLinesAllProdFcCategId | — |
| PRODUCT_CATEGORY | ApInvoiceLinesAllProductCategory3 | ✅ |
| PRODUCT_FISC_CLASSIFICATION | ApInvoiceLinesAllProductFiscClassification1 | ✅ |
| PRODUCT_TABLE | ApInvoiceLinesAllProductTable1 | — |
| PRODUCT_TYPE | ApInvoiceLinesAllProductType3 | ✅ |
| PROGRAM_APPLICATION_ID | ApInvoiceLinesAllProgramApplicationId | — |
| PROGRAM_ID | ApInvoiceLinesAllProgramId | — |
| PROGRAM_UPDATE_DATE | ApInvoiceLinesAllProgramUpdateDate | — |
| PROJECT_ID | ApInvoiceLinesAllProjectId2 | — |
| PRORATE_ACROSS_ALL_ITEMS | ApInvoiceLinesAllProrateAcrossAllItems | ✅ |
| PURCHASING_CATEGORY_ID | ApInvoiceLinesAllPurchasingCategoryId | — |
| QUANTITY_INVOICED | ApInvoiceLinesAllQuantityInvoiced | ✅ |
| RCV_SHIPMENT_LINE_ID | ApInvoiceLinesAllRcvShipmentLineId | — |
| RCV_TRANSACTION_ID | ApInvoiceLinesAllRcvTransactionId1 | — |
| RECEIPT_CONVERSION_RATE | ApInvoiceLinesAllReceiptConversionRate | — |
| RECEIPT_CURRENCY_AMOUNT | ApInvoiceLinesAllReceiptCurrencyAmount | — |
| RECEIPT_CURRENCY_CODE | ApInvoiceLinesAllReceiptCurrencyCode | — |
| RECEIPT_MISSING_FLAG | ApInvoiceLinesAllReceiptMissingFlag | — |
| RECEIPT_REQUIRED_FLAG | ApInvoiceLinesAllReceiptRequiredFlag1 | — |
| RECEIPT_VERIFIED_FLAG | ApInvoiceLinesAllReceiptVerifiedFlag | — |
| REFERENCE_1 | ApInvoiceLinesAllReference11 | — |
| REFERENCE_2 | ApInvoiceLinesAllReference21 | — |
| REFERENCE_KEY1 | ApInvoiceLinesAllReferenceKey11 | — |
| REFERENCE_KEY2 | ApInvoiceLinesAllReferenceKey21 | — |
| REFERENCE_KEY3 | ApInvoiceLinesAllReferenceKey31 | — |
| REFERENCE_KEY4 | ApInvoiceLinesAllReferenceKey41 | — |
| REFERENCE_KEY5 | ApInvoiceLinesAllReferenceKey51 | — |
| REQUEST_ID | ApInvoiceLinesAllRequestId11 | — |
| REQUESTER_ID | ApInvoiceLinesAllRequesterId1 | — |
| RETAINED_AMOUNT | ApInvoiceLinesAllRetainedAmount | — |
| RETAINED_AMOUNT_REMAINING | ApInvoiceLinesAllRetainedAmountRemaining | — |
| RETAINED_INVOICE_ID | ApInvoiceLinesAllRetainedInvoiceId | — |
| RETAINED_LINE_NUMBER | ApInvoiceLinesAllRetainedLineNumber | — |
| ROUNDING_AMT | ApInvoiceLinesAllRoundingAmt | — |
| SERIAL_NUMBER | ApInvoiceLinesAllSerialNumber | ✅ |
| SET_OF_BOOKS_ID | ApInvoiceLinesAllSetOfBooksId2 | — |
| SHIP_FROM_LOCATION_ID | ApInvoiceLinesAllShipFromLocationId3 | — |
| SHIP_TO_LOCATION_ID | ApInvoiceLinesAllShipToLocationId4 | — |
| SOURCE_APPLICATION_ID | ApInvoiceLinesAllSourceApplicationId | — |
| SOURCE_ENTITY_CODE | ApInvoiceLinesAllSourceEntityCode | — |
| SOURCE_EVENT_CLASS_CODE | ApInvoiceLinesAllSourceEventClassCode | — |
| SOURCE_LINE_ID | ApInvoiceLinesAllSourceLineId | — |
| SOURCE_TRX_ID | ApInvoiceLinesAllSourceTrxId | — |
| SOURCE_TRX_LEVEL_TYPE | ApInvoiceLinesAllSourceTrxLevelType | — |
| START_EXPENSE_DATE | ApInvoiceLinesAllStartExpenseDate | — |
| STAT_AMOUNT | ApInvoiceLinesAllStatAmount | — |
| SUMMARY_TAX_LINE_ID | ApInvoiceLinesAllSummaryTaxLineId | — |
| TASK_ID | ApInvoiceLinesAllTaskId2 | — |
| TAX | ApInvoiceLinesAllTax | ✅ |
| TAX_ALREADY_CALCULATED_FLAG | ApInvoiceLinesAllTaxAlreadyCalculatedFlag | ✅ |
| TAX_CLASSIFICATION_CODE | ApInvoiceLinesAllTaxClassificationCode2 | ✅ |
| TAX_CODE_ID | ApInvoiceLinesAllTaxCodeId2 | — |
| TAX_JURISDICTION_CODE | ApInvoiceLinesAllTaxJurisdictionCode | ✅ |
| TAX_RATE | ApInvoiceLinesAllTaxRate | ✅ |
| TAX_RATE_CODE | ApInvoiceLinesAllTaxRateCode | ✅ |
| TAX_RATE_ID | ApInvoiceLinesAllTaxRateId | — |
| TAX_REGIME_CODE | ApInvoiceLinesAllTaxRegimeCode | ✅ |
| TAX_STATUS_CODE | ApInvoiceLinesAllTaxStatusCode | ✅ |
| TOTAL_NREC_TAX_AMOUNT | ApInvoiceLinesAllTotalNrecTaxAmount | — |
| TOTAL_NREC_TAX_AMT_FUNCL_CURR | ApInvoiceLinesAllTotalNrecTaxAmtFunclCurr | — |
| TOTAL_REC_TAX_AMOUNT | ApInvoiceLinesAllTotalRecTaxAmount | — |
| TOTAL_REC_TAX_AMT_FUNCL_CURR | ApInvoiceLinesAllTotalRecTaxAmtFunclCurr | — |
| TRX_BUSINESS_CATEGORY | ApInvoiceLinesAllTrxBusinessCategory4 | ✅ |
| TYPE_1099 | ApInvoiceLinesAllType10991 | ✅ |
| UNIT_MEAS_LOOKUP_CODE | ApInvoiceLinesAllUnitMeasLookupCode | — |
| UNIT_PRICE | ApInvoiceLinesAllUnitPrice1 | ✅ |
| USER_DEFINED_FISC_CLASS | ApInvoiceLinesAllUserDefinedFiscClass4 | — |
| USSGL_TRANSACTION_CODE | ApInvoiceLinesAllUssglTransactionCode1 | — |
| WARRANTY_NUMBER | ApInvoiceLinesAllWarrantyNumber | ✅ |
| WEB_PARAMETER_ID | ApInvoiceLinesAllWebParameterId | — |
| WFAPPROVAL_STATUS | ApInvoiceLinesAllWfapprovalStatus1 | — |

### [[transactioneventpvo|TransactionEventPVO]] (OTHER · BICC: 14/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSESSABLE_VALUE | ApInvoiceLinesAllAssessableValue | ✅ |
| CONTROL_AMOUNT | ApInvoiceLinesAllControlAmount | ✅ |
| INVOICE_ID | ApInvoiceLinesAllInvoiceId | ✅ |
| LINE_NUMBER | ApInvoiceLinesAllLineNumber | ✅ |
| OBJECT_VERSION_NUMBER | ApInvoiceLinesAllObjectVersionNumber | ✅ |
| PRIMARY_INTENDED_USE | ApInvoiceLinesAllPrimaryIntendedUse | ✅ |
| PRODUCT_CATEGORY | ApInvoiceLinesAllProductCategory | ✅ |
| PRODUCT_FISC_CLASSIFICATION | ApInvoiceLinesAllProductFiscClassification | ✅ |
| PRODUCT_TYPE | ApInvoiceLinesAllProductType | ✅ |
| SHIP_FROM_LOCATION_ID | ApInvoiceLinesAllShipFromLocationId | ✅ |
| SHIP_TO_LOCATION_ID | ApInvoiceLinesAllShipToLocationId | ✅ |
| TAX_CLASSIFICATION_CODE | ApInvoiceLinesAllTaxClassificationCode | ✅ |
| TRX_BUSINESS_CATEGORY | ApInvoiceLinesAllTrxBusinessCategory | ✅ |
| USER_DEFINED_FISC_CLASS | ApInvoiceLinesAllUserDefinedFiscClass | ✅ |

---

## 📚 Referências

- [Oracle Docs — AP_INVOICE_LINES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/apinvoicelinesall-10010.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
