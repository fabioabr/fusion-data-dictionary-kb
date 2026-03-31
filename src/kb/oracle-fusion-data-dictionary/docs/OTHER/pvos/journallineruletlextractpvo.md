---
id: DOC-OTHER-PVO-JournalLineRuleTLExtractPVO
doc_type: system-doc
title: "JournalLineRuleTLExtractPVO — PVO Cross-Module"
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
  - JournalLineRuleTLExtractPVO
  - journallineruletlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalLineRuleTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Line Rule TLExtract. Acessa as tabelas: XLA_ACCT_LINE_TYPES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.JournalLineRuleTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 6 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_acct_line_types_tl|XLA_ACCT_LINE_TYPES_TL]] — 16 atributos (6 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[xla_acct_line_types_tl|XLA_ACCT_LINE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalLineRuleTranslationAccountingLineCode | ACCOUNTING_LINE_CODE | 🔑 | ✅ |
| 2 | JournalLineRuleTranslationAccountingLineTypeCode | ACCOUNTING_LINE_TYPE_CODE | 🔑 | ✅ |
| 3 | JournalLineRuleTranslationApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 4 | JournalLineRuleTranslationCreatedBy | CREATED_BY | — | ✅ |
| 5 | JournalLineRuleTranslationCreationDate | CREATION_DATE | — | ✅ |
| 6 | JournalLineRuleTranslationDescription | DESCRIPTION | — | ✅ |
| 7 | JournalLineRuleTranslationEntityCode | ENTITY_CODE | 🔑 | ✅ |
| 8 | JournalLineRuleTranslationEventClassCode | EVENT_CLASS_CODE | 🔑 | ✅ |
| 9 | JournalLineRuleTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 10 | JournalLineRuleTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | JournalLineRuleTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | JournalLineRuleTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | JournalLineRuleTranslationName | NAME | — | ✅ |
| 14 | JournalLineRuleTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | JournalLineRuleTranslationSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 16 | JournalLineRuleTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
