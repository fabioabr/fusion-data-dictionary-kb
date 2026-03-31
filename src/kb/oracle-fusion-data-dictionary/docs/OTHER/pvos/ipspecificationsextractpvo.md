---
id: DOC-OTHER-PVO-IpSpecificationsExtractPVO
doc_type: system-doc
title: "IpSpecificationsExtractPVO — PVO Cross-Module"
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
  - IpSpecificationsExtractPVO
  - ipspecificationsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IpSpecificationsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ip Specifications Extract. Acessa as tabelas: QA_IP_SPECIFICATIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.IpSpecificationsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 1 | 19 | 90% |

---

## 🔗 Tabelas Relacionadas

- [[qa_ip_specifications|QA_IP_SPECIFICATIONS]] — 21 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[qa_ip_specifications|QA_IP_SPECIFICATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AiSuggestion | AI_SUGGESTION | — | — |
| 2 | InspectionPlanSpecificationPEOCharacteristicId | CHARACTERISTIC_ID | — | ✅ |
| 3 | InspectionPlanSpecificationPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | InspectionPlanSpecificationPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | InspectionPlanSpecificationPEODefaultValueFlag | DEFAULT_VALUE_FLAG | — | ✅ |
| 6 | InspectionPlanSpecificationPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 7 | InspectionPlanSpecificationPEOInspectionPlanId | INSPECTION_PLAN_ID | — | ✅ |
| 8 | InspectionPlanSpecificationPEOIpSpecificationId | IP_SPECIFICATION_ID | 🔑 | ✅ |
| 9 | InspectionPlanSpecificationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | InspectionPlanSpecificationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | InspectionPlanSpecificationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | InspectionPlanSpecificationPEOMaximumValue | MAXIMUM_VALUE | — | ✅ |
| 13 | InspectionPlanSpecificationPEOMaximumValueDate | MAXIMUM_VALUE_DATE | — | ✅ |
| 14 | InspectionPlanSpecificationPEOMinimumValue | MINIMUM_VALUE | — | ✅ |
| 15 | InspectionPlanSpecificationPEOMinimumValueDate | MINIMUM_VALUE_DATE | — | ✅ |
| 16 | InspectionPlanSpecificationPEOOptionalFlag | OPTIONAL_FLAG | — | ✅ |
| 17 | InspectionPlanSpecificationPEOTargetValue | TARGET_VALUE | — | ✅ |
| 18 | InspectionPlanSpecificationPEOTargetValueDate | TARGET_VALUE_DATE | — | ✅ |
| 19 | InspectionPlanSpecificationPEOUomCode | UOM_CODE | — | ✅ |
| 20 | InspectionPlanSpecificationPEOUserSequence | USER_SEQUENCE | — | ✅ |
| 21 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
