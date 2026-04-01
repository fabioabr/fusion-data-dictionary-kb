---
id: DOC-AP-PVO-TaskStatusP1
doc_type: system-doc
title: "TaskStatusP1 — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - TaskStatusP1
  - taskstatusp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskStatusP1

## 📌 Visão Geral

Extrai a tabela de lookup de status de tarefas utilizada em processos de RH, incluindo código e significado de cada status. Serve como referência para interpretar o estado de tarefas nos fluxos de trabalho de gestão de pessoas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmApprovalsReportingAM.TaskStatusP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 2 | 14% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_lookups|FND_LOOKUPS]] — 14 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[fnd_lookups|FND_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LookupPEOCreatedBy | CREATED_BY | — | — |
| 2 | LookupPEOCreationDate | CREATION_DATE | — | — |
| 3 | LookupPEODescription | DESCRIPTION | — | — |
| 4 | LookupPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 5 | LookupPEOEnabledFlag | ENABLED_FLAG | — | — |
| 6 | LookupPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 7 | LookupPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | LookupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LookupPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | LookupPEOLookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 11 | LookupPEOLookupType | LOOKUP_TYPE | — | — |
| 12 | LookupPEOMeaning | MEANING | — | ✅ |
| 13 | LookupPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 14 | LookupPEOTag | TAG | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
