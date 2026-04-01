---
id: DOC-AP-004
doc_type: system-doc
title: "AP_CHECKS_ALL — Pagamentos (Cheques/Transferências) de Contas a Pagar"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, checks, pagamentos, payments, transferencias]
aliases: [AP_CHECKS_ALL, ap_checks_all, checks_ap, pagamentos_ap, cheques_ap]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_CHECKS_ALL

## Visão Geral

Tabela principal de pagamentos emitidos pelo módulo de Contas a Pagar. Apesar do nome legado "checks", armazena todos os tipos de pagamento — cheques, transferências bancárias (wire), boletos e pagamentos eletrônicos. Cada registro representa um instrumento de pagamento individual com valor, data, fornecedor e conta bancária associados. Particionada por `ORG_ID`.

## Propósito de Negócio

Registra cada desembolso realizado a fornecedores, sendo a tabela central para conciliação bancária, auditoria de pagamentos e controle de fluxo de caixa. No Banco Patria, é fundamental para rastrear pagamentos a prestadores de serviço, fornecedores de tecnologia e obrigações regulatórias, além de alimentar relatórios de conciliação com extratos bancários.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHECK_ID | NUMBER(15) | NOT NULL | PK | Chave primária. Identificador único do pagamento. | — | 🟢 100% |
| 2 | CHECK_NUMBER | NUMBER(15) | NOT NULL | Negócio | Número do cheque/pagamento. | — | 🟢 100% |
| 3 | CHECK_DATE | DATE | NOT NULL | Negócio | Data de emissão do pagamento. | — | 🟢 100% |
| 4 | AMOUNT | NUMBER | NOT NULL | Negócio | Valor do pagamento. | — | 🟢 100% |
| 5 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Negócio | Código da moeda do pagamento. | [[fnd_currencies]] | 🟢 100% |
| 6 | VENDOR_ID | NUMBER(15) | NOT NULL | FK | Identificador do fornecedor. | [[poz_suppliers]] | 🟢 100% |
| 7 | VENDOR_SITE_ID | NUMBER(15) | NULL | FK | Identificador do site do fornecedor. | [[poz_supplier_sites_all]] | 🟢 95% |
| 8 | BANK_ACCOUNT_ID | NUMBER(15) | NOT NULL | FK | Conta bancária de origem do pagamento. | [[ce_bank_accounts]] | 🟢 95% |
| 9 | PAYMENT_METHOD_CODE | VARCHAR2(30) | NULL | Negócio | Método de pagamento (CHECK, EFT, WIRE, etc.). | — | 🟢 95% |
| 10 | STATUS_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Controle | Status do pagamento (NEGOTIABLE, VOIDED, CLEARED, etc.). | — | 🟢 100% |
| 11 | CLEARED_DATE | DATE | NULL | Negócio | Data de compensação bancária. | — | 🟢 90% |
| 12 | CLEARED_AMOUNT | NUMBER | NULL | Negócio | Valor compensado no banco. | — | 🟢 90% |
| 13 | PAYMENT_TYPE_FLAG | VARCHAR2(1) | NULL | Classificação | Tipo: R (Refund), Q (Quick), A (Regular). | — | 🟡 75% |
| 14 | ORG_ID | NUMBER(15) | NOT NULL | Multiorg | Identificador da organização (business unit). | [[hr_operating_units]] | 🟢 100% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 16 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[poz_suppliers]]** — Fornecedor beneficiário do pagamento (via `VENDOR_ID`).
- **[[poz_supplier_sites_all]]** — Site do fornecedor (via `VENDOR_SITE_ID`).
- **[[ce_bank_accounts]]** — Conta bancária de origem (via `BANK_ACCOUNT_ID`).
- **[[hr_operating_units]]** — Organização/business unit (via `ORG_ID`).
- **[[fnd_currencies]]** — Moeda do pagamento (via `CURRENCY_CODE`).

### Tabelas-filha

- **[[ap_invoice_payments_all]]** — Relação pagamento × fatura (N:N via `CHECK_ID`).

## Uso Típico

```sql
-- Listar pagamentos emitidos nos últimos 30 dias com fornecedor
SELECT c.CHECK_NUMBER,
       c.CHECK_DATE,
       c.AMOUNT,
       c.CURRENCY_CODE,
       c.STATUS_LOOKUP_CODE,
       s.VENDOR_NAME
  FROM AP_CHECKS_ALL c
  JOIN POZ_SUPPLIERS s
    ON s.VENDOR_ID = c.VENDOR_ID
 WHERE c.ORG_ID = :p_org_id
   AND c.CHECK_DATE >= TRUNC(SYSDATE) - 30
 ORDER BY c.CHECK_DATE DESC;
```

## Observações

- O nome "checks" é legado do Oracle E-Business Suite; no Fusion, a tabela armazena todos os tipos de pagamento.
- O campo `STATUS_LOOKUP_CODE` governa o ciclo de vida: NEGOTIABLE → CLEARED → RECONCILED (ou VOIDED).
- Pagamentos voidados (VOIDED) permanecem na tabela para auditoria — não são excluídos fisicamente.
- Sempre filtrar por `ORG_ID` em consultas para performance e segurança multiorg.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle BICC — AP Payments Subject Area Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).

---

## 🔗 PVOs Relacionados

### [[disbursementheaderextractpvo|DisbursementHeaderExtractPVO]] (OTHER · BICC: 101/158)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE_DATE | ApChecksAllActualValueDate | ✅ |
| ADDRESS_LINE1 | ApChecksAllAddressLine1 | ✅ |
| ADDRESS_LINE2 | ApChecksAllAddressLine2 | ✅ |
| ADDRESS_LINE3 | ApChecksAllAddressLine3 | ✅ |
| ADDRESS_LINE4 | ApChecksAllAddressLine4 | ✅ |
| ADDRESS_STYLE | ApChecksAllAddressStyle | ✅ |
| AMOUNT | ApChecksAllAmount | ✅ |
| ANTICIPATED_VALUE_DATE | ApChecksAllAnticipatedValueDate | ✅ |
| ATTRIBUTE1 | ApChecksAllAttribute1 | — |
| ATTRIBUTE10 | ApChecksAllAttribute10 | — |
| ATTRIBUTE11 | ApChecksAllAttribute11 | — |
| ATTRIBUTE12 | ApChecksAllAttribute12 | — |
| ATTRIBUTE13 | ApChecksAllAttribute13 | — |
| ATTRIBUTE14 | ApChecksAllAttribute14 | — |
| ATTRIBUTE15 | ApChecksAllAttribute15 | — |
| ATTRIBUTE2 | ApChecksAllAttribute2 | — |
| ATTRIBUTE3 | ApChecksAllAttribute3 | — |
| ATTRIBUTE4 | ApChecksAllAttribute4 | — |
| ATTRIBUTE5 | ApChecksAllAttribute5 | — |
| ATTRIBUTE6 | ApChecksAllAttribute6 | — |
| ATTRIBUTE7 | ApChecksAllAttribute7 | — |
| ATTRIBUTE8 | ApChecksAllAttribute8 | — |
| ATTRIBUTE9 | ApChecksAllAttribute9 | — |
| ATTRIBUTE_CATEGORY | ApChecksAllAttributeCategory | — |
| ATTRIBUTE_DATE1 | ApChecksAllAttributeDate1 | — |
| ATTRIBUTE_DATE2 | ApChecksAllAttributeDate2 | — |
| ATTRIBUTE_DATE3 | ApChecksAllAttributeDate3 | — |
| ATTRIBUTE_DATE4 | ApChecksAllAttributeDate4 | — |
| ATTRIBUTE_DATE5 | ApChecksAllAttributeDate5 | — |
| ATTRIBUTE_NUMBER1 | ApChecksAllAttributeNumber1 | — |
| ATTRIBUTE_NUMBER2 | ApChecksAllAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | ApChecksAllAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | ApChecksAllAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | ApChecksAllAttributeNumber5 | — |
| BANK_ACCOUNT_NAME | ApChecksAllBankAccountName | ✅ |
| BANK_ACCOUNT_NUM | ApChecksAllBankAccountNum | ✅ |
| BANK_ACCOUNT_TYPE | ApChecksAllBankAccountType | ✅ |
| BANK_CHARGE_BEARER | ApChecksAllBankChargeBearer | ✅ |
| BANK_NUM | ApChecksAllBankNum | ✅ |
| BASE_AMOUNT | ApChecksAllBaseAmount | ✅ |
| CE_BANK_ACCT_USE_ID | ApChecksAllCeBankAcctUseId | ✅ |
| CHECK_DATE | ApChecksAllCheckDate | ✅ |
| CHECK_FORMAT_ID | ApChecksAllCheckFormatId | ✅ |
| CHECK_ID | ApChecksAllCheckId | ✅ |
| CHECK_NUMBER | ApChecksAllCheckNumber | ✅ |
| CHECK_STOCK_ID | ApChecksAllCheckStockId | ✅ |
| CHECK_VOUCHER_NUM | ApChecksAllCheckVoucherNum | ✅ |
| CHECKRUN_ID | ApChecksAllCheckrunId | ✅ |
| CHECKRUN_NAME | ApChecksAllCheckrunName | ✅ |
| CITY | ApChecksAllCity | ✅ |
| CLEARED_AMOUNT | ApChecksAllClearedAmount | ✅ |
| CLEARED_BASE_AMOUNT | ApChecksAllClearedBaseAmount | ✅ |
| CLEARED_CHARGES_AMOUNT | ApChecksAllClearedChargesAmount | ✅ |
| CLEARED_CHARGES_BASE_AMOUNT | ApChecksAllClearedChargesBaseAmount | ✅ |
| CLEARED_DATE | ApChecksAllClearedDate | ✅ |
| CLEARED_ERROR_AMOUNT | ApChecksAllClearedErrorAmount | ✅ |
| CLEARED_ERROR_BASE_AMOUNT | ApChecksAllClearedErrorBaseAmount | ✅ |
| CLEARED_EXCHANGE_DATE | ApChecksAllClearedExchangeDate | ✅ |
| CLEARED_EXCHANGE_RATE | ApChecksAllClearedExchangeRate | ✅ |
| CLEARED_EXCHANGE_RATE_TYPE | ApChecksAllClearedExchangeRateType | ✅ |
| COMPLETED_PMTS_GROUP_ID | ApChecksAllCompletedPmtsGroupId | ✅ |
| COUNTRY | ApChecksAllCountry | ✅ |
| COUNTY | ApChecksAllCounty | ✅ |
| CREATED_BY | ApChecksAllCreatedBy | ✅ |
| CREATION_DATE | ApChecksAllCreationDate | ✅ |
| CURRENCY_CODE | ApChecksAllCurrencyCode | ✅ |
| DESCRIPTION | ApChecksAllDescription | ✅ |
| DOC_CATEGORY_CODE | ApChecksAllDocCategoryCode | ✅ |
| DOC_SEQUENCE_ID | ApChecksAllDocSequenceId | ✅ |
| DOC_SEQUENCE_VALUE | ApChecksAllDocSequenceValue | ✅ |
| EMPLOYEE_ADDRESS_CODE | ApChecksAllEmployeeAddressCode | ✅ |
| EXCHANGE_DATE | ApChecksAllExchangeDate | ✅ |
| EXCHANGE_RATE | ApChecksAllExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | ApChecksAllExchangeRateType | ✅ |
| EXTERNAL_BANK_ACCOUNT_ID | ApChecksAllExternalBankAccountId | ✅ |
| FUTURE_PAY_DUE_DATE | ApChecksAllFuturePayDueDate | ✅ |
| GLOBAL_ATTRIBUTE1 | ApChecksAllGlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | ApChecksAllGlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | ApChecksAllGlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | ApChecksAllGlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | ApChecksAllGlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | ApChecksAllGlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | ApChecksAllGlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | ApChecksAllGlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | ApChecksAllGlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | ApChecksAllGlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | ApChecksAllGlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | ApChecksAllGlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | ApChecksAllGlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | ApChecksAllGlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | ApChecksAllGlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | ApChecksAllGlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | ApChecksAllGlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | ApChecksAllGlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | ApChecksAllGlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | ApChecksAllGlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ApChecksAllGlobalAttributeCategory | — |
| GLOBAL_ATTRIBUTE_DATE1 | ApChecksAllGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE2 | ApChecksAllGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | ApChecksAllGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | ApChecksAllGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | ApChecksAllGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | ApChecksAllGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | ApChecksAllGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | ApChecksAllGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | ApChecksAllGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | ApChecksAllGlobalAttributeNumber5 | — |
| IBAN_NUMBER | ApChecksAllIbanNumber | ✅ |
| LAST_UPDATE_DATE | ApChecksAllLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ApChecksAllLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ApChecksAllLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | ApChecksAllLegalEntityId | ✅ |
| LOGICAL_GROUP_REFERENCE | ApChecksAllLogicalGroupReference | ✅ |
| MATURITY_EXCHANGE_DATE | ApChecksAllMaturityExchangeDate | ✅ |
| MATURITY_EXCHANGE_RATE | ApChecksAllMaturityExchangeRate | ✅ |
| MATURITY_EXCHANGE_RATE_TYPE | ApChecksAllMaturityExchangeRateType | ✅ |
| OBJECT_VERSION_NUMBER | ApChecksAllObjectVersionNumber | ✅ |
| ORG_ID | ApChecksAllOrgId | ✅ |
| PARTY_ID | ApChecksAllPartyId | ✅ |
| PARTY_SITE_ID | ApChecksAllPartySiteId | ✅ |
| PAYMENT_DOCUMENT_ID | ApChecksAllPaymentDocumentId | ✅ |
| PAYMENT_ID | ApChecksAllPaymentId | ✅ |
| PAYMENT_INSTRUCTION_ID | ApChecksAllPaymentInstructionId | ✅ |
| PAYMENT_METHOD_CODE | ApChecksAllPaymentMethodCode | ✅ |
| PAYMENT_METHOD_LOOKUP_CODE | ApChecksAllPaymentMethodLookupCode | ✅ |
| PAYMENT_PROFILE_ID | ApChecksAllPaymentProfileId | ✅ |
| PAYMENT_TYPE_FLAG | ApChecksAllPaymentTypeFlag | ✅ |
| POSITIVE_PAY_STATUS_CODE | ApChecksAllPositivePayStatusCode | ✅ |
| PROVINCE | ApChecksAllProvince | ✅ |
| RECON_FLAG | ApChecksAllReconFlag | ✅ |
| RECONCILIATION_BATCH_ID | ApChecksAllReconciliationBatchId | ✅ |
| RELATIONSHIP_ID | ApChecksAllRelationshipId | ✅ |
| RELEASED_BY | ApChecksAllReleasedBy | ✅ |
| RELEASED_DATE | ApChecksAllReleasedDate | ✅ |
| REMIT_TO_ADDRESS_ID | ApChecksAllRemitToAddressId | ✅ |
| REMIT_TO_ADDRESS_NAME | ApChecksAllRemitToAddressName | ✅ |
| REMIT_TO_SUPPLIER_ID | ApChecksAllRemitToSupplierId | ✅ |
| REMIT_TO_SUPPLIER_NAME | ApChecksAllRemitToSupplierName | ✅ |
| REQUEST_ID | ApChecksAllRequestId | ✅ |
| SETTLEMENT_PRIORITY | ApChecksAllSettlementPriority | ✅ |
| STAMP_DUTY_AMT | ApChecksAllStampDutyAmt | ✅ |
| STAMP_DUTY_BASE_AMT | ApChecksAllStampDutyBaseAmt | ✅ |
| STATE | ApChecksAllState | ✅ |
| STATUS_LOOKUP_CODE | ApChecksAllStatusLookupCode | ✅ |
| STOPPED_BY | ApChecksAllStoppedBy | ✅ |
| STOPPED_DATE | ApChecksAllStoppedDate | ✅ |
| TRANSFER_PRIORITY | ApChecksAllTransferPriority | ✅ |
| TREASURY_PAY_DATE | ApChecksAllTreasuryPayDate | ✅ |
| TREASURY_PAY_NUMBER | ApChecksAllTreasuryPayNumber | ✅ |
| USSGL_TRANSACTION_CODE | ApChecksAllUssglTransactionCode | ✅ |
| USSGL_TRX_CODE_CONTEXT | ApChecksAllUssglTrxCodeContext | ✅ |
| VENDOR_ID | ApChecksAllVendorId | ✅ |
| VENDOR_NAME | ApChecksAllVendorName | ✅ |
| VENDOR_SITE_CODE | ApChecksAllVendorSiteCode | ✅ |
| VENDOR_SITE_ID | ApChecksAllVendorSiteId | ✅ |
| VOID_DATE | ApChecksAllVoidDate | ✅ |
| X_CURR_RATE_TYPE | ApChecksAllXCurrRateType | ✅ |
| ZIP | ApChecksAllZip | ✅ |

### [[disbursementheaderpvo|DisbursementHeaderPVO]] (AP · BICC: 49/114)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE_DATE | ChecksActualValueDate | ✅ |
| ADDRESS_LINE1 | ChecksAddressLine1 | ✅ |
| ADDRESS_LINE2 | ChecksAddressLine2 | ✅ |
| ADDRESS_LINE3 | ChecksAddressLine3 | ✅ |
| ADDRESS_LINE4 | ChecksAddressLine4 | ✅ |
| ADDRESS_STYLE | ChecksAddressStyle | — |
| AMOUNT | ChecksAmount | ✅ |
| ANTICIPATED_VALUE_DATE | ChecksAnticipatedValueDate | — |
| BANK_ACCOUNT_NAME | ChecksBankAccountName | — |
| BANK_ACCOUNT_NUM | ChecksBankAccountNum | — |
| BANK_ACCOUNT_TYPE | ChecksBankAccountType | ✅ |
| BANK_CHARGE_BEARER | ChecksBankChargeBearer | ✅ |
| BANK_NUM | ChecksBankNum | ✅ |
| BASE_AMOUNT | ChecksBaseAmount | ✅ |
| CE_BANK_ACCT_USE_ID | ChecksCeBankAcctUseId | — |
| CHECK_DATE | ChecksCheckDate | ✅ |
| CHECK_FORMAT_ID | ChecksCheckFormatId | — |
| CHECK_ID | CheckId | ✅ |
| CHECK_NUMBER | ChecksCheckNumber | ✅ |
| CHECK_STOCK_ID | ChecksCheckStockId | — |
| CHECK_VOUCHER_NUM | ChecksCheckVoucherNum | ✅ |
| CHECKRUN_ID | ChecksCheckrunId | — |
| CHECKRUN_NAME | ChecksCheckrunName | ✅ |
| CITY | ChecksCity | ✅ |
| CLEARED_AMOUNT | ChecksClearedAmount | ✅ |
| CLEARED_BASE_AMOUNT | ChecksClearedBaseAmount | — |
| CLEARED_CHARGES_AMOUNT | ChecksClearedChargesAmount | — |
| CLEARED_CHARGES_BASE_AMOUNT | ChecksClearedChargesBaseAmount | — |
| CLEARED_DATE | ChecksClearedDate | ✅ |
| CLEARED_ERROR_AMOUNT | ChecksClearedErrorAmount | — |
| CLEARED_ERROR_BASE_AMOUNT | ChecksClearedErrorBaseAmount | — |
| CLEARED_EXCHANGE_DATE | ChecksClearedExchangeDate | — |
| CLEARED_EXCHANGE_RATE | ChecksClearedExchangeRate | — |
| CLEARED_EXCHANGE_RATE_TYPE | ChecksClearedExchangeRateType | — |
| COMPLETED_PMTS_GROUP_ID | ChecksCompletedPmtsGroupId | — |
| COUNTRY | ChecksCountry | ✅ |
| COUNTY | ChecksCounty | ✅ |
| CREATED_BY | ChecksCreatedBy | ✅ |
| CREATION_DATE | ChecksCreationDate | ✅ |
| CURRENCY_CODE | ChecksCurrencyCode | ✅ |
| DESCRIPTION | ChecksDescription | ✅ |
| DOC_CATEGORY_CODE | ChecksDocCategoryCode | — |
| DOC_SEQUENCE_ID | ChecksDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ChecksDocSequenceValue | ✅ |
| EMPLOYEE_ADDRESS_CODE | ChecksEmployeeAddressCode | — |
| EXCHANGE_DATE | ChecksExchangeDate | ✅ |
| EXCHANGE_RATE | ChecksExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | ChecksExchangeRateType | — |
| EXTERNAL_BANK_ACCOUNT_ID | ChecksExternalBankAccountId | — |
| FUTURE_PAY_DUE_DATE | ChecksFuturePayDueDate | ✅ |
| LAST_UPDATE_DATE | ChecksLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ChecksLastUpdateLogin | — |
| LAST_UPDATED_BY | ChecksLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | ChecksLegalEntityId | — |
| LOGICAL_GROUP_REFERENCE | ChecksLogicalGroupReference | — |
| MATURITY_EXCHANGE_DATE | ChecksMaturityExchangeDate | ✅ |
| MATURITY_EXCHANGE_RATE | ChecksMaturityExchangeRate | ✅ |
| MATURITY_EXCHANGE_RATE_TYPE | ChecksMaturityExchangeRateType | ✅ |
| MRC_BASE_AMOUNT | ChecksMrcBaseAmount | — |
| MRC_CLEARED_BASE_AMOUNT | ChecksMrcClearedBaseAmount | — |
| MRC_CLEARED_CHARGES_BASE_AMT | ChecksMrcClearedChargesBaseAmt | — |
| MRC_CLEARED_ERROR_BASE_AMOUNT | ChecksMrcClearedErrorBaseAmount | — |
| MRC_CLEARED_EXCHANGE_DATE | ChecksMrcClearedExchangeDate | — |
| MRC_CLEARED_EXCHANGE_RATE | ChecksMrcClearedExchangeRate | — |
| MRC_CLEARED_EXCHANGE_RATE_TYPE | ChecksMrcClearedExchangeRateType | — |
| MRC_EXCHANGE_DATE | ChecksMrcExchangeDate | — |
| MRC_EXCHANGE_RATE | ChecksMrcExchangeRate | — |
| MRC_EXCHANGE_RATE_TYPE | ChecksMrcExchangeRateType | — |
| MRC_MATURITY_EXG_DATE | ChecksMrcMaturityExgDate | — |
| MRC_MATURITY_EXG_RATE | ChecksMrcMaturityExgRate | — |
| MRC_MATURITY_EXG_RATE_TYPE | ChecksMrcMaturityExgRateType | — |
| MRC_STAMP_DUTY_BASE_AMT | ChecksMrcStampDutyBaseAmt | — |
| OBJECT_VERSION_NUMBER | ChecksObjectVersionNumber | — |
| ORG_ID | ChecksOrgId | — |
| PARTY_ID | ChecksPartyId | — |
| PARTY_SITE_ID | ChecksPartySiteId | — |
| PAYMENT_DOCUMENT_ID | ChecksPaymentDocumentId | — |
| PAYMENT_ID | ChecksPaymentId | — |
| PAYMENT_INSTRUCTION_ID | ChecksPaymentInstructionId | — |
| PAYMENT_METHOD_CODE | ChecksPaymentMethodCode | ✅ |
| PAYMENT_METHOD_LOOKUP_CODE | ChecksPaymentMethodLookupCode | — |
| PAYMENT_PROFILE_ID | ChecksPaymentProfileId | — |
| PAYMENT_TYPE_FLAG | ChecksPaymentTypeFlag | ✅ |
| POSITIVE_PAY_STATUS_CODE | ChecksPositivePayStatusCode | — |
| PROVINCE | ChecksProvince | ✅ |
| RECON_FLAG | ChecksReconFlag | ✅ |
| RECONCILIATION_BATCH_ID | ChecksReconciliationBatchId | — |
| RELATIONSHIP_ID | ChecksRelationshipId | — |
| RELEASED_BY | ChecksReleasedBy | — |
| RELEASED_DATE | ChecksReleasedDate | ✅ |
| REMIT_TO_ADDRESS_ID | ChecksRemitToAddressId | — |
| REMIT_TO_ADDRESS_NAME | ChecksRemitToAddressName | ✅ |
| REMIT_TO_SUPPLIER_ID | ChecksRemitToSupplierId | — |
| REMIT_TO_SUPPLIER_NAME | ChecksRemitToSupplierName | ✅ |
| REQUEST_ID | ChecksRequestId | — |
| SETTLEMENT_PRIORITY | ChecksSettlementPriority | ✅ |
| STAMP_DUTY_AMT | ChecksStampDutyAmt | — |
| STAMP_DUTY_BASE_AMT | ChecksStampDutyBaseAmt | — |
| STATE | ChecksState | ✅ |
| STATUS_LOOKUP_CODE | ChecksStatusLookupCode | ✅ |
| STOPPED_BY | ChecksStoppedBy | — |
| STOPPED_DATE | ChecksStoppedDate | ✅ |
| TRANSFER_PRIORITY | ChecksTransferPriority | — |
| TREASURY_PAY_DATE | ChecksTreasuryPayDate | — |
| TREASURY_PAY_NUMBER | ChecksTreasuryPayNumber | — |
| USSGL_TRANSACTION_CODE | ChecksUssglTransactionCode | — |
| USSGL_TRX_CODE_CONTEXT | ChecksUssglTrxCodeContext | — |
| VENDOR_ID | ChecksVendorId | — |
| VENDOR_NAME | ChecksVendorName | ✅ |
| VENDOR_SITE_CODE | ChecksVendorSiteCode | ✅ |
| VENDOR_SITE_ID | ChecksVendorSiteId | — |
| VOID_DATE | ChecksVoidDate | ✅ |
| X_CURR_RATE_TYPE | ChecksXCurrRateType | ✅ |
| ZIP | ChecksZip | ✅ |

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP · BICC: 44/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE1 | ChecksAddressLine1 | ✅ |
| ADDRESS_LINE2 | ChecksAddressLine2 | ✅ |
| ADDRESS_LINE3 | ChecksAddressLine3 | ✅ |
| ADDRESS_LINE4 | ChecksAddressLine4 | ✅ |
| BANK_ACCOUNT_TYPE | ChecksBankAccountType | ✅ |
| BANK_CHARGE_BEARER | ChecksBankChargeBearer | ✅ |
| BANK_NUM | ChecksBankNum | ✅ |
| CHECK_DATE | ChecksCheckDate | ✅ |
| CHECK_ID | ChecksCheckId | — |
| CHECK_NUMBER | ChecksCheckNumber | ✅ |
| CHECK_VOUCHER_NUM | ChecksCheckVoucherNum | ✅ |
| CHECKRUN_NAME | ChecksCheckrunName | ✅ |
| CITY | ChecksCity | ✅ |
| CLEARED_DATE | ChecksClearedDate | ✅ |
| COUNTRY | ChecksCountry | ✅ |
| COUNTY | ChecksCounty | ✅ |
| CREATED_BY | ChecksCreatedBy | ✅ |
| CREATION_DATE | ChecksCreationDate | ✅ |
| CURRENCY_CODE | ChecksCurrencyCode | ✅ |
| DESCRIPTION | ChecksDescription | ✅ |
| DOC_SEQUENCE_VALUE | ChecksDocSequenceValue | ✅ |
| EXCHANGE_DATE | ChecksExchangeDate | ✅ |
| EXCHANGE_RATE | ChecksExchangeRate | ✅ |
| FUTURE_PAY_DUE_DATE | ChecksFuturePayDueDate | ✅ |
| LAST_UPDATE_DATE | ChecksLastUpdateDate | ✅ |
| LAST_UPDATED_BY | ChecksLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | ChecksLegalEntityId | — |
| MATURITY_EXCHANGE_DATE | ChecksMaturityExchangeDate | ✅ |
| MATURITY_EXCHANGE_RATE | ChecksMaturityExchangeRate | ✅ |
| MATURITY_EXCHANGE_RATE_TYPE | ChecksMaturityExchangeRateType | ✅ |
| ORG_ID | ChecksOrgId | — |
| PAYMENT_METHOD_CODE | ChecksPaymentMethodCode | ✅ |
| PAYMENT_TYPE_FLAG | ChecksPaymentTypeFlag | ✅ |
| PROVINCE | ChecksProvince | ✅ |
| RECON_FLAG | ChecksReconFlag | ✅ |
| RELEASED_DATE | ChecksReleasedDate | ✅ |
| REMIT_TO_ADDRESS_NAME | ChecksRemitToAddressName | ✅ |
| REMIT_TO_SUPPLIER_NAME | ChecksRemitToSupplierName | ✅ |
| SETTLEMENT_PRIORITY | ChecksSettlementPriority | ✅ |
| STATE | ChecksState | ✅ |
| STATUS_LOOKUP_CODE | ChecksStatusLookupCode | ✅ |
| STOPPED_DATE | ChecksStoppedDate | ✅ |
| VENDOR_ID | ChecksVendorId | — |
| VENDOR_NAME | ChecksVendorName | ✅ |
| VENDOR_SITE_CODE | ChecksVendorSiteCode | ✅ |
| VENDOR_SITE_ID | ChecksVendorSiteId | — |
| VOID_DATE | ChecksVoidDate | ✅ |
| X_CURR_RATE_TYPE | ChecksXCurrRateType | ✅ |
| ZIP | ChecksZip | ✅ |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 45/47)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE1 | ChecksAddressLine1 | ✅ |
| ADDRESS_LINE2 | ChecksAddressLine2 | ✅ |
| ADDRESS_LINE3 | ChecksAddressLine3 | ✅ |
| ADDRESS_LINE4 | ChecksAddressLine4 | ✅ |
| BANK_ACCOUNT_TYPE | ChecksBankAccountType | ✅ |
| BANK_CHARGE_BEARER | ChecksBankChargeBearer | ✅ |
| BANK_NUM | ChecksBankNum | ✅ |
| CHECK_DATE | ChecksCheckDate | ✅ |
| CHECK_ID | ChecksCheckId | ✅ |
| CHECK_NUMBER | ChecksCheckNumber | ✅ |
| CHECK_VOUCHER_NUM | ChecksCheckVoucherNum | ✅ |
| CHECKRUN_NAME | ChecksCheckrunName | ✅ |
| CITY | ChecksCity | ✅ |
| CLEARED_DATE | ChecksClearedDate | ✅ |
| COUNTRY | ChecksCountry | ✅ |
| COUNTY | ChecksCounty | ✅ |
| CREATED_BY | ChecksCreatedBy | ✅ |
| CREATION_DATE | ChecksCreationDate | ✅ |
| CURRENCY_CODE | ChecksCurrencyCode | ✅ |
| DESCRIPTION | ChecksDescription | ✅ |
| DOC_SEQUENCE_VALUE | ChecksDocSequenceValue | ✅ |
| EXCHANGE_DATE | ChecksExchangeDate | ✅ |
| EXCHANGE_RATE | ChecksExchangeRate | ✅ |
| FUTURE_PAY_DUE_DATE | ChecksFuturePayDueDate | ✅ |
| LAST_UPDATE_DATE | ChecksLastUpdateDate | ✅ |
| LAST_UPDATED_BY | ChecksLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | ChecksLegalEntityId | — |
| MATURITY_EXCHANGE_DATE | ChecksMaturityExchangeDate | ✅ |
| MATURITY_EXCHANGE_RATE | ChecksMaturityExchangeRate | ✅ |
| MATURITY_EXCHANGE_RATE_TYPE | ChecksMaturityExchangeRateType | ✅ |
| PAYMENT_METHOD_CODE | ChecksPaymentMethodCode | ✅ |
| PAYMENT_METHOD_LOOKUP_CODE | ChecksPaymentMethodLookupCode | — |
| PAYMENT_TYPE_FLAG | ChecksPaymentTypeFlag | ✅ |
| PROVINCE | ChecksProvince | ✅ |
| RECON_FLAG | ChecksReconFlag | ✅ |
| RELEASED_DATE | ChecksReleasedDate | ✅ |
| REMIT_TO_ADDRESS_NAME | ChecksRemitToAddressName | ✅ |
| REMIT_TO_SUPPLIER_NAME | ChecksRemitToSupplierName | ✅ |
| SETTLEMENT_PRIORITY | ChecksSettlementPriority | ✅ |
| STATE | ChecksState | ✅ |
| STATUS_LOOKUP_CODE | ChecksStatusLookupCode | ✅ |
| STOPPED_DATE | ChecksStoppedDate | ✅ |
| VENDOR_NAME | ChecksVendorName | ✅ |
| VENDOR_SITE_CODE | ChecksVendorSiteCode | ✅ |
| VOID_DATE | ChecksVoidDate | ✅ |
| X_CURR_RATE_TYPE | ChecksXCurrRateType | ✅ |
| ZIP | ChecksZip | ✅ |
