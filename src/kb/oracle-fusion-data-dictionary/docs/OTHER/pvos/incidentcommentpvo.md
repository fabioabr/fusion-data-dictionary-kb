---
id: DOC-OTHER-PVO-IncidentCommentPVO
doc_type: system-doc
title: "IncidentCommentPVO — PVO Cross-Module"
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
  - IncidentCommentPVO
  - incidentcommentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IncidentCommentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Incident Comment. Acessa as tabelas: GTG_INCIDENT_COMMENT, PER_PERSON_NAMES_F_V, PER_USERS.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.IncidentCommentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 3 | 1 | 8 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[gtg_incident_comment|GTG_INCIDENT_COMMENT]] — 8 atributos (1 PKs, 7 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (1 BICC)
- [[per_users|PER_USERS]] — 5 atributos

---

## ⚙️ Atributos

### [[gtg_incident_comment|GTG_INCIDENT_COMMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IncidentCommentPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | IncidentCommentPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | IncidentCommentPEOId | ID | 🔑 | ✅ |
| 4 | IncidentCommentPEOIncId | INCIDENT_ID | — | — |
| 5 | IncidentCommentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | IncidentCommentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | IncidentCommentPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | IncidentCommentPEOUserComment | USER_COMMENT | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmntPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | CmntPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | CmntPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | CmntPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | CmntPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmntCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | CmntCreatedByPersonId | PERSON_ID | — | — |
| 3 | CmntCreatedByUserGuid | USER_GUID | — | — |
| 4 | CmntCreatedByUserId | USER_ID | — | — |
| 5 | CmntCreatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
