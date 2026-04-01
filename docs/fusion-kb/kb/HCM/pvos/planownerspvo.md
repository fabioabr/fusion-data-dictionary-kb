---
id: DOC-HCM-PVO-PlanOwnersPVO
doc_type: system-doc
title: "PlanOwnersPVO — PVO Human Capital Management"
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
  - PlanOwnersPVO
  - planownerspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanOwnersPVO

## 📌 Visão Geral

Extrai os proprietários dos planos de sucessão, com tipo de propriedade e enterprise ID. Permite identificar responsáveis pela manutenção e atualização dos planos de sucessão.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmSuccessionPlansAM.PlanOwnersPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 2 | 2 | 14 | 88% |

---

## 🔗 Tabelas Relacionadas

- [[hcm_lookups|HCM_LOOKUPS]] — 3 atributos (3 BICC)
- [[hrm_plan_owners|HRM_PLAN_OWNERS]] — 13 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[hcm_lookups|HCM_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LookUpPEOForOwnerTypeCodeLookType | LOOKUP_TYPE | — | ✅ |
| 2 | LookUpPEOForOwnerTypeCodeLookUpCode | LOOKUP_CODE | — | ✅ |
| 3 | PlanOwnerPEOOwnerTypeCode | MEANING | — | ✅ |

### [[hrm_plan_owners|HRM_PLAN_OWNERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | PlanOwnerPEODateFrom | DATE_FROM | — | — |
| 8 | PlanOwnerPEOEnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 9 | PlanOwnerPEOLatestRecordFlag | LATEST_RECORD_FLAG | — | — |
| 10 | PlanOwnerPEOOwnerTypeCodeLookupCode | OWNER_TYPE_CODE | — | ✅ |
| 11 | PlanOwnerPEOPersonId | PERSON_ID | — | ✅ |
| 12 | PlanOwnerPEOPlanId | PLAN_ID | — | ✅ |
| 13 | PlanOwnerPEOPlanOwnerId | PLAN_OWNER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
