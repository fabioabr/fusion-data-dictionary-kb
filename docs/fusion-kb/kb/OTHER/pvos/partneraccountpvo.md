---
id: DOC-OTHER-PVO-PartnerAccountPVO
doc_type: system-doc
title: "PartnerAccountPVO — PVO Cross-Module"
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
  - PartnerAccountPVO
  - partneraccountpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PartnerAccountPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Partner Account. Acessa as tabelas: IRC_TP_CATEGORIES_B, IRC_TP_CATEGORIES_TL, IRC_TP_PARTNERS (+2).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecJobDistributionAM.PartnerAccountPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 5 | 1 | 34 | 79% |

---

## 🔗 Tabelas Relacionadas

- [[irc_tp_categories_b|IRC_TP_CATEGORIES_B]] — 2 atributos (1 BICC)
- [[irc_tp_categories_tl|IRC_TP_CATEGORIES_TL]] — 5 atributos (3 BICC)
- [[irc_tp_partners|IRC_TP_PARTNERS]] — 10 atributos (8 BICC)
- [[irc_tp_partner_accounts|IRC_TP_PARTNER_ACCOUNTS]] — 15 atributos (1 PKs, 13 BICC)
- [[irc_tp_partner_provisngs|IRC_TP_PARTNER_PROVISNGS]] — 11 atributos (9 BICC)

---

## ⚙️ Atributos

### [[irc_tp_categories_b|IRC_TP_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryBPEOCategoryId | CATEGORY_ID | — | — |
| 2 | CategoryBPEOCode | CODE | — | ✅ |

### [[irc_tp_categories_tl|IRC_TP_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryTLPEOCategoryId | CATEGORY_ID | — | — |
| 2 | CategoryTLPEOCategoryName | CATEGORY_NAME | — | ✅ |
| 3 | CategoryTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | CategoryTLPEOLanguage | LANGUAGE | — | — |
| 5 | CategoryTLPEOSubCategoryName | SUB_CATEGORY_NAME | — | ✅ |

### [[irc_tp_partners|IRC_TP_PARTNERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PartnerPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PartnerPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | PartnerPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | PartnerPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | PartnerPEOLogo | LOGO | — | — |
| 7 | PartnerPEOName | NAME | — | ✅ |
| 8 | PartnerPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | PartnerPEOPartnerGuid | PARTNER_GUID | — | ✅ |
| 10 | PartnerPEOPartnerId | PARTNER_ID | — | ✅ |

### [[irc_tp_partner_accounts|IRC_TP_PARTNER_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerAccountPEOAccountId | ACCOUNT_ID | 🔑 | ✅ |
| 2 | PartnerAccountPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 3 | PartnerAccountPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | PartnerAccountPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | PartnerAccountPEODefaultFlag | DEFAULT_FLAG | — | ✅ |
| 6 | PartnerAccountPEODescription | DESCRIPTION | — | ✅ |
| 7 | PartnerAccountPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PartnerAccountPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | PartnerAccountPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PartnerAccountPEOLastValidateDate | LAST_VALIDATE_DATE | — | ✅ |
| 11 | PartnerAccountPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PartnerAccountPEOProvisioningId | PROVISIONING_ID | — | ✅ |
| 13 | PartnerAccountPEOUserSaltedHash | USER_SALTED_HASH | — | — |
| 14 | PartnerAccountPEOUsername | USERNAME | — | ✅ |
| 15 | PartnerAccountPEOValidateFlag | VALIDATE_FLAG | — | ✅ |

### [[irc_tp_partner_provisngs|IRC_TP_PARTNER_PROVISNGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerProvisionPEOCategoryId | CATEGORY_ID | — | ✅ |
| 2 | PartnerProvisionPEOClientRefKey | CLIENT_REF_KEY | — | — |
| 3 | PartnerProvisionPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | PartnerProvisionPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | PartnerProvisionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PartnerProvisionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PartnerProvisionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PartnerProvisionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | PartnerProvisionPEOPartnerId | PARTNER_ID | — | ✅ |
| 10 | PartnerProvisionPEOProvisioningId | PROVISIONING_ID | — | ✅ |
| 11 | PartnerProvisionPEOStatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
