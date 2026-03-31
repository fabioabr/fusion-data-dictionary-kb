---
id: DOC-HCM-PVO-LearningPricingComponentsPVO
doc_type: system-doc
title: "LearningPricingComponentsPVO — PVO Human Capital Management"
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
  - LearningPricingComponentsPVO
  - learningpricingcomponentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LearningPricingComponentsPVO

## 📌 Visão Geral

Extrai componentes de precificação de treinamentos com tipo e valor. Utilizado para gestão de custos e cobrança de capacitações.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.LearningPricingComponentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 3 | 7 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_pricing_components_f|WLF_PRICING_COMPONENTS_F]] — 16 atributos (3 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[wlf_pricing_components_f|WLF_PRICING_COMPONENTS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LearningPricingComponentsDEOCreatedBy | CREATED_BY | — | — |
| 2 | LearningPricingComponentsDEOCreationDate | CREATION_DATE | — | — |
| 3 | LearningPricingComponentsDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 4 | LearningPricingComponentsDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 5 | LearningPricingComponentsDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 6 | LearningPricingComponentsDEOIsAdjustment | IS_ADJUSTMENT | — | — |
| 7 | LearningPricingComponentsDEOIsRequired | IS_REQUIRED | — | — |
| 8 | LearningPricingComponentsDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LearningPricingComponentsDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LearningPricingComponentsDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | LearningPricingComponentsDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | LearningPricingComponentsDEOPrice | PRICE | — | ✅ |
| 13 | LearningPricingComponentsDEOPricingComponentId | PRICING_COMPONENT_ID | 🔑 | ✅ |
| 14 | LearningPricingComponentsDEOPricingRuleId | PRICING_RULE_ID | — | — |
| 15 | LearningPricingComponentsDEOPricingType | PRICING_TYPE | — | ✅ |
| 16 | LearningPricingComponentsDEOUsedInCalc | USED_IN_CALC | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
