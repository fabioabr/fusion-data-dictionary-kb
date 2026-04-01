---
id: DOC-AP-PVO-ConsoleIssueFaultDetailsP1
doc_type: system-doc
title: "ConsoleIssueFaultDetailsP1 — PVO Accounts Payable"
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
  - ConsoleIssueFaultDetailsP1
  - consoleissuefaultdetailsp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ConsoleIssueFaultDetailsP1

## 📌 Visão Geral

Extrai os detalhes de erros e falhas identificados em transações no console de RH, incluindo descrição técnica do problema. Essencial para diagnóstico de falhas operacionais, análise de causa raiz e melhoria contínua dos processos de gestão de pessoas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmApprovalsReportingAM.ConsoleIssueFaultDetailsP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 6 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[hrc_console_fault_details_vl|HRC_CONSOLE_FAULT_DETAILS_VL]] — 17 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[hrc_console_fault_details_vl|HRC_CONSOLE_FAULT_DETAILS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConsoleIssueFaultDetailsPEOCreatedBy | CREATED_BY | — | — |
| 2 | ConsoleIssueFaultDetailsPEOCreationDate | CREATION_DATE | — | — |
| 3 | ConsoleIssueFaultDetailsPEODescription | DESCRIPTION | — | ✅ |
| 4 | ConsoleIssueFaultDetailsPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | ConsoleIssueFaultDetailsPEOErrorCode | ERROR_CODE | — | — |
| 6 | ConsoleIssueFaultDetailsPEOFaultCode | FAULT_CODE | — | — |
| 7 | ConsoleIssueFaultDetailsPEOFaultDetailsId | FAULT_DETAILS_ID | 🔑 | ✅ |
| 8 | ConsoleIssueFaultDetailsPEOIssueTitle | ISSUE_TITLE | — | ✅ |
| 9 | ConsoleIssueFaultDetailsPEOIssueType | ISSUE_TYPE | — | ✅ |
| 10 | ConsoleIssueFaultDetailsPEOIssueTypeCode | ISSUE_TYPE_CODE | — | — |
| 11 | ConsoleIssueFaultDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ConsoleIssueFaultDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | ConsoleIssueFaultDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | ConsoleIssueFaultDetailsPEOModuleId | MODULE_ID | — | — |
| 15 | ConsoleIssueFaultDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | ConsoleIssueFaultDetailsPEOResolution | RESOLUTION | — | ✅ |
| 17 | ConsoleIssueFaultDetailsPEOSguid | SGUID | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
