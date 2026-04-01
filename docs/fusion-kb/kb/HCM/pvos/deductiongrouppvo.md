---
id: DOC-HCM-PVO-DeductionGroupPVO
doc_type: system-doc
title: "DeductionGroupPVO — PVO Human Capital Management"
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
  - DeductionGroupPVO
  - deductiongrouppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DeductionGroupPVO

## 📌 Visão Geral

Disponibiliza grupos de deducao de folha com nome base e identificador. Referencia para agrupamento logico de deducoes em payroll.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayDeductionSetupAM.DeductionGroupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 9 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[pay_deduction_groups_vl|PAY_DEDUCTION_GROUPS_VL]] — 11 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[pay_deduction_groups_vl|PAY_DEDUCTION_GROUPS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeductionGroupPEOBaseDeductionGroupId | BASE_DEDUCTION_GROUP_ID | — | — |
| 2 | DeductionGroupPEOBaseName | BASE_NAME | — | ✅ |
| 3 | DeductionGroupPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | DeductionGroupPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | DeductionGroupPEODeductionGroupId | DEDUCTION_GROUP_ID | 🔑 | ✅ |
| 6 | DeductionGroupPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DeductionGroupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | DeductionGroupPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | DeductionGroupPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 10 | DeductionGroupPEOModuleId | MODULE_ID | — | — |
| 11 | DeductionGroupPEOName | NAME | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
