---
id: DOC-HCM-653
doc_type: system-doc
title: "JTF_RS_RESOURCE_PROFILES — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - JTF_RS_RESOURCE_PROFILES
  - jtf_rs_resource_profiles
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# JTF_RS_RESOURCE_PROFILES

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATED_BY_MODULE | — | — | — | — | — | — |
| 3 | CREATION_DATE | — | — | — | — | — | — |
| 4 | EMAIL_ADDRESS | — | — | — | — | — | — |
| 5 | END_DATE_ACTIVE | — | — | — | — | — | — |
| 6 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 7 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 8 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 9 | PARTY_ID | — | — | — | — | — | — |
| 10 | PERSONAL_EMAIL_FLAG | — | — | — | — | — | — |
| 11 | PERSON_FIRST_NAME | — | — | — | — | — | — |
| 12 | PERSON_LAST_NAME | — | — | — | — | — | — |
| 13 | PERSON_NAME | — | — | — | — | — | — |
| 14 | PERSON_TITLE | — | — | — | — | — | — |
| 15 | PRIMARY_PHONE_NUMBER | — | — | — | — | — | — |
| 16 | RESOURCE_PROFILE_ID | — | — | — | — | — | — |
| 17 | START_DATE_ACTIVE | — | — | — | — | — | — |
| 18 | TIMEZONE_CODE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[resourcep|ResourceP]] (OTHER · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EMAIL_ADDRESS | EmailAddress | ✅ |
| PARTY_ID | PartyId | ✅ |
| PERSON_FIRST_NAME | PersonFirstName | ✅ |
| PERSON_LAST_NAME | PersonLastName | ✅ |
| PERSON_NAME | PersonName | ✅ |
| PERSON_TITLE | PersonTitle | ✅ |
| PERSONAL_EMAIL_FLAG | PersonalEmailFlag | ✅ |
| PRIMARY_PHONE_NUMBER | PrimaryPhoneNumber | ✅ |
| RESOURCE_PROFILE_ID | ResourceProfileId | ✅ |
| RESOURCE_PROFILE_ID | ResourceProfileId1 | ✅ |
| START_DATE_ACTIVE | StartDateActive | ✅ |
| TIMEZONE_CODE | TimezoneCode | ✅ |

### [[resourcepartnerpvo|ResourcePartnerPVO]] (OTHER · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ResourcePEOCreatedBy | — |
| CREATED_BY_MODULE | ResourcePEOCreatedByModule | — |
| CREATION_DATE | ResourcePEOCreationDate | — |
| END_DATE_ACTIVE | EndDateActive | — |
| LAST_UPDATE_DATE | ResourcePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ResourcePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ResourcePEOLastUpdatedBy | — |
| PARTY_ID | ResourcePEOPartyId | — |
| RESOURCE_PROFILE_ID | ResourceProfileId | ✅ |
| START_DATE_ACTIVE | StartDateActive | — |
| TIMEZONE_CODE | TimezoneCode | — |
