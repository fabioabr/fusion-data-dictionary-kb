---
id: DOC-AR-PVO-ReceivablesReconciliationParameterPVO
doc_type: system-doc
title: "ReceivablesReconciliationParameterPVO — PVO Accounts Receivable"
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
  - ReceivablesReconciliationParameterPVO
  - receivablesreconciliationparameterpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceivablesReconciliationParameterPVO

## 📌 Visão Geral

Extrai os parâmetros utilizados nas execuções de reconciliação de recebíveis, incluindo critérios de filtragem e responsável. Documenta a configuração de cada rodada de reconciliação para rastreabilidade e auditoria.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.ReceivablesReconciliationParameterPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 3 | 1 | 17 | 47% |

---

## 🔗 Tabelas Relacionadas

- [[ar_recon_summary_parameters|AR_RECON_SUMMARY_PARAMETERS]] — 26 atributos (1 PKs, 15 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (1 BICC)
- [[per_users|PER_USERS]] — 5 atributos (1 BICC)

---

## ⚙️ Atributos

### [[ar_recon_summary_parameters|AR_RECON_SUMMARY_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReconParamBalancingSegmentFrom | BALANCING_SEGMENT_FROM | — | ✅ |
| 2 | ReconParamBalancingSegmentTo | BALANCING_SEGMENT_TO | — | ✅ |
| 3 | ReconParamBuId | BU_ID | — | — |
| 4 | ReconParamCostCentreSegmentFrom | COST_CENTRE_SEGMENT_FROM | — | — |
| 5 | ReconParamCostCentreSegmentTo | COST_CENTRE_SEGMENT_TO | — | — |
| 6 | ReconParamCreatedBy | CREATED_BY | — | — |
| 7 | ReconParamCreationDate | CREATION_DATE | — | — |
| 8 | ReconParamIncludeIntercompanyTrx | INCLUDE_INTERCOMPANY_TRX | — | ✅ |
| 9 | ReconParamIncludeOnAccountItem | INCLUDE_ON_ACCOUNT_ITEM | — | ✅ |
| 10 | ReconParamIncludeUnappUnidReceipts | INCLUDE_UNAPP_UNID_RECEIPTS | — | ✅ |
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
| 21 | ReconParamPeriodEndDate | PERIOD_END_DATE | — | ✅ |
| 22 | ReconParamPeriodName | PERIOD_NAME | — | ✅ |
| 23 | ReconParamPeriodStartDate | PERIOD_START_DATE | — | ✅ |
| 24 | ReconParamRequestId | REQUEST_ID | — | ✅ |
| 25 | ReconParamRequestName | REQUEST_NAME | — | ✅ |
| 26 | ReconSummaryParamId | RECON_SUMMARY_PARAM_ID | 🔑 | ✅ |

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

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
