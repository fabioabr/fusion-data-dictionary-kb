---
id: DOC-OTHER-PVO-JournalLineRuleExtractPVO
doc_type: system-doc
title: "JournalLineRuleExtractPVO — PVO Cross-Module"
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
  - JournalLineRuleExtractPVO
  - journallineruleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalLineRuleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Line Rule Extract. Acessa as tabelas: XLA_ACCT_LINE_TYPES_B, XLA_ACCT_LINE_TYPES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.JournalLineRuleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 2 | 5 | 40 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_acct_line_types_b|XLA_ACCT_LINE_TYPES_B]] — 24 atributos (5 PKs, 24 BICC)
- [[xla_acct_line_types_tl|XLA_ACCT_LINE_TYPES_TL]] — 16 atributos (16 BICC)

---

## ⚙️ Atributos

### [[xla_acct_line_types_b|XLA_ACCT_LINE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalLineRuleBaseAccountingClassCode | ACCOUNTING_CLASS_CODE | — | ✅ |
| 2 | JournalLineRuleBaseAccountingEntryTypeCode | ACCOUNTING_ENTRY_TYPE_CODE | — | ✅ |
| 3 | JournalLineRuleBaseAccountingLineCode | ACCOUNTING_LINE_CODE | 🔑 | ✅ |
| 4 | JournalLineRuleBaseAccountingLineTypeCode | ACCOUNTING_LINE_TYPE_CODE | 🔑 | ✅ |
| 5 | JournalLineRuleBaseApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 6 | JournalLineRuleBaseBusinessClassCode | BUSINESS_CLASS_CODE | — | ✅ |
| 7 | JournalLineRuleBaseBusinessMethodCode | BUSINESS_METHOD_CODE | — | ✅ |
| 8 | JournalLineRuleBaseCreatedBy | CREATED_BY | — | ✅ |
| 9 | JournalLineRuleBaseCreationDate | CREATION_DATE | — | ✅ |
| 10 | JournalLineRuleBaseEnabledFlag | ENABLED_FLAG | — | ✅ |
| 11 | JournalLineRuleBaseEntityCode | ENTITY_CODE | 🔑 | ✅ |
| 12 | JournalLineRuleBaseEventClassCode | EVENT_CLASS_CODE | 🔑 | ✅ |
| 13 | JournalLineRuleBaseGainOrLossFlag | GAIN_OR_LOSS_FLAG | — | ✅ |
| 14 | JournalLineRuleBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | JournalLineRuleBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | JournalLineRuleBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | JournalLineRuleBaseMergeDuplicateCode | MERGE_DUPLICATE_CODE | — | ✅ |
| 18 | JournalLineRuleBaseMultiperiodClassCode | MULTIPERIOD_CLASS_CODE | — | ✅ |
| 19 | JournalLineRuleBaseMultiperiodOptionFlag | MULTIPERIOD_OPTION_FLAG | — | ✅ |
| 20 | JournalLineRuleBaseNaturalSideCode | NATURAL_SIDE_CODE | — | ✅ |
| 21 | JournalLineRuleBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | JournalLineRuleBaseRoundingClassCode | ROUNDING_CLASS_CODE | — | ✅ |
| 23 | JournalLineRuleBaseSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 24 | JournalLineRuleBaseSwitchSideFlag | SWITCH_SIDE_FLAG | — | ✅ |

### [[xla_acct_line_types_tl|XLA_ACCT_LINE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalLineRuleTranslationAccountingLineCode | ACCOUNTING_LINE_CODE | — | ✅ |
| 2 | JournalLineRuleTranslationAccountingLineTypeCode | ACCOUNTING_LINE_TYPE_CODE | — | ✅ |
| 3 | JournalLineRuleTranslationAmbContextCode | AMB_CONTEXT_CODE | — | ✅ |
| 4 | JournalLineRuleTranslationApplicationId | APPLICATION_ID | — | ✅ |
| 5 | JournalLineRuleTranslationCreatedBy | CREATED_BY | — | ✅ |
| 6 | JournalLineRuleTranslationCreationDate | CREATION_DATE | — | ✅ |
| 7 | JournalLineRuleTranslationDescription | DESCRIPTION | — | ✅ |
| 8 | JournalLineRuleTranslationEntityCode | ENTITY_CODE | — | ✅ |
| 9 | JournalLineRuleTranslationEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 10 | JournalLineRuleTranslationLanguage | LANGUAGE | — | ✅ |
| 11 | JournalLineRuleTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | JournalLineRuleTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | JournalLineRuleTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | JournalLineRuleTranslationName | NAME | — | ✅ |
| 15 | JournalLineRuleTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | JournalLineRuleTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
