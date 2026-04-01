---
id: DOC-OTHER-PVO-RiskIssueXrefPVO
doc_type: system-doc
title: "RiskIssueXrefPVO — PVO Cross-Module"
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
  - RiskIssueXrefPVO
  - riskissuexrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RiskIssueXrefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Risk Issue Xref. Acessa as tabelas: GRC_ISSU_RISK_XREF.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.RiskIssueXrefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 2 | 4 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[grc_issu_risk_xref|GRC_ISSU_RISK_XREF]] — 16 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[grc_issu_risk_xref|GRC_ISSU_RISK_XREF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueRiskXrefPEOAssessmentResultId | ASSESSMENT_RESULT_ID | — | ✅ |
| 2 | IssueRiskXrefPEOChildObjectTypeId | CHILD_OBJECT_TYPE_ID | — | — |
| 3 | IssueRiskXrefPEOCreatedBy | CREATED_BY | — | — |
| 4 | IssueRiskXrefPEOCreationDate | CREATION_DATE | — | — |
| 5 | IssueRiskXrefPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 6 | IssueRiskXrefPEOIssueId | ISSUE_ID | 🔑 | ✅ |
| 7 | IssueRiskXrefPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | IssueRiskXrefPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | IssueRiskXrefPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | IssueRiskXrefPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | IssueRiskXrefPEORevisionDate | REVISION_DATE | — | — |
| 12 | IssueRiskXrefPEORevisionNumber | REVISION_NUMBER | — | — |
| 13 | IssueRiskXrefPEORiskAnalysisId | RISK_ANALYSIS_ID | — | — |
| 14 | IssueRiskXrefPEORiskEvaluationId | RISK_EVALUATION_ID | — | — |
| 15 | IssueRiskXrefPEORiskId | RISK_ID | 🔑 | ✅ |
| 16 | IssueRiskXrefPEOTreatmentId | TREATMENT_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
