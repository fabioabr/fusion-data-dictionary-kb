---
id: DOC-OTHER-PVO-CstCostInvOrgsExtractPVO
doc_type: system-doc
title: "CstCostInvOrgsExtractPVO — PVO Cross-Module"
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
  - CstCostInvOrgsExtractPVO
  - cstcostinvorgsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstCostInvOrgsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Cost Inv Orgs Extract. Acessa as tabelas: CST_COST_INV_ORGS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstCostInvOrgsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_inv_orgs|CST_COST_INV_ORGS]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cst_cost_inv_orgs|CST_COST_INV_ORGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstCostInvOrgsPEOCostInvOrgId | COST_INV_ORG_ID | — | ✅ |
| 2 | CstCostInvOrgsPEOCostOrgId | COST_ORG_ID | 🔑 | ✅ |
| 3 | CstCostInvOrgsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CstCostInvOrgsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CstCostInvOrgsPEOFromDate | FROM_DATE | — | ✅ |
| 6 | CstCostInvOrgsPEOInvOrgId | INV_ORG_ID | 🔑 | ✅ |
| 7 | CstCostInvOrgsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CstCostInvOrgsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | CstCostInvOrgsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | CstCostInvOrgsPEOMasterOrganizationId | MASTER_ORGANIZATION_ID | — | ✅ |
| 11 | CstCostInvOrgsPEOToDate | TO_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
