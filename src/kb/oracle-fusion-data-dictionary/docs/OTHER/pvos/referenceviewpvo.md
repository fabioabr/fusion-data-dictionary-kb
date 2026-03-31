---
id: DOC-OTHER-PVO-ReferenceViewPVO
doc_type: system-doc
title: "ReferenceViewPVO — PVO Cross-Module"
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
  - ReferenceViewPVO
  - referenceviewpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReferenceViewPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reference View. Acessa as tabelas: GMS_REFERENCES_VL.

**Caminho:** `FscmTopModelAM.GmsSetupAM.ReferenceViewPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 6 | 55% |

---

## 🔗 Tabelas Relacionadas

- [[gms_references_vl|GMS_REFERENCES_VL]] — 11 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[gms_references_vl|GMS_REFERENCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReferenceId | REFERENCE_ID | 🔑 | ✅ |
| 2 | ReferencePEOCreatedBy | CREATED_BY | — | — |
| 3 | ReferencePEOCreationDate | CREATION_DATE | — | — |
| 4 | ReferencePEODescription | DESCRIPTION | — | ✅ |
| 5 | ReferencePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 6 | ReferencePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ReferencePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ReferencePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ReferencePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ReferencePEOReferenceName | REFERENCE_NAME | — | ✅ |
| 11 | ReferencePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
