---
id: DOC-OTHER-PVO-ProjectPeriodExceptionRootCausePVO
doc_type: system-doc
title: "ProjectPeriodExceptionRootCausePVO — PVO Cross-Module"
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
  - ProjectPeriodExceptionRootCausePVO
  - projectperiodexceptionrootcausepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectPeriodExceptionRootCausePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Period Exception Root Cause. Acessa as tabelas: PJC_BIP_REPORT_DETAILS.

**Caminho:** `FscmTopModelAM.PjfSetupPeriodExceptionsAM.ProjectPeriodExceptionRootCausePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 9 | 90% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_bip_report_details|PJC_BIP_REPORT_DETAILS]] — 10 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[pjc_bip_report_details|PJC_BIP_REPORT_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectPeriodExceptionPEOPrimaryMessageFlag | PRIMARY_MESSAGE_FLAG | — | ✅ |
| 2 | ProjectPeriodExceptionPEORcaMessageAdminAction | RCA_MESSAGE_ADMIN_ACTION | — | ✅ |
| 3 | ProjectPeriodExceptionPEORcaMessageAdminDetails | RCA_MESSAGE_ADMIN_DETAILS | — | ✅ |
| 4 | ProjectPeriodExceptionPEORcaMessageCause | RCA_MESSAGE_CAUSE | — | ✅ |
| 5 | ProjectPeriodExceptionPEORcaMessageName | RCA_MESSAGE_NAME | — | ✅ |
| 6 | ProjectPeriodExceptionPEORcaMessageText | RCA_MESSAGE_TEXT | — | ✅ |
| 7 | ProjectPeriodExceptionPEORcaMessageUserAction | RCA_MESSAGE_USER_ACTION | — | ✅ |
| 8 | ProjectPeriodExceptionPEORcaMessageUserDetails | RCA_MESSAGE_USER_DETAILS | — | ✅ |
| 9 | ProjectPeriodExceptionPEOSrcReportDetailId | SRC_REPORT_DETAIL_ID | — | — |
| 10 | ReportDetailId | REPORT_DETAIL_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
