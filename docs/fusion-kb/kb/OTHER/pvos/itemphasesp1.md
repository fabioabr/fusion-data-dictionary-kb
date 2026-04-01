---
id: DOC-OTHER-PVO-ItemPhasesP1
doc_type: system-doc
title: "ItemPhasesP1 — PVO Cross-Module"
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
  - ItemPhasesP1
  - itemphasesp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemPhasesP1

## 📌 Visão Geral

View Object para extração BICC de dados de Item Phases P1. Acessa as tabelas: EGP_PHASES_B, EGP_PHASES_TL.

**Caminho:** `FscmTopModelAM.ItemClassesAM.ItemPhasesP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 2 | 2 | 15 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[egp_phases_b|EGP_PHASES_B]] — 11 atributos (1 PKs, 4 BICC)
- [[egp_phases_tl|EGP_PHASES_TL]] — 20 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[egp_phases_b|EGP_PHASES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhaseCode | PHASE_CODE | 🔑 | ✅ |
| 2 | PhasesBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | PhasesBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | PhasesBasePEOEndDate | END_DATE | — | — |
| 5 | PhasesBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PhasesBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | PhasesBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | PhasesBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | PhasesBasePEOPhaseSeq | PHASE_SEQ | — | ✅ |
| 10 | PhasesBasePEOPhaseType | PHASE_TYPE | — | ✅ |
| 11 | PhasesBasePEOStartDate | START_DATE | — | — |

### [[egp_phases_tl|EGP_PHASES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhasesTranPEO1CreatedBy | CREATED_BY | — | — |
| 2 | PhasesTranPEO1CreationDate | CREATION_DATE | — | — |
| 3 | PhasesTranPEO1Language | LANGUAGE | — | ✅ |
| 4 | PhasesTranPEO1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PhasesTranPEO1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | PhasesTranPEO1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | PhasesTranPEO1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | PhasesTranPEO1PhaseCode | PHASE_CODE | — | — |
| 9 | PhasesTranPEO1PhaseName | PHASE_NAME | — | ✅ |
| 10 | PhasesTranPEO1SourceLang | SOURCE_LANG | — | — |
| 11 | PhasesTranPEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | PhasesTranPEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | PhasesTranPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 14 | PhasesTranPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | PhasesTranPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | PhasesTranPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | PhasesTranPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | PhasesTranPEOPhaseCode | PHASE_CODE | — | ✅ |
| 19 | PhasesTranPEOPhaseName | PHASE_NAME | — | ✅ |
| 20 | PhasesTranPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
