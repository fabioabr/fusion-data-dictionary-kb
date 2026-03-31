---
id: DOC-OTHER-PVO-ItemPhasesTranslationExtractPVO
doc_type: system-doc
title: "ItemPhasesTranslationExtractPVO — PVO Cross-Module"
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
  - ItemPhasesTranslationExtractPVO
  - itemphasestranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemPhasesTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Phases Translation Extract. Acessa as tabelas: EGP_PHASES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.ItemPhasesTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_phases_tl|EGP_PHASES_TL]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[egp_phases_tl|EGP_PHASES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhasesTranPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PhasesTranPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PhasesTranPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | PhasesTranPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PhasesTranPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | PhasesTranPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | PhasesTranPEOPhaseCode | PHASE_CODE | 🔑 | ✅ |
| 8 | PhasesTranPEOPhaseName | PHASE_NAME | — | ✅ |
| 9 | PhasesTranPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
