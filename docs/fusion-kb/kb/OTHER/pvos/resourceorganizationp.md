---
id: DOC-OTHER-PVO-ResourceOrganizationP
doc_type: system-doc
title: "ResourceOrganizationP — PVO Cross-Module"
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
  - ResourceOrganizationP
  - resourceorganizationp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourceOrganizationP

## 📌 Visão Geral

View Object para extração BICC de dados de Resource Organization P. Acessa as tabelas: OKC_RESOURCE_ORGANIZATIONS_V.

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ResourceOrganizationP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[okc_resource_organizations_v|OKC_RESOURCE_ORGANIZATIONS_V]] — 9 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[okc_resource_organizations_v|OKC_RESOURCE_ORGANIZATIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 2 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 3 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | EstablishmentId | ESTABLISHMENT_ID | — | ✅ |
| 5 | InternalExternalFlag | INTERNAL_EXTERNAL_FLAG | — | ✅ |
| 6 | Name | NAME | — | ✅ |
| 7 | OrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 8 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 9 | Type | TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
