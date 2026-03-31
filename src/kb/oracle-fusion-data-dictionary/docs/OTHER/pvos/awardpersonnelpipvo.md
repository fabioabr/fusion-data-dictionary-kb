---
id: DOC-OTHER-PVO-AwardPersonnelPIPVO
doc_type: system-doc
title: "AwardPersonnelPIPVO — PVO Cross-Module"
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
  - AwardPersonnelPIPVO
  - awardpersonnelpipvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardPersonnelPIPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Personnel PI. Acessa as tabelas: GMS_AWARD_PERSONNEL, GMS_PERSONS, PER_ALL_PEOPLE_F (+1).

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardPersonnelPIPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 4 | 1 | 7 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_personnel|GMS_AWARD_PERSONNEL]] — 8 atributos (1 PKs, 3 BICC)
- [[gms_persons|GMS_PERSONS]] — 4 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (4 BICC)

---

## ⚙️ Atributos

### [[gms_award_personnel|GMS_AWARD_PERSONNEL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardPersonnelPEOAwardId | AWARD_ID | — | ✅ |
| 2 | AwardPersonnelPEOCreatedBy | CREATED_BY | — | — |
| 3 | AwardPersonnelPEOCreationDate | CREATION_DATE | — | — |
| 4 | AwardPersonnelPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | AwardPersonnelPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | AwardPersonnelPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | AwardPersonnelPEOPersonnelId | PERSONNEL_ID | — | ✅ |
| 8 | Id | ID | 🔑 | ✅ |

### [[gms_persons|GMS_PERSONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GrantsPersonnelPEOConflOfInterestCompDate | CONFL_OF_INTEREST_COMP_DATE | — | — |
| 2 | GrantsPersonnelPEOConflictOfInterestComplete | CONFLICT_OF_INTEREST_COMPLETE | — | — |
| 3 | GrantsPersonnelPEOEligiblePi | ELIGIBLE_PI | — | — |
| 4 | GrantsPersonnelPEOPersonId | PERSON_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonDPEOPersonId | PERSON_ID | — | — |
| 4 | PersonDPEOPersonNumber | PERSON_NUMBER | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNameDPEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 3 | PersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonNameDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | PersonNameDPEOPersonNameId | PERSON_NAME_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
