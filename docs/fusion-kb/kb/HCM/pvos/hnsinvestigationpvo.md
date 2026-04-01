---
id: DOC-HCM-PVO-HNSInvestigationPVO
doc_type: system-doc
title: "HNSInvestigationPVO — PVO Human Capital Management"
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
  - HNSInvestigationPVO
  - hnsinvestigationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HNSInvestigationPVO

## 📌 Visão Geral

Consolida investigações de incidentes de SST com achados e recomendações. Fundamental para análise de causa raiz e prevenção de recorrências.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HealthandSafetyAM.HNSInvestigationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 81 | 3 | 4 | 59 | 73% |

---

## 🔗 Tabelas Relacionadas

- [[hns_investigations_summary|HNS_INVESTIGATIONS_SUMMARY]] — 55 atributos (1 PKs, 33 BICC)
- [[hns_invest_findings|HNS_INVEST_FINDINGS]] — 14 atributos (1 PKs, 14 BICC)
- [[hns_invest_recommends|HNS_INVEST_RECOMMENDS]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hns_investigations_summary|HNS_INVESTIGATIONS_SUMMARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSInvestigationsSummaryPEOActComDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | HNSInvestigationsSummaryPEOActionRequirdFlag | ACTION_REQUIRED_FLAG | — | ✅ |
| 3 | HNSInvestigationsSummaryPEOAttrCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | HNSInvestigationsSummaryPEOAttrNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 5 | HNSInvestigationsSummaryPEOAttrNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 6 | HNSInvestigationsSummaryPEOAttrNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 7 | HNSInvestigationsSummaryPEOAttrNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 8 | HNSInvestigationsSummaryPEOAttrNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 9 | HNSInvestigationsSummaryPEOAttrTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 10 | HNSInvestigationsSummaryPEOAttrTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 11 | HNSInvestigationsSummaryPEOAttrTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 12 | HNSInvestigationsSummaryPEOAttrTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 13 | HNSInvestigationsSummaryPEOAttrTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 14 | HNSInvestigationsSummaryPEOAttribute1 | ATTRIBUTE1 | — | — |
| 15 | HNSInvestigationsSummaryPEOAttribute10 | ATTRIBUTE10 | — | — |
| 16 | HNSInvestigationsSummaryPEOAttribute2 | ATTRIBUTE2 | — | — |
| 17 | HNSInvestigationsSummaryPEOAttribute3 | ATTRIBUTE3 | — | — |
| 18 | HNSInvestigationsSummaryPEOAttribute4 | ATTRIBUTE4 | — | — |
| 19 | HNSInvestigationsSummaryPEOAttribute5 | ATTRIBUTE5 | — | — |
| 20 | HNSInvestigationsSummaryPEOAttribute6 | ATTRIBUTE6 | — | — |
| 21 | HNSInvestigationsSummaryPEOAttribute7 | ATTRIBUTE7 | — | — |
| 22 | HNSInvestigationsSummaryPEOAttribute8 | ATTRIBUTE8 | — | — |
| 23 | HNSInvestigationsSummaryPEOAttribute9 | ATTRIBUTE9 | — | — |
| 24 | HNSInvestigationsSummaryPEOCompletedFlag | COMPLETED_FLAG | — | ✅ |
| 25 | HNSInvestigationsSummaryPEOContFctCd | CONTRIBUTING_FACTORS_CODE | — | ✅ |
| 26 | HNSInvestigationsSummaryPEOCreatedBy | CREATED_BY | — | ✅ |
| 27 | HNSInvestigationsSummaryPEOCreationDate | CREATION_DATE | — | ✅ |
| 28 | HNSInvestigationsSummaryPEOCslFctCd | CASUAL_FACTORS_CODE | — | ✅ |
| 29 | HNSInvestigationsSummaryPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 30 | HNSInvestigationsSummaryPEOFindFinalResp | FINDING_FINAL_RESPONSE | — | ✅ |
| 31 | HNSInvestigationsSummaryPEOFindingComnt | FINDING_COMMENT | — | ✅ |
| 32 | HNSInvestigationsSummaryPEOImdtCseCd | IMMEDIATE_CAUSE_CODE | — | ✅ |
| 33 | HNSInvestigationsSummaryPEOIncdntDetId | INCIDENT_DETAIL_ID | — | ✅ |
| 34 | HNSInvestigationsSummaryPEOIncidentId | INCIDENT_ID | — | ✅ |
| 35 | HNSInvestigationsSummaryPEOInvAprEmlFlg | INVEST_APPROVER_EMAIL_FLAG | — | ✅ |
| 36 | HNSInvestigationsSummaryPEOInvOwnAsnId | INVEST_OWNER_ASSIGN_ID | — | — |
| 37 | HNSInvestigationsSummaryPEOInvPreEmlFlg | INVEST_PRECOM_EMAIL_FLAG | — | ✅ |
| 38 | HNSInvestigationsSummaryPEOInvRevEmlFlg | INVEST_REVIEWER_EMAIL_FLAG | — | ✅ |
| 39 | HNSInvestigationsSummaryPEOInvSummary | INVESTIGATE_SUMMARY | — | ✅ |
| 40 | HNSInvestigationsSummaryPEOInvTypeCode | INVESTIGATE_TYPE_CODE | — | ✅ |
| 41 | HNSInvestigationsSummaryPEOInvestOwnerId | INVESTIGATE_OWNER_ID | — | ✅ |
| 42 | HNSInvestigationsSummaryPEOInvestStatCd | INVEST_STATUS_CODE | — | ✅ |
| 43 | HNSInvestigationsSummaryPEOInvestigateDescr | INVESTIGATE_DESCRIPTION | — | ✅ |
| 44 | HNSInvestigationsSummaryPEOInvestigateDt | INVESTIGATE_DATE | — | ✅ |
| 45 | HNSInvestigationsSummaryPEOInvestigateId | INVESTIGATE_ID | 🔑 | ✅ |
| 46 | HNSInvestigationsSummaryPEOInvestigateNo | INVESTIGATE_NO | — | ✅ |
| 47 | HNSInvestigationsSummaryPEOLastUpdateDt | LAST_UPDATE_DATE | — | ✅ |
| 48 | HNSInvestigationsSummaryPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 49 | HNSInvestigationsSummaryPEOLastUpdtLog | LAST_UPDATE_LOGIN | — | ✅ |
| 50 | HNSInvestigationsSummaryPEOLsnsLearned | LESSONS_LEARNED | — | ✅ |
| 51 | HNSInvestigationsSummaryPEOObjVerNum | OBJECT_VERSION_NUMBER | — | ✅ |
| 52 | HNSInvestigationsSummaryPEOQuestionId | QUESTIONNAIRE_ID | — | ✅ |
| 53 | HNSInvestigationsSummaryPEORtCseCd | ROOT_CAUSE_CODE | — | ✅ |
| 54 | HNSInvestigationsSummaryPEOTarCompDate | TARGET_COMPLETION_DATE | — | ✅ |
| 55 | HNSInvestigationsSummaryPEOUndFctCd | UNDERLYING_FACTORS_CODE | — | ✅ |

### [[hns_invest_findings|HNS_INVEST_FINDINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSInvestFindingsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | HNSInvestFindingsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | HNSInvestFindingsPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 4 | HNSInvestFindingsPEOFindingId | FINDING_ID | 🔑 | ✅ |
| 5 | HNSInvestFindingsPEOFindingIssueFlag | FINDING_ISSUE_FLAG | — | ✅ |
| 6 | HNSInvestFindingsPEOFindingNotes | FINDING_NOTES | — | ✅ |
| 7 | HNSInvestFindingsPEOFindingResponse | FINDING_RESPONSE | — | ✅ |
| 8 | HNSInvestFindingsPEOFindingSummary | FINDING_SUMMARY | — | ✅ |
| 9 | HNSInvestFindingsPEOInvestigateId | INVESTIGATE_ID | — | ✅ |
| 10 | HNSInvestFindingsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | HNSInvestFindingsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | HNSInvestFindingsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | HNSInvestFindingsPEOSeverityLevelCode | SEVERITY_LEVEL_CODE | — | ✅ |
| 14 | HNSInvestFindingsPEObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

### [[hns_invest_recommends|HNS_INVEST_RECOMMENDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSInvestRecommendsPEOActionFlag | ACTION_FLAG | — | ✅ |
| 2 | HNSInvestRecommendsPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | HNSInvestRecommendsPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | HNSInvestRecommendsPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 5 | HNSInvestRecommendsPEOFindingId | FINDING_ID | 🔑 | ✅ |
| 6 | HNSInvestRecommendsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | HNSInvestRecommendsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | HNSInvestRecommendsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | HNSInvestRecommendsPEOObjectVersionNum | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | HNSInvestRecommendsPEORecommendId | RECOMMEND_ID | 🔑 | ✅ |
| 11 | HNSInvestRecommendsPEORecommendSuggFlag | RECOMMEND_SUGGESTION_FLAG | — | ✅ |
| 12 | HNSInvestRecommendsPEORecommendSummary | RECOMMENDATION_SUMMARY | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
