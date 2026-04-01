---
id: DOC-PO-PVO-NegotiationCollaborationTeamExtractPVO
doc_type: system-doc
title: "NegotiationCollaborationTeamExtractPVO — PVO Purchasing"
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
  - NegotiationCollaborationTeamExtractPVO
  - negotiationcollaborationteamextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationCollaborationTeamExtractPVO

## 📌 Visão Geral

Extrai membros das equipes de colaboração em negociações para carga BICC, com funções e permissões. Alimenta análises de participação e carga de trabalho das equipes de sourcing.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationCollaborationTeamExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 2 | 19 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_neg_team_members|PON_NEG_TEAM_MEMBERS]] — 19 atributos (2 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[pon_neg_team_members|PON_NEG_TEAM_MEMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessType | ACCESS_TYPE | — | ✅ |
| 2 | ApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 3 | ApproverFlag | APPROVER_FLAG | — | ✅ |
| 4 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 5 | CompletionDate | COMPLETION_DATE | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | LastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | ✅ |
| 9 | LastNotifiedDate | LAST_NOTIFIED_DATE | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | MemberType | MEMBER_TYPE | — | ✅ |
| 14 | ModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 15 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | PersonId | PERSON_ID | — | ✅ |
| 17 | SequenceNumber | SEQUENCE_NUMBER | 🔑 | ✅ |
| 18 | TargetDate | TARGET_DATE | — | ✅ |
| 19 | TaskName | TASK_NAME | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
