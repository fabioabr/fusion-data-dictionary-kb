---
id: DOC-OTHER-PVO-BusinessFunctionTLExtractPVO
doc_type: system-doc
title: "BusinessFunctionTLExtractPVO — PVO Cross-Module"
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
  - BusinessFunctionTLExtractPVO
  - businessfunctiontlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BusinessFunctionTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Business Function TLExtract. Acessa as tabelas: FUN_BUSINESS_FUNCTIONS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.FunBiccExtractAM.BusinessFunctionTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fun_business_functions_tl|FUN_BUSINESS_FUNCTIONS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[fun_business_functions_tl|FUN_BUSINESS_FUNCTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessFunctionTLBusinessFunctionId | BUSINESS_FUNCTION_ID | 🔑 | ✅ |
| 2 | BusinessFunctionTLBusinessFunctionName | BUSINESS_FUNCTION_NAME | — | ✅ |
| 3 | BusinessFunctionTLCreatedBy | CREATED_BY | — | ✅ |
| 4 | BusinessFunctionTLCreationDate | CREATION_DATE | — | ✅ |
| 5 | BusinessFunctionTLDescription | DESCRIPTION | — | ✅ |
| 6 | BusinessFunctionTLLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | BusinessFunctionTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | BusinessFunctionTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | BusinessFunctionTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | BusinessFunctionTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | BusinessFunctionTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
