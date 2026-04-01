---
id: DOC-OTHER-PVO-ImplPerfObligTlinesPVO
doc_type: system-doc
title: "ImplPerfObligTlinesPVO — PVO Cross-Module"
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
  - ImplPerfObligTlinesPVO
  - implperfobligtlinespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ImplPerfObligTlinesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Impl Perf Oblig Tlines. Acessa as tabelas: PER_PERSON_NAMES_F_V, PER_USERS, RA_RULES (+4).

**Caminho:** `FscmTopModelAM.FinVrmRRSharedPublicModelAM.ImplPerfObligTlinesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 129 | 7 | 1 | 25 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 8 atributos
- [[ra_rules|RA_RULES]] — 3 atributos (1 BICC)
- [[ra_rule_schedules|RA_RULE_SCHEDULES]] — 3 atributos
- [[vrm_impl_perf_oblig_tlines|VRM_IMPL_PERF_OBLIG_TLINES]] — 54 atributos (1 PKs, 12 BICC)
- [[vrm_impl_perf_oblig_tplt_b|VRM_IMPL_PERF_OBLIG_TPLT_B]] — 46 atributos (10 BICC)
- [[vrm_impl_perf_oblig_tplt_tl|VRM_IMPL_PERF_OBLIG_TPLT_TL]] — 5 atributos (2 BICC)

---

## ⚙️ Atributos

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByPersonId | PERSON_ID | — | — |
| 3 | UserCreatedByUserId | USER_ID | — | — |
| 4 | UserCreatedByUsername | USERNAME | — | — |
| 5 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 7 | UserUpdatedByUserId | USER_ID | — | — |
| 8 | UserUpdatedByUsername | USERNAME | — | — |

### [[ra_rules|RA_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaRulesPEOName | NAME | — | ✅ |
| 2 | RaRulesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | RaRulesPEORuleId | RULE_ID | — | — |

### [[ra_rule_schedules|RA_RULE_SCHEDULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaRuleSchedulesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | RaRuleSchedulesPEOPeriodNumber | PERIOD_NUMBER | — | — |
| 3 | RaRuleSchedulesPEORuleId | RULE_ID | — | — |

### [[vrm_impl_perf_oblig_tlines|VRM_IMPL_PERF_OBLIG_TLINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ImplPerfObligTlinesId | IMPL_PERF_OBLIG_TLINES_ID | 🔑 | ✅ |
| 2 | ImplPerfObligTlinesPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | ImplPerfObligTlinesPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | ImplPerfObligTlinesPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | ImplPerfObligTlinesPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | ImplPerfObligTlinesPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | ImplPerfObligTlinesPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | ImplPerfObligTlinesPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | ImplPerfObligTlinesPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | ImplPerfObligTlinesPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | ImplPerfObligTlinesPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | ImplPerfObligTlinesPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | ImplPerfObligTlinesPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | ImplPerfObligTlinesPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | ImplPerfObligTlinesPEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | ImplPerfObligTlinesPEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | ImplPerfObligTlinesPEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | ImplPerfObligTlinesPEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | ImplPerfObligTlinesPEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | ImplPerfObligTlinesPEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | ImplPerfObligTlinesPEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | ImplPerfObligTlinesPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | ImplPerfObligTlinesPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | ImplPerfObligTlinesPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | ImplPerfObligTlinesPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | ImplPerfObligTlinesPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | ImplPerfObligTlinesPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | ImplPerfObligTlinesPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 29 | ImplPerfObligTlinesPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | ImplPerfObligTlinesPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | ImplPerfObligTlinesPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | ImplPerfObligTlinesPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | ImplPerfObligTlinesPEOBuId | BU_ID | — | — |
| 34 | ImplPerfObligTlinesPEOCostAmount | COST_AMOUNT | — | ✅ |
| 35 | ImplPerfObligTlinesPEOCreatedBy | CREATED_BY | — | ✅ |
| 36 | ImplPerfObligTlinesPEOCreatedFrom | CREATED_FROM | — | — |
| 37 | ImplPerfObligTlinesPEOCreationDate | CREATION_DATE | — | ✅ |
| 38 | ImplPerfObligTlinesPEOImplPerfObligTemplateId | IMPL_PERF_OBLIG_TEMPLATE_ID | — | — |
| 39 | ImplPerfObligTlinesPEOInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 40 | ImplPerfObligTlinesPEOItemType | ITEM_TYPE | — | ✅ |
| 41 | ImplPerfObligTlinesPEOItemTypeId | ITEM_TYPE_ID | — | — |
| 42 | ImplPerfObligTlinesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 43 | ImplPerfObligTlinesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 44 | ImplPerfObligTlinesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 45 | ImplPerfObligTlinesPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 46 | ImplPerfObligTlinesPEOLineAmount | LINE_AMOUNT | — | — |
| 47 | ImplPerfObligTlinesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 48 | ImplPerfObligTlinesPEOQuantity | QUANTITY | — | ✅ |
| 49 | ImplPerfObligTlinesPEORevenueRuleId | REVENUE_RULE_ID | — | — |
| 50 | ImplPerfObligTlinesPEOSatisfactionMeasurementModel | SATISFACTION_MEASUREMENT_MODEL | — | ✅ |
| 51 | ImplPerfObligTlinesPEOUnitBasePrice | UNIT_BASE_PRICE | — | ✅ |
| 52 | ImplPerfObligTlinesPEOUnitListPrice | UNIT_LIST_PRICE | — | ✅ |
| 53 | ImplPerfObligTlinesPEOUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 54 | ImplPerfObligTlinesPEOUomCode | UOM_CODE | — | ✅ |

### [[vrm_impl_perf_oblig_tplt_b|VRM_IMPL_PERF_OBLIG_TPLT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ImpliedPerfObligationTemplat1Attribute101 | ATTRIBUTE10 | — | — |
| 2 | ImpliedPerfObligationTemplat1Attribute110 | ATTRIBUTE1 | — | — |
| 3 | ImpliedPerfObligationTemplat1Attribute111 | ATTRIBUTE11 | — | — |
| 4 | ImpliedPerfObligationTemplat1Attribute121 | ATTRIBUTE12 | — | — |
| 5 | ImpliedPerfObligationTemplat1Attribute131 | ATTRIBUTE13 | — | — |
| 6 | ImpliedPerfObligationTemplat1Attribute141 | ATTRIBUTE14 | — | — |
| 7 | ImpliedPerfObligationTemplat1Attribute151 | ATTRIBUTE15 | — | — |
| 8 | ImpliedPerfObligationTemplat1Attribute161 | ATTRIBUTE16 | — | — |
| 9 | ImpliedPerfObligationTemplat1Attribute171 | ATTRIBUTE17 | — | — |
| 10 | ImpliedPerfObligationTemplat1Attribute181 | ATTRIBUTE18 | — | — |
| 11 | ImpliedPerfObligationTemplat1Attribute191 | ATTRIBUTE19 | — | — |
| 12 | ImpliedPerfObligationTemplat1Attribute201 | ATTRIBUTE20 | — | — |
| 13 | ImpliedPerfObligationTemplat1Attribute21 | ATTRIBUTE2 | — | — |
| 14 | ImpliedPerfObligationTemplat1Attribute31 | ATTRIBUTE3 | — | — |
| 15 | ImpliedPerfObligationTemplat1Attribute41 | ATTRIBUTE4 | — | — |
| 16 | ImpliedPerfObligationTemplat1Attribute51 | ATTRIBUTE5 | — | — |
| 17 | ImpliedPerfObligationTemplat1Attribute61 | ATTRIBUTE6 | — | — |
| 18 | ImpliedPerfObligationTemplat1Attribute71 | ATTRIBUTE7 | — | — |
| 19 | ImpliedPerfObligationTemplat1Attribute81 | ATTRIBUTE8 | — | — |
| 20 | ImpliedPerfObligationTemplat1Attribute91 | ATTRIBUTE9 | — | — |
| 21 | ImpliedPerfObligationTemplat1AttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 22 | ImpliedPerfObligationTemplat1AttributeDate11 | ATTRIBUTE_DATE1 | — | — |
| 23 | ImpliedPerfObligationTemplat1AttributeDate21 | ATTRIBUTE_DATE2 | — | — |
| 24 | ImpliedPerfObligationTemplat1AttributeDate31 | ATTRIBUTE_DATE3 | — | — |
| 25 | ImpliedPerfObligationTemplat1AttributeDate41 | ATTRIBUTE_DATE4 | — | — |
| 26 | ImpliedPerfObligationTemplat1AttributeDate51 | ATTRIBUTE_DATE5 | — | — |
| 27 | ImpliedPerfObligationTemplat1AttributeNumber11 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | ImpliedPerfObligationTemplat1AttributeNumber21 | ATTRIBUTE_NUMBER2 | — | — |
| 29 | ImpliedPerfObligationTemplat1AttributeNumber31 | ATTRIBUTE_NUMBER3 | — | — |
| 30 | ImpliedPerfObligationTemplat1AttributeNumber41 | ATTRIBUTE_NUMBER4 | — | — |
| 31 | ImpliedPerfObligationTemplat1AttributeNumber51 | ATTRIBUTE_NUMBER5 | — | — |
| 32 | ImpliedPerfObligationTemplat1ClassificationCode | CLASSIFICATION_CODE | — | ✅ |
| 33 | ImpliedPerfObligationTemplat1CreateNewObligFlag | CREATE_NEW_OBLIG_FLAG | — | — |
| 34 | ImpliedPerfObligationTemplat1CreatedFrom1 | CREATED_FROM | — | — |
| 35 | ImpliedPerfObligationTemplat1CreationDate1 | CREATION_DATE | — | ✅ |
| 36 | ImpliedPerfObligationTemplat1CurrencyCode | CURRENCY_CODE | — | ✅ |
| 37 | ImpliedPerfObligationTemplat1DeriveFrRelatedLineFlag | DERIVE_FR_RELATED_LINE_FLAG | — | ✅ |
| 38 | ImpliedPerfObligationTemplat1DevolvePoFlag | DEVOLVE_PO_FLAG | — | ✅ |
| 39 | ImpliedPerfObligationTemplat1EnabledFlag | ENABLED_FLAG | — | ✅ |
| 40 | ImpliedPerfObligationTemplat1ExemptedFromAllocationFlag | EXEMPTED_FROM_ALLOCATION_FLAG | — | ✅ |
| 41 | ImpliedPerfObligationTemplat1ImplPerfObligTemplateId1 | IMPL_PERF_OBLIG_TEMPLATE_ID | — | — |
| 42 | ImpliedPerfObligationTemplat1InUseFlag | IN_USE_FLAG | — | ✅ |
| 43 | ImpliedPerfObligationTemplat1LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 44 | ImpliedPerfObligationTemplat1LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 45 | ImpliedPerfObligationTemplat1ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 46 | ImpliedPerfObligationTemplat1SatisfactionMethod | SATISFACTION_METHOD | — | ✅ |

### [[vrm_impl_perf_oblig_tplt_tl|VRM_IMPL_PERF_OBLIG_TPLT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ImpPerfObligTemp3ImplPerfObligTemplateId | IMPL_PERF_OBLIG_TEMPLATE_ID | — | — |
| 2 | ImplPerfObligTemp3Language | LANGUAGE | — | — |
| 3 | ImplPerfObligTemp3ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | ImpliedPerfObligationTemplat1Description | DESCRIPTION | — | ✅ |
| 5 | ImpliedPerfObligationTemplat1Name | NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
