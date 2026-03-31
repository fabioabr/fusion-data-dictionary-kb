---
id: DOC-AP-PVO-PayablesReconciliationParameterPVO
doc_type: system-doc
title: "PayablesReconciliationParameterPVO — PVO Accounts Payable"
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
  - PayablesReconciliationParameterPVO
  - payablesreconciliationparameterpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PayablesReconciliationParameterPVO

## 📌 Visão Geral

Extrai os parâmetros de execução das reconciliações de contas a pagar, incluindo critérios de filtro, usuário responsável e data de execução. Permite rastrear e auditar as rodadas de reconciliação realizadas no módulo AP.

**Caminho:** `FscmTopModelAM.FinApReportsReconciliationAM.PayablesReconciliationParameterPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 3 | 1 | 16 | 46% |

---

## 🔗 Tabelas Relacionadas

- [[ap_recon_summary_parameters|AP_RECON_SUMMARY_PARAMETERS]] — 25 atributos (1 PKs, 14 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (1 BICC)
- [[per_users|PER_USERS]] — 5 atributos (1 BICC)

---

## ⚙️ Atributos

### [[ap_recon_summary_parameters|AP_RECON_SUMMARY_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReconParamBalancingSegmentFrom | BALANCING_SEGMENT_FROM | — | ✅ |
| 2 | ReconParamBalancingSegmentTo | BALANCING_SEGMENT_TO | — | ✅ |
| 3 | ReconParamBuId | BU_ID | — | — |
| 4 | ReconParamCostCentreSegmentFrom | COST_CENTRE_SEGMENT_FROM | — | — |
| 5 | ReconParamCostCentreSegmentTo | COST_CENTRE_SEGMENT_TO | — | — |
| 6 | ReconParamCreatedBy | CREATED_BY | — | — |
| 7 | ReconParamCreationDate | CREATION_DATE | — | — |
| 8 | ReconParamEndDate | END_DATE | — | ✅ |
| 9 | ReconParamIncludeBillsPayable | INCLUDE_BILLS_PAYABLE | — | ✅ |
| 10 | ReconParamIncludeIntercompanyTrx | INCLUDE_INTERCOMPANY_TRX | — | ✅ |
| 11 | ReconParamIntercompanySegmentFrom | INTERCOMPANY_SEGMENT_FROM | — | — |
| 12 | ReconParamIntercompanySegmentTo | INTERCOMPANY_SEGMENT_TO | — | — |
| 13 | ReconParamJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 14 | ReconParamJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 15 | ReconParamLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | ReconParamLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | ReconParamLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | ReconParamLedgerId | LEDGER_ID | — | — |
| 19 | ReconParamNaturalAccountSegmentFrom | NATURAL_ACCOUNT_SEGMENT_FROM | — | ✅ |
| 20 | ReconParamNaturalAccountSegmentTo | NATURAL_ACCOUNT_SEGMENT_TO | — | ✅ |
| 21 | ReconParamPeriodName | PERIOD_NAME | — | ✅ |
| 22 | ReconParamRequestId | REQUEST_ID | — | ✅ |
| 23 | ReconParamRequestName | REQUEST_NAME | — | ✅ |
| 24 | ReconParamStartDate | START_DATE | — | ✅ |
| 25 | ReconSummaryParamId | RECON_SUMMARY_PARAM_ID | 🔑 | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UpdatedByPersonNameDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | UpdatedByPersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | UpdatedByPersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | UpdatedByPersonNamePersonId | PERSON_ID | — | — |
| 5 | UpdatedByPersonNamePersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UpdatedByPersonNameObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UpdatedByUserPersonId | PERSON_ID | — | — |
| 3 | UpdatedByUserUserGuid | USER_GUID | — | — |
| 4 | UpdatedByUserUserId | USER_ID | — | — |
| 5 | UpdatedByUserUsername | USERNAME | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
