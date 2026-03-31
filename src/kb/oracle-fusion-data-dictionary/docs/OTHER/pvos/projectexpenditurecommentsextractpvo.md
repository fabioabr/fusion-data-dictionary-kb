---
id: DOC-OTHER-PVO-ProjectExpenditureCommentsExtractPVO
doc_type: system-doc
title: "ProjectExpenditureCommentsExtractPVO — PVO Cross-Module"
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
  - ProjectExpenditureCommentsExtractPVO
  - projectexpenditurecommentsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectExpenditureCommentsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Expenditure Comments Extract. Acessa as tabelas: PJC_EXP_COMMENTS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.ProjectExpenditureCommentsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_exp_comments|PJC_EXP_COMMENTS]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjc_exp_comments|PJC_EXP_COMMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectExpenditureCommentsPE1CreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectExpenditureCommentsPE1CreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectExpenditureCommentsPE1ExpenditureComment | EXPENDITURE_COMMENT | — | ✅ |
| 4 | ProjectExpenditureCommentsPE1ExpenditureItemId | EXPENDITURE_ITEM_ID | 🔑 | ✅ |
| 5 | ProjectExpenditureCommentsPE1JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 6 | ProjectExpenditureCommentsPE1JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 7 | ProjectExpenditureCommentsPE1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ProjectExpenditureCommentsPE1LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ProjectExpenditureCommentsPE1LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ProjectExpenditureCommentsPE1LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 11 | ProjectExpenditureCommentsPE1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ProjectExpenditureCommentsPE1RequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
