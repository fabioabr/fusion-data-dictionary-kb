---
id: DOC-OTHER-PVO-AwardCertificationPVO
doc_type: system-doc
title: "AwardCertificationPVO — PVO Cross-Module"
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
  - AwardCertificationPVO
  - awardcertificationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardCertificationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Certification. Acessa as tabelas: GMS_AWARD_CERTS_VL, GMS_AWARD_PROJECTS, GMS_CERTIFICATIONS_VL (+1).

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardCertificationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 4 | 1 | 19 | 59% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_certs_vl|GMS_AWARD_CERTS_VL]] — 20 atributos (1 PKs, 12 BICC)
- [[gms_award_projects|GMS_AWARD_PROJECTS]] — 2 atributos
- [[gms_certifications_vl|GMS_CERTIFICATIONS_VL]] — 5 atributos (5 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (2 BICC)

---

## ⚙️ Atributos

### [[gms_award_certs_vl|GMS_AWARD_CERTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardCertificationPEOApprovalDate | APPROVAL_DATE | — | ✅ |
| 2 | AwardCertificationPEOAssuranceNumber | ASSURANCE_NUMBER | — | ✅ |
| 3 | AwardCertificationPEOAwardId | AWARD_ID | — | — |
| 4 | AwardCertificationPEOAwdProjectLnkId | AWD_PROJECT_LNK_ID | — | ✅ |
| 5 | AwardCertificationPEOCertificationDate | CERTIFICATION_DATE | — | ✅ |
| 6 | AwardCertificationPEOCertificationId | CERTIFICATION_ID | — | — |
| 7 | AwardCertificationPEOCertifiedBy | CERTIFIED_BY | — | — |
| 8 | AwardCertificationPEOComments | COMMENTS | — | ✅ |
| 9 | AwardCertificationPEOCreatedBy | CREATED_BY | — | — |
| 10 | AwardCertificationPEOCreationDate | CREATION_DATE | — | — |
| 11 | AwardCertificationPEOExemptionNumber | EXEMPTION_NUMBER | — | ✅ |
| 12 | AwardCertificationPEOExpeditedReview | EXPEDITED_REVIEW | — | ✅ |
| 13 | AwardCertificationPEOExpirationDate | EXPIRATION_DATE | — | ✅ |
| 14 | AwardCertificationPEOFullReview | FULL_REVIEW | — | ✅ |
| 15 | AwardCertificationPEOIndicator | INDICATOR | — | ✅ |
| 16 | AwardCertificationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | AwardCertificationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | AwardCertificationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | AwardCertificationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | Id | ID | 🔑 | ✅ |

### [[gms_award_projects|GMS_AWARD_PROJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardProjectPEOId | ID | — | — |
| 2 | AwardProjectPEOProjectId | PROJECT_ID | — | — |

### [[gms_certifications_vl|GMS_CERTIFICATIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CertificationPEOCertificationId | CERTIFICATION_ID | — | ✅ |
| 2 | CertificationPEOCertificationName | CERTIFICATION_NAME | — | ✅ |
| 3 | CertificationPEODescription | DESCRIPTION | — | ✅ |
| 4 | CertificationPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 5 | CertificationPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNameDPEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonNameDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | PersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
