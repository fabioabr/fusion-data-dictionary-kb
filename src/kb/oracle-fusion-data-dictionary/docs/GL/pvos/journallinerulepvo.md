---
id: DOC-GL-PVO-JournalLineRulePVO
doc_type: system-doc
title: "JournalLineRulePVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - JournalLineRulePVO
  - journallinerulepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalLineRulePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Line Rule. Acessa as tabelas: XLA_ACCT_LINE_TYPES_B, XLA_ACCT_LINE_TYPES_TL.

**Caminho:** `FscmTopModelAM.FinXlaJrnlEnterJrnlAM.JournalLineRulePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 47 | 2 | 6 | 7 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[xla_acct_line_types_b|XLA_ACCT_LINE_TYPES_B]] — 30 atributos (6 PKs, 6 BICC)
- [[xla_acct_line_types_tl|XLA_ACCT_LINE_TYPES_TL]] — 17 atributos (1 BICC)

---

## ⚙️ Atributos

### [[xla_acct_line_types_b|XLA_ACCT_LINE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalLineRuleBaseAccountingClassCode | ACCOUNTING_CLASS_CODE | — | — |
| 2 | JournalLineRuleBaseAccountingEntryTypeCode | ACCOUNTING_ENTRY_TYPE_CODE | — | — |
| 3 | JournalLineRuleBaseAccountingLineCode | ACCOUNTING_LINE_CODE | 🔑 | ✅ |
| 4 | JournalLineRuleBaseAccountingLineTypeCode | ACCOUNTING_LINE_TYPE_CODE | 🔑 | ✅ |
| 5 | JournalLineRuleBaseAmbContextCode | AMB_CONTEXT_CODE | 🔑 | ✅ |
| 6 | JournalLineRuleBaseApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 7 | JournalLineRuleBaseBusinessClassCode | BUSINESS_CLASS_CODE | — | — |
| 8 | JournalLineRuleBaseBusinessMethodCode | BUSINESS_METHOD_CODE | — | — |
| 9 | JournalLineRuleBaseCreatedBy | CREATED_BY | — | — |
| 10 | JournalLineRuleBaseCreationDate | CREATION_DATE | — | — |
| 11 | JournalLineRuleBaseCrossLedgerBalancingFlag | CROSS_LEDGER_BALANCING_FLAG | — | — |
| 12 | JournalLineRuleBaseEnabledFlag | ENABLED_FLAG | — | — |
| 13 | JournalLineRuleBaseEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | — |
| 14 | JournalLineRuleBaseEntityCode | ENTITY_CODE | 🔑 | ✅ |
| 15 | JournalLineRuleBaseEventClassCode | EVENT_CLASS_CODE | 🔑 | ✅ |
| 16 | JournalLineRuleBaseGainOrLossFlag | GAIN_OR_LOSS_FLAG | — | — |
| 17 | JournalLineRuleBaseGlTransferModeCode | GL_TRANSFER_MODE_CODE | — | — |
| 18 | JournalLineRuleBaseLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 19 | JournalLineRuleBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | JournalLineRuleBaseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | JournalLineRuleBaseMergeDuplicateCode | MERGE_DUPLICATE_CODE | — | — |
| 22 | JournalLineRuleBaseMpaOptionCode | MPA_OPTION_CODE | — | — |
| 23 | JournalLineRuleBaseMultiperiodClassCode | MULTIPERIOD_CLASS_CODE | — | — |
| 24 | JournalLineRuleBaseMultiperiodOptionFlag | MULTIPERIOD_OPTION_FLAG | — | — |
| 25 | JournalLineRuleBaseNaturalSideCode | NATURAL_SIDE_CODE | — | — |
| 26 | JournalLineRuleBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | JournalLineRuleBaseRoundingClassCode | ROUNDING_CLASS_CODE | — | — |
| 28 | JournalLineRuleBaseSeedDataSource | SEED_DATA_SOURCE | — | — |
| 29 | JournalLineRuleBaseSwitchSideFlag | SWITCH_SIDE_FLAG | — | — |
| 30 | JournalLineRuleBaseTransactionCoaId | TRANSACTION_COA_ID | — | — |

### [[xla_acct_line_types_tl|XLA_ACCT_LINE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalLineRuleTLAccountingLineCode | ACCOUNTING_LINE_CODE | — | — |
| 2 | JournalLineRuleTLAccountingLineTypeCode | ACCOUNTING_LINE_TYPE_CODE | — | — |
| 3 | JournalLineRuleTLAmbContextCode | AMB_CONTEXT_CODE | — | — |
| 4 | JournalLineRuleTLApplicationId | APPLICATION_ID | — | — |
| 5 | JournalLineRuleTLCreatedBy | CREATED_BY | — | — |
| 6 | JournalLineRuleTLCreationDate | CREATION_DATE | — | — |
| 7 | JournalLineRuleTLDescription | DESCRIPTION | — | — |
| 8 | JournalLineRuleTLEntityCode | ENTITY_CODE | — | — |
| 9 | JournalLineRuleTLEventClassCode | EVENT_CLASS_CODE | — | — |
| 10 | JournalLineRuleTLLanguage | LANGUAGE | — | — |
| 11 | JournalLineRuleTLLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 12 | JournalLineRuleTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | JournalLineRuleTLLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | JournalLineRuleTLName | NAME | — | ✅ |
| 15 | JournalLineRuleTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | JournalLineRuleTLSeedDataSource | SEED_DATA_SOURCE | — | — |
| 17 | JournalLineRuleTLSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
