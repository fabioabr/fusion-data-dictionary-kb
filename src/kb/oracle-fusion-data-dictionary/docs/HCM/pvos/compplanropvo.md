---
id: DOC-HCM-PVO-CompPlanROPVO
doc_type: system-doc
title: "CompPlanROPVO — PVO Human Capital Management"
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
  - CompPlanROPVO
  - compplanropvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CompPlanROPVO

## 📌 Visão Geral

Versao read-only dos planos de compensacao de incentivos com 38 atributos. Utilizado em consultas analiticas de planos de comissao e bonus.

**Caminho:** `FscmTopModelAM.CompensationPlanAM.CompPlanROPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 2 | 1 | 15 | 39% |

---

## 🔗 Tabelas Relacionadas

- [[cn_comp_plans_all_b|CN_COMP_PLANS_ALL_B]] — 30 atributos (1 PKs, 10 BICC)
- [[cn_comp_plans_all_tl|CN_COMP_PLANS_ALL_TL]] — 8 atributos (5 BICC)

---

## ⚙️ Atributos

### [[cn_comp_plans_all_b|CN_COMP_PLANS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllowEcatOverlapFlag | ALLOW_ECAT_OVERLAP_FLAG | — | ✅ |
| 2 | ApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 3 | Attribute1 | ATTRIBUTE1 | — | — |
| 4 | Attribute10 | ATTRIBUTE10 | — | — |
| 5 | Attribute11 | ATTRIBUTE11 | — | — |
| 6 | Attribute12 | ATTRIBUTE12 | — | — |
| 7 | Attribute13 | ATTRIBUTE13 | — | — |
| 8 | Attribute14 | ATTRIBUTE14 | — | — |
| 9 | Attribute15 | ATTRIBUTE15 | — | — |
| 10 | Attribute2 | ATTRIBUTE2 | — | — |
| 11 | Attribute3 | ATTRIBUTE3 | — | — |
| 12 | Attribute4 | ATTRIBUTE4 | — | — |
| 13 | Attribute5 | ATTRIBUTE5 | — | — |
| 14 | Attribute6 | ATTRIBUTE6 | — | — |
| 15 | Attribute7 | ATTRIBUTE7 | — | — |
| 16 | Attribute8 | ATTRIBUTE8 | — | — |
| 17 | Attribute9 | ATTRIBUTE9 | — | — |
| 18 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | CompPlanId | COMP_PLAN_ID | 🔑 | ✅ |
| 20 | CreatedBy | CREATED_BY | — | ✅ |
| 21 | CreationDate | CREATION_DATE | — | ✅ |
| 22 | EndDate | END_DATE | — | ✅ |
| 23 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 26 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | OrgId | ORG_ID | — | — |
| 28 | PlanStatus | PLAN_STATUS | — | ✅ |
| 29 | StartDate | START_DATE | — | ✅ |
| 30 | TargetIncentive | TARGET_INCENTIVE | — | ✅ |

### [[cn_comp_plans_all_tl|CN_COMP_PLANS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CompPlanId1 | COMP_PLAN_ID | — | ✅ |
| 2 | CompPlanName | COMP_PLAN_NAME | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | DisplayName | DISPLAY_NAME | — | ✅ |
| 5 | Language | LANGUAGE | — | ✅ |
| 6 | Language1 | LANGUAGE | — | — |
| 7 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 8 | OrgId1 | ORG_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
