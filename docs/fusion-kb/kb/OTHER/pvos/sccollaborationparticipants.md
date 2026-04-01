---
id: DOC-OTHER-PVO-SCCollaborationParticipants
doc_type: system-doc
title: "SCCollaborationParticipants — PVO Cross-Module"
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
  - SCCollaborationParticipants
  - sccollaborationparticipants
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SCCollaborationParticipants

## 📌 Visão Geral

View Object para extração BICC de dados de SCCollaboration Participants. Acessa as tabelas: VCS_PARTICIPANTS.

**Caminho:** `FscmTopModelAM.SupplyCollaborationAM.SCCollaborationParticipants`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 4 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_participants|VCS_PARTICIPANTS]] — 13 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[vcs_participants|VCS_PARTICIPANTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SCCollaborationParticipantsPEOCreatedBy | CREATED_BY | — | — |
| 2 | SCCollaborationParticipantsPEOCreationDate | CREATION_DATE | — | — |
| 3 | SCCollaborationParticipantsPEOCustomerId | CUSTOMER_ID | — | — |
| 4 | SCCollaborationParticipantsPEOCustomerSiteId | CUSTOMER_SITE_ID | — | — |
| 5 | SCCollaborationParticipantsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SCCollaborationParticipantsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | SCCollaborationParticipantsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | SCCollaborationParticipantsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SCCollaborationParticipantsPEOOrganizationId | ORGANIZATION_ID | — | — |
| 10 | SCCollaborationParticipantsPEOPartnerCode | PARTNER_CODE | — | — |
| 11 | SCCollaborationParticipantsPEOVendorId | VENDOR_ID | — | ✅ |
| 12 | SCCollaborationParticipantsPEOVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 13 | VcsParticipantId | VCS_PARTICIPANT_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
