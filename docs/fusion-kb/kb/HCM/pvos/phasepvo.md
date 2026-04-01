---
id: DOC-HCM-PVO-PhasePVO
doc_type: system-doc
title: "PhasePVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PhasePVO
  - phasepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PhasePVO

## 📌 Visão Geral

Extrai as fases dos processos de recrutamento (triagem, entrevista, oferta, etc.), com código e traduções. Dimensão de referência para o pipeline de seleção e contratação.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingSetupAM.PhasePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 2 | 2 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[irc_phases_b|IRC_PHASES_B]] — 11 atributos (1 PKs, 11 BICC)
- [[irc_phases_tl|IRC_PHASES_TL]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[irc_phases_b|IRC_PHASES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Code | CODE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ModuleId | MODULE_ID | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | PhaseId | PHASE_ID | 🔑 | ✅ |
| 10 | SequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 11 | TypeCode | TYPE_CODE | — | ✅ |

### [[irc_phases_tl|IRC_PHASES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy1 | CREATED_BY | — | ✅ |
| 2 | CreationDate1 | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | — | ✅ |
| 5 | Language1 | LANGUAGE | 🔑 | ✅ |
| 6 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 9 | Name | NAME | — | ✅ |
| 10 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PhaseId1 | PHASE_ID | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
