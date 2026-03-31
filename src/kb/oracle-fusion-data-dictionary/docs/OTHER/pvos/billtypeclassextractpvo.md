---
id: DOC-OTHER-PVO-BillTypeClassExtractPVO
doc_type: system-doc
title: "BillTypeClassExtractPVO — PVO Cross-Module"
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
  - BillTypeClassExtractPVO
  - billtypeclassextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillTypeClassExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bill Type Class Extract. Acessa as tabelas: PJB_BILL_TYPE_CLASSES_B, PJB_BILL_TYPE_CLASSES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.BillTypeClassExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 3 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_bill_type_classes_b|PJB_BILL_TYPE_CLASSES_B]] — 10 atributos (1 PKs, 10 BICC)
- [[pjb_bill_type_classes_tl|PJB_BILL_TYPE_CLASSES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjb_bill_type_classes_b|PJB_BILL_TYPE_CLASSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillTypeClassBasePEOBillTypeClassificationCode | BILL_TYPE_CLASSIFICATION_CODE | 🔑 | ✅ |
| 2 | BillTypeClassBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | BillTypeClassBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | BillTypeClassBasePEOInvoiceFlag | INVOICE_FLAG | — | ✅ |
| 5 | BillTypeClassBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | BillTypeClassBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | BillTypeClassBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | BillTypeClassBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | BillTypeClassBasePEORevenueFlag | REVENUE_FLAG | — | ✅ |
| 10 | BillTypeClassBasePEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |

### [[pjb_bill_type_classes_tl|PJB_BILL_TYPE_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillTypeClassTransLangPEOBillTypeClassificationCode | BILL_TYPE_CLASSIFICATION_CODE | 🔑 | ✅ |
| 2 | BillTypeClassTransLangPEOBillTypeDesc | BILL_TYPE_DESC | — | ✅ |
| 3 | BillTypeClassTransLangPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | BillTypeClassTransLangPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | BillTypeClassTransLangPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | BillTypeClassTransLangPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | BillTypeClassTransLangPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | BillTypeClassTransLangPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | BillTypeClassTransLangPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | BillTypeClassTransLangPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 11 | BillTypeClassTransLangPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
