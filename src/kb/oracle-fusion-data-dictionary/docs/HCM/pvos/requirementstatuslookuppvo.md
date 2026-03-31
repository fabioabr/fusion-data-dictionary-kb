---
id: DOC-HCM-PVO-RequirementStatusLookupPVO
doc_type: system-doc
title: "RequirementStatusLookupPVO — PVO Human Capital Management"
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
  - RequirementStatusLookupPVO
  - requirementstatuslookuppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequirementStatusLookupPVO

## 📌 Visão Geral

Disponibiliza valores de lookup para status de requisitos. Padroniza os estados possíveis (ativo, inativo, aprovado) de requisitos de produto.

**Caminho:** `FscmTopModelAM.RelationshipsAnalyticsAM.RequirementStatusLookupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 2 | 7 | 88% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_lookups|FND_LOOKUPS]] — 8 atributos (2 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[fnd_lookups|FND_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | — |
| 2 | DisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 3 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 4 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 5 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 6 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 7 | Meaning | MEANING | — | ✅ |
| 8 | StartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
