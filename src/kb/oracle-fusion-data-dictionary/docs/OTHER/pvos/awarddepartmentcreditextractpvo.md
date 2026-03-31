---
id: DOC-OTHER-PVO-AwardDepartmentCreditExtractPVO
doc_type: system-doc
title: "AwardDepartmentCreditExtractPVO — PVO Cross-Module"
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
  - AwardDepartmentCreditExtractPVO
  - awarddepartmentcreditextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardDepartmentCreditExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Department Credit Extract. Acessa as tabelas: GMS_AWARD_DEPARTMENT_CREDITS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardDepartmentCreditExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_department_credits|GMS_AWARD_DEPARTMENT_CREDITS]] — 11 atributos (1 PKs, 11 BICC)

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
| 6 | AwardDepartmentCreditPEOId | ID | 🔑 | ✅ |
| 7 | AwardDepartmentCreditPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AwardDepartmentCreditPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | AwardDepartmentCreditPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | AwardDepartmentCreditPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | AwardDepartmentCreditPEOOrganizationId | ORGANIZATION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
