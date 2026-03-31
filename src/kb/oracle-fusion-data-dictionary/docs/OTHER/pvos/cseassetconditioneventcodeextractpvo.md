---
id: DOC-OTHER-PVO-CseAssetConditionEventCodeExtractPVO
doc_type: system-doc
title: "CseAssetConditionEventCodeExtractPVO — PVO Cross-Module"
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
  - CseAssetConditionEventCodeExtractPVO
  - cseassetconditioneventcodeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CseAssetConditionEventCodeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cse Asset Condition Event Code Extract. Acessa as tabelas: CSE_CONDITION_EVENT_CODES_B, CSE_CONDITION_EVENT_CODES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.CseAssetConditionEventCodeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 2 | 3 | 26 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_condition_event_codes_b|CSE_CONDITION_EVENT_CODES_B]] — 15 atributos (1 PKs, 15 BICC)
- [[cse_condition_event_codes_tl|CSE_CONDITION_EVENT_CODES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cse_condition_event_codes_b|CSE_CONDITION_EVENT_CODES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | CategoryCode | CATEGORY_CODE | — | ✅ |
| 3 | ConditionEventCode | CONDITION_EVENT_CODE | — | ✅ |
| 4 | ConditionEventCodeId | CONDITION_EVENT_CODE_ID | 🔑 | ✅ |
| 5 | ConditionEventTypeCode | CONDITION_EVENT_TYPE_CODE | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 9 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | RequestId | REQUEST_ID | — | ✅ |
| 15 | SourceRefId | SOURCE_REF_ID | — | ✅ |

### [[cse_condition_event_codes_tl|CSE_CONDITION_EVENT_CODES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CondEventCodeTLAnalyticsPEOConditionEventCodeDesc | CONDITION_EVENT_CODE_DESC | — | ✅ |
| 2 | CondEventCodeTLAnalyticsPEOConditionEventCodeId | CONDITION_EVENT_CODE_ID | 🔑 | ✅ |
| 3 | CondEventCodeTLAnalyticsPEOConditionEventCodeName | CONDITION_EVENT_CODE_NAME | — | ✅ |
| 4 | CondEventCodeTLAnalyticsPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | CondEventCodeTLAnalyticsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | CondEventCodeTLAnalyticsPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | CondEventCodeTLAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CondEventCodeTLAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | CondEventCodeTLAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | CondEventCodeTLAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | CondEventCodeTLAnalyticsPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
