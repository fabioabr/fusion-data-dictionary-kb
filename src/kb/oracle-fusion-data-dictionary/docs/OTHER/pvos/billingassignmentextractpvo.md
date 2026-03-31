---
id: DOC-OTHER-PVO-BillingAssignmentExtractPVO
doc_type: system-doc
title: "BillingAssignmentExtractPVO — PVO Cross-Module"
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
  - BillingAssignmentExtractPVO
  - billingassignmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillingAssignmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Billing Assignment Extract. Acessa as tabelas: PJB_BILLING_ASSIGNMENTS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.BillingAssignmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_billing_assignments|PJB_BILLING_ASSIGNMENTS]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[pjb_billing_assignments|PJB_BILLING_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillingAssignmentPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | BillingAssignmentPEOBillMethodId | BILL_METHOD_ID | — | ✅ |
| 3 | BillingAssignmentPEOBillingAssignmentId | BILLING_ASSIGNMENT_ID | 🔑 | ✅ |
| 4 | BillingAssignmentPEOBillingExtensionId | BILLING_EXTENSION_ID | — | ✅ |
| 5 | BillingAssignmentPEOConfigurationId | CONFIGURATION_ID | — | ✅ |
| 6 | BillingAssignmentPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | BillingAssignmentPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | BillingAssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | BillingAssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | BillingAssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | BillingAssignmentPEOMethodCfgType | METHOD_CFG_TYPE | — | ✅ |
| 12 | BillingAssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | BillingAssignmentPEOProcessingOrder | PROCESSING_ORDER | — | ✅ |
| 14 | BillingAssignmentPEOTransactionCode | TRANSACTION_CODE | — | ✅ |
| 15 | BillingAssignmentPEOTransactionDesc | TRANSACTION_DESC | — | ✅ |
| 16 | BillingAssignmentPEOTransactionType | TRANSACTION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
