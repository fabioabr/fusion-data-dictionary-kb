---
id: DOC-OTHER-PVO-MaintenanceProgramTranslationExtractPVO
doc_type: system-doc
title: "MaintenanceProgramTranslationExtractPVO — PVO Cross-Module"
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
  - MaintenanceProgramTranslationExtractPVO
  - maintenanceprogramtranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceProgramTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance Program Translation Extract. Acessa as tabelas: MNT_PROGRAMS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.MntBiccExtractAM.MaintenanceProgramTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_programs_tl|MNT_PROGRAMS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[mnt_programs_tl|MNT_PROGRAMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ProgramDescription | PROGRAM_DESCRIPTION | — | ✅ |
| 9 | ProgramId | PROGRAM_ID | 🔑 | ✅ |
| 10 | ProgramName | PROGRAM_NAME | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
