---
id: DOC-PO-PVO-QuestionnaireQuestionExtractPVO
doc_type: system-doc
title: "QuestionnaireQuestionExtractPVO — PVO Purchasing"
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
  - QuestionnaireQuestionExtractPVO
  - questionnairequestionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireQuestionExtractPVO

## 📌 Visão Geral

Extrai a vinculação entre questionários e perguntas para carga BICC, mapeando a composição de cada instrumento. Permite análise da abrangência e estrutura dos questionários.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.QuestionnaireQuestionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_questnaire_questions|POQ_QUESTNAIRE_QUESTIONS]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[poq_questnaire_questions|POQ_QUESTNAIRE_QUESTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BranchLevel | BRANCH_LEVEL | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DisplayNumber | DISPLAY_NUMBER | — | ✅ |
| 5 | DisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ParentAccResponseId | PARENT_ACC_RESPONSE_ID | — | ✅ |
| 11 | ParentQuestionId | PARENT_QUESTION_ID | — | ✅ |
| 12 | ParentQuestnaireQuestId | PARENT_QUESTNAIRE_QUEST_ID | — | ✅ |
| 13 | QuestionId | QUESTION_ID | — | ✅ |
| 14 | QuestnaireId | QUESTNAIRE_ID | — | ✅ |
| 15 | QuestnaireQuestionId | QUESTNAIRE_QUESTION_ID | 🔑 | ✅ |
| 16 | QuestnaireSectionId | QUESTNAIRE_SECTION_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
