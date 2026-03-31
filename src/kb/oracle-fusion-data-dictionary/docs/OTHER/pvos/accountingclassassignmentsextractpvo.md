---
id: DOC-OTHER-PVO-AccountingClassAssignmentsExtractPVO
doc_type: system-doc
title: "AccountingClassAssignmentsExtractPVO — PVO Cross-Module"
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
  - AccountingClassAssignmentsExtractPVO
  - accountingclassassignmentsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AccountingClassAssignmentsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Accounting Class Assignments Extract. Acessa as tabelas: XLA_ACCT_CLASS_ASSGNS.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.AccountingClassAssignmentsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 5 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_acct_class_assgns|XLA_ACCT_CLASS_ASSGNS]] — 11 atributos (5 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[xla_acct_class_assgns|XLA_ACCT_CLASS_ASSGNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountingClassAssignmentAccountingClassCode | ACCOUNTING_CLASS_CODE | 🔑 | ✅ |
| 2 | AccountingClassAssignmentCode | ASSIGNMENT_CODE | 🔑 | ✅ |
| 3 | AccountingClassAssignmentCreatedBy | CREATED_BY | — | ✅ |
| 4 | AccountingClassAssignmentCreationDate | CREATION_DATE | — | ✅ |
| 5 | AccountingClassAssignmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AccountingClassAssignmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | AccountingClassAssignmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | AccountingClassAssignmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | AccountingClassAssignmentOwnerCode | ASSIGNMENT_OWNER_CODE | 🔑 | ✅ |
| 10 | AccountingClassAssignmentProgramCode | PROGRAM_CODE | 🔑 | ✅ |
| 11 | AccountingClassAssignmentProgramOwnerCode | PROGRAM_OWNER_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
