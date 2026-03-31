---
id: DOC-HCM-136
doc_type: system-doc
title: "FND_LOOKUP_VALUES_TL — (título a preencher)"
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
  - FND_LOOKUP_VALUES_TL
  - fnd_lookup_values_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_LOOKUP_VALUES_TL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | DESCRIPTION | — | — | — | — | — | — |
| 4 | ENTERPRISE_ID | — | — | — | — | — | — |
| 5 | LANGUAGE | — | — | — | — | — | — |
| 6 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 7 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 8 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 9 | LOOKUP_CODE | — | — | — | — | — | — |
| 10 | LOOKUP_TYPE | — | — | — | — | — | — |
| 11 | MEANING | — | — | — | — | — | — |
| 12 | SET_ID | — | — | — | — | — | — |
| 13 | SOURCE_LANG | — | — | — | — | — | — |
| 14 | VIEW_APPLICATION_ID | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[lookupvaluespvo|LookupValuesPVO]] (HCM · BICC: 2/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | — |
| LOOKUP_CODE | LookupCode1 | — |
| LOOKUP_TYPE | LookupType1 | — |
| MEANING | Meaning | ✅ |
| SET_ID | SetId1 | — |
| SOURCE_LANG | SourceLang | — |
| VIEW_APPLICATION_ID | ViewApplicationId1 | — |

### [[lookupvaluestlextractpvo|LookupValuesTLExtractPVO]] (OTHER · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| MEANING | Meaning | ✅ |
| SET_ID | SetId | ✅ |
| SOURCE_LANG | SourceLang | ✅ |
| VIEW_APPLICATION_ID | ViewApplicationId | ✅ |

### [[lookupvaluestlpvo|LookupValuesTLPVO]] (HCM · BICC: 12/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| MEANING | Meaning | ✅ |
| SET_ID | SetId | ✅ |
| SOURCE_LANG | SourceLang | ✅ |
| VIEW_APPLICATION_ID | ViewApplicationId | ✅ |

### [[selectedproducts|SelectedProducts]] (PO · BICC: 13/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | LookupTLCreatedBy | ✅ |
| CREATION_DATE | LookupTLCreationDate | ✅ |
| DESCRIPTION | LookupTLDescription | — |
| ENTERPRISE_ID | LookupTLEnterpriseId | ✅ |
| LANGUAGE | LookupTLLanguage | ✅ |
| LAST_UPDATE_DATE | LookupTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LookupTLLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LookupTLLastUpdatedBy | ✅ |
| LOOKUP_CODE | LookupTLLookupCode | ✅ |
| LOOKUP_TYPE | LookupTLLookupType | ✅ |
| MEANING | LookupTLMeaning | ✅ |
| SET_ID | LookupTLSetId | ✅ |
| SOURCE_LANG | LookupTLSourceLang | ✅ |
| VIEW_APPLICATION_ID | LookupTLViewApplicationId | ✅ |

### [[selectedproductsstg|SelectedProductsStg]] (PO · BICC: 13/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | LookupTLCreatedBy | ✅ |
| CREATION_DATE | LookupTLCreationDate | ✅ |
| DESCRIPTION | LookupTLDescription | — |
| ENTERPRISE_ID | LookupTLEnterpriseId | ✅ |
| LANGUAGE | LookupTLLanguage | ✅ |
| LAST_UPDATE_DATE | LookupTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LookupTLLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LookupTLLastUpdatedBy | ✅ |
| LOOKUP_CODE | LookupTLLookupCode | ✅ |
| LOOKUP_TYPE | LookupTLLookupType | ✅ |
| MEANING | LookupTLMeaning | ✅ |
| SET_ID | LookupTLSetId | ✅ |
| SOURCE_LANG | LookupTLSourceLang | ✅ |
| VIEW_APPLICATION_ID | LookupTLViewApplicationId | ✅ |
