---
id: DOC-OTHER-PVO-QualifierRulePVO
doc_type: system-doc
title: "QualifierRulePVO — PVO Cross-Module"
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
  - QualifierRulePVO
  - qualifierrulepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualifierRulePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Qualifier Rule. Acessa as tabelas: FOS_QUALIFIER_DEFINITIONS_VL, FOS_QUALIFIER_RULES, FOS_QUALIFIER_RULE_SET.

**Caminho:** `FscmTopModelAM.FosOrchestrationProcessAM.QualifierRulePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 42 | 3 | 2 | 41 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[fos_qualifier_definitions_vl|FOS_QUALIFIER_DEFINITIONS_VL]] — 15 atributos (14 BICC)
- [[fos_qualifier_rules|FOS_QUALIFIER_RULES]] — 16 atributos (1 PKs, 16 BICC)
- [[fos_qualifier_rule_set|FOS_QUALIFIER_RULE_SET]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[fos_qualifier_definitions_vl|FOS_QUALIFIER_DEFINITIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualifierDefinitionPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | QualifierDefinitionPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | QualifierDefinitionPEODropShipQualifierFlag | DROP_SHIP_QUALIFIER_FLAG | — | ✅ |
| 4 | QualifierDefinitionPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | QualifierDefinitionPEOGpQualifierFlag | GP_QUALIFIER_FLAG | — | ✅ |
| 6 | QualifierDefinitionPEOImtQualifierFlag | IMT_QUALIFIER_FLAG | — | ✅ |
| 7 | QualifierDefinitionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | QualifierDefinitionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | QualifierDefinitionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | QualifierDefinitionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | QualifierDefinitionPEOQualifierCode | QUALIFIER_CODE | — | ✅ |
| 12 | QualifierDefinitionPEOQualifierId | QUALIFIER_ID | — | ✅ |
| 13 | QualifierDefinitionPEOQualifierMeaning | QUALIFIER_MEANING | — | ✅ |
| 14 | QualifierDefinitionPEOServiceSalesQualifierFlag | SERVICE_SALES_QUALIFIER_FLAG | — | — |
| 15 | QualifierDefinitionPEOShipmentQualifierFlag | SHIPMENT_QUALIFIER_FLAG | — | ✅ |

### [[fos_qualifier_rules|FOS_QUALIFIER_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualifierRulePEOCloseBrace | CLOSE_BRACE | — | ✅ |
| 2 | QualifierRulePEOConjunction | CONJUNCTION | — | ✅ |
| 3 | QualifierRulePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | QualifierRulePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | QualifierRulePEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 6 | QualifierRulePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | QualifierRulePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | QualifierRulePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | QualifierRulePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | QualifierRulePEOOpenBrace | OPEN_BRACE | — | ✅ |
| 11 | QualifierRulePEOQualifierCode | QUALIFIER_CODE | — | ✅ |
| 12 | QualifierRulePEOQualifierOperator | QUALIFIER_OPERATOR | — | ✅ |
| 13 | QualifierRulePEOQualifierRuleLineId | QUALIFIER_RULE_LINE_ID | 🔑 | ✅ |
| 14 | QualifierRulePEOQualifierRuleLineNumber | QUALIFIER_RULE_LINE_NUMBER | — | ✅ |
| 15 | QualifierRulePEOQualifierRuleSetId | QUALIFIER_RULE_SET_ID | — | ✅ |
| 16 | QualifierRulePEOValue | VALUE | — | ✅ |

### [[fos_qualifier_rule_set|FOS_QUALIFIER_RULE_SET]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualifierRuleSetPEOAgreementType | AGREEMENT_TYPE | — | ✅ |
| 2 | QualifierRuleSetPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | QualifierRuleSetPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | QualifierRuleSetPEODescription | DESCRIPTION | — | ✅ |
| 5 | QualifierRuleSetPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 6 | QualifierRuleSetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | QualifierRuleSetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | QualifierRuleSetPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | QualifierRuleSetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | QualifierRuleSetPEOQualifierRuleSetId | QUALIFIER_RULE_SET_ID | 🔑 | ✅ |
| 11 | QualifierRuleSetPEOQualifierRuleSetName | QUALIFIER_RULE_SET_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
