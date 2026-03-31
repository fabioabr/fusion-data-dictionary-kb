---
id: DOC-OTHER-PVO-AwardOrganizationCreditPVO
doc_type: system-doc
title: "AwardOrganizationCreditPVO — PVO Cross-Module"
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
  - AwardOrganizationCreditPVO
  - awardorganizationcreditpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardOrganizationCreditPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Organization Credit. Acessa as tabelas: GMS_AWARD_DEPARTMENT_CREDITS, GMS_AWARD_PROJECTS, GMS_ORGANIZATIONS_ALL_V.

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardOrganizationCreditPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 3 | 2 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_department_credits|GMS_AWARD_DEPARTMENT_CREDITS]] — 11 atributos (1 PKs, 11 BICC)
- [[gms_award_projects|GMS_AWARD_PROJECTS]] — 2 atributos (2 BICC)
- [[gms_organizations_all_v|GMS_ORGANIZATIONS_ALL_V]] — 2 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[gms_award_department_credits|GMS_AWARD_DEPARTMENT_CREDITS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardDepartmentCreditPEOAwardId | AWARD_ID | — | ✅ |
| 2 | AwardDepartmentCreditPEOAwdProjectLnkId | AWD_PROJECT_LNK_ID | — | ✅ |
| 3 | AwardDepartmentCreditPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AwardDepartmentCreditPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AwardDepartmentCreditPEODepartmentCredit | DEPARTMENT_CREDIT | — | ✅ |
| 6 | AwardDepartmentCreditPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AwardDepartmentCreditPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AwardDepartmentCreditPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AwardDepartmentCreditPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | AwardDepartmentCreditPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 11 | Id | ID | 🔑 | ✅ |

### [[gms_award_projects|GMS_AWARD_PROJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardProjectPEOId | ID | — | ✅ |
| 2 | AwardProjectPEOProjectId | PROJECT_ID | — | ✅ |

### [[gms_organizations_all_v|GMS_ORGANIZATIONS_ALL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardOwningOrganizationPEOName | NAME | — | ✅ |
| 2 | AwardOwningOrganizationPEOOrganizationId | ORGANIZATION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
