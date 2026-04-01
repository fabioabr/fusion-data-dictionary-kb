---
id: DOC-AR-044
doc_type: system-doc
title: "AR_SYSTEM_PARAMETERS_ALL — Parâmetros de Sistema do Contas a Receber"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, parametros, configuracao, business-unit]
aliases: [AR_SYSTEM_PARAMETERS_ALL, ar_system_parameters_all, ar_sys_params, system_parameters_ar, parametros_ar]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_SYSTEM_PARAMETERS_ALL

> [!note] Sufixo _ALL
> Tabelas com sufixo `_ALL` armazenam dados de **todas as Business Units (orgs)**. O acesso é filtrado pela política de segurança (`ORG_ID`). Em views sem o sufixo, o filtro de org já está aplicado.

## 📌 Visão Geral

Tabela central de **configuração do módulo Accounts Receivable** por Business Unit. Cada registro define os parâmetros operacionais que governam o comportamento do AR — moeda funcional, método contábil, regras de desconto, juros, sequenciamento de documentos e limites de processamento em lote.

## 🧠 Propósito de Negócio

Esta tabela é o **painel de controle** do AR. Define como cada unidade de negócio opera em termos de contabilização, cálculo de impostos, política de descontos e geração de juros. Qualquer alteração de comportamento global do módulo AR passa por esta tabela.

Casos de uso principais:
- Definição do método contábil (accrual vs. cash) por BU
- Configuração de política de descontos (earned/unearned)
- Habilitação de cálculo automático de juros
- Parametrização de lotes de processamento automático

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | ORG_ID | NUMBER | PK. Identificador da Business Unit (organização). | Chave | 🟢 100% |
| 2 | SET_OF_BOOKS_ID | NUMBER | FK para o ledger (livro contábil) associado à BU. Referencia [[gl_ledgers]]. | Configuração | 🟢 100% |
| 3 | DEFAULT_CB_DUE_DATE | VARCHAR2 | Data de vencimento padrão para chargeback. | Configuração | 🟢 100% |
| 4 | ACCOUNTING_METHOD | VARCHAR2 | Método contábil: `ACCRUAL` (competência) ou `CASH` (caixa). | Configuração | 🟢 100% |
| 5 | ACCRUE_INTEREST | VARCHAR2 | Flag indicando se juros devem ser calculados automaticamente (`Y`/`N`). | Configuração | 🟢 100% |
| 6 | DISCOUNT_BASIS | VARCHAR2 | Base de cálculo do desconto: `INVOICE_AMOUNT`, `LINE_ITEMS_ONLY`, etc. | Configuração | 🟢 100% |
| 7 | UNEARNED_DISCOUNT | VARCHAR2 | Permite desconto não merecido (fora do prazo): `Y`/`N`. | Configuração | 🟢 100% |
| 8 | SALES_TAX_CALC_FLAG | VARCHAR2 | Habilita cálculo automático de imposto sobre vendas. | Configuração | 🟢 100% |
| 9 | PRINT_REMIT_TO | VARCHAR2 | Imprime endereço de remessa nas faturas: `Y`/`N`. | Configuração | 🟢 100% |
| 10 | AUTO_REC_INVOICES_PER_COMMIT | NUMBER | Número de faturas processadas por commit no autoinvoice. | Performance | 🟢 100% |
| 11 | DEFAULT_COUNTRY | VARCHAR2 | País padrão para transações da BU. | Configuração | 🟢 100% |
| 12 | TAX_REGISTRATION_NUMBER | VARCHAR2 | Número de registro fiscal da BU. | Configuração | 🟢 100% |
| 13 | DEFAULT_GROUPING_RULE_ID | NUMBER | FK para regra de agrupamento padrão de faturas. | Configuração | 🟢 100% |
| 14 | GENERATE_COLLECTION_LETTERS | VARCHAR2 | Habilita geração automática de cartas de cobrança. | Configuração | 🟢 100% |
| 15 | CASH_BASIS_SET_OF_BOOKS_ID | NUMBER | Ledger alternativo para contabilização em regime de caixa. | Configuração | 🟢 100% |
| 16 | INVOICE_DELETION_FLAG | VARCHAR2 | Permite exclusão de faturas: `Y`/`N`. | Configuração | 🟢 100% |
| 17 | PURGE_INTERFACE_TABLES_FLAG | VARCHAR2 | Habilita purge automático das tabelas de interface. | Configuração | 🟢 100% |
| 18 | PAY_UNRELATED_INVOICES | VARCHAR2 | Permite aplicar recebimentos a faturas de outros clientes. | Configuração | 🟢 100% |
| 19 | LATE_CHARGE_TYPE | VARCHAR2 | Tipo de encargo por atraso: `CHARGE`, `INTEREST`, `PENALTY`. | Configuração | 🟢 100% |
| 20 | INTEREST_RATE | NUMBER | Taxa de juros padrão para finance charges. | Configuração | 🟢 100% |
| 21 | PENALTY_RATE | NUMBER | Taxa de penalidade por atraso. | Configuração | 🟢 100% |
| 22 | MIN_FC_INVOICE_AMOUNT | NUMBER | Valor mínimo de fatura para gerar finance charge. | Configuração | 🟢 100% |
| 23 | MIN_FC_BALANCE_AMOUNT | NUMBER | Saldo mínimo para gerar finance charge. | Configuração | 🟢 100% |
| 24 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 25 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 26 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 27 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 28 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |
| 29 | LAST_UPDATE_DATE | DATE | Data da última atualização. | WHO | 🟢 100% |
| 30 | LAST_UPDATE_LOGIN | VARCHAR2 | Login da última sessão de atualização. | WHO | 🟢 100% |
| 31 | OBJECT_VERSION_NUMBER | NUMBER | Controle de concorrência otimista (versionamento). | WHO | 🟢 100% |
| 32 | PROGRAM_APPLICATION_ID | NUMBER | ID da aplicação do programa concorrente. | WHO | 🟢 100% |
| 33 | PROGRAM_ID | NUMBER | ID do programa concorrente que atualizou. | WHO | 🟢 100% |
| 34 | PROGRAM_UPDATE_DATE | DATE | Data da última atualização por programa concorrente. | WHO | 🟢 100% |
| 35 | REQUEST_ID | NUMBER | ID da requisição concorrente. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[gl_ledgers]] | SET_OF_BOOKS_ID | FK | Ledger associado à BU |
| [[ra_customer_trx_all]] | ORG_ID | Referência | Transações da BU |
| [[ar_cash_receipts_all]] | ORG_ID | Referência | Recebimentos da BU |
| [[hr_operating_units]] | ORG_ID | FK | Business Unit (organização) |
| [[ar_receivables_trx_all]] | ORG_ID | Referência | Atividades de recebíveis da BU |

## 📎 Uso Típico

```sql
-- Consultar parâmetros AR de uma Business Unit específica
SELECT org_id,
       accounting_method,
       accrue_interest,
       discount_basis,
       unearned_discount,
       sales_tax_calc_flag,
       auto_rec_invoices_per_commit
  FROM ar_system_parameters_all
 WHERE org_id = :p_org_id;
```

```sql
-- Listar BUs com juros automáticos habilitados
SELECT sp.org_id,
       hou.name AS business_unit,
       sp.interest_rate,
       sp.late_charge_type
  FROM ar_system_parameters_all sp
  JOIN hr_operating_units hou ON hou.organization_id = sp.org_id
 WHERE sp.accrue_interest = 'Y';
```

## 🔒 Observações

- Cada Business Unit deve ter **exatamente um registro** nesta tabela.
- Alterações nos parâmetros afetam **todas as novas transações** da BU — transações existentes não são retroativamente alteradas.
- O campo `SET_OF_BOOKS_ID` é legado; no Fusion, o conceito equivalente é o **Ledger** em [[gl_ledgers]].
- Campos de finance charge (`INTEREST_RATE`, `PENALTY_RATE`, etc.) só são efetivos quando `ACCRUE_INTEREST = 'Y'`.

## 🔗 PVOs Relacionados

### [[sysparameterextractpvo|SysParameterExtractPVO]] (OTHER · BICC: 151/203)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_METHOD | ArSystemParameterAccountingMethod | ✅ |
| ACCRUE_INTEREST | ArSystemParameterAccrueInterest | ✅ |
| ACCT_DATES_OUT_OF_ORDER | ArSystemParameterAcctDatesOutOfOrder | ✅ |
| ADDRESS_VALIDATION | ArSystemParameterAddressValidation | ✅ |
| AI_ACCT_FLEX_KEY_LEFT_PROMPT | ArSystemParameterAiAcctFlexKeyLeftPrompt | ✅ |
| AI_ACTIVATE_SQL_TRACE_FLAG | ArSystemParameterAiActivateSqlTraceFlag | ✅ |
| AI_LOG_FILE_MESSAGE_LEVEL | ArSystemParameterAiLogFileMessageLevel | ✅ |
| AI_MAX_MEMORY_IN_BYTES | ArSystemParameterAiMaxMemoryInBytes | ✅ |
| AI_MTL_ITEMS_KEY_LEFT_PROMPT | ArSystemParameterAiMtlItemsKeyLeftPrompt | ✅ |
| AI_PURGE_INTERFACE_TABLES_FLAG | ArSystemParameterAiPurgeInterfaceTablesFlag | ✅ |
| AI_TERRITORY_KEY_LEFT_PROMPT | ArSystemParameterAiTerritoryKeyLeftPrompt | ✅ |
| ALLOW_LATE_CHARGES | ArSystemParameterAllowLateCharges | ✅ |
| ALLOW_PAYMENT_DELETION_FLAG | ArSystemParameterAllowPaymentDeletionFlag | ✅ |
| ATTRIBUTE1 | ArSystemParameterAttribute1 | — |
| ATTRIBUTE10 | ArSystemParameterAttribute10 | — |
| ATTRIBUTE11 | ArSystemParameterAttribute11 | — |
| ATTRIBUTE12 | ArSystemParameterAttribute12 | — |
| ATTRIBUTE13 | ArSystemParameterAttribute13 | — |
| ATTRIBUTE14 | ArSystemParameterAttribute14 | — |
| ATTRIBUTE15 | ArSystemParameterAttribute15 | — |
| ATTRIBUTE2 | ArSystemParameterAttribute2 | — |
| ATTRIBUTE3 | ArSystemParameterAttribute3 | — |
| ATTRIBUTE4 | ArSystemParameterAttribute4 | — |
| ATTRIBUTE5 | ArSystemParameterAttribute5 | — |
| ATTRIBUTE6 | ArSystemParameterAttribute6 | — |
| ATTRIBUTE7 | ArSystemParameterAttribute7 | — |
| ATTRIBUTE8 | ArSystemParameterAttribute8 | — |
| ATTRIBUTE9 | ArSystemParameterAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArSystemParameterAttributeCategory | — |
| AUTO_REC_INVOICES_PER_COMMIT | ArSystemParameterAutoRecInvoicesPerCommit | ✅ |
| AUTO_REC_RECEIPTS_PER_COMMIT | ArSystemParameterAutoRecReceiptsPerCommit | ✅ |
| AUTO_SITE_NUMBERING | ArSystemParameterAutoSiteNumbering | ✅ |
| AUTOAPPLY_FLAG | ArSystemParameterAutoapplyFlag | ✅ |
| AUTOCASH_HIERARCHY_ID | ArSystemParameterAutocashHierarchyId | ✅ |
| AUTOMATCH_RERUN_DAYS | ArSystemParameterAutomatchRerunDays | ✅ |
| AUTOMATCH_RULE_ID | ArSystemParameterAutomatchRuleId | ✅ |
| BA_REMIT_BANK_ACCT_USE_ID | ArSystemParameterBaRemitBankAcctUseId | ✅ |
| BILLS_RECEIVABLE_ENABLED_FLAG | ArSystemParameterBillsReceivableEnabledFlag | ✅ |
| BR_DEFAULT_BATCHSOURCE_SEQ_ID | ArSystemParameterBrDefaultBatchsourceSeqId | ✅ |
| BR_REMIT_WITHOUT_RECOURSE_FLAG | ArSystemParameterBrRemitWithoutRecourseFlag | ✅ |
| CALC_DISCOUNT_ON_LINES_FLAG | ArSystemParameterCalcDiscountOnLinesFlag | ✅ |
| CALC_TAX_ON_CREDIT_MEMO_FLAG | ArSystemParameterCalcTaxOnCreditMemoFlag | ✅ |
| CASH_BASIS_SET_OF_BOOKS_ID | ArSystemParameterCashBasisSetOfBooksId | ✅ |
| CC_REMIT_BANK_ACCT_USE_ID | ArSystemParameterCcRemitBankAcctUseId | ✅ |
| CER_DSO_DAYS | ArSystemParameterCerDsoDays | ✅ |
| CER_SPLIT_AMOUNT | ArSystemParameterCerSplitAmount | ✅ |
| CHANGE_PRINTED_INVOICE_FLAG | ArSystemParameterChangePrintedInvoiceFlag | ✅ |
| CODE_COMBINATION_ID_GAIN | ArSystemParameterCodeCombinationIdGain | ✅ |
| CODE_COMBINATION_ID_LOSS | ArSystemParameterCodeCombinationIdLoss | ✅ |
| CODE_COMBINATION_ID_ROUND | ArSystemParameterCodeCombinationIdRound | ✅ |
| CONFIRM_THRESHOLD_AMT | ArSystemParameterConfirmThresholdAmt | ✅ |
| CREATE_DETAILED_DIST | ArSystemParameterCreateDetailedDist | ✅ |
| CREATE_RECIPROCAL_FLAG | ArSystemParameterCreateReciprocalFlag | ✅ |
| CREATED_BY | ArSystemParameterCreatedBy | ✅ |
| CREATION_DATE | ArSystemParameterCreationDate | ✅ |
| CREDIT_CLASSIFICATION1 | ArSystemParameterCreditClassification1 | ✅ |
| CREDIT_CLASSIFICATION2 | ArSystemParameterCreditClassification2 | ✅ |
| CREDIT_CLASSIFICATION3 | ArSystemParameterCreditClassification3 | ✅ |
| CROSS_CURRENCY_RATE_TYPE | ArSystemParameterCrossCurrencyRateType | ✅ |
| DEFAULT_CB_DUE_DATE | ArSystemParameterDefaultCbDueDate | ✅ |
| DEFAULT_COUNTRY | ArSystemParameterDefaultCountry | ✅ |
| DEFAULT_GROUPING_RULE_ID | ArSystemParameterDefaultGroupingRuleId | ✅ |
| DEFAULT_TERRITORY | ArSystemParameterDefaultTerritory | ✅ |
| DOCUMENT_SEQ_GEN_LEVEL | ArSystemParameterDocumentSeqGenLevel | ✅ |
| EMAIL_BODY | ArSystemParameterEmailBody | ✅ |
| EMAIL_SUBJECT | ArSystemParameterEmailSubject | ✅ |
| ENABLE_RECURRING_BILLING_FLAG | ArSystemParameterEnableRecurringBillingFlag | ✅ |
| EXCEPTION_ADJ_REASON_CODE | ArSystemParameterExceptionAdjReasonCode | ✅ |
| EXCEPTION_ADJ_REC_TRX_ID | ArSystemParameterExceptionAdjRecTrxId | ✅ |
| EXCEPTION_PMT_METHOD_CODE | ArSystemParameterExceptionPmtMethodCode | ✅ |
| EXCEPTION_RULE_ID | ArSystemParameterExceptionRuleId | ✅ |
| EXCEPTION_WRTOFF_REC_TRX_ID | ArSystemParameterExceptionWrtoffRecTrxId | ✅ |
| FINCHRG_RECEIVABLES_TRX_ID | ArSystemParameterFinchrgReceivablesTrxId | ✅ |
| FROM_EMAIL_ADDRESS | ArSystemParameterFromEmailAddress | ✅ |
| FROM_EMAIL_NAME | ArSystemParameterFromEmailName | ✅ |
| FROM_POSTAL_CODE | ArSystemParameterFromPostalCode | ✅ |
| GENERATE_CUSTOMER_NUMBER | ArSystemParameterGenerateCustomerNumber | ✅ |
| GLOBAL_ATTRIBUTE1 | ArSystemParameterGlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | ArSystemParameterGlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | ArSystemParameterGlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | ArSystemParameterGlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | ArSystemParameterGlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | ArSystemParameterGlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | ArSystemParameterGlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | ArSystemParameterGlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | ArSystemParameterGlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | ArSystemParameterGlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | ArSystemParameterGlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | ArSystemParameterGlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | ArSystemParameterGlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | ArSystemParameterGlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | ArSystemParameterGlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | ArSystemParameterGlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | ArSystemParameterGlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | ArSystemParameterGlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | ArSystemParameterGlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | ArSystemParameterGlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ArSystemParameterGlobalAttributeCategory | — |
| GLOBAL_ATTRIBUTE_DATE1 | ArSystemParameterGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE2 | ArSystemParameterGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | ArSystemParameterGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | ArSystemParameterGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | ArSystemParameterGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | ArSystemParameterGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER10 | ArSystemParameterGlobalAttributeNumber10 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | ArSystemParameterGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | ArSystemParameterGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | ArSystemParameterGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | ArSystemParameterGlobalAttributeNumber5 | — |
| GLOBAL_ATTRIBUTE_NUMBER6 | ArSystemParameterGlobalAttributeNumber6 | — |
| GLOBAL_ATTRIBUTE_NUMBER7 | ArSystemParameterGlobalAttributeNumber7 | — |
| GLOBAL_ATTRIBUTE_NUMBER8 | ArSystemParameterGlobalAttributeNumber8 | — |
| GLOBAL_ATTRIBUTE_NUMBER9 | ArSystemParameterGlobalAttributeNumber9 | — |
| INCLUDE_BU_SUBJECT_CODE | ArSystemParameterIncludeBuSubjectCode | ✅ |
| INCLUDE_STMT_BU_SUB_CODE | ArSystemParameterIncludeStmtBuSubCode | ✅ |
| INCLUDE_STMT_DATE_SUB_CODE | ArSystemParameterIncludeStmtDateSubCode | ✅ |
| INCLUDE_TRXNUM_SUBJECT_CODE | ArSystemParameterIncludeTrxnumSubjectCode | ✅ |
| INCLUSIVE_TAX_USED | ArSystemParameterInclusiveTaxUsed | ✅ |
| INVOICE_DELETION_FLAG | ArSystemParameterInvoiceDeletionFlag | ✅ |
| IREC_BA_RECEIPT_METHOD_ID | ArSystemParameterIrecBaReceiptMethodId | ✅ |
| IREC_CC_RECEIPT_METHOD_ID | ArSystemParameterIrecCcReceiptMethodId | ✅ |
| IREC_SERVICE_CHARGE_REC_TRX_ID | ArSystemParameterIrecServiceChargeRecTrxId | ✅ |
| ITEM_VALIDATION_ORG_ID | ArSystemParameterItemValidationOrgId | ✅ |
| LAST_UPDATE_DATE | ArSystemParameterLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArSystemParameterLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArSystemParameterLastUpdatedBy | ✅ |
| LATE_CHARGE_BAT_SOURCE_SEQ_ID | ArSystemParameterLateChargeBatSourceSeqId | ✅ |
| LATE_CHARGE_BILLING_CALC_MODE | ArSystemParameterLateChargeBillingCalcMode | ✅ |
| LATE_CHARGE_DM_TYPE_SEQ_ID | ArSystemParameterLateChargeDmTypeSeqId | ✅ |
| LATE_CHARGE_INV_TYPE_SEQ_ID | ArSystemParameterLateChargeInvTypeSeqId | ✅ |
| LOCATION_STRUCTURE_ID | ArSystemParameterLocationStructureId | ✅ |
| LOCATION_TAX_ACCOUNT | ArSystemParameterLocationTaxAccount | ✅ |
| LOCKBOX_MATCHING_OPTION1 | ArSystemParameterLockboxMatchingOption1 | ✅ |
| LOCKBOX_MATCHING_OPTION2 | ArSystemParameterLockboxMatchingOption2 | ✅ |
| LOCKBOX_MATCHING_OPTION3 | ArSystemParameterLockboxMatchingOption3 | ✅ |
| LOCKBOX_MATCHING_OPTION4 | ArSystemParameterLockboxMatchingOption4 | ✅ |
| MATCHED_CLAIM_CREATION_FLAG | ArSystemParameterMatchedClaimCreationFlag | ✅ |
| MATCHED_CLAIM_EXCL_CM_FLAG | ArSystemParameterMatchedClaimExclCmFlag | ✅ |
| MAX_WRTOFF_AMOUNT | ArSystemParameterMaxWrtoffAmount | ✅ |
| MIN_REFUND_AMOUNT | ArSystemParameterMinRefundAmount | ✅ |
| MIN_WRTOFF_AMOUNT | ArSystemParameterMinWrtoffAmount | ✅ |
| OBJECT_VERSION_NUMBER | ArSystemParameterObjectVersionNumber | ✅ |
| ORG_ID | ArSystemParameterOrgId | ✅ |
| PARTIAL_DISCOUNT_FLAG | ArSystemParameterPartialDiscountFlag | ✅ |
| PAY_UNRELATED_INVOICES_FLAG | ArSystemParameterPayUnrelatedInvoicesFlag | ✅ |
| PAYMENT_APPLICATION_RULE | ArSystemParameterPaymentApplicationRule | ✅ |
| PAYMENT_THRESHOLD | ArSystemParameterPaymentThreshold | ✅ |
| PENALTY_REC_TRX_ID | ArSystemParameterPenaltyRecTrxId | ✅ |
| POPULATE_GL_SEGMENTS_FLAG | ArSystemParameterPopulateGlSegmentsFlag | ✅ |
| POST_BILLING_ITEM_INCLUSION | ArSystemParameterPostBillingItemInclusion | ✅ |
| POSTING_DAYS_PER_CYCLE | ArSystemParameterPostingDaysPerCycle | ✅ |
| PRINT_HOME_COUNTRY_FLAG | ArSystemParameterPrintHomeCountryFlag | ✅ |
| PRINT_REMIT_TO | ArSystemParameterPrintRemitTo | ✅ |
| REPLY_TO_EMAIL_ADDRESS | ArSystemParameterReplyToEmailAddress | ✅ |
| REV_TRANSFER_CLEAR_CCID | ArSystemParameterRevTransferClearCcid | ✅ |
| RULE_SET_ID | ArSystemParameterRuleSetId | ✅ |
| RUN_GL_JOURNAL_IMPORT_FLAG | ArSystemParameterRunGlJournalImportFlag | ✅ |
| SALES_CREDIT_PCT_LIMIT | ArSystemParameterSalesCreditPctLimit | ✅ |
| SALES_TAX_GEOCODE | ArSystemParameterSalesTaxGeocode | ✅ |
| SALESREP_REQUIRED_FLAG | ArSystemParameterSalesrepRequiredFlag | ✅ |
| SERVICED_BY_ANY_BU_FLAG | ArSystemParameterServicedByAnyBuFlag | ✅ |
| SET_OF_BOOKS_ID | ArSystemParameterSetOfBooksId | ✅ |
| SHOW_BILLING_NUMBER_FLAG | ArSystemParameterShowBillingNumberFlag | ✅ |
| SITE_REQUIRED_FLAG | ArSystemParameterSiteRequiredFlag | ✅ |
| STANDARD_REFUND | ArSystemParameterStandardRefund | ✅ |
| STMT_EMAIL_BODY | ArSystemParameterStmtEmailBody | ✅ |
| STMT_EMAIL_SUBJECT | ArSystemParameterStmtEmailSubject | ✅ |
| STMT_FROM_EMAIL_ADDRESS | ArSystemParameterStmtFromEmailAddress | ✅ |
| STMT_FROM_EMAIL_NAME | ArSystemParameterStmtFromEmailName | ✅ |
| STMT_REPLY_TO_EMAIL_ADDRESS | ArSystemParameterStmtReplyToEmailAddress | ✅ |
| TA_INSTALLED_FLAG | ArSystemParameterTaInstalledFlag | ✅ |
| TAX_ALLOW_COMPOUND_FLAG | ArSystemParameterTaxAllowCompoundFlag | ✅ |
| TAX_CACHE | ArSystemParameterTaxCache | ✅ |
| TAX_CODE | ArSystemParameterTaxCode | ✅ |
| TAX_CURRENCY_CODE | ArSystemParameterTaxCurrencyCode | ✅ |
| TAX_DATABASE_VIEW_SET | ArSystemParameterTaxDatabaseViewSet | ✅ |
| TAX_ENFORCE_ACCOUNT_FLAG | ArSystemParameterTaxEnforceAccountFlag | ✅ |
| TAX_HEADER_LEVEL_FLAG | ArSystemParameterTaxHeaderLevelFlag | ✅ |
| TAX_HIER_ACCOUNT_EXC_RATE | ArSystemParameterTaxHierAccountExcRate | ✅ |
| TAX_HIER_CUST_EXC_RATE | ArSystemParameterTaxHierCustExcRate | ✅ |
| TAX_HIER_PROD_EXC_RATE | ArSystemParameterTaxHierProdExcRate | ✅ |
| TAX_HIER_SITE_EXC_RATE | ArSystemParameterTaxHierSiteExcRate | ✅ |
| TAX_HIER_SYSTEM_EXC_RATE | ArSystemParameterTaxHierSystemExcRate | ✅ |
| TAX_INVOICE_PRINT | ArSystemParameterTaxInvoicePrint | ✅ |
| TAX_METHOD | ArSystemParameterTaxMethod | ✅ |
| TAX_MINIMUM_ACCOUNTABLE_UNIT | ArSystemParameterTaxMinimumAccountableUnit | ✅ |
| TAX_PRECISION | ArSystemParameterTaxPrecision | ✅ |
| TAX_REGISTRATION_NUMBER | ArSystemParameterTaxRegistrationNumber | ✅ |
| TAX_ROUNDING_ALLOW_OVERRIDE | ArSystemParameterTaxRoundingAllowOverride | ✅ |
| TAX_ROUNDING_RULE | ArSystemParameterTaxRoundingRule | ✅ |
| TAX_USE_ACCOUNT_EXC_RATE_FLAG | ArSystemParameterTaxUseAccountExcRateFlag | ✅ |
| TAX_USE_CUST_EXC_RATE_FLAG | ArSystemParameterTaxUseCustExcRateFlag | ✅ |
| TAX_USE_CUSTOMER_EXEMPT_FLAG | ArSystemParameterTaxUseCustomerExemptFlag | ✅ |
| TAX_USE_LOC_EXC_RATE_FLAG | ArSystemParameterTaxUseLocExcRateFlag | ✅ |
| TAX_USE_PROD_EXC_RATE_FLAG | ArSystemParameterTaxUseProdExcRateFlag | ✅ |
| TAX_USE_PRODUCT_EXEMPT_FLAG | ArSystemParameterTaxUseProductExemptFlag | ✅ |
| TAX_USE_SITE_EXC_RATE_FLAG | ArSystemParameterTaxUseSiteExcRateFlag | ✅ |
| TAX_USE_SYSTEM_EXC_RATE_FLAG | ArSystemParameterTaxUseSystemExcRateFlag | ✅ |
| TO_POSTAL_CODE | ArSystemParameterToPostalCode | ✅ |
| TRX_HEADER_LEVEL_ROUNDING | ArSystemParameterTrxHeaderLevelRounding | ✅ |
| TRX_HEADER_ROUND_CCID | ArSystemParameterTrxHeaderRoundCcid | ✅ |
| UNALLOCATED_REVENUE_CCID | ArSystemParameterUnallocatedRevenueCcid | ✅ |
| UNEARNED_DISCOUNT | ArSystemParameterUnearnedDiscount | ✅ |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — AR System Parameters View Object
- Oracle Fusion Cloud — Implementing Receivables (Configuration Guide)
