---
id: DOC-OTHER-PVO-AcademicOrganizationPVO
doc_type: system-doc
title: "AcademicOrganizationPVO — PVO Cross-Module"
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
  - AcademicOrganizationPVO
  - academicorganizationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AcademicOrganizationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Academic Organization. Acessa as tabelas: HER_ACADEMIC_ORG_VL.

**Caminho:** `FscmTopModelAM.StudentEnrollmentAM.AcademicOrganizationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 68 | 1 | 3 | 7 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[her_academic_org_vl|HER_ACADEMIC_ORG_VL]] — 68 atributos (3 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[her_academic_org_vl|HER_ACADEMIC_ORG_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcademicOrgDPEOAcademicOrgId | ACADEMIC_ORG_ID | 🔑 | ✅ |
| 2 | AcademicOrgDPEOAcademicOrgName | ACADEMIC_ORG_NAME | — | ✅ |
| 3 | AcademicOrgDPEOAcademicOrgStatusCode | ACADEMIC_ORG_STATUS_CODE | — | — |
| 4 | AcademicOrgDPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 5 | AcademicOrgDPEOAttribute1 | ATTRIBUTE1 | — | — |
| 6 | AcademicOrgDPEOAttribute10 | ATTRIBUTE10 | — | — |
| 7 | AcademicOrgDPEOAttribute11 | ATTRIBUTE11 | — | — |
| 8 | AcademicOrgDPEOAttribute12 | ATTRIBUTE12 | — | — |
| 9 | AcademicOrgDPEOAttribute13 | ATTRIBUTE13 | — | — |
| 10 | AcademicOrgDPEOAttribute14 | ATTRIBUTE14 | — | — |
| 11 | AcademicOrgDPEOAttribute15 | ATTRIBUTE15 | — | — |
| 12 | AcademicOrgDPEOAttribute16 | ATTRIBUTE16 | — | — |
| 13 | AcademicOrgDPEOAttribute17 | ATTRIBUTE17 | — | — |
| 14 | AcademicOrgDPEOAttribute18 | ATTRIBUTE18 | — | — |
| 15 | AcademicOrgDPEOAttribute19 | ATTRIBUTE19 | — | — |
| 16 | AcademicOrgDPEOAttribute2 | ATTRIBUTE2 | — | — |
| 17 | AcademicOrgDPEOAttribute20 | ATTRIBUTE20 | — | — |
| 18 | AcademicOrgDPEOAttribute3 | ATTRIBUTE3 | — | — |
| 19 | AcademicOrgDPEOAttribute4 | ATTRIBUTE4 | — | — |
| 20 | AcademicOrgDPEOAttribute5 | ATTRIBUTE5 | — | — |
| 21 | AcademicOrgDPEOAttribute6 | ATTRIBUTE6 | — | — |
| 22 | AcademicOrgDPEOAttribute7 | ATTRIBUTE7 | — | — |
| 23 | AcademicOrgDPEOAttribute8 | ATTRIBUTE8 | — | — |
| 24 | AcademicOrgDPEOAttribute9 | ATTRIBUTE9 | — | — |
| 25 | AcademicOrgDPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 26 | AcademicOrgDPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 27 | AcademicOrgDPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 28 | AcademicOrgDPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 29 | AcademicOrgDPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 30 | AcademicOrgDPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 31 | AcademicOrgDPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 32 | AcademicOrgDPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 33 | AcademicOrgDPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 34 | AcademicOrgDPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 35 | AcademicOrgDPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 36 | AcademicOrgDPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 37 | AcademicOrgDPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 38 | AcademicOrgDPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 39 | AcademicOrgDPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 40 | AcademicOrgDPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 41 | AcademicOrgDPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 42 | AcademicOrgDPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 43 | AcademicOrgDPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 44 | AcademicOrgDPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 45 | AcademicOrgDPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 46 | AcademicOrgDPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 47 | AcademicOrgDPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 48 | AcademicOrgDPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 49 | AcademicOrgDPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 50 | AcademicOrgDPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 51 | AcademicOrgDPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 52 | AcademicOrgDPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 53 | AcademicOrgDPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 54 | AcademicOrgDPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 55 | AcademicOrgDPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 56 | AcademicOrgDPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 57 | AcademicOrgDPEOCampusId | CAMPUS_ID | — | — |
| 58 | AcademicOrgDPEOCreatedBy | CREATED_BY | — | — |
| 59 | AcademicOrgDPEOCreationDate | CREATION_DATE | — | — |
| 60 | AcademicOrgDPEODescription | DESCRIPTION | — | — |
| 61 | AcademicOrgDPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 62 | AcademicOrgDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 63 | AcademicOrgDPEOInstitutionId | INSTITUTION_ID | — | — |
| 64 | AcademicOrgDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 65 | AcademicOrgDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 66 | AcademicOrgDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 67 | AcademicOrgDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | AcademicOrgDPEOStorefrontOptionCode | STOREFRONT_OPTION_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
