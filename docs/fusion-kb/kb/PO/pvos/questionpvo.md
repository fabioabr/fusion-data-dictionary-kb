---
id: DOC-PO-PVO-QuestionPVO
doc_type: system-doc
title: "QuestionPVO — PVO Purchasing"
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
  - QuestionPVO
  - questionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionPVO

## 📌 Visão Geral

Extrai o banco de perguntas utilizadas em questionários de qualificação e sourcing, com texto, tipo e estrutura hierárquica. Permite análise de cobertura de critérios e padronização de avaliações.

**Caminho:** `FscmTopModelAM.PrcPoqPublicViewAM.QuestionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 81 | 2 | 5 | 78 | 96% |

---

## 🔗 Tabelas Relacionadas

- [[poq_questions_vl|POQ_QUESTIONS_VL]] — 78 atributos (2 PKs, 75 BICC)
- [[poq_question_structure_v|POQ_QUESTION_STRUCTURE_V]] — 3 atributos (3 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[poq_questions_vl|POQ_QUESTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChildQuestionActivationDate | ACTIVATION_DATE | — | ✅ |
| 2 | ChildQuestionAllowRespCommentFlag | ALLOW_RESP_COMMENT_FLAG | — | ✅ |
| 3 | ChildQuestionAttachmentAllowedCode | ATTACHMENT_ALLOWED_CODE | — | ✅ |
| 4 | ChildQuestionCreatedBy | CREATED_BY | — | ✅ |
| 5 | ChildQuestionCreationDate | CREATION_DATE | — | ✅ |
| 6 | ChildQuestionCreationSource | CREATION_SOURCE | — | — |
| 7 | ChildQuestionCriticalQuestionFlag | CRITICAL_QUESTION_FLAG | — | ✅ |
| 8 | ChildQuestionDisplayPreferredRespFlag | DISPLAY_PREFERRED_RESP_FLAG | — | ✅ |
| 9 | ChildQuestionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ChildQuestionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | ChildQuestionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ChildQuestionLatestRevisionFlag | LATEST_REVISION_FLAG | — | ✅ |
| 13 | ChildQuestionMaximumScore | MAXIMUM_SCORE | — | ✅ |
| 14 | ChildQuestionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | ChildQuestionOriginalQuestionId | ORIGINAL_QUESTION_ID | — | ✅ |
| 16 | ChildQuestionOwnerId | OWNER_ID | — | ✅ |
| 17 | ChildQuestionPreferredResponseDate | PREFERRED_RESPONSE_DATE | — | ✅ |
| 18 | ChildQuestionPreferredResponseDatetime | PREFERRED_RESPONSE_DATETIME | — | ✅ |
| 19 | ChildQuestionPreferredResponseNumber | PREFERRED_RESPONSE_NUMBER | — | ✅ |
| 20 | ChildQuestionPreferredResponseText | PREFERRED_RESPONSE_TEXT | — | ✅ |
| 21 | ChildQuestionQuestionHint | QUESTION_HINT | — | ✅ |
| 22 | ChildQuestionQuestionLevel | QUESTION_LEVEL | — | ✅ |
| 23 | ChildQuestionQuestionName | QUESTION_NAME | — | ✅ |
| 24 | ChildQuestionQuestionStatus | QUESTION_STATUS | — | ✅ |
| 25 | ChildQuestionQuestionText | QUESTION_TEXT | — | ✅ |
| 26 | ChildQuestionQuestionType | QUESTION_TYPE | — | ✅ |
| 27 | ChildQuestionResponderType | RESPONDER_TYPE | — | ✅ |
| 28 | ChildQuestionResponseRequiredFlag | RESPONSE_REQUIRED_FLAG | — | ✅ |
| 29 | ChildQuestionResponseType | RESPONSE_TYPE | — | ✅ |
| 30 | ChildQuestionRevisionNumber | REVISION_NUMBER | — | ✅ |
| 31 | ChildQuestionScoreForNoResponse | SCORE_FOR_NO_RESPONSE | — | ✅ |
| 32 | ChildQuestionScoringApproach | SCORING_APPROACH | — | ✅ |
| 33 | ChildQuestionScoringMethod | SCORING_METHOD | — | ✅ |
| 34 | ChildQuestionStdsOrgCode | STDS_ORG_CODE | — | ✅ |
| 35 | ChildQuestionSubjectCode | SUBJECT_CODE | — | ✅ |
| 36 | ChildQuestionSupplierAttributeCode | SUPPLIER_ATTRIBUTE_CODE | — | ✅ |
| 37 | ChildQuestionSupplierAttributeFlag | SUPPLIER_ATTRIBUTE_FLAG | — | ✅ |
| 38 | CreationSource | CREATION_SOURCE | — | — |
| 39 | QuestionActivationDate | ACTIVATION_DATE | — | ✅ |
| 40 | QuestionAllowRespCommentFlag | ALLOW_RESP_COMMENT_FLAG | — | ✅ |
| 41 | QuestionAttachmentAllowedCode | ATTACHMENT_ALLOWED_CODE | — | ✅ |
| 42 | QuestionCreatedBy | CREATED_BY | — | ✅ |
| 43 | QuestionCreationDate | CREATION_DATE | — | ✅ |
| 44 | QuestionCriticalQuestionFlag | CRITICAL_QUESTION_FLAG | — | ✅ |
| 45 | QuestionDisplayPreferredRespFlag | DISPLAY_PREFERRED_RESP_FLAG | — | ✅ |
| 46 | QuestionId | QUESTION_ID | 🔑 | ✅ |
| 47 | QuestionId1 | QUESTION_ID | 🔑 | ✅ |
| 48 | QuestionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | QuestionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 50 | QuestionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 51 | QuestionLatestRevisionFlag | LATEST_REVISION_FLAG | — | ✅ |
| 52 | QuestionMaximumScore | MAXIMUM_SCORE | — | ✅ |
| 53 | QuestionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 54 | QuestionOriginalQuestionId | ORIGINAL_QUESTION_ID | — | ✅ |
| 55 | QuestionOwnerId | OWNER_ID | — | ✅ |
| 56 | QuestionPreferredResponseDate | PREFERRED_RESPONSE_DATE | — | ✅ |
| 57 | QuestionPreferredResponseDatetime | PREFERRED_RESPONSE_DATETIME | — | ✅ |
| 58 | QuestionPreferredResponseNumber | PREFERRED_RESPONSE_NUMBER | — | ✅ |
| 59 | QuestionPreferredResponseText | PREFERRED_RESPONSE_TEXT | — | ✅ |
| 60 | QuestionQuestionHint | QUESTION_HINT | — | ✅ |
| 61 | QuestionQuestionLevel | QUESTION_LEVEL | — | ✅ |
| 62 | QuestionQuestionName | QUESTION_NAME | — | ✅ |
| 63 | QuestionQuestionStatus | QUESTION_STATUS | — | ✅ |
| 64 | QuestionQuestionText | QUESTION_TEXT | — | ✅ |
| 65 | QuestionQuestionType | QUESTION_TYPE | — | ✅ |
| 66 | QuestionResponderType | RESPONDER_TYPE | — | ✅ |
| 67 | QuestionResponseRequiredFlag | RESPONSE_REQUIRED_FLAG | — | ✅ |
| 68 | QuestionResponseType | RESPONSE_TYPE | — | ✅ |
| 69 | QuestionRevisionNumber | REVISION_NUMBER | — | ✅ |
| 70 | QuestionScoreForNoResponse | SCORE_FOR_NO_RESPONSE | — | ✅ |
| 71 | QuestionScoringApproach | SCORING_APPROACH | — | ✅ |
| 72 | QuestionScoringMethod | SCORING_METHOD | — | ✅ |
| 73 | QuestionStdsOrgCode | STDS_ORG_CODE | — | ✅ |
| 74 | QuestionSubjectCode | SUBJECT_CODE | — | ✅ |
| 75 | QuestionSupplierAttributeCode | SUPPLIER_ATTRIBUTE_CODE | — | ✅ |
| 76 | QuestionSupplierAttributeFlag | SUPPLIER_ATTRIBUTE_FLAG | — | ✅ |
| 77 | QuestionSurveyFlag | QUESTION_SURVEY_FLAG | — | ✅ |
| 78 | QuestionUsageCode | QUESTION_USAGE_CODE | — | — |

### [[poq_question_structure_v|POQ_QUESTION_STRUCTURE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BranchLevel | BRANCH_LEVEL | 🔑 | ✅ |
| 2 | QuestionStructureQuestionId | QUESTION_ID | 🔑 | ✅ |
| 3 | QuestionStructureRootQuestionId | ROOT_QUESTION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
