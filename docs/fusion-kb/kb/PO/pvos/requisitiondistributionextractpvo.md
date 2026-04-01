---
id: DOC-PO-PVO-RequisitionDistributionExtractPVO
doc_type: system-doc
title: "RequisitionDistributionExtractPVO — PVO Purchasing"
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
  - RequisitionDistributionExtractPVO
  - requisitiondistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequisitionDistributionExtractPVO

## 📌 Visão Geral

Extrai as distribuições contábeis de requisições para carga BICC, associando cada linha a centros de custo, contas e projetos. Essencial para controle orçamentário pré-compra.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PorBiccExtractAM.RequisitionDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 90 | 1 | 1 | 39 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[por_req_distributions_all|POR_REQ_DISTRIBUTIONS_ALL]] — 90 atributos (1 PKs, 39 BICC)

---

## ⚙️ Atributos

### [[por_req_distributions_all|POR_REQ_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountUserOverrideFlag | ACCOUNT_USER_OVERRIDE_FLAG | — | ✅ |
| 2 | Attribute1 | ATTRIBUTE1 | — | — |
| 3 | Attribute10 | ATTRIBUTE10 | — | — |
| 4 | Attribute11 | ATTRIBUTE11 | — | — |
| 5 | Attribute12 | ATTRIBUTE12 | — | — |
| 6 | Attribute13 | ATTRIBUTE13 | — | — |
| 7 | Attribute14 | ATTRIBUTE14 | — | — |
| 8 | Attribute15 | ATTRIBUTE15 | — | — |
| 9 | Attribute16 | ATTRIBUTE16 | — | — |
| 10 | Attribute17 | ATTRIBUTE17 | — | — |
| 11 | Attribute18 | ATTRIBUTE18 | — | — |
| 12 | Attribute19 | ATTRIBUTE19 | — | — |
| 13 | Attribute2 | ATTRIBUTE2 | — | — |
| 14 | Attribute20 | ATTRIBUTE20 | — | — |
| 15 | Attribute3 | ATTRIBUTE3 | — | — |
| 16 | Attribute4 | ATTRIBUTE4 | — | — |
| 17 | Attribute5 | ATTRIBUTE5 | — | — |
| 18 | Attribute6 | ATTRIBUTE6 | — | — |
| 19 | Attribute7 | ATTRIBUTE7 | — | — |
| 20 | Attribute8 | ATTRIBUTE8 | — | — |
| 21 | Attribute9 | ATTRIBUTE9 | — | — |
| 22 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 25 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 30 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 31 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 32 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 33 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 45 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 46 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 47 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 48 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 49 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 50 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 51 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 52 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 53 | BudgetDate | BUDGET_DATE | — | ✅ |
| 54 | CodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 55 | CreatedBy | CREATED_BY | — | ✅ |
| 56 | CreationDate | CREATION_DATE | — | ✅ |
| 57 | DistributionAmount | DISTRIBUTION_AMOUNT | — | ✅ |
| 58 | DistributionCurrencyAmount | DISTRIBUTION_CURRENCY_AMOUNT | — | ✅ |
| 59 | DistributionId | DISTRIBUTION_ID | 🔑 | ✅ |
| 60 | DistributionNumber | DISTRIBUTION_NUMBER | — | ✅ |
| 61 | DistributionQuantity | DISTRIBUTION_QUANTITY | — | ✅ |
| 62 | FundsStatus | FUNDS_STATUS | — | ✅ |
| 63 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 64 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 65 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 66 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 67 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 68 | NonrecoverableCurrencyTax | NONRECOVERABLE_CURRENCY_TAX | — | ✅ |
| 69 | NonrecoverableTax | NONRECOVERABLE_TAX | — | ✅ |
| 70 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 71 | PJC_BILLABLE_FLAG | PJC_BILLABLE_FLAG | — | ✅ |
| 72 | PJC_CAPITALIZABLE_FLAG | PJC_CAPITALIZABLE_FLAG | — | ✅ |
| 73 | PJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | ✅ |
| 74 | PJC_CONTRACT_ID | PJC_CONTRACT_ID | — | ✅ |
| 75 | PJC_CONTRACT_LINE_ID | PJC_CONTRACT_LINE_ID | — | ✅ |
| 76 | PJC_EXPENDITURE_ITEM_DATE | PJC_EXPENDITURE_ITEM_DATE | — | ✅ |
| 77 | PJC_EXPENDITURE_TYPE_ID | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 78 | PJC_FUNDING_ALLOCATION_ID | PJC_FUNDING_ALLOCATION_ID | — | ✅ |
| 79 | PJC_ORGANIZATION_ID | PJC_ORGANIZATION_ID | — | ✅ |
| 80 | PJC_PROJECT_ID | PJC_PROJECT_ID | — | ✅ |
| 81 | PJC_TASK_ID | PJC_TASK_ID | — | ✅ |
| 82 | PJC_WORK_TYPE_ID | PJC_WORK_TYPE_ID | — | ✅ |
| 83 | Percent | PERCENT | — | ✅ |
| 84 | PrimaryLedgerId | PRIMARY_LEDGER_ID | — | ✅ |
| 85 | RecoverableCurrencyTax | RECOVERABLE_CURRENCY_TAX | — | ✅ |
| 86 | RecoverableTax | RECOVERABLE_TAX | — | ✅ |
| 87 | ReqBuId | REQ_BU_ID | — | ✅ |
| 88 | RequestId | REQUEST_ID | — | ✅ |
| 89 | RequisitionLineId | REQUISITION_LINE_ID | — | ✅ |
| 90 | VarianceAccountId | VARIANCE_ACCOUNT_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
