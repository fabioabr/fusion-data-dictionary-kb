---
id: DOC-OTHER-PVO-AgreementPVO
doc_type: system-doc
title: "AgreementPVO — PVO Cross-Module"
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
  - AgreementPVO
  - agreementpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AgreementPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Agreement. Acessa as tabelas: FOS_AGREEMENT_DEFINITION_VL.

**Caminho:** `FscmTopModelAM.FosOrchestrationProcessAM.AgreementPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 1 | 3 | 27 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_agreement_definition_vl|FOS_AGREEMENT_DEFINITION_VL]] — 27 atributos (3 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[fos_agreement_definition_vl|FOS_AGREEMENT_DEFINITION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgreementDefinitionDPEOAgreementId | AGREEMENT_ID | 🔑 | ✅ |
| 2 | AgreementDefinitionDPEOAgreementNumber | AGREEMENT_NUMBER | — | ✅ |
| 3 | AgreementDefinitionDPEOAgreementType | AGREEMENT_TYPE | — | ✅ |
| 4 | AgreementDefinitionDPEOAutoActiveFlag | AUTO_ACTIVE_FLAG | — | ✅ |
| 5 | AgreementDefinitionDPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | AgreementDefinitionDPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | AgreementDefinitionDPEODescription | DESCRIPTION | — | ✅ |
| 8 | AgreementDefinitionDPEODsFwdOwnsChangeEventId | DS_FWD_OWNS_CHANGE_EVENT_ID | — | ✅ |
| 9 | AgreementDefinitionDPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 10 | AgreementDefinitionDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 11 | AgreementDefinitionDPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 12 | AgreementDefinitionDPEOFromEntityBasis | FROM_ENTITY_BASIS | — | ✅ |
| 13 | AgreementDefinitionDPEOFromEntityValue | FROM_ENTITY_VALUE | — | ✅ |
| 14 | AgreementDefinitionDPEOFwdCstOwnsChangeEventId | FWD_CST_OWNS_CHANGE_EVENT_ID | — | ✅ |
| 15 | AgreementDefinitionDPEOFwdSplrOwnsChangeEventId | FWD_SPLR_OWNS_CHANGE_EVENT_ID | — | ✅ |
| 16 | AgreementDefinitionDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | AgreementDefinitionDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | AgreementDefinitionDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | AgreementDefinitionDPEOMultiFtrFlag | MULTI_FTR_FLAG | — | ✅ |
| 20 | AgreementDefinitionDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | AgreementDefinitionDPEOPriority | PRIORITY | — | ✅ |
| 22 | AgreementDefinitionDPEOQualifierRuleSetId | QUALIFIER_RULE_SET_ID | — | ✅ |
| 23 | AgreementDefinitionDPEORtnCstOwnsChangeEventId | RTN_CST_OWNS_CHANGE_EVENT_ID | — | ✅ |
| 24 | AgreementDefinitionDPEORtnSplrOwnsChangeEventId | RTN_SPLR_OWNS_CHANGE_EVENT_ID | — | ✅ |
| 25 | AgreementDefinitionDPEOStatus | STATUS | — | ✅ |
| 26 | AgreementDefinitionDPEOToEntityBasis | TO_ENTITY_BASIS | — | ✅ |
| 27 | AgreementDefinitionDPEOToEntityValue | TO_ENTITY_VALUE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
