---
id: DOC-OTHER-PVO-BillTypeClassTLExtractPVO
doc_type: system-doc
title: "BillTypeClassTLExtractPVO — PVO Cross-Module"
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
  - BillTypeClassTLExtractPVO
  - billtypeclasstlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillTypeClassTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bill Type Class TLExtract. Acessa as tabelas: PJB_BILL_TYPE_CLASSES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.BillTypeClassTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_bill_type_classes_tl|PJB_BILL_TYPE_CLASSES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjb_bill_type_classes_tl|PJB_BILL_TYPE_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillTypeClassTLPEOBillTypeClassificationCode | BILL_TYPE_CLASSIFICATION_CODE | 🔑 | ✅ |
| 2 | BillTypeClassTLPEOBillTypeDesc | BILL_TYPE_DESC | — | ✅ |
| 3 | BillTypeClassTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | BillTypeClassTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | BillTypeClassTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | BillTypeClassTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | BillTypeClassTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | BillTypeClassTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | BillTypeClassTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | BillTypeClassTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 11 | BillTypeClassTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
