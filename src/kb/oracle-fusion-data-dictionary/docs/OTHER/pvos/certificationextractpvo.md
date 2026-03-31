---
id: DOC-OTHER-PVO-CertificationExtractPVO
doc_type: system-doc
title: "CertificationExtractPVO — PVO Cross-Module"
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
  - CertificationExtractPVO
  - certificationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CertificationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Certification Extract. Acessa as tabelas: GMS_CERTIFICATIONS_B, GMS_CERTIFICATIONS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.CertificationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_certifications_b|GMS_CERTIFICATIONS_B]] — 10 atributos (1 PKs, 10 BICC)
- [[gms_certifications_tl|GMS_CERTIFICATIONS_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[gms_certifications_b|GMS_CERTIFICATIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CertificationBaseCertificationId | CERTIFICATION_ID | 🔑 | ✅ |
| 2 | CertificationBaseCertificationUsage | CERTIFICATION_USAGE | — | ✅ |
| 3 | CertificationBaseCreatedBy | CREATED_BY | — | ✅ |
| 4 | CertificationBaseCreationDate | CREATION_DATE | — | ✅ |
| 5 | CertificationBaseEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 6 | CertificationBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CertificationBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CertificationBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CertificationBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | CertificationBaseStartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[gms_certifications_tl|GMS_CERTIFICATIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CertificationTransLangCertificationId | CERTIFICATION_ID | — | ✅ |
| 2 | CertificationTransLangCertificationName | CERTIFICATION_NAME | — | ✅ |
| 3 | CertificationTransLangCreatedBy | CREATED_BY | — | ✅ |
| 4 | CertificationTransLangCreationDate | CREATION_DATE | — | ✅ |
| 5 | CertificationTransLangDescription | DESCRIPTION | — | ✅ |
| 6 | CertificationTransLangLanguage | LANGUAGE | — | ✅ |
| 7 | CertificationTransLangLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CertificationTransLangLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | CertificationTransLangLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | CertificationTransLangObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | CertificationTransLangSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
