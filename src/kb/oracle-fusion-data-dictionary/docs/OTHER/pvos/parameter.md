---
id: DOC-OTHER-PVO-Parameter
doc_type: system-doc
title: "Parameter — PVO Cross-Module"
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
  - Parameter
  - parameter
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Parameter

## 📌 Visão Geral

View Object para extração BICC de dados de Parameter. Acessa as tabelas: MSC_ORGS_WITH_PIMID_V.

**Caminho:** `FscmTopModelAM.DooTopAM.Parameter`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 74 | 1 | 1 | 3 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[msc_orgs_with_pimid_v|MSC_ORGS_WITH_PIMID_V]] — 74 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[msc_orgs_with_pimid_v|MSC_ORGS_WITH_PIMID_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcceptDemandsFromUnmetPo | ACCEPT_DEMANDS_FROM_UNMET_PO | — | — |
| 2 | BusinessGroupName | BUSINESS_GROUP_NAME | — | — |
| 3 | CalendarCode | CALENDAR_CODE | — | — |
| 4 | CalendarExceptionSetId | CALENDAR_EXCEPTION_SET_ID | — | — |
| 5 | CollectedFlag | COLLECTED_FLAG | — | — |
| 6 | CompanyId | COMPANY_ID | — | — |
| 7 | ConsiderPo | CONSIDER_PO | — | — |
| 8 | ConsiderReservations | CONSIDER_RESERVATIONS | — | — |
| 9 | ConsiderWip | CONSIDER_WIP | — | — |
| 10 | CreatedBy | CREATED_BY | — | — |
| 11 | CreationDate | CREATION_DATE | — | — |
| 12 | CurrencyCode | CURRENCY_CODE | — | — |
| 13 | CustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 14 | DefaultAbcAssignmentGroup | DEFAULT_ABC_ASSIGNMENT_GROUP | — | — |
| 15 | DefaultAtpRuleId | DEFAULT_ATP_RULE_ID | — | — |
| 16 | DefaultDemandClass | DEFAULT_DEMAND_CLASS | — | — |
| 17 | DemandLatenessCost | DEMAND_LATENESS_COST | — | — |
| 18 | DemandTimeFenceFlag | DEMAND_TIME_FENCE_FLAG | — | — |
| 19 | ExpenseAccount | EXPENSE_ACCOUNT | — | — |
| 20 | IncludeMdsDays | INCLUDE_MDS_DAYS | — | — |
| 21 | IncludePastDueForecast | INCLUDE_PAST_DUE_FORECAST | — | — |
| 22 | IncludeRepSupplyDays | INCLUDE_REP_SUPPLY_DAYS | — | — |
| 23 | InheritOcOpSeqNum | INHERIT_OC_OP_SEQ_NUM | — | — |
| 24 | InheritPhantomOpSeq | INHERIT_PHANTOM_OP_SEQ | — | — |
| 25 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 28 | LegalEntityName | LEGAL_ENTITY_NAME | — | — |
| 29 | MasterOrganizationId | MASTER_ORGANIZATION_ID | — | — |
| 30 | MaterialAccount | MATERIAL_ACCOUNT | — | — |
| 31 | MaximumVolume | MAXIMUM_VOLUME | — | — |
| 32 | MaximumWeight | MAXIMUM_WEIGHT | — | — |
| 33 | ModeledCustomerId | MODELED_CUSTOMER_ID | — | — |
| 34 | ModeledCustomerSiteId | MODELED_CUSTOMER_SITE_ID | — | — |
| 35 | ModeledSupplierId | MODELED_SUPPLIER_ID | — | — |
| 36 | ModeledSupplierSiteId | MODELED_SUPPLIER_SITE_ID | — | — |
| 37 | NetOnHand | NET_ON_HAND | — | — |
| 38 | NetworkSchedulingMethod | NETWORK_SCHEDULING_METHOD | — | — |
| 39 | OperatingUnit | OPERATING_UNIT | — | — |
| 40 | OperatingUnitName | OPERATING_UNIT_NAME | — | — |
| 41 | OperationScheduleType | OPERATION_SCHEDULE_TYPE | — | — |
| 42 | OrgSupplierMapped | ORG_SUPPLIER_MAPPED | — | — |
| 43 | OrganizationCode | ORGANIZATION_CODE | — | — |
| 44 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 45 | OrganizationName | ORGANIZATION_NAME | — | ✅ |
| 46 | OrganizationType | ORGANIZATION_TYPE | — | — |
| 47 | PartIncludeType | PART_INCLUDE_TYPE | — | — |
| 48 | PartnerId | PARTNER_ID | — | — |
| 49 | PeriodType | PERIOD_TYPE | — | — |
| 50 | PlanDateDefaultType | PLAN_DATE_DEFAULT_TYPE | — | — |
| 51 | PlanSafetyStock | PLAN_SAFETY_STOCK | — | — |
| 52 | PlanningTimeFenceFlag | PLANNING_TIME_FENCE_FLAG | — | — |
| 53 | ProjectControlLevel | PROJECT_CONTROL_LEVEL | — | — |
| 54 | ProjectReferenceEnabled | PROJECT_REFERENCE_ENABLED | — | — |
| 55 | RepetitiveAnchorDate | REPETITIVE_ANCHOR_DATE | — | — |
| 56 | RepetitiveBucketSize1 | REPETITIVE_BUCKET_SIZE1 | — | — |
| 57 | RepetitiveBucketSize2 | REPETITIVE_BUCKET_SIZE2 | — | — |
| 58 | RepetitiveBucketSize3 | REPETITIVE_BUCKET_SIZE3 | — | — |
| 59 | RepetitiveHorizon1 | REPETITIVE_HORIZON1 | — | — |
| 60 | RepetitiveHorizon2 | REPETITIVE_HORIZON2 | — | — |
| 61 | ReschedAssumption | RESCHED_ASSUMPTION | — | — |
| 62 | ResourceCapOverutilCost | RESOURCE_CAP_OVERUTIL_COST | — | — |
| 63 | ServiceLevel | SERVICE_LEVEL | — | — |
| 64 | SnapshotLock | SNAPSHOT_LOCK | — | — |
| 65 | SrBusinessGroupId | SR_BUSINESS_GROUP_ID | — | — |
| 66 | SrChartOfAccountsId | SR_CHART_OF_ACCOUNTS_ID | — | — |
| 67 | SrInstanceId | SR_INSTANCE_ID | — | — |
| 68 | SrLegalEntity | SR_LEGAL_ENTITY | — | — |
| 69 | SrSetOfBooksId | SR_SET_OF_BOOKS_ID | — | — |
| 70 | SupplierCapOverutilCost | SUPPLIER_CAP_OVERUTIL_COST | — | — |
| 71 | TransportCapOverUtilCost | TRANSPORT_CAP_OVER_UTIL_COST | — | — |
| 72 | UsePhantomRoutings | USE_PHANTOM_ROUTINGS | — | — |
| 73 | VolumeUom | VOLUME_UOM | — | — |
| 74 | WeightUom | WEIGHT_UOM | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
