---
id: DOC-OTHER-PVO-FOBContractLookup
doc_type: system-doc
title: "FOBContractLookup — PVO Cross-Module"
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
  - FOBContractLookup
  - fobcontractlookup
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FOBContractLookup

## 📌 Visão Geral

View Object para extração BICC de dados de FOBContract Lookup. Acessa as tabelas: FND_LOOKUPS.

**Caminho:** `FscmTopModelAM.ContractsCoreAM.FOBContractLookup`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 5 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_lookups|FND_LOOKUPS]] — 13 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[fnd_lookups|FND_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LookupPEOCreatedBy | CREATED_BY | — | — |
| 2 | LookupPEOCreationDate | CREATION_DATE | — | — |
| 3 | LookupPEODescription | DESCRIPTION | — | ✅ |
| 4 | LookupPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 5 | LookupPEOEnabledFlag | ENABLED_FLAG | — | — |
| 6 | LookupPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 7 | LookupPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LookupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LookupPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | LookupPEOLookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 11 | LookupPEOLookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 12 | LookupPEOMeaning | MEANING | — | ✅ |
| 13 | LookupPEOStartDateActive | START_DATE_ACTIVE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
