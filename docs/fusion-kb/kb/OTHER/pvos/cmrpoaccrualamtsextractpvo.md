---
id: DOC-OTHER-PVO-CmrPoAccrualAmtsExtractPVO
doc_type: system-doc
title: "CmrPoAccrualAmtsExtractPVO — PVO Cross-Module"
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
  - CmrPoAccrualAmtsExtractPVO
  - cmrpoaccrualamtsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrPoAccrualAmtsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Po Accrual Amts Extract. Acessa as tabelas: CMR_PO_ACCRUAL_AMTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrPoAccrualAmtsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 3 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_po_accrual_amts|CMR_PO_ACCRUAL_AMTS]] — 16 atributos (3 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[cmr_po_accrual_amts|CMR_PO_ACCRUAL_AMTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrPoAccrualAmtsPEOAccrualAmt | ACCRUAL_AMT | — | ✅ |
| 2 | CmrPoAccrualAmtsPEOAccrualQty | ACCRUAL_QTY | — | ✅ |
| 3 | CmrPoAccrualAmtsPEOBillToBuId | BILL_TO_BU_ID | — | ✅ |
| 4 | CmrPoAccrualAmtsPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 5 | CmrPoAccrualAmtsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | 🔑 | ✅ |
| 6 | CmrPoAccrualAmtsPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | CmrPoAccrualAmtsPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | CmrPoAccrualAmtsPEOEncumbranceReversalEntrAmt | ENCUMBRANCE_REVERSAL_ENTR_AMT | — | ✅ |
| 9 | CmrPoAccrualAmtsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | CmrPoAccrualAmtsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | CmrPoAccrualAmtsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | CmrPoAccrualAmtsPEONonrecoverableTax | NONRECOVERABLE_TAX | — | ✅ |
| 13 | CmrPoAccrualAmtsPEOPeriodEndAccrualAdjDate | PERIOD_END_ACCRUAL_ADJ_DATE | — | ✅ |
| 14 | CmrPoAccrualAmtsPEORunId | RUN_ID | 🔑 | ✅ |
| 15 | CmrPoAccrualAmtsPEORunPeriodId | RUN_PERIOD_ID | 🔑 | ✅ |
| 16 | CmrPoAccrualAmtsPEOTaxExcludeAccrualAmount | TAX_EXCLUDE_ACCRUAL_AMOUNT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
