---
id: DOC-OTHER-PVO-WrkFlowLookup
doc_type: system-doc
title: "WrkFlowLookup — PVO Cross-Module"
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
  - WrkFlowLookup
  - wrkflowlookup
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WrkFlowLookup

## 📌 Visão Geral

View Object para extração BICC de dados de Wrk Flow Lookup. Acessa as tabelas: ACA_WF_STATUS_VL.

**Caminho:** `FscmTopModelAM.QualityCommonAnalyticsAM.WrkFlowLookup`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[aca_wf_status_vl|ACA_WF_STATUS_VL]] — 18 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[aca_wf_status_vl|ACA_WF_STATUS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WrkFlowLookupPEOApplicationId | APPLICATION_ID | — | ✅ |
| 2 | WrkFlowLookupPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | WrkFlowLookupPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | WrkFlowLookupPEODeleteFlag | DELETE_FLAG | — | ✅ |
| 5 | WrkFlowLookupPEODescription | DESCRIPTION | — | ✅ |
| 6 | WrkFlowLookupPEODisableDate | DISABLE_DATE | — | ✅ |
| 7 | WrkFlowLookupPEOInternalName | INTERNAL_NAME | — | ✅ |
| 8 | WrkFlowLookupPEOIsSystem | IS_SYSTEM | — | ✅ |
| 9 | WrkFlowLookupPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | WrkFlowLookupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | WrkFlowLookupPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | WrkFlowLookupPEOObjectTypeId | OBJECT_TYPE_ID | — | ✅ |
| 13 | WrkFlowLookupPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | WrkFlowLookupPEOSeedFlag | SEED_FLAG | — | ✅ |
| 15 | WrkFlowLookupPEOSortSequenceNum | SORT_SEQUENCE_NUM | — | ✅ |
| 16 | WrkFlowLookupPEOStatusCode | STATUS_CODE | 🔑 | ✅ |
| 17 | WrkFlowLookupPEOStatusName | STATUS_NAME | — | ✅ |
| 18 | WrkFlowLookupPEOStatusType | STATUS_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
