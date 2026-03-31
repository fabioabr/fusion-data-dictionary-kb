---
id: DOC-OTHER-PVO-AwardCertExtractPVO
doc_type: system-doc
title: "AwardCertExtractPVO — PVO Cross-Module"
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
  - AwardCertExtractPVO
  - awardcertextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardCertExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Cert Extract. Acessa as tabelas: GMS_AWARD_CERTS_B, GMS_AWARD_CERTS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardCertExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 2 | 1 | 29 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_certs_b|GMS_AWARD_CERTS_B]] — 19 atributos (1 PKs, 19 BICC)
- [[gms_award_certs_tl|GMS_AWARD_CERTS_TL]] — 10 atributos (10 BICC)

---

## ⚙️ Atributos

### [[gms_award_certs_b|GMS_AWARD_CERTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardCertBaseApprovalDate | APPROVAL_DATE | — | ✅ |
| 2 | AwardCertBaseAssuranceNumber | ASSURANCE_NUMBER | — | ✅ |
| 3 | AwardCertBaseAwardId | AWARD_ID | — | ✅ |
| 4 | AwardCertBaseAwdProjectLnkId | AWD_PROJECT_LNK_ID | — | ✅ |
| 5 | AwardCertBaseCertificationDate | CERTIFICATION_DATE | — | ✅ |
| 6 | AwardCertBaseCertificationId | CERTIFICATION_ID | — | ✅ |
| 7 | AwardCertBaseCertifiedBy | CERTIFIED_BY | — | ✅ |
| 8 | AwardCertBaseCreatedBy | CREATED_BY | — | ✅ |
| 9 | AwardCertBaseCreationDate | CREATION_DATE | — | ✅ |
| 10 | AwardCertBaseExemptionNumber | EXEMPTION_NUMBER | — | ✅ |
| 11 | AwardCertBaseExpeditedReview | EXPEDITED_REVIEW | — | ✅ |
| 12 | AwardCertBaseExpirationDate | EXPIRATION_DATE | — | ✅ |
| 13 | AwardCertBaseFullReview | FULL_REVIEW | — | ✅ |
| 14 | AwardCertBaseId | ID | 🔑 | ✅ |
| 15 | AwardCertBaseIndicator | INDICATOR | — | ✅ |
| 16 | AwardCertBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | AwardCertBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | AwardCertBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | AwardCertBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

### [[gms_award_certs_tl|GMS_AWARD_CERTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardCertTransLangComments | COMMENTS | — | ✅ |
| 2 | AwardCertTransLangCreatedBy | CREATED_BY | — | ✅ |
| 3 | AwardCertTransLangCreationDate | CREATION_DATE | — | ✅ |
| 4 | AwardCertTransLangId | ID | — | ✅ |
| 5 | AwardCertTransLangLanguage | LANGUAGE | — | ✅ |
| 6 | AwardCertTransLangLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AwardCertTransLangLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AwardCertTransLangLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AwardCertTransLangObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | AwardCertTransLangSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
