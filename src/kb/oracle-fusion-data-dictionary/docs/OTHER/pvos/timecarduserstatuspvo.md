---
id: DOC-OTHER-PVO-TimeCardUserStatusPVO
doc_type: system-doc
title: "TimeCardUserStatusPVO — PVO Cross-Module"
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
  - TimeCardUserStatusPVO
  - timecarduserstatuspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeCardUserStatusPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Card User Status. Acessa as tabelas: HCM_LOOKUPS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.TimeCardUserStatusPVO`

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

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
