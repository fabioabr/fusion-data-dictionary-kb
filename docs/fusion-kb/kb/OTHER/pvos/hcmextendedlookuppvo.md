---
id: DOC-OTHER-PVO-HcmExtendedLookupPVO
doc_type: system-doc
title: "HcmExtendedLookupPVO — PVO Cross-Module"
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
  - HcmExtendedLookupPVO
  - hcmextendedlookuppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HcmExtendedLookupPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Hcm Extended Lookup. Acessa as tabelas: HCM_EXTENDED_LOOKUP_CODES_VL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CommonAM.HcmExtendedLookupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 80 | 1 | 1 | 3 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[hcm_extended_lookup_codes_vl|HCM_EXTENDED_LOOKUP_CODES_VL]] — 80 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hcm_extended_lookup_codes_vl|HCM_EXTENDED_LOOKUP_CODES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | EnterpriseId | ENTERPRISE_ID | — | — |
| 4 | ExtendedLookupCode | EXTENDED_LOOKUP_CODE | — | — |
| 5 | ExtendedLookupCodeId | EXTENDED_LOOKUP_CODE_ID | 🔑 | ✅ |
| 6 | ExtendedLookupCodeName | EXTENDED_LOOKUP_CODE_NAME | — | ✅ |
| 7 | Information1 | INFORMATION1 | — | — |
| 8 | Information10 | INFORMATION10 | — | — |
| 9 | Information11 | INFORMATION11 | — | — |
| 10 | Information12 | INFORMATION12 | — | — |
| 11 | Information13 | INFORMATION13 | — | — |
| 12 | Information14 | INFORMATION14 | — | — |
| 13 | Information15 | INFORMATION15 | — | — |
| 14 | Information16 | INFORMATION16 | — | — |
| 15 | Information17 | INFORMATION17 | — | — |
| 16 | Information18 | INFORMATION18 | — | — |
| 17 | Information19 | INFORMATION19 | — | — |
| 18 | Information2 | INFORMATION2 | — | — |
| 19 | Information20 | INFORMATION20 | — | — |
| 20 | Information21 | INFORMATION21 | — | — |
| 21 | Information22 | INFORMATION22 | — | — |
| 22 | Information23 | INFORMATION23 | — | — |
| 23 | Information24 | INFORMATION24 | — | — |
| 24 | Information25 | INFORMATION25 | — | — |
| 25 | Information26 | INFORMATION26 | — | — |
| 26 | Information27 | INFORMATION27 | — | — |
| 27 | Information28 | INFORMATION28 | — | — |
| 28 | Information29 | INFORMATION29 | — | — |
| 29 | Information3 | INFORMATION3 | — | — |
| 30 | Information30 | INFORMATION30 | — | — |
| 31 | Information4 | INFORMATION4 | — | — |
| 32 | Information5 | INFORMATION5 | — | — |
| 33 | Information6 | INFORMATION6 | — | — |
| 34 | Information7 | INFORMATION7 | — | — |
| 35 | Information8 | INFORMATION8 | — | — |
| 36 | Information9 | INFORMATION9 | — | — |
| 37 | InformationCategory | INFORMATION_CATEGORY | — | — |
| 38 | InformationDate1 | INFORMATION_DATE1 | — | — |
| 39 | InformationDate10 | INFORMATION_DATE10 | — | — |
| 40 | InformationDate11 | INFORMATION_DATE11 | — | — |
| 41 | InformationDate12 | INFORMATION_DATE12 | — | — |
| 42 | InformationDate13 | INFORMATION_DATE13 | — | — |
| 43 | InformationDate14 | INFORMATION_DATE14 | — | — |
| 44 | InformationDate15 | INFORMATION_DATE15 | — | — |
| 45 | InformationDate2 | INFORMATION_DATE2 | — | — |
| 46 | InformationDate3 | INFORMATION_DATE3 | — | — |
| 47 | InformationDate4 | INFORMATION_DATE4 | — | — |
| 48 | InformationDate5 | INFORMATION_DATE5 | — | — |
| 49 | InformationDate6 | INFORMATION_DATE6 | — | — |
| 50 | InformationDate7 | INFORMATION_DATE7 | — | — |
| 51 | InformationDate8 | INFORMATION_DATE8 | — | — |
| 52 | InformationDate9 | INFORMATION_DATE9 | — | — |
| 53 | InformationNumber1 | INFORMATION_NUMBER1 | — | — |
| 54 | InformationNumber10 | INFORMATION_NUMBER10 | — | — |
| 55 | InformationNumber11 | INFORMATION_NUMBER11 | — | — |
| 56 | InformationNumber12 | INFORMATION_NUMBER12 | — | — |
| 57 | InformationNumber13 | INFORMATION_NUMBER13 | — | — |
| 58 | InformationNumber14 | INFORMATION_NUMBER14 | — | — |
| 59 | InformationNumber15 | INFORMATION_NUMBER15 | — | — |
| 60 | InformationNumber16 | INFORMATION_NUMBER16 | — | — |
| 61 | InformationNumber17 | INFORMATION_NUMBER17 | — | — |
| 62 | InformationNumber18 | INFORMATION_NUMBER18 | — | — |
| 63 | InformationNumber19 | INFORMATION_NUMBER19 | — | — |
| 64 | InformationNumber2 | INFORMATION_NUMBER2 | — | — |
| 65 | InformationNumber20 | INFORMATION_NUMBER20 | — | — |
| 66 | InformationNumber3 | INFORMATION_NUMBER3 | — | — |
| 67 | InformationNumber4 | INFORMATION_NUMBER4 | — | — |
| 68 | InformationNumber5 | INFORMATION_NUMBER5 | — | — |
| 69 | InformationNumber6 | INFORMATION_NUMBER6 | — | — |
| 70 | InformationNumber7 | INFORMATION_NUMBER7 | — | — |
| 71 | InformationNumber8 | INFORMATION_NUMBER8 | — | — |
| 72 | InformationNumber9 | INFORMATION_NUMBER9 | — | — |
| 73 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 74 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 75 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 76 | LegislationCode | LEGISLATION_CODE | — | — |
| 77 | LookupCode | LOOKUP_CODE | — | — |
| 78 | LookupType | LOOKUP_TYPE | — | — |
| 79 | ModuleId | MODULE_ID | — | — |
| 80 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
