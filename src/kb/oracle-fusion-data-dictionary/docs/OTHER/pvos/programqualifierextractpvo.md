---
id: DOC-OTHER-PVO-ProgramQualifierExtractPVO
doc_type: system-doc
title: "ProgramQualifierExtractPVO — PVO Cross-Module"
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
  - ProgramQualifierExtractPVO
  - programqualifierextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProgramQualifierExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Program Qualifier Extract. Acessa as tabelas: CJM_PROGRAM_QUALIFIERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ProgramQualifierExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_program_qualifiers|CJM_PROGRAM_QUALIFIERS]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[cjm_program_qualifiers|CJM_PROGRAM_QUALIFIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ComparisonOperatorCode | COMPARISON_OPERATOR_CODE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EndDate | END_DATE | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | MandatoryQualifier | MANDATORY_QUALIFIER | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ProgramHeaderId | PROGRAM_HEADER_ID | — | ✅ |
| 11 | ProgramQualifierId | PROGRAM_QUALIFIER_ID | 🔑 | ✅ |
| 12 | QualifierTypeCode | QUALIFIER_TYPE_CODE | — | ✅ |
| 13 | QualifierValueCode | QUALIFIER_VALUE_CODE | — | ✅ |
| 14 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
