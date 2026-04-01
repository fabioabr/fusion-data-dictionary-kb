---
id: DOC-OTHER-PVO-DefaultExpenditureTypesExtractPVO
doc_type: system-doc
title: "DefaultExpenditureTypesExtractPVO — PVO Cross-Module"
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
  - DefaultExpenditureTypesExtractPVO
  - defaultexpendituretypesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DefaultExpenditureTypesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Default Expenditure Types Extract. Acessa as tabelas: RCS_DEFAULT_EXPENDITURE_TYPES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.DefaultExpenditureTypesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[rcs_default_expenditure_types|RCS_DEFAULT_EXPENDITURE_TYPES]] — 9 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[rcs_default_expenditure_types|RCS_DEFAULT_EXPENDITURE_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | ExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ScmTransactionType | SCM_TRANSACTION_TYPE | — | ✅ |
| 9 | ScmTransactionTypeId | SCM_TRANSACTION_TYPE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
