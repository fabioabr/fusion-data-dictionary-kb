---
id: DOC-OTHER-PVO-QuestionnairePVO
doc_type: system-doc
title: "QuestionnairePVO — PVO Cross-Module"
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
  - QuestionnairePVO
  - questionnairepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnairePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Questionnaire. Acessa as tabelas: HRQ_QUESTIONNAIRES_B, HRQ_QUESTIONNAIRES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.QuestionnaireLibraryAM.QuestionnairePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 41 | 2 | 3 | 8 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_questionnaires_b|HRQ_QUESTIONNAIRES_B]] — 26 atributos (3 PKs, 6 BICC)
- [[hrq_questionnaires_tl|HRQ_QUESTIONNAIRES_TL]] — 15 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hrq_questionnaires_b|HRQ_QUESTIONNAIRES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CategoryId | CATEGORY_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | — |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | InUse | IN_USE | — | — |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | LatestVersion | LATEST_VERSION | — | — |
| 10 | ModuleId | MODULE_ID | — | — |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | Owner | OWNER | — | — |
| 13 | PageLayout | PAGE_LAYOUT | — | — |
| 14 | PrivacyFlag | PRIVACY_FLAG | — | — |
| 15 | QstnrTemplateId | QSTNR_TEMPLATE_ID | — | — |
| 16 | QstnrVersionNum | QSTNR_VERSION_NUM | 🔑 | ✅ |
| 17 | QstnsPerPage | QSTNS_PER_PAGE | — | — |
| 18 | QuestionnaireCode | QUESTIONNAIRE_CODE | — | ✅ |
| 19 | QuestionnaireId | QUESTIONNAIRE_ID | 🔑 | ✅ |
| 20 | SectionOrder | SECTION_ORDER | — | — |
| 21 | SectionPresentation | SECTION_PRESENTATION | — | — |
| 22 | Status | STATUS | — | — |
| 23 | SubscriberId | SUBSCRIBER_ID | — | — |
| 24 | TemplateFlag | TEMPLATE_FLAG | — | — |
| 25 | UpdateAllowed | UPDATE_ALLOWED | — | — |
| 26 | VersionDescription | VERSION_DESCRIPTION | — | — |

### [[hrq_questionnaires_tl|HRQ_QUESTIONNAIRES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | CreatedBy1 | CREATED_BY | — | — |
| 3 | CreationDate1 | CREATION_DATE | — | — |
| 4 | Description | DESCRIPTION | — | — |
| 5 | IntroText | INTRO_TEXT | — | — |
| 6 | Keywords | KEYWORDS | — | — |
| 7 | Language1 | LANGUAGE | — | — |
| 8 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 11 | Name | NAME | — | ✅ |
| 12 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 13 | QstnrVersionNum1 | QSTNR_VERSION_NUM | — | — |
| 14 | QuestionnaireId1 | QUESTIONNAIRE_ID | — | — |
| 15 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
