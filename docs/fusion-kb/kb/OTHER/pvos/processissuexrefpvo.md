---
id: DOC-OTHER-PVO-ProcessIssueXrefPVO
doc_type: system-doc
title: "ProcessIssueXrefPVO — PVO Cross-Module"
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
  - ProcessIssueXrefPVO
  - processissuexrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProcessIssueXrefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Process Issue Xref. Acessa as tabelas: GRC_ISSU_PROC_XREF.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.ProcessIssueXrefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 5 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[grc_issu_proc_xref|GRC_ISSU_PROC_XREF]] — 13 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[grc_issu_proc_xref|GRC_ISSU_PROC_XREF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueProcessXrefPEOAssessmentResultId | ASSESSMENT_RESULT_ID | — | ✅ |
| 2 | IssueProcessXrefPEOChildObjectTypeId | CHILD_OBJECT_TYPE_ID | — | — |
| 3 | IssueProcessXrefPEOCreatedBy | CREATED_BY | — | — |
| 4 | IssueProcessXrefPEOCreationDate | CREATION_DATE | — | — |
| 5 | IssueProcessXrefPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 6 | IssueProcessXrefPEOIssueId | ISSUE_ID | 🔑 | ✅ |
| 7 | IssueProcessXrefPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | IssueProcessXrefPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | IssueProcessXrefPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | IssueProcessXrefPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | IssueProcessXrefPEOProcessId | PROCESS_ID | 🔑 | ✅ |
| 12 | IssueProcessXrefPEORevisionDate | REVISION_DATE | — | — |
| 13 | IssueProcessXrefPEORevisionNumber | REVISION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
