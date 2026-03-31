---
id: DOC-HCM-PVO-PersonTagAssignmentPVO
doc_type: system-doc
title: "PersonTagAssignmentPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PersonTagAssignmentPVO
  - persontagassignmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonTagAssignmentPVO

## 📌 Visão Geral

Extrai atribuições de tags a pessoas no contexto de Higher Education (Student), com períodos acadêmicos e comentários. Suporta classificação e segmentação de estudantes.

**Caminho:** `FscmTopModelAM.HedHeyPersonTagAssignmentAM.PersonTagAssignmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 66 | 1 | 1 | 7 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[hey_person_tag_assignment|HEY_PERSON_TAG_ASSIGNMENT]] — 66 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[hey_person_tag_assignment|HEY_PERSON_TAG_ASSIGNMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonTagAssignmentPEOAcademicPeriodEndId | ACADEMIC_PERIOD_END_ID | — | ✅ |
| 2 | PersonTagAssignmentPEOAcademicPeriodStartId | ACADEMIC_PERIOD_START_ID | — | ✅ |
| 3 | PersonTagAssignmentPEOAssignmentComments | ASSIGNMENT_COMMENTS | — | ✅ |
| 4 | PersonTagAssignmentPEOAttribute1 | ATTRIBUTE1 | — | — |
| 5 | PersonTagAssignmentPEOAttribute10 | ATTRIBUTE10 | — | — |
| 6 | PersonTagAssignmentPEOAttribute11 | ATTRIBUTE11 | — | — |
| 7 | PersonTagAssignmentPEOAttribute12 | ATTRIBUTE12 | — | — |
| 8 | PersonTagAssignmentPEOAttribute13 | ATTRIBUTE13 | — | — |
| 9 | PersonTagAssignmentPEOAttribute14 | ATTRIBUTE14 | — | — |
| 10 | PersonTagAssignmentPEOAttribute15 | ATTRIBUTE15 | — | — |
| 11 | PersonTagAssignmentPEOAttribute16 | ATTRIBUTE16 | — | — |
| 12 | PersonTagAssignmentPEOAttribute17 | ATTRIBUTE17 | — | — |
| 13 | PersonTagAssignmentPEOAttribute18 | ATTRIBUTE18 | — | — |
| 14 | PersonTagAssignmentPEOAttribute19 | ATTRIBUTE19 | — | — |
| 15 | PersonTagAssignmentPEOAttribute2 | ATTRIBUTE2 | — | — |
| 16 | PersonTagAssignmentPEOAttribute20 | ATTRIBUTE20 | — | — |
| 17 | PersonTagAssignmentPEOAttribute3 | ATTRIBUTE3 | — | — |
| 18 | PersonTagAssignmentPEOAttribute4 | ATTRIBUTE4 | — | — |
| 19 | PersonTagAssignmentPEOAttribute5 | ATTRIBUTE5 | — | — |
| 20 | PersonTagAssignmentPEOAttribute6 | ATTRIBUTE6 | — | — |
| 21 | PersonTagAssignmentPEOAttribute7 | ATTRIBUTE7 | — | — |
| 22 | PersonTagAssignmentPEOAttribute8 | ATTRIBUTE8 | — | — |
| 23 | PersonTagAssignmentPEOAttribute9 | ATTRIBUTE9 | — | — |
| 24 | PersonTagAssignmentPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 25 | PersonTagAssignmentPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 26 | PersonTagAssignmentPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 27 | PersonTagAssignmentPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 28 | PersonTagAssignmentPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 29 | PersonTagAssignmentPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 30 | PersonTagAssignmentPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 31 | PersonTagAssignmentPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 32 | PersonTagAssignmentPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 33 | PersonTagAssignmentPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 34 | PersonTagAssignmentPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 35 | PersonTagAssignmentPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 36 | PersonTagAssignmentPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 37 | PersonTagAssignmentPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 38 | PersonTagAssignmentPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 39 | PersonTagAssignmentPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 40 | PersonTagAssignmentPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 41 | PersonTagAssignmentPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 42 | PersonTagAssignmentPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 43 | PersonTagAssignmentPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 44 | PersonTagAssignmentPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 45 | PersonTagAssignmentPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 46 | PersonTagAssignmentPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 47 | PersonTagAssignmentPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 48 | PersonTagAssignmentPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 49 | PersonTagAssignmentPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 50 | PersonTagAssignmentPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 51 | PersonTagAssignmentPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 52 | PersonTagAssignmentPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 53 | PersonTagAssignmentPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 54 | PersonTagAssignmentPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 55 | PersonTagAssignmentPEOCreatedBy | CREATED_BY | — | — |
| 56 | PersonTagAssignmentPEOCreationDate | CREATION_DATE | — | — |
| 57 | PersonTagAssignmentPEOEndDate | END_DATE | — | ✅ |
| 58 | PersonTagAssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 59 | PersonTagAssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 60 | PersonTagAssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 61 | PersonTagAssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 62 | PersonTagAssignmentPEOPartyId | PARTY_ID | — | — |
| 63 | PersonTagAssignmentPEOPersonTagAssignmentId | PERSON_TAG_ASSIGNMENT_ID | 🔑 | ✅ |
| 64 | PersonTagAssignmentPEOPersonTagNameId | PERSON_TAG_NAME_ID | — | — |
| 65 | PersonTagAssignmentPEOShowToRecipientFlag | SHOW_TO_RECIPIENT_FLAG | — | — |
| 66 | PersonTagAssignmentPEOStartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
