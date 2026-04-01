---
id: DOC-OTHER-PVO-PjeIssueType
doc_type: system-doc
title: "PjeIssueType — PVO Cross-Module"
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
  - PjeIssueType
  - pjeissuetype
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjeIssueType

## 📌 Visão Geral

View Object para extração BICC de dados de Pje Issue Type. Acessa as tabelas: PJE_ISSUE_TYPES_B, PJE_ISSUE_TYPES_TL.

**Caminho:** `FscmTopModelAM.PjeIssuesAM.PjeIssueType`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 2 | 6 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[pje_issue_types_b|PJE_ISSUE_TYPES_B]] — 11 atributos (2 PKs, 3 BICC)
- [[pje_issue_types_tl|PJE_ISSUE_TYPES_TL]] — 11 atributos (3 BICC)

---

## ⚙️ Atributos

### [[pje_issue_types_b|PJE_ISSUE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 2 | IssueTypeBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | IssueTypeBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | IssueTypeBasePEODisabled | DISABLED | — | — |
| 5 | IssueTypeBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 6 | IssueTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | IssueTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | IssueTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | IssueTypeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | IssueTypeBasePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 11 | IssueTypeId | ISSUE_TYPE_ID | 🔑 | ✅ |

### [[pje_issue_types_tl|PJE_ISSUE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueTypeTranslationPEOCreatedBy1 | CREATED_BY | — | — |
| 2 | IssueTypeTranslationPEOCreationDate1 | CREATION_DATE | — | — |
| 3 | IssueTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | IssueTypeTranslationPEOEnterpriseId1 | ENTERPRISE_ID | — | — |
| 5 | IssueTypeTranslationPEOIssueTypeId2 | ISSUE_TYPE_ID | — | — |
| 6 | IssueTypeTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | IssueTypeTranslationPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 8 | IssueTypeTranslationPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 9 | IssueTypeTranslationPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 10 | IssueTypeTranslationPEOName | NAME | — | ✅ |
| 11 | IssueTypeTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
