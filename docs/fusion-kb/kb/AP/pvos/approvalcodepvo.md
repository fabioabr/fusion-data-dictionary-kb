---
id: DOC-AP-PVO-ApprovalCodePVO
doc_type: system-doc
title: "ApprovalCodePVO — PVO Accounts Payable"
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
  - ApprovalCodePVO
  - approvalcodepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ApprovalCodePVO

## 📌 Visão Geral

Extrai os códigos de retenção (hold codes) de faturas no contas a pagar, incluindo descrição e tipo de bloqueio. Permite catalogar os motivos de retenção de faturas e padronizar o fluxo de aprovação de pagamentos.

**Caminho:** `FscmTopModelAM.FinApInvSetupInvHoldsAM.ApprovalCodePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 7 | 41% |

---

## 🔗 Tabelas Relacionadas

- [[ap_hold_codes|AP_HOLD_CODES]] — 17 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[ap_hold_codes|AP_HOLD_CODES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApHoldCodesCreatedBy | CREATED_BY | — | ✅ |
| 2 | ApHoldCodesCreationDate | CREATION_DATE | — | ✅ |
| 3 | ApHoldCodesExternalDescription | EXTERNAL_DESCRIPTION | — | — |
| 4 | ApHoldCodesHoldInstruction | HOLD_INSTRUCTION | — | — |
| 5 | ApHoldCodesHoldType | HOLD_TYPE | — | ✅ |
| 6 | ApHoldCodesInactiveDate | INACTIVE_DATE | — | ✅ |
| 7 | ApHoldCodesInitiateWorkflowFlag | INITIATE_WORKFLOW_FLAG | — | — |
| 8 | ApHoldCodesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ApHoldCodesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ApHoldCodesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ApHoldCodesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ApHoldCodesPostableFlag | POSTABLE_FLAG | — | — |
| 13 | ApHoldCodesReminderDays | REMINDER_DAYS | — | — |
| 14 | ApHoldCodesUserReleaseableFlag | USER_RELEASEABLE_FLAG | — | — |
| 15 | ApHoldCodesUserUpdateableFlag | USER_UPDATEABLE_FLAG | — | — |
| 16 | ApHoldCodesWaitBeforeNotifyDays | WAIT_BEFORE_NOTIFY_DAYS | — | — |
| 17 | HoldLookupCode | HOLD_LOOKUP_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
