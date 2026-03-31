---
id: DOC-HCM-PVO-BIAssignedPayrollDPVO
doc_type: system-doc
title: "BIAssignedPayrollDPVO — PVO Human Capital Management"
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
  - BIAssignedPayrollDPVO
  - biassignedpayrolldpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BIAssignedPayrollDPVO

## 📌 Visão Geral

Extrai payrolls atribuidos (versao date-effective) via BICC com informacoes customizaveis. Suporta cargas analiticas de vinculo colaborador-folha.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmPayRegsBiccExtractAM.BIAssignedPayrollDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 77 | 1 | 3 | 77 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pay_assigned_payrolls_f|PAY_ASSIGNED_PAYROLLS_F]] — 77 atributos (3 PKs, 77 BICC)

---

## ⚙️ Atributos

### [[pay_assigned_payrolls_f|PAY_ASSIGNED_PAYROLLS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollUsageDPEOAsgInformation1 | ASG_INFORMATION1 | — | ✅ |
| 2 | PayrollUsageDPEOAsgInformation10 | ASG_INFORMATION10 | — | ✅ |
| 3 | PayrollUsageDPEOAsgInformation11 | ASG_INFORMATION11 | — | ✅ |
| 4 | PayrollUsageDPEOAsgInformation12 | ASG_INFORMATION12 | — | ✅ |
| 5 | PayrollUsageDPEOAsgInformation13 | ASG_INFORMATION13 | — | ✅ |
| 6 | PayrollUsageDPEOAsgInformation14 | ASG_INFORMATION14 | — | ✅ |
| 7 | PayrollUsageDPEOAsgInformation15 | ASG_INFORMATION15 | — | ✅ |
| 8 | PayrollUsageDPEOAsgInformation16 | ASG_INFORMATION16 | — | ✅ |
| 9 | PayrollUsageDPEOAsgInformation17 | ASG_INFORMATION17 | — | ✅ |
| 10 | PayrollUsageDPEOAsgInformation18 | ASG_INFORMATION18 | — | ✅ |
| 11 | PayrollUsageDPEOAsgInformation19 | ASG_INFORMATION19 | — | ✅ |
| 12 | PayrollUsageDPEOAsgInformation2 | ASG_INFORMATION2 | — | ✅ |
| 13 | PayrollUsageDPEOAsgInformation20 | ASG_INFORMATION20 | — | ✅ |
| 14 | PayrollUsageDPEOAsgInformation21 | ASG_INFORMATION21 | — | ✅ |
| 15 | PayrollUsageDPEOAsgInformation22 | ASG_INFORMATION22 | — | ✅ |
| 16 | PayrollUsageDPEOAsgInformation23 | ASG_INFORMATION23 | — | ✅ |
| 17 | PayrollUsageDPEOAsgInformation24 | ASG_INFORMATION24 | — | ✅ |
| 18 | PayrollUsageDPEOAsgInformation25 | ASG_INFORMATION25 | — | ✅ |
| 19 | PayrollUsageDPEOAsgInformation26 | ASG_INFORMATION26 | — | ✅ |
| 20 | PayrollUsageDPEOAsgInformation27 | ASG_INFORMATION27 | — | ✅ |
| 21 | PayrollUsageDPEOAsgInformation28 | ASG_INFORMATION28 | — | ✅ |
| 22 | PayrollUsageDPEOAsgInformation29 | ASG_INFORMATION29 | — | ✅ |
| 23 | PayrollUsageDPEOAsgInformation3 | ASG_INFORMATION3 | — | ✅ |
| 24 | PayrollUsageDPEOAsgInformation30 | ASG_INFORMATION30 | — | ✅ |
| 25 | PayrollUsageDPEOAsgInformation4 | ASG_INFORMATION4 | — | ✅ |
| 26 | PayrollUsageDPEOAsgInformation5 | ASG_INFORMATION5 | — | ✅ |
| 27 | PayrollUsageDPEOAsgInformation6 | ASG_INFORMATION6 | — | ✅ |
| 28 | PayrollUsageDPEOAsgInformation7 | ASG_INFORMATION7 | — | ✅ |
| 29 | PayrollUsageDPEOAsgInformation8 | ASG_INFORMATION8 | — | ✅ |
| 30 | PayrollUsageDPEOAsgInformation9 | ASG_INFORMATION9 | — | ✅ |
| 31 | PayrollUsageDPEOAsgInformationDate1 | ASG_INFORMATION_DATE1 | — | ✅ |
| 32 | PayrollUsageDPEOAsgInformationDate10 | ASG_INFORMATION_DATE10 | — | ✅ |
| 33 | PayrollUsageDPEOAsgInformationDate11 | ASG_INFORMATION_DATE11 | — | ✅ |
| 34 | PayrollUsageDPEOAsgInformationDate12 | ASG_INFORMATION_DATE12 | — | ✅ |
| 35 | PayrollUsageDPEOAsgInformationDate13 | ASG_INFORMATION_DATE13 | — | ✅ |
| 36 | PayrollUsageDPEOAsgInformationDate14 | ASG_INFORMATION_DATE14 | — | ✅ |
| 37 | PayrollUsageDPEOAsgInformationDate15 | ASG_INFORMATION_DATE15 | — | ✅ |
| 38 | PayrollUsageDPEOAsgInformationDate2 | ASG_INFORMATION_DATE2 | — | ✅ |
| 39 | PayrollUsageDPEOAsgInformationDate3 | ASG_INFORMATION_DATE3 | — | ✅ |
| 40 | PayrollUsageDPEOAsgInformationDate4 | ASG_INFORMATION_DATE4 | — | ✅ |
| 41 | PayrollUsageDPEOAsgInformationDate5 | ASG_INFORMATION_DATE5 | — | ✅ |
| 42 | PayrollUsageDPEOAsgInformationDate6 | ASG_INFORMATION_DATE6 | — | ✅ |
| 43 | PayrollUsageDPEOAsgInformationDate7 | ASG_INFORMATION_DATE7 | — | ✅ |
| 44 | PayrollUsageDPEOAsgInformationDate8 | ASG_INFORMATION_DATE8 | — | ✅ |
| 45 | PayrollUsageDPEOAsgInformationDate9 | ASG_INFORMATION_DATE9 | — | ✅ |
| 46 | PayrollUsageDPEOAsgInformationNumber1 | ASG_INFORMATION_NUMBER1 | — | ✅ |
| 47 | PayrollUsageDPEOAsgInformationNumber10 | ASG_INFORMATION_NUMBER10 | — | ✅ |
| 48 | PayrollUsageDPEOAsgInformationNumber11 | ASG_INFORMATION_NUMBER11 | — | ✅ |
| 49 | PayrollUsageDPEOAsgInformationNumber12 | ASG_INFORMATION_NUMBER12 | — | ✅ |
| 50 | PayrollUsageDPEOAsgInformationNumber13 | ASG_INFORMATION_NUMBER13 | — | ✅ |
| 51 | PayrollUsageDPEOAsgInformationNumber14 | ASG_INFORMATION_NUMBER14 | — | ✅ |
| 52 | PayrollUsageDPEOAsgInformationNumber15 | ASG_INFORMATION_NUMBER15 | — | ✅ |
| 53 | PayrollUsageDPEOAsgInformationNumber16 | ASG_INFORMATION_NUMBER16 | — | ✅ |
| 54 | PayrollUsageDPEOAsgInformationNumber17 | ASG_INFORMATION_NUMBER17 | — | ✅ |
| 55 | PayrollUsageDPEOAsgInformationNumber18 | ASG_INFORMATION_NUMBER18 | — | ✅ |
| 56 | PayrollUsageDPEOAsgInformationNumber19 | ASG_INFORMATION_NUMBER19 | — | ✅ |
| 57 | PayrollUsageDPEOAsgInformationNumber2 | ASG_INFORMATION_NUMBER2 | — | ✅ |
| 58 | PayrollUsageDPEOAsgInformationNumber20 | ASG_INFORMATION_NUMBER20 | — | ✅ |
| 59 | PayrollUsageDPEOAsgInformationNumber3 | ASG_INFORMATION_NUMBER3 | — | ✅ |
| 60 | PayrollUsageDPEOAsgInformationNumber4 | ASG_INFORMATION_NUMBER4 | — | ✅ |
| 61 | PayrollUsageDPEOAsgInformationNumber5 | ASG_INFORMATION_NUMBER5 | — | ✅ |
| 62 | PayrollUsageDPEOAsgInformationNumber6 | ASG_INFORMATION_NUMBER6 | — | ✅ |
| 63 | PayrollUsageDPEOAsgInformationNumber7 | ASG_INFORMATION_NUMBER7 | — | ✅ |
| 64 | PayrollUsageDPEOAsgInformationNumber8 | ASG_INFORMATION_NUMBER8 | — | ✅ |
| 65 | PayrollUsageDPEOAsgInformationNumber9 | ASG_INFORMATION_NUMBER9 | — | ✅ |
| 66 | PayrollUsageDPEOAsgInformationType | ASG_INFORMATION_TYPE | — | ✅ |
| 67 | PayrollUsageDPEOAssignedPayrollId | ASSIGNED_PAYROLL_ID | 🔑 | ✅ |
| 68 | PayrollUsageDPEOCreatedBy | CREATED_BY | — | ✅ |
| 69 | PayrollUsageDPEOCreationDate | CREATION_DATE | — | ✅ |
| 70 | PayrollUsageDPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 71 | PayrollUsageDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 72 | PayrollUsageDPEOElementCriteriaId | ELEMENT_CRITERIA_ID | — | ✅ |
| 73 | PayrollUsageDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 74 | PayrollUsageDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 75 | PayrollUsageDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 76 | PayrollUsageDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 77 | PayrollUsageDPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
