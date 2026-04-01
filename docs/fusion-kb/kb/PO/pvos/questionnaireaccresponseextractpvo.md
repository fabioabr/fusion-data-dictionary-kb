---
id: DOC-PO-PVO-QuestionnaireAccResponseExtractPVO
doc_type: system-doc
title: "QuestionnaireAccResponseExtractPVO — PVO Purchasing"
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
  - QuestionnaireAccResponseExtractPVO
  - questionnaireaccresponseextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireAccResponseExtractPVO

## 📌 Visão Geral

Extrai respostas aceitáveis de questionários para carga BICC, definindo critérios automáticos de aprovação por pergunta. Alimenta regras de scoring automatizado.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.QuestionnaireAccResponseExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_questnaire_acc_resps|POQ_QUESTNAIRE_ACC_RESPS]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[poq_questnaire_acc_resps|POQ_QUESTNAIRE_ACC_RESPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccResponseId | ACC_RESPONSE_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DisplayNumber | DISPLAY_NUMBER | — | ✅ |
| 5 | DisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | QuestionId | QUESTION_ID | — | ✅ |
| 11 | QuestnaireAccResponseId | QUESTNAIRE_ACC_RESPONSE_ID | 🔑 | ✅ |
| 12 | QuestnaireId | QUESTNAIRE_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
