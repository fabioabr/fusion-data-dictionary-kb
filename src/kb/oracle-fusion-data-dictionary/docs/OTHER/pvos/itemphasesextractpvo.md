---
id: DOC-OTHER-PVO-ItemPhasesExtractPVO
doc_type: system-doc
title: "ItemPhasesExtractPVO — PVO Cross-Module"
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
  - ItemPhasesExtractPVO
  - itemphasesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemPhasesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Phases Extract. Acessa as tabelas: EGP_PHASES_B, EGP_PHASES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.ItemPhasesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 2 | 1 | 10 | 77% |

---

## 🔗 Tabelas Relacionadas

- [[egp_phases_b|EGP_PHASES_B]] — 10 atributos (1 PKs, 10 BICC)
- [[egp_phases_tl|EGP_PHASES_TL]] — 3 atributos

---

## ⚙️ Atributos

### [[egp_phases_b|EGP_PHASES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhasesBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PhasesBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PhasesBasePEOEndDate | END_DATE | — | ✅ |
| 4 | PhasesBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PhasesBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | PhasesBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | PhasesBasePEOPhaseCode | PHASE_CODE | 🔑 | ✅ |
| 8 | PhasesBasePEOPhaseSeq | PHASE_SEQ | — | ✅ |
| 9 | PhasesBasePEOPhaseType | PHASE_TYPE | — | ✅ |
| 10 | PhasesBasePEOStartDate | START_DATE | — | ✅ |

### [[egp_phases_tl|EGP_PHASES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhasesTranPEOLanguage | LANGUAGE | — | — |
| 2 | PhasesTranPEOPhaseCode | PHASE_CODE | — | — |
| 3 | PhasesTranPEOPhaseName | PHASE_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
