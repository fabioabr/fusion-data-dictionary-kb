---
id: DOC-OTHER-PVO-AssignmentDefinitionExtractPVO
doc_type: system-doc
title: "AssignmentDefinitionExtractPVO — PVO Cross-Module"
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
  - AssignmentDefinitionExtractPVO
  - assignmentdefinitionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssignmentDefinitionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Assignment Definition Extract. Acessa as tabelas: XLA_ASSIGNMENT_DEFNS_B, XLA_ASSIGNMENT_DEFNS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.AssignmentDefinitionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 4 | 25 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_assignment_defns_b|XLA_ASSIGNMENT_DEFNS_B]] — 13 atributos (4 PKs, 13 BICC)
- [[xla_assignment_defns_tl|XLA_ASSIGNMENT_DEFNS_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[xla_assignment_defns_b|XLA_ASSIGNMENT_DEFNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentDefinitionAssignmentCode | ASSIGNMENT_CODE | 🔑 | ✅ |
| 2 | AssignmentDefinitionAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 3 | AssignmentDefinitionAssignmentOwnerCode | ASSIGNMENT_OWNER_CODE | 🔑 | ✅ |
| 4 | AssignmentDefinitionCreatedBy | CREATED_BY | — | ✅ |
| 5 | AssignmentDefinitionCreationDate | CREATION_DATE | — | ✅ |
| 6 | AssignmentDefinitionEnabledFlag | ENABLED_FLAG | — | ✅ |
| 7 | AssignmentDefinitionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AssignmentDefinitionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | AssignmentDefinitionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | AssignmentDefinitionLedgerId | LEDGER_ID | — | ✅ |
| 11 | AssignmentDefinitionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | AssignmentDefinitionProgramCode | PROGRAM_CODE | 🔑 | ✅ |
| 13 | AssignmentDefinitionProgramOwnerCode | PROGRAM_OWNER_CODE | 🔑 | ✅ |

### [[xla_assignment_defns_tl|XLA_ASSIGNMENT_DEFNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentDefinitionTLAssignmentCode | ASSIGNMENT_CODE | — | ✅ |
| 2 | AssignmentDefinitionTLAssignmentOwnerCode | ASSIGNMENT_OWNER_CODE | — | ✅ |
| 3 | AssignmentDefinitionTLCreatedBy | CREATED_BY | — | ✅ |
| 4 | AssignmentDefinitionTLCreationDate | CREATION_DATE | — | ✅ |
| 5 | AssignmentDefinitionTLLanguage | LANGUAGE | — | ✅ |
| 6 | AssignmentDefinitionTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AssignmentDefinitionTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AssignmentDefinitionTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AssignmentDefinitionTLName | NAME | — | ✅ |
| 10 | AssignmentDefinitionTLProgramCode | PROGRAM_CODE | — | ✅ |
| 11 | AssignmentDefinitionTLProgramOwnerCode | PROGRAM_OWNER_CODE | — | ✅ |
| 12 | AssignmentDefinitionTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
