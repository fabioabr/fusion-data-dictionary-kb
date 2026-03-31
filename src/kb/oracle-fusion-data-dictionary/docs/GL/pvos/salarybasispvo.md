---
id: DOC-GL-PVO-SalaryBasisPVO
doc_type: system-doc
title: "SalaryBasisPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SalaryBasisPVO
  - salarybasispvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SalaryBasisPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Salary Basis. Acessa as tabelas: CMP_SALARY_BASES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GradeAM.SalaryBasisPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 18 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_salary_bases|CMP_SALARY_BASES]] — 19 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[cmp_salary_bases|CMP_SALARY_BASES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalaryBasisId | SALARY_BASIS_ID | 🔑 | ✅ |
| 2 | SalaryBasisPEOAnnualizedHours | ANNUALIZED_HOURS | — | ✅ |
| 3 | SalaryBasisPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 4 | SalaryBasisPEOComponentUsage | COMPONENT_USAGE | — | ✅ |
| 5 | SalaryBasisPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | SalaryBasisPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | SalaryBasisPEOElementTypeId | ELEMENT_TYPE_ID | — | ✅ |
| 8 | SalaryBasisPEOGradeAnnualizationFactor | GRADE_ANNUALIZATION_FACTOR | — | ✅ |
| 9 | SalaryBasisPEOGradeRateBasisCode | GRADE_RATE_BASIS_CODE | — | ✅ |
| 10 | SalaryBasisPEOGradeRateId | GRADE_RATE_ID | — | ✅ |
| 11 | SalaryBasisPEOInputValueId | INPUT_VALUE_ID | — | ✅ |
| 12 | SalaryBasisPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | SalaryBasisPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | SalaryBasisPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | SalaryBasisPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 16 | SalaryBasisPEOName | NAME | — | ✅ |
| 17 | SalaryBasisPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | SalaryBasisPEOSalaryAnnualizationFactor | SALARY_ANNUALIZATION_FACTOR | — | ✅ |
| 19 | SalaryBasisPEOSalaryBasisCode | SALARY_BASIS_CODE | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
