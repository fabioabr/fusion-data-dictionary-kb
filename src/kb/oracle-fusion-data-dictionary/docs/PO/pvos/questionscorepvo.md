---
id: DOC-PO-PVO-QuestionScorePVO
doc_type: system-doc
title: "QuestionScorePVO — PVO Purchasing"
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
  - QuestionScorePVO
  - questionscorepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionScorePVO

## 📌 Visão Geral

Extrai as pontuações atribuídas a respostas de perguntas, definindo critérios de scoring para qualificação. Suporta calibração de modelos de avaliação e análise de consistência de notas.

**Caminho:** `FscmTopModelAM.PrcPoqPublicViewAM.QuestionScorePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 11 | 92% |

---

## 🔗 Tabelas Relacionadas

- [[poq_question_scores|POQ_QUESTION_SCORES]] — 12 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[poq_question_scores|POQ_QUESTION_SCORES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CriticalResponseFlag | CRITICAL_RESPONSE_FLAG | — | — |
| 2 | QuestionScoreCreatedBy | CREATED_BY | — | ✅ |
| 3 | QuestionScoreCreationDate | CREATION_DATE | — | ✅ |
| 4 | QuestionScoreFromResponseValue | FROM_RESPONSE_VALUE | — | ✅ |
| 5 | QuestionScoreLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | QuestionScoreLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | QuestionScoreLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | QuestionScoreObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | QuestionScoreQuestionId | QUESTION_ID | — | ✅ |
| 10 | QuestionScoreQuestionScoreId | QUESTION_SCORE_ID | 🔑 | ✅ |
| 11 | QuestionScoreScore | SCORE | — | ✅ |
| 12 | QuestionScoreToResponseValue | TO_RESPONSE_VALUE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
