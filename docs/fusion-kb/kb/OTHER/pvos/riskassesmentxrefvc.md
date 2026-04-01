---
id: DOC-OTHER-PVO-RiskAssesmentXrefVC
doc_type: system-doc
title: "RiskAssesmentXrefVC — PVO Cross-Module"
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
  - RiskAssesmentXrefVC
  - riskassesmentxrefvc
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RiskAssesmentXrefVC

## 📌 Visão Geral

View Object para extração BICC de dados de Risk Assesment Xref VC. Acessa as tabelas: GRC_ASMT_ASSESSMENT_B, GRC_ASMT_BUSENTITY, GTG_SC_FRC_ACCESS_V.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.RiskAssesmentXrefVC`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 3 | 2 | 4 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[grc_asmt_assessment_b|GRC_ASMT_ASSESSMENT_B]] — 2 atributos
- [[grc_asmt_busentity|GRC_ASMT_BUSENTITY]] — 11 atributos (2 PKs, 4 BICC)
- [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]] — 3 atributos

---

## ⚙️ Atributos

### [[grc_asmt_assessment_b|GRC_ASMT_ASSESSMENT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentBasePEOAssessmentId | ASSESSMENT_ID | — | — |
| 2 | AssessmentBasePEOStateCode | STATE_CODE | — | — |

### [[grc_asmt_busentity|GRC_ASMT_BUSENTITY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentXrefPEOAssessmentId | ASSESSMENT_ID | 🔑 | ✅ |
| 2 | AssessmentXrefPEOBusEntityId | BUS_ENTITY_ID | 🔑 | ✅ |
| 3 | AssessmentXrefPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AssessmentXrefPEOCreationDate | CREATION_DATE | — | — |
| 5 | AssessmentXrefPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 6 | AssessmentXrefPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AssessmentXrefPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AssessmentXrefPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AssessmentXrefPEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 10 | AssessmentXrefPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | AssessmentXrefPEOPerspItemId | PERSPECTIVE_ITEM_ID | — | — |

### [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FRCSecurityPEOSecurableId | SECURABLE_ID | — | — |
| 2 | FRCSecurityPEOSecurableType | SECURABLE_TYPE | — | — |
| 3 | FRCSecurityPEOUserId | USER_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
