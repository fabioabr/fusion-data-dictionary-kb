---
id: DOC-OTHER-PVO-PostAccountingProgramTLExtractPVO
doc_type: system-doc
title: "PostAccountingProgramTLExtractPVO — PVO Cross-Module"
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
  - PostAccountingProgramTLExtractPVO
  - postaccountingprogramtlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PostAccountingProgramTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Post Accounting Program TLExtract. Acessa as tabelas: XLA_POST_ACCT_PROGS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.PostAccountingProgramTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_post_acct_progs_tl|XLA_POST_ACCT_PROGS_TL]] — 12 atributos (3 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[xla_post_acct_progs_tl|XLA_POST_ACCT_PROGS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PostAccountingProgramTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | PostAccountingProgramTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | PostAccountingProgramTLDescription | DESCRIPTION | — | ✅ |
| 4 | PostAccountingProgramTLLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | PostAccountingProgramTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PostAccountingProgramTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PostAccountingProgramTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PostAccountingProgramTLName | NAME | — | ✅ |
| 9 | PostAccountingProgramTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PostAccountingProgramTLProgramCode | PROGRAM_CODE | 🔑 | ✅ |
| 11 | PostAccountingProgramTLProgramOwnerCode | PROGRAM_OWNER_CODE | 🔑 | ✅ |
| 12 | PostAccountingProgramTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
