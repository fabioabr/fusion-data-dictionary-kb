---
id: DOC-OTHER-PVO-SponsorReferencePVO
doc_type: system-doc
title: "SponsorReferencePVO — PVO Cross-Module"
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
  - SponsorReferencePVO
  - sponsorreferencepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SponsorReferencePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Sponsor Reference. Acessa as tabelas: GMS_REFERENCES_VL, GMS_SPONSORS_REFERENCES_VL.

**Caminho:** `FscmTopModelAM.GmsSetupAM.SponsorReferencePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 1 | 9 | 41% |

---

## 🔗 Tabelas Relacionadas

- [[gms_references_vl|GMS_REFERENCES_VL]] — 11 atributos (5 BICC)
- [[gms_sponsors_references_vl|GMS_SPONSORS_REFERENCES_VL]] — 11 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[gms_references_vl|GMS_REFERENCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReferenceCreatedBy | CREATED_BY | — | — |
| 2 | ReferenceCreationDate | CREATION_DATE | — | — |
| 3 | ReferenceDescription | DESCRIPTION | — | ✅ |
| 4 | ReferenceEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 5 | ReferenceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ReferenceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ReferenceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ReferenceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ReferenceReferenceId | REFERENCE_ID | — | — |
| 10 | ReferenceReferenceName | REFERENCE_NAME | — | ✅ |
| 11 | ReferenceStartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[gms_sponsors_references_vl|GMS_SPONSORS_REFERENCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SponsReferenceId | SPONS_REFERENCE_ID | 🔑 | ✅ |
| 2 | SponsorReferenceComments | COMMENTS | — | ✅ |
| 3 | SponsorReferenceCreatedBy | CREATED_BY | — | — |
| 4 | SponsorReferenceCreationDate | CREATION_DATE | — | — |
| 5 | SponsorReferenceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SponsorReferenceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | SponsorReferenceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | SponsorReferenceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SponsorReferenceReferenceId | REFERENCE_ID | — | — |
| 10 | SponsorReferenceSponsorId | SPONSOR_ID | — | — |
| 11 | SponsorReferenceValue | VALUE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
