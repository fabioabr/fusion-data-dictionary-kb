---
id: DOC-HCM-148
doc_type: system-doc
title: "FUN_BUSINESS_FUNCTIONS_B — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - FUN_BUSINESS_FUNCTIONS_B
  - fun_business_functions_b
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FUN_BUSINESS_FUNCTIONS_B

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BUSINESS_FUNCTION_CODE | — | — | — | — | — | — |
| 2 | BUSINESS_FUNCTION_ID | — | — | — | — | — | — |
| 3 | CREATED_BY | — | — | — | — | — | — |
| 4 | CREATION_DATE | — | — | — | — | — | — |
| 5 | GENERATE_FIN_TXN_FLAG | — | — | — | — | — | — |
| 6 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 7 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 8 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 9 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 10 | SETUP_API | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[billingandrevenuebuusagepvo|BillingAndRevenueBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[businessfunctionextractpvo|BusinessFunctionExtractPVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[businessunitusagepvo|BusinessUnitUsagePVO]] (OTHER · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | — |
| CREATED_BY | BusinessFunctionCreatedBy | — |
| CREATION_DATE | BusinessFunctionCreationDate | — |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | — |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | — |
| SETUP_API | BusinessFunctionSetupApi | — |

### [[collectionbuusagepvo|CollectionBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[customercontractbuusagepvo|CustomerContractBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[customerpaymentsbuusagepvo|CustomerPaymentsBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[expensebuusagepvo|ExpenseBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[incentivecompensationbuusagepvo|IncentiveCompensationBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[materialmanagementbuusagepvo|MaterialManagementBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[payablesinvoicingbuusagepvo|PayablesInvoicingBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[payablespaymentsbuusagepvo|PayablesPaymentsBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[procurementbuusagepvo|ProcurementBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[procurementcontractbuusagepvo|ProcurementContractBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[projectaccountingbuusagepvo|ProjectAccountingBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[receivingbuusagepvo|ReceivingBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[requisitionbuusagepvo|RequisitionBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |

### [[salesbuusagepvo|SalesBUUsagePVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_CODE | BusinessFunctionBusinessFunctionCode | ✅ |
| BUSINESS_FUNCTION_ID | BusinessFunctionBusinessFunctionId | ✅ |
| CREATED_BY | BusinessFunctionCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionCreationDate | ✅ |
| GENERATE_FIN_TXN_FLAG | BusinessFunctionGenerateFinTxnFlag | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionObjectVersionNumber | ✅ |
| SETUP_API | BusinessFunctionSetupApi | ✅ |
