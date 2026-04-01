---
id: DOC-OTHER-PVO-LearningPricingRulesPVO
doc_type: system-doc
title: "LearningPricingRulesPVO — PVO Cross-Module"
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
  - LearningPricingRulesPVO
  - learningpricingrulespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LearningPricingRulesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Learning Pricing Rules. Acessa as tabelas: WLF_PRICING_RULES_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.LearningPricingRulesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 3 | 6 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_pricing_rules_f|WLF_PRICING_RULES_F]] — 17 atributos (3 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[wlf_pricing_rules_f|WLF_PRICING_RULES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LearningPricingRulesDEOCreatedBy | CREATED_BY | — | — |
| 2 | LearningPricingRulesDEOCreationDate | CREATION_DATE | — | — |
| 3 | LearningPricingRulesDEOCurrency | CURRENCY | — | ✅ |
| 4 | LearningPricingRulesDEODeliveryMode | DELIVERY_MODE | — | — |
| 5 | LearningPricingRulesDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 6 | LearningPricingRulesDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | LearningPricingRulesDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 8 | LearningPricingRulesDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LearningPricingRulesDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LearningPricingRulesDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | LearningPricingRulesDEOLearningItemType | LEARNING_ITEM_TYPE | — | — |
| 12 | LearningPricingRulesDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | LearningPricingRulesDEOPriceLockType | PRICE_LOCK_TYPE | — | — |
| 14 | LearningPricingRulesDEOPricingRuleId | PRICING_RULE_ID | 🔑 | ✅ |
| 15 | LearningPricingRulesDEOTotalPrice | TOTAL_PRICE | — | ✅ |
| 16 | LearningPricingRulesDEOUsage | USAGE | — | — |
| 17 | LearningPricingRulesDEOUsesPricing | USES_PRICING | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
