---
id: DOC-OTHER-PVO-HNSActionsPVO
doc_type: system-doc
title: "HNSActionsPVO — PVO Cross-Module"
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
  - HNSActionsPVO
  - hnsactionspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HNSActionsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de HNSActions. Acessa as tabelas: HNS_ACTIONS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HealthandSafetyAM.HNSActionsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 1 | 1 | 25 | 54% |

---

## 🔗 Tabelas Relacionadas

- [[hns_actions|HNS_ACTIONS]] — 46 atributos (1 PKs, 25 BICC)

---

## ⚙️ Atributos

### [[hns_actions|HNS_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSActionsPEOActionApproverEmailFlag | ACTION_APPROVER_EMAIL_FLAG | — | ✅ |
| 2 | HNSActionsPEOActionDate | ACTION_DATE | — | ✅ |
| 3 | HNSActionsPEOActionId | ACTION_ID | 🔑 | ✅ |
| 4 | HNSActionsPEOActionNo | ACTION_NO | — | ✅ |
| 5 | HNSActionsPEOActionPrecomEmailFlag | ACTION_PRECOM_EMAIL_FLAG | — | ✅ |
| 6 | HNSActionsPEOActionReviewerEmailFlag | ACTION_REVIEWER_EMAIL_FLAG | — | ✅ |
| 7 | HNSActionsPEOActionStatusCode | ACTION_STATUS_CODE | — | ✅ |
| 8 | HNSActionsPEOActionSummary | ACTION_SUMMARY | — | ✅ |
| 9 | HNSActionsPEOActionTypeCode | ACTION_TYPE_CODE | — | ✅ |
| 10 | HNSActionsPEOAttrNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 11 | HNSActionsPEOAttrNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 12 | HNSActionsPEOAttrNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 13 | HNSActionsPEOAttrNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 14 | HNSActionsPEOAttrNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 15 | HNSActionsPEOAttrTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 16 | HNSActionsPEOAttrTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 17 | HNSActionsPEOAttrTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 18 | HNSActionsPEOAttrTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 19 | HNSActionsPEOAttrTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 20 | HNSActionsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 21 | HNSActionsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 22 | HNSActionsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 23 | HNSActionsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 24 | HNSActionsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 25 | HNSActionsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 26 | HNSActionsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 27 | HNSActionsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 28 | HNSActionsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 29 | HNSActionsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 30 | HNSActionsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 31 | HNSActionsPEOCompletedFlag | COMPLETED_FLAG | — | ✅ |
| 32 | HNSActionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 33 | HNSActionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 34 | HNSActionsPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 35 | HNSActionsPEODescription | DESCRIPTION | — | ✅ |
| 36 | HNSActionsPEOEstCostCurrencyCode | EST_COST_CURRENCY_CODE | — | ✅ |
| 37 | HNSActionsPEOEstimatedCost | ESTIMATED_COST | — | ✅ |
| 38 | HNSActionsPEOIncidentId | INCIDENT_ID | — | ✅ |
| 39 | HNSActionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 40 | HNSActionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 41 | HNSActionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 42 | HNSActionsPEOLessonsLearned | LESSONS_LEARNED | — | ✅ |
| 43 | HNSActionsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 44 | HNSActionsPEOPriorityCode | PRIORITY_CODE | — | ✅ |
| 45 | HNSActionsPEORecommendId | RECOMMEND_ID | — | ✅ |
| 46 | HNSActionsPEOReqResources | REQ_RESOURCES | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
