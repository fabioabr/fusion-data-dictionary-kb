---
id: DOC-OTHER-PVO-OfferHiringManagerPVO
doc_type: system-doc
title: "OfferHiringManagerPVO — PVO Cross-Module"
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
  - OfferHiringManagerPVO
  - offerhiringmanagerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OfferHiringManagerPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Offer Hiring Manager. Acessa as tabelas: IRC_TEAM_MEMBERS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingCommonAM.OfferHiringManagerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 3 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[irc_team_members|IRC_TEAM_MEMBERS]] — 13 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[irc_team_members|IRC_TEAM_MEMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | MemberTypeCode | MEMBER_TYPE_CODE | — | — |
| 8 | ObjectId | OBJECT_ID | — | — |
| 9 | ObjectType | OBJECT_TYPE | — | — |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PersonId | PERSON_ID | — | — |
| 12 | TeamMemberEOCollaboratorRespTypeCode | COLLABORATOR_RESP_TYPE_CODE | — | — |
| 13 | TeamMemberId | TEAM_MEMBER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
