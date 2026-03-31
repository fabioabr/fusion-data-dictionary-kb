---
id: DOC-OTHER-PVO-BIPayrollRelationshipGroupDPVO
doc_type: system-doc
title: "BIPayrollRelationshipGroupDPVO — PVO Cross-Module"
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
  - BIPayrollRelationshipGroupDPVO
  - bipayrollrelationshipgroupdpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BIPayrollRelationshipGroupDPVO

## 📌 Visão Geral

View Object para extração BICC de dados de BIPayroll Relationship Group D. Acessa as tabelas: PAY_REL_GROUPS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmPayRegsBiccExtractAM.BIPayrollRelationshipGroupDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 80 | 1 | 3 | 14 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[pay_rel_groups_f|PAY_REL_GROUPS_F]] — 80 atributos (3 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[pay_rel_groups_f|PAY_REL_GROUPS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollRelationshipGroupDPEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | ✅ |
| 2 | PayrollRelationshipGroupDPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | PayrollRelationshipGroupDPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | PayrollRelationshipGroupDPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 5 | PayrollRelationshipGroupDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 6 | PayrollRelationshipGroupDPEOElementCriteriaId | ELEMENT_CRITERIA_ID | — | ✅ |
| 7 | PayrollRelationshipGroupDPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 8 | PayrollRelationshipGroupDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | PayrollRelationshipGroupDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | PayrollRelationshipGroupDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | PayrollRelationshipGroupDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | PayrollRelationshipGroupDPEOOverridingPeriodId | OVERRIDING_PERIOD_ID | — | ✅ |
| 13 | PayrollRelationshipGroupDPEORelInformation1 | REL_INFORMATION1 | — | — |
| 14 | PayrollRelationshipGroupDPEORelInformation10 | REL_INFORMATION10 | — | — |
| 15 | PayrollRelationshipGroupDPEORelInformation11 | REL_INFORMATION11 | — | — |
| 16 | PayrollRelationshipGroupDPEORelInformation12 | REL_INFORMATION12 | — | — |
| 17 | PayrollRelationshipGroupDPEORelInformation13 | REL_INFORMATION13 | — | — |
| 18 | PayrollRelationshipGroupDPEORelInformation14 | REL_INFORMATION14 | — | — |
| 19 | PayrollRelationshipGroupDPEORelInformation15 | REL_INFORMATION15 | — | — |
| 20 | PayrollRelationshipGroupDPEORelInformation16 | REL_INFORMATION16 | — | — |
| 21 | PayrollRelationshipGroupDPEORelInformation17 | REL_INFORMATION17 | — | — |
| 22 | PayrollRelationshipGroupDPEORelInformation18 | REL_INFORMATION18 | — | — |
| 23 | PayrollRelationshipGroupDPEORelInformation19 | REL_INFORMATION19 | — | — |
| 24 | PayrollRelationshipGroupDPEORelInformation2 | REL_INFORMATION2 | — | — |
| 25 | PayrollRelationshipGroupDPEORelInformation20 | REL_INFORMATION20 | — | — |
| 26 | PayrollRelationshipGroupDPEORelInformation21 | REL_INFORMATION21 | — | — |
| 27 | PayrollRelationshipGroupDPEORelInformation22 | REL_INFORMATION22 | — | — |
| 28 | PayrollRelationshipGroupDPEORelInformation23 | REL_INFORMATION23 | — | — |
| 29 | PayrollRelationshipGroupDPEORelInformation24 | REL_INFORMATION24 | — | — |
| 30 | PayrollRelationshipGroupDPEORelInformation25 | REL_INFORMATION25 | — | — |
| 31 | PayrollRelationshipGroupDPEORelInformation26 | REL_INFORMATION26 | — | — |
| 32 | PayrollRelationshipGroupDPEORelInformation27 | REL_INFORMATION27 | — | — |
| 33 | PayrollRelationshipGroupDPEORelInformation28 | REL_INFORMATION28 | — | — |
| 34 | PayrollRelationshipGroupDPEORelInformation29 | REL_INFORMATION29 | — | — |
| 35 | PayrollRelationshipGroupDPEORelInformation3 | REL_INFORMATION3 | — | — |
| 36 | PayrollRelationshipGroupDPEORelInformation30 | REL_INFORMATION30 | — | — |
| 37 | PayrollRelationshipGroupDPEORelInformation4 | REL_INFORMATION4 | — | — |
| 38 | PayrollRelationshipGroupDPEORelInformation5 | REL_INFORMATION5 | — | — |
| 39 | PayrollRelationshipGroupDPEORelInformation6 | REL_INFORMATION6 | — | — |
| 40 | PayrollRelationshipGroupDPEORelInformation7 | REL_INFORMATION7 | — | — |
| 41 | PayrollRelationshipGroupDPEORelInformation8 | REL_INFORMATION8 | — | — |
| 42 | PayrollRelationshipGroupDPEORelInformation9 | REL_INFORMATION9 | — | — |
| 43 | PayrollRelationshipGroupDPEORelInformationDate1 | REL_INFORMATION_DATE1 | — | — |
| 44 | PayrollRelationshipGroupDPEORelInformationDate10 | REL_INFORMATION_DATE10 | — | — |
| 45 | PayrollRelationshipGroupDPEORelInformationDate11 | REL_INFORMATION_DATE11 | — | — |
| 46 | PayrollRelationshipGroupDPEORelInformationDate12 | REL_INFORMATION_DATE12 | — | — |
| 47 | PayrollRelationshipGroupDPEORelInformationDate13 | REL_INFORMATION_DATE13 | — | — |
| 48 | PayrollRelationshipGroupDPEORelInformationDate14 | REL_INFORMATION_DATE14 | — | — |
| 49 | PayrollRelationshipGroupDPEORelInformationDate15 | REL_INFORMATION_DATE15 | — | — |
| 50 | PayrollRelationshipGroupDPEORelInformationDate2 | REL_INFORMATION_DATE2 | — | — |
| 51 | PayrollRelationshipGroupDPEORelInformationDate3 | REL_INFORMATION_DATE3 | — | — |
| 52 | PayrollRelationshipGroupDPEORelInformationDate4 | REL_INFORMATION_DATE4 | — | — |
| 53 | PayrollRelationshipGroupDPEORelInformationDate5 | REL_INFORMATION_DATE5 | — | — |
| 54 | PayrollRelationshipGroupDPEORelInformationDate6 | REL_INFORMATION_DATE6 | — | — |
| 55 | PayrollRelationshipGroupDPEORelInformationDate7 | REL_INFORMATION_DATE7 | — | — |
| 56 | PayrollRelationshipGroupDPEORelInformationDate8 | REL_INFORMATION_DATE8 | — | — |
| 57 | PayrollRelationshipGroupDPEORelInformationDate9 | REL_INFORMATION_DATE9 | — | — |
| 58 | PayrollRelationshipGroupDPEORelInformationNumber1 | REL_INFORMATION_NUMBER1 | — | — |
| 59 | PayrollRelationshipGroupDPEORelInformationNumber10 | REL_INFORMATION_NUMBER10 | — | — |
| 60 | PayrollRelationshipGroupDPEORelInformationNumber11 | REL_INFORMATION_NUMBER11 | — | — |
| 61 | PayrollRelationshipGroupDPEORelInformationNumber12 | REL_INFORMATION_NUMBER12 | — | — |
| 62 | PayrollRelationshipGroupDPEORelInformationNumber13 | REL_INFORMATION_NUMBER13 | — | — |
| 63 | PayrollRelationshipGroupDPEORelInformationNumber14 | REL_INFORMATION_NUMBER14 | — | — |
| 64 | PayrollRelationshipGroupDPEORelInformationNumber15 | REL_INFORMATION_NUMBER15 | — | — |
| 65 | PayrollRelationshipGroupDPEORelInformationNumber16 | REL_INFORMATION_NUMBER16 | — | — |
| 66 | PayrollRelationshipGroupDPEORelInformationNumber17 | REL_INFORMATION_NUMBER17 | — | — |
| 67 | PayrollRelationshipGroupDPEORelInformationNumber18 | REL_INFORMATION_NUMBER18 | — | — |
| 68 | PayrollRelationshipGroupDPEORelInformationNumber19 | REL_INFORMATION_NUMBER19 | — | — |
| 69 | PayrollRelationshipGroupDPEORelInformationNumber2 | REL_INFORMATION_NUMBER2 | — | — |
| 70 | PayrollRelationshipGroupDPEORelInformationNumber20 | REL_INFORMATION_NUMBER20 | — | — |
| 71 | PayrollRelationshipGroupDPEORelInformationNumber3 | REL_INFORMATION_NUMBER3 | — | — |
| 72 | PayrollRelationshipGroupDPEORelInformationNumber4 | REL_INFORMATION_NUMBER4 | — | — |
| 73 | PayrollRelationshipGroupDPEORelInformationNumber5 | REL_INFORMATION_NUMBER5 | — | — |
| 74 | PayrollRelationshipGroupDPEORelInformationNumber6 | REL_INFORMATION_NUMBER6 | — | — |
| 75 | PayrollRelationshipGroupDPEORelInformationNumber7 | REL_INFORMATION_NUMBER7 | — | — |
| 76 | PayrollRelationshipGroupDPEORelInformationNumber8 | REL_INFORMATION_NUMBER8 | — | — |
| 77 | PayrollRelationshipGroupDPEORelInformationNumber9 | REL_INFORMATION_NUMBER9 | — | — |
| 78 | PayrollRelationshipGroupDPEORelInformationType | REL_INFORMATION_TYPE | — | — |
| 79 | PayrollRelationshipGroupDPEORelationshipGroupId | RELATIONSHIP_GROUP_ID | 🔑 | ✅ |
| 80 | PayrollRelationshipGroupDPEOTimeCardReq | TIME_CARD_REQ | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
