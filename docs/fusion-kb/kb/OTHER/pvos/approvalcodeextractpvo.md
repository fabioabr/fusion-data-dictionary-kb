---
id: DOC-OTHER-PVO-ApprovalCodeExtractPVO
doc_type: system-doc
title: "ApprovalCodeExtractPVO — PVO Cross-Module"
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
  - ApprovalCodeExtractPVO
  - approvalcodeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ApprovalCodeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Approval Code Extract. Acessa as tabelas: AP_HOLD_CODES.

**Caminho:** `FscmTopModelAM.FinExtractAM.ApBiccExtractAM.ApprovalCodeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ap_hold_codes|AP_HOLD_CODES]] — 17 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[ap_hold_codes|AP_HOLD_CODES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApHoldCodesCreatedBy | CREATED_BY | — | ✅ |
| 2 | ApHoldCodesCreationDate | CREATION_DATE | — | ✅ |
| 3 | ApHoldCodesExternalDescription | EXTERNAL_DESCRIPTION | — | ✅ |
| 4 | ApHoldCodesHoldInstruction | HOLD_INSTRUCTION | — | ✅ |
| 5 | ApHoldCodesHoldLookupCode | HOLD_LOOKUP_CODE | 🔑 | ✅ |
| 6 | ApHoldCodesHoldType | HOLD_TYPE | — | ✅ |
| 7 | ApHoldCodesInactiveDate | INACTIVE_DATE | — | ✅ |
| 8 | ApHoldCodesInitiateWorkflowFlag | INITIATE_WORKFLOW_FLAG | — | ✅ |
| 9 | ApHoldCodesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ApHoldCodesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | ApHoldCodesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ApHoldCodesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | ApHoldCodesPostableFlag | POSTABLE_FLAG | — | ✅ |
| 14 | ApHoldCodesReminderDays | REMINDER_DAYS | — | ✅ |
| 15 | ApHoldCodesUserReleaseableFlag | USER_RELEASEABLE_FLAG | — | ✅ |
| 16 | ApHoldCodesUserUpdateableFlag | USER_UPDATEABLE_FLAG | — | ✅ |
| 17 | ApHoldCodesWaitBeforeNotifyDays | WAIT_BEFORE_NOTIFY_DAYS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
