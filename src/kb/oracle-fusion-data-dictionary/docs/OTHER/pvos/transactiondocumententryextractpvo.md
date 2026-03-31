---
id: DOC-OTHER-PVO-TransactionDocumentEntryExtractPVO
doc_type: system-doc
title: "TransactionDocumentEntryExtractPVO — PVO Cross-Module"
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
  - TransactionDocumentEntryExtractPVO
  - transactiondocumententryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionDocumentEntryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Document Entry Extract. Acessa as tabelas: PJF_TXN_DOC_ENTRY_B, PJF_TXN_DOC_ENTRY_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.TransactionDocumentEntryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 2 | 1 | 28 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_txn_doc_entry_b|PJF_TXN_DOC_ENTRY_B]] — 33 atributos (1 PKs, 17 BICC)
- [[pjf_txn_doc_entry_tl|PJF_TXN_DOC_ENTRY_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_txn_doc_entry_b|PJF_TXN_DOC_ENTRY_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocEntryBasePEOAllowAdjustmentsFlag | ALLOW_ADJUSTMENTS_FLAG | — | ✅ |
| 2 | TransactionDocEntryBasePEOAllowReversalFlag | ALLOW_REVERSAL_FLAG | — | ✅ |
| 3 | TransactionDocEntryBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 4 | TransactionDocEntryBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 5 | TransactionDocEntryBasePEOAttribute11 | ATTRIBUTE11 | — | — |
| 6 | TransactionDocEntryBasePEOAttribute12 | ATTRIBUTE12 | — | — |
| 7 | TransactionDocEntryBasePEOAttribute13 | ATTRIBUTE13 | — | — |
| 8 | TransactionDocEntryBasePEOAttribute14 | ATTRIBUTE14 | — | — |
| 9 | TransactionDocEntryBasePEOAttribute15 | ATTRIBUTE15 | — | — |
| 10 | TransactionDocEntryBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 11 | TransactionDocEntryBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 12 | TransactionDocEntryBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 13 | TransactionDocEntryBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 14 | TransactionDocEntryBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 15 | TransactionDocEntryBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 16 | TransactionDocEntryBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 17 | TransactionDocEntryBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 18 | TransactionDocEntryBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | TransactionDocEntryBasePEOCcProcessFlag | CC_PROCESS_FLAG | — | ✅ |
| 20 | TransactionDocEntryBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 21 | TransactionDocEntryBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 22 | TransactionDocEntryBasePEODocEntryCode | DOC_ENTRY_CODE | — | ✅ |
| 23 | TransactionDocEntryBasePEODocEntryId | DOC_ENTRY_ID | 🔑 | ✅ |
| 24 | TransactionDocEntryBasePEODocumentId | DOCUMENT_ID | — | ✅ |
| 25 | TransactionDocEntryBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | TransactionDocEntryBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 27 | TransactionDocEntryBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | TransactionDocEntryBasePEOModifyInterfaceFlag | MODIFY_INTERFACE_FLAG | — | ✅ |
| 29 | TransactionDocEntryBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 30 | TransactionDocEntryBasePEOPredefinedFlag | PREDEFINED_FLAG | — | ✅ |
| 31 | TransactionDocEntryBasePEORelatedItemsFlag | RELATED_ITEMS_FLAG | — | ✅ |
| 32 | TransactionDocEntryBasePEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 33 | TransactionDocEntryBasePEOSystemLinkageFunction | SYSTEM_LINKAGE_FUNCTION | — | ✅ |

### [[pjf_txn_doc_entry_tl|PJF_TXN_DOC_ENTRY_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocEntryTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TransactionDocEntryTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TransactionDocEntryTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | TransactionDocEntryTLPEODocEntryId | DOC_ENTRY_ID | — | ✅ |
| 5 | TransactionDocEntryTLPEODocEntryName | DOC_ENTRY_NAME | — | ✅ |
| 6 | TransactionDocEntryTLPEOLanguage | LANGUAGE | — | ✅ |
| 7 | TransactionDocEntryTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | TransactionDocEntryTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | TransactionDocEntryTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | TransactionDocEntryTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | TransactionDocEntryTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
