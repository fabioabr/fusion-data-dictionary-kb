---
id: DOC-HCM-832
doc_type: system-doc
title: "PJF_EXP_TYPES_TL — (título a preencher)"
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
  - PJF_EXP_TYPES_TL
  - pjf_exp_types_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PJF_EXP_TYPES_TL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | DESCRIPTION | — | — | — | — | — | — |
| 4 | EXPENDITURE_TYPE_ID | — | — | — | — | — | — |
| 5 | EXPENDITURE_TYPE_NAME | — | — | — | — | — | — |
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

### [[assetinvoicepvo|AssetInvoicePVO]] (OTHER · BICC: 1/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ExpenditureTypeCreatedBy | — |
| CREATION_DATE | ExpenditureTypeCreationDate | — |
| DESCRIPTION | ExpenditureTypeDescription | — |
| EXPENDITURE_TYPE_ID | ExpenditureTypeExpenditureTypeId | — |
| EXPENDITURE_TYPE_NAME | ExpenditureTypeExpenditureTypeName | ✅ |
| LANGUAGE | ExpenditureTypeLanguage | — |
| LAST_UPDATE_DATE | ExpenditureTypeLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ExpenditureTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenditureTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ExpenditureTypeObjectVersionNumber | — |

### [[contractheaderlinesall|ContractHeaderLinesAll]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EXPENDITURE_TYPE_ID | ExpenditureTypeId | — |
| EXPENDITURE_TYPE_NAME | ExpenditureTypeTranslationPEOExpenditureTypeName | — |
| LANGUAGE | ExpenditureTypeTranslationPEOLanguage | — |

### [[contractheaderlinesallunsec|ContractHeaderLinesAllUnsec]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EXPENDITURE_TYPE_ID | ExpenditureTypeId | — |
| EXPENDITURE_TYPE_NAME | ExpenditureTypeTranslationPEOExpenditureTypeName | — |
| LANGUAGE | ExpenditureTypeTranslationPEOLanguage | — |

### [[contractheaderlinesp|ContractHeaderLinesP]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EXPENDITURE_TYPE_ID | ExpenditureTypeId | — |
| EXPENDITURE_TYPE_NAME | ExpenditureTypeTranslationPEOExpenditureTypeName | ✅ |
| LANGUAGE | ExpenditureTypeTranslationPEOLanguage | — |

### [[contractheaderlinesrefp|ContractHeaderLinesRefP]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EXPENDITURE_TYPE_ID | ExpenditureTypeId | — |
| EXPENDITURE_TYPE_NAME | ExpenditureTypeTranslationPEOExpenditureTypeName | ✅ |
| LANGUAGE | ExpenditureTypeTranslationPEOLanguage | — |

### [[expendituretype|ExpenditureType]] (OTHER · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ExpenditureTypeTransCreatedBy | — |
| CREATION_DATE | ExpenditureTypeTransCreationDate | — |
| DESCRIPTION | ExpenditureTypeTransDescription | ✅ |
| EXPENDITURE_TYPE_ID | ExpenditureTypeTransExpenditureTypeId | — |
| EXPENDITURE_TYPE_NAME | ExpenditureTypeTransExpenditureTypeName | ✅ |
| LANGUAGE | ExpenditureTypeTransLanguage | — |
| LAST_UPDATE_DATE | ExpenditureTypeTransLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpenditureTypeTransLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenditureTypeTransLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ExpenditureTypeTransObjectVersionNumber | — |
| SOURCE_LANG | ExpenditureTypeTransSourceLang | — |

### [[expendituretypeextractpvo|ExpenditureTypeExtractPVO]] (OTHER · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ExpenditureTypeTranslangPEOCreatedBy | ✅ |
| CREATION_DATE | ExpenditureTypeTranslangPEOCreationDate | ✅ |
| DESCRIPTION | ExpenditureTypeTranslangPEODescription | ✅ |
| EXPENDITURE_TYPE_ID | ExpenditureTypeTranslangPEOExpenditureTypeId | ✅ |
| EXPENDITURE_TYPE_NAME | ExpenditureTypeTranslangPEOExpenditureTypeName | ✅ |
| LANGUAGE | ExpenditureTypeTranslangPEOLanguage | ✅ |
| LAST_UPDATE_DATE | ExpenditureTypeTranslangPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpenditureTypeTranslangPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ExpenditureTypeTranslangPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ExpenditureTypeTranslangPEOObjectVersionNumber | ✅ |
| SOURCE_LANG | ExpenditureTypeTranslangPEOSourceLang | ✅ |

### [[expendituretypetranslation|ExpenditureTypeTranslation]] (OTHER · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| EXPENDITURE_TYPE_ID | ExpenditureTypeId | ✅ |
| EXPENDITURE_TYPE_NAME | ExpenditureTypeName | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[expendituretypetranslationextractpvo|ExpenditureTypeTranslationExtractPVO]] (OTHER · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ExpenditureTypeTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | ExpenditureTypeTranslationPEOCreationDate | ✅ |
| DESCRIPTION | ExpenditureTypeTranslationPEODescription | ✅ |
| EXPENDITURE_TYPE_ID | ExpenditureTypeTranslationPEOExpenditureTypeId | ✅ |
| EXPENDITURE_TYPE_NAME | ExpenditureTypeTranslationPEOExpenditureTypeName | ✅ |
| LANGUAGE | ExpenditureTypeTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | ExpenditureTypeTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpenditureTypeTranslationPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ExpenditureTypeTranslationPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ExpenditureTypeTranslationPEOObjectVersionNumber | ✅ |
| SOURCE_LANG | ExpenditureTypeTranslationPEOSourceLang | ✅ |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ExpenditureTypeCreatedBy1 | — |
| CREATION_DATE | ExpenditureTypeCreationDate1 | — |
| DESCRIPTION | ExpenditureTypeDescription | ✅ |
| EXPENDITURE_TYPE_ID | ExpenditureTypeExpenditureTypeId | — |
| EXPENDITURE_TYPE_NAME | ExpenditureTypeExpenditureTypeName | ✅ |
| LANGUAGE | ExpenditureTypeLanguage | — |
| LAST_UPDATE_DATE | ExpenditureTypeLastUpdateDate1 | — |
| LAST_UPDATE_LOGIN | ExpenditureTypeLastUpdateLogin1 | — |
| LAST_UPDATED_BY | ExpenditureTypeLastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ExpenditureTypeObjectVersionNumber1 | — |

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EXPENDITURE_TYPE_ID | ExpTypeExpenditureTypeId | — |
| EXPENDITURE_TYPE_NAME | ExpTypeExpenditureTypeName | ✅ |
| LANGUAGE | ExpTypeLanguage | — |

### [[nonlaborresource|NonLaborResource]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ExpenditureTypeTranslationPE1CreatedBy | — |
| CREATION_DATE | ExpenditureTypeTranslationPE1CreationDate | — |
| DESCRIPTION | ExpenditureTypeTranslationPE1Description | — |
| EXPENDITURE_TYPE_ID | ExpenditureTypeTranslationPE1ExpenditureTypeId | — |
| EXPENDITURE_TYPE_NAME | ExpenditureTypeTranslationPE1ExpenditureTypeName | — |
| LANGUAGE | ExpenditureTypeTranslationPE1Language | — |
| LAST_UPDATE_DATE | ExpenditureTypeTranslationPE1LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpenditureTypeTranslationPE1LastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenditureTypeTranslationPE1LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ExpenditureTypeTranslationPE1ObjectVersionNumber | — |
| SOURCE_LANG | ExpenditureTypeTranslationPE1SourceLang | — |
