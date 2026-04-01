---
id: DOC-OTHER-PVO-SupplyRequestHeadersExtractPVO
doc_type: system-doc
title: "SupplyRequestHeadersExtractPVO — PVO Cross-Module"
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
  - SupplyRequestHeadersExtractPVO
  - supplyrequestheadersextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplyRequestHeadersExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supply Request Headers Extract. Acessa as tabelas: DOS_SUPPLY_HEADERS_INT.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DosBiccExtractAM.SupplyRequestHeadersExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 19 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[dos_supply_headers_int|DOS_SUPPLY_HEADERS_INT]] — 19 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[dos_supply_headers_int|DOS_SUPPLY_HEADERS_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosSupplyHeadersIntPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | DosSupplyHeadersIntPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | DosSupplyHeadersIntPEOHeaderInterfaceId | HEADER_INTERFACE_ID | 🔑 | ✅ |
| 4 | DosSupplyHeadersIntPEOInterfaceBatchNumber | INTERFACE_BATCH_NUMBER | — | ✅ |
| 5 | DosSupplyHeadersIntPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | ✅ |
| 6 | DosSupplyHeadersIntPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 7 | DosSupplyHeadersIntPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 8 | DosSupplyHeadersIntPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | DosSupplyHeadersIntPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | DosSupplyHeadersIntPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | DosSupplyHeadersIntPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | DosSupplyHeadersIntPEOProcessStatus | PROCESS_STATUS | — | ✅ |
| 13 | DosSupplyHeadersIntPEORequestId | REQUEST_ID | — | ✅ |
| 14 | DosSupplyHeadersIntPEOSourceRefDocDescription | SOURCE_REF_DOC_DESCRIPTION | — | ✅ |
| 15 | DosSupplyHeadersIntPEOSupplyOrderReferenceId | SUPPLY_ORDER_REFERENCE_ID | — | ✅ |
| 16 | DosSupplyHeadersIntPEOSupplyOrderReferenceNumber | SUPPLY_ORDER_REFERENCE_NUMBER | — | ✅ |
| 17 | DosSupplyHeadersIntPEOSupplyOrderSource | SUPPLY_ORDER_SOURCE | — | ✅ |
| 18 | DosSupplyHeadersIntPEOSupplyRequestDate | SUPPLY_REQUEST_DATE | — | ✅ |
| 19 | DosSupplyHeadersIntPEOTrustedSource | TRUSTED_SOURCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
