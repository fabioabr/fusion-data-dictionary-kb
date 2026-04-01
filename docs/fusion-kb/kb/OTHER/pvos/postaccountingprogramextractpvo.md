---
id: DOC-OTHER-PVO-PostAccountingProgramExtractPVO
doc_type: system-doc
title: "PostAccountingProgramExtractPVO — PVO Cross-Module"
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
  - PostAccountingProgramExtractPVO
  - postaccountingprogramextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PostAccountingProgramExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Post Accounting Program Extract. Acessa as tabelas: XLA_POST_ACCT_PROGS_B, XLA_POST_ACCT_PROGS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.PostAccountingProgramExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 2 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_post_acct_progs_b|XLA_POST_ACCT_PROGS_B]] — 9 atributos (2 PKs, 9 BICC)
- [[xla_post_acct_progs_tl|XLA_POST_ACCT_PROGS_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[xla_post_acct_progs_b|XLA_POST_ACCT_PROGS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PostAccountingProgramApplicationId | APPLICATION_ID | — | ✅ |
| 2 | PostAccountingProgramCode | PROGRAM_CODE | 🔑 | ✅ |
| 3 | PostAccountingProgramCreatedBy | CREATED_BY | — | ✅ |
| 4 | PostAccountingProgramCreationDate | CREATION_DATE | — | ✅ |
| 5 | PostAccountingProgramLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PostAccountingProgramLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PostAccountingProgramLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PostAccountingProgramObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | PostAccountingProgramOwnerCode | PROGRAM_OWNER_CODE | 🔑 | ✅ |

### [[xla_post_acct_progs_tl|XLA_POST_ACCT_PROGS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PostAccountingProgramTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | PostAccountingProgramTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | PostAccountingProgramTLDescription | DESCRIPTION | — | ✅ |
| 4 | PostAccountingProgramTLLanguage | LANGUAGE | — | ✅ |
| 5 | PostAccountingProgramTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PostAccountingProgramTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PostAccountingProgramTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PostAccountingProgramTLName | NAME | — | ✅ |
| 9 | PostAccountingProgramTLProgramCode | PROGRAM_CODE | — | ✅ |
| 10 | PostAccountingProgramTLProgramOwnerCode | PROGRAM_OWNER_CODE | — | ✅ |
| 11 | PostAccountingProgramTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
