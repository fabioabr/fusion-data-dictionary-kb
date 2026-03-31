---
id: DOC-PO-PVO-AssessmentQualificationExtractPVO
doc_type: system-doc
title: "AssessmentQualificationExtractPVO — PVO Purchasing"
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
  - AssessmentQualificationExtractPVO
  - assessmentqualificationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssessmentQualificationExtractPVO

## 📌 Visão Geral

Extrai o vínculo entre avaliações e qualificações de fornecedores para carga BICC. Alimenta análises de como resultados de assessments impactam o status de homologação.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.AssessmentQualificationExtractPVO`

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
| 1 | AssessmentId | ASSESSMENT_ID | — | ✅ |
| 2 | AssessmentQualId | ASSESSMENT_QUAL_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | EvaluationNote | EVALUATION_NOTE | — | ✅ |
| 6 | InitiativeId | INITIATIVE_ID | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | QualificationId | QUALIFICATION_ID | — | ✅ |
| 12 | ReusedFlag | REUSED_FLAG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
