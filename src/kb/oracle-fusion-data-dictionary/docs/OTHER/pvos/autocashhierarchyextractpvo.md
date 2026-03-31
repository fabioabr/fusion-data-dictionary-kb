---
id: DOC-OTHER-PVO-AutoCashHierarchyExtractPVO
doc_type: system-doc
title: "AutoCashHierarchyExtractPVO — PVO Cross-Module"
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
  - AutoCashHierarchyExtractPVO
  - autocashhierarchyextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AutoCashHierarchyExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Auto Cash Hierarchy Extract. Acessa as tabelas: AR_AUTOCASH_HIERARCHIES.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.AutoCashHierarchyExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 1 | 1 | 17 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[ar_autocash_hierarchies|AR_AUTOCASH_HIERARCHIES]] — 33 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[ar_autocash_hierarchies|AR_AUTOCASH_HIERARCHIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArAutoCashHierarchyApplyPartialPayments | APPLY_PARTIAL_PAYMENTS | — | ✅ |
| 2 | ArAutoCashHierarchyAttribute1 | ATTRIBUTE1 | — | — |
| 3 | ArAutoCashHierarchyAttribute10 | ATTRIBUTE10 | — | — |
| 4 | ArAutoCashHierarchyAttribute11 | ATTRIBUTE11 | — | — |
| 5 | ArAutoCashHierarchyAttribute12 | ATTRIBUTE12 | — | — |
| 6 | ArAutoCashHierarchyAttribute13 | ATTRIBUTE13 | — | — |
| 7 | ArAutoCashHierarchyAttribute14 | ATTRIBUTE14 | — | — |
| 8 | ArAutoCashHierarchyAttribute15 | ATTRIBUTE15 | — | — |
| 9 | ArAutoCashHierarchyAttribute2 | ATTRIBUTE2 | — | — |
| 10 | ArAutoCashHierarchyAttribute3 | ATTRIBUTE3 | — | — |
| 11 | ArAutoCashHierarchyAttribute4 | ATTRIBUTE4 | — | — |
| 12 | ArAutoCashHierarchyAttribute5 | ATTRIBUTE5 | — | — |
| 13 | ArAutoCashHierarchyAttribute6 | ATTRIBUTE6 | — | — |
| 14 | ArAutoCashHierarchyAttribute7 | ATTRIBUTE7 | — | — |
| 15 | ArAutoCashHierarchyAttribute8 | ATTRIBUTE8 | — | — |
| 16 | ArAutoCashHierarchyAttribute9 | ATTRIBUTE9 | — | — |
| 17 | ArAutoCashHierarchyAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 18 | ArAutoCashHierarchyAutocashHierarchyId | AUTOCASH_HIERARCHY_ID | 🔑 | ✅ |
| 19 | ArAutoCashHierarchyCreatedBy | CREATED_BY | — | ✅ |
| 20 | ArAutoCashHierarchyCreationDate | CREATION_DATE | — | ✅ |
| 21 | ArAutoCashHierarchyDescription | DESCRIPTION | — | ✅ |
| 22 | ArAutoCashHierarchyHierarchyName | HIERARCHY_NAME | — | ✅ |
| 23 | ArAutoCashHierarchyIncludeDiscounts | INCLUDE_DISCOUNTS | — | ✅ |
| 24 | ArAutoCashHierarchyIncludeDisputeItems | INCLUDE_DISPUTE_ITEMS | — | ✅ |
| 25 | ArAutoCashHierarchyIncludeFinanceCharges | INCLUDE_FINANCE_CHARGES | — | ✅ |
| 26 | ArAutoCashHierarchyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | ArAutoCashHierarchyLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 28 | ArAutoCashHierarchyLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | ArAutoCashHierarchyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 30 | ArAutoCashHierarchyRemainingAmount | REMAINING_AMOUNT | — | ✅ |
| 31 | ArAutoCashHierarchySeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 32 | ArAutoCashHierarchySetId | SET_ID | — | ✅ |
| 33 | ArAutoCashHierarchyStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
