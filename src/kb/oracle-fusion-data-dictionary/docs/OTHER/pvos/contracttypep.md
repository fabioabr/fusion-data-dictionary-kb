---
id: DOC-OTHER-PVO-ContractTypeP
doc_type: system-doc
title: "ContractTypeP — PVO Cross-Module"
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
  - ContractTypeP
  - contracttypep
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractTypeP

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Type P. Acessa as tabelas: OKC_CONTRACT_TYPES_B, OKC_CONTRACT_TYPES_TL.

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractTypeP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 51 | 2 | 1 | 45 | 88% |

---

## 🔗 Tabelas Relacionadas

- [[okc_contract_types_b|OKC_CONTRACT_TYPES_B]] — 38 atributos (1 PKs, 38 BICC)
- [[okc_contract_types_tl|OKC_CONTRACT_TYPES_TL]] — 13 atributos (7 BICC)

---

## ⚙️ Atributos

### [[okc_contract_types_b|OKC_CONTRACT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgreementEnabledFlag | AGREEMENT_ENABLED_FLAG | — | ✅ |
| 2 | AllowLinesFlag | ALLOW_LINES_FLAG | — | ✅ |
| 3 | BillingLimitType | BILLING_LIMIT_TYPE | — | ✅ |
| 4 | ContractClass | CONTRACT_CLASS | — | ✅ |
| 5 | ContractGroupId | CONTRACT_GROUP_ID | — | ✅ |
| 6 | ContractLayoutTemplate | CONTRACT_LAYOUT_TEMPLATE | — | ✅ |
| 7 | ContractNumbMethod | CONTRACT_NUMB_METHOD | — | ✅ |
| 8 | ContractNumbSeqCat | CONTRACT_NUMB_SEQ_CAT | — | ✅ |
| 9 | ContractTypeCode | CONTRACT_TYPE_CODE | — | ✅ |
| 10 | ContractTypeContractTypeId | CONTRACT_TYPE_ID | 🔑 | ✅ |
| 11 | ContractTypeCreatedBy | CREATED_BY | — | ✅ |
| 12 | ContractTypeCreationDate | CREATION_DATE | — | ✅ |
| 13 | ContractTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ContractTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | ContractTypeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ContractTypeLineClass | LINE_CLASS | — | ✅ |
| 17 | ContractTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | DaysToExpiration | DAYS_TO_EXPIRATION | — | ✅ |
| 19 | EnableBillingCtrlFlag | ENABLE_BILLING_CTRL_FLAG | — | ✅ |
| 20 | EndDate | END_DATE | — | ✅ |
| 21 | Intent | INTENT | — | ✅ |
| 22 | InterCompanyFlag | INTER_COMPANY_FLAG | — | ✅ |
| 23 | InterProjectFlag | INTER_PROJECT_FLAG | — | ✅ |
| 24 | InteractionsEnabledFlag | INTERACTIONS_ENABLED_FLAG | — | ✅ |
| 25 | LayoutTemplateId | LAYOUT_TEMPLATE_ID | — | ✅ |
| 26 | LineAutonumberEnabledFlag | LINE_AUTONUMBER_ENABLED_FLAG | — | ✅ |
| 27 | NotifyBeforeExpFlag | NOTIFY_BEFORE_EXP_FLAG | — | ✅ |
| 28 | NotifyContactRole | NOTIFY_CONTACT_ROLE | — | ✅ |
| 29 | PrimaryBuyerRole | PRIMARY_BUYER_ROLE | — | ✅ |
| 30 | QclId | QCL_ID | — | ✅ |
| 31 | RelatedKEnabledFlag | RELATED_K_ENABLED_FLAG | — | ✅ |
| 32 | RequesterContactRole | REQUESTER_CONTACT_ROLE | — | ✅ |
| 33 | RisksEnabledFlag | RISKS_ENABLED_FLAG | — | ✅ |
| 34 | SetId | SET_ID | — | ✅ |
| 35 | SignatureRequiredFlag | SIGNATURE_REQUIRED_FLAG | — | ✅ |
| 36 | StartDate | START_DATE | — | ✅ |
| 37 | TermsEnabledFlag | TERMS_ENABLED_FLAG | — | ✅ |
| 38 | TermsLayoutTemplate | TERMS_LAYOUT_TEMPLATE | — | ✅ |

### [[okc_contract_types_tl|OKC_CONTRACT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractTypeTranslationContractTypeId | CONTRACT_TYPE_ID | — | — |
| 2 | ContractTypeTranslationCreatedBy | CREATED_BY | — | — |
| 3 | ContractTypeTranslationCreationDate | CREATION_DATE | — | — |
| 4 | ContractTypeTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ContractTypeTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ContractTypeTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ContractTypeTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | Description | DESCRIPTION | — | ✅ |
| 9 | EmailMessageText | EMAIL_MESSAGE_TEXT | — | ✅ |
| 10 | EmailSubject | EMAIL_SUBJECT | — | ✅ |
| 11 | Language | LANGUAGE | — | ✅ |
| 12 | Name | NAME | — | ✅ |
| 13 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
