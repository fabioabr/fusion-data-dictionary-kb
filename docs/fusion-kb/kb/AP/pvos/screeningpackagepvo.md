---
id: DOC-AP-PVO-ScreeningPackagePVO
doc_type: system-doc
title: "ScreeningPackagePVO — PVO Accounts Payable"
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
  - ScreeningPackagePVO
  - screeningpackagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ScreeningPackagePVO

## 📌 Visão Geral

Extrai os pacotes de screening (verificação de antecedentes) configurados para requisições de recrutamento, incluindo parceiros terceirizados e contas. Permite gerenciar a integração com fornecedores de background check no processo seletivo.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecBackgroundCheckAM.ScreeningPackagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 6 | 1 | 19 | 73% |

---

## 🔗 Tabelas Relacionadas

- [[irc_bc_req_sp_assgmnts|IRC_BC_REQ_SP_ASSGMNTS]] — 16 atributos (1 PKs, 15 BICC)
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 2 atributos (1 BICC)
- [[irc_tp_partners|IRC_TP_PARTNERS]] — 2 atributos (2 BICC)
- [[irc_tp_partner_accounts|IRC_TP_PARTNER_ACCOUNTS]] — 2 atributos (1 BICC)
- [[irc_tp_partner_provisngs|IRC_TP_PARTNER_PROVISNGS]] — 1 atributos
- [[per_users|PER_USERS]] — 3 atributos

---

## ⚙️ Atributos

### [[irc_bc_req_sp_assgmnts|IRC_BC_REQ_SP_ASSGMNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReqSpAssgmntId | REQ_SP_ASSGMNT_ID | 🔑 | ✅ |
| 2 | ScreeningPackagePEOAccountId | ACCOUNT_ID | — | ✅ |
| 3 | ScreeningPackagePEOAddedBy | ADDED_BY | — | ✅ |
| 4 | ScreeningPackagePEOAddedDate | ADDED_DATE | — | ✅ |
| 5 | ScreeningPackagePEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | ScreeningPackagePEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | ScreeningPackagePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ScreeningPackagePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ScreeningPackagePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ScreeningPackagePEOObjectStatus | OBJECT_STATUS | — | ✅ |
| 11 | ScreeningPackagePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ScreeningPackagePEOProvisioningId | PROVISIONING_ID | — | ✅ |
| 13 | ScreeningPackagePEORequisitionId | REQUISITION_ID | — | ✅ |
| 14 | ScreeningPackagePEOScrPkgCode | SCR_PKG_CODE | — | ✅ |
| 15 | ScreeningPackagePEOScrPkgName | SCR_PKG_NAME | — | ✅ |
| 16 | ScreeningPackagePEOScrSequence | SCR_SEQUENCE | — | ✅ |

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

### [[irc_tp_partner_accounts|IRC_TP_PARTNER_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerAccountPEOAccountId | ACCOUNT_ID | — | — |
| 2 | PartnerAccountPEOUsername | USERNAME | — | ✅ |

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

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
