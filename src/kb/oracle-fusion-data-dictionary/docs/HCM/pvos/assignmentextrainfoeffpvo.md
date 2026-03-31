---
id: DOC-HCM-PVO-AssignmentExtraInfoEFFPVO
doc_type: system-doc
title: "AssignmentExtraInfoEFFPVO — PVO Human Capital Management"
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
aliases:
  - AssignmentExtraInfoEFFPVO
  - assignmentextrainfoeffpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssignmentExtraInfoEFFPVO

## 📌 Visão Geral

Extrai informacoes extras de assignment com campos extensiveis (EFF). Suporta dados customizados por legislacao ou necessidade especifica do cliente.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AssignmentAM.AssignmentExtraInfoEFFPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 0 | 0 | 0% |

---

## 🔗 Tabelas Relacionadas

- [[per_assignment_extra_info_m|PER_ASSIGNMENT_EXTRA_INFO_M]] — 16 atributos

---

## ⚙️ Atributos

### [[per_assignment_extra_info_m|PER_ASSIGNMENT_EXTRA_INFO_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | AeiInformationCategory | AEI_INFORMATION_CATEGORY | — | — |
| 3 | AssignmentExtraInfoId | ASSIGNMENT_EXTRA_INFO_ID | — | — |
| 4 | AssignmentId | ASSIGNMENT_ID | — | — |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreationDate | CREATION_DATE | — | — |
| 7 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | EffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 9 | EffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 10 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 11 | InformationType | INFORMATION_TYPE | — | — |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | LegislationCode | LEGISLATION_CODE | — | — |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
