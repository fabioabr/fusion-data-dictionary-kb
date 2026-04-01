---
id: DOC-OTHER-PVO-UNNumberHazardClass1
doc_type: system-doc
title: "UNNumberHazardClass1 — PVO Cross-Module"
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
  - UNNumberHazardClass1
  - unnumberhazardclass1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# UNNumberHazardClass1

## 📌 Visão Geral

View Object para extração BICC de dados de UNNumber Hazard Class1. Acessa as tabelas: PO_HAZARD_CLASSES_VL, PO_UN_NUMBERS_VL.

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.UNNumberHazardClass1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 7 | 2 | 1 | 2 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[po_hazard_classes_vl|PO_HAZARD_CLASSES_VL]] — 3 atributos
- [[po_un_numbers_vl|PO_UN_NUMBERS_VL]] — 4 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[po_hazard_classes_vl|PO_HAZARD_CLASSES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HazardClass | HAZARD_CLASS | — | — |
| 2 | HazardClassId | HAZARD_CLASS_ID | — | — |
| 3 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

### [[po_un_numbers_vl|PO_UN_NUMBERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | — |
| 2 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | UnNumber | UN_NUMBER | — | ✅ |
| 4 | UnNumberId | UN_NUMBER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
