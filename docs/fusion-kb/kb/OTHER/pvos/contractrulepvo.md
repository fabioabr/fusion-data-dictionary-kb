---
id: DOC-OTHER-PVO-ContractRulePVO
doc_type: system-doc
title: "ContractRulePVO — PVO Cross-Module"
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
  - ContractRulePVO
  - contractrulepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractRulePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Rule. Acessa as tabelas: VRM_CONTRACT_RULES_B, VRM_CONTRACT_RULES_TL.

**Caminho:** `FscmTopModelAM.FinVrmRRSharedPublicModelAM.ContractRulePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 55 | 2 | 2 | 11 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[vrm_contract_rules_b|VRM_CONTRACT_RULES_B]] — 44 atributos (6 BICC)
- [[vrm_contract_rules_tl|VRM_CONTRACT_RULES_TL]] — 11 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[vrm_contract_rules_b|VRM_CONTRACT_RULES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractRuleBaseAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ContractRuleBaseAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ContractRuleBaseAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ContractRuleBaseAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ContractRuleBaseAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ContractRuleBaseAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ContractRuleBaseAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ContractRuleBaseAttribute16 | ATTRIBUTE16 | — | — |
| 9 | ContractRuleBaseAttribute17 | ATTRIBUTE17 | — | — |
| 10 | ContractRuleBaseAttribute18 | ATTRIBUTE18 | — | — |
| 11 | ContractRuleBaseAttribute19 | ATTRIBUTE19 | — | — |
| 12 | ContractRuleBaseAttribute2 | ATTRIBUTE2 | — | — |
| 13 | ContractRuleBaseAttribute20 | ATTRIBUTE20 | — | — |
| 14 | ContractRuleBaseAttribute3 | ATTRIBUTE3 | — | — |
| 15 | ContractRuleBaseAttribute4 | ATTRIBUTE4 | — | — |
| 16 | ContractRuleBaseAttribute5 | ATTRIBUTE5 | — | — |
| 17 | ContractRuleBaseAttribute6 | ATTRIBUTE6 | — | — |
| 18 | ContractRuleBaseAttribute7 | ATTRIBUTE7 | — | — |
| 19 | ContractRuleBaseAttribute8 | ATTRIBUTE8 | — | — |
| 20 | ContractRuleBaseAttribute9 | ATTRIBUTE9 | — | — |
| 21 | ContractRuleBaseAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | ContractRuleBaseAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | ContractRuleBaseAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | ContractRuleBaseAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | ContractRuleBaseAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | ContractRuleBaseAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | ContractRuleBaseAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | ContractRuleBaseAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 29 | ContractRuleBaseAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 30 | ContractRuleBaseAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 31 | ContractRuleBaseAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 32 | ContractRuleBaseClassificationCode | CLASSIFICATION_CODE | — | ✅ |
| 33 | ContractRuleBaseContractRuleId | CONTRACT_RULE_ID | — | — |
| 34 | ContractRuleBaseCreatedBy | CREATED_BY | — | — |
| 35 | ContractRuleBaseCreatedFrom | CREATED_FROM | — | — |
| 36 | ContractRuleBaseCreationDate | CREATION_DATE | — | — |
| 37 | ContractRuleBaseEnabledFlag | ENABLED_FLAG | — | ✅ |
| 38 | ContractRuleBaseFreezeDays | FREEZE_DAYS | — | ✅ |
| 39 | ContractRuleBaseInUseFlag | IN_USE_FLAG | — | ✅ |
| 40 | ContractRuleBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | ContractRuleBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 42 | ContractRuleBaseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 43 | ContractRuleBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 44 | ContractRuleBasePriority | PRIORITY | — | ✅ |

### [[vrm_contract_rules_tl|VRM_CONTRACT_RULES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractRuleId | CONTRACT_RULE_ID | 🔑 | ✅ |
| 2 | ContractRuleTranslationCreatedBy | CREATED_BY | — | — |
| 3 | ContractRuleTranslationCreationDate | CREATION_DATE | — | — |
| 4 | ContractRuleTranslationDescription | DESCRIPTION | — | ✅ |
| 5 | ContractRuleTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | ContractRuleTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ContractRuleTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ContractRuleTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ContractRuleTranslationName | NAME | — | ✅ |
| 10 | ContractRuleTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ContractRuleTranslationSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
