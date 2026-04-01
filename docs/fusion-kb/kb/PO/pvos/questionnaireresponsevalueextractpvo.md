---
id: DOC-PO-PVO-QuestionnaireResponseValueExtractPVO
doc_type: system-doc
title: "QuestionnaireResponseValueExtractPVO — PVO Purchasing"
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
  - QuestionnaireResponseValueExtractPVO
  - questionnaireresponsevalueextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireResponseValueExtractPVO

## 📌 Visão Geral

Extrai os valores específicos de cada resposta de questionário para carga BICC, com tipo de dado e pergunta associada. Permite scoring automatizado e análise quantitativa.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.QuestionnaireResponseValueExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_questnaire_resp_values|POQ_QUESTNAIRE_RESP_VALUES]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[poq_questnaire_resp_values|POQ_QUESTNAIRE_RESP_VALUES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccResponseId | ACC_RESPONSE_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | IsSelectedFlag | IS_SELECTED_FLAG | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | QuestnaireAccResponseId | QUESTNAIRE_ACC_RESPONSE_ID | — | ✅ |
| 10 | QuestnaireRespValueId | QUESTNAIRE_RESP_VALUE_ID | 🔑 | ✅ |
| 11 | QuestnaireResponseId | QUESTNAIRE_RESPONSE_ID | — | ✅ |
| 12 | ResponseValidate | RESPONSE_VALIDATE | — | ✅ |
| 13 | ResponseValueDate | RESPONSE_VALUE_DATE | — | ✅ |
| 14 | ResponseValueDatetime | RESPONSE_VALUE_DATETIME | — | ✅ |
| 15 | ResponseValueNum | RESPONSE_VALUE_NUM | — | ✅ |
| 16 | ResponseValueTxt | RESPONSE_VALUE_TXT | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
