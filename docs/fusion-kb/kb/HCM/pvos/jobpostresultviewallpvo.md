---
id: DOC-HCM-PVO-JobPostResultViewAllPVO
doc_type: system-doc
title: "JobPostResultViewAllPVO — PVO Human Capital Management"
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
  - JobPostResultViewAllPVO
  - jobpostresultviewallpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobPostResultViewAllPVO

## 📌 Visão Geral

Visão completa (sem filtro de segurança) de resultados de publicações de vagas. Utilizado em análise global de performance de canais de recrutamento.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecJobDistributionAM.JobPostResultViewAllPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 6 | 1 | 27 | 77% |

---

## 🔗 Tabelas Relacionadas

- [[irc_jd_req_postings|IRC_JD_REQ_POSTINGS]] — 12 atributos (10 BICC)
- [[irc_jd_req_post_results|IRC_JD_REQ_POST_RESULTS]] — 15 atributos (1 PKs, 14 BICC)
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 2 atributos (1 BICC)
- [[irc_tp_partners|IRC_TP_PARTNERS]] — 2 atributos (2 BICC)
- [[irc_tp_partner_provisngs|IRC_TP_PARTNER_PROVISNGS]] — 1 atributos
- [[per_users|PER_USERS]] — 3 atributos

---

## ⚙️ Atributos

### [[irc_jd_req_postings|IRC_JD_REQ_POSTINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PostingPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PostingPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PostingPEOJdErrorDesc | JD_ERROR_DESC | — | ✅ |
| 4 | PostingPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PostingPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | PostingPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | PostingPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | PostingPEOPostedBy | POSTED_BY | — | ✅ |
| 9 | PostingPEOPostedDate | POSTED_DATE | — | ✅ |
| 10 | PostingPEOPostingId | POSTING_ID | — | — |
| 11 | PostingPEOProvisioningId | PROVISIONING_ID | — | ✅ |
| 12 | PostingPEORequisitionId | REQUISITION_ID | — | ✅ |

### [[irc_jd_req_post_results|IRC_JD_REQ_POST_RESULTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PostResultPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PostResultPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PostResultPEOErrorDesc | ERROR_DESC | — | ✅ |
| 4 | PostResultPEOJobBoardId | JOB_BOARD_ID | — | ✅ |
| 5 | PostResultPEOJobBoardName | JOB_BOARD_NAME | — | ✅ |
| 6 | PostResultPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PostResultPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | PostResultPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | PostResultPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PostResultPEOPostingEndDate | POSTING_END_DATE | — | ✅ |
| 11 | PostResultPEOPostingId | POSTING_ID | — | ✅ |
| 12 | PostResultPEOPostingLang | POSTING_LANG | — | ✅ |
| 13 | PostResultPEOPostingStartDate | POSTING_START_DATE | — | ✅ |
| 14 | PostResultPEOPostingStatusCode | POSTING_STATUS_CODE | — | ✅ |
| 15 | ResultId | RESULT_ID | 🔑 | ✅ |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionBPEORequisitionId | REQUISITION_ID | — | — |
| 2 | RequisitionBPEORequisitionNumber | REQUISITION_NUMBER | — | ✅ |

### [[irc_tp_partners|IRC_TP_PARTNERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerPEOName | NAME | — | ✅ |
| 2 | PatnerPEOPartnerId | PARTNER_ID | — | ✅ |

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
