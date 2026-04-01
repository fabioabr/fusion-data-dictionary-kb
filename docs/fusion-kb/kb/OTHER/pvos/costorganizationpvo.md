---
id: DOC-OTHER-PVO-CostOrganizationPVO
doc_type: system-doc
title: "CostOrganizationPVO — PVO Cross-Module"
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
  - CostOrganizationPVO
  - costorganizationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostOrganizationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Organization. Acessa as tabelas: CST_COST_ORGS_V.

**Caminho:** `FscmTopModelAM.CostOrganizationAM.CostOrganizationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 5 | 1 | 1 | 5 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_orgs_v|CST_COST_ORGS_V]] — 5 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[cst_cost_orgs_v|CST_COST_ORGS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrganizationVEOCostOrgId | COST_ORG_ID | 🔑 | ✅ |
| 2 | CostOrganizationVEOCostOrgName | COST_ORG_NAME | — | ✅ |
| 3 | CostOrganizationVEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 4 | CostOrganizationVEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | CostOrganizationVEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
