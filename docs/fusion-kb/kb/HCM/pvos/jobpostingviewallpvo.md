---
id: DOC-HCM-PVO-JobPostingViewAllPVO
doc_type: system-doc
title: "JobPostingViewAllPVO — PVO Human Capital Management"
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
  - JobPostingViewAllPVO
  - jobpostingviewallpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobPostingViewAllPVO

## 📌 Visão Geral

Visão completa (sem filtro de segurança) de publicações de vagas. Utilizado em relatórios analíticos de divulgação de vagas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecJobDistributionAM.JobPostingViewAllPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 5 | 1 | 14 | 70% |

---

## 🔗 Tabelas Relacionadas

- [[irc_jd_req_postings|IRC_JD_REQ_POSTINGS]] — 12 atributos (1 PKs, 11 BICC)
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 2 atributos (1 BICC)
- [[irc_tp_partners|IRC_TP_PARTNERS]] — 2 atributos (2 BICC)
- [[irc_tp_partner_provisngs|IRC_TP_PARTNER_PROVISNGS]] — 1 atributos
- [[per_users|PER_USERS]] — 3 atributos

---

## ⚙️ Atributos

### [[irc_jd_req_postings|IRC_JD_REQ_POSTINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PostingId | POSTING_ID | 🔑 | ✅ |
| 2 | PostingPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | PostingPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | PostingPEOJdErrorDesc | JD_ERROR_DESC | — | ✅ |
| 5 | PostingPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PostingPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PostingPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PostingPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | PostingPEOPostedBy | POSTED_BY | — | ✅ |
| 10 | PostingPEOPostedDate | POSTED_DATE | — | ✅ |
| 11 | PostingPEOProvisioningId | PROVISIONING_ID | — | ✅ |
| 12 | PostingPEORequisitionId | REQUISITION_ID | — | ✅ |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionBPEORequisitionId | REQUISITION_ID | — | — |
| 2 | RequisitionBPEORequisitionNumber | REQUISITION_NUMBER | — | ✅ |

### [[irc_tp_partners|IRC_TP_PARTNERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerPEOName | NAME | — | ✅ |
| 2 | PartnerPEOPartnerId | PARTNER_ID | — | ✅ |

### [[irc_tp_partner_provisngs|IRC_TP_PARTNER_PROVISNGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerProvisionPEOProvisioningId | PROVISIONING_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserPEOPersonId | PERSON_ID | — | — |
| 3 | UserPEOUserId | USER_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
