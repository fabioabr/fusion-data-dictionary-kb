---
id: DOC-OTHER-PVO-QuestionnaireQuestionSubscriberPVO
doc_type: system-doc
title: "QuestionnaireQuestionSubscriberPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - QuestionnaireQuestionSubscriberPVO
  - questionnairequestionsubscriberpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireQuestionSubscriberPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Questionnaire Question Subscriber. Acessa as tabelas: HRQ_SUBSCRIBERS_B, HRQ_SUBSCRIBERS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.QuestionnaireAM.QuestionnaireQuestionSubscriberPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 2 | 5 | 8 | 89% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_subscribers_b|HRQ_SUBSCRIBERS_B]] — 4 atributos (2 PKs, 3 BICC)
- [[hrq_subscribers_tl|HRQ_SUBSCRIBERS_TL]] — 5 atributos (3 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[hrq_subscribers_b|HRQ_SUBSCRIBERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubscriberBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | SubscriberBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | SubscriberBPEOSubscriberCode | SUBSCRIBER_CODE | — | — |
| 4 | SubscriberBPEOSubscriberId | SUBSCRIBER_ID | 🔑 | ✅ |

### [[hrq_subscribers_tl|HRQ_SUBSCRIBERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubscriberTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | SubscriberTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 3 | SubscriberTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | SubscriberTranslationPEOName | NAME | — | ✅ |
| 5 | SubscriberTranslationPEOSubscriberId | SUBSCRIBER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
