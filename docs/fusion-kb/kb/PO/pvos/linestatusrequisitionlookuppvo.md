---
id: DOC-PO-PVO-LineStatusRequisitionLookupPVO
doc_type: system-doc
title: "LineStatusRequisitionLookupPVO — PVO Purchasing"
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
  - LineStatusRequisitionLookupPVO
  - linestatusrequisitionlookuppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LineStatusRequisitionLookupPVO

## 📌 Visão Geral

Extrai os valores de lookup para status de linhas de requisição (pendente, processada, cancelada). Permite análise granular de gargalos por linha e acompanhamento detalhado de solicitações.

**Caminho:** `FscmTopModelAM.PrcPorPublicViewAM.LineStatusRequisitionLookupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 2 | 5 | 62% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_lookups|FND_LOOKUPS]] — 8 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[fnd_lookups|FND_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | DisplaySequence | DISPLAY_SEQUENCE | — | — |
| 3 | EnabledFlag | ENABLED_FLAG | — | — |
| 4 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 5 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 6 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 7 | Meaning | MEANING | — | ✅ |
| 8 | StartDateActive | START_DATE_ACTIVE | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
