---
id: DOC-PO-PVO-AssessmentQualPVO
doc_type: system-doc
title: "AssessmentQualPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - AssessmentQualPVO
  - assessmentqualpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssessmentQualPVO

## 📌 Visão Geral

Extrai a vinculação entre avaliações e qualificações de fornecedores, determinando como resultados de assessments influenciam o status de qualificação. Suporta processos de homologação e renovação.

**Caminho:** `FscmTopModelAM.PrcPoqPublicViewAM.AssessmentQualPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_assessment_quals|POQ_ASSESSMENT_QUALS]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[poq_assessment_quals|POQ_ASSESSMENT_QUALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentQualAssessmentId | ASSESSMENT_ID | — | ✅ |
| 2 | AssessmentQualAssessmentQualId | ASSESSMENT_QUAL_ID | 🔑 | ✅ |
| 3 | AssessmentQualCreatedBy | CREATED_BY | — | ✅ |
| 4 | AssessmentQualCreationDate | CREATION_DATE | — | ✅ |
| 5 | AssessmentQualEvaluationNote | EVALUATION_NOTE | — | ✅ |
| 6 | AssessmentQualInitiativeId | INITIATIVE_ID | — | ✅ |
| 7 | AssessmentQualLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AssessmentQualLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | AssessmentQualLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | AssessmentQualObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | AssessmentQualQualificationId | QUALIFICATION_ID | — | ✅ |
| 12 | AssessmentQualReusedFlag | REUSED_FLAG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
