---
id: DOC-PO-PVO-SearchActionDetailPVO
doc_type: system-doc
title: "SearchActionDetailPVO — PVO Purchasing"
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
  - SearchActionDetailPVO
  - searchactiondetailpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SearchActionDetailPVO

## 📌 Visão Geral

Extrai detalhes granulares de ações tomadas após buscas no sistema de recrutamento, com timestamps e contexto da interação. Permite análise de jornada do usuário e otimização do processo.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecSourcingCoreAM.SearchActionDetailPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 6 | 2 | 9 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[irc_candidates|IRC_CANDIDATES]] — 3 atributos (1 BICC)
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 2 atributos (1 BICC)
- [[irc_requisitions_tl|IRC_REQUISITIONS_TL]] — 3 atributos (1 BICC)
- [[irc_search_actions|IRC_SEARCH_ACTIONS]] — 11 atributos (1 PKs, 2 BICC)
- [[irc_search_action_details|IRC_SEARCH_ACTION_DETAILS]] — 11 atributos (1 PKs, 3 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (1 BICC)

---

## ⚙️ Atributos

### [[irc_candidates|IRC_CANDIDATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CandidatePEOCandidateNumber | CANDIDATE_NUMBER | — | ✅ |
| 2 | CandidatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | CandidatePEOPersonId | PERSON_ID | — | — |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionBPEORequisitionId | REQUISITION_ID | — | — |
| 2 | RequisitionBPEORequisitionNumber | REQUISITION_NUMBER | — | ✅ |

### [[irc_requisitions_tl|IRC_REQUISITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | RequisitionTranslationPEORequisitionId | REQUISITION_ID | — | — |
| 3 | RequisitionTranslationPEOTitle | TITLE | — | ✅ |

### [[irc_search_actions|IRC_SEARCH_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionId | ACTION_ID | 🔑 | ✅ |
| 2 | SearchActionPEOAction | ACTION | — | ✅ |
| 3 | SearchActionPEOCreatedBy | CREATED_BY | — | — |
| 4 | SearchActionPEOCreationDate | CREATION_DATE | — | — |
| 5 | SearchActionPEOEntityIds | ENTITY_IDS | — | — |
| 6 | SearchActionPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | SearchActionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | SearchActionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | SearchActionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | SearchActionPEOSearchId | SEARCH_ID | — | — |
| 11 | SearchActionPEOSelectedCandidates | SELECTED_CANDIDATES | — | — |

### [[irc_search_action_details|IRC_SEARCH_ACTION_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionDetailId | ACTION_DETAIL_ID | 🔑 | ✅ |
| 2 | SearchActionDetailPEOActionId | ACTION_ID | — | — |
| 3 | SearchActionDetailPEOCreatedBy | CREATED_BY | — | — |
| 4 | SearchActionDetailPEOCreationDate | CREATION_DATE | — | — |
| 5 | SearchActionDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | SearchActionDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | SearchActionDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | SearchActionDetailPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SearchActionDetailPEOSearchId | SEARCH_ID | — | — |
| 10 | SearchActionDetailPEOSelectedEntityId | SELECTED_ENTITY_ID | — | ✅ |
| 11 | SearchActionDetailPEOTargetEntityId | TARGET_ENTITY_ID | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonNamePEOFullName | FULL_NAME | — | ✅ |
| 4 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
