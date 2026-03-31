---
id: DOC-HCM-PVO-QuestionnaireAnswerPVO
doc_type: system-doc
title: "QuestionnaireAnswerPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - QuestionnaireAnswerPVO
  - questionnaireanswerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireAnswerPVO

## 📌 Visão Geral

Extrai respostas vinculadas a questionários específicos. Permite rastrear vínculos entre respostas individuais e instrumentos de pesquisa no HCM.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.QuestionnaireLibraryAM.QuestionnaireAnswerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_qstnr_answers|HRQ_QSTNR_ANSWERS]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[hrq_qstnr_answers|HRQ_QSTNR_ANSWERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnaireAnswerPEOAnswerId | ANSWER_ID | — | ✅ |
| 2 | QuestionnaireAnswerPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | QuestionnaireAnswerPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | QuestionnaireAnswerPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | QuestionnaireAnswerPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | QuestionnaireAnswerPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | QuestionnaireAnswerPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | QuestionnaireAnswerPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | QuestionnaireAnswerPEOQstnrAnswerId | QSTNR_ANSWER_ID | 🔑 | ✅ |
| 10 | QuestionnaireAnswerPEOQstnrQuestionId | QSTNR_QUESTION_ID | — | ✅ |
| 11 | QuestionnaireAnswerPEORatingLevelId | RATING_LEVEL_ID | — | ✅ |
| 12 | QuestionnaireAnswerPEOScore | SCORE | — | ✅ |
| 13 | QuestionnaireAnswerPEOSubQuestionId | SUB_QUESTION_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
