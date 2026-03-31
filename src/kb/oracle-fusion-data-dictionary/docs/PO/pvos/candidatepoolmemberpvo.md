---
id: DOC-PO-PVO-CandidatePoolMemberPVO
doc_type: system-doc
title: "CandidatePoolMemberPVO — PVO Purchasing"
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
  - CandidatePoolMemberPVO
  - candidatepoolmemberpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CandidatePoolMemberPVO

## 📌 Visão Geral

Extrai os membros de pools de candidatos, incluindo perfil, qualificações e status de participação. Permite gestão de banco de talentos para contratação de serviços e sourcing de mão de obra.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecSourcingCandPoolsAM.CandidatePoolMemberPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 41 | 9 | 1 | 21 | 51% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_pools_vl|HRT_POOLS_VL]] — 1 atributos
- [[hrt_pool_members|HRT_POOL_MEMBERS]] — 5 atributos
- [[irc_cand_pool_members|IRC_CAND_POOL_MEMBERS]] — 14 atributos (1 PKs, 7 BICC)
- [[irc_cand_profile_usages_m|IRC_CAND_PROFILE_USAGES_M]] — 6 atributos (1 BICC)
- [[irc_phases_b|IRC_PHASES_B]] — 4 atributos (4 BICC)
- [[irc_phases_tl|IRC_PHASES_TL]] — 3 atributos (3 BICC)
- [[irc_poolmem_last_interaction_v|IRC_POOLMEM_LAST_INTERACTION_V]] — 2 atributos
- [[irc_states_b|IRC_STATES_B]] — 3 atributos (3 BICC)
- [[irc_states_tl|IRC_STATES_TL]] — 3 atributos (3 BICC)

---

## ⚙️ Atributos

### [[hrt_pools_vl|HRT_POOLS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoolId1 | POOL_ID | — | — |

### [[hrt_pool_members|HRT_POOL_MEMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EnterpriseId | ENTERPRISE_ID | — | — |
| 2 | EnterpriseId1 | ENTERPRISE_ID | — | — |
| 3 | MemberId | MEMBER_ID | — | — |
| 4 | PoolMemberId1 | POOL_MEMBER_ID | — | — |
| 5 | Status | STATUS | — | — |

### [[irc_cand_pool_members|IRC_CAND_POOL_MEMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CandPoolMemberPEOProcessInstanceId | PROCESS_INSTANCE_ID | — | — |
| 2 | CandPoolMemberPEOProcessTemplateId | PROCESS_TEMPLATE_ID | — | — |
| 3 | CreatedBy | CREATED_BY | — | — |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | CurrentPhaseId | CURRENT_PHASE_ID | — | ✅ |
| 6 | CurrentStateId | CURRENT_STATE_ID | — | ✅ |
| 7 | LastAddToReqDate | LAST_ADD_TO_REQ_DATE | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | LastUpdatedByPersonId | LAST_UPDATED_BY_PERSON_ID | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | PoolId | POOL_ID | — | ✅ |
| 14 | PoolMemberId | POOL_MEMBER_ID | 🔑 | ✅ |

### [[irc_cand_profile_usages_m|IRC_CAND_PROFILE_USAGES_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CandProfileUsageId | CAND_PROFILE_USAGE_ID | — | — |
| 2 | CandProfileUsgsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | CandProfileUsgsPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 4 | CandProfileUsgsPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | CandProfileUsgsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | CandProfileUsgsPEOProfileId | PROFILE_ID | — | — |

### [[irc_phases_b|IRC_PHASES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Code | CODE | — | ✅ |
| 2 | PhaseBPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 3 | PhaseId | PHASE_ID | — | ✅ |
| 4 | TypeCode | TYPE_CODE | — | ✅ |

### [[irc_phases_tl|IRC_PHASES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | — | ✅ |
| 2 | Name | NAME | — | ✅ |
| 3 | PhaseId1 | PHASE_ID | — | ✅ |

### [[irc_poolmem_last_interaction_v|IRC_POOLMEM_LAST_INTERACTION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CandPoolMemLastInteractionPEOInteractionDate | INTERACTION_DATE | — | — |
| 2 | CandPoolMemLastInteractionPEOInteractionId | INTERACTION_ID | — | — |

### [[irc_states_b|IRC_STATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Code1 | CODE | — | ✅ |
| 2 | StateId | STATE_ID | — | ✅ |
| 3 | TypeCode1 | TYPE_CODE | — | ✅ |

### [[irc_states_tl|IRC_STATES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language1 | LANGUAGE | — | ✅ |
| 2 | Name1 | NAME | — | ✅ |
| 3 | StateId1 | STATE_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
