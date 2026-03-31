---
id: DOC-OTHER-PVO-PjeIssue
doc_type: system-doc
title: "PjeIssue — PVO Cross-Module"
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
  - PjeIssue
  - pjeissue
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjeIssue

## 📌 Visão Geral

View Object para extração BICC de dados de Pje Issue. Acessa as tabelas: PJE_ISSUES_B, PJE_ISSUES_TL, PJF_PROJECTS_ALL_B.

**Caminho:** `FscmTopModelAM.PjeIssuesAM.PjeIssue`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 3 | 2 | 18 | 53% |

---

## 🔗 Tabelas Relacionadas

- [[pje_issues_b|PJE_ISSUES_B]] — 23 atributos (2 PKs, 14 BICC)
- [[pje_issues_tl|PJE_ISSUES_TL]] — 7 atributos (4 BICC)
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 4 atributos

---

## ⚙️ Atributos

### [[pje_issues_b|PJE_ISSUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 2 | IssueBasePEOClosedReason | CLOSED_REASON | — | — |
| 3 | IssueBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | IssueBasePEOCreatedById | CREATED_BY_ID | — | ✅ |
| 5 | IssueBasePEOCreationDate | CREATION_DATE | — | — |
| 6 | IssueBasePEODateClosed | DATE_CLOSED | — | ✅ |
| 7 | IssueBasePEODateCreated | DATE_CREATED | — | ✅ |
| 8 | IssueBasePEOIssueNumber | ISSUE_NUMBER | — | ✅ |
| 9 | IssueBasePEOIssueTypeId | ISSUE_TYPE_ID | — | ✅ |
| 10 | IssueBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | IssueBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | IssueBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | IssueBasePEONeedByDate | NEED_BY_DATE | — | ✅ |
| 14 | IssueBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | IssueBasePEOOwnerId | OWNER_ID | — | — |
| 16 | IssueBasePEOPriorityCode | PRIORITY_CODE | — | ✅ |
| 17 | IssueBasePEOProjectId | PROJECT_ID | — | ✅ |
| 18 | IssueBasePEOStatusCode | STATUS_CODE | — | ✅ |
| 19 | IssueBasePEOTaskId | TASK_ID | — | — |
| 20 | IssueId | ISSUE_ID | 🔑 | ✅ |
| 21 | ObjectId | OBJECT_ID | — | — |
| 22 | ObjectType | OBJECT_TYPE | — | — |
| 23 | OwnerId | OWNER_ID | — | — |

### [[pje_issues_tl|PJE_ISSUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueTranslationPEODescription | DESCRIPTION | — | ✅ |
| 2 | IssueTranslationPEOEnterpriseId1 | ENTERPRISE_ID | — | — |
| 3 | IssueTranslationPEOIssueId2 | ISSUE_ID | — | — |
| 4 | IssueTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | IssueTranslationPEOReopenSummary | REOPEN_SUMMARY | — | ✅ |
| 6 | IssueTranslationPEOResolution | RESOLUTION | — | ✅ |
| 7 | IssueTranslationPEOSummary | SUMMARY | — | ✅ |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | ProjectBasePEOOrgId | ORG_ID | — | — |
| 3 | ProjectBasePEOProjectId | PROJECT_ID | — | — |
| 4 | ProjectBasePEOProjectUnitId | PROJECT_UNIT_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
