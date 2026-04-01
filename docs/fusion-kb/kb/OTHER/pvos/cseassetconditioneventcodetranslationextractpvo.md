---
id: DOC-OTHER-PVO-CseAssetConditionEventCodeTranslationExtractPVO
doc_type: system-doc
title: "CseAssetConditionEventCodeTranslationExtractPVO — PVO Cross-Module"
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
  - CseAssetConditionEventCodeTranslationExtractPVO
  - cseassetconditioneventcodetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CseAssetConditionEventCodeTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cse Asset Condition Event Code Translation Extract. Acessa as tabelas: CSE_CONDITION_EVENT_CODES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.CseAssetConditionEventCodeTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_condition_event_codes_tl|CSE_CONDITION_EVENT_CODES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cse_condition_event_codes_tl|CSE_CONDITION_EVENT_CODES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConditionEventCodeDesc | CONDITION_EVENT_CODE_DESC | — | ✅ |
| 2 | ConditionEventCodeId | CONDITION_EVENT_CODE_ID | 🔑 | ✅ |
| 3 | ConditionEventCodeName | CONDITION_EVENT_CODE_NAME | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
