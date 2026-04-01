---
id: DOC-OTHER-PVO-PSCAssesmentDetailPVO
doc_type: system-doc
title: "PSCAssesmentDetailPVO — PVO Cross-Module"
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
  - PSCAssesmentDetailPVO
  - pscassesmentdetailpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCAssesmentDetailPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCAssesment Detail. Acessa as tabelas: PSC_INS_ASSESSMENT_DTL_B, PSC_INS_ASSESSMENT_DTL_TL.

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCAssesmentDetailPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 2 | 3 | 6 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[psc_ins_assessment_dtl_b|PSC_INS_ASSESSMENT_DTL_B]] — 16 atributos (3 PKs, 5 BICC)
- [[psc_ins_assessment_dtl_tl|PSC_INS_ASSESSMENT_DTL_TL]] — 12 atributos (1 BICC)

---

## ⚙️ Atributos

### [[psc_ins_assessment_dtl_b|PSC_INS_ASSESSMENT_DTL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssesmentDetailPEOAgencyId | AGENCY_ID | 🔑 | ✅ |
| 2 | AssesmentDetailPEOAssessmentCode | ASSESSMENT_CODE | 🔑 | ✅ |
| 3 | AssesmentDetailPEOAssessmentType | ASSESSMENT_TYPE | 🔑 | ✅ |
| 4 | AssesmentDetailPEOCreatedBy | CREATED_BY | — | — |
| 5 | AssesmentDetailPEOCreationDate | CREATION_DATE | — | — |
| 6 | AssesmentDetailPEOCustom1 | CUSTOM1 | — | — |
| 7 | AssesmentDetailPEOCustom2 | CUSTOM2 | — | — |
| 8 | AssesmentDetailPEOCustom3 | CUSTOM3 | — | — |
| 9 | AssesmentDetailPEOCustom4 | CUSTOM4 | — | — |
| 10 | AssesmentDetailPEOCustom5 | CUSTOM5 | — | — |
| 11 | AssesmentDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | AssesmentDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | AssesmentDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | AssesmentDetailPEOModuleId | MODULE_ID | — | — |
| 15 | AssesmentDetailPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | AssesmentDetailPEOSystemResult | SYSTEM_RESULT | — | ✅ |

### [[psc_ins_assessment_dtl_tl|PSC_INS_ASSESSMENT_DTL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssesmentDetailTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | AssesmentDetailTLPEOAssessmentCode | ASSESSMENT_CODE | — | — |
| 3 | AssesmentDetailTLPEOAssessmentType | ASSESSMENT_TYPE | — | — |
| 4 | AssesmentDetailTLPEOCreatedBy | CREATED_BY | — | — |
| 5 | AssesmentDetailTLPEOCreationDate | CREATION_DATE | — | — |
| 6 | AssesmentDetailTLPEODescription | DESCRIPTION | — | ✅ |
| 7 | AssesmentDetailTLPEOLanguage | LANGUAGE | — | — |
| 8 | AssesmentDetailTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | AssesmentDetailTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | AssesmentDetailTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | AssesmentDetailTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | AssesmentDetailTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
