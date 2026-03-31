---
id: DOC-OTHER-PVO-CseAssetFailureSetExtractPVO
doc_type: system-doc
title: "CseAssetFailureSetExtractPVO — PVO Cross-Module"
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
  - CseAssetFailureSetExtractPVO
  - cseassetfailuresetextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CseAssetFailureSetExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cse Asset Failure Set Extract. Acessa as tabelas: CSE_FAILURE_SETS_B, CSE_FAILURE_SETS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.CseAssetFailureSetExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 3 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_failure_sets_b|CSE_FAILURE_SETS_B]] — 10 atributos (1 PKs, 10 BICC)
- [[cse_failure_sets_tl|CSE_FAILURE_SETS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cse_failure_sets_b|CSE_FAILURE_SETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | FailureChainsEnforcedFlag | FAILURE_CHAINS_ENFORCED_FLAG | — | ✅ |
| 5 | FailureSetCode | FAILURE_SET_CODE | — | ✅ |
| 6 | FailureSetId | FAILURE_SET_ID | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

### [[cse_failure_sets_tl|CSE_FAILURE_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FailureSetTLAnalyticsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | FailureSetTLAnalyticsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | FailureSetTLAnalyticsPEOFailureSetDesc | FAILURE_SET_DESC | — | ✅ |
| 4 | FailureSetTLAnalyticsPEOFailureSetId | FAILURE_SET_ID | 🔑 | ✅ |
| 5 | FailureSetTLAnalyticsPEOFailureSetName | FAILURE_SET_NAME | — | ✅ |
| 6 | FailureSetTLAnalyticsPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | FailureSetTLAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | FailureSetTLAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | FailureSetTLAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | FailureSetTLAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | FailureSetTLAnalyticsPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
