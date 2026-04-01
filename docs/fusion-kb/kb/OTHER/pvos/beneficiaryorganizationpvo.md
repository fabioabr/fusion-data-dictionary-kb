---
id: DOC-OTHER-PVO-BeneficiaryOrganizationPVO
doc_type: system-doc
title: "BeneficiaryOrganizationPVO — PVO Cross-Module"
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
  - BeneficiaryOrganizationPVO
  - beneficiaryorganizationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BeneficiaryOrganizationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Beneficiary Organization. Acessa as tabelas: BEN_PER_BNF_ORG.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.BeneficiaryOrganizationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 11 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[ben_per_bnf_org|BEN_PER_BNF_ORG]] — 18 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[ben_per_bnf_org|BEN_PER_BNF_ORG]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BeneficiaryOrganizationPEOBnfOrganizationId | BNF_ORGANIZATION_ID | — | ✅ |
| 2 | BeneficiaryOrganizationPEOBnfTypCd | BNF_TYP_CD | — | ✅ |
| 3 | BeneficiaryOrganizationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | BeneficiaryOrganizationPEOCreatedBy | CREATED_BY | — | — |
| 5 | BeneficiaryOrganizationPEOCreationDate | CREATION_DATE | — | — |
| 6 | BeneficiaryOrganizationPEOEndDate | END_DATE | — | ✅ |
| 7 | BeneficiaryOrganizationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | BeneficiaryOrganizationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | BeneficiaryOrganizationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | BeneficiaryOrganizationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | BeneficiaryOrganizationPEOPerBnfOrgId | PER_BNF_ORG_ID | 🔑 | ✅ |
| 12 | BeneficiaryOrganizationPEOPersonId | PERSON_ID | — | — |
| 13 | BeneficiaryOrganizationPEOStartDate | START_DATE | — | ✅ |
| 14 | BeneficiaryOrganizationPEOTrusteeAddlDetails | TRUSTEE_ADDL_DETAILS | — | ✅ |
| 15 | BeneficiaryOrganizationPEOTrusteeExecutorName | TRUSTEE_EXECUTOR_NAME | — | ✅ |
| 16 | BeneficiaryOrganizationPEOTrusteeOrgDescription | TRUSTEE_ORG_DESCRIPTION | — | ✅ |
| 17 | BeneficiaryOrganizationPEOTrusteeOrgName | TRUSTEE_ORG_NAME | — | ✅ |
| 18 | BeneficiaryOrganizationPEOTrusteeOrgRegCd | TRUSTEE_ORG_REG_CD | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
