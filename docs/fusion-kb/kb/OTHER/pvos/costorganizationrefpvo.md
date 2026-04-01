---
id: DOC-OTHER-PVO-CostOrganizationRefPVO
doc_type: system-doc
title: "CostOrganizationRefPVO — PVO Cross-Module"
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
  - CostOrganizationRefPVO
  - costorganizationrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostOrganizationRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Organization Ref. Acessa as tabelas: CST_COST_ORGS_V.

**Caminho:** `FscmTopModelAM.CostOrganizationAM.CostOrganizationRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 6 | 1 | 1 | 5 | 83% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_orgs_v|CST_COST_ORGS_V]] — 6 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[cst_cost_orgs_v|CST_COST_ORGS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrgId | COST_ORG_ID | 🔑 | ✅ |
| 2 | CostOrganizationVPEOCostOrgCode | COST_ORG_CODE | — | — |
| 3 | CostOrganizationVPEOCostOrgName | COST_ORG_NAME | — | ✅ |
| 4 | CostOrganizationVPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 5 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
