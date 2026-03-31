---
id: DOC-OTHER-PVO-InstitutionCertificationsPVO
doc_type: system-doc
title: "InstitutionCertificationsPVO — PVO Cross-Module"
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
  - InstitutionCertificationsPVO
  - institutioncertificationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InstitutionCertificationsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Institution Certifications. Acessa as tabelas: GMS_CERTIFICATIONS_VL, GMS_INSTITUTION_CERTS_VL, GMS_SPONSORS_VL (+1).

**Caminho:** `FscmTopModelAM.GmsSetupAM.InstitutionCertificationsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 4 | 1 | 13 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[gms_certifications_vl|GMS_CERTIFICATIONS_VL]] — 11 atributos (5 BICC)
- [[gms_institution_certs_vl|GMS_INSTITUTION_CERTS_VL]] — 12 atributos (1 PKs, 7 BICC)
- [[gms_sponsors_vl|GMS_SPONSORS_VL]] — 2 atributos
- [[hz_parties|HZ_PARTIES]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[gms_certifications_vl|GMS_CERTIFICATIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CertificationPEOCertificationId | CERTIFICATION_ID | — | — |
| 2 | CertificationPEOCertificationName | CERTIFICATION_NAME | — | ✅ |
| 3 | CertificationPEOCreatedBy | CREATED_BY | — | — |
| 4 | CertificationPEOCreationDate | CREATION_DATE | — | — |
| 5 | CertificationPEODescription | DESCRIPTION | — | ✅ |
| 6 | CertificationPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 7 | CertificationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CertificationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | CertificationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | CertificationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | CertificationPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[gms_institution_certs_vl|GMS_INSTITUTION_CERTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstitutionCertificationsPEOCertificationDate | CERTIFICATION_DATE | — | ✅ |
| 2 | InstitutionCertificationsPEOCertificationId | CERTIFICATION_ID | — | — |
| 3 | InstitutionCertificationsPEOComments | COMMENTS | — | ✅ |
| 4 | InstitutionCertificationsPEOExpirationDate | EXPIRATION_DATE | — | ✅ |
| 5 | InstitutionCertificationsPEOInstitutionId | INSTITUTION_ID | — | — |
| 6 | InstitutionCertificationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InstitutionCertificationsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | InstitutionCertificationsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | InstitutionCertificationsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | InstitutionCertificationsPEOReferenceNumber | REFERENCE_NUMBER | — | ✅ |
| 11 | InstitutionCertificationsPEOStatus | STATUS | — | ✅ |
| 12 | InstnCertId | INSTN_CERT_ID | 🔑 | ✅ |

### [[gms_sponsors_vl|GMS_SPONSORS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SponsorPEOPartyId | PARTY_ID | — | — |
| 2 | SponsorPEOSponsorId | SPONSOR_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPEOPartyId | PARTY_ID | — | — |
| 2 | PartyPEOPartyName | PARTY_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
