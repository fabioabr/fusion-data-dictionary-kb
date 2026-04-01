---
id: DOC-OTHER-PVO-InstitutionReferencesPVO
doc_type: system-doc
title: "InstitutionReferencesPVO — PVO Cross-Module"
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
  - InstitutionReferencesPVO
  - institutionreferencespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InstitutionReferencesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Institution References. Acessa as tabelas: GMS_INSTN_REFERENCES_VL, GMS_REFERENCES_VL.

**Caminho:** `FscmTopModelAM.GmsSetupAM.InstitutionReferencesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 2 | 1 | 8 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[gms_instn_references_vl|GMS_INSTN_REFERENCES_VL]] — 5 atributos (1 PKs, 3 BICC)
- [[gms_references_vl|GMS_REFERENCES_VL]] — 11 atributos (5 BICC)

---

## ⚙️ Atributos

### [[gms_instn_references_vl|GMS_INSTN_REFERENCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstitutionReferencesComments | COMMENTS | — | ✅ |
| 2 | InstitutionReferencesInstitutionId | INSTITUTION_ID | — | — |
| 3 | InstitutionReferencesReferenceId | REFERENCE_ID | — | — |
| 4 | InstitutionReferencesValue | VALUE | — | ✅ |
| 5 | InstnReferenceId | INSTN_REFERENCE_ID | 🔑 | ✅ |

### [[gms_references_vl|GMS_REFERENCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 2 | ReferenceCreatedBy | CREATED_BY | — | — |
| 3 | ReferenceCreationDate | CREATION_DATE | — | — |
| 4 | ReferenceDescription | DESCRIPTION | — | ✅ |
| 5 | ReferenceEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 6 | ReferenceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ReferenceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ReferenceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ReferenceReferenceId | REFERENCE_ID | — | — |
| 10 | ReferenceReferenceName | REFERENCE_NAME | — | ✅ |
| 11 | ReferenceStartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
