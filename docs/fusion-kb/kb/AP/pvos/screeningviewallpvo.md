---
id: DOC-AP-PVO-ScreeningViewAllPVO
doc_type: system-doc
title: "ScreeningViewAllPVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ScreeningViewAllPVO
  - screeningviewallpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ScreeningViewAllPVO

## 📌 Visão Geral

Extrai a visão consolidada de screenings (verificações de antecedentes) de candidatos, incluindo solicitação, resultado, candidatura e oferta. Permite monitorar todo o ciclo de verificação de antecedentes e tomar decisões de contratação informadas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecBackgroundCheckAM.ScreeningViewAllPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 10 | 1 | 32 | 70% |

---

## 🔗 Tabelas Relacionadas

- [[irc_bc_cand_results|IRC_BC_CAND_RESULTS]] — 14 atributos (13 BICC)
- [[irc_bc_cand_screenings|IRC_BC_CAND_SCREENINGS]] — 13 atributos (1 PKs, 11 BICC)
- [[irc_offers|IRC_OFFERS]] — 1 atributos
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 2 atributos (1 BICC)
- [[irc_submissions|IRC_SUBMISSIONS]] — 4 atributos (2 BICC)
- [[irc_tp_partners|IRC_TP_PARTNERS]] — 2 atributos (2 BICC)
- [[irc_tp_partner_accounts|IRC_TP_PARTNER_ACCOUNTS]] — 2 atributos (1 BICC)
- [[irc_tp_partner_provisngs|IRC_TP_PARTNER_PROVISNGS]] — 1 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (2 BICC)
- [[per_users|PER_USERS]] — 3 atributos

---

## ⚙️ Atributos

### [[irc_bc_cand_results|IRC_BC_CAND_RESULTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScreeningResultPEOAccountId | ACCOUNT_ID | — | ✅ |
| 2 | ScreeningResultPEOBcErrorDesc | BC_ERROR_DESC | — | ✅ |
| 3 | ScreeningResultPEOBcStatusCode | BC_STATUS_CODE | — | ✅ |
| 4 | ScreeningResultPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | ScreeningResultPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | ScreeningResultPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ScreeningResultPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ScreeningResultPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ScreeningResultPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ScreeningResultPEOProvisioningId | PROVISIONING_ID | — | ✅ |
| 11 | ScreeningResultPEORequestDate | REQUEST_DATE | — | ✅ |
| 12 | ScreeningResultPEORequestedBy | REQUESTED_BY | — | ✅ |
| 13 | ScreeningResultPEOResultId | RESULT_ID | — | ✅ |
| 14 | ScreeningResultPEOSubmissionId | SUBMISSION_ID | — | ✅ |

### [[irc_bc_cand_screenings|IRC_BC_CAND_SCREENINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | screeningPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | screeningPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | screeningPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | screeningPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | screeningPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | screeningPEOObjectStatus | OBJECT_STATUS | — | ✅ |
| 7 | screeningPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | screeningPEOResultId | RESULT_ID | — | — |
| 9 | screeningPEOScrErrorDesc | SCR_ERROR_DESC | — | ✅ |
| 10 | screeningPEOScrPkgCode | SCR_PKG_CODE | — | ✅ |
| 11 | screeningPEOScrPkgName | SCR_PKG_NAME | — | ✅ |
| 12 | screeningPEOScrStatusCode | SCR_STATUS_CODE | — | ✅ |
| 13 | screeningPEOScreeningId | SCREENING_ID | 🔑 | ✅ |

### [[irc_offers|IRC_OFFERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OffersPEOOfferId | OFFER_ID | — | — |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionBPEORequisitionId | REQUISITION_ID | — | — |
| 2 | RequisitionBPEORequisitionNumber | REQUISITION_NUMBER | — | ✅ |

### [[irc_submissions|IRC_SUBMISSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | SubmissionPEOPersonId | PERSON_ID | — | ✅ |
| 3 | SubmissionPEORequisitionId | REQUISITION_ID | — | ✅ |
| 4 | SubmissionPEOSubmissionId | SUBMISSION_ID | — | — |

### [[irc_tp_partners|IRC_TP_PARTNERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerPEOName | NAME | — | ✅ |
| 2 | PartnerPEOPartnerId | PARTNER_ID | — | ✅ |

### [[irc_tp_partner_accounts|IRC_TP_PARTNER_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerAccountPEOAccountId | ACCOUNT_ID | — | — |
| 2 | PartnerAccountPEOUsername | USERNAME | — | ✅ |

### [[irc_tp_partner_provisngs|IRC_TP_PARTNER_PROVISNGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerProvisionPEOProvisioningId | PROVISIONING_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserPEOPersonId | PERSON_ID | — | — |
| 3 | UserPEOUserId | USER_ID | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
