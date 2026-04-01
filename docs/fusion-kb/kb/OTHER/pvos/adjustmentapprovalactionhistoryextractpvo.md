---
id: DOC-OTHER-PVO-AdjustmentApprovalActionHistoryExtractPVO
doc_type: system-doc
title: "AdjustmentApprovalActionHistoryExtractPVO — PVO Cross-Module"
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
  - AdjustmentApprovalActionHistoryExtractPVO
  - adjustmentapprovalactionhistoryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdjustmentApprovalActionHistoryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Adjustment Approval Action History Extract. Acessa as tabelas: AR_APPROVAL_ACTION_HISTORY.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.AdjustmentApprovalActionHistoryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 1 | 1 | 11 | 41% |

---

## 🔗 Tabelas Relacionadas

- [[ar_approval_action_history|AR_APPROVAL_ACTION_HISTORY]] — 27 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[ar_approval_action_history|AR_APPROVAL_ACTION_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArApprovalActionHistoryActionDate | ACTION_DATE | — | ✅ |
| 2 | ArApprovalActionHistoryActionName | ACTION_NAME | — | ✅ |
| 3 | ArApprovalActionHistoryAdjustmentId | ADJUSTMENT_ID | — | ✅ |
| 4 | ArApprovalActionHistoryApprovalActionHistoryId | APPROVAL_ACTION_HISTORY_ID | 🔑 | ✅ |
| 5 | ArApprovalActionHistoryAttribute1 | ATTRIBUTE1 | — | — |
| 6 | ArApprovalActionHistoryAttribute10 | ATTRIBUTE10 | — | — |
| 7 | ArApprovalActionHistoryAttribute11 | ATTRIBUTE11 | — | — |
| 8 | ArApprovalActionHistoryAttribute12 | ATTRIBUTE12 | — | — |
| 9 | ArApprovalActionHistoryAttribute13 | ATTRIBUTE13 | — | — |
| 10 | ArApprovalActionHistoryAttribute14 | ATTRIBUTE14 | — | — |
| 11 | ArApprovalActionHistoryAttribute15 | ATTRIBUTE15 | — | — |
| 12 | ArApprovalActionHistoryAttribute2 | ATTRIBUTE2 | — | — |
| 13 | ArApprovalActionHistoryAttribute3 | ATTRIBUTE3 | — | — |
| 14 | ArApprovalActionHistoryAttribute4 | ATTRIBUTE4 | — | — |
| 15 | ArApprovalActionHistoryAttribute5 | ATTRIBUTE5 | — | — |
| 16 | ArApprovalActionHistoryAttribute6 | ATTRIBUTE6 | — | — |
| 17 | ArApprovalActionHistoryAttribute7 | ATTRIBUTE7 | — | — |
| 18 | ArApprovalActionHistoryAttribute8 | ATTRIBUTE8 | — | — |
| 19 | ArApprovalActionHistoryAttribute9 | ATTRIBUTE9 | — | — |
| 20 | ArApprovalActionHistoryAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 21 | ArApprovalActionHistoryComments | COMMENTS | — | ✅ |
| 22 | ArApprovalActionHistoryCreatedBy | CREATED_BY | — | ✅ |
| 23 | ArApprovalActionHistoryCreationDate | CREATION_DATE | — | ✅ |
| 24 | ArApprovalActionHistoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | ArApprovalActionHistoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 26 | ArApprovalActionHistoryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | ArApprovalActionHistoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
