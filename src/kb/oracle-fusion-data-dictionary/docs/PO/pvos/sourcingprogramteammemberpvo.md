---
id: DOC-PO-PVO-SourcingProgramTeamMemberPVO
doc_type: system-doc
title: "SourcingProgramTeamMemberPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SourcingProgramTeamMemberPVO
  - sourcingprogramteammemberpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourcingProgramTeamMemberPVO

## 📌 Visão Geral

Extrai os membros das equipes de programas de sourcing, com funções e responsabilidades atribuídas. Permite análise de alocação de recursos e governança dos programas de compras.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.SourcingProgramTeamMemberPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 1 | 2 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos (1 BICC)
- [[pon_program_team_members|PON_PROGRAM_TEAM_MEMBERS]] — 12 atributos (1 PKs, 1 BICC)

---

## ⚙️ Atributos

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgramTeamMemberNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | ProgramTeamMemberNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ProgramTeamMemberNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | ProgramTeamMemberNamePEOFullName | FULL_NAME | — | — |
| 5 | ProgramTeamMemberNamePEOListName | LIST_NAME | — | — |
| 6 | ProgramTeamMemberNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | ProgramTeamMemberNamePEOPersonId | PERSON_ID | — | — |
| 8 | ProgramTeamMemberNamePEOPersonNameId | PERSON_NAME_ID | — | — |

### [[pon_program_team_members|PON_PROGRAM_TEAM_MEMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgramTeamMemberPEOAccessType | ACCESS_TYPE | — | ✅ |
| 2 | ProgramTeamMemberPEOCreatedBy | CREATED_BY | — | — |
| 3 | ProgramTeamMemberPEOCreationDate | CREATION_DATE | — | — |
| 4 | ProgramTeamMemberPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | ProgramTeamMemberPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ProgramTeamMemberPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ProgramTeamMemberPEOMemberType | MEMBER_TYPE | — | — |
| 8 | ProgramTeamMemberPEONote | NOTE | — | — |
| 9 | ProgramTeamMemberPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ProgramTeamMemberPEOPersonId | PERSON_ID | — | — |
| 11 | ProgramTeamMemberPEOProgramHeaderId | PROGRAM_HEADER_ID | — | — |
| 12 | ProgramTeamMemberPEOTeamMemberId | TEAM_MEMBER_ID | 🔑 | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
