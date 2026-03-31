---
id: DOC-HCM-PVO-SourceTrackingViewAllPVO
doc_type: system-doc
title: "SourceTrackingViewAllPVO — PVO Human Capital Management"
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
  - SourceTrackingViewAllPVO
  - sourcetrackingviewallpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourceTrackingViewAllPVO

## 📌 Visão Geral

Disponibiliza rastreamento completo de fontes de recrutamento sem restrição de segurança. Integra dados de campanhas, pools e requisições para análise de sourcing.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecSrcTrackingAM.SourceTrackingViewAllPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 73 | 11 | 1 | 40 | 55% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_pools_vl|HRT_POOLS_VL]] — 3 atributos (1 BICC)
- [[hrt_pool_members|HRT_POOL_MEMBERS]] — 2 atributos
- [[irc_agent_requisitions|IRC_AGENT_REQUISITIONS]] — 4 atributos (2 BICC)
- [[irc_campaigns_b|IRC_CAMPAIGNS_B]] — 1 atributos
- [[irc_campaigns_tl|IRC_CAMPAIGNS_TL]] — 3 atributos (1 BICC)
- [[irc_candidates|IRC_CANDIDATES]] — 3 atributos (1 BICC)
- [[irc_dimension_def_b|IRC_DIMENSION_DEF_B]] — 15 atributos (6 BICC)
- [[irc_dimension_def_tl|IRC_DIMENSION_DEF_TL]] — 7 atributos (2 BICC)
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 4 atributos (2 BICC)
- [[irc_requisitions_tl|IRC_REQUISITIONS_TL]] — 3 atributos (1 BICC)
- [[irc_source_tracking|IRC_SOURCE_TRACKING]] — 28 atributos (1 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[hrt_pools_vl|HRT_POOLS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EnterpriseId | ENTERPRISE_ID | — | — |
| 2 | FromPoolPEOPoolId | POOL_ID | — | — |
| 3 | FromPoolPEOPoolName | POOL_NAME | — | ✅ |

### [[hrt_pool_members|HRT_POOL_MEMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoolMemberPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 2 | PoolMemberPEOPoolMemberId | POOL_MEMBER_ID | — | — |

### [[irc_agent_requisitions|IRC_AGENT_REQUISITIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobRequisitionAgentPEOAgentRequisitionId | AGENT_REQUISITION_ID | — | — |
| 2 | JobRequisitionAgentPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | JobRequisitionAgentPEOInvitedFlag | INVITED_FLAG | — | — |
| 4 | JobRequisitionAgentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[irc_campaigns_b|IRC_CAMPAIGNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampaignBPEOCampaignId | CAMPAIGN_ID | — | — |

### [[irc_campaigns_tl|IRC_CAMPAIGNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampaignTranslationPEOCampaignId | CAMPAIGN_ID | — | — |
| 2 | CampaignTranslationPEOCampaignName | CAMPAIGN_NAME | — | ✅ |
| 3 | CampaignTranslationPEOLanguage | LANGUAGE | — | — |

### [[irc_candidates|IRC_CANDIDATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CandidatePEOCandidateNumber | CANDIDATE_NUMBER | — | ✅ |
| 2 | CandidatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | CandidatePEOPersonId | PERSON_ID | — | — |

### [[irc_dimension_def_b|IRC_DIMENSION_DEF_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParentSourceDimensionBPEODimensionId | DIMENSION_ID | — | — |
| 2 | SourceDimensionBPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | SourceDimensionBPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | SourceDimensionBPEODimensionId | DIMENSION_ID | — | — |
| 5 | SourceDimensionBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SourceDimensionBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | SourceDimensionBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | SourceDimensionBPEOModuleId | MODULE_ID | — | — |
| 9 | SourceDimensionBPEOPriority | PRIORITY | — | — |
| 10 | SourceDimensionBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 11 | SourceDimensionBPEOSequence | SEQUENCE | — | — |
| 12 | SourceDimensionBPEOSourceMedium | SOURCE_MEDIUM | — | ✅ |
| 13 | SourceDimensionBPEOSourceMediumUrlValue | SOURCE_MEDIUM_URL_VALUE | — | — |
| 14 | SourceDimensionBPEOSourceUrlValue | SOURCE_URL_VALUE | — | — |
| 15 | SourceDimensionBPEOUrlHeaderRegex | URL_HEADER_REGEX | — | — |

### [[irc_dimension_def_tl|IRC_DIMENSION_DEF_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParentSourceDimensionTLPEODimensionId | DIMENSION_ID | — | — |
| 2 | ParentSourceDimensionTLPEOLanguage | LANGUAGE | — | — |
| 3 | ParentSourceDimensionTLPEOSourceName | SOURCE_NAME | — | ✅ |
| 4 | SourceDimensionTLPEODimensionId | DIMENSION_ID | — | — |
| 5 | SourceDimensionTLPEOLanguage | LANGUAGE | — | — |
| 6 | SourceDimensionTLPEOSourceName | SOURCE_NAME | — | ✅ |
| 7 | SourceDisplayName | SOURCE_DISPLAY_NAME | — | — |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FromRequisitionBPEORequisitionId | REQUISITION_ID | — | — |
| 2 | FromRequisitionBPEORequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 3 | RequisitionBPEORequisitionId | REQUISITION_ID | — | — |
| 4 | RequisitionBPEORequisitionNumber | REQUISITION_NUMBER | — | ✅ |

### [[irc_requisitions_tl|IRC_REQUISITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FromRequisitionTLPEOLanguage | LANGUAGE | — | — |
| 2 | FromRequisitionTLPEORequisitionId | REQUISITION_ID | — | — |
| 3 | FromRequisitionTLPEOTitle | TITLE | — | ✅ |

### [[irc_source_tracking|IRC_SOURCE_TRACKING]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParentSourceTrackingPEOSourceTrackingId | SOURCE_TRACKING_ID | — | — |
| 2 | SourceTrackingId | SOURCE_TRACKING_ID | 🔑 | ✅ |
| 3 | SourceTrackingPEOAgencyId | AGENCY_ID | — | ✅ |
| 4 | SourceTrackingPEOAgentId | AGENT_ID | — | ✅ |
| 5 | SourceTrackingPEOCampaignCode | CAMPAIGN_CODE | — | ✅ |
| 6 | SourceTrackingPEOCandidateNumber | CANDIDATE_NUMBER | — | ✅ |
| 7 | SourceTrackingPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | SourceTrackingPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | SourceTrackingPEODimensionId | DIMENSION_ID | — | ✅ |
| 10 | SourceTrackingPEOEventId | EVENT_ID | — | — |
| 11 | SourceTrackingPEOFromPoolId | FROM_POOL_ID | — | ✅ |
| 12 | SourceTrackingPEOFromRequisitionId | FROM_REQUISITION_ID | — | ✅ |
| 13 | SourceTrackingPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | SourceTrackingPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | SourceTrackingPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | SourceTrackingPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | SourceTrackingPEOParentSourceTrackingId | PARENT_SOURCE_TRACKING_ID | — | ✅ |
| 18 | SourceTrackingPEOPoolId | POOL_ID | — | ✅ |
| 19 | SourceTrackingPEOPoolMemberId | POOL_MEMBER_ID | — | ✅ |
| 20 | SourceTrackingPEOProspectId | PROSPECT_ID | — | ✅ |
| 21 | SourceTrackingPEORecruiterId | RECRUITER_ID | — | ✅ |
| 22 | SourceTrackingPEOReferralId | REFERRAL_ID | — | ✅ |
| 23 | SourceTrackingPEOReferredDate | REFERRED_DATE | — | ✅ |
| 24 | SourceTrackingPEORequisitionId | REQUISITION_ID | — | ✅ |
| 25 | SourceTrackingPEOShareId | SHARE_ID | — | ✅ |
| 26 | SourceTrackingPEOSourceLevel | SOURCE_LEVEL | — | ✅ |
| 27 | SourceTrackingPEOSubmissionId | SUBMISSION_ID | — | ✅ |
| 28 | SourceTrackingPEOTokenId | TOKEN_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
