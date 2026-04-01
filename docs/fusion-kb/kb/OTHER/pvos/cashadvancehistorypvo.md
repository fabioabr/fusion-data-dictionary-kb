---
id: DOC-OTHER-PVO-CashAdvanceHistoryPVO
doc_type: system-doc
title: "CashAdvanceHistoryPVO — PVO Cross-Module"
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
  - CashAdvanceHistoryPVO
  - cashadvancehistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CashAdvanceHistoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cash Advance History. Acessa as tabelas: EXM_CASH_ADV_HISTORY, PER_PERSON_NAMES_F_V.

**Caminho:** `FscmTopModelAM.FinExmEntrySharedAM.CashAdvanceHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 1 | 5 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[exm_cash_adv_history|EXM_CASH_ADV_HISTORY]] — 16 atributos (1 PKs, 4 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (1 BICC)

---

## ⚙️ Atributos

### [[exm_cash_adv_history|EXM_CASH_ADV_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Action | EVENT | — | ✅ |
| 2 | ActionDate | EVENT_DATE | — | ✅ |
| 3 | ActionTakenBy | EVENT_PERFORMER | — | — |
| 4 | ApprovalLevel | APPROVAL_LEVEL | — | — |
| 5 | AuditReturnReasonCode | AUDIT_RETURN_REASON_CODE | — | — |
| 6 | CashAdvanceHistId | CASH_ADVANCE_HIST_ID | 🔑 | ✅ |
| 7 | CashAdvanceId | CASH_ADVANCE_ID | — | — |
| 8 | CreatedBy | CREATED_BY | — | — |
| 9 | CreationDate | CREATION_DATE | — | — |
| 10 | ExportRejectCode | EXPORT_REJECT_CODE | — | — |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | RequestId | REQUEST_ID | — | — |
| 16 | StatusCode | STATUS_CODE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerActionTakenByDisplayName | LIST_NAME | — | ✅ |
| 2 | PerActionTakenByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PerActionTakenByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PerActionTakenByPersonId | PERSON_ID | — | — |
| 5 | PerActionTakenByPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
