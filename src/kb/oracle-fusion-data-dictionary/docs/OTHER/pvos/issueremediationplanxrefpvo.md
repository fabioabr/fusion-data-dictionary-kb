---
id: DOC-OTHER-PVO-IssueRemediationPlanXrefPVO
doc_type: system-doc
title: "IssueRemediationPlanXrefPVO — PVO Cross-Module"
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
  - IssueRemediationPlanXrefPVO
  - issueremediationplanxrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IssueRemediationPlanXrefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Issue Remediation Plan Xref. Acessa as tabelas: GRC_ISSU_RMPLAN_XREF.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.IssueRemediationPlanXrefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 3 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[grc_issu_rmplan_xref|GRC_ISSU_RMPLAN_XREF]] — 11 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[grc_issu_rmplan_xref|GRC_ISSU_RMPLAN_XREF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueRemediationPlanXrefPEOCreatedBy | CREATED_BY | — | — |
| 2 | IssueRemediationPlanXrefPEOCreationDate | CREATION_DATE | — | — |
| 3 | IssueRemediationPlanXrefPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 4 | IssueRemediationPlanXrefPEOIssueId | ISSUE_ID | 🔑 | ✅ |
| 5 | IssueRemediationPlanXrefPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | IssueRemediationPlanXrefPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | IssueRemediationPlanXrefPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | IssueRemediationPlanXrefPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | IssueRemediationPlanXrefPEORemedPlanId | REMED_PLAN_ID | 🔑 | ✅ |
| 10 | IssueRemediationPlanXrefPEORevisionDate | REVISION_DATE | — | — |
| 11 | IssueRemediationPlanXrefPEORevisionNumber | REVISION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
