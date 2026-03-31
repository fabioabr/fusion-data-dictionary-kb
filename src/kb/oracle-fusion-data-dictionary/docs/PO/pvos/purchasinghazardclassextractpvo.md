---
id: DOC-PO-PVO-PurchasingHazardClassExtractPVO
doc_type: system-doc
title: "PurchasingHazardClassExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PurchasingHazardClassExtractPVO
  - purchasinghazardclassextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingHazardClassExtractPVO

## 📌 Visão Geral

Extrai as classes de materiais perigosos para carga BICC, incluindo códigos de risco, descrições e regulamentações. Essencial para compliance em transporte e armazenamento de produtos controlados.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingHazardClassExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 0 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[po_hazard_classes_b|PO_HAZARD_CLASSES_B]] — 9 atributos (9 BICC)
- [[po_hazard_classes_tl|PO_HAZARD_CLASSES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[po_hazard_classes_b|PO_HAZARD_CLASSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HazardClassId | HAZARD_CLASS_ID | — | ✅ |
| 2 | PurchasingHazardClsCreatedBy | CREATED_BY | — | ✅ |
| 3 | PurchasingHazardClsCreationDate | CREATION_DATE | — | ✅ |
| 4 | PurchasingHazardClsHazardClassCode | HAZARD_CLASS_CODE | — | ✅ |
| 5 | PurchasingHazardClsInactiveDate | INACTIVE_DATE | — | ✅ |
| 6 | PurchasingHazardClsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PurchasingHazardClsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | PurchasingHazardClsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | PurchasingHazardClsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

### [[po_hazard_classes_tl|PO_HAZARD_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingHazardClsTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | PurchasingHazardClsTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | PurchasingHazardClsTLDescription | DESCRIPTION | — | ✅ |
| 4 | PurchasingHazardClsTLHazardClass | HAZARD_CLASS | — | ✅ |
| 5 | PurchasingHazardClsTLHazardClassId | HAZARD_CLASS_ID | — | ✅ |
| 6 | PurchasingHazardClsTLLanguage | LANGUAGE | — | ✅ |
| 7 | PurchasingHazardClsTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PurchasingHazardClsTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | PurchasingHazardClsTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PurchasingHazardClsTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PurchasingHazardClsTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
