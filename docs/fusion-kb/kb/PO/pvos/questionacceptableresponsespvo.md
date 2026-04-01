---
id: DOC-PO-PVO-QuestionAcceptableResponsesPVO
doc_type: system-doc
title: "QuestionAcceptableResponsesPVO — PVO Purchasing"
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
  - QuestionAcceptableResponsesPVO
  - questionacceptableresponsespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionAcceptableResponsesPVO

## 📌 Visão Geral

Extrai as respostas aceitáveis para cada pergunta de qualificação, definindo critérios de aprovação automática. Permite análise de rigor e consistência dos processos de avaliação.

**Caminho:** `FscmTopModelAM.PrcPoqPublicViewAM.QuestionAcceptableResponsesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 2 | 1 | 54 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[poq_questions_vl|POQ_QUESTIONS_VL]] — 34 atributos (33 BICC)
- [[poq_ques_acc_responses_vl|POQ_QUES_ACC_RESPONSES_VL]] — 23 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[poq_questions_vl|POQ_QUESTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionActivationDate | ACTIVATION_DATE | — | ✅ |
| 2 | QuestionAllowRespCommentFlag | ALLOW_RESP_COMMENT_FLAG | — | ✅ |
| 3 | QuestionAttachmentAllowedCode | ATTACHMENT_ALLOWED_CODE | — | ✅ |
| 4 | QuestionCreatedBy | CREATED_BY | — | ✅ |
| 5 | QuestionCreationDate | CREATION_DATE | — | ✅ |
| 6 | QuestionCriticalQuestionFlag | CRITICAL_QUESTION_FLAG | — | ✅ |
| 7 | QuestionDisplayPreferredRespFlag | DISPLAY_PREFERRED_RESP_FLAG | — | ✅ |
| 8 | QuestionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | QuestionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | QuestionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | QuestionLatestRevisionFlag | LATEST_REVISION_FLAG | — | ✅ |
| 12 | QuestionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | QuestionOriginalQuestionId | ORIGINAL_QUESTION_ID | — | ✅ |
| 14 | QuestionOwnerId | OWNER_ID | — | ✅ |
| 15 | QuestionPreferredResponseDate | PREFERRED_RESPONSE_DATE | — | ✅ |
| 16 | QuestionPreferredResponseDatetime | PREFERRED_RESPONSE_DATETIME | — | ✅ |
| 17 | QuestionPreferredResponseNumber | PREFERRED_RESPONSE_NUMBER | — | ✅ |
| 18 | QuestionPreferredResponseText | PREFERRED_RESPONSE_TEXT | — | ✅ |
| 19 | QuestionQuestionHint | QUESTION_HINT | — | ✅ |
| 20 | QuestionQuestionId | QUESTION_ID | — | ✅ |
| 21 | QuestionQuestionLevel | QUESTION_LEVEL | — | ✅ |
| 22 | QuestionQuestionName | QUESTION_NAME | — | ✅ |
| 23 | QuestionQuestionStatus | QUESTION_STATUS | — | ✅ |
| 24 | QuestionQuestionText | QUESTION_TEXT | — | ✅ |
| 25 | QuestionQuestionType | QUESTION_TYPE | — | ✅ |
| 26 | QuestionResponderType | RESPONDER_TYPE | — | ✅ |
| 27 | QuestionResponseRequiredFlag | RESPONSE_REQUIRED_FLAG | — | ✅ |
| 28 | QuestionResponseType | RESPONSE_TYPE | — | ✅ |
| 29 | QuestionRevisionNumber | REVISION_NUMBER | — | ✅ |
| 30 | QuestionStdsOrgCode | STDS_ORG_CODE | — | ✅ |
| 31 | QuestionSubjectCode | SUBJECT_CODE | — | ✅ |
| 32 | QuestionSupplierAttributeCode | SUPPLIER_ATTRIBUTE_CODE | — | ✅ |
| 33 | QuestionSupplierAttributeFlag | SUPPLIER_ATTRIBUTE_FLAG | — | ✅ |
| 34 | QuestionUsageCode | QUESTION_USAGE_CODE | — | — |

### [[poq_ques_acc_responses_vl|POQ_QUES_ACC_RESPONSES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccResponseId | ACC_RESPONSE_ID | 🔑 | ✅ |
| 2 | CriticalResponseFlag | CRITICAL_RESPONSE_FLAG | — | — |
| 3 | ExcludeScoringFlag | EXCLUDE_SCORING_FLAG | — | — |
| 4 | QuestionAcceptableResponseAttachmentAllowedCode | ATTACHMENT_ALLOWED_CODE | — | ✅ |
| 5 | QuestionAcceptableResponseAttributeCode | ATTRIBUTE_CODE | — | ✅ |
| 6 | QuestionAcceptableResponseAttributeCode2 | ATTRIBUTE_CODE2 | — | ✅ |
| 7 | QuestionAcceptableResponseAttributeId | ATTRIBUTE_ID | — | ✅ |
| 8 | QuestionAcceptableResponseCategoryId | CATEGORY_ID | — | ✅ |
| 9 | QuestionAcceptableResponseCategoryName | CATEGORY_NAME | — | ✅ |
| 10 | QuestionAcceptableResponseCreatedBy | CREATED_BY | — | ✅ |
| 11 | QuestionAcceptableResponseCreationDate | CREATION_DATE | — | ✅ |
| 12 | QuestionAcceptableResponseDisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 13 | QuestionAcceptableResponseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | QuestionAcceptableResponseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | QuestionAcceptableResponseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | QuestionAcceptableResponseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | QuestionAcceptableResponseOriginalAccResponseId | ORIGINAL_ACC_RESPONSE_ID | — | ✅ |
| 18 | QuestionAcceptableResponseParentCategoryId | PARENT_CATEGORY_ID | — | ✅ |
| 19 | QuestionAcceptableResponsePreferredResponseFlag | PREFERRED_RESPONSE_FLAG | — | ✅ |
| 20 | QuestionAcceptableResponsePurchasingCatFlag | PURCHASING_CAT_FLAG | — | ✅ |
| 21 | QuestionAcceptableResponseQuestionId | QUESTION_ID | — | ✅ |
| 22 | QuestionAcceptableResponseResponseText | RESPONSE_TEXT | — | ✅ |
| 23 | QuestionAcceptableResponseScore | SCORE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
