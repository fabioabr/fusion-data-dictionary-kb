---
id: DOC-OTHER-PVO-FosTaRuleSetTranslationExtractPVO
doc_type: system-doc
title: "FosTaRuleSetTranslationExtractPVO — PVO Cross-Module"
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
  - FosTaRuleSetTranslationExtractPVO
  - fostarulesettranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosTaRuleSetTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Ta Rule Set Translation Extract. Acessa as tabelas: FOS_TA_RULE_SET_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosTaRuleSetTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 4 | 12 | 86% |

---

## 🔗 Tabelas Relacionadas

- [[fos_ta_rule_set_tl|FOS_TA_RULE_SET_TL]] — 14 atributos (4 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[fos_ta_rule_set_tl|FOS_TA_RULE_SET_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaRuleSetTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TaRuleSetTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TaRuleSetTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | TaRuleSetTLPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 5 | TaRuleSetTLPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 6 | TaRuleSetTLPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 7 | TaRuleSetTLPEOLanguage | LANGUAGE | 🔑 | — |
| 8 | TaRuleSetTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | TaRuleSetTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | TaRuleSetTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | TaRuleSetTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | TaRuleSetTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 13 | TaRuleSetTLPEOSourceLang | SOURCE_LANG | — | — |
| 14 | TaRuleSetTLPEOTaRuleSetId | TA_RULE_SET_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
