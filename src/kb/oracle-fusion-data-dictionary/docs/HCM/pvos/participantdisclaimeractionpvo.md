---
id: DOC-HCM-PVO-ParticipantDisclaimerActionPVO
doc_type: system-doc
title: "ParticipantDisclaimerActionPVO — PVO Human Capital Management"
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
  - ParticipantDisclaimerActionPVO
  - participantdisclaimeractionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ParticipantDisclaimerActionPVO

## 📌 Visão Geral

Extrai ações de aceite/recusa de disclaimers legais por participantes de planos de benefícios. Registra conformidade legal e consentimento no processo de inscrição em benefícios.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.ParticipantDisclaimerActionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 17 | 89% |

---

## 🔗 Tabelas Relacionadas

- [[ben_prtt_leg_discmr_actn|BEN_PRTT_LEG_DISCMR_ACTN]] — 19 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[ben_prtt_leg_discmr_actn|BEN_PRTT_LEG_DISCMR_ACTN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionTime | ACTION_TIME | — | ✅ |
| 2 | BenefitRelationId | BENEFIT_RELATION_ID | — | ✅ |
| 3 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | LegalDisclaimerId | LEGAL_DISCLAIMER_ID | — | ✅ |
| 10 | LegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 11 | LerId | LER_ID | — | ✅ |
| 12 | PerInLerId | PER_IN_LER_ID | — | ✅ |
| 13 | PersonId | PERSON_ID | — | ✅ |
| 14 | PgmId | PGM_ID | — | ✅ |
| 15 | PlId | PL_ID | — | ✅ |
| 16 | PlipId | PLIP_ID | — | — |
| 17 | PrttLegDiscmrActnId | PRTT_LEG_DISCMR_ACTN_ID | 🔑 | ✅ |
| 18 | PtipId | PTIP_ID | — | — |
| 19 | Status | STATUS | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
