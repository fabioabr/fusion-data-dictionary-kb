---
id: DOC-HCM-PVO-StatePVO
doc_type: system-doc
title: "StatePVO — PVO Human Capital Management"
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
  - StatePVO
  - statepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StatePVO

## 📌 Visão Geral

Disponibiliza estados configurados no fluxo de recrutamento com códigos e traduções. Define os status possíveis de candidatos e requisições no Oracle Recruiting.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingSetupAM.StatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 2 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[irc_states_b|IRC_STATES_B]] — 10 atributos (1 PKs, 10 BICC)
- [[irc_states_tl|IRC_STATES_TL]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[irc_states_b|IRC_STATES_B]]

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
| 9 | StateId | STATE_ID | 🔑 | ✅ |
| 10 | TypeCode | TYPE_CODE | — | ✅ |

### [[irc_states_tl|IRC_STATES_TL]]

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
| 11 | SourceLang | SOURCE_LANG | — | ✅ |
| 12 | StateId1 | STATE_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
