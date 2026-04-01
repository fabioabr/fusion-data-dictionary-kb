---
id: DOC-HCM-PVO-CandidateAddressesPVO
doc_type: system-doc
title: "CandidateAddressesPVO — PVO Human Capital Management"
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
  - CandidateAddressesPVO
  - candidateaddressespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CandidateAddressesPVO

## 📌 Visão Geral

Extrai enderecos de candidatos com dados de logradouro. Suporta gestao de localizacao e correspondencia com candidatos em processos seletivos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCandidatesAM.CandidateAddressesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 2 | 1 | 13 | 93% |

---

## 🔗 Tabelas Relacionadas

- [[irc_candidate_address_v|IRC_CANDIDATE_ADDRESS_V]] — 2 atributos (1 PKs, 1 BICC)
- [[per_addresses_f|PER_ADDRESSES_F]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[irc_candidate_address_v|IRC_CANDIDATE_ADDRESS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CandidateAddressPEOAddressId | ADDRESS_ID | — | — |
| 2 | PersonId | PERSON_ID | 🔑 | ✅ |

### [[per_addresses_f|PER_ADDRESSES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressId | ADDRESS_ID | — | ✅ |
| 2 | AddressLine1 | ADDRESS_LINE_1 | — | ✅ |
| 3 | AddressLine2 | ADDRESS_LINE_2 | — | ✅ |
| 4 | Country | COUNTRY | — | ✅ |
| 5 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PostalCode | POSTAL_CODE | — | ✅ |
| 9 | Region1 | REGION_1 | — | ✅ |
| 10 | Region2 | REGION_2 | — | ✅ |
| 11 | Region3 | REGION_3 | — | ✅ |
| 12 | TownOrCity | TOWN_OR_CITY | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
