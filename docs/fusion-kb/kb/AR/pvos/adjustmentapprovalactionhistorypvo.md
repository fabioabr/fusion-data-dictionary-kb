---
id: DOC-AR-PVO-AdjustmentApprovalActionHistoryPVO
doc_type: system-doc
title: "AdjustmentApprovalActionHistoryPVO — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - AdjustmentApprovalActionHistoryPVO
  - adjustmentapprovalactionhistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdjustmentApprovalActionHistoryPVO

## 📌 Visão Geral

Extrai o histórico de ações de aprovação de ajustes em recebíveis, incluindo aprovador, data e decisão. Fornece trilha de auditoria completa para compliance e governança sobre alterações em valores a receber.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.AdjustmentApprovalActionHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 41 | 2 | 1 | 5 | 12% |

---

## 🔗 Tabelas Relacionadas

- [[ar_adjustments_all|AR_ADJUSTMENTS_ALL]] — 29 atributos
- [[ar_approval_action_history|AR_APPROVAL_ACTION_HISTORY]] — 12 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[ar_adjustments_all|AR_ADJUSTMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentAcctdAmount | ACCTD_AMOUNT | — | — |
| 2 | AdjustmentAdjTaxAcctRule | ADJ_TAX_ACCT_RULE | — | — |
| 3 | AdjustmentAdjustmentId | ADJUSTMENT_ID | — | — |
| 4 | AdjustmentAdjustmentNumber | ADJUSTMENT_NUMBER | — | — |
| 5 | AdjustmentAdjustmentType | ADJUSTMENT_TYPE | — | — |
| 6 | AdjustmentAmount | AMOUNT | — | — |
| 7 | AdjustmentApplyDate | APPLY_DATE | — | — |
| 8 | AdjustmentApprovedBy | APPROVED_BY | — | — |
| 9 | AdjustmentAutomaticallyGenerated | AUTOMATICALLY_GENERATED | — | — |
| 10 | AdjustmentAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 11 | AdjustmentComments | COMMENTS | — | — |
| 12 | AdjustmentCreatedFrom | CREATED_FROM | — | — |
| 13 | AdjustmentDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 14 | AdjustmentFreightAdjusted | FREIGHT_ADJUSTED | — | — |
| 15 | AdjustmentGlDate | GL_DATE | — | — |
| 16 | AdjustmentGlPostedDate | GL_POSTED_DATE | — | — |
| 17 | AdjustmentLineAdjusted | LINE_ADJUSTED | — | — |
| 18 | AdjustmentMrcAcctdAmount | MRC_ACCTD_AMOUNT | — | — |
| 19 | AdjustmentMrcGlPostedDate | MRC_GL_POSTED_DATE | — | — |
| 20 | AdjustmentPostable | POSTABLE | — | — |
| 21 | AdjustmentProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 22 | AdjustmentReasonCode | REASON_CODE | — | — |
| 23 | AdjustmentReceivablesChargesAdjusted | RECEIVABLES_CHARGES_ADJUSTED | — | — |
| 24 | AdjustmentStatus | STATUS | — | — |
| 25 | AdjustmentTaxAdjusted | TAX_ADJUSTED | — | — |
| 26 | AdjustmentType | TYPE | — | — |
| 27 | AdjustmentUpgradeMethod | UPGRADE_METHOD | — | — |
| 28 | AdjustmentUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 29 | AdjustmentUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | — |

### [[ar_approval_action_history|AR_APPROVAL_ACTION_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalActionHistoryActionDate | ACTION_DATE | — | ✅ |
| 2 | ApprovalActionHistoryActionName | ACTION_NAME | — | ✅ |
| 3 | ApprovalActionHistoryAdjustmentId | ADJUSTMENT_ID | — | — |
| 4 | ApprovalActionHistoryComments | COMMENTS | — | ✅ |
| 5 | ApprovalActionHistoryContext | CONTEXT | — | — |
| 6 | ApprovalActionHistoryCreatedBy | CREATED_BY | — | — |
| 7 | ApprovalActionHistoryCreationDate | CREATION_DATE | — | — |
| 8 | ApprovalActionHistoryId | APPROVAL_ACTION_HISTORY_ID | 🔑 | ✅ |
| 9 | ApprovalActionHistoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ApprovalActionHistoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ApprovalActionHistoryLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ApprovalActionHistoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
