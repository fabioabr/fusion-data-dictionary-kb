---
id: DOC-OTHER-PVO-QaResultEvaluationsExtractPVO
doc_type: system-doc
title: "QaResultEvaluationsExtractPVO — PVO Cross-Module"
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
  - QaResultEvaluationsExtractPVO
  - qaresultevaluationsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QaResultEvaluationsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Qa Result Evaluations Extract. Acessa as tabelas: QA_RESULT_EVALUATIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.QaResultEvaluationsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[qa_result_evaluations|QA_RESULT_EVALUATIONS]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[qa_result_evaluations|QA_RESULT_EVALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QaResultEvaluationsPEOAdditionalCharFlag | ADDITIONAL_CHAR_FLAG | — | ✅ |
| 2 | QaResultEvaluationsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | QaResultEvaluationsPEOEvaluationFlag | EVALUATION_FLAG | — | ✅ |
| 4 | QaResultEvaluationsPEOInSpecFlag | IN_SPEC_FLAG | — | ✅ |
| 5 | QaResultEvaluationsPEOIpEventDispositionId | IP_EVENT_DISPOSITION_ID | — | ✅ |
| 6 | QaResultEvaluationsPEOIpEventId | IP_EVENT_ID | — | ✅ |
| 7 | QaResultEvaluationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | QaResultEvaluationsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | QaResultEvaluationsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | QaResultEvaluationsPEOQaResultEvaluationsPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | QaResultEvaluationsPEOResultEvaluationId | RESULT_EVALUATION_ID | 🔑 | ✅ |
| 12 | QaResultEvaluationsPEOSampleResultId | SAMPLE_RESULT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
