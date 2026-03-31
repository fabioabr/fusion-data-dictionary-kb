---
id: DOC-PO-PVO-QuestionnaireResponseExtractPVO
doc_type: system-doc
title: "QuestionnaireResponseExtractPVO — PVO Purchasing"
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
  - QuestionnaireResponseExtractPVO
  - questionnaireresponseextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireResponseExtractPVO

## 📌 Visão Geral

Extrai respostas individuais a questionários de qualificação para carga BICC. Alimenta análises detalhadas de conformidade e desempenho por pergunta e fornecedor.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.QuestionnaireResponseExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_questnaire_responses|POQ_QUESTNAIRE_RESPONSES]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[poq_questnaire_responses|POQ_QUESTNAIRE_RESPONSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcceptanceNote | ACCEPTANCE_NOTE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | FailedPozValidationFlag | FAILED_POZ_VALIDATION_FLAG | — | ✅ |
| 5 | HasNewerResponseFlag | HAS_NEWER_RESPONSE_FLAG | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | QuestionDisplayedFlag | QUESTION_DISPLAYED_FLAG | — | ✅ |
| 11 | QuestionId | QUESTION_ID | — | ✅ |
| 12 | QuestnaireQuestionId | QUESTNAIRE_QUESTION_ID | — | ✅ |
| 13 | QuestnaireRespHeaderId | QUESTNAIRE_RESP_HEADER_ID | — | ✅ |
| 14 | QuestnaireRespSectionId | QUESTNAIRE_RESP_SECTION_ID | — | ✅ |
| 15 | QuestnaireResponseId | QUESTNAIRE_RESPONSE_ID | 🔑 | ✅ |
| 16 | ResponseComments | RESPONSE_COMMENTS | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
