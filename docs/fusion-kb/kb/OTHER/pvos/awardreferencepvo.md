---
id: DOC-OTHER-PVO-AwardReferencePVO
doc_type: system-doc
title: "AwardReferencePVO — PVO Cross-Module"
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
  - AwardReferencePVO
  - awardreferencepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardReferencePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Reference. Acessa as tabelas: GMS_AWARD_PROJECTS, GMS_AWARD_REFERENCES_VL, GMS_REFERENCES_VL.

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardReferencePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 3 | 1 | 10 | 53% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_projects|GMS_AWARD_PROJECTS]] — 2 atributos
- [[gms_award_references_vl|GMS_AWARD_REFERENCES_VL]] — 12 atributos (1 PKs, 5 BICC)
- [[gms_references_vl|GMS_REFERENCES_VL]] — 5 atributos (5 BICC)

---

## ⚙️ Atributos

### [[gms_award_projects|GMS_AWARD_PROJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardProjectPEOId | ID | — | — |
| 2 | AwardProjectPEOProjectId | PROJECT_ID | — | — |

### [[gms_award_references_vl|GMS_AWARD_REFERENCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardReferencePEOAwardId | AWARD_ID | — | — |
| 2 | AwardReferencePEOAwdProjectLnkId | AWD_PROJECT_LNK_ID | — | ✅ |
| 3 | AwardReferencePEOCreatedBy | CREATED_BY | — | — |
| 4 | AwardReferencePEOCreationDate | CREATION_DATE | — | — |
| 5 | AwardReferencePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AwardReferencePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | AwardReferencePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | AwardReferencePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | AwardReferencePEOReferenceComment | REFERENCE_COMMENT | — | ✅ |
| 10 | AwardReferencePEOReferenceType | REFERENCE_TYPE | — | — |
| 11 | AwardReferencePEOReferenceValue | REFERENCE_VALUE | — | ✅ |
| 12 | Id | ID | 🔑 | ✅ |

### [[gms_references_vl|GMS_REFERENCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReferencePEODescription | DESCRIPTION | — | ✅ |
| 2 | ReferencePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 3 | ReferencePEOReferenceId | REFERENCE_ID | — | ✅ |
| 4 | ReferencePEOReferenceName | REFERENCE_NAME | — | ✅ |
| 5 | ReferencePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
