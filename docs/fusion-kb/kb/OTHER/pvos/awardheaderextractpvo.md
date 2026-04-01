---
id: DOC-OTHER-PVO-AwardHeaderExtractPVO
doc_type: system-doc
title: "AwardHeaderExtractPVO — PVO Cross-Module"
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
  - AwardHeaderExtractPVO
  - awardheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Header Extract. Acessa as tabelas: GMS_AWARD_HEADERS_B, GMS_AWARD_HEADERS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 108 | 2 | 1 | 57 | 53% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_headers_b|GMS_AWARD_HEADERS_B]] — 95 atributos (1 PKs, 44 BICC)
- [[gms_award_headers_tl|GMS_AWARD_HEADERS_TL]] — 13 atributos (13 BICC)

---

## ⚙️ Atributos

### [[gms_award_headers_b|GMS_AWARD_HEADERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardHeaderBaseAttribute1 | ATTRIBUTE1 | — | — |
| 2 | AwardHeaderBaseAttribute10 | ATTRIBUTE10 | — | — |
| 3 | AwardHeaderBaseAttribute11 | ATTRIBUTE11 | — | — |
| 4 | AwardHeaderBaseAttribute12 | ATTRIBUTE12 | — | — |
| 5 | AwardHeaderBaseAttribute13 | ATTRIBUTE13 | — | — |
| 6 | AwardHeaderBaseAttribute14 | ATTRIBUTE14 | — | — |
| 7 | AwardHeaderBaseAttribute15 | ATTRIBUTE15 | — | — |
| 8 | AwardHeaderBaseAttribute16 | ATTRIBUTE16 | — | — |
| 9 | AwardHeaderBaseAttribute17 | ATTRIBUTE17 | — | — |
| 10 | AwardHeaderBaseAttribute18 | ATTRIBUTE18 | — | — |
| 11 | AwardHeaderBaseAttribute19 | ATTRIBUTE19 | — | — |
| 12 | AwardHeaderBaseAttribute2 | ATTRIBUTE2 | — | — |
| 13 | AwardHeaderBaseAttribute20 | ATTRIBUTE20 | — | — |
| 14 | AwardHeaderBaseAttribute3 | ATTRIBUTE3 | — | — |
| 15 | AwardHeaderBaseAttribute4 | ATTRIBUTE4 | — | — |
| 16 | AwardHeaderBaseAttribute5 | ATTRIBUTE5 | — | — |
| 17 | AwardHeaderBaseAttribute6 | ATTRIBUTE6 | — | — |
| 18 | AwardHeaderBaseAttribute7 | ATTRIBUTE7 | — | — |
| 19 | AwardHeaderBaseAttribute8 | ATTRIBUTE8 | — | — |
| 20 | AwardHeaderBaseAttribute9 | ATTRIBUTE9 | — | — |
| 21 | AwardHeaderBaseAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | AwardHeaderBaseAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | AwardHeaderBaseAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | AwardHeaderBaseAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | AwardHeaderBaseAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | AwardHeaderBaseAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | AwardHeaderBaseAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | AwardHeaderBaseAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | AwardHeaderBaseAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | AwardHeaderBaseAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | AwardHeaderBaseAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | AwardHeaderBaseAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | AwardHeaderBaseAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | AwardHeaderBaseAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | AwardHeaderBaseAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | AwardHeaderBaseAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | AwardHeaderBaseAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | AwardHeaderBaseAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | AwardHeaderBaseAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | AwardHeaderBaseAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | AwardHeaderBaseAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | AwardHeaderBaseAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | AwardHeaderBaseAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | AwardHeaderBaseAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | AwardHeaderBaseAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | AwardHeaderBaseAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | AwardHeaderBaseAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | AwardHeaderBaseAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | AwardHeaderBaseAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | AwardHeaderBaseAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | AwardHeaderBaseAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | AwardHeaderBaseAwardOwningOrgId | AWARD_OWNING_ORG_ID | — | ✅ |
| 53 | AwardHeaderBaseAwardPurposeCode | AWARD_PURPOSE_CODE | — | ✅ |
| 54 | AwardHeaderBaseAwardType | AWARD_TYPE | — | ✅ |
| 55 | AwardHeaderBaseBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 56 | AwardHeaderBaseCfdaNumber | CFDA_NUMBER | — | ✅ |
| 57 | AwardHeaderBaseCloseDate | CLOSE_DATE | — | ✅ |
| 58 | AwardHeaderBaseCoiApprovalDate | COI_APPROVAL_DATE | — | ✅ |
| 59 | AwardHeaderBaseCoiInstPolicyCompliant | COI_INST_POLICY_COMPLIANT | — | ✅ |
| 60 | AwardHeaderBaseCoiReviewCompleted | COI_REVIEW_COMPLETED | — | ✅ |
| 61 | AwardHeaderBaseCostIndSchFixedDate | COST_IND_SCH_FIXED_DATE | — | ✅ |
| 62 | AwardHeaderBaseCreatedBy | CREATED_BY | — | ✅ |
| 63 | AwardHeaderBaseCreationDate | CREATION_DATE | — | ✅ |
| 64 | AwardHeaderBaseExpandedAuthFlag | EXPANDED_AUTH_FLAG | — | ✅ |
| 65 | AwardHeaderBaseFtAmount | FT_AMOUNT | — | ✅ |
| 66 | AwardHeaderBaseFtFromDate | FT_FROM_DATE | — | ✅ |
| 67 | AwardHeaderBaseFtIsFederal | FT_IS_FEDERAL | — | ✅ |
| 68 | AwardHeaderBaseFtPrimarySponsor | FT_PRIMARY_SPONSOR | — | ✅ |
| 69 | AwardHeaderBaseFtToDate | FT_TO_DATE | — | ✅ |
| 70 | AwardHeaderBaseId | ID | 🔑 | ✅ |
| 71 | AwardHeaderBaseIdcScheduleId | IDC_SCHEDULE_ID | — | ✅ |
| 72 | AwardHeaderBaseIfsApprovalDate | IFS_APPROVAL_DATE | — | ✅ |
| 73 | AwardHeaderBaseIfsApproverId | IFS_APPROVER_ID | — | ✅ |
| 74 | AwardHeaderBaseIfsSponsorApprovalReqFlag | IFS_SPONSOR_APPROVAL_REQ_FLAG | — | ✅ |
| 75 | AwardHeaderBaseInstitutionId | INSTITUTION_ID | — | ✅ |
| 76 | AwardHeaderBaseIsIntellPropReported | IS_INTELL_PROP_REPORTED | — | ✅ |
| 77 | AwardHeaderBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 78 | AwardHeaderBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 79 | AwardHeaderBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 80 | AwardHeaderBaseLastValidated | LAST_VALIDATED | — | ✅ |
| 81 | AwardHeaderBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 82 | AwardHeaderBasePreAwardDate | PRE_AWARD_DATE | — | ✅ |
| 83 | AwardHeaderBasePreAwardSpendingAllowed | PRE_AWARD_SPENDING_ALLOWED | — | ✅ |
| 84 | AwardHeaderBasePrevAwardAbr | PREV_AWARD_ABR | — | ✅ |
| 85 | AwardHeaderBasePrevAwardBu | PREV_AWARD_BU | — | ✅ |
| 86 | AwardHeaderBasePrevAwardId | PREV_AWARD_ID | — | ✅ |
| 87 | AwardHeaderBasePrevAwardRenewalInprg | PREV_AWARD_RENEWAL_INPRG | — | ✅ |
| 88 | AwardHeaderBasePrincipalInvestigatorId | PRINCIPAL_INVESTIGATOR_ID | — | ✅ |
| 89 | AwardHeaderBaseProposalId | PROPOSAL_ID | — | ✅ |
| 90 | AwardHeaderBaseSourceAwardId | SOURCE_AWARD_ID | — | ✅ |
| 91 | AwardHeaderBaseSourceTemplateId | SOURCE_TEMPLATE_ID | — | ✅ |
| 92 | AwardHeaderBaseSponsorAwardNumber | SPONSOR_AWARD_NUMBER | — | ✅ |
| 93 | AwardHeaderBaseSponsorId | SPONSOR_ID | — | ✅ |
| 94 | AwardHeaderBaseTemplateFlag | TEMPLATE_FLAG | — | ✅ |
| 95 | AwardHeaderBaseValidateStatus | VALIDATE_STATUS | — | ✅ |

### [[gms_award_headers_tl|GMS_AWARD_HEADERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardHeaderTransLangCreatedBy | CREATED_BY | — | ✅ |
| 2 | AwardHeaderTransLangCreationDate | CREATION_DATE | — | ✅ |
| 3 | AwardHeaderTransLangDescription | DESCRIPTION | — | ✅ |
| 4 | AwardHeaderTransLangFtRefAwardName | FT_REF_AWARD_NAME | — | ✅ |
| 5 | AwardHeaderTransLangId | ID | — | ✅ |
| 6 | AwardHeaderTransLangIntellPropDesc | INTELL_PROP_DESC | — | ✅ |
| 7 | AwardHeaderTransLangLanguage | LANGUAGE | — | ✅ |
| 8 | AwardHeaderTransLangLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | AwardHeaderTransLangLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | AwardHeaderTransLangLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | AwardHeaderTransLangObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | AwardHeaderTransLangPreAwardGsf | PRE_AWARD_GSF | — | ✅ |
| 13 | AwardHeaderTransLangSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
