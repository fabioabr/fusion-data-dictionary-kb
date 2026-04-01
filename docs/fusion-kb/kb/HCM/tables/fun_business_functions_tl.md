---
id: DOC-HCM-149
doc_type: system-doc
title: "FUN_BUSINESS_FUNCTIONS_TL — (título a preencher)"
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
  - FUN_BUSINESS_FUNCTIONS_TL
  - fun_business_functions_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FUN_BUSINESS_FUNCTIONS_TL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BUSINESS_FUNCTION_ID | — | — | — | — | — | — |
| 2 | BUSINESS_FUNCTION_NAME | — | — | — | — | — | — |
| 3 | CREATED_BY | — | — | — | — | — | — |
| 4 | CREATION_DATE | — | — | — | — | — | — |
| 5 | DESCRIPTION | — | — | — | — | — | — |
| 6 | LANGUAGE | — | — | — | — | — | — |
| 7 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 8 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 9 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 10 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 11 | SOURCE_LANG | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[billingandrevenuebuusagepvo|BillingAndRevenueBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[businessfunctionextractpvo|BusinessFunctionExtractPVO]] (OTHER · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTLBusinessFunctionId | ✅ |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTLBusinessFunctionName | ✅ |
| CREATED_BY | BusinessFunctionTLCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionTLCreationDate | ✅ |
| DESCRIPTION | BusinessFunctionTLDescription | ✅ |
| LANGUAGE | BusinessFunctionTLLanguage | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionTLLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionTLLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionTLObjectVersionNumber | ✅ |
| SOURCE_LANG | BusinessFunctionTLSourceLang | ✅ |

### [[businessfunctiontlextractpvo|BusinessFunctionTLExtractPVO]] (OTHER · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTLBusinessFunctionId | ✅ |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTLBusinessFunctionName | ✅ |
| CREATED_BY | BusinessFunctionTLCreatedBy | ✅ |
| CREATION_DATE | BusinessFunctionTLCreationDate | ✅ |
| DESCRIPTION | BusinessFunctionTLDescription | ✅ |
| LANGUAGE | BusinessFunctionTLLanguage | ✅ |
| LAST_UPDATE_DATE | BusinessFunctionTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessFunctionTLLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessFunctionTLLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BusinessFunctionTLObjectVersionNumber | ✅ |
| SOURCE_LANG | BusinessFunctionTLSourceLang | ✅ |

### [[businessunitusagepvo|BusinessUnitUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[collectionbuusagepvo|CollectionBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[customercontractbuusagepvo|CustomerContractBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[customerpaymentsbuusagepvo|CustomerPaymentsBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[expensebuusagepvo|ExpenseBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[incentivecompensationbuusagepvo|IncentiveCompensationBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[materialmanagementbuusagepvo|MaterialManagementBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[payablesinvoicingbuusagepvo|PayablesInvoicingBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[payablespaymentsbuusagepvo|PayablesPaymentsBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[procurementbuusagepvo|ProcurementBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[procurementcontractbuusagepvo|ProcurementContractBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[projectaccountingbuusagepvo|ProjectAccountingBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[receivingbuusagepvo|ReceivingBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[requisitionbuusagepvo|RequisitionBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |

### [[salesbuusagepvo|SalesBUUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_FUNCTION_ID | BusinessFunctionTranslationBusinessFunctionId | — |
| BUSINESS_FUNCTION_NAME | BusinessFunctionTranslationBusinessFunctionName | — |
| DESCRIPTION | BusinessFunctionTranslationDescription | — |
| LANGUAGE | BusinessFunctionTranslationLanguage | — |
| SOURCE_LANG | BusinessFunctionTranslationSourceLang | — |
