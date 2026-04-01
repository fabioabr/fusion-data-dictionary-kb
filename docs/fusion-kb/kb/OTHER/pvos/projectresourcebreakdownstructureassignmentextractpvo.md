---
id: DOC-OTHER-PVO-ProjectResourceBreakdownStructureAssignmentExtractPVO
doc_type: system-doc
title: "ProjectResourceBreakdownStructureAssignmentExtractPVO — PVO Cross-Module"
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
  - ProjectResourceBreakdownStructureAssignmentExtractPVO
  - projectresourcebreakdownstructureassignmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectResourceBreakdownStructureAssignmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Resource Breakdown Structure Assignment Extract. Acessa as tabelas: PJF_RBS_PRJ_ASSIGNMENTS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectResourceBreakdownStructureAssignmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_rbs_prj_assignments|PJF_RBS_PRJ_ASSIGNMENTS]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[pjf_rbs_prj_assignments|PJF_RBS_PRJ_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PRBSAssignmentPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PRBSAssignmentPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PRBSAssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | PRBSAssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | PRBSAssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | PRBSAssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | PRBSAssignmentPEOPlanningUsageFlag | PLANNING_USAGE_FLAG | — | ✅ |
| 8 | PRBSAssignmentPEOPrimaryPlanningRbsFlag | PRIMARY_PLANNING_RBS_FLAG | — | ✅ |
| 9 | PRBSAssignmentPEOPrimaryReportingRbsFlag | PRIMARY_REPORTING_RBS_FLAG | — | ✅ |
| 10 | PRBSAssignmentPEOProjectId | PROJECT_ID | — | ✅ |
| 11 | PRBSAssignmentPEORbsHeaderId | RBS_HEADER_ID | — | ✅ |
| 12 | PRBSAssignmentPEORbsPrjAssignmentId | RBS_PRJ_ASSIGNMENT_ID | 🔑 | ✅ |
| 13 | PRBSAssignmentPEORbsVersionId | RBS_VERSION_ID | — | ✅ |
| 14 | PRBSAssignmentPEOReportingUsageFlag | REPORTING_USAGE_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
