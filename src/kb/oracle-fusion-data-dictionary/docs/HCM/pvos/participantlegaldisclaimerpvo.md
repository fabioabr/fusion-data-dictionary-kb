---
id: DOC-HCM-PVO-ParticipantLegalDisclaimerPVO
doc_type: system-doc
title: "ParticipantLegalDisclaimerPVO — PVO Human Capital Management"
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
  - ParticipantLegalDisclaimerPVO
  - participantlegaldisclaimerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ParticipantLegalDisclaimerPVO

## 📌 Visão Geral

Disponibiliza textos de disclaimers legais associados a planos de benefícios por grupo empresarial. Base para gestão de conformidade jurídica no processo de enrollment.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.ParticipantLegalDisclaimerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ben_legal_disclaimer|BEN_LEGAL_DISCLAIMER]] — 18 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[ben_legal_disclaimer|BEN_LEGAL_DISCLAIMER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | DisclaimerText | DISCLAIMER_TEXT | — | ✅ |
| 6 | EndDate | END_DATE | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | LegalDisclaimerId | LEGAL_DISCLAIMER_ID | 🔑 | ✅ |
| 11 | LegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 12 | LerId | LER_ID | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | PgmId | PGM_ID | — | ✅ |
| 15 | PlId | PL_ID | — | ✅ |
| 16 | PlipId | PLIP_ID | — | ✅ |
| 17 | PtipId | PTIP_ID | — | ✅ |
| 18 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
