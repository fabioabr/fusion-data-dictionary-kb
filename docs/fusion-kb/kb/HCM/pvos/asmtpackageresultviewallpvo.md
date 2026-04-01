---
id: DOC-HCM-PVO-AsmtPackageResultViewAllPVO
doc_type: system-doc
title: "AsmtPackageResultViewAllPVO — PVO Human Capital Management"
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
  - AsmtPackageResultViewAllPVO
  - asmtpackageresultviewallpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AsmtPackageResultViewAllPVO

## 📌 Visão Geral

Consolida resultados de pacotes de avaliacao com banda, comentarios e vinculo a requisicoes. Visao completa para analise de resultados de assessment.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecAssessmentsAM.AsmtPackageResultViewAllPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 41 | 10 | 1 | 21 | 51% |

---

## 🔗 Tabelas Relacionadas

- [[irc_asmt_package_results|IRC_ASMT_PACKAGE_RESULTS]] — 20 atributos (1 PKs, 12 BICC)
- [[irc_asmt_req_config|IRC_ASMT_REQ_CONFIG]] — 4 atributos (3 BICC)
- [[irc_asmt_req_packages|IRC_ASMT_REQ_PACKAGES]] — 2 atributos
- [[irc_offers|IRC_OFFERS]] — 1 atributos
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 2 atributos
- [[irc_submissions|IRC_SUBMISSIONS]] — 4 atributos (2 BICC)
- [[irc_tp_partners|IRC_TP_PARTNERS]] — 2 atributos (2 BICC)
- [[irc_tp_partner_accounts|IRC_TP_PARTNER_ACCOUNTS]] — 1 atributos (1 BICC)
- [[irc_tp_partner_provisngs|IRC_TP_PARTNER_PROVISNGS]] — 1 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (1 BICC)

---

## ⚙️ Atributos

### [[irc_asmt_package_results|IRC_ASMT_PACKAGE_RESULTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AsmtPackageResultPEOBand | BAND | — | ✅ |
| 2 | AsmtPackageResultPEOComments | COMMENTS | — | ✅ |
| 3 | AsmtPackageResultPEOCreatedBy | CREATED_BY | — | — |
| 4 | AsmtPackageResultPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AsmtPackageResultPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 6 | AsmtPackageResultPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 7 | AsmtPackageResultPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AsmtPackageResultPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | AsmtPackageResultPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | AsmtPackageResultPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | AsmtPackageResultPEOPackageStatusCode | PACKAGE_STATUS_CODE | — | ✅ |
| 12 | AsmtPackageResultPEOPercentile | PERCENTILE | — | ✅ |
| 13 | AsmtPackageResultPEOReqPackageId | REQ_PACKAGE_ID | — | ✅ |
| 14 | AsmtPackageResultPEORequestDate | REQUEST_DATE | — | ✅ |
| 15 | AsmtPackageResultPEORequestId | REQUEST_ID | — | — |
| 16 | AsmtPackageResultPEORequestedBy | REQUESTED_BY | — | ✅ |
| 17 | AsmtPackageResultPEOScore | SCORE | — | ✅ |
| 18 | AsmtPackageResultPEOSubmissionId | SUBMISSION_ID | — | ✅ |
| 19 | AsmtPackageResultPEOTryCount | TRY_COUNT | — | — |
| 20 | PackageResultId | PACKAGE_RESULT_ID | 🔑 | ✅ |

### [[irc_asmt_req_config|IRC_ASMT_REQ_CONFIG]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AsmtReqConfigPEOAccountUsername | ACCOUNT_USERNAME | — | ✅ |
| 2 | AsmtReqConfigPEOAssessmentConfigId | ASSESSMENT_CONFIG_ID | — | — |
| 3 | AsmtReqConfigPEOProvisioningId | PROVISIONING_ID | — | ✅ |
| 4 | AsmtReqConfigPEORequisitionId | REQUISITION_ID | — | ✅ |

### [[irc_asmt_req_packages|IRC_ASMT_REQ_PACKAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AsmtReqPackagePEOAssessmentConfigId | ASSESSMENT_CONFIG_ID | — | — |
| 2 | AsmtReqPackagePEOReqPackageId | REQ_PACKAGE_ID | — | — |

### [[irc_offers|IRC_OFFERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OffersPEOOfferId | OFFER_ID | — | — |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionBPEORequisitionId | REQUISITION_ID | — | — |
| 2 | RequisitionBPEORequisitionNumber | REQUISITION_NUMBER | — | — |

### [[irc_submissions|IRC_SUBMISSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubmissionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | SubmissionPEOPersonId | PERSON_ID | — | ✅ |
| 3 | SubmissionPEORequisitionId | REQUISITION_ID | — | — |
| 4 | SubmissionPEOSubmissionId | SUBMISSION_ID | — | ✅ |

### [[irc_tp_partners|IRC_TP_PARTNERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerPEOName | NAME | — | ✅ |
| 2 | PartnerPEOPartnerId | PARTNER_ID | — | ✅ |

### [[irc_tp_partner_accounts|IRC_TP_PARTNER_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerAccountPEOAccountId | ACCOUNT_ID | — | ✅ |

### [[irc_tp_partner_provisngs|IRC_TP_PARTNER_PROVISNGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerProvisionPEOProvisioningId | PROVISIONING_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerPEODisplayName | DISPLAY_NAME | — | — |
| 2 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
