---
id: DOC-OTHER-PVO-IpCriteriaExtractPVO
doc_type: system-doc
title: "IpCriteriaExtractPVO — PVO Cross-Module"
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
  - IpCriteriaExtractPVO
  - ipcriteriaextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IpCriteriaExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ip Criteria Extract. Acessa as tabelas: QA_IP_CRITERIA.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.IpCriteriaExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[qa_ip_criteria|QA_IP_CRITERIA]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[qa_ip_criteria|QA_IP_CRITERIA]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionPlanCriteriaPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InspectionPlanCriteriaPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InspectionPlanCriteriaPEODispatchStatus | DISPATCH_STATUS | — | ✅ |
| 4 | InspectionPlanCriteriaPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 5 | InspectionPlanCriteriaPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | InspectionPlanCriteriaPEOInspectionPlanId | INSPECTION_PLAN_ID | — | ✅ |
| 7 | InspectionPlanCriteriaPEOInspectionPlanType | INSPECTION_PLAN_TYPE | — | ✅ |
| 8 | InspectionPlanCriteriaPEOIpCriteriaId | IP_CRITERIA_ID | 🔑 | ✅ |
| 9 | InspectionPlanCriteriaPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | InspectionPlanCriteriaPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | InspectionPlanCriteriaPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | InspectionPlanCriteriaPEOLocatorId | LOCATOR_ID | — | ✅ |
| 13 | InspectionPlanCriteriaPEOOperationCode | OPERATION_CODE | — | ✅ |
| 14 | InspectionPlanCriteriaPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | ✅ |
| 15 | InspectionPlanCriteriaPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 16 | InspectionPlanCriteriaPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 17 | InspectionPlanCriteriaPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 18 | InspectionPlanCriteriaPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 19 | InspectionPlanCriteriaPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 20 | InspectionPlanCriteriaPEOWorkDefinitionNameId | WORK_DEFINITION_NAME_ID | — | ✅ |
| 21 | InspectionPlanCriteriaPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | ✅ |
| 22 | InspectionPlanCriteriaPEOWorkOrderType | WORK_ORDER_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
