---
id: DOC-HCM-PVO-ProposalLookupProposalTypePVO
doc_type: system-doc
title: "ProposalLookupProposalTypePVO — PVO Human Capital Management"
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
  - ProposalLookupProposalTypePVO
  - proposallookupproposaltypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProposalLookupProposalTypePVO

## 📌 Visão Geral

Disponibiliza valores de lookup para tipo de proposta. Classifica propostas por natureza (novo produto, extensão, descontinuação) no portfólio.

**Caminho:** `FscmTopModelAM.RelationshipsAnalyticsAM.ProposalLookupProposalTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 12 | 92% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_lookups|FND_LOOKUPS]] — 13 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[fnd_lookups|FND_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | — |
| 4 | DisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 5 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 11 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 12 | Meaning | MEANING | — | ✅ |
| 13 | StartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
