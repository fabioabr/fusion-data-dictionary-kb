---
id: DOC-OTHER-PVO-PayrollRelationshipPVO
doc_type: system-doc
title: "PayrollRelationshipPVO — PVO Cross-Module"
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
  - PayrollRelationshipPVO
  - payrollrelationshippvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PayrollRelationshipPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Payroll Relationship. Acessa as tabelas: PAY_PAY_RELATIONSHIPS_DN, PAY_PAY_RELATIONSHIPS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayRegsAM.PayrollRelationshipPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 90 | 2 | 3 | 15 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]] — 14 atributos (1 PKs, 12 BICC)
- [[pay_pay_relationships_f|PAY_PAY_RELATIONSHIPS_F]] — 76 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | 🔑 | ✅ |
| 2 | PayrollRelationshipPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | PayrollRelationshipPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | PayrollRelationshipPEOEndDate | END_DATE | — | ✅ |
| 5 | PayrollRelationshipPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PayrollRelationshipPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | PayrollRelationshipPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PayrollRelationshipPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 9 | PayrollRelationshipPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PayrollRelationshipPEOPayrollRelationshipNumber | PAYROLL_RELATIONSHIP_NUMBER | — | ✅ |
| 11 | PayrollRelationshipPEOPayrollStatUnitId | PAYROLL_STAT_UNIT_ID | — | ✅ |
| 12 | PayrollRelationshipPEOPersonId | PERSON_ID | — | ✅ |
| 13 | PayrollRelationshipPEORelationshipTypeId | RELATIONSHIP_TYPE_ID | — | ✅ |
| 14 | PayrollRelationshipPEOStartDate | START_DATE | — | ✅ |

### [[pay_pay_relationships_f|PAY_PAY_RELATIONSHIPS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollRelationshipDPEOCreatedBy | CREATED_BY | — | — |
| 2 | PayrollRelationshipDPEOCreationDate | CREATION_DATE | — | — |
| 3 | PayrollRelationshipDPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 4 | PayrollRelationshipDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 5 | PayrollRelationshipDPEOElementCriteriaId | ELEMENT_CRITERIA_ID | — | — |
| 6 | PayrollRelationshipDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PayrollRelationshipDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PayrollRelationshipDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | PayrollRelationshipDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PayrollRelationshipDPEOPayrollRelationshipId1 | PAYROLL_RELATIONSHIP_ID | — | — |
| 11 | PayrollRelationshipDPEORelInformation1 | REL_INFORMATION1 | — | — |
| 12 | PayrollRelationshipDPEORelInformation10 | REL_INFORMATION10 | — | — |
| 13 | PayrollRelationshipDPEORelInformation11 | REL_INFORMATION11 | — | — |
| 14 | PayrollRelationshipDPEORelInformation12 | REL_INFORMATION12 | — | — |
| 15 | PayrollRelationshipDPEORelInformation13 | REL_INFORMATION13 | — | — |
| 16 | PayrollRelationshipDPEORelInformation14 | REL_INFORMATION14 | — | — |
| 17 | PayrollRelationshipDPEORelInformation15 | REL_INFORMATION15 | — | — |
| 18 | PayrollRelationshipDPEORelInformation16 | REL_INFORMATION16 | — | — |
| 19 | PayrollRelationshipDPEORelInformation17 | REL_INFORMATION17 | — | — |
| 20 | PayrollRelationshipDPEORelInformation18 | REL_INFORMATION18 | — | — |
| 21 | PayrollRelationshipDPEORelInformation19 | REL_INFORMATION19 | — | — |
| 22 | PayrollRelationshipDPEORelInformation2 | REL_INFORMATION2 | — | — |
| 23 | PayrollRelationshipDPEORelInformation20 | REL_INFORMATION20 | — | — |
| 24 | PayrollRelationshipDPEORelInformation21 | REL_INFORMATION21 | — | — |
| 25 | PayrollRelationshipDPEORelInformation22 | REL_INFORMATION22 | — | — |
| 26 | PayrollRelationshipDPEORelInformation23 | REL_INFORMATION23 | — | — |
| 27 | PayrollRelationshipDPEORelInformation24 | REL_INFORMATION24 | — | — |
| 28 | PayrollRelationshipDPEORelInformation25 | REL_INFORMATION25 | — | — |
| 29 | PayrollRelationshipDPEORelInformation26 | REL_INFORMATION26 | — | — |
| 30 | PayrollRelationshipDPEORelInformation27 | REL_INFORMATION27 | — | — |
| 31 | PayrollRelationshipDPEORelInformation28 | REL_INFORMATION28 | — | — |
| 32 | PayrollRelationshipDPEORelInformation29 | REL_INFORMATION29 | — | — |
| 33 | PayrollRelationshipDPEORelInformation3 | REL_INFORMATION3 | — | — |
| 34 | PayrollRelationshipDPEORelInformation30 | REL_INFORMATION30 | — | — |
| 35 | PayrollRelationshipDPEORelInformation4 | REL_INFORMATION4 | — | — |
| 36 | PayrollRelationshipDPEORelInformation5 | REL_INFORMATION5 | — | — |
| 37 | PayrollRelationshipDPEORelInformation6 | REL_INFORMATION6 | — | — |
| 38 | PayrollRelationshipDPEORelInformation7 | REL_INFORMATION7 | — | — |
| 39 | PayrollRelationshipDPEORelInformation8 | REL_INFORMATION8 | — | — |
| 40 | PayrollRelationshipDPEORelInformation9 | REL_INFORMATION9 | — | — |
| 41 | PayrollRelationshipDPEORelInformationDate1 | REL_INFORMATION_DATE1 | — | — |
| 42 | PayrollRelationshipDPEORelInformationDate10 | REL_INFORMATION_DATE10 | — | — |
| 43 | PayrollRelationshipDPEORelInformationDate11 | REL_INFORMATION_DATE11 | — | — |
| 44 | PayrollRelationshipDPEORelInformationDate12 | REL_INFORMATION_DATE12 | — | — |
| 45 | PayrollRelationshipDPEORelInformationDate13 | REL_INFORMATION_DATE13 | — | — |
| 46 | PayrollRelationshipDPEORelInformationDate14 | REL_INFORMATION_DATE14 | — | — |
| 47 | PayrollRelationshipDPEORelInformationDate15 | REL_INFORMATION_DATE15 | — | — |
| 48 | PayrollRelationshipDPEORelInformationDate2 | REL_INFORMATION_DATE2 | — | — |
| 49 | PayrollRelationshipDPEORelInformationDate3 | REL_INFORMATION_DATE3 | — | — |
| 50 | PayrollRelationshipDPEORelInformationDate4 | REL_INFORMATION_DATE4 | — | — |
| 51 | PayrollRelationshipDPEORelInformationDate5 | REL_INFORMATION_DATE5 | — | — |
| 52 | PayrollRelationshipDPEORelInformationDate6 | REL_INFORMATION_DATE6 | — | — |
| 53 | PayrollRelationshipDPEORelInformationDate7 | REL_INFORMATION_DATE7 | — | — |
| 54 | PayrollRelationshipDPEORelInformationDate8 | REL_INFORMATION_DATE8 | — | — |
| 55 | PayrollRelationshipDPEORelInformationDate9 | REL_INFORMATION_DATE9 | — | — |
| 56 | PayrollRelationshipDPEORelInformationNumber1 | REL_INFORMATION_NUMBER1 | — | — |
| 57 | PayrollRelationshipDPEORelInformationNumber10 | REL_INFORMATION_NUMBER10 | — | — |
| 58 | PayrollRelationshipDPEORelInformationNumber11 | REL_INFORMATION_NUMBER11 | — | — |
| 59 | PayrollRelationshipDPEORelInformationNumber12 | REL_INFORMATION_NUMBER12 | — | — |
| 60 | PayrollRelationshipDPEORelInformationNumber13 | REL_INFORMATION_NUMBER13 | — | — |
| 61 | PayrollRelationshipDPEORelInformationNumber14 | REL_INFORMATION_NUMBER14 | — | — |
| 62 | PayrollRelationshipDPEORelInformationNumber15 | REL_INFORMATION_NUMBER15 | — | — |
| 63 | PayrollRelationshipDPEORelInformationNumber16 | REL_INFORMATION_NUMBER16 | — | — |
| 64 | PayrollRelationshipDPEORelInformationNumber17 | REL_INFORMATION_NUMBER17 | — | — |
| 65 | PayrollRelationshipDPEORelInformationNumber18 | REL_INFORMATION_NUMBER18 | — | — |
| 66 | PayrollRelationshipDPEORelInformationNumber19 | REL_INFORMATION_NUMBER19 | — | — |
| 67 | PayrollRelationshipDPEORelInformationNumber2 | REL_INFORMATION_NUMBER2 | — | — |
| 68 | PayrollRelationshipDPEORelInformationNumber20 | REL_INFORMATION_NUMBER20 | — | — |
| 69 | PayrollRelationshipDPEORelInformationNumber3 | REL_INFORMATION_NUMBER3 | — | — |
| 70 | PayrollRelationshipDPEORelInformationNumber4 | REL_INFORMATION_NUMBER4 | — | — |
| 71 | PayrollRelationshipDPEORelInformationNumber5 | REL_INFORMATION_NUMBER5 | — | — |
| 72 | PayrollRelationshipDPEORelInformationNumber6 | REL_INFORMATION_NUMBER6 | — | — |
| 73 | PayrollRelationshipDPEORelInformationNumber7 | REL_INFORMATION_NUMBER7 | — | — |
| 74 | PayrollRelationshipDPEORelInformationNumber8 | REL_INFORMATION_NUMBER8 | — | — |
| 75 | PayrollRelationshipDPEORelInformationNumber9 | REL_INFORMATION_NUMBER9 | — | — |
| 76 | PayrollRelationshipDPEORelInformationType | REL_INFORMATION_TYPE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
