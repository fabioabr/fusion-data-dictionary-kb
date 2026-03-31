---
id: DOC-HCM-834
doc_type: system-doc
title: "PJF_PROJECTS_ALL_TL — (título a preencher)"
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
  - PJF_PROJECTS_ALL_TL
  - pjf_projects_all_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PJF_PROJECTS_ALL_TL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | DESCRIPTION | — | — | — | — | — | — |
| 4 | EXECUTION_CUSTOMER_NAME | — | — | — | — | — | — |
| 5 | LANGUAGE | — | — | — | — | — | — |
| 6 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 7 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 8 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 9 | NAME | — | — | — | — | — | — |
| 10 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 11 | PROJECT_ID | — | — | — | — | — | — |
| 12 | SOURCE_LANG | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[contractheaderlinesall|ContractHeaderLinesAll]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | ProjectTranslationPEOLanguage | — |
| NAME | ProjectTranslationPEOName | — |
| PROJECT_ID | ProjectTranslationPEOProjectId | — |

### [[contractheaderlinesallunsec|ContractHeaderLinesAllUnsec]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | ProjectTranslationPEOLanguage | — |
| NAME | ProjectTranslationPEOName | — |
| PROJECT_ID | ProjectTranslationPEOProjectId | — |

### [[contractheaderlinesp|ContractHeaderLinesP]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | ProjectTranslationPEOLanguage | — |
| NAME | ProjectTranslationPEOName | ✅ |
| PROJECT_ID | ProjectTranslationPEOProjectId | — |

### [[contractheaderlinesrefp|ContractHeaderLinesRefP]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | ProjectTranslationPEOLanguage | — |
| NAME | ProjectTranslationPEOName | ✅ |
| PROJECT_ID | ProjectTranslationPEOProjectId | — |

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | ProjectTLLAnguage | — |
| NAME | ProjectName | ✅ |
| PROJECT_ID | ProjectTLProjectId | — |

### [[project|Project]] (OTHER · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ProjectTranslationPEOCreatedBy | — |
| CREATION_DATE | ProjectTranslationPEOCreationDate | — |
| DESCRIPTION | ProjectTranslationPEODescription | ✅ |
| EXECUTION_CUSTOMER_NAME | ProjectTranslationPEOExecutionCustomerName | ✅ |
| LANGUAGE | ProjectTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ProjectTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProjectTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProjectTranslationPEOLastUpdatedBy | — |
| NAME | ProjectTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | ProjectTranslationPEOObjectVersionNumber | — |
| PROJECT_ID | ProjectTranslationPEOProjectId | — |
| SOURCE_LANG | ProjectTranslationPEOSourceLang | — |

### [[projectexec|ProjectExec]] (OTHER · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ProjectTranslationPEOCreatedBy | — |
| CREATION_DATE | ProjectTranslationPEOCreationDate | — |
| DESCRIPTION | ProjectTranslationPEODescription | ✅ |
| EXECUTION_CUSTOMER_NAME | ProjectTranslationPEOExecutionCustomerName | ✅ |
| LANGUAGE | ProjectTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ProjectTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProjectTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProjectTranslationPEOLastUpdatedBy | — |
| NAME | ProjectTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | ProjectTranslationPEOObjectVersionNumber | — |
| PROJECT_ID | ProjectTranslationPEOProjectId | — |
| SOURCE_LANG | ProjectTranslationPEOSourceLang | — |

### [[projectplanlinebudgetpvo|ProjectPlanLineBudgetPVO]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ProjectTranslationPEOCreatedBy | — |
| CREATION_DATE | ProjectTranslationPEOCreationDate | — |
| DESCRIPTION | ProjectTranslationPEODescription | — |
| LANGUAGE | ProjectTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ProjectTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProjectTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProjectTranslationPEOLastUpdatedBy | — |
| NAME | ProjectTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | ProjectTranslationPEOObjectVersionNumber | — |
| PROJECT_ID | ProjectTranslationPEOProjectId | — |
| SOURCE_LANG | ProjectTranslationPEOSourceLang | — |

### [[projectplanlinedetailbudgetpvo|ProjectPlanLineDetailBudgetPVO]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ProjectTranslationPEOCreatedBy | — |
| CREATION_DATE | ProjectTranslationPEOCreationDate | — |
| DESCRIPTION | ProjectTranslationPEODescription | — |
| LANGUAGE | ProjectTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ProjectTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProjectTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProjectTranslationPEOLastUpdatedBy | — |
| NAME | ProjectTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | ProjectTranslationPEOObjectVersionNumber | — |
| PROJECT_ID | ProjectTranslationPEOProjectId | — |
| SOURCE_LANG | ProjectTranslationPEOSourceLang | — |

### [[projectplanlineforecastpvo|ProjectPlanLineForecastPVO]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ProjectTranslationPEOCreatedBy | — |
| CREATION_DATE | ProjectTranslationPEOCreationDate | — |
| DESCRIPTION | ProjectTranslationPEODescription | — |
| LANGUAGE | ProjectTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ProjectTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProjectTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProjectTranslationPEOLastUpdatedBy | — |
| NAME | ProjectTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | ProjectTranslationPEOObjectVersionNumber | — |
| PROJECT_ID | ProjectTranslationPEOProjectId | — |
| SOURCE_LANG | ProjectTranslationPEOSourceLang | — |

### [[projectplanversionbudgetpvo|ProjectPlanVersionBudgetPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | ProjectTranslationPEOLanguage | — |
| NAME | ProjectTranslationPEOName | ✅ |
| PROJECT_ID | ProjectTranslationPEOProjectId | — |

### [[projectplanversionforecastpvo|ProjectPlanVersionForecastPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | ProjectTranslationPEOLanguage | — |
| NAME | ProjectTranslationPEOName | ✅ |
| PROJECT_ID | ProjectTranslationPEOProjectId | — |

### [[projectrefpvo|ProjectRefPVO]] (OTHER · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ProjectTranslationPEOCreatedBy | — |
| CREATION_DATE | ProjectTranslationPEOCreationDate | — |
| DESCRIPTION | ProjectTranslationPEODescription | ✅ |
| EXECUTION_CUSTOMER_NAME | ProjectTranslationPEOExecutionCustomerName | ✅ |
| LANGUAGE | ProjectTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ProjectTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProjectTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProjectTranslationPEOLastUpdatedBy | — |
| NAME | ProjectTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | ProjectTranslationPEOObjectVersionNumber | — |
| PROJECT_ID | ProjectTranslationPEOProjectId | — |
| SOURCE_LANG | ProjectTranslationPEOSourceLang | — |

### [[projecttranslation|ProjectTranslation]] (OTHER · BICC: 9/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| EXECUTION_CUSTOMER_NAME | ExecutionCustomerName | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PROJECT_ID | ProjectId | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[projecttranslationextractpvo|ProjectTranslationExtractPVO]] (OTHER · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ProjectTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | ProjectTranslationPEOCreationDate | ✅ |
| DESCRIPTION | ProjectTranslationPEODescription | ✅ |
| EXECUTION_CUSTOMER_NAME | ProjectTranslationPEOExecutionCustomerName | ✅ |
| LANGUAGE | ProjectTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | ProjectTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProjectTranslationPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ProjectTranslationPEOLastUpdatedBy | ✅ |
| NAME | ProjectTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | ProjectTranslationPEOObjectVersionNumber | ✅ |
| PROJECT_ID | ProjectTranslationPEOProjectId | ✅ |
| SOURCE_LANG | ProjectTranslationPEOSourceLang | ✅ |

### [[projplanlinedetailforecastpvo|ProjPlanLineDetailForecastPVO]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ProjectTranslationPEOCreatedBy | — |
| CREATION_DATE | ProjectTranslationPEOCreationDate | — |
| DESCRIPTION | ProjectTranslationPEODescription | — |
| LANGUAGE | ProjectTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ProjectTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProjectTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProjectTranslationPEOLastUpdatedBy | — |
| NAME | ProjectTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | ProjectTranslationPEOObjectVersionNumber | — |
| PROJECT_ID | ProjectTranslationPEOProjectId | — |
| SOURCE_LANG | ProjectTranslationPEOSourceLang | — |
