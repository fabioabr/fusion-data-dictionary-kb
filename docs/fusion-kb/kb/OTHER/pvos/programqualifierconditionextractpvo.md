---
id: DOC-OTHER-PVO-ProgramQualifierConditionExtractPVO
doc_type: system-doc
title: "ProgramQualifierConditionExtractPVO — PVO Cross-Module"
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
  - ProgramQualifierConditionExtractPVO
  - programqualifierconditionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProgramQualifierConditionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Program Qualifier Condition Extract. Acessa as tabelas: CJM_PROGRAM_CONDITIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ProgramQualifierConditionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_program_conditions|CJM_PROGRAM_CONDITIONS]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cjm_program_conditions|CJM_PROGRAM_CONDITIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ComparisonOperatorCode | COMPARISON_OPERATOR_CODE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ProgramQualifierId | PROGRAM_QUALIFIER_ID | — | ✅ |
| 9 | QualifierConditionId | QUALIFIER_CONDITION_ID | 🔑 | ✅ |
| 10 | QualifierTypeCode | QUALIFIER_TYPE_CODE | — | ✅ |
| 11 | QualifierValueCode | QUALIFIER_VALUE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
