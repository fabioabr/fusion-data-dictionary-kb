---
id: DOC-OTHER-PVO-ControlIssueXrefPVO
doc_type: system-doc
title: "ControlIssueXrefPVO — PVO Cross-Module"
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
  - ControlIssueXrefPVO
  - controlissuexrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ControlIssueXrefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Control Issue Xref. Acessa as tabelas: GRC_ISSU_CTRL_XREF.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.ControlIssueXrefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 4 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[grc_issu_ctrl_xref|GRC_ISSU_CTRL_XREF]] — 13 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[grc_issu_ctrl_xref|GRC_ISSU_CTRL_XREF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueControlXrefPEOAssessmentResultId | ASSESSMENT_RESULT_ID | — | ✅ |
| 2 | IssueControlXrefPEOChildObjectTypeId | CHILD_OBJECT_TYPE_ID | — | — |
| 3 | IssueControlXrefPEOControlId | CONTROL_ID | 🔑 | ✅ |
| 4 | IssueControlXrefPEOCreatedBy | CREATED_BY | — | — |
| 5 | IssueControlXrefPEOCreationDate | CREATION_DATE | — | — |
| 6 | IssueControlXrefPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 7 | IssueControlXrefPEOIssueId | ISSUE_ID | 🔑 | ✅ |
| 8 | IssueControlXrefPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | IssueControlXrefPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | IssueControlXrefPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | IssueControlXrefPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | IssueControlXrefPEORevisionDate | REVISION_DATE | — | — |
| 13 | IssueControlXrefPEORevisionNumber | REVISION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
