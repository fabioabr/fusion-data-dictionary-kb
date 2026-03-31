---
id: DOC-OTHER-PVO-CmrPoSchedAccrualClrDtlsExtractPVO
doc_type: system-doc
title: "CmrPoSchedAccrualClrDtlsExtractPVO — PVO Cross-Module"
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
  - CmrPoSchedAccrualClrDtlsExtractPVO
  - cmrposchedaccrualclrdtlsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrPoSchedAccrualClrDtlsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Po Sched Accrual Clr Dtls Extract. Acessa as tabelas: CMR_PO_SCHED_ACCRUAL_CLR_DTLS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrPoSchedAccrualClrDtlsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 2 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_po_sched_accrual_clr_dtls|CMR_PO_SCHED_ACCRUAL_CLR_DTLS]] — 15 atributos (2 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[cmr_po_sched_accrual_clr_dtls|CMR_PO_SCHED_ACCRUAL_CLR_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrPoSchedAccrualClrDtlsPEOAccrualClearedDate | ACCRUAL_CLEARED_DATE | 🔑 | ✅ |
| 2 | CmrPoSchedAccrualClrDtlsPEOAccrualClearingAmount | ACCRUAL_CLEARING_AMOUNT | — | ✅ |
| 3 | CmrPoSchedAccrualClrDtlsPEOAccrualClearingStatus | ACCRUAL_CLEARING_STATUS | — | ✅ |
| 4 | CmrPoSchedAccrualClrDtlsPEOAccrualClrGroupId | ACCRUAL_CLR_GROUP_ID | — | ✅ |
| 5 | CmrPoSchedAccrualClrDtlsPEOAccrualClrRuleName | ACCRUAL_CLR_RULE_NAME | — | ✅ |
| 6 | CmrPoSchedAccrualClrDtlsPEOAccrualProcessedFlag | ACCRUAL_PROCESSED_FLAG | — | ✅ |
| 7 | CmrPoSchedAccrualClrDtlsPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 8 | CmrPoSchedAccrualClrDtlsPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 9 | CmrPoSchedAccrualClrDtlsPEOCmrPoLineLocationId | CMR_PO_LINE_LOCATION_ID | 🔑 | ✅ |
| 10 | CmrPoSchedAccrualClrDtlsPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | CmrPoSchedAccrualClrDtlsPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | CmrPoSchedAccrualClrDtlsPEODeliveryProcessedFlag | DELIVERY_PROCESSED_FLAG | — | ✅ |
| 13 | CmrPoSchedAccrualClrDtlsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | CmrPoSchedAccrualClrDtlsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | CmrPoSchedAccrualClrDtlsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
