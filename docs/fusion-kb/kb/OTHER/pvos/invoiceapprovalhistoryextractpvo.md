---
id: DOC-OTHER-PVO-InvoiceApprovalHistoryExtractPVO
doc_type: system-doc
title: "InvoiceApprovalHistoryExtractPVO — PVO Cross-Module"
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
  - InvoiceApprovalHistoryExtractPVO
  - invoiceapprovalhistoryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvoiceApprovalHistoryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Invoice Approval History Extract. Acessa as tabelas: AP_INV_APRVL_HIST_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ApBiccExtractAM.InvoiceApprovalHistoryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 19 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ap_inv_aprvl_hist_all|AP_INV_APRVL_HIST_ALL]] — 19 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[ap_inv_aprvl_hist_all|AP_INV_APRVL_HIST_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApInvAprvlHistAllAmountApproved | AMOUNT_APPROVED | — | ✅ |
| 2 | ApInvAprvlHistAllApprovalHistoryId | APPROVAL_HISTORY_ID | 🔑 | ✅ |
| 3 | ApInvAprvlHistAllApproverComments | APPROVER_COMMENTS | — | ✅ |
| 4 | ApInvAprvlHistAllApproverId | APPROVER_ID | — | ✅ |
| 5 | ApInvAprvlHistAllCreatedBy | CREATED_BY | — | ✅ |
| 6 | ApInvAprvlHistAllCreationDate | CREATION_DATE | — | ✅ |
| 7 | ApInvAprvlHistAllHistoryType | HISTORY_TYPE | — | ✅ |
| 8 | ApInvAprvlHistAllHoldId | HOLD_ID | — | ✅ |
| 9 | ApInvAprvlHistAllInvoiceId | INVOICE_ID | — | ✅ |
| 10 | ApInvAprvlHistAllIteration | ITERATION | — | ✅ |
| 11 | ApInvAprvlHistAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ApInvAprvlHistAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | ApInvAprvlHistAllLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | ApInvAprvlHistAllLineNumber | LINE_NUMBER | — | ✅ |
| 15 | ApInvAprvlHistAllNotificationOrder | NOTIFICATION_ORDER | — | ✅ |
| 16 | ApInvAprvlHistAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | ApInvAprvlHistAllOrgId | ORG_ID | — | ✅ |
| 18 | ApInvAprvlHistAllOrigSystem | ORIG_SYSTEM | — | ✅ |
| 19 | ApInvAprvlHistAllResponse | RESPONSE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
