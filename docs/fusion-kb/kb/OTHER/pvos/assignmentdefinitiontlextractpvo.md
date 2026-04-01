---
id: DOC-OTHER-PVO-AssignmentDefinitionTLExtractPVO
doc_type: system-doc
title: "AssignmentDefinitionTLExtractPVO — PVO Cross-Module"
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
  - AssignmentDefinitionTLExtractPVO
  - assignmentdefinitiontlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssignmentDefinitionTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Assignment Definition TLExtract. Acessa as tabelas: XLA_ASSIGNMENT_DEFNS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.AssignmentDefinitionTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 5 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_assignment_defns_tl|XLA_ASSIGNMENT_DEFNS_TL]] — 13 atributos (5 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[xla_assignment_defns_tl|XLA_ASSIGNMENT_DEFNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentDefinitionTLAssignmentCode | ASSIGNMENT_CODE | 🔑 | ✅ |
| 2 | AssignmentDefinitionTLAssignmentOwnerCode | ASSIGNMENT_OWNER_CODE | 🔑 | ✅ |
| 3 | AssignmentDefinitionTLCreatedBy | CREATED_BY | — | ✅ |
| 4 | AssignmentDefinitionTLCreationDate | CREATION_DATE | — | ✅ |
| 5 | AssignmentDefinitionTLLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | AssignmentDefinitionTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AssignmentDefinitionTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AssignmentDefinitionTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AssignmentDefinitionTLName | NAME | — | ✅ |
| 10 | AssignmentDefinitionTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | AssignmentDefinitionTLProgramCode | PROGRAM_CODE | 🔑 | ✅ |
| 12 | AssignmentDefinitionTLProgramOwnerCode | PROGRAM_OWNER_CODE | 🔑 | ✅ |
| 13 | AssignmentDefinitionTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
