---
id: DOC-OTHER-PVO-ContractFulLineLookup
doc_type: system-doc
title: "ContractFulLineLookup — PVO Cross-Module"
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
  - ContractFulLineLookup
  - contractfullinelookup
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractFulLineLookup

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Ful Line Lookup. Acessa as tabelas: PO_LOOKUP_CODES.

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractFulLineLookup`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 2 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[po_lookup_codes|PO_LOOKUP_CODES]] — 15 atributos (2 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[po_lookup_codes|PO_LOOKUP_CODES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | DisplayedField | DISPLAYED_FIELD | — | ✅ |
| 5 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 11 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 12 | ProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 13 | ProgramId | PROGRAM_ID | — | ✅ |
| 14 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 15 | RequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
