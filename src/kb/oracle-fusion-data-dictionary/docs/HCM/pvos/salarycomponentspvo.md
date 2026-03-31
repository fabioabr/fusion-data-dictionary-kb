---
id: DOC-HCM-PVO-SalaryComponentsPVO
doc_type: system-doc
title: "SalaryComponentsPVO — PVO Human Capital Management"
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
  - SalaryComponentsPVO
  - salarycomponentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SalaryComponentsPVO

## 📌 Visão Geral

Disponibiliza componentes de salário com valores de alteração e percentuais. Suporta detalhamento de composição salarial e análise de remuneração por componente.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.SalaryComponentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 9 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_salary_components|CMP_SALARY_COMPONENTS]] — 14 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[cmp_salary_components|CMP_SALARY_COMPONENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ComponentsEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | ComponentsEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ComponentsEOChangeAmount | CHANGE_AMOUNT | — | ✅ |
| 4 | ComponentsEOChangePercentage | CHANGE_PERCENTAGE | — | ✅ |
| 5 | ComponentsEOComponentApproved | COMPONENT_APPROVED | — | ✅ |
| 6 | ComponentsEOComponentReasonCode | COMPONENT_REASON_CODE | — | ✅ |
| 7 | ComponentsEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | ComponentsEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | ComponentsEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ComponentsEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ComponentsEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ComponentsEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | ComponentsEOSalaryId | SALARY_ID | — | — |
| 14 | SalaryComponentId | SALARY_COMPONENT_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
