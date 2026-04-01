---
id: DOC-AP-011
doc_type: system-doc
title: "AP_INVOICES_ALL — Faturas de Fornecedores (Invoices)"
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
  - faturas
  - invoices
  - ap-invoices
aliases:
  - AP_INVOICES_ALL
  - ap_invoices_all
  - faturas-ap
  - invoices-ap
  - faturas-fornecedores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_INVOICES_ALL

## 📌 Visão Geral

Armazena um registro para **cada fatura** (invoice) do módulo Accounts Payable. Cada linha representa uma fatura individual recebida de fornecedores, contendo número, valor, moeda, data, tipo (Standard, Credit Memo, Debit Memo, Prepayment, Mixed), status de validação e referência ao fornecedor emissor. É a tabela central do módulo AP e ponto de partida para todo o fluxo de contas a pagar — da entrada até o pagamento.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de faturas:** Cada fatura de fornecedor gera um registro, seja entrada manual, importação via interface, OCR ou EDI.
- **Validação e aprovação:** Controle do status de validação (Validated, Needs Revalidation, Never Validated) e workflow de aprovação.
- **Contabilização:** Base para geração de lançamentos contábeis no General Ledger via Subledger Accounting.
- **Pagamentos:** Faturas validadas e aprovadas tornam-se elegíveis para seleção de pagamento.
- **Conciliação:** Vinculação de faturas a pedidos de compra (PO) e recebimentos para three-way matching.
- **Auditoria e compliance:** Rastreabilidade completa com sequência de documento, WHO columns e histórico de aprovação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INVOICE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da fatura | — | 🟢 100% |
| 2 | INVOICE_NUM | VARCHAR2(50) | NOT NULL | Identificação | Número da fatura do fornecedor | — | 🟢 100% |
| 3 | INVOICE_TYPE_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Classificação | Tipo da fatura (STANDARD/CREDIT/DEBIT/PREPAYMENT/MIXED) | [[ap_lookup_codes]] | 🟢 100% |
| 4 | INVOICE_DATE | DATE | NOT NULL | Data | Data da fatura | — | 🟢 100% |
| 5 | VENDOR_ID | NUMBER(18) | NOT NULL | Fornecedor | Identificador do fornecedor | [[poz_suppliers]] | 🟢 100% |
| 6 | VENDOR_SITE_ID | NUMBER(18) | NOT NULL | Fornecedor | Site do fornecedor | [[poz_supplier_sites_all_m]] | 🟢 100% |
| 7 | INVOICE_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor total da fatura na moeda da transação | — | 🟢 100% |
| 8 | INVOICE_CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Financeiro | Código da moeda da fatura (ISO 4217) | — | 🟢 100% |
| 9 | PAYMENT_CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda de pagamento | — | 🟢 100% |
| 10 | EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio | [[gl_daily_conversion_types]] | 🟢 100% |
| 11 | EXCHANGE_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio aplicada | — | 🟢 100% |
| 12 | EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 100% |
| 13 | TERMS_ID | NUMBER(18) | NULL | Condições | Condição de pagamento | [[ap_terms_b]] | 🟢 100% |
| 14 | TERMS_DATE | DATE | NULL | Condições | Data-base para cálculo de vencimento | — | 🟢 100% |
| 15 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição da fatura | — | 🟢 100% |
| 16 | SOURCE | VARCHAR2(80) | NULL | Classificação | Origem da fatura (ex: Manual, ScanSnap, ERS) | — | 🟢 100% |
| 17 | PAYMENT_METHOD_CODE | VARCHAR2(30) | NULL | Pagamento | Método de pagamento (CHECK/EFT/WIRE) | [[iby_payment_methods_b]] | 🟢 100% |
| 18 | PAY_GROUP_LOOKUP_CODE | VARCHAR2(25) | NULL | Pagamento | Grupo de pagamento | [[ap_lookup_codes]] | 🟢 100% |
| 19 | GL_DATE | DATE | NULL | Contabilidade | Data contábil (General Ledger) | — | 🟢 100% |
| 20 | ACCTS_PAY_CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Conta contábil de AP (liability) | [[gl_code_combinations]] | 🟢 100% |
| 21 | PAYMENT_STATUS_FLAG | VARCHAR2(1) | NULL | Status | Status do pagamento (Y=pago/N=pendente/P=parcial) | — | 🟢 100% |
| 22 | APPROVAL_STATUS | VARCHAR2(25) | NULL | Status | Status de aprovação (APPROVED/REJECTED/INITIATED/etc.) | — | 🟢 100% |
| 23 | WFAPPROVAL_STATUS | VARCHAR2(50) | NULL | Status | Status do workflow de aprovação | — | 🟢 100% |
| 24 | CANCELLED_DATE | DATE | NULL | Status | Data de cancelamento da fatura | — | 🟢 100% |
| 25 | CANCELLED_BY | NUMBER(18) | NULL | Status | Usuário que cancelou | — | 🟢 100% |
| 26 | AMOUNT_PAID | NUMBER | NULL | Financeiro | Valor total já pago | — | 🟢 100% |
| 27 | DISCOUNT_AMOUNT_TAKEN | NUMBER | NULL | Financeiro | Desconto financeiro obtido | — | 🟢 100% |
| 28 | BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda funcional (ledger) | — | 🟢 100% |
| 29 | DOC_SEQUENCE_ID | NUMBER(18) | NULL | Identificação | ID da sequência de documento | [[fnd_document_sequences]] | 🟢 100% |
| 30 | DOC_SEQUENCE_VALUE | NUMBER(15) | NULL | Identificação | Número de sequência de documento legal | — | 🟢 100% |
| 31 | PO_HEADER_ID | NUMBER(18) | NULL | Referência cruzada | Pedido de compra vinculado (quick match) | [[po_headers_all]] | 🟢 100% |
| 32 | PARTY_ID | NUMBER(18) | NULL | Fornecedor | Trading Community party do fornecedor | [[hz_parties]] | 🟢 100% |
| 33 | PARTY_SITE_ID | NUMBER(18) | NULL | Fornecedor | Party site do fornecedor | [[hz_party_sites]] | 🟢 100% |
| 34 | LEGAL_ENTITY_ID | NUMBER(18) | NULL | Multi-Org | Entidade legal | [[xle_entity_profiles]] | 🟢 100% |
| 35 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 36 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 37 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 38 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 39 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 40 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 41 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 42 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 43 | GLOBAL_ATTRIBUTE1–20 | VARCHAR2(150) | NULL | DFF | Atributos globais (localizações por país) | — | 🟢 100% |
| 44 | GLOBAL_ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Global Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor emissor da fatura)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor)
- [[hz_parties]] — via `PARTY_ID` (trading community party)
- [[hz_party_sites]] — via `PARTY_SITE_ID` (endereço do fornecedor na fatura)
- [[ap_terms_b]] — via `TERMS_ID` (condição de pagamento)
- [[iby_payment_methods_b]] — via `PAYMENT_METHOD_CODE` (método de pagamento)
- [[gl_code_combinations]] — via `ACCTS_PAY_CODE_COMBINATION_ID` (conta contábil padrão de contas a pagar)
- [[gl_daily_conversion_types]] — via `EXCHANGE_RATE_TYPE` (tipo de câmbio usado na conversão da fatura)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit proprietária da fatura)
- [[xle_entity_profiles]] — via `LEGAL_ENTITY_ID` (entidade legal responsável pela fatura)

### Tabelas-filha (FK de saída)
- [[ap_invoice_lines_all]] — via `INVOICE_ID` (linhas da fatura)
- [[ap_invoice_distributions_all]] — via `INVOICE_ID` (distribuições contábeis)
- [[ap_invoice_payments_all]] — via `INVOICE_ID` (pagamentos da fatura)
- [[ap_payment_schedules_all]] — via `INVOICE_ID` (parcelas/vencimentos)
- [[ap_inv_aprvl_hist_all]] — via `INVOICE_ID` (histórico de aprovação)

---

## 📎 Uso Típico

### Listar faturas pendentes de pagamento
```sql
SELECT ai.INVOICE_NUM, ai.INVOICE_DATE, ai.INVOICE_AMOUNT,
       ai.INVOICE_CURRENCY_CODE, ai.PAYMENT_STATUS_FLAG
FROM   AP_INVOICES_ALL ai
WHERE  ai.PAYMENT_STATUS_FLAG = 'N'
  AND  ai.CANCELLED_DATE IS NULL
  AND  ai.ORG_ID = :p_org_id;
```

### Faturas com dados do fornecedor
```sql
SELECT ai.INVOICE_NUM, ai.INVOICE_AMOUNT, ai.INVOICE_DATE,
       ps.VENDOR_NAME, ps.SEGMENT1 AS vendor_number
FROM   AP_INVOICES_ALL ai
JOIN   POZ_SUPPLIERS ps ON ps.VENDOR_ID = ai.VENDOR_ID
WHERE  ai.INVOICE_DATE BETWEEN :start_date AND :end_date
  AND  ai.ORG_ID = :p_org_id;
```

### Filtros comuns
- `INVOICE_TYPE_LOOKUP_CODE = 'STANDARD'` — Faturas padrão
- `PAYMENT_STATUS_FLAG = 'N'` — Faturas não pagas
- `CANCELLED_DATE IS NULL` — Exclui canceladas
- `WFAPPROVAL_STATUS = 'WFAPPROVED'` — Aprovadas no workflow

---

## 🔒 Observações

- O campo `INVOICE_TYPE_LOOKUP_CODE` determina o tipo: **STANDARD** (fatura normal), **CREDIT** (nota de crédito), **DEBIT** (nota de débito), **PREPAYMENT** (adiantamento), **MIXED** (misto).
- O status de pagamento é controlado por `PAYMENT_STATUS_FLAG`: **Y** (totalmente pago), **N** (não pago), **P** (parcialmente pago).
- A validação da fatura é pré-requisito para pagamento; faturas inválidas não aparecem na seleção de pagamento.
- Campos `CANCELLED_*` são preenchidos apenas quando a fatura é cancelada; faturas canceladas não podem ser pagas.
- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.
- O campo `SOURCE` indica a origem da fatura e é importante para rastreabilidade de integrações.

---

## 🔗 PVOs Relacionados

### [[costaccountingtransactionspvo|CostAccountingTransactionsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INVOICE_CURRENCY_CODE | InvoiceHeaderPEOInvoiceCurrencyCode | — |
| INVOICE_ID | InvoiceHeaderPEOInvoiceId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |

### [[costaccountingtransactionsrefpvo|CostAccountingTransactionsRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INVOICE_CURRENCY_CODE | InvoiceHeaderPEOInvoiceCurrencyCode | — |
| INVOICE_ID | InvoiceHeaderPEOInvoiceId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER · BICC: 4/133)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTS_PAY_CODE_COMBINATION_ID | InvoiceAcctsPayCodeCombinationId | — |
| AMOUNT_APPLICABLE_TO_DISCOUNT | InvoiceAmountApplicableToDiscount | — |
| AMOUNT_PAID | InvoiceAmountPaid | — |
| AMT_DUE_CCARD_COMPANY | InvoiceAmtDueCcardCompany | — |
| AMT_DUE_EMPLOYEE | InvoiceAmtDueEmployee | — |
| APPLICATION_ID | InvoiceApplicationId | — |
| APPROVAL_DESCRIPTION | InvoiceApprovalDescription | — |
| APPROVAL_ITERATION | InvoiceApprovalIteration | — |
| APPROVAL_READY_FLAG | InvoiceApprovalReadyFlag | — |
| APPROVAL_STATUS | InvoiceApprovalStatus | — |
| APPROVED_AMOUNT | InvoiceApprovedAmount | — |
| AWARD_ID | InvoiceAwardId | — |
| AWT_FLAG | InvoiceAwtFlag | — |
| AWT_GROUP_ID | InvoiceAwtGroupId | — |
| BANK_CHARGE_BEARER | InvoiceBankChargeBearer | — |
| BASE_AMOUNT | InvoiceBaseAmount | — |
| BATCH_ID | InvoiceBatchId | — |
| CANCELLED_AMOUNT | InvoiceCancelledAmount | — |
| CANCELLED_BY | InvoiceCancelledBy | — |
| CANCELLED_DATE | InvoiceCancelledDate | — |
| CONTROL_AMOUNT | InvoiceControlAmount | — |
| CREATED_BY | InvoiceCreatedBy | — |
| CREATION_DATE | InvoiceCreationDate | — |
| CREDITED_INVOICE_ID | InvoiceCreditedInvoiceId | — |
| CUST_REGISTRATION_CODE | InvoiceCustRegistrationCode | — |
| CUST_REGISTRATION_NUMBER | InvoiceCustRegistrationNumber | — |
| DELIVERY_CHANNEL_CODE | InvoiceDeliveryChannelCode | — |
| DESCRIPTION | InvoiceDescription | — |
| DISC_IS_INV_LESS_TAX_FLAG | InvoiceDiscIsInvLessTaxFlag | — |
| DISCOUNT_AMOUNT_TAKEN | InvoiceDiscountAmountTaken | — |
| DISTRIBUTION_SET_ID | InvoiceDistributionSetId | — |
| DOC_CATEGORY_CODE | InvoiceDocCategoryCode | — |
| DOC_SEQUENCE_ID | InvoiceDocSequenceId | — |
| DOC_SEQUENCE_VALUE | InvoiceDocSequenceValue | — |
| DOCUMENT_SUB_TYPE | InvoiceDocumentSubType | — |
| EARLIEST_SETTLEMENT_DATE | InvoiceEarliestSettlementDate | — |
| EXCHANGE_DATE | InvoiceExchangeDate | — |
| EXCHANGE_RATE | InvoiceExchangeRate | — |
| EXCHANGE_RATE_TYPE | InvoiceExchangeRateType | — |
| EXCLUDE_FREIGHT_FROM_DISCOUNT | InvoiceExcludeFreightFromDiscount | — |
| EXCLUSIVE_PAYMENT_FLAG | InvoiceExclusivePaymentFlag | — |
| EXTERNAL_BANK_ACCOUNT_ID | InvoiceExternalBankAccountId | — |
| FORCE_REVALIDATION_FLAG | InvoiceForceRevalidationFlag | — |
| FREIGHT_AMOUNT | InvoiceFreightAmount | — |
| GL_DATE | InvoiceGlDate | — |
| GOODS_RECEIVED_DATE | InvoiceGoodsReceivedDate | — |
| HISTORICAL_FLAG | InvoiceHistoricalFlag | — |
| INTERCOMPANY_FLAG | InvoiceIntercompanyFlag | — |
| INTERNAL_CONTACT_EMAIL | InvoiceInternalContactEmail | — |
| INVOICE_AMOUNT | InvoiceInvoiceAmount | — |
| INVOICE_CURRENCY_CODE | InvoiceInvoiceCurrencyCode | — |
| INVOICE_DATE | InvoiceInvoiceDate | ✅ |
| INVOICE_ID | InvoiceInvoiceId | — |
| INVOICE_NUM | InvoiceInvoiceNum | ✅ |
| INVOICE_RECEIVED_DATE | InvoiceInvoiceReceivedDate | — |
| INVOICE_TYPE_LOOKUP_CODE | InvoiceInvoiceTypeLookupCode | — |
| LAST_UPDATE_DATE | InvoiceLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvoiceLastUpdateLogin | — |
| LAST_UPDATED_BY | InvoiceLastUpdatedBy | — |
| LEGAL_ENTITY_ID | InvoiceLegalEntityId | — |
| MRC_BASE_AMOUNT | InvoiceMrcBaseAmount | — |
| MRC_EXCHANGE_DATE | InvoiceMrcExchangeDate | — |
| MRC_EXCHANGE_RATE | InvoiceMrcExchangeRate | — |
| MRC_EXCHANGE_RATE_TYPE | InvoiceMrcExchangeRateType | — |
| MRC_POSTING_STATUS | InvoiceMrcPostingStatus | — |
| NET_OF_RETAINAGE_FLAG | InvoiceNetOfRetainageFlag | — |
| OBJECT_VERSION_NUMBER | InvoiceObjectVersionNumber | — |
| ORG_ID | InvoiceOrgId | — |
| PAID_ON_BEHALF_EMPLOYEE_ID | InvoicePaidOnBehalfEmployeeId | — |
| PARTY_ID | InvoicePartyId | — |
| PARTY_SITE_ID | InvoicePartySiteId | — |
| PAY_CURR_INVOICE_AMOUNT | InvoicePayCurrInvoiceAmount | — |
| PAY_GROUP_LOOKUP_CODE | InvoicePayGroupLookupCode | — |
| PAY_PROC_TRXN_TYPE_CODE | InvoicePayProcTrxnTypeCode | — |
| PAYMENT_AMOUNT_TOTAL | InvoicePaymentAmountTotal | — |
| PAYMENT_CROSS_RATE | InvoicePaymentCrossRate | — |
| PAYMENT_CROSS_RATE_DATE | InvoicePaymentCrossRateDate | — |
| PAYMENT_CROSS_RATE_TYPE | InvoicePaymentCrossRateType | — |
| PAYMENT_CURRENCY_CODE | InvoicePaymentCurrencyCode | — |
| PAYMENT_FUNCTION | InvoicePaymentFunction | — |
| PAYMENT_METHOD_CODE | InvoicePaymentMethodCode | — |
| PAYMENT_METHOD_LOOKUP_CODE | InvoicePaymentMethodLookupCode | — |
| PAYMENT_REASON_CODE | InvoicePaymentReasonCode | — |
| PAYMENT_REASON_COMMENTS | InvoicePaymentReasonComments | — |
| PAYMENT_STATUS_FLAG | InvoicePaymentStatusFlag | — |
| PO_HEADER_ID | InvoicePoHeaderId | — |
| PORT_OF_ENTRY_CODE | InvoicePortOfEntryCode | — |
| POSTING_STATUS | InvoicePostingStatus | — |
| PRE_WITHHOLDING_AMOUNT | InvoicePreWithholdingAmount | — |
| PRODUCT_TABLE | InvoiceProductTable | — |
| QUICK_CREDIT | InvoiceQuickCredit | — |
| QUICK_PO_HEADER_ID | InvoiceQuickPoHeaderId | — |
| RECURRING_PAYMENT_ID | InvoiceRecurringPaymentId | — |
| REFERENCE_1 | InvoiceReference1 | — |
| REFERENCE_2 | InvoiceReference2 | — |
| REFERENCE_KEY1 | InvoiceReferenceKey1 | — |
| REFERENCE_KEY2 | InvoiceReferenceKey2 | — |
| REFERENCE_KEY3 | InvoiceReferenceKey3 | — |
| REFERENCE_KEY4 | InvoiceReferenceKey4 | — |
| REFERENCE_KEY5 | InvoiceReferenceKey5 | — |
| RELEASE_AMOUNT_NET_OF_TAX | InvoiceReleaseAmountNetOfTax | — |
| REMITTANCE_MESSAGE1 | InvoiceRemittanceMessage1 | — |
| REMITTANCE_MESSAGE2 | InvoiceRemittanceMessage2 | — |
| REMITTANCE_MESSAGE3 | InvoiceRemittanceMessage3 | — |
| REQUESTER_ID | InvoiceRequesterId | — |
| SELF_ASSESSED_TAX_AMOUNT | InvoiceSelfAssessedTaxAmount | — |
| SET_OF_BOOKS_ID | InvoiceSetOfBooksId | ✅ |
| SETTLEMENT_PRIORITY | InvoiceSettlementPriority | — |
| SOURCE | InvoiceSource | — |
| SUPPLIER_TAX_EXCHANGE_RATE | InvoiceSupplierTaxExchangeRate | — |
| SUPPLIER_TAX_INVOICE_DATE | InvoiceSupplierTaxInvoiceDate | — |
| SUPPLIER_TAX_INVOICE_NUMBER | InvoiceSupplierTaxInvoiceNumber | — |
| TAX_INVOICE_INTERNAL_SEQ | InvoiceTaxInvoiceInternalSeq | — |
| TAX_INVOICE_RECORDING_DATE | InvoiceTaxInvoiceRecordingDate | — |
| TAX_RELATED_INVOICE_ID | InvoiceTaxRelatedInvoiceId | — |
| TAXATION_COUNTRY | InvoiceTaxationCountry | — |
| TEMP_CANCELLED_AMOUNT | InvoiceTempCancelledAmount | — |
| TERMS_DATE | InvoiceTermsDate | — |
| TERMS_ID | InvoiceTermsId | — |
| TOTAL_TAX_AMOUNT | InvoiceTotalTaxAmount | — |
| TRX_BUSINESS_CATEGORY | InvoiceTrxBusinessCategory | — |
| UNIQUE_REMITTANCE_IDENTIFIER | InvoiceUniqueRemittanceIdentifier | — |
| URI_CHECK_DIGIT | InvoiceUriCheckDigit | — |
| USER_DEFINED_FISC_CLASS | InvoiceUserDefinedFiscClass | — |
| USSGL_TRANSACTION_CODE | InvoiceUssglTransactionCode | — |
| USSGL_TRX_CODE_CONTEXT | InvoiceUssglTrxCodeContext | — |
| VALIDATED_TAX_AMOUNT | InvoiceValidatedTaxAmount | — |
| VALIDATION_REQUEST_ID | InvoiceValidationRequestId | — |
| VENDOR_CONTACT_ID | InvoiceVendorContactId | — |
| VENDOR_ID | InvoiceVendorId | — |
| VENDOR_SITE_ID | InvoiceVendorSiteId | — |
| VOUCHER_NUM | InvoiceVoucherNum | — |
| WFAPPROVAL_STATUS | InvoiceWfapprovalStatus | — |

### [[fiscaldocheadersp|FiscalDocHeadersP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTS_PAY_CODE_COMBINATION_ID | ApInvoicesAllAcctsPayCodeCombinationId | — |
| AMOUNT_APPLICABLE_TO_DISCOUNT | ApInvoicesAllAmountApplicableToDiscount | — |
| AMOUNT_PAID | ApInvoicesAllAmountPaid | — |
| AMT_DUE_CCARD_COMPANY | ApInvoicesAllAmtDueCcardCompany | — |
| AMT_DUE_EMPLOYEE | ApInvoicesAllAmtDueEmployee | — |
| APPLICATION_ID | ApInvoicesAllApplicationId | — |
| APPROVAL_DESCRIPTION | ApInvoicesAllApprovalDescription | — |
| APPROVAL_ITERATION | ApInvoicesAllApprovalIteration | — |
| APPROVAL_READY_FLAG | ApInvoicesAllApprovalReadyFlag | — |
| APPROVAL_STATUS | ApInvoicesAllApprovalStatus | — |
| APPROVED_AMOUNT | ApInvoicesAllApprovedAmount | — |
| AWARD_ID | ApInvoicesAllAwardId | — |
| AWT_FLAG | ApInvoicesAllAwtFlag | — |
| AWT_GROUP_ID | ApInvoicesAllAwtGroupId | — |
| BANK_CHARGE_BEARER | ApInvoicesAllBankChargeBearer | — |
| BASE_AMOUNT | ApInvoicesAllBaseAmount | — |
| BATCH_ID | ApInvoicesAllBatchId | — |
| BUDGET_DATE | ApInvoicesAllBudgetDate | — |
| CANCELLED_AMOUNT | ApInvoicesAllCancelledAmount | — |
| CANCELLED_BY | ApInvoicesAllCancelledBy | — |
| CANCELLED_DATE | ApInvoicesAllCancelledDate | — |
| CHECK_VAT_AMOUNT_PAID | ApInvoicesAllCheckVatAmountPaid | — |
| CONTROL_AMOUNT | ApInvoicesAllControlAmount | — |
| CORRECTION_PERIOD | ApInvoicesAllCorrectionPeriod | — |
| CORRECTION_YEAR | ApInvoicesAllCorrectionYear | — |
| CREATED_BY | ApInvoicesAllCreatedBy | — |
| CREATION_DATE | ApInvoicesAllCreationDate | — |
| CREDITED_INVOICE_ID | ApInvoicesAllCreditedInvoiceId | — |
| CUST_REGISTRATION_CODE | ApInvoicesAllCustRegistrationCode | — |
| CUST_REGISTRATION_NUMBER | ApInvoicesAllCustRegistrationNumber | — |
| DATA_SET_ID | ApInvoicesAllDataSetId | — |
| DELIVERY_CHANNEL_CODE | ApInvoicesAllDeliveryChannelCode | — |
| DESCRIPTION | ApInvoicesAllDescription | — |
| DISC_IS_INV_LESS_TAX_FLAG | ApInvoicesAllDiscIsInvLessTaxFlag | — |
| DISCOUNT_AMOUNT_TAKEN | ApInvoicesAllDiscountAmountTaken | — |
| DISTRIBUTION_SET_ID | ApInvoicesAllDistributionSetId | — |
| DOC_CATEGORY_CODE | ApInvoicesAllDocCategoryCode | — |
| DOC_SEQUENCE_ID | ApInvoicesAllDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ApInvoicesAllDocSequenceValue | — |
| DOCUMENT_SUB_TYPE | ApInvoicesAllDocumentSubType | — |
| EARLIEST_SETTLEMENT_DATE | ApInvoicesAllEarliestSettlementDate | — |
| EMPLOYEE_ADDRESS_CODE | ApInvoicesAllEmployeeAddressCode | — |
| EXCHANGE_DATE | ApInvoicesAllExchangeDate | — |
| EXCHANGE_RATE | ApInvoicesAllExchangeRate | — |
| EXCHANGE_RATE_TYPE | ApInvoicesAllExchangeRateType | — |
| EXCLUDE_FREIGHT_FROM_DISCOUNT | ApInvoicesAllExcludeFreightFromDiscount | — |
| EXCLUSIVE_PAYMENT_FLAG | ApInvoicesAllExclusivePaymentFlag | — |
| EXPENDITURE_ITEM_DATE | ApInvoicesAllExpenditureItemDate | — |
| EXPENDITURE_ORGANIZATION_ID | ApInvoicesAllExpenditureOrganizationId | — |
| EXPENDITURE_TYPE | ApInvoicesAllExpenditureType | — |
| EXTERNAL_BANK_ACCOUNT_ID | ApInvoicesAllExternalBankAccountId | — |
| FIRST_PARTY_REGISTRATION_ID | ApInvoicesAllFirstPartyRegistrationId | — |
| FISCAL_DOC_ACCESS_KEY | ApInvoicesAllFiscalDocAccessKey | — |
| FORCE_REVALIDATION_FLAG | ApInvoicesAllForceRevalidationFlag | — |
| FREIGHT_AMOUNT | ApInvoicesAllFreightAmount | — |
| FUNDS_STATUS | ApInvoicesAllFundsStatus | — |
| GL_DATE | ApInvoicesAllGlDate | — |
| GOODS_RECEIVED_DATE | ApInvoicesAllGoodsReceivedDate | — |
| HISTORICAL_FLAG | ApInvoicesAllHistoricalFlag | — |
| IMAGE_DOCUMENT_NUM | ApInvoicesAllImageDocumentNum | — |
| IMPORT_DOCUMENT_DATE | ApInvoicesAllImportDocumentDate | — |
| IMPORT_DOCUMENT_NUMBER | ApInvoicesAllImportDocumentNumber | — |
| INTERCOMPANY_FLAG | ApInvoicesAllIntercompanyFlag | — |
| INTERNAL_CONTACT_EMAIL | ApInvoicesAllInternalContactEmail | — |
| INVOICE_AMOUNT | ApInvoicesAllInvoiceAmount | — |
| INVOICE_CURRENCY_CODE | ApInvoicesAllInvoiceCurrencyCode | — |
| INVOICE_DATE | ApInvoicesAllInvoiceDate | — |
| INVOICE_ID | ApInvoicesAllInvoiceId | — |
| INVOICE_NUM | ApInvoicesAllInvoiceNum | — |
| INVOICE_RECEIVED_DATE | ApInvoicesAllInvoiceReceivedDate | — |
| INVOICE_TYPE_LOOKUP_CODE | ApInvoicesAllInvoiceTypeLookupCode | — |
| JOB_DEFINITION_NAME | ApInvoicesAllJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | ApInvoicesAllJobDefinitionPackage | — |
| LAST_UPDATE_DATE | ApInvoicesAllLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ApInvoicesAllLastUpdateLogin | — |
| LAST_UPDATED_BY | ApInvoicesAllLastUpdatedBy | — |
| LEGAL_ENTITY_ID | ApInvoicesAllLegalEntityId | — |
| LOCK_TIME | ApInvoicesAllLockTime | — |
| LOCKED_BY | ApInvoicesAllLockedBy | — |
| MERGE_REQUEST_ID | ApInvoicesAllMergeRequestId | — |
| MRC_BASE_AMOUNT | ApInvoicesAllMrcBaseAmount | — |
| MRC_EXCHANGE_DATE | ApInvoicesAllMrcExchangeDate | — |
| MRC_EXCHANGE_RATE | ApInvoicesAllMrcExchangeRate | — |
| MRC_EXCHANGE_RATE_TYPE | ApInvoicesAllMrcExchangeRateType | — |
| MRC_POSTING_STATUS | ApInvoicesAllMrcPostingStatus | — |
| NET_OF_RETAINAGE_FLAG | ApInvoicesAllNetOfRetainageFlag | — |
| OBJECT_VERSION_NUMBER | ApInvoicesAllObjectVersionNumber | — |
| ORG_ID | ApInvoicesAllOrgId | — |
| PA_DEFAULT_DIST_CCID | ApInvoicesAllPaDefaultDistCcid | — |
| PA_QUANTITY | ApInvoicesAllPaQuantity | — |
| PAID_ON_BEHALF_EMPLOYEE_ID | ApInvoicesAllPaidOnBehalfEmployeeId | — |
| PARTY_ID | ApInvoicesAllPartyId | — |
| PARTY_SITE_ID | ApInvoicesAllPartySiteId | — |
| PAY_CURR_INVOICE_AMOUNT | ApInvoicesAllPayCurrInvoiceAmount | — |
| PAY_GROUP_LOOKUP_CODE | ApInvoicesAllPayGroupLookupCode | — |
| PAY_PROC_TRXN_TYPE_CODE | ApInvoicesAllPayProcTrxnTypeCode | — |
| PAYMENT_AMOUNT_TOTAL | ApInvoicesAllPaymentAmountTotal | — |
| PAYMENT_CROSS_RATE | ApInvoicesAllPaymentCrossRate | — |
| PAYMENT_CROSS_RATE_DATE | ApInvoicesAllPaymentCrossRateDate | — |
| PAYMENT_CROSS_RATE_TYPE | ApInvoicesAllPaymentCrossRateType | — |
| PAYMENT_CURRENCY_CODE | ApInvoicesAllPaymentCurrencyCode | — |
| PAYMENT_FUNCTION | ApInvoicesAllPaymentFunction | — |
| PAYMENT_METHOD_CODE | ApInvoicesAllPaymentMethodCode | — |
| PAYMENT_METHOD_LOOKUP_CODE | ApInvoicesAllPaymentMethodLookupCode | — |
| PAYMENT_REASON_CODE | ApInvoicesAllPaymentReasonCode | — |
| PAYMENT_REASON_COMMENTS | ApInvoicesAllPaymentReasonComments | — |
| PAYMENT_STATUS_FLAG | ApInvoicesAllPaymentStatusFlag | — |
| PO_HEADER_ID | ApInvoicesAllPoHeaderId | — |
| PO_MATCHED_FLAG | ApInvoicesAllPoMatchedFlag | — |
| PORT_OF_ENTRY_CODE | ApInvoicesAllPortOfEntryCode | — |
| POSTING_STATUS | ApInvoicesAllPostingStatus | — |
| PRE_WITHHOLDING_AMOUNT | ApInvoicesAllPreWithholdingAmount | — |
| PRODUCT_TABLE | ApInvoicesAllProductTable | — |
| PROJECT_ID | ApInvoicesAllProjectId | — |
| QUICK_CREDIT | ApInvoicesAllQuickCredit | — |
| QUICK_PO_HEADER_ID | ApInvoicesAllQuickPoHeaderId | — |
| RECURRING_PAYMENT_ID | ApInvoicesAllRecurringPaymentId | — |
| REFERENCE_1 | ApInvoicesAllReference1 | — |
| REFERENCE_2 | ApInvoicesAllReference2 | — |
| REFERENCE_KEY1 | ApInvoicesAllReferenceKey1 | — |
| REFERENCE_KEY2 | ApInvoicesAllReferenceKey2 | — |
| REFERENCE_KEY3 | ApInvoicesAllReferenceKey3 | — |
| REFERENCE_KEY4 | ApInvoicesAllReferenceKey4 | — |
| REFERENCE_KEY5 | ApInvoicesAllReferenceKey5 | — |
| RELEASE_AMOUNT_NET_OF_TAX | ApInvoicesAllReleaseAmountNetOfTax | — |
| REMITTANCE_MESSAGE1 | ApInvoicesAllRemittanceMessage1 | — |
| REMITTANCE_MESSAGE2 | ApInvoicesAllRemittanceMessage2 | — |
| REMITTANCE_MESSAGE3 | ApInvoicesAllRemittanceMessage3 | — |
| REQUEST_ID | ApInvoicesAllRequestId | — |
| REQUESTER_ID | ApInvoicesAllRequesterId | — |
| ROUTING_STATUS_LOOKUP_CODE | ApInvoicesAllRoutingStatusLookupCode | — |
| SELF_ASSESSED_TAX_AMOUNT | ApInvoicesAllSelfAssessedTaxAmount | — |
| SET_OF_BOOKS_ID | ApInvoicesAllSetOfBooksId | — |
| SETTLEMENT_PRIORITY | ApInvoicesAllSettlementPriority | — |
| SOURCE | ApInvoicesAllSource | — |
| SUPPLIER_TAX_EXCHANGE_RATE | ApInvoicesAllSupplierTaxExchangeRate | — |
| SUPPLIER_TAX_INVOICE_DATE | ApInvoicesAllSupplierTaxInvoiceDate | — |
| SUPPLIER_TAX_INVOICE_NUMBER | ApInvoicesAllSupplierTaxInvoiceNumber | — |
| TASK_ID | ApInvoicesAllTaskId | — |
| TAX_INVOICE_INTERNAL_SEQ | ApInvoicesAllTaxInvoiceInternalSeq | — |
| TAX_INVOICE_RECORDING_DATE | ApInvoicesAllTaxInvoiceRecordingDate | — |
| TAX_RELATED_INVOICE_ID | ApInvoicesAllTaxRelatedInvoiceId | — |
| TAXATION_COUNTRY | ApInvoicesAllTaxationCountry | — |
| TEMP_CANCELLED_AMOUNT | ApInvoicesAllTempCancelledAmount | — |
| TERMS_DATE | ApInvoicesAllTermsDate | — |
| TERMS_ID | ApInvoicesAllTermsId | — |
| THIRD_PARTY_REGISTRATION_ID | ApInvoicesAllThirdPartyRegistrationId | — |
| TOTAL_TAX_AMOUNT | ApInvoicesAllTotalTaxAmount | — |
| TRANSACTION_DEADLINE | ApInvoicesAllTransactionDeadline | — |
| TRX_BUSINESS_CATEGORY | ApInvoicesAllTrxBusinessCategory | — |
| UNIQUE_REMITTANCE_IDENTIFIER | ApInvoicesAllUniqueRemittanceIdentifier | — |
| URI_CHECK_DIGIT | ApInvoicesAllUriCheckDigit | — |
| USER_DEFINED_FISC_CLASS | ApInvoicesAllUserDefinedFiscClass | — |
| USSGL_TRANSACTION_CODE | ApInvoicesAllUssglTransactionCode | — |
| USSGL_TRX_CODE_CONTEXT | ApInvoicesAllUssglTrxCodeContext | — |
| VALIDATED_TAX_AMOUNT | ApInvoicesAllValidatedTaxAmount | — |
| VALIDATION_REQUEST_ID | ApInvoicesAllValidationRequestId | — |
| VALIDATION_WORKER_ID | ApInvoicesAllValidationWorkerId | — |
| VENDOR_CONTACT_ID | ApInvoicesAllVendorContactId | — |
| VENDOR_ID | ApInvoicesAllVendorId | — |
| VENDOR_SITE_ID | ApInvoicesAllVendorSiteId | — |
| VOUCHER_NUM | ApInvoicesAllVoucherNum | — |
| WFAPPROVAL_STATUS | ApInvoicesAllWfapprovalStatus | — |

### [[fiscaldocumentchargeassocp|FiscalDocumentChargeAssocP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTS_PAY_CODE_COMBINATION_ID | ApInvoicesAllAcctsPayCodeCombinationId | — |
| AMOUNT_APPLICABLE_TO_DISCOUNT | ApInvoicesAllAmountApplicableToDiscount | — |
| AMOUNT_PAID | ApInvoicesAllAmountPaid | — |
| AMT_DUE_CCARD_COMPANY | ApInvoicesAllAmtDueCcardCompany | — |
| AMT_DUE_EMPLOYEE | ApInvoicesAllAmtDueEmployee | — |
| APPLICATION_ID | ApInvoicesAllApplicationId | — |
| APPROVAL_DESCRIPTION | ApInvoicesAllApprovalDescription | — |
| APPROVAL_ITERATION | ApInvoicesAllApprovalIteration | — |
| APPROVAL_READY_FLAG | ApInvoicesAllApprovalReadyFlag | — |
| APPROVAL_STATUS | ApInvoicesAllApprovalStatus | — |
| APPROVED_AMOUNT | ApInvoicesAllApprovedAmount | — |
| AWARD_ID | ApInvoicesAllAwardId | — |
| AWT_FLAG | ApInvoicesAllAwtFlag | — |
| AWT_GROUP_ID | ApInvoicesAllAwtGroupId | — |
| BANK_CHARGE_BEARER | ApInvoicesAllBankChargeBearer | — |
| BASE_AMOUNT | ApInvoicesAllBaseAmount | — |
| BATCH_ID | ApInvoicesAllBatchId | — |
| BUDGET_DATE | ApInvoicesAllBudgetDate | — |
| CANCELLED_AMOUNT | ApInvoicesAllCancelledAmount | — |
| CANCELLED_BY | ApInvoicesAllCancelledBy | — |
| CANCELLED_DATE | ApInvoicesAllCancelledDate | — |
| CHECK_VAT_AMOUNT_PAID | ApInvoicesAllCheckVatAmountPaid | — |
| CONTROL_AMOUNT | ApInvoicesAllControlAmount | — |
| CORRECTION_PERIOD | ApInvoicesAllCorrectionPeriod | — |
| CORRECTION_YEAR | ApInvoicesAllCorrectionYear | — |
| CREATED_BY | ApInvoicesAllCreatedBy | — |
| CREATION_DATE | ApInvoicesAllCreationDate | — |
| CREDITED_INVOICE_ID | ApInvoicesAllCreditedInvoiceId | — |
| CUST_REGISTRATION_CODE | ApInvoicesAllCustRegistrationCode | — |
| CUST_REGISTRATION_NUMBER | ApInvoicesAllCustRegistrationNumber | — |
| DATA_SET_ID | ApInvoicesAllDataSetId | — |
| DELIVERY_CHANNEL_CODE | ApInvoicesAllDeliveryChannelCode | — |
| DESCRIPTION | ApInvoicesAllDescription | — |
| DISC_IS_INV_LESS_TAX_FLAG | ApInvoicesAllDiscIsInvLessTaxFlag | — |
| DISCOUNT_AMOUNT_TAKEN | ApInvoicesAllDiscountAmountTaken | — |
| DISTRIBUTION_SET_ID | ApInvoicesAllDistributionSetId | — |
| DOC_CATEGORY_CODE | ApInvoicesAllDocCategoryCode | — |
| DOC_SEQUENCE_ID | ApInvoicesAllDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ApInvoicesAllDocSequenceValue | — |
| DOCUMENT_SUB_TYPE | ApInvoicesAllDocumentSubType | — |
| EARLIEST_SETTLEMENT_DATE | ApInvoicesAllEarliestSettlementDate | — |
| EMPLOYEE_ADDRESS_CODE | ApInvoicesAllEmployeeAddressCode | — |
| EXCHANGE_DATE | ApInvoicesAllExchangeDate | — |
| EXCHANGE_RATE | ApInvoicesAllExchangeRate | — |
| EXCHANGE_RATE_TYPE | ApInvoicesAllExchangeRateType | — |
| EXCLUDE_FREIGHT_FROM_DISCOUNT | ApInvoicesAllExcludeFreightFromDiscount | — |
| EXCLUSIVE_PAYMENT_FLAG | ApInvoicesAllExclusivePaymentFlag | — |
| EXPENDITURE_ITEM_DATE | ApInvoicesAllExpenditureItemDate | — |
| EXPENDITURE_ORGANIZATION_ID | ApInvoicesAllExpenditureOrganizationId | — |
| EXPENDITURE_TYPE | ApInvoicesAllExpenditureType | — |
| EXTERNAL_BANK_ACCOUNT_ID | ApInvoicesAllExternalBankAccountId | — |
| FIRST_PARTY_REGISTRATION_ID | ApInvoicesAllFirstPartyRegistrationId | — |
| FISCAL_DOC_ACCESS_KEY | ApInvoicesAllFiscalDocAccessKey | — |
| FORCE_REVALIDATION_FLAG | ApInvoicesAllForceRevalidationFlag | — |
| FREIGHT_AMOUNT | ApInvoicesAllFreightAmount | — |
| FUNDS_STATUS | ApInvoicesAllFundsStatus | — |
| GL_DATE | ApInvoicesAllGlDate | — |
| GOODS_RECEIVED_DATE | ApInvoicesAllGoodsReceivedDate | — |
| HISTORICAL_FLAG | ApInvoicesAllHistoricalFlag | — |
| IMAGE_DOCUMENT_NUM | ApInvoicesAllImageDocumentNum | — |
| IMPORT_DOCUMENT_DATE | ApInvoicesAllImportDocumentDate | — |
| IMPORT_DOCUMENT_NUMBER | ApInvoicesAllImportDocumentNumber | — |
| INTERCOMPANY_FLAG | ApInvoicesAllIntercompanyFlag | — |
| INTERNAL_CONTACT_EMAIL | ApInvoicesAllInternalContactEmail | — |
| INVOICE_AMOUNT | ApInvoicesAllInvoiceAmount | — |
| INVOICE_CURRENCY_CODE | ApInvoicesAllInvoiceCurrencyCode | — |
| INVOICE_DATE | ApInvoicesAllInvoiceDate | — |
| INVOICE_ID | ApInvoicesAllInvoiceId | — |
| INVOICE_NUM | ApInvoicesAllInvoiceNum | — |
| INVOICE_RECEIVED_DATE | ApInvoicesAllInvoiceReceivedDate | — |
| INVOICE_TYPE_LOOKUP_CODE | ApInvoicesAllInvoiceTypeLookupCode | — |
| JOB_DEFINITION_NAME | ApInvoicesAllJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | ApInvoicesAllJobDefinitionPackage | — |
| LAST_UPDATE_DATE | ApInvoicesAllLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ApInvoicesAllLastUpdateLogin | — |
| LAST_UPDATED_BY | ApInvoicesAllLastUpdatedBy | — |
| LEGAL_ENTITY_ID | ApInvoicesAllLegalEntityId | — |
| LOCK_TIME | ApInvoicesAllLockTime | — |
| LOCKED_BY | ApInvoicesAllLockedBy | — |
| MERGE_REQUEST_ID | ApInvoicesAllMergeRequestId | — |
| MRC_BASE_AMOUNT | ApInvoicesAllMrcBaseAmount | — |
| MRC_EXCHANGE_DATE | ApInvoicesAllMrcExchangeDate | — |
| MRC_EXCHANGE_RATE | ApInvoicesAllMrcExchangeRate | — |
| MRC_EXCHANGE_RATE_TYPE | ApInvoicesAllMrcExchangeRateType | — |
| MRC_POSTING_STATUS | ApInvoicesAllMrcPostingStatus | — |
| NET_OF_RETAINAGE_FLAG | ApInvoicesAllNetOfRetainageFlag | — |
| OBJECT_VERSION_NUMBER | ApInvoicesAllObjectVersionNumber | — |
| ORG_ID | ApInvoicesAllOrgId | — |
| PA_DEFAULT_DIST_CCID | ApInvoicesAllPaDefaultDistCcid | — |
| PA_QUANTITY | ApInvoicesAllPaQuantity | — |
| PAID_ON_BEHALF_EMPLOYEE_ID | ApInvoicesAllPaidOnBehalfEmployeeId | — |
| PARTY_ID | ApInvoicesAllPartyId | — |
| PARTY_SITE_ID | ApInvoicesAllPartySiteId | — |
| PAY_CURR_INVOICE_AMOUNT | ApInvoicesAllPayCurrInvoiceAmount | — |
| PAY_GROUP_LOOKUP_CODE | ApInvoicesAllPayGroupLookupCode | — |
| PAY_PROC_TRXN_TYPE_CODE | ApInvoicesAllPayProcTrxnTypeCode | — |
| PAYMENT_AMOUNT_TOTAL | ApInvoicesAllPaymentAmountTotal | — |
| PAYMENT_CROSS_RATE | ApInvoicesAllPaymentCrossRate | — |
| PAYMENT_CROSS_RATE_DATE | ApInvoicesAllPaymentCrossRateDate | — |
| PAYMENT_CROSS_RATE_TYPE | ApInvoicesAllPaymentCrossRateType | — |
| PAYMENT_CURRENCY_CODE | ApInvoicesAllPaymentCurrencyCode | — |
| PAYMENT_FUNCTION | ApInvoicesAllPaymentFunction | — |
| PAYMENT_METHOD_CODE | ApInvoicesAllPaymentMethodCode | — |
| PAYMENT_METHOD_LOOKUP_CODE | ApInvoicesAllPaymentMethodLookupCode | — |
| PAYMENT_REASON_CODE | ApInvoicesAllPaymentReasonCode | — |
| PAYMENT_REASON_COMMENTS | ApInvoicesAllPaymentReasonComments | — |
| PAYMENT_STATUS_FLAG | ApInvoicesAllPaymentStatusFlag | — |
| PO_HEADER_ID | ApInvoicesAllPoHeaderId | — |
| PO_MATCHED_FLAG | ApInvoicesAllPoMatchedFlag | — |
| PORT_OF_ENTRY_CODE | ApInvoicesAllPortOfEntryCode | — |
| POSTING_STATUS | ApInvoicesAllPostingStatus | — |
| PRE_WITHHOLDING_AMOUNT | ApInvoicesAllPreWithholdingAmount | — |
| PRODUCT_TABLE | ApInvoicesAllProductTable | — |
| PROJECT_ID | ApInvoicesAllProjectId | — |
| QUICK_CREDIT | ApInvoicesAllQuickCredit | — |
| QUICK_PO_HEADER_ID | ApInvoicesAllQuickPoHeaderId | — |
| RECURRING_PAYMENT_ID | ApInvoicesAllRecurringPaymentId | — |
| REFERENCE_1 | ApInvoicesAllReference1 | — |
| REFERENCE_2 | ApInvoicesAllReference2 | — |
| REFERENCE_KEY1 | ApInvoicesAllReferenceKey1 | — |
| REFERENCE_KEY2 | ApInvoicesAllReferenceKey2 | — |
| REFERENCE_KEY3 | ApInvoicesAllReferenceKey3 | — |
| REFERENCE_KEY4 | ApInvoicesAllReferenceKey4 | — |
| REFERENCE_KEY5 | ApInvoicesAllReferenceKey5 | — |
| RELEASE_AMOUNT_NET_OF_TAX | ApInvoicesAllReleaseAmountNetOfTax | — |
| REMITTANCE_MESSAGE1 | ApInvoicesAllRemittanceMessage1 | — |
| REMITTANCE_MESSAGE2 | ApInvoicesAllRemittanceMessage2 | — |
| REMITTANCE_MESSAGE3 | ApInvoicesAllRemittanceMessage3 | — |
| REQUEST_ID | ApInvoicesAllRequestId | — |
| REQUESTER_ID | ApInvoicesAllRequesterId | — |
| ROUTING_STATUS_LOOKUP_CODE | ApInvoicesAllRoutingStatusLookupCode | — |
| SELF_ASSESSED_TAX_AMOUNT | ApInvoicesAllSelfAssessedTaxAmount | — |
| SET_OF_BOOKS_ID | ApInvoicesAllSetOfBooksId | — |
| SETTLEMENT_PRIORITY | ApInvoicesAllSettlementPriority | — |
| SOURCE | ApInvoicesAllSource | — |
| SUPPLIER_TAX_EXCHANGE_RATE | ApInvoicesAllSupplierTaxExchangeRate | — |
| SUPPLIER_TAX_INVOICE_DATE | ApInvoicesAllSupplierTaxInvoiceDate | — |
| SUPPLIER_TAX_INVOICE_NUMBER | ApInvoicesAllSupplierTaxInvoiceNumber | — |
| TASK_ID | ApInvoicesAllTaskId | — |
| TAX_INVOICE_INTERNAL_SEQ | ApInvoicesAllTaxInvoiceInternalSeq | — |
| TAX_INVOICE_RECORDING_DATE | ApInvoicesAllTaxInvoiceRecordingDate | — |
| TAX_RELATED_INVOICE_ID | ApInvoicesAllTaxRelatedInvoiceId | — |
| TAXATION_COUNTRY | ApInvoicesAllTaxationCountry | — |
| TEMP_CANCELLED_AMOUNT | ApInvoicesAllTempCancelledAmount | — |
| TERMS_DATE | ApInvoicesAllTermsDate | — |
| TERMS_ID | ApInvoicesAllTermsId | — |
| THIRD_PARTY_REGISTRATION_ID | ApInvoicesAllThirdPartyRegistrationId | — |
| TOTAL_TAX_AMOUNT | ApInvoicesAllTotalTaxAmount | — |
| TRANSACTION_DEADLINE | ApInvoicesAllTransactionDeadline | — |
| TRX_BUSINESS_CATEGORY | ApInvoicesAllTrxBusinessCategory | — |
| UNIQUE_REMITTANCE_IDENTIFIER | ApInvoicesAllUniqueRemittanceIdentifier | — |
| URI_CHECK_DIGIT | ApInvoicesAllUriCheckDigit | — |
| USER_DEFINED_FISC_CLASS | ApInvoicesAllUserDefinedFiscClass | — |
| USSGL_TRANSACTION_CODE | ApInvoicesAllUssglTransactionCode | — |
| USSGL_TRX_CODE_CONTEXT | ApInvoicesAllUssglTrxCodeContext | — |
| VALIDATED_TAX_AMOUNT | ApInvoicesAllValidatedTaxAmount | — |
| VALIDATION_REQUEST_ID | ApInvoicesAllValidationRequestId | — |
| VALIDATION_WORKER_ID | ApInvoicesAllValidationWorkerId | — |
| VENDOR_CONTACT_ID | ApInvoicesAllVendorContactId | — |
| VENDOR_ID | ApInvoicesAllVendorId | — |
| VENDOR_SITE_ID | ApInvoicesAllVendorSiteId | — |
| VOUCHER_NUM | ApInvoicesAllVoucherNum | — |
| WFAPPROVAL_STATUS | ApInvoicesAllWfapprovalStatus | — |

### [[fiscaldocumentlinesp|FiscalDocumentLinesP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTS_PAY_CODE_COMBINATION_ID | ApInvoicesAllAcctsPayCodeCombinationId | — |
| AMOUNT_APPLICABLE_TO_DISCOUNT | ApInvoicesAllAmountApplicableToDiscount | — |
| AMOUNT_PAID | ApInvoicesAllAmountPaid | — |
| AMT_DUE_CCARD_COMPANY | ApInvoicesAllAmtDueCcardCompany | — |
| AMT_DUE_EMPLOYEE | ApInvoicesAllAmtDueEmployee | — |
| APPLICATION_ID | ApInvoicesAllApplicationId | — |
| APPROVAL_DESCRIPTION | ApInvoicesAllApprovalDescription | — |
| APPROVAL_ITERATION | ApInvoicesAllApprovalIteration | — |
| APPROVAL_READY_FLAG | ApInvoicesAllApprovalReadyFlag | — |
| APPROVAL_STATUS | ApInvoicesAllApprovalStatus | — |
| APPROVED_AMOUNT | ApInvoicesAllApprovedAmount | — |
| AWARD_ID | ApInvoicesAllAwardId | — |
| AWT_FLAG | ApInvoicesAllAwtFlag | — |
| AWT_GROUP_ID | ApInvoicesAllAwtGroupId | — |
| BANK_CHARGE_BEARER | ApInvoicesAllBankChargeBearer | — |
| BASE_AMOUNT | ApInvoicesAllBaseAmount | — |
| BATCH_ID | ApInvoicesAllBatchId | — |
| BUDGET_DATE | ApInvoicesAllBudgetDate | — |
| CANCELLED_AMOUNT | ApInvoicesAllCancelledAmount | — |
| CANCELLED_BY | ApInvoicesAllCancelledBy | — |
| CANCELLED_DATE | ApInvoicesAllCancelledDate | — |
| CHECK_VAT_AMOUNT_PAID | ApInvoicesAllCheckVatAmountPaid | — |
| CONTROL_AMOUNT | ApInvoicesAllControlAmount | — |
| CORRECTION_PERIOD | ApInvoicesAllCorrectionPeriod | — |
| CORRECTION_YEAR | ApInvoicesAllCorrectionYear | — |
| CREATED_BY | ApInvoicesAllCreatedBy | — |
| CREATION_DATE | ApInvoicesAllCreationDate | — |
| CREDITED_INVOICE_ID | ApInvoicesAllCreditedInvoiceId | — |
| CUST_REGISTRATION_CODE | ApInvoicesAllCustRegistrationCode | — |
| CUST_REGISTRATION_NUMBER | ApInvoicesAllCustRegistrationNumber | — |
| DATA_SET_ID | ApInvoicesAllDataSetId | — |
| DELIVERY_CHANNEL_CODE | ApInvoicesAllDeliveryChannelCode | — |
| DESCRIPTION | ApInvoicesAllDescription | — |
| DISC_IS_INV_LESS_TAX_FLAG | ApInvoicesAllDiscIsInvLessTaxFlag | — |
| DISCOUNT_AMOUNT_TAKEN | ApInvoicesAllDiscountAmountTaken | — |
| DISTRIBUTION_SET_ID | ApInvoicesAllDistributionSetId | — |
| DOC_CATEGORY_CODE | ApInvoicesAllDocCategoryCode | — |
| DOC_SEQUENCE_ID | ApInvoicesAllDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ApInvoicesAllDocSequenceValue | — |
| DOCUMENT_SUB_TYPE | ApInvoicesAllDocumentSubType | — |
| EARLIEST_SETTLEMENT_DATE | ApInvoicesAllEarliestSettlementDate | — |
| EMPLOYEE_ADDRESS_CODE | ApInvoicesAllEmployeeAddressCode | — |
| EXCHANGE_DATE | ApInvoicesAllExchangeDate | — |
| EXCHANGE_RATE | ApInvoicesAllExchangeRate | — |
| EXCHANGE_RATE_TYPE | ApInvoicesAllExchangeRateType | — |
| EXCLUDE_FREIGHT_FROM_DISCOUNT | ApInvoicesAllExcludeFreightFromDiscount | — |
| EXCLUSIVE_PAYMENT_FLAG | ApInvoicesAllExclusivePaymentFlag | — |
| EXPENDITURE_ITEM_DATE | ApInvoicesAllExpenditureItemDate | — |
| EXPENDITURE_ORGANIZATION_ID | ApInvoicesAllExpenditureOrganizationId | — |
| EXPENDITURE_TYPE | ApInvoicesAllExpenditureType | — |
| EXTERNAL_BANK_ACCOUNT_ID | ApInvoicesAllExternalBankAccountId | — |
| FIRST_PARTY_REGISTRATION_ID | ApInvoicesAllFirstPartyRegistrationId | — |
| FISCAL_DOC_ACCESS_KEY | ApInvoicesAllFiscalDocAccessKey | — |
| FORCE_REVALIDATION_FLAG | ApInvoicesAllForceRevalidationFlag | — |
| FREIGHT_AMOUNT | ApInvoicesAllFreightAmount | — |
| FUNDS_STATUS | ApInvoicesAllFundsStatus | — |
| GL_DATE | ApInvoicesAllGlDate | — |
| GOODS_RECEIVED_DATE | ApInvoicesAllGoodsReceivedDate | — |
| HISTORICAL_FLAG | ApInvoicesAllHistoricalFlag | — |
| IMAGE_DOCUMENT_NUM | ApInvoicesAllImageDocumentNum | — |
| IMPORT_DOCUMENT_DATE | ApInvoicesAllImportDocumentDate | — |
| IMPORT_DOCUMENT_NUMBER | ApInvoicesAllImportDocumentNumber | — |
| INTERCOMPANY_FLAG | ApInvoicesAllIntercompanyFlag | — |
| INTERNAL_CONTACT_EMAIL | ApInvoicesAllInternalContactEmail | — |
| INVOICE_AMOUNT | ApInvoicesAllInvoiceAmount | — |
| INVOICE_CURRENCY_CODE | ApInvoicesAllInvoiceCurrencyCode | — |
| INVOICE_DATE | ApInvoicesAllInvoiceDate | — |
| INVOICE_ID | ApInvoicesAllInvoiceId | — |
| INVOICE_NUM | ApInvoicesAllInvoiceNum | — |
| INVOICE_RECEIVED_DATE | ApInvoicesAllInvoiceReceivedDate | — |
| INVOICE_TYPE_LOOKUP_CODE | ApInvoicesAllInvoiceTypeLookupCode | — |
| JOB_DEFINITION_NAME | ApInvoicesAllJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | ApInvoicesAllJobDefinitionPackage | — |
| LAST_UPDATE_DATE | ApInvoicesAllLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ApInvoicesAllLastUpdateLogin | — |
| LAST_UPDATED_BY | ApInvoicesAllLastUpdatedBy | — |
| LEGAL_ENTITY_ID | ApInvoicesAllLegalEntityId | — |
| LOCK_TIME | ApInvoicesAllLockTime | — |
| LOCKED_BY | ApInvoicesAllLockedBy | — |
| MERGE_REQUEST_ID | ApInvoicesAllMergeRequestId | — |
| MRC_BASE_AMOUNT | ApInvoicesAllMrcBaseAmount | — |
| MRC_EXCHANGE_DATE | ApInvoicesAllMrcExchangeDate | — |
| MRC_EXCHANGE_RATE | ApInvoicesAllMrcExchangeRate | — |
| MRC_EXCHANGE_RATE_TYPE | ApInvoicesAllMrcExchangeRateType | — |
| MRC_POSTING_STATUS | ApInvoicesAllMrcPostingStatus | — |
| NET_OF_RETAINAGE_FLAG | ApInvoicesAllNetOfRetainageFlag | — |
| OBJECT_VERSION_NUMBER | ApInvoicesAllObjectVersionNumber | — |
| ORG_ID | ApInvoicesAllOrgId | — |
| PA_DEFAULT_DIST_CCID | ApInvoicesAllPaDefaultDistCcid | — |
| PA_QUANTITY | ApInvoicesAllPaQuantity | — |
| PAID_ON_BEHALF_EMPLOYEE_ID | ApInvoicesAllPaidOnBehalfEmployeeId | — |
| PARTY_ID | ApInvoicesAllPartyId | — |
| PARTY_SITE_ID | ApInvoicesAllPartySiteId | — |
| PAY_CURR_INVOICE_AMOUNT | ApInvoicesAllPayCurrInvoiceAmount | — |
| PAY_GROUP_LOOKUP_CODE | ApInvoicesAllPayGroupLookupCode | — |
| PAY_PROC_TRXN_TYPE_CODE | ApInvoicesAllPayProcTrxnTypeCode | — |
| PAYMENT_AMOUNT_TOTAL | ApInvoicesAllPaymentAmountTotal | — |
| PAYMENT_CROSS_RATE | ApInvoicesAllPaymentCrossRate | — |
| PAYMENT_CROSS_RATE_DATE | ApInvoicesAllPaymentCrossRateDate | — |
| PAYMENT_CROSS_RATE_TYPE | ApInvoicesAllPaymentCrossRateType | — |
| PAYMENT_CURRENCY_CODE | ApInvoicesAllPaymentCurrencyCode | — |
| PAYMENT_FUNCTION | ApInvoicesAllPaymentFunction | — |
| PAYMENT_METHOD_CODE | ApInvoicesAllPaymentMethodCode | — |
| PAYMENT_METHOD_LOOKUP_CODE | ApInvoicesAllPaymentMethodLookupCode | — |
| PAYMENT_REASON_CODE | ApInvoicesAllPaymentReasonCode | — |
| PAYMENT_REASON_COMMENTS | ApInvoicesAllPaymentReasonComments | — |
| PAYMENT_STATUS_FLAG | ApInvoicesAllPaymentStatusFlag | — |
| PO_HEADER_ID | ApInvoicesAllPoHeaderId | — |
| PO_MATCHED_FLAG | ApInvoicesAllPoMatchedFlag | — |
| PORT_OF_ENTRY_CODE | ApInvoicesAllPortOfEntryCode | — |
| POSTING_STATUS | ApInvoicesAllPostingStatus | — |
| PRE_WITHHOLDING_AMOUNT | ApInvoicesAllPreWithholdingAmount | — |
| PRODUCT_TABLE | ApInvoicesAllProductTable | — |
| PROJECT_ID | ApInvoicesAllProjectId | — |
| QUICK_CREDIT | ApInvoicesAllQuickCredit | — |
| QUICK_PO_HEADER_ID | ApInvoicesAllQuickPoHeaderId | — |
| RECURRING_PAYMENT_ID | ApInvoicesAllRecurringPaymentId | — |
| REFERENCE_1 | ApInvoicesAllReference1 | — |
| REFERENCE_2 | ApInvoicesAllReference2 | — |
| REFERENCE_KEY1 | ApInvoicesAllReferenceKey1 | — |
| REFERENCE_KEY2 | ApInvoicesAllReferenceKey2 | — |
| REFERENCE_KEY3 | ApInvoicesAllReferenceKey3 | — |
| REFERENCE_KEY4 | ApInvoicesAllReferenceKey4 | — |
| REFERENCE_KEY5 | ApInvoicesAllReferenceKey5 | — |
| RELEASE_AMOUNT_NET_OF_TAX | ApInvoicesAllReleaseAmountNetOfTax | — |
| REMITTANCE_MESSAGE1 | ApInvoicesAllRemittanceMessage1 | — |
| REMITTANCE_MESSAGE2 | ApInvoicesAllRemittanceMessage2 | — |
| REMITTANCE_MESSAGE3 | ApInvoicesAllRemittanceMessage3 | — |
| REQUEST_ID | ApInvoicesAllRequestId | — |
| REQUESTER_ID | ApInvoicesAllRequesterId | — |
| ROUTING_STATUS_LOOKUP_CODE | ApInvoicesAllRoutingStatusLookupCode | — |
| SELF_ASSESSED_TAX_AMOUNT | ApInvoicesAllSelfAssessedTaxAmount | — |
| SET_OF_BOOKS_ID | ApInvoicesAllSetOfBooksId | — |
| SETTLEMENT_PRIORITY | ApInvoicesAllSettlementPriority | — |
| SOURCE | ApInvoicesAllSource | — |
| SUPPLIER_TAX_EXCHANGE_RATE | ApInvoicesAllSupplierTaxExchangeRate | — |
| SUPPLIER_TAX_INVOICE_DATE | ApInvoicesAllSupplierTaxInvoiceDate | — |
| SUPPLIER_TAX_INVOICE_NUMBER | ApInvoicesAllSupplierTaxInvoiceNumber | — |
| TASK_ID | ApInvoicesAllTaskId | — |
| TAX_INVOICE_INTERNAL_SEQ | ApInvoicesAllTaxInvoiceInternalSeq | — |
| TAX_INVOICE_RECORDING_DATE | ApInvoicesAllTaxInvoiceRecordingDate | — |
| TAX_RELATED_INVOICE_ID | ApInvoicesAllTaxRelatedInvoiceId | — |
| TAXATION_COUNTRY | ApInvoicesAllTaxationCountry | — |
| TEMP_CANCELLED_AMOUNT | ApInvoicesAllTempCancelledAmount | — |
| TERMS_DATE | ApInvoicesAllTermsDate | — |
| TERMS_ID | ApInvoicesAllTermsId | — |
| THIRD_PARTY_REGISTRATION_ID | ApInvoicesAllThirdPartyRegistrationId | — |
| TOTAL_TAX_AMOUNT | ApInvoicesAllTotalTaxAmount | — |
| TRANSACTION_DEADLINE | ApInvoicesAllTransactionDeadline | — |
| TRX_BUSINESS_CATEGORY | ApInvoicesAllTrxBusinessCategory | — |
| UNIQUE_REMITTANCE_IDENTIFIER | ApInvoicesAllUniqueRemittanceIdentifier | — |
| URI_CHECK_DIGIT | ApInvoicesAllUriCheckDigit | — |
| USER_DEFINED_FISC_CLASS | ApInvoicesAllUserDefinedFiscClass | — |
| USSGL_TRANSACTION_CODE | ApInvoicesAllUssglTransactionCode | — |
| USSGL_TRX_CODE_CONTEXT | ApInvoicesAllUssglTrxCodeContext | — |
| VALIDATED_TAX_AMOUNT | ApInvoicesAllValidatedTaxAmount | — |
| VALIDATION_REQUEST_ID | ApInvoicesAllValidationRequestId | — |
| VALIDATION_WORKER_ID | ApInvoicesAllValidationWorkerId | — |
| VENDOR_CONTACT_ID | ApInvoicesAllVendorContactId | — |
| VENDOR_ID | ApInvoicesAllVendorId | — |
| VENDOR_SITE_ID | ApInvoicesAllVendorSiteId | — |
| VOUCHER_NUM | ApInvoicesAllVoucherNum | — |
| WFAPPROVAL_STATUS | ApInvoicesAllWfapprovalStatus | — |

### [[fiscaldocumentrcvchargeallocsp|FiscalDocumentRcvChargeAllocsP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTS_PAY_CODE_COMBINATION_ID | ApInvoicesAllAcctsPayCodeCombinationId | — |
| AMOUNT_APPLICABLE_TO_DISCOUNT | ApInvoicesAllAmountApplicableToDiscount | — |
| AMOUNT_PAID | ApInvoicesAllAmountPaid | — |
| AMT_DUE_CCARD_COMPANY | ApInvoicesAllAmtDueCcardCompany | — |
| AMT_DUE_EMPLOYEE | ApInvoicesAllAmtDueEmployee | — |
| APPLICATION_ID | ApInvoicesAllApplicationId | — |
| APPROVAL_DESCRIPTION | ApInvoicesAllApprovalDescription | — |
| APPROVAL_ITERATION | ApInvoicesAllApprovalIteration | — |
| APPROVAL_READY_FLAG | ApInvoicesAllApprovalReadyFlag | — |
| APPROVAL_STATUS | ApInvoicesAllApprovalStatus | — |
| APPROVED_AMOUNT | ApInvoicesAllApprovedAmount | — |
| AWARD_ID | ApInvoicesAllAwardId | — |
| AWT_FLAG | ApInvoicesAllAwtFlag | — |
| AWT_GROUP_ID | ApInvoicesAllAwtGroupId | — |
| BANK_CHARGE_BEARER | ApInvoicesAllBankChargeBearer | — |
| BASE_AMOUNT | ApInvoicesAllBaseAmount | — |
| BATCH_ID | ApInvoicesAllBatchId | — |
| BUDGET_DATE | ApInvoicesAllBudgetDate | — |
| CANCELLED_AMOUNT | ApInvoicesAllCancelledAmount | — |
| CANCELLED_BY | ApInvoicesAllCancelledBy | — |
| CANCELLED_DATE | ApInvoicesAllCancelledDate | — |
| CHECK_VAT_AMOUNT_PAID | ApInvoicesAllCheckVatAmountPaid | — |
| CONTROL_AMOUNT | ApInvoicesAllControlAmount | — |
| CORRECTION_PERIOD | ApInvoicesAllCorrectionPeriod | — |
| CORRECTION_YEAR | ApInvoicesAllCorrectionYear | — |
| CREATED_BY | ApInvoicesAllCreatedBy | — |
| CREATION_DATE | ApInvoicesAllCreationDate | — |
| CREDITED_INVOICE_ID | ApInvoicesAllCreditedInvoiceId | — |
| CUST_REGISTRATION_CODE | ApInvoicesAllCustRegistrationCode | — |
| CUST_REGISTRATION_NUMBER | ApInvoicesAllCustRegistrationNumber | — |
| DATA_SET_ID | ApInvoicesAllDataSetId | — |
| DELIVERY_CHANNEL_CODE | ApInvoicesAllDeliveryChannelCode | — |
| DESCRIPTION | ApInvoicesAllDescription | — |
| DISC_IS_INV_LESS_TAX_FLAG | ApInvoicesAllDiscIsInvLessTaxFlag | — |
| DISCOUNT_AMOUNT_TAKEN | ApInvoicesAllDiscountAmountTaken | — |
| DISTRIBUTION_SET_ID | ApInvoicesAllDistributionSetId | — |
| DOC_CATEGORY_CODE | ApInvoicesAllDocCategoryCode | — |
| DOC_SEQUENCE_ID | ApInvoicesAllDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ApInvoicesAllDocSequenceValue | — |
| DOCUMENT_SUB_TYPE | ApInvoicesAllDocumentSubType | — |
| EARLIEST_SETTLEMENT_DATE | ApInvoicesAllEarliestSettlementDate | — |
| EMPLOYEE_ADDRESS_CODE | ApInvoicesAllEmployeeAddressCode | — |
| EXCHANGE_DATE | ApInvoicesAllExchangeDate | — |
| EXCHANGE_RATE | ApInvoicesAllExchangeRate | — |
| EXCHANGE_RATE_TYPE | ApInvoicesAllExchangeRateType | — |
| EXCLUDE_FREIGHT_FROM_DISCOUNT | ApInvoicesAllExcludeFreightFromDiscount | — |
| EXCLUSIVE_PAYMENT_FLAG | ApInvoicesAllExclusivePaymentFlag | — |
| EXPENDITURE_ITEM_DATE | ApInvoicesAllExpenditureItemDate | — |
| EXPENDITURE_ORGANIZATION_ID | ApInvoicesAllExpenditureOrganizationId | — |
| EXPENDITURE_TYPE | ApInvoicesAllExpenditureType | — |
| EXTERNAL_BANK_ACCOUNT_ID | ApInvoicesAllExternalBankAccountId | — |
| FIRST_PARTY_REGISTRATION_ID | ApInvoicesAllFirstPartyRegistrationId | — |
| FISCAL_DOC_ACCESS_KEY | ApInvoicesAllFiscalDocAccessKey | — |
| FORCE_REVALIDATION_FLAG | ApInvoicesAllForceRevalidationFlag | — |
| FREIGHT_AMOUNT | ApInvoicesAllFreightAmount | — |
| FUNDS_STATUS | ApInvoicesAllFundsStatus | — |
| GL_DATE | ApInvoicesAllGlDate | — |
| GOODS_RECEIVED_DATE | ApInvoicesAllGoodsReceivedDate | — |
| HISTORICAL_FLAG | ApInvoicesAllHistoricalFlag | — |
| IMAGE_DOCUMENT_NUM | ApInvoicesAllImageDocumentNum | — |
| IMPORT_DOCUMENT_DATE | ApInvoicesAllImportDocumentDate | — |
| IMPORT_DOCUMENT_NUMBER | ApInvoicesAllImportDocumentNumber | — |
| INTERCOMPANY_FLAG | ApInvoicesAllIntercompanyFlag | — |
| INTERNAL_CONTACT_EMAIL | ApInvoicesAllInternalContactEmail | — |
| INVOICE_AMOUNT | ApInvoicesAllInvoiceAmount | — |
| INVOICE_CURRENCY_CODE | ApInvoicesAllInvoiceCurrencyCode | — |
| INVOICE_DATE | ApInvoicesAllInvoiceDate | — |
| INVOICE_ID | ApInvoicesAllInvoiceId | — |
| INVOICE_NUM | ApInvoicesAllInvoiceNum | — |
| INVOICE_RECEIVED_DATE | ApInvoicesAllInvoiceReceivedDate | — |
| INVOICE_TYPE_LOOKUP_CODE | ApInvoicesAllInvoiceTypeLookupCode | — |
| JOB_DEFINITION_NAME | ApInvoicesAllJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | ApInvoicesAllJobDefinitionPackage | — |
| LAST_UPDATE_DATE | ApInvoicesAllLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ApInvoicesAllLastUpdateLogin | — |
| LAST_UPDATED_BY | ApInvoicesAllLastUpdatedBy | — |
| LEGAL_ENTITY_ID | ApInvoicesAllLegalEntityId | — |
| LOCK_TIME | ApInvoicesAllLockTime | — |
| LOCKED_BY | ApInvoicesAllLockedBy | — |
| MERGE_REQUEST_ID | ApInvoicesAllMergeRequestId | — |
| MRC_BASE_AMOUNT | ApInvoicesAllMrcBaseAmount | — |
| MRC_EXCHANGE_DATE | ApInvoicesAllMrcExchangeDate | — |
| MRC_EXCHANGE_RATE | ApInvoicesAllMrcExchangeRate | — |
| MRC_EXCHANGE_RATE_TYPE | ApInvoicesAllMrcExchangeRateType | — |
| MRC_POSTING_STATUS | ApInvoicesAllMrcPostingStatus | — |
| NET_OF_RETAINAGE_FLAG | ApInvoicesAllNetOfRetainageFlag | — |
| OBJECT_VERSION_NUMBER | ApInvoicesAllObjectVersionNumber | — |
| ORG_ID | ApInvoicesAllOrgId | — |
| PA_DEFAULT_DIST_CCID | ApInvoicesAllPaDefaultDistCcid | — |
| PA_QUANTITY | ApInvoicesAllPaQuantity | — |
| PAID_ON_BEHALF_EMPLOYEE_ID | ApInvoicesAllPaidOnBehalfEmployeeId | — |
| PARTY_ID | ApInvoicesAllPartyId | — |
| PARTY_SITE_ID | ApInvoicesAllPartySiteId | — |
| PAY_CURR_INVOICE_AMOUNT | ApInvoicesAllPayCurrInvoiceAmount | — |
| PAY_GROUP_LOOKUP_CODE | ApInvoicesAllPayGroupLookupCode | — |
| PAY_PROC_TRXN_TYPE_CODE | ApInvoicesAllPayProcTrxnTypeCode | — |
| PAYMENT_AMOUNT_TOTAL | ApInvoicesAllPaymentAmountTotal | — |
| PAYMENT_CROSS_RATE | ApInvoicesAllPaymentCrossRate | — |
| PAYMENT_CROSS_RATE_DATE | ApInvoicesAllPaymentCrossRateDate | — |
| PAYMENT_CROSS_RATE_TYPE | ApInvoicesAllPaymentCrossRateType | — |
| PAYMENT_CURRENCY_CODE | ApInvoicesAllPaymentCurrencyCode | — |
| PAYMENT_FUNCTION | ApInvoicesAllPaymentFunction | — |
| PAYMENT_METHOD_CODE | ApInvoicesAllPaymentMethodCode | — |
| PAYMENT_METHOD_LOOKUP_CODE | ApInvoicesAllPaymentMethodLookupCode | — |
| PAYMENT_REASON_CODE | ApInvoicesAllPaymentReasonCode | — |
| PAYMENT_REASON_COMMENTS | ApInvoicesAllPaymentReasonComments | — |
| PAYMENT_STATUS_FLAG | ApInvoicesAllPaymentStatusFlag | — |
| PO_HEADER_ID | ApInvoicesAllPoHeaderId | — |
| PO_MATCHED_FLAG | ApInvoicesAllPoMatchedFlag | — |
| PORT_OF_ENTRY_CODE | ApInvoicesAllPortOfEntryCode | — |
| POSTING_STATUS | ApInvoicesAllPostingStatus | — |
| PRE_WITHHOLDING_AMOUNT | ApInvoicesAllPreWithholdingAmount | — |
| PRODUCT_TABLE | ApInvoicesAllProductTable | — |
| PROJECT_ID | ApInvoicesAllProjectId | — |
| QUICK_CREDIT | ApInvoicesAllQuickCredit | — |
| QUICK_PO_HEADER_ID | ApInvoicesAllQuickPoHeaderId | — |
| RECURRING_PAYMENT_ID | ApInvoicesAllRecurringPaymentId | — |
| REFERENCE_1 | ApInvoicesAllReference1 | — |
| REFERENCE_2 | ApInvoicesAllReference2 | — |
| REFERENCE_KEY1 | ApInvoicesAllReferenceKey1 | — |
| REFERENCE_KEY2 | ApInvoicesAllReferenceKey2 | — |
| REFERENCE_KEY3 | ApInvoicesAllReferenceKey3 | — |
| REFERENCE_KEY4 | ApInvoicesAllReferenceKey4 | — |
| REFERENCE_KEY5 | ApInvoicesAllReferenceKey5 | — |
| RELEASE_AMOUNT_NET_OF_TAX | ApInvoicesAllReleaseAmountNetOfTax | — |
| REMITTANCE_MESSAGE1 | ApInvoicesAllRemittanceMessage1 | — |
| REMITTANCE_MESSAGE2 | ApInvoicesAllRemittanceMessage2 | — |
| REMITTANCE_MESSAGE3 | ApInvoicesAllRemittanceMessage3 | — |
| REQUEST_ID | ApInvoicesAllRequestId | — |
| REQUESTER_ID | ApInvoicesAllRequesterId | — |
| ROUTING_STATUS_LOOKUP_CODE | ApInvoicesAllRoutingStatusLookupCode | — |
| SELF_ASSESSED_TAX_AMOUNT | ApInvoicesAllSelfAssessedTaxAmount | — |
| SET_OF_BOOKS_ID | ApInvoicesAllSetOfBooksId | — |
| SETTLEMENT_PRIORITY | ApInvoicesAllSettlementPriority | — |
| SOURCE | ApInvoicesAllSource | — |
| SUPPLIER_TAX_EXCHANGE_RATE | ApInvoicesAllSupplierTaxExchangeRate | — |
| SUPPLIER_TAX_INVOICE_DATE | ApInvoicesAllSupplierTaxInvoiceDate | — |
| SUPPLIER_TAX_INVOICE_NUMBER | ApInvoicesAllSupplierTaxInvoiceNumber | — |
| TASK_ID | ApInvoicesAllTaskId | — |
| TAX_INVOICE_INTERNAL_SEQ | ApInvoicesAllTaxInvoiceInternalSeq | — |
| TAX_INVOICE_RECORDING_DATE | ApInvoicesAllTaxInvoiceRecordingDate | — |
| TAX_RELATED_INVOICE_ID | ApInvoicesAllTaxRelatedInvoiceId | — |
| TAXATION_COUNTRY | ApInvoicesAllTaxationCountry | — |
| TEMP_CANCELLED_AMOUNT | ApInvoicesAllTempCancelledAmount | — |
| TERMS_DATE | ApInvoicesAllTermsDate | — |
| TERMS_ID | ApInvoicesAllTermsId | — |
| THIRD_PARTY_REGISTRATION_ID | ApInvoicesAllThirdPartyRegistrationId | — |
| TOTAL_TAX_AMOUNT | ApInvoicesAllTotalTaxAmount | — |
| TRANSACTION_DEADLINE | ApInvoicesAllTransactionDeadline | — |
| TRX_BUSINESS_CATEGORY | ApInvoicesAllTrxBusinessCategory | — |
| UNIQUE_REMITTANCE_IDENTIFIER | ApInvoicesAllUniqueRemittanceIdentifier | — |
| URI_CHECK_DIGIT | ApInvoicesAllUriCheckDigit | — |
| USER_DEFINED_FISC_CLASS | ApInvoicesAllUserDefinedFiscClass | — |
| USSGL_TRANSACTION_CODE | ApInvoicesAllUssglTransactionCode | — |
| USSGL_TRX_CODE_CONTEXT | ApInvoicesAllUssglTrxCodeContext | — |
| VALIDATED_TAX_AMOUNT | ApInvoicesAllValidatedTaxAmount | — |
| VALIDATION_REQUEST_ID | ApInvoicesAllValidationRequestId | — |
| VALIDATION_WORKER_ID | ApInvoicesAllValidationWorkerId | — |
| VENDOR_CONTACT_ID | ApInvoicesAllVendorContactId | — |
| VENDOR_ID | ApInvoicesAllVendorId | — |
| VENDOR_SITE_ID | ApInvoicesAllVendorSiteId | — |
| VOUCHER_NUM | ApInvoicesAllVoucherNum | — |
| WFAPPROVAL_STATUS | ApInvoicesAllWfapprovalStatus | — |

### [[fiscaldocumentschedulesp|FiscalDocumentSchedulesP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTS_PAY_CODE_COMBINATION_ID | ApInvoicesAllAcctsPayCodeCombinationId | — |
| AMOUNT_APPLICABLE_TO_DISCOUNT | ApInvoicesAllAmountApplicableToDiscount | — |
| AMOUNT_PAID | ApInvoicesAllAmountPaid | — |
| AMT_DUE_CCARD_COMPANY | ApInvoicesAllAmtDueCcardCompany | — |
| AMT_DUE_EMPLOYEE | ApInvoicesAllAmtDueEmployee | — |
| APPLICATION_ID | ApInvoicesAllApplicationId | — |
| APPROVAL_DESCRIPTION | ApInvoicesAllApprovalDescription | — |
| APPROVAL_ITERATION | ApInvoicesAllApprovalIteration | — |
| APPROVAL_READY_FLAG | ApInvoicesAllApprovalReadyFlag | — |
| APPROVAL_STATUS | ApInvoicesAllApprovalStatus | — |
| APPROVED_AMOUNT | ApInvoicesAllApprovedAmount | — |
| AWARD_ID | ApInvoicesAllAwardId | — |
| AWT_FLAG | ApInvoicesAllAwtFlag | — |
| AWT_GROUP_ID | ApInvoicesAllAwtGroupId | — |
| BANK_CHARGE_BEARER | ApInvoicesAllBankChargeBearer | — |
| BASE_AMOUNT | ApInvoicesAllBaseAmount | — |
| BATCH_ID | ApInvoicesAllBatchId | — |
| BUDGET_DATE | ApInvoicesAllBudgetDate | — |
| CANCELLED_AMOUNT | ApInvoicesAllCancelledAmount | — |
| CANCELLED_BY | ApInvoicesAllCancelledBy | — |
| CANCELLED_DATE | ApInvoicesAllCancelledDate | — |
| CHECK_VAT_AMOUNT_PAID | ApInvoicesAllCheckVatAmountPaid | — |
| CONTROL_AMOUNT | ApInvoicesAllControlAmount | — |
| CORRECTION_PERIOD | ApInvoicesAllCorrectionPeriod | — |
| CORRECTION_YEAR | ApInvoicesAllCorrectionYear | — |
| CREATED_BY | ApInvoicesAllCreatedBy | — |
| CREATION_DATE | ApInvoicesAllCreationDate | — |
| CREDITED_INVOICE_ID | ApInvoicesAllCreditedInvoiceId | — |
| CUST_REGISTRATION_CODE | ApInvoicesAllCustRegistrationCode | — |
| CUST_REGISTRATION_NUMBER | ApInvoicesAllCustRegistrationNumber | — |
| DATA_SET_ID | ApInvoicesAllDataSetId | — |
| DELIVERY_CHANNEL_CODE | ApInvoicesAllDeliveryChannelCode | — |
| DESCRIPTION | ApInvoicesAllDescription | — |
| DISC_IS_INV_LESS_TAX_FLAG | ApInvoicesAllDiscIsInvLessTaxFlag | — |
| DISCOUNT_AMOUNT_TAKEN | ApInvoicesAllDiscountAmountTaken | — |
| DISTRIBUTION_SET_ID | ApInvoicesAllDistributionSetId | — |
| DOC_CATEGORY_CODE | ApInvoicesAllDocCategoryCode | — |
| DOC_SEQUENCE_ID | ApInvoicesAllDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ApInvoicesAllDocSequenceValue | — |
| DOCUMENT_SUB_TYPE | ApInvoicesAllDocumentSubType | — |
| EARLIEST_SETTLEMENT_DATE | ApInvoicesAllEarliestSettlementDate | — |
| EMPLOYEE_ADDRESS_CODE | ApInvoicesAllEmployeeAddressCode | — |
| EXCHANGE_DATE | ApInvoicesAllExchangeDate | — |
| EXCHANGE_RATE | ApInvoicesAllExchangeRate | — |
| EXCHANGE_RATE_TYPE | ApInvoicesAllExchangeRateType | — |
| EXCLUDE_FREIGHT_FROM_DISCOUNT | ApInvoicesAllExcludeFreightFromDiscount | — |
| EXCLUSIVE_PAYMENT_FLAG | ApInvoicesAllExclusivePaymentFlag | — |
| EXPENDITURE_ITEM_DATE | ApInvoicesAllExpenditureItemDate | — |
| EXPENDITURE_ORGANIZATION_ID | ApInvoicesAllExpenditureOrganizationId | — |
| EXPENDITURE_TYPE | ApInvoicesAllExpenditureType | — |
| EXTERNAL_BANK_ACCOUNT_ID | ApInvoicesAllExternalBankAccountId | — |
| FIRST_PARTY_REGISTRATION_ID | ApInvoicesAllFirstPartyRegistrationId | — |
| FISCAL_DOC_ACCESS_KEY | ApInvoicesAllFiscalDocAccessKey | — |
| FORCE_REVALIDATION_FLAG | ApInvoicesAllForceRevalidationFlag | — |
| FREIGHT_AMOUNT | ApInvoicesAllFreightAmount | — |
| FUNDS_STATUS | ApInvoicesAllFundsStatus | — |
| GL_DATE | ApInvoicesAllGlDate | — |
| GOODS_RECEIVED_DATE | ApInvoicesAllGoodsReceivedDate | — |
| HISTORICAL_FLAG | ApInvoicesAllHistoricalFlag | — |
| IMAGE_DOCUMENT_NUM | ApInvoicesAllImageDocumentNum | — |
| IMPORT_DOCUMENT_DATE | ApInvoicesAllImportDocumentDate | — |
| IMPORT_DOCUMENT_NUMBER | ApInvoicesAllImportDocumentNumber | — |
| INTERCOMPANY_FLAG | ApInvoicesAllIntercompanyFlag | — |
| INTERNAL_CONTACT_EMAIL | ApInvoicesAllInternalContactEmail | — |
| INVOICE_AMOUNT | ApInvoicesAllInvoiceAmount | — |
| INVOICE_CURRENCY_CODE | ApInvoicesAllInvoiceCurrencyCode | — |
| INVOICE_DATE | ApInvoicesAllInvoiceDate | — |
| INVOICE_ID | ApInvoicesAllInvoiceId | — |
| INVOICE_NUM | ApInvoicesAllInvoiceNum | — |
| INVOICE_RECEIVED_DATE | ApInvoicesAllInvoiceReceivedDate | — |
| INVOICE_TYPE_LOOKUP_CODE | ApInvoicesAllInvoiceTypeLookupCode | — |
| JOB_DEFINITION_NAME | ApInvoicesAllJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | ApInvoicesAllJobDefinitionPackage | — |
| LAST_UPDATE_DATE | ApInvoicesAllLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ApInvoicesAllLastUpdateLogin | — |
| LAST_UPDATED_BY | ApInvoicesAllLastUpdatedBy | — |
| LEGAL_ENTITY_ID | ApInvoicesAllLegalEntityId | — |
| LOCK_TIME | ApInvoicesAllLockTime | — |
| LOCKED_BY | ApInvoicesAllLockedBy | — |
| MERGE_REQUEST_ID | ApInvoicesAllMergeRequestId | — |
| MRC_BASE_AMOUNT | ApInvoicesAllMrcBaseAmount | — |
| MRC_EXCHANGE_DATE | ApInvoicesAllMrcExchangeDate | — |
| MRC_EXCHANGE_RATE | ApInvoicesAllMrcExchangeRate | — |
| MRC_EXCHANGE_RATE_TYPE | ApInvoicesAllMrcExchangeRateType | — |
| MRC_POSTING_STATUS | ApInvoicesAllMrcPostingStatus | — |
| NET_OF_RETAINAGE_FLAG | ApInvoicesAllNetOfRetainageFlag | — |
| OBJECT_VERSION_NUMBER | ApInvoicesAllObjectVersionNumber | — |
| ORG_ID | ApInvoicesAllOrgId | — |
| PA_DEFAULT_DIST_CCID | ApInvoicesAllPaDefaultDistCcid | — |
| PA_QUANTITY | ApInvoicesAllPaQuantity | — |
| PAID_ON_BEHALF_EMPLOYEE_ID | ApInvoicesAllPaidOnBehalfEmployeeId | — |
| PARTY_ID | ApInvoicesAllPartyId | — |
| PARTY_SITE_ID | ApInvoicesAllPartySiteId | — |
| PAY_CURR_INVOICE_AMOUNT | ApInvoicesAllPayCurrInvoiceAmount | — |
| PAY_GROUP_LOOKUP_CODE | ApInvoicesAllPayGroupLookupCode | — |
| PAY_PROC_TRXN_TYPE_CODE | ApInvoicesAllPayProcTrxnTypeCode | — |
| PAYMENT_AMOUNT_TOTAL | ApInvoicesAllPaymentAmountTotal | — |
| PAYMENT_CROSS_RATE | ApInvoicesAllPaymentCrossRate | — |
| PAYMENT_CROSS_RATE_DATE | ApInvoicesAllPaymentCrossRateDate | — |
| PAYMENT_CROSS_RATE_TYPE | ApInvoicesAllPaymentCrossRateType | — |
| PAYMENT_CURRENCY_CODE | ApInvoicesAllPaymentCurrencyCode | — |
| PAYMENT_FUNCTION | ApInvoicesAllPaymentFunction | — |
| PAYMENT_METHOD_CODE | ApInvoicesAllPaymentMethodCode | — |
| PAYMENT_METHOD_LOOKUP_CODE | ApInvoicesAllPaymentMethodLookupCode | — |
| PAYMENT_REASON_CODE | ApInvoicesAllPaymentReasonCode | — |
| PAYMENT_REASON_COMMENTS | ApInvoicesAllPaymentReasonComments | — |
| PAYMENT_STATUS_FLAG | ApInvoicesAllPaymentStatusFlag | — |
| PO_HEADER_ID | ApInvoicesAllPoHeaderId | — |
| PO_MATCHED_FLAG | ApInvoicesAllPoMatchedFlag | — |
| PORT_OF_ENTRY_CODE | ApInvoicesAllPortOfEntryCode | — |
| POSTING_STATUS | ApInvoicesAllPostingStatus | — |
| PRE_WITHHOLDING_AMOUNT | ApInvoicesAllPreWithholdingAmount | — |
| PRODUCT_TABLE | ApInvoicesAllProductTable | — |
| PROJECT_ID | ApInvoicesAllProjectId | — |
| QUICK_CREDIT | ApInvoicesAllQuickCredit | — |
| QUICK_PO_HEADER_ID | ApInvoicesAllQuickPoHeaderId | — |
| RECURRING_PAYMENT_ID | ApInvoicesAllRecurringPaymentId | — |
| REFERENCE_1 | ApInvoicesAllReference1 | — |
| REFERENCE_2 | ApInvoicesAllReference2 | — |
| REFERENCE_KEY1 | ApInvoicesAllReferenceKey1 | — |
| REFERENCE_KEY2 | ApInvoicesAllReferenceKey2 | — |
| REFERENCE_KEY3 | ApInvoicesAllReferenceKey3 | — |
| REFERENCE_KEY4 | ApInvoicesAllReferenceKey4 | — |
| REFERENCE_KEY5 | ApInvoicesAllReferenceKey5 | — |
| RELEASE_AMOUNT_NET_OF_TAX | ApInvoicesAllReleaseAmountNetOfTax | — |
| REMITTANCE_MESSAGE1 | ApInvoicesAllRemittanceMessage1 | — |
| REMITTANCE_MESSAGE2 | ApInvoicesAllRemittanceMessage2 | — |
| REMITTANCE_MESSAGE3 | ApInvoicesAllRemittanceMessage3 | — |
| REQUEST_ID | ApInvoicesAllRequestId | — |
| REQUESTER_ID | ApInvoicesAllRequesterId | — |
| ROUTING_STATUS_LOOKUP_CODE | ApInvoicesAllRoutingStatusLookupCode | — |
| SELF_ASSESSED_TAX_AMOUNT | ApInvoicesAllSelfAssessedTaxAmount | — |
| SET_OF_BOOKS_ID | ApInvoicesAllSetOfBooksId | — |
| SETTLEMENT_PRIORITY | ApInvoicesAllSettlementPriority | — |
| SOURCE | ApInvoicesAllSource | — |
| SUPPLIER_TAX_EXCHANGE_RATE | ApInvoicesAllSupplierTaxExchangeRate | — |
| SUPPLIER_TAX_INVOICE_DATE | ApInvoicesAllSupplierTaxInvoiceDate | — |
| SUPPLIER_TAX_INVOICE_NUMBER | ApInvoicesAllSupplierTaxInvoiceNumber | — |
| TASK_ID | ApInvoicesAllTaskId | — |
| TAX_INVOICE_INTERNAL_SEQ | ApInvoicesAllTaxInvoiceInternalSeq | — |
| TAX_INVOICE_RECORDING_DATE | ApInvoicesAllTaxInvoiceRecordingDate | — |
| TAX_RELATED_INVOICE_ID | ApInvoicesAllTaxRelatedInvoiceId | — |
| TAXATION_COUNTRY | ApInvoicesAllTaxationCountry | — |
| TEMP_CANCELLED_AMOUNT | ApInvoicesAllTempCancelledAmount | — |
| TERMS_DATE | ApInvoicesAllTermsDate | — |
| TERMS_ID | ApInvoicesAllTermsId | — |
| THIRD_PARTY_REGISTRATION_ID | ApInvoicesAllThirdPartyRegistrationId | — |
| TOTAL_TAX_AMOUNT | ApInvoicesAllTotalTaxAmount | — |
| TRANSACTION_DEADLINE | ApInvoicesAllTransactionDeadline | — |
| TRX_BUSINESS_CATEGORY | ApInvoicesAllTrxBusinessCategory | — |
| UNIQUE_REMITTANCE_IDENTIFIER | ApInvoicesAllUniqueRemittanceIdentifier | — |
| URI_CHECK_DIGIT | ApInvoicesAllUriCheckDigit | — |
| USER_DEFINED_FISC_CLASS | ApInvoicesAllUserDefinedFiscClass | — |
| USSGL_TRANSACTION_CODE | ApInvoicesAllUssglTransactionCode | — |
| USSGL_TRX_CODE_CONTEXT | ApInvoicesAllUssglTrxCodeContext | — |
| VALIDATED_TAX_AMOUNT | ApInvoicesAllValidatedTaxAmount | — |
| VALIDATION_REQUEST_ID | ApInvoicesAllValidationRequestId | — |
| VALIDATION_WORKER_ID | ApInvoicesAllValidationWorkerId | — |
| VENDOR_CONTACT_ID | ApInvoicesAllVendorContactId | — |
| VENDOR_ID | ApInvoicesAllVendorId | — |
| VENDOR_SITE_ID | ApInvoicesAllVendorSiteId | — |
| VOUCHER_NUM | ApInvoicesAllVoucherNum | — |
| WFAPPROVAL_STATUS | ApInvoicesAllWfapprovalStatus | — |

### [[invoiceheaderholdspvo|InvoiceHeaderHoldsPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EARLIEST_SETTLEMENT_DATE | InvoiceHeaderEarliestSettlementDate | — |
| EXCHANGE_DATE | InvoiceHeaderExchangeDate | — |
| EXCHANGE_RATE | InvoiceHeaderExchangeRate | — |
| EXCHANGE_RATE_TYPE | InvoiceHeaderExchangeRateType | — |
| INVOICE_AMOUNT | InvoiceHeaderInvoiceAmount | — |
| INVOICE_CURRENCY_CODE | InvoiceHeaderInvoiceCurrencyCode | — |
| INVOICE_DATE | InvoiceHeaderInvoiceDate | — |
| INVOICE_ID | InvoiceHeaderInvoiceId | — |
| INVOICE_NUM | InvoiceHeaderInvoiceNum | — |
| LEGAL_ENTITY_ID | InvoiceHeaderLegalEntityId | — |
| OBJECT_VERSION_NUMBER | InvoiceHeaderObjectVersionNumber | — |
| ORG_ID | InvoiceHeaderOrgId | — |
| PARTY_ID | InvoiceHeaderPartyId | — |
| PARTY_SITE_ID | InvoiceHeaderPartySiteId | — |
| PAYMENT_METHOD_CODE | InvoiceHeaderPaymentMethodCode | — |
| SET_OF_BOOKS_ID | InvoiceHeaderSetOfBooksId | — |
| SOURCE | InvoiceHeaderSource | — |
| TERMS_ID | InvoiceHeaderTermsId | — |
| VENDOR_SITE_ID | InvoiceHeaderVendorSiteId | — |

### [[invoiceheaderpvo|InvoiceHeaderPVO]] (AP · BICC: 72/160)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTS_PAY_CODE_COMBINATION_ID | InvoiceHeaderAcctsPayCodeCombinationId | — |
| AMOUNT_APPLICABLE_TO_DISCOUNT | InvoiceHeaderAmountApplicableToDiscount | ✅ |
| AMOUNT_PAID | InvoiceHeaderAmountPaid | ✅ |
| AMT_DUE_CCARD_COMPANY | InvoiceHeaderAmtDueCcardCompany | — |
| AMT_DUE_EMPLOYEE | InvoiceHeaderAmtDueEmployee | — |
| APPLICATION_ID | InvoiceHeaderApplicationId | — |
| APPROVAL_DESCRIPTION | InvoiceHeaderApprovalDescription | ✅ |
| APPROVAL_ITERATION | InvoiceHeaderApprovalIteration | ✅ |
| APPROVAL_READY_FLAG | InvoiceHeaderApprovalReadyFlag | — |
| APPROVAL_STATUS | InvoiceHeaderApprovalStatus | ✅ |
| APPROVED_AMOUNT | InvoiceHeaderApprovedAmount | — |
| AWARD_ID | InvoiceHeaderAwardId | — |
| AWT_FLAG | InvoiceHeaderAwtFlag | — |
| AWT_GROUP_ID | InvoiceHeaderAwtGroupId | — |
| BANK_CHARGE_BEARER | InvoiceHeaderBankChargeBearer | — |
| BASE_AMOUNT | InvoiceHeaderBaseAmount | ✅ |
| BATCH_ID | InvoiceHeaderBatchId | — |
| BUDGET_DATE | InvoiceHeaderBudgetDate | ✅ |
| CANCELLED_AMOUNT | InvoiceHeaderCancelledAmount | ✅ |
| CANCELLED_BY | InvoiceHeaderCancelledBy | ✅ |
| CANCELLED_DATE | InvoiceHeaderCancelledDate | ✅ |
| CHECK_VAT_AMOUNT_PAID | InvoiceHeaderCheckVatAmountPaid | — |
| CONTROL_AMOUNT | InvoiceHeaderControlAmount | ✅ |
| CORRECTION_PERIOD | InvoiceHeaderCorrectionPeriod | ✅ |
| CORRECTION_YEAR | InvoiceHeaderCorrectionYear | ✅ |
| CREATED_BY | InvoiceHeaderCreatedBy | ✅ |
| CREATION_DATE | InvoiceHeaderCreationDate | ✅ |
| CREDITED_INVOICE_ID | InvoiceHeaderCreditedInvoiceId | — |
| CUST_REGISTRATION_CODE | InvoiceHeaderCustRegistrationCode | — |
| CUST_REGISTRATION_NUMBER | InvoiceHeaderCustRegistrationNumber | — |
| DELIVERY_CHANNEL_CODE | InvoiceHeaderDeliveryChannelCode | — |
| DESCRIPTION | InvoiceHeaderDescription | ✅ |
| DISC_IS_INV_LESS_TAX_FLAG | InvoiceHeaderDiscIsInvLessTaxFlag | — |
| DISCOUNT_AMOUNT_TAKEN | InvoiceHeaderDiscountAmountTaken | ✅ |
| DISTRIBUTION_SET_ID | InvoiceHeaderDistributionSetId | — |
| DOC_CATEGORY_CODE | InvoiceHeaderDocCategoryCode | ✅ |
| DOC_SEQUENCE_ID | InvoiceHeaderDocSequenceId | — |
| DOC_SEQUENCE_VALUE | InvoiceHeaderDocSequenceValue | ✅ |
| DOCUMENT_SUB_TYPE | InvoiceHeaderDocumentSubType | — |
| EARLIEST_SETTLEMENT_DATE | InvoiceHeaderEarliestSettlementDate | ✅ |
| EMPLOYEE_ADDRESS_CODE | InvoiceHeaderEmployeeAddressCode | — |
| EXCHANGE_DATE | InvoiceHeaderExchangeDate | ✅ |
| EXCHANGE_RATE | InvoiceHeaderExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | InvoiceHeaderExchangeRateType | — |
| EXCLUDE_FREIGHT_FROM_DISCOUNT | InvoiceHeaderExcludeFreightFromDiscount | ✅ |
| EXCLUSIVE_PAYMENT_FLAG | InvoiceHeaderExclusivePaymentFlag | ✅ |
| EXPENDITURE_ITEM_DATE | InvoiceHeaderExpenditureItemDate | — |
| EXPENDITURE_ORGANIZATION_ID | InvoiceHeaderExpenditureOrganizationId | — |
| EXPENDITURE_TYPE | InvoiceHeaderExpenditureType | — |
| EXTERNAL_BANK_ACCOUNT_ID | InvoiceHeaderExternalBankAccountId | — |
| FISCAL_DOC_ACCESS_KEY | InvoiceHeaderFiscalDocAccessKey | — |
| FORCE_REVALIDATION_FLAG | InvoiceHeaderForceRevalidationFlag | — |
| FREIGHT_AMOUNT | InvoiceHeaderFreightAmount | ✅ |
| FUNDS_STATUS | InvoiceHeaderFundsStatus | ✅ |
| GL_DATE | InvoiceHeaderGlDate | ✅ |
| GOODS_RECEIVED_DATE | InvoiceHeaderGoodsReceivedDate | ✅ |
| HISTORICAL_FLAG | InvoiceHeaderHistoricalFlag | — |
| IMPORT_DOCUMENT_DATE | InvoiceHeaderImportDocumentDate | ✅ |
| IMPORT_DOCUMENT_NUMBER | InvoiceHeaderImportDocumentNumber | — |
| INTERCOMPANY_FLAG | InvoiceHeaderIntercompanyFlag | ✅ |
| INTERNAL_CONTACT_EMAIL | InvoiceHeaderInternalContactEmail | — |
| INVOICE_AMOUNT | InvoiceHeaderInvoiceAmount | ✅ |
| INVOICE_CURRENCY_CODE | InvoiceHeaderInvoiceCurrencyCode | ✅ |
| INVOICE_DATE | InvoiceHeaderInvoiceDate | ✅ |
| INVOICE_ID | InvHdrCrInvInvoiceId | — |
| INVOICE_ID | InvHdrTaxRelInvInvoiceId | — |
| INVOICE_ID | InvoiceId | ✅ |
| INVOICE_NUM | InvHdrCrInvInvoiceNum | ✅ |
| INVOICE_NUM | InvHdrTaxRelInvInvoiceNum | ✅ |
| INVOICE_NUM | InvoiceHeaderInvoiceNum | ✅ |
| INVOICE_RECEIVED_DATE | InvoiceHeaderInvoiceReceivedDate | ✅ |
| INVOICE_TYPE_LOOKUP_CODE | InvoiceHeaderInvoiceTypeLookupCode | ✅ |
| LAST_UPDATE_DATE | InvoiceHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvoiceHeaderLastUpdateLogin | — |
| LAST_UPDATED_BY | InvoiceHeaderLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | InvoiceHeaderLegalEntityId | — |
| MRC_BASE_AMOUNT | InvoiceHeaderMrcBaseAmount | — |
| MRC_EXCHANGE_DATE | InvoiceHeaderMrcExchangeDate | — |
| MRC_EXCHANGE_RATE | InvoiceHeaderMrcExchangeRate | — |
| MRC_EXCHANGE_RATE_TYPE | InvoiceHeaderMrcExchangeRateType | — |
| MRC_POSTING_STATUS | InvoiceHeaderMrcPostingStatus | — |
| NET_OF_RETAINAGE_FLAG | InvoiceHeaderNetOfRetainageFlag | ✅ |
| OBJECT_VERSION_NUMBER | InvoiceHeaderObjectVersionNumber | — |
| ORG_ID | InvoiceHeaderOrgId | — |
| PA_DEFAULT_DIST_CCID | InvoiceHeaderPaDefaultDistCcid | — |
| PA_QUANTITY | InvoiceHeaderPaQuantity | — |
| PAID_ON_BEHALF_EMPLOYEE_ID | InvoiceHeaderPaidOnBehalfEmployeeId | — |
| PARTY_ID | InvoiceHeaderPartyId | — |
| PARTY_SITE_ID | InvoiceHeaderPartySiteId | — |
| PAY_CURR_INVOICE_AMOUNT | InvoiceHeaderPayCurrInvoiceAmount | — |
| PAY_GROUP_LOOKUP_CODE | InvoiceHeaderPayGroupLookupCode | ✅ |
| PAY_PROC_TRXN_TYPE_CODE | InvoiceHeaderPayProcTrxnTypeCode | — |
| PAYMENT_AMOUNT_TOTAL | InvoiceHeaderPaymentAmountTotal | ✅ |
| PAYMENT_CROSS_RATE | InvoiceHeaderPaymentCrossRate | ✅ |
| PAYMENT_CROSS_RATE_DATE | InvoiceHeaderPaymentCrossRateDate | ✅ |
| PAYMENT_CROSS_RATE_TYPE | InvoiceHeaderPaymentCrossRateType | ✅ |
| PAYMENT_CURRENCY_CODE | InvoiceHeaderPaymentCurrencyCode | ✅ |
| PAYMENT_FUNCTION | InvoiceHeaderPaymentFunction | — |
| PAYMENT_METHOD_CODE | InvoiceHeaderPaymentMethodCode | — |
| PAYMENT_METHOD_LOOKUP_CODE | InvoiceHeaderPaymentMethodLookupCode | — |
| PAYMENT_REASON_CODE | InvoiceHeaderPaymentReasonCode | — |
| PAYMENT_REASON_COMMENTS | InvoiceHeaderPaymentReasonComments | ✅ |
| PAYMENT_STATUS_FLAG | InvoiceHeaderPaymentStatusFlag | ✅ |
| PO_HEADER_ID | InvoiceHeaderPoHeaderId | — |
| PORT_OF_ENTRY_CODE | InvoiceHeaderPortOfEntryCode | ✅ |
| POSTING_STATUS | InvoiceHeaderPostingStatus | ✅ |
| PRE_WITHHOLDING_AMOUNT | InvoiceHeaderPreWithholdingAmount | — |
| PRODUCT_TABLE | InvoiceHeaderProductTable | — |
| PROJECT_ID | InvoiceHeaderProjectId | — |
| QUICK_CREDIT | InvoiceHeaderQuickCredit | — |
| QUICK_PO_HEADER_ID | InvoiceHeaderQuickPoHeaderId | — |
| RECURRING_PAYMENT_ID | InvoiceHeaderRecurringPaymentId | — |
| REFERENCE_1 | InvoiceHeaderReference1 | — |
| REFERENCE_2 | InvoiceHeaderReference2 | — |
| REFERENCE_KEY1 | InvoiceHeaderReferenceKey1 | — |
| REFERENCE_KEY2 | InvoiceHeaderReferenceKey2 | — |
| REFERENCE_KEY3 | InvoiceHeaderReferenceKey3 | — |
| REFERENCE_KEY4 | InvoiceHeaderReferenceKey4 | — |
| REFERENCE_KEY5 | InvoiceHeaderReferenceKey5 | — |
| RELEASE_AMOUNT_NET_OF_TAX | InvoiceHeaderReleaseAmountNetOfTax | ✅ |
| REMITTANCE_MESSAGE1 | InvoiceHeaderRemittanceMessage1 | — |
| REMITTANCE_MESSAGE2 | InvoiceHeaderRemittanceMessage2 | — |
| REMITTANCE_MESSAGE3 | InvoiceHeaderRemittanceMessage3 | — |
| REQUESTER_ID | InvoiceHeaderRequesterId | — |
| ROUTING_ATTRIBUTE1 | InvoiceHeaderRoutingAttribute1 | ✅ |
| ROUTING_ATTRIBUTE2 | InvoiceHeaderRoutingAttribute2 | ✅ |
| ROUTING_ATTRIBUTE3 | InvoiceHeaderRoutingAttribute3 | ✅ |
| ROUTING_ATTRIBUTE4 | InvoiceHeaderRoutingAttribute4 | ✅ |
| ROUTING_ATTRIBUTE5 | InvoiceHeaderRoutingAttribute5 | — |
| ROUTING_STATUS_LOOKUP_CODE | InvoiceHeaderRoutingStatusLookupCode | ✅ |
| SELF_ASSESSED_TAX_AMOUNT | InvoiceHeaderSelfAssessedTaxAmount | ✅ |
| SET_OF_BOOKS_ID | InvoiceHeaderSetOfBooksId | — |
| SETTLEMENT_PRIORITY | InvoiceHeaderSettlementPriority | ✅ |
| SOURCE | InvoiceHeaderSource | — |
| SUPPLIER_TAX_EXCHANGE_RATE | InvoiceHeaderSupplierTaxExchangeRate | ✅ |
| SUPPLIER_TAX_INVOICE_DATE | InvoiceHeaderSupplierTaxInvoiceDate | ✅ |
| SUPPLIER_TAX_INVOICE_NUMBER | InvoiceHeaderSupplierTaxInvoiceNumber | ✅ |
| TASK_ID | InvoiceHeaderTaskId | — |
| TAX_INVOICE_INTERNAL_SEQ | InvoiceHeaderTaxInvoiceInternalSeq | ✅ |
| TAX_INVOICE_RECORDING_DATE | InvoiceHeaderTaxInvoiceRecordingDate | ✅ |
| TAX_RELATED_INVOICE_ID | InvoiceHeaderTaxRelatedInvoiceId | — |
| TAXATION_COUNTRY | InvoiceHeaderTaxationCountry | ✅ |
| TEMP_CANCELLED_AMOUNT | InvoiceHeaderTempCancelledAmount | — |
| TERMS_DATE | InvoiceHeaderTermsDate | ✅ |
| TERMS_ID | InvoiceHeaderTermsId | — |
| TOTAL_TAX_AMOUNT | InvoiceHeaderTotalTaxAmount | ✅ |
| TRANSACTION_DEADLINE | InvoiceHdrTransactionDeadline | ✅ |
| TRX_BUSINESS_CATEGORY | InvoiceHeaderTrxBusinessCategory | — |
| UNIQUE_REMITTANCE_IDENTIFIER | InvoiceHeaderUniqueRemittanceIdentifier | ✅ |
| URI_CHECK_DIGIT | InvoiceHeaderUriCheckDigit | — |
| USER_DEFINED_FISC_CLASS | InvoiceHeaderUserDefinedFiscClass | — |
| USSGL_TRANSACTION_CODE | InvoiceHeaderUssglTransactionCode | — |
| USSGL_TRX_CODE_CONTEXT | InvoiceHeaderUssglTrxCodeContext | — |
| VALIDATED_TAX_AMOUNT | InvoiceHeaderValidatedTaxAmount | — |
| VALIDATION_REQUEST_ID | InvoiceHeaderValidationRequestId | — |
| VENDOR_CONTACT_ID | InvoiceHeaderVendorContactId | — |
| VENDOR_ID | InvoiceHeaderVendorId | — |
| VENDOR_SITE_ID | InvoiceHeaderVendorSiteId | — |
| VOUCHER_NUM | InvoiceHeaderVoucherNum | ✅ |
| WFAPPROVAL_STATUS | InvoiceHeaderWfapprovalStatus | ✅ |

### [[invoiceholdpvo|InvoiceHoldPVO]] (AP · BICC: 15/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EARLIEST_SETTLEMENT_DATE | InvoiceHeaderEarliestSettlementDate | — |
| EXCHANGE_DATE | InvoiceHeaderExchangeDate | ✅ |
| EXCHANGE_RATE | InvoiceHeaderExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | InvoiceHeaderExchangeRateType | ✅ |
| INVOICE_AMOUNT | InvoiceHeaderInvoiceAmount | ✅ |
| INVOICE_CURRENCY_CODE | InvoiceHeaderInvoiceCurrencyCode | ✅ |
| INVOICE_DATE | InvoiceHeaderInvoiceDate | ✅ |
| INVOICE_ID | InvoiceHeaderInvoiceId | — |
| INVOICE_NUM | InvoiceHeaderInvoiceNum | ✅ |
| LEGAL_ENTITY_ID | InvoiceHeaderLegalEntityId | ✅ |
| OBJECT_VERSION_NUMBER | InvoiceHeaderObjectVersionNumber | — |
| ORG_ID | InvoiceHeaderOrgId | ✅ |
| PARTY_ID | InvoiceHeaderPartyId | ✅ |
| PARTY_SITE_ID | InvoiceHeaderPartySiteId | — |
| PAYMENT_METHOD_CODE | InvoiceHeaderPaymentMethodCode | ✅ |
| SET_OF_BOOKS_ID | InvoiceHeaderSetOfBooksId | ✅ |
| SOURCE | InvoiceHeaderSource | ✅ |
| TERMS_ID | InvoiceHeaderTermsId | ✅ |
| VENDOR_SITE_ID | InvoiceHeaderVendorSiteId | ✅ |

### [[invoiceholdpvoactiveholds|InvoiceHoldPVOActiveHolds]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EARLIEST_SETTLEMENT_DATE | InvoiceHeaderEarliestSettlementDate | — |
| EXCHANGE_DATE | InvoiceHeaderExchangeDate | — |
| EXCHANGE_RATE | InvoiceHeaderExchangeRate | — |
| EXCHANGE_RATE_TYPE | InvoiceHeaderExchangeRateType | — |
| INVOICE_AMOUNT | InvoiceHeaderInvoiceAmount | — |
| INVOICE_CURRENCY_CODE | InvoiceHeaderInvoiceCurrencyCode | — |
| INVOICE_DATE | InvoiceHeaderInvoiceDate | — |
| INVOICE_ID | InvoiceHeaderInvoiceId | — |
| INVOICE_NUM | InvoiceHeaderInvoiceNum | — |
| LEGAL_ENTITY_ID | InvoiceHeaderLegalEntityId | — |
| OBJECT_VERSION_NUMBER | InvoiceHeaderObjectVersionNumber | — |
| ORG_ID | InvoiceHeaderOrgId | — |
| PARTY_ID | InvoiceHeaderPartyId | — |
| PARTY_SITE_ID | InvoiceHeaderPartySiteId | — |
| PAYMENT_METHOD_CODE | InvoiceHeaderPaymentMethodCode | — |
| SET_OF_BOOKS_ID | InvoiceHeaderSetOfBooksId | — |
| SOURCE | InvoiceHeaderSource | — |
| TERMS_ID | InvoiceHeaderTermsId | — |
| VENDOR_SITE_ID | InvoiceHeaderVendorSiteId | — |

### [[invoicelineholdspvo|InvoiceLineHoldsPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EARLIEST_SETTLEMENT_DATE | InvoiceHeaderEarliestSettlementDate | — |
| EXCHANGE_DATE | InvoiceHeaderExchangeDate | — |
| EXCHANGE_RATE | InvoiceHeaderExchangeRate | — |
| EXCHANGE_RATE_TYPE | InvoiceHeaderExchangeRateType | — |
| INVOICE_AMOUNT | InvoiceHeaderInvoiceAmount | — |
| INVOICE_CURRENCY_CODE | InvoiceHeaderInvoiceCurrencyCode | — |
| INVOICE_DATE | InvoiceHeaderInvoiceDate | — |
| INVOICE_ID | InvoiceHeaderInvoiceId | — |
| INVOICE_NUM | InvoiceHeaderInvoiceNum | — |
| LEGAL_ENTITY_ID | InvoiceHeaderLegalEntityId | — |
| OBJECT_VERSION_NUMBER | InvoiceHeaderObjectVersionNumber | — |
| ORG_ID | InvoiceHeaderOrgId | — |
| PARTY_ID | InvoiceHeaderPartyId | — |
| PARTY_SITE_ID | InvoiceHeaderPartySiteId | — |
| PAYMENT_METHOD_CODE | InvoiceHeaderPaymentMethodCode | — |
| SET_OF_BOOKS_ID | InvoiceHeaderSetOfBooksId | — |
| SOURCE | InvoiceHeaderSource | — |
| TERMS_ID | InvoiceHeaderTermsId | — |
| VENDOR_SITE_ID | InvoiceHeaderVendorSiteId | — |

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 63/90)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTS_PAY_CODE_COMBINATION_ID | InvoiceHeaderAcctsPayCodeCombinationId | — |
| APPROVAL_DESCRIPTION | InvoiceHeaderApprovalDescription | ✅ |
| APPROVAL_ITERATION | InvoiceHeaderApprovalIteration | ✅ |
| APPROVAL_STATUS | InvoiceHeaderApprovalStatus | ✅ |
| BUDGET_DATE | InvoiceHeaderBudgetDate | ✅ |
| CANCELLED_BY | InvoiceHeaderCancelledBy | ✅ |
| CANCELLED_DATE | InvoiceHeaderCancelledDate | ✅ |
| CORRECTION_PERIOD | InvoiceHeaderCorrectionPeriod | ✅ |
| CORRECTION_YEAR | InvoiceHeaderCorrectionYear | ✅ |
| CREATED_BY | InvoiceHeaderCreatedBy | ✅ |
| CREATION_DATE | InvoiceHeaderCreationDate | ✅ |
| DESCRIPTION | InvoiceHeaderDescription | ✅ |
| DOC_CATEGORY_CODE | InvoiceHeaderDocCategoryCode | ✅ |
| DOC_SEQUENCE_ID | InvoiceHeaderDocSequenceId | — |
| DOC_SEQUENCE_VALUE | InvoiceHeaderDocSequenceValue | ✅ |
| EARLIEST_SETTLEMENT_DATE | InvoiceHeaderEarliestSettlementDate | ✅ |
| EXCHANGE_DATE | InvoiceHeaderExchangeDate | ✅ |
| EXCHANGE_RATE | InvoiceHeaderExchangeRate | ✅ |
| EXCLUDE_FREIGHT_FROM_DISCOUNT | InvoiceHeaderExcludeFreightFromDiscount | ✅ |
| EXCLUSIVE_PAYMENT_FLAG | InvoiceHeaderExclusivePaymentFlag | ✅ |
| FISCAL_DOC_ACCESS_KEY | InvoiceHeaderFiscalDocAccessKey | — |
| FUNDS_STATUS | InvoiceHeaderFundsStatus | ✅ |
| GL_DATE | InvoiceHeaderGlDate | ✅ |
| GOODS_RECEIVED_DATE | InvoiceHeaderGoodsReceivedDate | ✅ |
| INTERCOMPANY_FLAG | InvoiceHeaderIntercompanyFlag | ✅ |
| INVOICE_AMOUNT | InvoiceHeaderInvoiceAmount | — |
| INVOICE_CURRENCY_CODE | InvoiceHeaderInvoiceCurrencyCode | ✅ |
| INVOICE_DATE | InvoiceHeaderInvoiceDate | ✅ |
| INVOICE_ID | InvHdrCorrInvInvoiceId | — |
| INVOICE_ID | InvHdrCrInvInvoiceId | — |
| INVOICE_ID | InvHdrPreInvInvoiceId | — |
| INVOICE_ID | InvHdrTaxRelInvInvoiceId | — |
| INVOICE_ID | InvoiceHeaderInvoiceId | ✅ |
| INVOICE_ID | RetainedInvoiceInvoiceId | — |
| INVOICE_NUM | InvHdrCorrInvInvoiceNum | ✅ |
| INVOICE_NUM | InvHdrCrInvInvoiceNum | ✅ |
| INVOICE_NUM | InvHdrPreInvInvoiceNum | ✅ |
| INVOICE_NUM | InvHdrTaxRelInvInvoiceNum | ✅ |
| INVOICE_NUM | InvoiceHeaderInvoiceNum | ✅ |
| INVOICE_NUM | RetainedInvoiceInvoiceNum | ✅ |
| INVOICE_RECEIVED_DATE | InvoiceHeaderInvoiceReceivedDate | ✅ |
| INVOICE_TYPE_LOOKUP_CODE | InvoiceHeaderInvoiceTypeLookupCode | ✅ |
| LAST_UPDATE_DATE | InvoiceHeaderLastUpdateDate | ✅ |
| LAST_UPDATED_BY | InvoiceHeaderLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | InvoiceHeaderLegalEntityId | — |
| NET_OF_RETAINAGE_FLAG | InvoiceHeaderNetOfRetainageFlag | ✅ |
| OBJECT_VERSION_NUMBER | InvHdrTaxRelInvObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | InvLineAprvlPersonNameObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | InvoiceHeaderObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RetainedInvoiceObjectVersionNumber | — |
| ORG_ID | InvoiceHeaderOrgId | — |
| PARTY_ID | InvoiceHeaderPartyId | — |
| PARTY_SITE_ID | InvoiceHeaderPartySiteId | — |
| PAY_GROUP_LOOKUP_CODE | InvoiceHeaderPayGroupLookupCode | ✅ |
| PAYMENT_CROSS_RATE | InvoiceHeaderPaymentCrossRate | ✅ |
| PAYMENT_CROSS_RATE_DATE | InvoiceHeaderPaymentCrossRateDate | ✅ |
| PAYMENT_CROSS_RATE_TYPE | InvoiceHeaderPaymentCrossRateType | ✅ |
| PAYMENT_CURRENCY_CODE | InvoiceHeaderPaymentCurrencyCode | ✅ |
| PAYMENT_METHOD_CODE | InvoiceHeaderPaymentMethodCode | — |
| PAYMENT_METHOD_LOOKUP_CODE | InvoiceHeaderPaymentMethodLookupCode | — |
| PAYMENT_REASON_COMMENTS | InvoiceHeaderPaymentReasonComments | ✅ |
| PAYMENT_STATUS_FLAG | InvoiceHeaderPaymentStatusFlag | ✅ |
| PORT_OF_ENTRY_CODE | InvoiceHeaderPortOfEntryCode | ✅ |
| POSTING_STATUS | InvoiceHeaderPostingStatus | ✅ |
| RELEASE_AMOUNT_NET_OF_TAX | InvoiceHeaderReleaseAmountNetOfTax | — |
| ROUTING_ATTRIBUTE1 | InvoiceHeaderRoutingAttribute1 | ✅ |
| ROUTING_ATTRIBUTE2 | InvoiceHeaderRoutingAttribute2 | ✅ |
| ROUTING_ATTRIBUTE3 | InvoiceHeaderRoutingAttribute3 | ✅ |
| ROUTING_ATTRIBUTE4 | InvoiceHeaderRoutingAttribute4 | ✅ |
| ROUTING_ATTRIBUTE5 | InvoiceHeaderRoutingAttribute5 | — |
| ROUTING_STATUS_LOOKUP_CODE | InvoiceHeaderRoutingStatusLookupCode | ✅ |
| SET_OF_BOOKS_ID | InvoiceHeaderSetOfBooksId | — |
| SETTLEMENT_PRIORITY | InvoiceHeaderSettlementPriority | ✅ |
| SOURCE | InvoiceHeaderSource | ✅ |
| SUPPLIER_TAX_EXCHANGE_RATE | InvoiceHeaderSupplierTaxExchangeRate | ✅ |
| SUPPLIER_TAX_INVOICE_DATE | InvoiceHeaderSupplierTaxInvoiceDate | ✅ |
| SUPPLIER_TAX_INVOICE_NUMBER | InvoiceHeaderSupplierTaxInvoiceNumber | ✅ |
| TAX_INVOICE_INTERNAL_SEQ | InvoiceHeaderTaxInvoiceInternalSeq | ✅ |
| TAX_INVOICE_RECORDING_DATE | InvoiceHeaderTaxInvoiceRecordingDate | ✅ |
| TAXATION_COUNTRY | InvoiceHeaderTaxationCountry | ✅ |
| TERMS_DATE | InvoiceHeaderTermsDate | ✅ |
| TERMS_ID | InvoiceHeaderTermsId | — |
| TRANSACTION_DEADLINE | InvoiceHdrTransactionDeadline | ✅ |
| UNIQUE_REMITTANCE_IDENTIFIER | InvoiceHeaderUniqueRemittanceIdentifier | ✅ |
| USER_DEFINED_FISC_CLASS | InvoiceHeaderUserDefinedFiscClass | — |
| VENDOR_ID | InvoiceHeaderVendorId | — |
| VENDOR_SITE_ID | InvoiceHeaderVendorSiteId | — |
| VOUCHER_NUM | InvoiceHeaderVoucherNum | ✅ |
| WFAPPROVAL_STATUS | InvoiceHeaderWfapprovalStatus | ✅ |

### [[invoicepaymentschedulepvo|InvoicePaymentSchedulePVO]] (AP · BICC: 26/43)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTS_PAY_CODE_COMBINATION_ID | InvoiceHeaderAcctsPayCodeCombinationId | ✅ |
| BANK_CHARGE_BEARER | InvoiceHeaderBankChargeBearer | ✅ |
| BUDGET_DATE | InvoiceHeaderBudgetDate | ✅ |
| CANCELLED_DATE | InvoiceHeaderCancelledDate | ✅ |
| CORRECTION_PERIOD | InvoiceHeaderCorrectionPeriod | — |
| CORRECTION_YEAR | InvoiceHeaderCorrectionYear | — |
| CREATION_DATE | InvoiceHeaderCreationDate | ✅ |
| DESCRIPTION | InvoiceHeaderDescription | ✅ |
| DOC_CATEGORY_CODE | InvoiceHeaderDocCategoryCode | — |
| DOC_SEQUENCE_ID | InvoiceHeaderDocSequenceId | — |
| EMPLOYEE_ADDRESS_CODE | InvoiceHeaderEmployeeAddressCode | — |
| EXCHANGE_DATE | InvoiceHeaderExchangeDate | ✅ |
| EXCHANGE_RATE | InvoiceHeaderExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | InvoiceHeaderExchangeRateType | ✅ |
| EXPENDITURE_ITEM_DATE | InvoiceHeaderExpenditureItemDate | — |
| EXPENDITURE_ORGANIZATION_ID | InvoiceHeaderExpenditureOrganizationId | — |
| EXPENDITURE_TYPE | InvoiceHeaderExpenditureType | — |
| FUNDS_STATUS | InvoiceHeaderFundsStatus | ✅ |
| INVOICE_CURRENCY_CODE | InvoiceHeaderInvoiceCurrencyCode | ✅ |
| INVOICE_DATE | InvoiceHeaderInvoiceDate | ✅ |
| INVOICE_ID | InvoiceHeaderInvoiceId | — |
| INVOICE_NUM | InvoiceHeaderInvoiceNum | ✅ |
| INVOICE_RECEIVED_DATE | InvoiceHeaderInvoiceReceivedDate | ✅ |
| INVOICE_TYPE_LOOKUP_CODE | InvoiceHeaderInvoiceTypeLookupCode | ✅ |
| LAST_UPDATE_DATE | InvoiceHeaderLastUpdateDate | ✅ |
| LEGAL_ENTITY_ID | InvoiceHeaderLegalEntityId | ✅ |
| OBJECT_VERSION_NUMBER | InvoiceHeaderObjectVersionNumber | — |
| ORG_ID | InvoiceHeaderOrgId | ✅ |
| PARTY_ID | InvoiceHeaderPartyId | ✅ |
| PAYMENT_CURRENCY_CODE | InvoiceHeaderPaymentCurrencyCode | — |
| PAYMENT_METHOD_CODE | InvoiceHeaderPaymentMethodCode | ✅ |
| PAYMENT_METHOD_LOOKUP_CODE | InvoiceHeaderPaymentMethodLookupCode | — |
| PAYMENT_REASON_COMMENTS | InvoiceHeaderPaymentReasonComments | ✅ |
| PAYMENT_STATUS_FLAG | InvoiceHeaderPaymentStatusFlag | — |
| PROJECT_ID | InvoiceHeaderProjectId | — |
| REQUESTER_ID | InvoiceHeaderRequesterId | — |
| SET_OF_BOOKS_ID | InvoiceHeaderSetOfBooksId | ✅ |
| SOURCE | InvoiceHeaderSource | ✅ |
| TERMS_ID | InvoiceHeaderTermsId | ✅ |
| VENDOR_CONTACT_ID | InvoiceHeaderVendorContactId | — |
| VENDOR_ID | InvoiceHeaderVendorId | — |
| VENDOR_SITE_ID | InvoiceHeaderVendorSiteId | ✅ |
| WFAPPROVAL_STATUS | InvoiceHeaderWfapprovalStatus | ✅ |

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP · BICC: 18/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT_PAID | InvoiceHeaderAmountPaid | ✅ |
| BASE_AMOUNT | InvoiceHeaderBaseAmount | ✅ |
| DESCRIPTION | InvoiceHeaderDescription | ✅ |
| EXCHANGE_DATE | InvoiceHeaderExchangeDate | ✅ |
| EXCHANGE_RATE | InvoiceHeaderExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | InvoiceHeaderExchangeRateType | ✅ |
| INVOICE_AMOUNT | InvoiceHeaderInvoiceAmount | ✅ |
| INVOICE_CURRENCY_CODE | InvoiceHeaderInvoiceCurrencyCode | — |
| INVOICE_DATE | InvoiceHeaderInvoiceDate | ✅ |
| INVOICE_ID | InvoiceHeaderInvoiceId | — |
| INVOICE_NUM | InvoiceHeaderInvoiceNum | ✅ |
| INVOICE_TYPE_LOOKUP_CODE | InvoiceHeaderInvoiceTypeLookupCode | ✅ |
| PAYMENT_STATUS_FLAG | InvoiceHeaderPaymentStatusFlag | ✅ |
| ROUTING_ATTRIBUTE1 | InvoiceHeaderRoutingAttribute1 | ✅ |
| ROUTING_ATTRIBUTE2 | InvoiceHeaderRoutingAttribute2 | ✅ |
| ROUTING_ATTRIBUTE3 | InvoiceHeaderRoutingAttribute3 | ✅ |
| ROUTING_ATTRIBUTE4 | InvoiceHeaderRoutingAttribute4 | ✅ |
| SETTLEMENT_PRIORITY | InvoiceHeaderSettlementPriority | ✅ |
| UNIQUE_REMITTANCE_IDENTIFIER | InvoiceHeaderUniqueRemittanceIdentifier | ✅ |
| VOUCHER_NUM | InvoiceHeaderVoucherNum | ✅ |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 35/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTS_PAY_CODE_COMBINATION_ID | InvoiceHeaderAcctsPayCodeCombinationId | ✅ |
| AMOUNT_PAID | InvoiceHeaderAmountPaid | ✅ |
| BASE_AMOUNT | InvoiceHeaderBaseAmount | ✅ |
| CANCELLED_DATE | InvoiceHeaderCancelledDate | ✅ |
| CREATION_DATE | InvoiceHeaderCreationDate | ✅ |
| DESCRIPTION | InvoiceHeaderDescription | ✅ |
| EXCHANGE_DATE | InvoiceHeaderExchangeDate | ✅ |
| EXCHANGE_RATE | InvoiceHeaderExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | InvoiceHeaderExchangeRateType | ✅ |
| INVOICE_AMOUNT | InvoiceHeaderInvoiceAmount | ✅ |
| INVOICE_CURRENCY_CODE | InvoiceHeaderInvoiceCurrencyCode | ✅ |
| INVOICE_DATE | InvoiceHeaderInvoiceDate | ✅ |
| INVOICE_ID | InvoiceHeaderInvoiceId | — |
| INVOICE_ID | InvoiceHeaderSchedInvoiceId | — |
| INVOICE_NUM | InvoiceHeaderInvoiceNum | ✅ |
| INVOICE_RECEIVED_DATE | InvoiceHeaderInvoiceReceivedDate | ✅ |
| INVOICE_TYPE_LOOKUP_CODE | InvoiceHeaderInvoiceTypeLookupCode | ✅ |
| LAST_UPDATE_DATE | InvoiceHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | InvoiceHeaderSchedLastUpdateDate | ✅ |
| LEGAL_ENTITY_ID | InvoiceHeaderLegalEntityId | ✅ |
| ORG_ID | InvoiceHeaderOrgId | ✅ |
| PARTY_ID | InvoiceHeaderPartyId | ✅ |
| PAYMENT_CURRENCY_CODE | InvoiceHeaderPaymentCurrencyCode | ✅ |
| PAYMENT_METHOD_CODE | InvoiceHeaderPaymentMethodCode | ✅ |
| PAYMENT_REASON_COMMENTS | InvoiceHeaderPaymentReasonComments | ✅ |
| PAYMENT_STATUS_FLAG | InvoiceHeaderPaymentStatusFlag | ✅ |
| ROUTING_ATTRIBUTE1 | InvoiceHeaderRoutingAttribute1 | ✅ |
| ROUTING_ATTRIBUTE2 | InvoiceHeaderRoutingAttribute2 | ✅ |
| ROUTING_ATTRIBUTE3 | InvoiceHeaderRoutingAttribute3 | ✅ |
| ROUTING_ATTRIBUTE4 | InvoiceHeaderRoutingAttribute4 | ✅ |
| SET_OF_BOOKS_ID | InvoiceHeaderSetOfBooksId | ✅ |
| SETTLEMENT_PRIORITY | InvoiceHeaderSettlementPriority | ✅ |
| SOURCE | InvoiceHeaderSource | ✅ |
| TERMS_ID | InvoiceHeaderTermsId | ✅ |
| UNIQUE_REMITTANCE_IDENTIFIER | InvoiceHeaderUniqueRemittanceIdentifier | ✅ |
| VENDOR_ID | InvoiceHeaderVendorId | — |
| VENDOR_SITE_ID | InvoiceHeaderVendorSiteId | ✅ |
| VOUCHER_NUM | InvoiceHeaderVoucherNum | ✅ |

### [[prepaymentappliationdistributionpvo|PrepaymentAppliationDistributionPVO]] (AP · BICC: 3/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTS_PAY_CODE_COMBINATION_ID | InvoiceHeaderAcctsPayCodeCombinationId | — |
| INVOICE_DATE | InvoiceHeaderInvoiceDate | — |
| INVOICE_DATE | InvoiceHeaderPrtInvInvoiceDate | ✅ |
| INVOICE_ID | InvoiceHeaderInvoiceId | — |
| INVOICE_ID | InvoiceHeaderPrtInvInvoiceId | — |
| INVOICE_NUM | InvoiceHeaderInvoiceNum | ✅ |
| LAST_UPDATE_DATE | InvoiceHeaderLastUpdateDate | ✅ |
| SET_OF_BOOKS_ID | InvoiceHeaderSetOfBooksId | — |

### [[receiptaccountingtxnp1|ReceiptAccountingTxnP1]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTS_PAY_CODE_COMBINATION_ID | ApInvoicesAllAcctsPayCodeCombinationId | — |
| AMOUNT_APPLICABLE_TO_DISCOUNT | ApInvoicesAllAmountApplicableToDiscount | — |
| AMOUNT_PAID | ApInvoicesAllAmountPaid | — |
| AMT_DUE_CCARD_COMPANY | ApInvoicesAllAmtDueCcardCompany | — |
| AMT_DUE_EMPLOYEE | ApInvoicesAllAmtDueEmployee | — |
| APPLICATION_ID | ApInvoicesAllApplicationId | — |
| APPROVAL_DESCRIPTION | ApInvoicesAllApprovalDescription | — |
| APPROVAL_ITERATION | ApInvoicesAllApprovalIteration | — |
| APPROVAL_READY_FLAG | ApInvoicesAllApprovalReadyFlag | — |
| APPROVAL_STATUS | ApInvoicesAllApprovalStatus2 | — |
| APPROVED_AMOUNT | ApInvoicesAllApprovedAmount | — |
| ATTRIBUTE1 | ApInvoicesAllAttribute127 | — |
| ATTRIBUTE10 | ApInvoicesAllAttribute107 | — |
| ATTRIBUTE11 | ApInvoicesAllAttribute1111 | — |
| ATTRIBUTE12 | ApInvoicesAllAttribute128 | — |
| ATTRIBUTE13 | ApInvoicesAllAttribute137 | — |
| ATTRIBUTE14 | ApInvoicesAllAttribute147 | — |
| ATTRIBUTE15 | ApInvoicesAllAttribute157 | — |
| ATTRIBUTE2 | ApInvoicesAllAttribute27 | — |
| ATTRIBUTE3 | ApInvoicesAllAttribute37 | — |
| ATTRIBUTE4 | ApInvoicesAllAttribute47 | — |
| ATTRIBUTE5 | ApInvoicesAllAttribute57 | — |
| ATTRIBUTE6 | ApInvoicesAllAttribute67 | — |
| ATTRIBUTE7 | ApInvoicesAllAttribute77 | — |
| ATTRIBUTE8 | ApInvoicesAllAttribute87 | — |
| ATTRIBUTE9 | ApInvoicesAllAttribute97 | — |
| ATTRIBUTE_CATEGORY | ApInvoicesAllAttributeCategory7 | — |
| ATTRIBUTE_DATE1 | ApInvoicesAllAttributeDate17 | — |
| ATTRIBUTE_DATE2 | ApInvoicesAllAttributeDate27 | — |
| ATTRIBUTE_DATE3 | ApInvoicesAllAttributeDate37 | — |
| ATTRIBUTE_DATE4 | ApInvoicesAllAttributeDate47 | — |
| ATTRIBUTE_DATE5 | ApInvoicesAllAttributeDate57 | — |
| ATTRIBUTE_NUMBER1 | ApInvoicesAllAttributeNumber17 | — |
| ATTRIBUTE_NUMBER2 | ApInvoicesAllAttributeNumber27 | — |
| ATTRIBUTE_NUMBER3 | ApInvoicesAllAttributeNumber37 | — |
| ATTRIBUTE_NUMBER4 | ApInvoicesAllAttributeNumber47 | — |
| ATTRIBUTE_NUMBER5 | ApInvoicesAllAttributeNumber57 | — |
| AWARD_ID | ApInvoicesAllAwardId1 | — |
| AWT_FLAG | ApInvoicesAllAwtFlag | — |
| AWT_GROUP_ID | ApInvoicesAllAwtGroupId | — |
| BANK_CHARGE_BEARER | ApInvoicesAllBankChargeBearer | — |
| BASE_AMOUNT | ApInvoicesAllBaseAmount | — |
| BATCH_ID | ApInvoicesAllBatchId | — |
| BUDGET_DATE | ApInvoicesAllBudgetDate1 | — |
| CANCELLED_AMOUNT | ApInvoicesAllCancelledAmount | — |
| CANCELLED_BY | ApInvoicesAllCancelledBy2 | — |
| CANCELLED_DATE | ApInvoicesAllCancelledDate | — |
| CHECK_VAT_AMOUNT_PAID | ApInvoicesAllCheckVatAmountPaid | — |
| CONTROL_AMOUNT | ApInvoicesAllControlAmount | — |
| CORRECTION_PERIOD | ApInvoicesAllCorrectionPeriod | — |
| CORRECTION_YEAR | ApInvoicesAllCorrectionYear | — |
| CREATED_BY | ApInvoicesAllCreatedBy10 | — |
| CREATION_DATE | ApInvoicesAllCreationDate10 | — |
| CREDITED_INVOICE_ID | ApInvoicesAllCreditedInvoiceId | — |
| CUST_REGISTRATION_CODE | ApInvoicesAllCustRegistrationCode | — |
| CUST_REGISTRATION_NUMBER | ApInvoicesAllCustRegistrationNumber | — |
| DATA_SET_ID | ApInvoicesAllDataSetId | — |
| DELIVERY_CHANNEL_CODE | ApInvoicesAllDeliveryChannelCode | — |
| DESCRIPTION | ApInvoicesAllDescription1 | — |
| DISC_IS_INV_LESS_TAX_FLAG | ApInvoicesAllDiscIsInvLessTaxFlag | — |
| DISCOUNT_AMOUNT_TAKEN | ApInvoicesAllDiscountAmountTaken | — |
| DISTRIBUTION_SET_ID | ApInvoicesAllDistributionSetId | — |
| DOC_CATEGORY_CODE | ApInvoicesAllDocCategoryCode | — |
| DOC_SEQUENCE_ID | ApInvoicesAllDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ApInvoicesAllDocSequenceValue | — |
| DOCUMENT_SUB_TYPE | ApInvoicesAllDocumentSubType | — |
| EARLIEST_SETTLEMENT_DATE | ApInvoicesAllEarliestSettlementDate | — |
| EMPLOYEE_ADDRESS_CODE | ApInvoicesAllEmployeeAddressCode | — |
| EXCHANGE_DATE | ApInvoicesAllExchangeDate1 | — |
| EXCHANGE_RATE | ApInvoicesAllExchangeRate1 | — |
| EXCHANGE_RATE_TYPE | ApInvoicesAllExchangeRateType1 | — |
| EXCLUDE_FREIGHT_FROM_DISCOUNT | ApInvoicesAllExcludeFreightFromDiscount | — |
| EXCLUSIVE_PAYMENT_FLAG | ApInvoicesAllExclusivePaymentFlag | — |
| EXPENDITURE_ITEM_DATE | ApInvoicesAllExpenditureItemDate | — |
| EXPENDITURE_ORGANIZATION_ID | ApInvoicesAllExpenditureOrganizationId | — |
| EXPENDITURE_TYPE | ApInvoicesAllExpenditureType | — |
| EXTERNAL_BANK_ACCOUNT_ID | ApInvoicesAllExternalBankAccountId | — |
| FIRST_PARTY_REGISTRATION_ID | ApInvoicesAllFirstPartyRegistrationId | — |
| FORCE_REVALIDATION_FLAG | ApInvoicesAllForceRevalidationFlag | — |
| FREIGHT_AMOUNT | ApInvoicesAllFreightAmount1 | — |
| FUNDS_STATUS | ApInvoicesAllFundsStatus4 | — |
| GL_DATE | ApInvoicesAllGlDate1 | — |
| GLOBAL_ATTRIBUTE1 | ApInvoicesAllGlobalAttribute114 | — |
| GLOBAL_ATTRIBUTE10 | ApInvoicesAllGlobalAttribute103 | — |
| GLOBAL_ATTRIBUTE11 | ApInvoicesAllGlobalAttribute115 | — |
| GLOBAL_ATTRIBUTE12 | ApInvoicesAllGlobalAttribute123 | — |
| GLOBAL_ATTRIBUTE13 | ApInvoicesAllGlobalAttribute133 | — |
| GLOBAL_ATTRIBUTE14 | ApInvoicesAllGlobalAttribute143 | — |
| GLOBAL_ATTRIBUTE15 | ApInvoicesAllGlobalAttribute153 | — |
| GLOBAL_ATTRIBUTE16 | ApInvoicesAllGlobalAttribute163 | — |
| GLOBAL_ATTRIBUTE17 | ApInvoicesAllGlobalAttribute173 | — |
| GLOBAL_ATTRIBUTE18 | ApInvoicesAllGlobalAttribute183 | — |
| GLOBAL_ATTRIBUTE19 | ApInvoicesAllGlobalAttribute193 | — |
| GLOBAL_ATTRIBUTE2 | ApInvoicesAllGlobalAttribute23 | — |
| GLOBAL_ATTRIBUTE20 | ApInvoicesAllGlobalAttribute203 | — |
| GLOBAL_ATTRIBUTE3 | ApInvoicesAllGlobalAttribute33 | — |
| GLOBAL_ATTRIBUTE4 | ApInvoicesAllGlobalAttribute43 | — |
| GLOBAL_ATTRIBUTE5 | ApInvoicesAllGlobalAttribute53 | — |
| GLOBAL_ATTRIBUTE6 | ApInvoicesAllGlobalAttribute63 | — |
| GLOBAL_ATTRIBUTE7 | ApInvoicesAllGlobalAttribute73 | — |
| GLOBAL_ATTRIBUTE8 | ApInvoicesAllGlobalAttribute83 | — |
| GLOBAL_ATTRIBUTE9 | ApInvoicesAllGlobalAttribute93 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ApInvoicesAllGlobalAttributeCategory3 | — |
| GLOBAL_ATTRIBUTE_DATE1 | ApInvoicesAllGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE2 | ApInvoicesAllGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | ApInvoicesAllGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | ApInvoicesAllGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | ApInvoicesAllGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | ApInvoicesAllGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | ApInvoicesAllGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | ApInvoicesAllGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | ApInvoicesAllGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | ApInvoicesAllGlobalAttributeNumber5 | — |
| GOODS_RECEIVED_DATE | ApInvoicesAllGoodsReceivedDate | — |
| HISTORICAL_FLAG | ApInvoicesAllHistoricalFlag | — |
| IMPORT_DOCUMENT_DATE | ApInvoicesAllImportDocumentDate | — |
| IMPORT_DOCUMENT_NUMBER | ApInvoicesAllImportDocumentNumber | — |
| INTERCOMPANY_FLAG | ApInvoicesAllIntercompanyFlag | — |
| INTERNAL_CONTACT_EMAIL | ApInvoicesAllInternalContactEmail | — |
| INVOICE_AMOUNT | ApInvoicesAllInvoiceAmount1 | — |
| INVOICE_CURRENCY_CODE | ApInvoicesAllInvoiceCurrencyCode1 | — |
| INVOICE_DATE | ApInvoicesAllInvoiceDate1 | — |
| INVOICE_ID | ApInvoicesAllInvoiceId1 | — |
| INVOICE_NUM | ApInvoicesAllInvoiceNum1 | — |
| INVOICE_RECEIVED_DATE | ApInvoicesAllInvoiceReceivedDate | — |
| INVOICE_TYPE_LOOKUP_CODE | ApInvoicesAllInvoiceTypeLookupCode | — |
| LAST_UPDATE_DATE | ApInvoicesAllLastUpdateDate10 | — |
| LAST_UPDATE_LOGIN | ApInvoicesAllLastUpdateLogin10 | — |
| LAST_UPDATED_BY | ApInvoicesAllLastUpdatedBy10 | — |
| LEGAL_ENTITY_ID | ApInvoicesAllLegalEntityId1 | — |
| MERGE_REQUEST_ID | ApInvoicesAllMergeRequestId1 | — |
| MRC_BASE_AMOUNT | ApInvoicesAllMrcBaseAmount | — |
| MRC_EXCHANGE_DATE | ApInvoicesAllMrcExchangeDate | — |
| MRC_EXCHANGE_RATE | ApInvoicesAllMrcExchangeRate | — |
| MRC_EXCHANGE_RATE_TYPE | ApInvoicesAllMrcExchangeRateType | — |
| MRC_POSTING_STATUS | ApInvoicesAllMrcPostingStatus | — |
| NET_OF_RETAINAGE_FLAG | ApInvoicesAllNetOfRetainageFlag | — |
| OBJECT_VERSION_NUMBER | ApInvoicesAllObjectVersionNumber7 | — |
| ORG_ID | ApInvoicesAllOrgId | — |
| PA_DEFAULT_DIST_CCID | ApInvoicesAllPaDefaultDistCcid | — |
| PA_QUANTITY | ApInvoicesAllPaQuantity | — |
| PAID_ON_BEHALF_EMPLOYEE_ID | ApInvoicesAllPaidOnBehalfEmployeeId | — |
| PARTY_ID | ApInvoicesAllPartyId | — |
| PARTY_SITE_ID | ApInvoicesAllPartySiteId | — |
| PAY_CURR_INVOICE_AMOUNT | ApInvoicesAllPayCurrInvoiceAmount | — |
| PAY_GROUP_LOOKUP_CODE | ApInvoicesAllPayGroupLookupCode | — |
| PAY_PROC_TRXN_TYPE_CODE | ApInvoicesAllPayProcTrxnTypeCode | — |
| PAYMENT_AMOUNT_TOTAL | ApInvoicesAllPaymentAmountTotal | — |
| PAYMENT_CROSS_RATE | ApInvoicesAllPaymentCrossRate | — |
| PAYMENT_CROSS_RATE_DATE | ApInvoicesAllPaymentCrossRateDate | — |
| PAYMENT_CROSS_RATE_TYPE | ApInvoicesAllPaymentCrossRateType | — |
| PAYMENT_CURRENCY_CODE | ApInvoicesAllPaymentCurrencyCode | — |
| PAYMENT_FUNCTION | ApInvoicesAllPaymentFunction | — |
| PAYMENT_METHOD_CODE | ApInvoicesAllPaymentMethodCode | — |
| PAYMENT_METHOD_LOOKUP_CODE | ApInvoicesAllPaymentMethodLookupCode | — |
| PAYMENT_REASON_CODE | ApInvoicesAllPaymentReasonCode | — |
| PAYMENT_REASON_COMMENTS | ApInvoicesAllPaymentReasonComments | — |
| PAYMENT_STATUS_FLAG | ApInvoicesAllPaymentStatusFlag | — |
| PO_HEADER_ID | ApInvoicesAllPoHeaderId6 | — |
| PORT_OF_ENTRY_CODE | ApInvoicesAllPortOfEntryCode | — |
| POSTING_STATUS | ApInvoicesAllPostingStatus | — |
| PRE_WITHHOLDING_AMOUNT | ApInvoicesAllPreWithholdingAmount | — |
| PRODUCT_TABLE | ApInvoicesAllProductTable | — |
| PROJECT_ID | ApInvoicesAllProjectId1 | — |
| QUICK_CREDIT | ApInvoicesAllQuickCredit | — |
| QUICK_PO_HEADER_ID | ApInvoicesAllQuickPoHeaderId | — |
| RECURRING_PAYMENT_ID | ApInvoicesAllRecurringPaymentId | — |
| REFERENCE_1 | ApInvoicesAllReference1 | — |
| REFERENCE_2 | ApInvoicesAllReference2 | — |
| REFERENCE_KEY1 | ApInvoicesAllReferenceKey1 | — |
| REFERENCE_KEY2 | ApInvoicesAllReferenceKey2 | — |
| REFERENCE_KEY3 | ApInvoicesAllReferenceKey3 | — |
| REFERENCE_KEY4 | ApInvoicesAllReferenceKey4 | — |
| REFERENCE_KEY5 | ApInvoicesAllReferenceKey5 | — |
| RELEASE_AMOUNT_NET_OF_TAX | ApInvoicesAllReleaseAmountNetOfTax | — |
| REMITTANCE_MESSAGE1 | ApInvoicesAllRemittanceMessage1 | — |
| REMITTANCE_MESSAGE2 | ApInvoicesAllRemittanceMessage2 | — |
| REMITTANCE_MESSAGE3 | ApInvoicesAllRemittanceMessage3 | — |
| REQUEST_ID | ApInvoicesAllRequestId10 | — |
| REQUESTER_ID | ApInvoicesAllRequesterId | — |
| SELF_ASSESSED_TAX_AMOUNT | ApInvoicesAllSelfAssessedTaxAmount | — |
| SET_OF_BOOKS_ID | ApInvoicesAllSetOfBooksId1 | — |
| SETTLEMENT_PRIORITY | ApInvoicesAllSettlementPriority | — |
| SOURCE | ApInvoicesAllSource | — |
| SUPPLIER_TAX_EXCHANGE_RATE | ApInvoicesAllSupplierTaxExchangeRate | — |
| SUPPLIER_TAX_INVOICE_DATE | ApInvoicesAllSupplierTaxInvoiceDate | — |
| SUPPLIER_TAX_INVOICE_NUMBER | ApInvoicesAllSupplierTaxInvoiceNumber | — |
| TASK_ID | ApInvoicesAllTaskId1 | — |
| TAX_INVOICE_INTERNAL_SEQ | ApInvoicesAllTaxInvoiceInternalSeq | — |
| TAX_INVOICE_RECORDING_DATE | ApInvoicesAllTaxInvoiceRecordingDate | — |
| TAX_RELATED_INVOICE_ID | ApInvoicesAllTaxRelatedInvoiceId | — |
| TAXATION_COUNTRY | ApInvoicesAllTaxationCountry | — |
| TEMP_CANCELLED_AMOUNT | ApInvoicesAllTempCancelledAmount | — |
| TERMS_DATE | ApInvoicesAllTermsDate | — |
| TERMS_ID | ApInvoicesAllTermsId2 | — |
| THIRD_PARTY_REGISTRATION_ID | ApInvoicesAllThirdPartyRegistrationId | — |
| TOTAL_TAX_AMOUNT | ApInvoicesAllTotalTaxAmount | — |
| TRANSACTION_DEADLINE | ApInvoicesAllTransactionDeadline | — |
| TRX_BUSINESS_CATEGORY | ApInvoicesAllTrxBusinessCategory3 | — |
| UNIQUE_REMITTANCE_IDENTIFIER | ApInvoicesAllUniqueRemittanceIdentifier | — |
| URI_CHECK_DIGIT | ApInvoicesAllUriCheckDigit | — |
| USER_DEFINED_FISC_CLASS | ApInvoicesAllUserDefinedFiscClass3 | — |
| USSGL_TRANSACTION_CODE | ApInvoicesAllUssglTransactionCode | — |
| USSGL_TRX_CODE_CONTEXT | ApInvoicesAllUssglTrxCodeContext | — |
| VALIDATED_TAX_AMOUNT | ApInvoicesAllValidatedTaxAmount | — |
| VALIDATION_REQUEST_ID | ApInvoicesAllValidationRequestId | — |
| VENDOR_CONTACT_ID | ApInvoicesAllVendorContactId1 | — |
| VENDOR_ID | ApInvoicesAllVendorId4 | — |
| VENDOR_SITE_ID | ApInvoicesAllVendorSiteId4 | — |
| VOUCHER_NUM | ApInvoicesAllVoucherNum | — |
| WFAPPROVAL_STATUS | ApInvoicesAllWfapprovalStatus | — |

### [[receiptaccountingtxnrefpvo|ReceiptAccountingTxnRefPVO]] (AR · BICC: 39/211)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTS_PAY_CODE_COMBINATION_ID | ApInvoicesAllAcctsPayCodeCombinationId | — |
| AMOUNT_APPLICABLE_TO_DISCOUNT | ApInvoicesAllAmountApplicableToDiscount | — |
| AMOUNT_PAID | ApInvoicesAllAmountPaid | — |
| AMT_DUE_CCARD_COMPANY | ApInvoicesAllAmtDueCcardCompany | — |
| AMT_DUE_EMPLOYEE | ApInvoicesAllAmtDueEmployee | — |
| APPLICATION_ID | ApInvoicesAllApplicationId | — |
| APPROVAL_DESCRIPTION | ApInvoicesAllApprovalDescription | — |
| APPROVAL_ITERATION | ApInvoicesAllApprovalIteration | — |
| APPROVAL_READY_FLAG | ApInvoicesAllApprovalReadyFlag | — |
| APPROVAL_STATUS | ApInvoicesAllApprovalStatus2 | — |
| APPROVED_AMOUNT | ApInvoicesAllApprovedAmount | — |
| ATTRIBUTE1 | ApInvoicesAllAttribute127 | — |
| ATTRIBUTE10 | ApInvoicesAllAttribute107 | — |
| ATTRIBUTE11 | ApInvoicesAllAttribute1111 | — |
| ATTRIBUTE12 | ApInvoicesAllAttribute128 | — |
| ATTRIBUTE13 | ApInvoicesAllAttribute137 | — |
| ATTRIBUTE14 | ApInvoicesAllAttribute147 | — |
| ATTRIBUTE15 | ApInvoicesAllAttribute157 | — |
| ATTRIBUTE2 | ApInvoicesAllAttribute27 | — |
| ATTRIBUTE3 | ApInvoicesAllAttribute37 | — |
| ATTRIBUTE4 | ApInvoicesAllAttribute47 | — |
| ATTRIBUTE5 | ApInvoicesAllAttribute57 | — |
| ATTRIBUTE6 | ApInvoicesAllAttribute67 | — |
| ATTRIBUTE7 | ApInvoicesAllAttribute77 | — |
| ATTRIBUTE8 | ApInvoicesAllAttribute87 | — |
| ATTRIBUTE9 | ApInvoicesAllAttribute97 | — |
| ATTRIBUTE_CATEGORY | ApInvoicesAllAttributeCategory7 | — |
| ATTRIBUTE_DATE1 | ApInvoicesAllAttributeDate17 | — |
| ATTRIBUTE_DATE2 | ApInvoicesAllAttributeDate27 | — |
| ATTRIBUTE_DATE3 | ApInvoicesAllAttributeDate37 | — |
| ATTRIBUTE_DATE4 | ApInvoicesAllAttributeDate47 | — |
| ATTRIBUTE_DATE5 | ApInvoicesAllAttributeDate57 | — |
| ATTRIBUTE_NUMBER1 | ApInvoicesAllAttributeNumber17 | — |
| ATTRIBUTE_NUMBER2 | ApInvoicesAllAttributeNumber27 | — |
| ATTRIBUTE_NUMBER3 | ApInvoicesAllAttributeNumber37 | — |
| ATTRIBUTE_NUMBER4 | ApInvoicesAllAttributeNumber47 | — |
| ATTRIBUTE_NUMBER5 | ApInvoicesAllAttributeNumber57 | — |
| AWARD_ID | ApInvoicesAllAwardId1 | — |
| AWT_FLAG | ApInvoicesAllAwtFlag | — |
| AWT_GROUP_ID | ApInvoicesAllAwtGroupId | — |
| BANK_CHARGE_BEARER | ApInvoicesAllBankChargeBearer | — |
| BASE_AMOUNT | ApInvoicesAllBaseAmount | — |
| BATCH_ID | ApInvoicesAllBatchId | — |
| BUDGET_DATE | ApInvoicesAllBudgetDate1 | ✅ |
| CANCELLED_AMOUNT | ApInvoicesAllCancelledAmount | — |
| CANCELLED_BY | ApInvoicesAllCancelledBy2 | — |
| CANCELLED_DATE | ApInvoicesAllCancelledDate | ✅ |
| CHECK_VAT_AMOUNT_PAID | ApInvoicesAllCheckVatAmountPaid | — |
| CONTROL_AMOUNT | ApInvoicesAllControlAmount | — |
| CORRECTION_PERIOD | ApInvoicesAllCorrectionPeriod | ✅ |
| CORRECTION_YEAR | ApInvoicesAllCorrectionYear | ✅ |
| CREATED_BY | ApInvoicesAllCreatedBy10 | ✅ |
| CREATION_DATE | ApInvoicesAllCreationDate10 | ✅ |
| CREDITED_INVOICE_ID | ApInvoicesAllCreditedInvoiceId | — |
| CUST_REGISTRATION_CODE | ApInvoicesAllCustRegistrationCode | — |
| CUST_REGISTRATION_NUMBER | ApInvoicesAllCustRegistrationNumber | — |
| DATA_SET_ID | ApInvoicesAllDataSetId | — |
| DELIVERY_CHANNEL_CODE | ApInvoicesAllDeliveryChannelCode | — |
| DESCRIPTION | ApInvoicesAllDescription1 | ✅ |
| DISC_IS_INV_LESS_TAX_FLAG | ApInvoicesAllDiscIsInvLessTaxFlag | — |
| DISCOUNT_AMOUNT_TAKEN | ApInvoicesAllDiscountAmountTaken | — |
| DISTRIBUTION_SET_ID | ApInvoicesAllDistributionSetId | — |
| DOC_CATEGORY_CODE | ApInvoicesAllDocCategoryCode | ✅ |
| DOC_SEQUENCE_ID | ApInvoicesAllDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ApInvoicesAllDocSequenceValue | ✅ |
| DOCUMENT_SUB_TYPE | ApInvoicesAllDocumentSubType | — |
| EARLIEST_SETTLEMENT_DATE | ApInvoicesAllEarliestSettlementDate | ✅ |
| EMPLOYEE_ADDRESS_CODE | ApInvoicesAllEmployeeAddressCode | — |
| EXCHANGE_DATE | ApInvoicesAllExchangeDate1 | ✅ |
| EXCHANGE_RATE | ApInvoicesAllExchangeRate1 | ✅ |
| EXCHANGE_RATE_TYPE | ApInvoicesAllExchangeRateType1 | ✅ |
| EXCLUDE_FREIGHT_FROM_DISCOUNT | ApInvoicesAllExcludeFreightFromDiscount | ✅ |
| EXCLUSIVE_PAYMENT_FLAG | ApInvoicesAllExclusivePaymentFlag | — |
| EXPENDITURE_ITEM_DATE | ApInvoicesAllExpenditureItemDate | — |
| EXPENDITURE_ORGANIZATION_ID | ApInvoicesAllExpenditureOrganizationId | — |
| EXPENDITURE_TYPE | ApInvoicesAllExpenditureType | — |
| EXTERNAL_BANK_ACCOUNT_ID | ApInvoicesAllExternalBankAccountId | — |
| FIRST_PARTY_REGISTRATION_ID | ApInvoicesAllFirstPartyRegistrationId | — |
| FORCE_REVALIDATION_FLAG | ApInvoicesAllForceRevalidationFlag | — |
| FREIGHT_AMOUNT | ApInvoicesAllFreightAmount1 | — |
| FUNDS_STATUS | ApInvoicesAllFundsStatus4 | ✅ |
| GL_DATE | ApInvoicesAllGlDate1 | ✅ |
| GLOBAL_ATTRIBUTE1 | ApInvoicesAllGlobalAttribute114 | — |
| GLOBAL_ATTRIBUTE10 | ApInvoicesAllGlobalAttribute103 | — |
| GLOBAL_ATTRIBUTE11 | ApInvoicesAllGlobalAttribute115 | — |
| GLOBAL_ATTRIBUTE12 | ApInvoicesAllGlobalAttribute123 | — |
| GLOBAL_ATTRIBUTE13 | ApInvoicesAllGlobalAttribute133 | — |
| GLOBAL_ATTRIBUTE14 | ApInvoicesAllGlobalAttribute143 | — |
| GLOBAL_ATTRIBUTE15 | ApInvoicesAllGlobalAttribute153 | — |
| GLOBAL_ATTRIBUTE16 | ApInvoicesAllGlobalAttribute163 | — |
| GLOBAL_ATTRIBUTE17 | ApInvoicesAllGlobalAttribute173 | — |
| GLOBAL_ATTRIBUTE18 | ApInvoicesAllGlobalAttribute183 | — |
| GLOBAL_ATTRIBUTE19 | ApInvoicesAllGlobalAttribute193 | — |
| GLOBAL_ATTRIBUTE2 | ApInvoicesAllGlobalAttribute23 | — |
| GLOBAL_ATTRIBUTE20 | ApInvoicesAllGlobalAttribute203 | — |
| GLOBAL_ATTRIBUTE3 | ApInvoicesAllGlobalAttribute33 | — |
| GLOBAL_ATTRIBUTE4 | ApInvoicesAllGlobalAttribute43 | — |
| GLOBAL_ATTRIBUTE5 | ApInvoicesAllGlobalAttribute53 | — |
| GLOBAL_ATTRIBUTE6 | ApInvoicesAllGlobalAttribute63 | — |
| GLOBAL_ATTRIBUTE7 | ApInvoicesAllGlobalAttribute73 | — |
| GLOBAL_ATTRIBUTE8 | ApInvoicesAllGlobalAttribute83 | — |
| GLOBAL_ATTRIBUTE9 | ApInvoicesAllGlobalAttribute93 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ApInvoicesAllGlobalAttributeCategory3 | — |
| GLOBAL_ATTRIBUTE_DATE1 | ApInvoicesAllGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE2 | ApInvoicesAllGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | ApInvoicesAllGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | ApInvoicesAllGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | ApInvoicesAllGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | ApInvoicesAllGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | ApInvoicesAllGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | ApInvoicesAllGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | ApInvoicesAllGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | ApInvoicesAllGlobalAttributeNumber5 | — |
| GOODS_RECEIVED_DATE | ApInvoicesAllGoodsReceivedDate | ✅ |
| HISTORICAL_FLAG | ApInvoicesAllHistoricalFlag | — |
| IMPORT_DOCUMENT_DATE | ApInvoicesAllImportDocumentDate | — |
| IMPORT_DOCUMENT_NUMBER | ApInvoicesAllImportDocumentNumber | — |
| INTERCOMPANY_FLAG | ApInvoicesAllIntercompanyFlag | ✅ |
| INTERNAL_CONTACT_EMAIL | ApInvoicesAllInternalContactEmail | — |
| INVOICE_AMOUNT | ApInvoicesAllInvoiceAmount1 | — |
| INVOICE_CURRENCY_CODE | ApInvoicesAllInvoiceCurrencyCode1 | — |
| INVOICE_DATE | ApInvoicesAllInvoiceDate1 | ✅ |
| INVOICE_ID | ApInvoicesAllInvoiceId1 | ✅ |
| INVOICE_NUM | ApInvoicesAllInvoiceNum1 | ✅ |
| INVOICE_RECEIVED_DATE | ApInvoicesAllInvoiceReceivedDate | ✅ |
| INVOICE_TYPE_LOOKUP_CODE | ApInvoicesAllInvoiceTypeLookupCode | — |
| LAST_UPDATE_DATE | ApInvoicesAllLastUpdateDate10 | ✅ |
| LAST_UPDATE_LOGIN | ApInvoicesAllLastUpdateLogin10 | — |
| LAST_UPDATED_BY | ApInvoicesAllLastUpdatedBy10 | — |
| LEGAL_ENTITY_ID | ApInvoicesAllLegalEntityId1 | — |
| MERGE_REQUEST_ID | ApInvoicesAllMergeRequestId1 | — |
| MRC_BASE_AMOUNT | ApInvoicesAllMrcBaseAmount | — |
| MRC_EXCHANGE_DATE | ApInvoicesAllMrcExchangeDate | — |
| MRC_EXCHANGE_RATE | ApInvoicesAllMrcExchangeRate | — |
| MRC_EXCHANGE_RATE_TYPE | ApInvoicesAllMrcExchangeRateType | — |
| MRC_POSTING_STATUS | ApInvoicesAllMrcPostingStatus | — |
| NET_OF_RETAINAGE_FLAG | ApInvoicesAllNetOfRetainageFlag | — |
| OBJECT_VERSION_NUMBER | ApInvoicesAllObjectVersionNumber7 | — |
| ORG_ID | ApInvoicesAllOrgId | — |
| PA_DEFAULT_DIST_CCID | ApInvoicesAllPaDefaultDistCcid | — |
| PA_QUANTITY | ApInvoicesAllPaQuantity | — |
| PAID_ON_BEHALF_EMPLOYEE_ID | ApInvoicesAllPaidOnBehalfEmployeeId | — |
| PARTY_ID | ApInvoicesAllPartyId | — |
| PARTY_SITE_ID | ApInvoicesAllPartySiteId | — |
| PAY_CURR_INVOICE_AMOUNT | ApInvoicesAllPayCurrInvoiceAmount | — |
| PAY_GROUP_LOOKUP_CODE | ApInvoicesAllPayGroupLookupCode | ✅ |
| PAY_PROC_TRXN_TYPE_CODE | ApInvoicesAllPayProcTrxnTypeCode | — |
| PAYMENT_AMOUNT_TOTAL | ApInvoicesAllPaymentAmountTotal | — |
| PAYMENT_CROSS_RATE | ApInvoicesAllPaymentCrossRate | — |
| PAYMENT_CROSS_RATE_DATE | ApInvoicesAllPaymentCrossRateDate | — |
| PAYMENT_CROSS_RATE_TYPE | ApInvoicesAllPaymentCrossRateType | — |
| PAYMENT_CURRENCY_CODE | ApInvoicesAllPaymentCurrencyCode | ✅ |
| PAYMENT_FUNCTION | ApInvoicesAllPaymentFunction | — |
| PAYMENT_METHOD_CODE | ApInvoicesAllPaymentMethodCode | — |
| PAYMENT_METHOD_LOOKUP_CODE | ApInvoicesAllPaymentMethodLookupCode | — |
| PAYMENT_REASON_CODE | ApInvoicesAllPaymentReasonCode | — |
| PAYMENT_REASON_COMMENTS | ApInvoicesAllPaymentReasonComments | — |
| PAYMENT_STATUS_FLAG | ApInvoicesAllPaymentStatusFlag | ✅ |
| PO_HEADER_ID | ApInvoicesAllPoHeaderId6 | — |
| PORT_OF_ENTRY_CODE | ApInvoicesAllPortOfEntryCode | ✅ |
| POSTING_STATUS | ApInvoicesAllPostingStatus | — |
| PRE_WITHHOLDING_AMOUNT | ApInvoicesAllPreWithholdingAmount | — |
| PRODUCT_TABLE | ApInvoicesAllProductTable | — |
| PROJECT_ID | ApInvoicesAllProjectId1 | — |
| QUICK_CREDIT | ApInvoicesAllQuickCredit | — |
| QUICK_PO_HEADER_ID | ApInvoicesAllQuickPoHeaderId | — |
| RECURRING_PAYMENT_ID | ApInvoicesAllRecurringPaymentId | — |
| REFERENCE_1 | ApInvoicesAllReference1 | — |
| REFERENCE_2 | ApInvoicesAllReference2 | — |
| REFERENCE_KEY1 | ApInvoicesAllReferenceKey1 | — |
| REFERENCE_KEY2 | ApInvoicesAllReferenceKey2 | — |
| REFERENCE_KEY3 | ApInvoicesAllReferenceKey3 | — |
| REFERENCE_KEY4 | ApInvoicesAllReferenceKey4 | — |
| REFERENCE_KEY5 | ApInvoicesAllReferenceKey5 | — |
| RELEASE_AMOUNT_NET_OF_TAX | ApInvoicesAllReleaseAmountNetOfTax | — |
| REMITTANCE_MESSAGE1 | ApInvoicesAllRemittanceMessage1 | — |
| REMITTANCE_MESSAGE2 | ApInvoicesAllRemittanceMessage2 | — |
| REMITTANCE_MESSAGE3 | ApInvoicesAllRemittanceMessage3 | — |
| REQUEST_ID | ApInvoicesAllRequestId10 | — |
| REQUESTER_ID | ApInvoicesAllRequesterId | — |
| SELF_ASSESSED_TAX_AMOUNT | ApInvoicesAllSelfAssessedTaxAmount | — |
| SET_OF_BOOKS_ID | ApInvoicesAllSetOfBooksId1 | — |
| SETTLEMENT_PRIORITY | ApInvoicesAllSettlementPriority | ✅ |
| SOURCE | ApInvoicesAllSource | — |
| SUPPLIER_TAX_EXCHANGE_RATE | ApInvoicesAllSupplierTaxExchangeRate | ✅ |
| SUPPLIER_TAX_INVOICE_DATE | ApInvoicesAllSupplierTaxInvoiceDate | ✅ |
| SUPPLIER_TAX_INVOICE_NUMBER | ApInvoicesAllSupplierTaxInvoiceNumber | ✅ |
| TASK_ID | ApInvoicesAllTaskId1 | — |
| TAX_INVOICE_INTERNAL_SEQ | ApInvoicesAllTaxInvoiceInternalSeq | ✅ |
| TAX_INVOICE_RECORDING_DATE | ApInvoicesAllTaxInvoiceRecordingDate | ✅ |
| TAX_RELATED_INVOICE_ID | ApInvoicesAllTaxRelatedInvoiceId | — |
| TAXATION_COUNTRY | ApInvoicesAllTaxationCountry | ✅ |
| TEMP_CANCELLED_AMOUNT | ApInvoicesAllTempCancelledAmount | — |
| TERMS_DATE | ApInvoicesAllTermsDate | ✅ |
| TERMS_ID | ApInvoicesAllTermsId2 | — |
| THIRD_PARTY_REGISTRATION_ID | ApInvoicesAllThirdPartyRegistrationId | — |
| TOTAL_TAX_AMOUNT | ApInvoicesAllTotalTaxAmount | — |
| TRANSACTION_DEADLINE | ApInvoicesAllTransactionDeadline | — |
| TRX_BUSINESS_CATEGORY | ApInvoicesAllTrxBusinessCategory3 | — |
| UNIQUE_REMITTANCE_IDENTIFIER | ApInvoicesAllUniqueRemittanceIdentifier | ✅ |
| URI_CHECK_DIGIT | ApInvoicesAllUriCheckDigit | — |
| USER_DEFINED_FISC_CLASS | ApInvoicesAllUserDefinedFiscClass3 | ✅ |
| USSGL_TRANSACTION_CODE | ApInvoicesAllUssglTransactionCode | — |
| USSGL_TRX_CODE_CONTEXT | ApInvoicesAllUssglTrxCodeContext | — |
| VALIDATED_TAX_AMOUNT | ApInvoicesAllValidatedTaxAmount | — |
| VALIDATION_REQUEST_ID | ApInvoicesAllValidationRequestId | — |
| VENDOR_CONTACT_ID | ApInvoicesAllVendorContactId1 | — |
| VENDOR_ID | ApInvoicesAllVendorId4 | — |
| VENDOR_SITE_ID | ApInvoicesAllVendorSiteId4 | — |
| VOUCHER_NUM | ApInvoicesAllVoucherNum | ✅ |
| WFAPPROVAL_STATUS | ApInvoicesAllWfapprovalStatus | ✅ |

### [[transactioneventpvo|TransactionEventPVO]] (OTHER · BICC: 8/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EXCHANGE_RATE | ApInvoicesAllExchangeRate | ✅ |
| INVOICE_AMOUNT | ApInvoicesAllInvoiceAmount | ✅ |
| INVOICE_CURRENCY_CODE | ApInvoicesAllInvoiceCurrencyCode | ✅ |
| INVOICE_DATE | ApInvoicesAllInvoiceDate | ✅ |
| INVOICE_ID | ApInvoicesAllInvoiceId | ✅ |
| OBJECT_VERSION_NUMBER | ApInvoicesAllObjectVersionNumber | ✅ |
| VENDOR_ID | ApInvoicesAllVendorId | ✅ |
| VENDOR_SITE_ID | ApInvoicesAllVendorSiteId | ✅ |

### [[trialbalancepvo|TrialBalancePVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INVOICE_ID | InvHdrInvoiceId | — |
| LEGAL_ENTITY_ID | InvHdrLegalEntityId | — |

---

## 📚 Referências

- [Oracle Docs — AP_INVOICES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/apinvoicesall-25702.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
