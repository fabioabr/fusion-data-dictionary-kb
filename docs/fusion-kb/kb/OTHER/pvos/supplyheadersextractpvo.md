---
id: DOC-OTHER-PVO-SupplyHeadersExtractPVO
doc_type: system-doc
title: "SupplyHeadersExtractPVO — PVO Cross-Module"
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
  - SupplyHeadersExtractPVO
  - supplyheadersextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplyHeadersExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supply Headers Extract. Acessa as tabelas: DOS_SUPPLY_HEADERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DosBiccExtractAM.SupplyHeadersExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 1 | 1 | 59 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[dos_supply_headers|DOS_SUPPLY_HEADERS]] — 59 atributos (1 PKs, 59 BICC)

---

## ⚙️ Atributos

### [[dos_supply_headers|DOS_SUPPLY_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosSupplyHeadersPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | DosSupplyHeadersPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | DosSupplyHeadersPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | DosSupplyHeadersPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | DosSupplyHeadersPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | DosSupplyHeadersPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | DosSupplyHeadersPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | DosSupplyHeadersPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | DosSupplyHeadersPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 10 | DosSupplyHeadersPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 11 | DosSupplyHeadersPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 12 | DosSupplyHeadersPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 13 | DosSupplyHeadersPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 14 | DosSupplyHeadersPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 15 | DosSupplyHeadersPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 16 | DosSupplyHeadersPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 17 | DosSupplyHeadersPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 18 | DosSupplyHeadersPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 19 | DosSupplyHeadersPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 20 | DosSupplyHeadersPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 21 | DosSupplyHeadersPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 22 | DosSupplyHeadersPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 23 | DosSupplyHeadersPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 24 | DosSupplyHeadersPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 25 | DosSupplyHeadersPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 26 | DosSupplyHeadersPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 27 | DosSupplyHeadersPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 28 | DosSupplyHeadersPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 29 | DosSupplyHeadersPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 30 | DosSupplyHeadersPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | DosSupplyHeadersPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 32 | DosSupplyHeadersPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 33 | DosSupplyHeadersPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 34 | DosSupplyHeadersPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 35 | DosSupplyHeadersPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 36 | DosSupplyHeadersPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 37 | DosSupplyHeadersPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 38 | DosSupplyHeadersPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 39 | DosSupplyHeadersPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 40 | DosSupplyHeadersPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 41 | DosSupplyHeadersPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 42 | DosSupplyHeadersPEOCreatedBy | CREATED_BY | — | ✅ |
| 43 | DosSupplyHeadersPEOCreationDate | CREATION_DATE | — | ✅ |
| 44 | DosSupplyHeadersPEOHeaderId | HEADER_ID | 🔑 | ✅ |
| 45 | DosSupplyHeadersPEOInterfaceBatchName | INTERFACE_BATCH_NAME | — | ✅ |
| 46 | DosSupplyHeadersPEOInterfaceBatchNumber | INTERFACE_BATCH_NUMBER | — | ✅ |
| 47 | DosSupplyHeadersPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | ✅ |
| 48 | DosSupplyHeadersPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | DosSupplyHeadersPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 50 | DosSupplyHeadersPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 51 | DosSupplyHeadersPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 52 | DosSupplyHeadersPEOSourceRefDocDescription | SOURCE_REF_DOC_DESCRIPTION | — | ✅ |
| 53 | DosSupplyHeadersPEOStatusCode | STATUS_CODE | — | ✅ |
| 54 | DosSupplyHeadersPEOSupplyOrderNumber | SUPPLY_ORDER_NUMBER | — | ✅ |
| 55 | DosSupplyHeadersPEOSupplyOrderReferenceId | SUPPLY_ORDER_REFERENCE_ID | — | ✅ |
| 56 | DosSupplyHeadersPEOSupplyOrderReferenceNumber | SUPPLY_ORDER_REFERENCE_NUMBER | — | ✅ |
| 57 | DosSupplyHeadersPEOSupplyOrderSource | SUPPLY_ORDER_SOURCE | — | ✅ |
| 58 | DosSupplyHeadersPEOSupplyRequestDate | SUPPLY_REQUEST_DATE | — | ✅ |
| 59 | DosSupplyHeadersPEOTrustedSource | TRUSTED_SOURCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
