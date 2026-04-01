---
id: DOC-OTHER-PVO-PersonDetailsRefPVO
doc_type: system-doc
title: "PersonDetailsRefPVO — PVO Cross-Module"
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
  - PersonDetailsRefPVO
  - persondetailsrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonDetailsRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Details Ref. Acessa as tabelas: HZ_PARTIES, HZ_PARTY_USG_ASSIGNMENTS, WIS_PARTY_PERSON_DETAILS_V.

**Caminho:** `FscmTopModelAM.ResourceAM.PersonDetailsRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 3 | 2 | 12 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 10 atributos (1 PKs, 8 BICC)
- [[hz_party_usg_assignments|HZ_PARTY_USG_ASSIGNMENTS]] — 5 atributos (1 PKs, 2 BICC)
- [[wis_party_person_details_v|WIS_PARTY_PERSON_DETAILS_V]] — 2 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyId | PARTY_ID | 🔑 | ✅ |
| 2 | PartyPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 3 | PartyPEOPartyName | PARTY_NAME | — | ✅ |
| 4 | PartyPEOPartyNumber | PARTY_NUMBER | — | ✅ |
| 5 | PartyPEOPartyType | PARTY_TYPE | — | — |
| 6 | PartyPEOPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 7 | PartyPEOPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 8 | PartyPEOPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 9 | PartyPEOPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 10 | Status | STATUS | — | — |

### [[hz_party_usg_assignments|HZ_PARTY_USG_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | StatusFlag | STATUS_FLAG | — | — |
| 4 | USGAssPEOPartyUsageCode | PARTY_USAGE_CODE | — | ✅ |
| 5 | USGAssPEOPartyUsgAssignmentId | PARTY_USG_ASSIGNMENT_ID | 🔑 | ✅ |

### [[wis_party_person_details_v|WIS_PARTY_PERSON_DETAILS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPEOPersonId | PERSON_ID | — | ✅ |
| 2 | PartyPEOPersonNumber | PERSON_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
