---
id: DOC-GL-PVO-BalanceCategoriesPVO
doc_type: system-doc
title: "BalanceCategoriesPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - BalanceCategoriesPVO
  - balancecategoriespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BalanceCategoriesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Balance Categories. Acessa as tabelas: PAY_BALANCE_CATEGORIES_VL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBalancesSetupAM.BalanceCategoriesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 83 | 1 | 1 | 83 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pay_balance_categories_vl|PAY_BALANCE_CATEGORIES_VL]] — 83 atributos (1 PKs, 83 BICC)

---

## ⚙️ Atributos

### [[pay_balance_categories_vl|PAY_BALANCE_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BalanceCategoriesPEOBalanceCategoryId | BALANCE_CATEGORY_ID | 🔑 | ✅ |
| 2 | BalanceCategoriesPEOBaseBalanceCategoryId | BASE_BALANCE_CATEGORY_ID | — | ✅ |
| 3 | BalanceCategoriesPEOBaseCategoryName | BASE_CATEGORY_NAME | — | ✅ |
| 4 | BalanceCategoriesPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | BalanceCategoriesPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | BalanceCategoriesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 7 | BalanceCategoriesPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | BalanceCategoriesPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 9 | BalanceCategoriesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | BalanceCategoriesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | BalanceCategoriesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | BalanceCategoriesPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 13 | BalanceCategoriesPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 14 | BalanceCategoriesPEOModuleId | MODULE_ID | — | ✅ |
| 15 | BalanceCategoriesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | BalanceCategoriesPEOPbcInformation1 | PBC_INFORMATION1 | — | ✅ |
| 17 | BalanceCategoriesPEOPbcInformation10 | PBC_INFORMATION10 | — | ✅ |
| 18 | BalanceCategoriesPEOPbcInformation11 | PBC_INFORMATION11 | — | ✅ |
| 19 | BalanceCategoriesPEOPbcInformation12 | PBC_INFORMATION12 | — | ✅ |
| 20 | BalanceCategoriesPEOPbcInformation13 | PBC_INFORMATION13 | — | ✅ |
| 21 | BalanceCategoriesPEOPbcInformation14 | PBC_INFORMATION14 | — | ✅ |
| 22 | BalanceCategoriesPEOPbcInformation15 | PBC_INFORMATION15 | — | ✅ |
| 23 | BalanceCategoriesPEOPbcInformation16 | PBC_INFORMATION16 | — | ✅ |
| 24 | BalanceCategoriesPEOPbcInformation17 | PBC_INFORMATION17 | — | ✅ |
| 25 | BalanceCategoriesPEOPbcInformation18 | PBC_INFORMATION18 | — | ✅ |
| 26 | BalanceCategoriesPEOPbcInformation19 | PBC_INFORMATION19 | — | ✅ |
| 27 | BalanceCategoriesPEOPbcInformation2 | PBC_INFORMATION2 | — | ✅ |
| 28 | BalanceCategoriesPEOPbcInformation20 | PBC_INFORMATION20 | — | ✅ |
| 29 | BalanceCategoriesPEOPbcInformation21 | PBC_INFORMATION21 | — | ✅ |
| 30 | BalanceCategoriesPEOPbcInformation22 | PBC_INFORMATION22 | — | ✅ |
| 31 | BalanceCategoriesPEOPbcInformation23 | PBC_INFORMATION23 | — | ✅ |
| 32 | BalanceCategoriesPEOPbcInformation24 | PBC_INFORMATION24 | — | ✅ |
| 33 | BalanceCategoriesPEOPbcInformation25 | PBC_INFORMATION25 | — | ✅ |
| 34 | BalanceCategoriesPEOPbcInformation26 | PBC_INFORMATION26 | — | ✅ |
| 35 | BalanceCategoriesPEOPbcInformation27 | PBC_INFORMATION27 | — | ✅ |
| 36 | BalanceCategoriesPEOPbcInformation28 | PBC_INFORMATION28 | — | ✅ |
| 37 | BalanceCategoriesPEOPbcInformation29 | PBC_INFORMATION29 | — | ✅ |
| 38 | BalanceCategoriesPEOPbcInformation3 | PBC_INFORMATION3 | — | ✅ |
| 39 | BalanceCategoriesPEOPbcInformation30 | PBC_INFORMATION30 | — | ✅ |
| 40 | BalanceCategoriesPEOPbcInformation4 | PBC_INFORMATION4 | — | ✅ |
| 41 | BalanceCategoriesPEOPbcInformation5 | PBC_INFORMATION5 | — | ✅ |
| 42 | BalanceCategoriesPEOPbcInformation6 | PBC_INFORMATION6 | — | ✅ |
| 43 | BalanceCategoriesPEOPbcInformation7 | PBC_INFORMATION7 | — | ✅ |
| 44 | BalanceCategoriesPEOPbcInformation8 | PBC_INFORMATION8 | — | ✅ |
| 45 | BalanceCategoriesPEOPbcInformation9 | PBC_INFORMATION9 | — | ✅ |
| 46 | BalanceCategoriesPEOPbcInformationCategory | PBC_INFORMATION_CATEGORY | — | ✅ |
| 47 | BalanceCategoriesPEOPbcInformationDate1 | PBC_INFORMATION_DATE1 | — | ✅ |
| 48 | BalanceCategoriesPEOPbcInformationDate10 | PBC_INFORMATION_DATE10 | — | ✅ |
| 49 | BalanceCategoriesPEOPbcInformationDate11 | PBC_INFORMATION_DATE11 | — | ✅ |
| 50 | BalanceCategoriesPEOPbcInformationDate12 | PBC_INFORMATION_DATE12 | — | ✅ |
| 51 | BalanceCategoriesPEOPbcInformationDate13 | PBC_INFORMATION_DATE13 | — | ✅ |
| 52 | BalanceCategoriesPEOPbcInformationDate14 | PBC_INFORMATION_DATE14 | — | ✅ |
| 53 | BalanceCategoriesPEOPbcInformationDate15 | PBC_INFORMATION_DATE15 | — | ✅ |
| 54 | BalanceCategoriesPEOPbcInformationDate2 | PBC_INFORMATION_DATE2 | — | ✅ |
| 55 | BalanceCategoriesPEOPbcInformationDate3 | PBC_INFORMATION_DATE3 | — | ✅ |
| 56 | BalanceCategoriesPEOPbcInformationDate4 | PBC_INFORMATION_DATE4 | — | ✅ |
| 57 | BalanceCategoriesPEOPbcInformationDate5 | PBC_INFORMATION_DATE5 | — | ✅ |
| 58 | BalanceCategoriesPEOPbcInformationDate6 | PBC_INFORMATION_DATE6 | — | ✅ |
| 59 | BalanceCategoriesPEOPbcInformationDate7 | PBC_INFORMATION_DATE7 | — | ✅ |
| 60 | BalanceCategoriesPEOPbcInformationDate8 | PBC_INFORMATION_DATE8 | — | ✅ |
| 61 | BalanceCategoriesPEOPbcInformationDate9 | PBC_INFORMATION_DATE9 | — | ✅ |
| 62 | BalanceCategoriesPEOPbcInformationNumber1 | PBC_INFORMATION_NUMBER1 | — | ✅ |
| 63 | BalanceCategoriesPEOPbcInformationNumber10 | PBC_INFORMATION_NUMBER10 | — | ✅ |
| 64 | BalanceCategoriesPEOPbcInformationNumber11 | PBC_INFORMATION_NUMBER11 | — | ✅ |
| 65 | BalanceCategoriesPEOPbcInformationNumber12 | PBC_INFORMATION_NUMBER12 | — | ✅ |
| 66 | BalanceCategoriesPEOPbcInformationNumber13 | PBC_INFORMATION_NUMBER13 | — | ✅ |
| 67 | BalanceCategoriesPEOPbcInformationNumber14 | PBC_INFORMATION_NUMBER14 | — | ✅ |
| 68 | BalanceCategoriesPEOPbcInformationNumber15 | PBC_INFORMATION_NUMBER15 | — | ✅ |
| 69 | BalanceCategoriesPEOPbcInformationNumber16 | PBC_INFORMATION_NUMBER16 | — | ✅ |
| 70 | BalanceCategoriesPEOPbcInformationNumber17 | PBC_INFORMATION_NUMBER17 | — | ✅ |
| 71 | BalanceCategoriesPEOPbcInformationNumber18 | PBC_INFORMATION_NUMBER18 | — | ✅ |
| 72 | BalanceCategoriesPEOPbcInformationNumber19 | PBC_INFORMATION_NUMBER19 | — | ✅ |
| 73 | BalanceCategoriesPEOPbcInformationNumber2 | PBC_INFORMATION_NUMBER2 | — | ✅ |
| 74 | BalanceCategoriesPEOPbcInformationNumber20 | PBC_INFORMATION_NUMBER20 | — | ✅ |
| 75 | BalanceCategoriesPEOPbcInformationNumber3 | PBC_INFORMATION_NUMBER3 | — | ✅ |
| 76 | BalanceCategoriesPEOPbcInformationNumber4 | PBC_INFORMATION_NUMBER4 | — | ✅ |
| 77 | BalanceCategoriesPEOPbcInformationNumber5 | PBC_INFORMATION_NUMBER5 | — | ✅ |
| 78 | BalanceCategoriesPEOPbcInformationNumber6 | PBC_INFORMATION_NUMBER6 | — | ✅ |
| 79 | BalanceCategoriesPEOPbcInformationNumber7 | PBC_INFORMATION_NUMBER7 | — | ✅ |
| 80 | BalanceCategoriesPEOPbcInformationNumber8 | PBC_INFORMATION_NUMBER8 | — | ✅ |
| 81 | BalanceCategoriesPEOPbcInformationNumber9 | PBC_INFORMATION_NUMBER9 | — | ✅ |
| 82 | BalanceCategoriesPEOSaveRunBalanceEnabled | SAVE_RUN_BALANCE_ENABLED | — | ✅ |
| 83 | BalanceCategoriesPEOUserCategoryName | USER_CATEGORY_NAME | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
