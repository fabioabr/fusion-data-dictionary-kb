---
id: DOC-OTHER-PVO-CertificationTranslationExtractPVO
doc_type: system-doc
title: "CertificationTranslationExtractPVO — PVO Cross-Module"
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
  - CertificationTranslationExtractPVO
  - certificationtranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CertificationTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Certification Translation Extract. Acessa as tabelas: GMS_CERTIFICATIONS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.CertificationTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_certifications_tl|GMS_CERTIFICATIONS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[gms_certifications_tl|GMS_CERTIFICATIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CertificationTranslationCertificationId | CERTIFICATION_ID | 🔑 | ✅ |
| 2 | CertificationTranslationCertificationName | CERTIFICATION_NAME | — | ✅ |
| 3 | CertificationTranslationCreatedBy | CREATED_BY | — | ✅ |
| 4 | CertificationTranslationCreationDate | CREATION_DATE | — | ✅ |
| 5 | CertificationTranslationDescription | DESCRIPTION | — | ✅ |
| 6 | CertificationTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | CertificationTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CertificationTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | CertificationTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | CertificationTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | CertificationTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
