---
id: DOC-HCM-120
doc_type: system-doc
title: "FND_CONSOLE_ISSUE — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - FND_CONSOLE_ISSUE
  - fnd_console_issue
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_CONSOLE_ISSUE

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ATTRIBUTE10_VARCHAR2 | — | — | — | — | — | — |
| 2 | ATTRIBUTE11_VARCHAR2 | — | — | — | — | — | — |
| 3 | ATTRIBUTE12_VARCHAR2 | — | — | — | — | — | — |
| 4 | ATTRIBUTE13_VARCHAR2 | — | — | — | — | — | — |
| 5 | ATTRIBUTE14_VARCHAR2 | — | — | — | — | — | — |
| 6 | ATTRIBUTE15_VARCHAR2 | — | — | — | — | — | — |
| 7 | ATTRIBUTE1_VARCHAR2 | — | — | — | — | — | — |
| 8 | ATTRIBUTE2_VARCHAR2 | — | — | — | — | — | — |
| 9 | ATTRIBUTE3_VARCHAR2 | — | — | — | — | — | — |
| 10 | ATTRIBUTE4_VARCHAR2 | — | — | — | — | — | — |
| 11 | ATTRIBUTE5_VARCHAR2 | — | — | — | — | — | — |
| 12 | ATTRIBUTE6_VARCHAR2 | — | — | — | — | — | — |
| 13 | ATTRIBUTE7_VARCHAR2 | — | — | — | — | — | — |
| 14 | ATTRIBUTE8_VARCHAR2 | — | — | — | — | — | — |
| 15 | ATTRIBUTE9_VARCHAR2 | — | — | — | — | — | — |
| 16 | ATTRIBUTE_CATEGORY | — | — | — | — | — | — |
| 17 | CONSOLE_TRANSACTION_ID | — | — | — | — | — | — |
| 18 | CREATED_BY | — | — | — | — | — | — |
| 19 | CREATION_DATE | — | — | — | — | — | — |
| 20 | ERROR_CODE | — | — | — | — | — | — |
| 21 | FAULT_CODE | — | — | — | — | — | — |
| 22 | FAULT_ID | — | — | — | — | — | — |
| 23 | FAULT_PAYLOAD | — | — | — | — | — | — |
| 24 | ISSUE_ACTION_CODE | — | — | — | — | — | — |
| 25 | ISSUE_ID | — | — | — | — | — | — |
| 26 | ISSUE_STATUS_CODE | — | — | — | — | — | — |
| 27 | ISSUE_TITLE | — | — | — | — | — | — |
| 28 | ISSUE_TYPE_CODE | — | — | — | — | — | — |
| 29 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 30 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 31 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[transactionconsolep1|TransactionConsoleP1]] (AP · BICC: 3/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE10_VARCHAR2 | FndConsoleIssuePEOAttribute10Varchar21 | — |
| ATTRIBUTE11_VARCHAR2 | FndConsoleIssuePEOAttribute11Varchar21 | — |
| ATTRIBUTE12_VARCHAR2 | FndConsoleIssuePEOAttribute12Varchar21 | — |
| ATTRIBUTE13_VARCHAR2 | FndConsoleIssuePEOAttribute13Varchar21 | — |
| ATTRIBUTE14_VARCHAR2 | FndConsoleIssuePEOAttribute14Varchar21 | — |
| ATTRIBUTE15_VARCHAR2 | FndConsoleIssuePEOAttribute15Varchar21 | — |
| ATTRIBUTE1_VARCHAR2 | FndConsoleIssuePEOAttribute1Varchar21 | — |
| ATTRIBUTE2_VARCHAR2 | FndConsoleIssuePEOAttribute2Varchar21 | — |
| ATTRIBUTE3_VARCHAR2 | FndConsoleIssuePEOAttribute3Varchar21 | — |
| ATTRIBUTE4_VARCHAR2 | FndConsoleIssuePEOAttribute4Varchar21 | — |
| ATTRIBUTE5_VARCHAR2 | FndConsoleIssuePEOAttribute5Varchar21 | — |
| ATTRIBUTE6_VARCHAR2 | FndConsoleIssuePEOAttribute6Varchar21 | — |
| ATTRIBUTE7_VARCHAR2 | FndConsoleIssuePEOAttribute7Varchar21 | — |
| ATTRIBUTE8_VARCHAR2 | FndConsoleIssuePEOAttribute8Varchar21 | — |
| ATTRIBUTE9_VARCHAR2 | FndConsoleIssuePEOAttribute9Varchar21 | — |
| ATTRIBUTE_CATEGORY | FndConsoleIssuePEOAttributeCategory2 | — |
| CONSOLE_TRANSACTION_ID | FndConsoleIssuePEOConsoleTransactionId1 | — |
| CREATED_BY | FndConsoleIssuePEOCreatedBy5 | — |
| CREATION_DATE | FndConsoleIssuePEOCreationDate3 | — |
| ERROR_CODE | FndConsoleIssuePEOErrorCode | — |
| FAULT_CODE | FndConsoleIssuePEOFaultCode | — |
| FAULT_ID | FndConsoleIssuePEOFaultId | — |
| FAULT_PAYLOAD | FndConsoleIssuePEOFaultPayload | — |
| ISSUE_ACTION_CODE | FndConsoleIssuePEOIssueActionCode | — |
| ISSUE_ID | FndConsoleIssuePEOIssueId | ✅ |
| ISSUE_STATUS_CODE | FndConsoleIssuePEOIssueStatusCode | ✅ |
| ISSUE_TITLE | FndConsoleIssuePEOIssueTitle | — |
| ISSUE_TYPE_CODE | FndConsoleIssuePEOIssueTypeCode | — |
| LAST_UPDATE_DATE | FndConsoleIssuePEOLastUpdateDate4 | ✅ |
| LAST_UPDATE_LOGIN | FndConsoleIssuePEOLastUpdateLogin4 | — |
| LAST_UPDATED_BY | FndConsoleIssuePEOLastUpdatedBy4 | — |
