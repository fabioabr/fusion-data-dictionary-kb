---
id: DOC-OTHER-PVO-CostOrgParametersExtractPVO
doc_type: system-doc
title: "CostOrgParametersExtractPVO — PVO Cross-Module"
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
  - CostOrgParametersExtractPVO
  - costorgparametersextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostOrgParametersExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Org Parameters Extract. Acessa as tabelas: CST_COST_ORG_PARAMETERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CostOrgParametersExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 1 | 7 | 88% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_org_parameters|CST_COST_ORG_PARAMETERS]] — 8 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[cst_cost_org_parameters|CST_COST_ORG_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrgParameterPEOCostOrgId | COST_ORG_ID | 🔑 | ✅ |
| 2 | CostOrgParametersPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | CostOrgParametersPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | CostOrgParametersPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | CostOrgParametersPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | CostOrgParametersPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | CostOrgParametersPEOMasterOrganizationId | MASTER_ORGANIZATION_ID | — | ✅ |
| 8 | CostOrgParametersPEOValidationOrganizationId | VALIDATION_ORGANIZATION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
