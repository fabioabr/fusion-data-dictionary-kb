---
id: DOC-OTHER-PVO-BusinessFunctionExtractPVO
doc_type: system-doc
title: "BusinessFunctionExtractPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - BusinessFunctionExtractPVO
  - businessfunctionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BusinessFunctionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Business Function Extract. Acessa as tabelas: FUN_BUSINESS_FUNCTIONS_B, FUN_BUSINESS_FUNCTIONS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.FunBiccExtractAM.BusinessFunctionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fun_business_functions_b|FUN_BUSINESS_FUNCTIONS_B]] — 10 atributos (1 PKs, 10 BICC)
- [[fun_business_functions_tl|FUN_BUSINESS_FUNCTIONS_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[fun_business_functions_b|FUN_BUSINESS_FUNCTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessFunctionBusinessFunctionCode | BUSINESS_FUNCTION_CODE | — | ✅ |
| 2 | BusinessFunctionBusinessFunctionId | BUSINESS_FUNCTION_ID | 🔑 | ✅ |
| 3 | BusinessFunctionCreatedBy | CREATED_BY | — | ✅ |
| 4 | BusinessFunctionCreationDate | CREATION_DATE | — | ✅ |
| 5 | BusinessFunctionGenerateFinTxnFlag | GENERATE_FIN_TXN_FLAG | — | ✅ |
| 6 | BusinessFunctionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | BusinessFunctionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | BusinessFunctionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | BusinessFunctionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | BusinessFunctionSetupApi | SETUP_API | — | ✅ |

### [[fun_business_functions_tl|FUN_BUSINESS_FUNCTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessFunctionTLBusinessFunctionId | BUSINESS_FUNCTION_ID | — | ✅ |
| 2 | BusinessFunctionTLBusinessFunctionName | BUSINESS_FUNCTION_NAME | — | ✅ |
| 3 | BusinessFunctionTLCreatedBy | CREATED_BY | — | ✅ |
| 4 | BusinessFunctionTLCreationDate | CREATION_DATE | — | ✅ |
| 5 | BusinessFunctionTLDescription | DESCRIPTION | — | ✅ |
| 6 | BusinessFunctionTLLanguage | LANGUAGE | — | ✅ |
| 7 | BusinessFunctionTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | BusinessFunctionTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | BusinessFunctionTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | BusinessFunctionTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | BusinessFunctionTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
