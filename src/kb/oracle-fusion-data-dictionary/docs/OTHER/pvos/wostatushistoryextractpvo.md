---
id: DOC-OTHER-PVO-WOStatusHistoryExtractPVO
doc_type: system-doc
title: "WOStatusHistoryExtractPVO — PVO Cross-Module"
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
  - WOStatusHistoryExtractPVO
  - wostatushistoryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOStatusHistoryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOStatus History Extract. Acessa as tabelas: WIE_WO_STATUS_HISTORY.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WieBiccExtractAM.WOStatusHistoryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wie_wo_status_history|WIE_WO_STATUS_HISTORY]] — 18 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[wie_wo_status_history|WIE_WO_STATUS_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOStatusHistoryPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | WOStatusHistoryPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WOStatusHistoryPEOCstInterfacedFlag | CST_INTERFACED_FLAG | — | ✅ |
| 4 | WOStatusHistoryPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 5 | WOStatusHistoryPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 6 | WOStatusHistoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | WOStatusHistoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | WOStatusHistoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | WOStatusHistoryPEONewStatusId | NEW_STATUS_ID | — | ✅ |
| 10 | WOStatusHistoryPEONextStatusId | NEXT_STATUS_ID | — | ✅ |
| 11 | WOStatusHistoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | WOStatusHistoryPEOOldStatusId | OLD_STATUS_ID | — | ✅ |
| 13 | WOStatusHistoryPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 14 | WOStatusHistoryPEOReason | REASON | — | ✅ |
| 15 | WOStatusHistoryPEORequestId | REQUEST_ID | — | ✅ |
| 16 | WOStatusHistoryPEOStatusChangeDate | STATUS_CHANGE_DATE | — | ✅ |
| 17 | WOStatusHistoryPEOWoStatusHistoryId | WO_STATUS_HISTORY_ID | 🔑 | ✅ |
| 18 | WOStatusHistoryPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
