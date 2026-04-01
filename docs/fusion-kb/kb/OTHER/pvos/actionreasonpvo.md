---
id: DOC-OTHER-PVO-ActionReasonPVO
doc_type: system-doc
title: "ActionReasonPVO — PVO Cross-Module"
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
  - ActionReasonPVO
  - actionreasonpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ActionReasonPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Action Reason. Acessa as tabelas: HER_ACTION_REASON_VL.

**Caminho:** `FscmTopModelAM.StudentEnrollmentAM.ActionReasonPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 3 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[her_action_reason_vl|HER_ACTION_REASON_VL]] — 16 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[her_action_reason_vl|HER_ACTION_REASON_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionReasonPEOActionReason | ACTION_REASON | — | — |
| 2 | ActionReasonPEOActionReasonCode | ACTION_REASON_CODE | — | — |
| 3 | ActionReasonPEOActionReasonContext | ACTION_REASON_CONTEXT | — | — |
| 4 | ActionReasonPEOActionReasonDisplay | ACTION_REASON_DISPLAY | — | — |
| 5 | ActionReasonPEOActionReasonId | ACTION_REASON_ID | 🔑 | ✅ |
| 6 | ActionReasonPEOCreatedBy | CREATED_BY | — | — |
| 7 | ActionReasonPEOCreationDate | CREATION_DATE | — | — |
| 8 | ActionReasonPEODescription | DESCRIPTION | — | ✅ |
| 9 | ActionReasonPEOEndDate | END_DATE | — | — |
| 10 | ActionReasonPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | ActionReasonPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | ActionReasonPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | ActionReasonPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | ActionReasonPEOReasonProcessingSequence | REASON_PROCESSING_SEQUENCE | — | — |
| 15 | ActionReasonPEOSetId | SET_ID | — | — |
| 16 | ActionReasonPEOStartDate | START_DATE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
