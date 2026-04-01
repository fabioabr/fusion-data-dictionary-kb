---
id: DOC-OTHER-PVO-CertificationViewPVO
doc_type: system-doc
title: "CertificationViewPVO — PVO Cross-Module"
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
  - CertificationViewPVO
  - certificationviewpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CertificationViewPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Certification View. Acessa as tabelas: GMS_CERTIFICATIONS_VL.

**Caminho:** `FscmTopModelAM.GmsSetupAM.CertificationViewPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 6 | 55% |

---

## 🔗 Tabelas Relacionadas

- [[gms_certifications_vl|GMS_CERTIFICATIONS_VL]] — 11 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[gms_certifications_vl|GMS_CERTIFICATIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CertificationId | CERTIFICATION_ID | 🔑 | ✅ |
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

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
