---
id: DOC-PO-PVO-SupplierApprovalHistoryPVO
doc_type: system-doc
title: "SupplierApprovalHistoryPVO — PVO Purchasing"
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
  - SupplierApprovalHistoryPVO
  - supplierapprovalhistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierApprovalHistoryPVO

## 📌 Visão Geral

Extrai o histórico de aprovações do cadastro de fornecedores, registrando quem aprovou, quando, com que justificativa e comentários. Essencial para auditoria do processo de homologação.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierApprovalHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 1 | 5 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[poz_approval_history|POZ_APPROVAL_HISTORY]] — 17 atributos (1 PKs, 5 BICC)
- [[poz_bi_appr_user_comments_v|POZ_BI_APPR_USER_COMMENTS_V]] — 4 atributos

---

## ⚙️ Atributos

### [[poz_approval_history|POZ_APPROVAL_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalHistoryId | APPROVAL_HISTORY_ID | 🔑 | ✅ |
| 2 | SupplierApprovalHistoryActionCode | ACTION_CODE | — | ✅ |
| 3 | SupplierApprovalHistoryActionDate | ACTION_DATE | — | ✅ |
| 4 | SupplierApprovalHistoryAdditionalInfo | ADDITIONAL_INFO | — | ✅ |
| 5 | SupplierApprovalHistoryAmxIdentificationKey | AMX_IDENTIFICATION_KEY | — | — |
| 6 | SupplierApprovalHistoryApprovalFlowCode | APPROVAL_FLOW_CODE | — | — |
| 7 | SupplierApprovalHistoryCreatedBy | CREATED_BY | — | — |
| 8 | SupplierApprovalHistoryCreationDate | CREATION_DATE | — | — |
| 9 | SupplierApprovalHistoryFlowObjectId | FLOW_OBJECT_ID | — | — |
| 10 | SupplierApprovalHistoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | SupplierApprovalHistoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | SupplierApprovalHistoryLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | SupplierApprovalHistoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | SupplierApprovalHistoryPerformerId | PERFORMER_ID | — | — |
| 15 | SupplierApprovalHistoryPerformerType | PERFORMER_TYPE | — | — |
| 16 | SupplierApprovalHistorySequenceNum | SEQUENCE_NUM | — | — |
| 17 | SupplierApprovalHistoryVendorId | VENDOR_ID | — | — |

### [[poz_bi_appr_user_comments_v|POZ_BI_APPR_USER_COMMENTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SuppApprUserCommentsActionSeqNum | ACTION_SEQ_NUM | — | — |
| 2 | SuppApprUserCommentsAmxIdentificationKey | AMX_IDENTIFICATION_KEY | — | — |
| 3 | SuppApprUserCommentsLatestComment | LATEST_COMMENT | — | — |
| 4 | SuppApprUserCommentsPerformerId | PERFORMER_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
