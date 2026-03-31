---
id: DOC-OTHER-PVO-WarrantyCoverageApplicabilityExtractPVO
doc_type: system-doc
title: "WarrantyCoverageApplicabilityExtractPVO — PVO Cross-Module"
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
  - WarrantyCoverageApplicabilityExtractPVO
  - warrantycoverageapplicabilityextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WarrantyCoverageApplicabilityExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Warranty Coverage Applicability Extract. Acessa as tabelas: CSE_W_COVERAGE_APPLICABILITIES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.WarrantyCoverageApplicabilityExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_w_coverage_applicabilities|CSE_W_COVERAGE_APPLICABILITIES]] — 17 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[cse_w_coverage_applicabilities|CSE_W_COVERAGE_APPLICABILITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | AutoAssignFlag | AUTO_ASSIGN_FLAG | — | ✅ |
| 3 | ContractDfltStatusCode | CONTRACT_DFLT_STATUS_CODE | — | ✅ |
| 4 | CoverageApplicabilityId | COVERAGE_APPLICABILITY_ID | 🔑 | ✅ |
| 5 | CoverageId | COVERAGE_ID | — | ✅ |
| 6 | CoveredItemId | COVERED_ITEM_ID | — | ✅ |
| 7 | CoveredOrganizationId | COVERED_ORGANIZATION_ID | — | ✅ |
| 8 | CreatedBy | CREATED_BY | — | ✅ |
| 9 | CreationDate | CREATION_DATE | — | ✅ |
| 10 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 11 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | RequestId | REQUEST_ID | — | ✅ |
| 17 | SupplierId | SUPPLIER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
