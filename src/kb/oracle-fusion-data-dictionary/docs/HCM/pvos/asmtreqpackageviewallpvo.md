---
id: DOC-HCM-PVO-AsmtReqPackageViewAllPVO
doc_type: system-doc
title: "AsmtReqPackageViewAllPVO — PVO Human Capital Management"
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
  - AsmtReqPackageViewAllPVO
  - asmtreqpackageviewallpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AsmtReqPackageViewAllPVO

## 📌 Visão Geral

Relaciona pacotes de avaliacao a requisicoes de recrutamento com configuracao multi-fase. Permite rastreamento de assessments por vaga e fase.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecAssessmentsAM.AsmtReqPackageViewAllPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 8 | 1 | 21 | 54% |

---

## 🔗 Tabelas Relacionadas

- [[irc_asmt_req_config|IRC_ASMT_REQ_CONFIG]] — 11 atributos (5 BICC)
- [[irc_asmt_req_packages|IRC_ASMT_REQ_PACKAGES]] — 13 atributos (1 PKs, 11 BICC)
- [[irc_phases_tl|IRC_PHASES_TL]] — 3 atributos (1 BICC)
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 3 atributos
- [[irc_states_tl|IRC_STATES_TL]] — 3 atributos (1 BICC)
- [[irc_tp_partners|IRC_TP_PARTNERS]] — 2 atributos (2 BICC)
- [[irc_tp_partner_accounts|IRC_TP_PARTNER_ACCOUNTS]] — 3 atributos (1 BICC)
- [[irc_tp_partner_provisngs|IRC_TP_PARTNER_PROVISNGS]] — 1 atributos

---

## ⚙️ Atributos

### [[irc_asmt_req_config|IRC_ASMT_REQ_CONFIG]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AsmtReqConfigPEOAccountUsername | ACCOUNT_USERNAME | — | ✅ |
| 2 | AsmtReqConfigPEOAssessmentConfigId | ASSESSMENT_CONFIG_ID | — | — |
| 3 | AsmtReqConfigPEOCreatedBy | CREATED_BY | — | — |
| 4 | AsmtReqConfigPEOCreationDate | CREATION_DATE | — | — |
| 5 | AsmtReqConfigPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AsmtReqConfigPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | AsmtReqConfigPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | AsmtReqConfigPEOMultiPhaseCspFlag | MULTI_PHASE_CSP_FLAG | — | ✅ |
| 9 | AsmtReqConfigPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | AsmtReqConfigPEOProvisioningId | PROVISIONING_ID | — | ✅ |
| 11 | AsmtReqConfigPEORequisitionId | REQUISITION_ID | — | ✅ |

### [[irc_asmt_req_packages|IRC_ASMT_REQ_PACKAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AsmtReqPackagePEOAssessmentConfigId | ASSESSMENT_CONFIG_ID | — | ✅ |
| 2 | AsmtReqPackagePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | AsmtReqPackagePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | AsmtReqPackagePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | AsmtReqPackagePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | AsmtReqPackagePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | AsmtReqPackagePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | AsmtReqPackagePEOPackageCode | PACKAGE_CODE | — | ✅ |
| 9 | AsmtReqPackagePEOPackageSequence | PACKAGE_SEQUENCE | — | ✅ |
| 10 | AsmtReqPackagePEOPhaseId | PHASE_ID | — | ✅ |
| 11 | AsmtReqPackagePEOStateId | STATE_ID | — | ✅ |
| 12 | AsmtReqPackagePEOTriggerTypeCode | TRIGGER_TYPE_CODE | — | ✅ |
| 13 | ReqPackageId | REQ_PACKAGE_ID | 🔑 | ✅ |

### [[irc_phases_tl|IRC_PHASES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhaseTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | PhaseTranslationPEOName | NAME | — | ✅ |
| 3 | PhaseTranslationPEOPhaseId | PHASE_ID | — | — |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionBPEOReqUsageCode | REQ_USAGE_CODE | — | — |
| 2 | RequisitionBPEORequisitionId | REQUISITION_ID | — | — |
| 3 | RequisitionBPEORequisitionNumber | REQUISITION_NUMBER | — | — |

### [[irc_states_tl|IRC_STATES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StateTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | StateTranslationPEOName | NAME | — | ✅ |
| 3 | StateTranslationPEOStateId | STATE_ID | — | — |

### [[irc_tp_partners|IRC_TP_PARTNERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerPEOName | NAME | — | ✅ |
| 2 | PartnerPEOPartnerId | PARTNER_ID | — | ✅ |

### [[irc_tp_partner_accounts|IRC_TP_PARTNER_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerAccountPEOAccountId | ACCOUNT_ID | — | ✅ |
| 2 | PartnerAccountPEODescription | DESCRIPTION | — | — |
| 3 | PartnerAccountPEOUsername | USERNAME | — | — |

### [[irc_tp_partner_provisngs|IRC_TP_PARTNER_PROVISNGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerProvisionPEOProvisioningId | PROVISIONING_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
