---
id: DOC-OTHER-PVO-CharactersticTLPVO
doc_type: system-doc
title: "CharactersticTLPVO — PVO Cross-Module"
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
  - CharactersticTLPVO
  - characterstictlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CharactersticTLPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Characterstic TL. Acessa as tabelas: QA_CHARACTERISTICS_TL.

**Caminho:** `FscmTopModelAM.InspectionPlansAM.CharactersticTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 5 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[qa_characteristics_tl|QA_CHARACTERISTICS_TL]] — 11 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[qa_characteristics_tl|QA_CHARACTERISTICS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QaCharacteristicRptTLPEOCharacteristicId | CHARACTERISTIC_ID | 🔑 | ✅ |
| 2 | QaCharacteristicRptTLPEOCreatedBy | CREATED_BY | — | — |
| 3 | QaCharacteristicRptTLPEOCreationDate | CREATION_DATE | — | — |
| 4 | QaCharacteristicRptTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | QaCharacteristicRptTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | QaCharacteristicRptTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | QaCharacteristicRptTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | QaCharacteristicRptTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | QaCharacteristicRptTLPEOName | NAME | — | ✅ |
| 10 | QaCharacteristicRptTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | QaCharacteristicRptTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
