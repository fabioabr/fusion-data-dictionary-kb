---
id: DOC-OTHER-PVO-ClinInternalAttributeExtractPVO
doc_type: system-doc
title: "ClinInternalAttributeExtractPVO — PVO Cross-Module"
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
  - ClinInternalAttributeExtractPVO
  - clininternalattributeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClinInternalAttributeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Clin Internal Attribute Extract. Acessa as tabelas: PJB_CLIN_INTERNAL_ATTRIBUTES.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.ClinInternalAttributeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 2 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_clin_internal_attributes|PJB_CLIN_INTERNAL_ATTRIBUTES]] — 21 atributos (2 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[pjb_clin_internal_attributes|PJB_CLIN_INTERNAL_ATTRIBUTES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClinInternalAttributePEOContractId | CONTRACT_ID | — | ✅ |
| 2 | ClinInternalAttributePEOContractLineId | CONTRACT_LINE_ID | 🔑 | ✅ |
| 3 | ClinInternalAttributePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ClinInternalAttributePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ClinInternalAttributePEOExpOrgSource | EXP_ORG_SOURCE | — | ✅ |
| 6 | ClinInternalAttributePEOExpTypeOrigEiFlag | EXP_TYPE_ORIG_EI_FLAG | — | ✅ |
| 7 | ClinInternalAttributePEOExpenditureOrgId | EXPENDITURE_ORG_ID | — | ✅ |
| 8 | ClinInternalAttributePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 9 | ClinInternalAttributePEOExternalKey1 | EXTERNAL_KEY1 | — | ✅ |
| 10 | ClinInternalAttributePEOExternalKey2 | EXTERNAL_KEY2 | — | ✅ |
| 11 | ClinInternalAttributePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ClinInternalAttributePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | ClinInternalAttributePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | ClinInternalAttributePEOMajorVersion | MAJOR_VERSION | 🔑 | ✅ |
| 15 | ClinInternalAttributePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | ClinInternalAttributePEOProviderBusinessUnitId | PROVIDER_BUSINESS_UNIT_ID | — | ✅ |
| 17 | ClinInternalAttributePEORcvrBusinessUnitId | RCVR_BUSINESS_UNIT_ID | — | ✅ |
| 18 | ClinInternalAttributePEORcvrSetupCode | RCVR_SETUP_CODE | — | ✅ |
| 19 | ClinInternalAttributePEOReceiverProjectId | RECEIVER_PROJECT_ID | — | ✅ |
| 20 | ClinInternalAttributePEOReceiverTaskId | RECEIVER_TASK_ID | — | ✅ |
| 21 | ClinInternalAttributePEOVersionType | VERSION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
