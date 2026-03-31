---
id: DOC-HCM-PVO-QuestionnaireResponse
doc_type: system-doc
title: "QuestionnaireResponse — PVO Human Capital Management"
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
  - QuestionnaireResponse
  - questionnaireresponse
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireResponse

## 📌 Visão Geral

Extrai respostas a questionários para carga BICC, com tentativas e datas. Suporta extração analítica de resultados de pesquisas e avaliações organizacionais.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.QuestionnaireBiccExtractAM.QuestionnaireResponse`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 2 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_qstnr_responses|HRQ_QSTNR_RESPONSES]] — 15 atributos (2 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[hrq_qstnr_responses|HRQ_QSTNR_RESPONSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttemptNum | ATTEMPT_NUM | — | ✅ |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | LatestAttemptFlag | LATEST_ATTEMPT_FLAG | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | QstnrParticipantId | QSTNR_PARTICIPANT_ID | — | ✅ |
| 11 | QstnrResponseId | QSTNR_RESPONSE_ID | 🔑 | ✅ |
| 12 | QstnrVersionNum | QSTNR_VERSION_NUM | — | ✅ |
| 13 | Status | STATUS | — | ✅ |
| 14 | SubmittedDateTime | SUBMITTED_DATE_TIME | — | ✅ |
| 15 | TotalScore | TOTAL_SCORE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
