---
id: DOC-HCM-PVO-TimeEntryPayrollApprovalStatusPVO
doc_type: system-doc
title: "TimeEntryPayrollApprovalStatusPVO — PVO Human Capital Management"
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
  - TimeEntryPayrollApprovalStatusPVO
  - timeentrypayrollapprovalstatuspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeEntryPayrollApprovalStatusPVO

## 📌 Visão Geral

Extrai status de aprovação de payroll para entradas de tempo. Rastreia o fluxo de aprovação de horas para integração com folha de pagamento.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.TimeEntryPayrollApprovalStatusPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 4 | 1 | 2 | 4 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hcm_lookups|HCM_LOOKUPS]] — 4 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hcm_lookups|HCM_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Code | LOOKUP_CODE | 🔑 | ✅ |
| 2 | Description | DESCRIPTION | — | ✅ |
| 3 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 4 | Name | MEANING | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
