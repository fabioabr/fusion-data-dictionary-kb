---
id: DOC-OTHER-PVO-CseAssetFailureChainExtractPVO
doc_type: system-doc
title: "CseAssetFailureChainExtractPVO — PVO Cross-Module"
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
  - CseAssetFailureChainExtractPVO
  - cseassetfailurechainextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CseAssetFailureChainExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cse Asset Failure Chain Extract. Acessa as tabelas: CSE_FAILURE_CHAINS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.CseAssetFailureChainExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_failure_chains|CSE_FAILURE_CHAINS]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[cse_failure_chains|CSE_FAILURE_CHAINS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | CauseCodeId | CAUSE_CODE_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | FailureChainId | FAILURE_CHAIN_ID | 🔑 | ✅ |
| 6 | FailureCodeId | FAILURE_CODE_ID | — | ✅ |
| 7 | FailureSetId | FAILURE_SET_ID | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ResolutionCodeId | RESOLUTION_CODE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
