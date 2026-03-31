---
id: DOC-OTHER-PVO-FosAgreementDefinitionExtractPVO
doc_type: system-doc
title: "FosAgreementDefinitionExtractPVO — PVO Cross-Module"
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
  - FosAgreementDefinitionExtractPVO
  - fosagreementdefinitionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosAgreementDefinitionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Agreement Definition Extract. Acessa as tabelas: FOS_AGREEMENT_DEFINITION_B_F, FOS_AGREEMENT_DEFINITION_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosAgreementDefinitionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 70 | 2 | 3 | 68 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[fos_agreement_definition_b_f|FOS_AGREEMENT_DEFINITION_B_F]] — 56 atributos (3 PKs, 56 BICC)
- [[fos_agreement_definition_tl|FOS_AGREEMENT_DEFINITION_TL]] — 14 atributos (12 BICC)

---

## ⚙️ Atributos

### [[fos_agreement_definition_b_f|FOS_AGREEMENT_DEFINITION_B_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgreementDefinitionBPEOAgreementId | AGREEMENT_ID | 🔑 | ✅ |
| 2 | AgreementDefinitionBPEOAgreementNumber | AGREEMENT_NUMBER | — | ✅ |
| 3 | AgreementDefinitionBPEOAgreementType | AGREEMENT_TYPE | — | ✅ |
| 4 | AgreementDefinitionBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 5 | AgreementDefinitionBPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 6 | AgreementDefinitionBPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 7 | AgreementDefinitionBPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 8 | AgreementDefinitionBPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 9 | AgreementDefinitionBPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 10 | AgreementDefinitionBPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 11 | AgreementDefinitionBPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 12 | AgreementDefinitionBPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 13 | AgreementDefinitionBPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 14 | AgreementDefinitionBPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 15 | AgreementDefinitionBPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 16 | AgreementDefinitionBPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 17 | AgreementDefinitionBPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 18 | AgreementDefinitionBPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 19 | AgreementDefinitionBPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 20 | AgreementDefinitionBPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 21 | AgreementDefinitionBPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 22 | AgreementDefinitionBPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 23 | AgreementDefinitionBPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 24 | AgreementDefinitionBPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 25 | AgreementDefinitionBPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 26 | AgreementDefinitionBPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 27 | AgreementDefinitionBPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 28 | AgreementDefinitionBPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 29 | AgreementDefinitionBPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 30 | AgreementDefinitionBPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 31 | AgreementDefinitionBPEOAutoActiveFlag | AUTO_ACTIVE_FLAG | — | ✅ |
| 32 | AgreementDefinitionBPEOCreatedBy | CREATED_BY | — | ✅ |
| 33 | AgreementDefinitionBPEOCreationDate | CREATION_DATE | — | ✅ |
| 34 | AgreementDefinitionBPEODsFwdOwnsChangeEventId | DS_FWD_OWNS_CHANGE_EVENT_ID | — | ✅ |
| 35 | AgreementDefinitionBPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 36 | AgreementDefinitionBPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 37 | AgreementDefinitionBPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 38 | AgreementDefinitionBPEOFromEntityBasis | FROM_ENTITY_BASIS | — | ✅ |
| 39 | AgreementDefinitionBPEOFromEntityOperator | FROM_ENTITY_OPERATOR | — | ✅ |
| 40 | AgreementDefinitionBPEOFromEntityValue | FROM_ENTITY_VALUE | — | ✅ |
| 41 | AgreementDefinitionBPEOFwdCstOwnsChangeEventId | FWD_CST_OWNS_CHANGE_EVENT_ID | — | ✅ |
| 42 | AgreementDefinitionBPEOFwdSplrOwnsChangeEventId | FWD_SPLR_OWNS_CHANGE_EVENT_ID | — | ✅ |
| 43 | AgreementDefinitionBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | AgreementDefinitionBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 45 | AgreementDefinitionBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 46 | AgreementDefinitionBPEOMultiFtrFlag | MULTI_FTR_FLAG | — | ✅ |
| 47 | AgreementDefinitionBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 48 | AgreementDefinitionBPEOPriority | PRIORITY | — | ✅ |
| 49 | AgreementDefinitionBPEOQualifierRuleSetId | QUALIFIER_RULE_SET_ID | — | ✅ |
| 50 | AgreementDefinitionBPEORtnCstOwnsChangeEventId | RTN_CST_OWNS_CHANGE_EVENT_ID | — | ✅ |
| 51 | AgreementDefinitionBPEORtnSplrOwnsChangeEventId | RTN_SPLR_OWNS_CHANGE_EVENT_ID | — | ✅ |
| 52 | AgreementDefinitionBPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 53 | AgreementDefinitionBPEOStatus | STATUS | — | ✅ |
| 54 | AgreementDefinitionBPEOToEntityBasis | TO_ENTITY_BASIS | — | ✅ |
| 55 | AgreementDefinitionBPEOToEntityOperator | TO_ENTITY_OPERATOR | — | ✅ |
| 56 | AgreementDefinitionBPEOToEntityValue | TO_ENTITY_VALUE | — | ✅ |

### [[fos_agreement_definition_tl|FOS_AGREEMENT_DEFINITION_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgreementDefinitionTLPEOAgreementId | AGREEMENT_ID | — | ✅ |
| 2 | AgreementDefinitionTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | AgreementDefinitionTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | AgreementDefinitionTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | AgreementDefinitionTLPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 6 | AgreementDefinitionTLPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | AgreementDefinitionTLPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 8 | AgreementDefinitionTLPEOLanguage | LANGUAGE | — | — |
| 9 | AgreementDefinitionTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | AgreementDefinitionTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | AgreementDefinitionTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | AgreementDefinitionTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | AgreementDefinitionTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 14 | AgreementDefinitionTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
