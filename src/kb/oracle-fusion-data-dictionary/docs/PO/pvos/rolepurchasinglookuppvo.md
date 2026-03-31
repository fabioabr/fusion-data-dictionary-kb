---
id: DOC-PO-PVO-RolePurchasingLookupPVO
doc_type: system-doc
title: "RolePurchasingLookupPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - RolePurchasingLookupPVO
  - rolepurchasinglookuppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RolePurchasingLookupPVO

## 📌 Visão Geral

Extrai os papéis de compras configurados (comprador, aprovador, receiver, requisitante). Suporta auditoria de segregação de funções e análise de distribuição de responsabilidades em procurement.

**Caminho:** `FscmTopModelAM.PrcPoPublicViewAM.RolePurchasingLookupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 2 | 4 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[po_lookup_codes|PO_LOOKUP_CODES]] — 15 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[po_lookup_codes|PO_LOOKUP_CODES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 3 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 4 | PoLookupCreationDate | CREATION_DATE | — | — |
| 5 | PoLookupDescription | DESCRIPTION | — | — |
| 6 | PoLookupDisplayedField | DISPLAYED_FIELD | — | ✅ |
| 7 | PoLookupEnabledFlag | ENABLED_FLAG | — | — |
| 8 | PoLookupEndDateActive | END_DATE_ACTIVE | — | — |
| 9 | PoLookupLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | PoLookupLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | PoLookupLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | PoLookupProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 13 | PoLookupProgramId | PROGRAM_ID | — | — |
| 14 | PoLookupProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 15 | PoLookupRequestId | REQUEST_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
