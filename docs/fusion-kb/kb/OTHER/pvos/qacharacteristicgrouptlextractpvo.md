---
id: DOC-OTHER-PVO-QaCharacteristicGroupTLExtractPVO
doc_type: system-doc
title: "QaCharacteristicGroupTLExtractPVO — PVO Cross-Module"
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
  - QaCharacteristicGroupTLExtractPVO
  - qacharacteristicgrouptlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QaCharacteristicGroupTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Qa Characteristic Group TLExtract. Acessa as tabelas: QA_CS_GROUPS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.QaCharacteristicGroupTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[qa_cs_groups_tl|QA_CS_GROUPS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[qa_cs_groups_tl|QA_CS_GROUPS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CharacteristicGroupTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | CharacteristicGroupTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | CharacteristicGroupTLPEOCsGroupId | CS_GROUP_ID | 🔑 | ✅ |
| 4 | CharacteristicGroupTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | CharacteristicGroupTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | CharacteristicGroupTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CharacteristicGroupTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CharacteristicGroupTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CharacteristicGroupTLPEOName | NAME | — | ✅ |
| 10 | CharacteristicGroupTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
