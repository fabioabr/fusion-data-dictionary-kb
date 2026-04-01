---
id: DOC-AP-PVO-ConsoleIssueCommentsP2
doc_type: system-doc
title: "ConsoleIssueCommentsP2 — PVO Accounts Payable"
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
  - ConsoleIssueCommentsP2
  - consoleissuecommentsp2
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ConsoleIssueCommentsP2

## 📌 Visão Geral

Extrai os comentários registrados em ocorrências do console de transações de RH. Permite rastrear o histórico de comunicação e decisões tomadas durante a resolução de problemas em transações de gestão de pessoas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmApprovalsReportingAM.ConsoleIssueCommentsP2`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 2 | 5 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[hrc_console_issue_comments|HRC_CONSOLE_ISSUE_COMMENTS]] — 15 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[hrc_console_issue_comments|HRC_CONSOLE_ISSUE_COMMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConsoleIssueCommentsPEOCommentSequence | COMMENT_SEQUENCE | 🔑 | ✅ |
| 2 | ConsoleIssueCommentsPEOComments | COMMENTS | — | ✅ |
| 3 | ConsoleIssueCommentsPEOConsoleTransactionId | CONSOLE_TRANSACTION_ID | — | — |
| 4 | ConsoleIssueCommentsPEOCreatedBy | CREATED_BY | — | — |
| 5 | ConsoleIssueCommentsPEOCreationDate | CREATION_DATE | — | — |
| 6 | ConsoleIssueCommentsPEODateTime | DATE_TIME | — | — |
| 7 | ConsoleIssueCommentsPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 8 | ConsoleIssueCommentsPEOIssueCommentId | ISSUE_COMMENT_ID | 🔑 | ✅ |
| 9 | ConsoleIssueCommentsPEOIssueId | ISSUE_ID | — | — |
| 10 | ConsoleIssueCommentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | ConsoleIssueCommentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | ConsoleIssueCommentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | ConsoleIssueCommentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | ConsoleIssueCommentsPEOTransactionId | TRANSACTION_ID | — | — |
| 15 | ConsoleIssueCommentsPEOUserName | USER_NAME | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
