---
id: DOC-OTHER-PVO-PlanningOrganizationPVO
doc_type: system-doc
title: "PlanningOrganizationPVO — PVO Cross-Module"
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
  - PlanningOrganizationPVO
  - planningorganizationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanningOrganizationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Planning Organization. Acessa as tabelas: MSC_ANALYTIC_ORG_FLAT_V_DYD.

**Caminho:** `FscmTopModelAM.MscAnalyticsTopAM.PlanningOrganizationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 7 | 1 | 1 | 7 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[msc_analytic_org_flat_v_dyd|MSC_ANALYTIC_ORG_FLAT_V_DYD]] — 7 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[msc_analytic_org_flat_v_dyd|MSC_ANALYTIC_ORG_FLAT_V_DYD]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 2 | OrganizationPEOBusinessUnit | BUSINESS_UNIT_NAME | — | ✅ |
| 3 | OrganizationPEOBusinessUnitId | BUSINESS_UNIT | — | ✅ |
| 4 | OrganizationPEOLegalEntity | LEGAL_ENTITY_NAME | — | ✅ |
| 5 | OrganizationPEOLegalEntityId | LEGAL_ENTITY | — | ✅ |
| 6 | OrganizationPEOOrganization | ORGANIZATION_NAME | — | ✅ |
| 7 | OrganizationPEOOrganizationCode | ORGANIZATION_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
