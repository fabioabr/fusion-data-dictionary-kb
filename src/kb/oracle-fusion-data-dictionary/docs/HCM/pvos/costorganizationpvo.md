---
id: DOC-HCM-PVO-CostOrganizationPVO
doc_type: system-doc
title: "CostOrganizationPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
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

Extrai organizacoes de custo com nome e vigencia. Referencia para alocacao contabil de custos de pessoal por unidade.

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

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
