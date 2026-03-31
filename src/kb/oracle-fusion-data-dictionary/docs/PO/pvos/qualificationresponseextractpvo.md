---
id: DOC-PO-PVO-QualificationResponseExtractPVO
doc_type: system-doc
title: "QualificationResponseExtractPVO — PVO Purchasing"
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
  - QualificationResponseExtractPVO
  - qualificationresponseextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualificationResponseExtractPVO

## 📌 Visão Geral

Extrai as respostas de fornecedores a processos de qualificação para carga BICC, incluindo áreas respondidas e status. Alimenta análises de aderência e completude.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.QualificationResponseExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_qual_responses|POQ_QUAL_RESPONSES]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[poq_qual_responses|POQ_QUAL_RESPONSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | QualResponseId | QUAL_RESPONSE_ID | 🔑 | ✅ |
| 8 | QualificationId | QUALIFICATION_ID | — | ✅ |
| 9 | QuestionId | QUESTION_ID | — | ✅ |
| 10 | QuestionRespNotes | QUESTION_RESP_NOTES | — | ✅ |
| 11 | QuestionRespScore | QUESTION_RESP_SCORE | — | ✅ |
| 12 | ReassignedWeight | REASSIGNED_WEIGHT | — | ✅ |
| 13 | ResponseRepositoryId | RESPONSE_REPOSITORY_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
