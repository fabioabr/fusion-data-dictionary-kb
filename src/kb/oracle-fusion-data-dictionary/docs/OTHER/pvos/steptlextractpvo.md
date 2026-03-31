---
id: DOC-OTHER-PVO-StepTLExtractPVO
doc_type: system-doc
title: "StepTLExtractPVO — PVO Cross-Module"
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
  - StepTLExtractPVO
  - steptlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StepTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Step TLExtract. Acessa as tabelas: DOO_PROCESS_STEPS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.StepTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_process_steps_tl|DOO_PROCESS_STEPS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[doo_process_steps_tl|DOO_PROCESS_STEPS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurrentStepTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | CurrentStepTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | CurrentStepTranslationId | STEP_ID | 🔑 | ✅ |
| 4 | CurrentStepTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | CurrentStepTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | CurrentStepTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | CurrentStepTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | CurrentStepTranslationName | STEP_NAME | — | ✅ |
| 9 | CurrentStepTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | CurrentStepTranslationSourceLang | SOURCE_LANG | — | ✅ |
| 11 | CurrentStepTranslationSplitUnitDisplayName | SPLIT_UNIT_DISPLAY_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
