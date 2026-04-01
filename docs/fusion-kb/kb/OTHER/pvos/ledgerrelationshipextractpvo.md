---
id: DOC-OTHER-PVO-LedgerRelationshipExtractPVO
doc_type: system-doc
title: "LedgerRelationshipExtractPVO — PVO Cross-Module"
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
  - LedgerRelationshipExtractPVO
  - ledgerrelationshipextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LedgerRelationshipExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ledger Relationship Extract. Acessa as tabelas: GL_LEDGER_RELATIONSHIPS.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.LedgerRelationshipExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 1 | 1 | 38 | 70% |

---

## 🔗 Tabelas Relacionadas

- [[gl_ledger_relationships|GL_LEDGER_RELATIONSHIPS]] — 54 atributos (1 PKs, 38 BICC)

---

## ⚙️ Atributos

### [[gl_ledger_relationships|GL_LEDGER_RELATIONSHIPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgerRelationshipsAlcDefaultConvRateType | ALC_DEFAULT_CONV_RATE_TYPE | — | ✅ |
| 2 | GlLedgerRelationshipsAlcInheritConversionType | ALC_INHERIT_CONVERSION_TYPE | — | ✅ |
| 3 | GlLedgerRelationshipsAlcInitConvOptionCode | ALC_INIT_CONV_OPTION_CODE | — | ✅ |
| 4 | GlLedgerRelationshipsAlcInitDate | ALC_INIT_DATE | — | ✅ |
| 5 | GlLedgerRelationshipsAlcInitPeriod | ALC_INIT_PERIOD | — | ✅ |
| 6 | GlLedgerRelationshipsAlcInitializingRateDate | ALC_INITIALIZING_RATE_DATE | — | ✅ |
| 7 | GlLedgerRelationshipsAlcInitializingRateType | ALC_INITIALIZING_RATE_TYPE | — | ✅ |
| 8 | GlLedgerRelationshipsAlcMaxDaysRollRate | ALC_MAX_DAYS_ROLL_RATE | — | ✅ |
| 9 | GlLedgerRelationshipsAlcNoRateActionCode | ALC_NO_RATE_ACTION_CODE | — | ✅ |
| 10 | GlLedgerRelationshipsAlcPeriodAverageRateType | ALC_PERIOD_AVERAGE_RATE_TYPE | — | ✅ |
| 11 | GlLedgerRelationshipsAlcPeriodEndRateType | ALC_PERIOD_END_RATE_TYPE | — | ✅ |
| 12 | GlLedgerRelationshipsApplicationId | APPLICATION_ID | — | ✅ |
| 13 | GlLedgerRelationshipsAttribute1 | ATTRIBUTE1 | — | — |
| 14 | GlLedgerRelationshipsAttribute10 | ATTRIBUTE10 | — | — |
| 15 | GlLedgerRelationshipsAttribute11 | ATTRIBUTE11 | — | — |
| 16 | GlLedgerRelationshipsAttribute12 | ATTRIBUTE12 | — | — |
| 17 | GlLedgerRelationshipsAttribute13 | ATTRIBUTE13 | — | — |
| 18 | GlLedgerRelationshipsAttribute14 | ATTRIBUTE14 | — | — |
| 19 | GlLedgerRelationshipsAttribute15 | ATTRIBUTE15 | — | — |
| 20 | GlLedgerRelationshipsAttribute2 | ATTRIBUTE2 | — | — |
| 21 | GlLedgerRelationshipsAttribute3 | ATTRIBUTE3 | — | — |
| 22 | GlLedgerRelationshipsAttribute4 | ATTRIBUTE4 | — | — |
| 23 | GlLedgerRelationshipsAttribute5 | ATTRIBUTE5 | — | — |
| 24 | GlLedgerRelationshipsAttribute6 | ATTRIBUTE6 | — | — |
| 25 | GlLedgerRelationshipsAttribute7 | ATTRIBUTE7 | — | — |
| 26 | GlLedgerRelationshipsAttribute8 | ATTRIBUTE8 | — | — |
| 27 | GlLedgerRelationshipsAttribute9 | ATTRIBUTE9 | — | — |
| 28 | GlLedgerRelationshipsAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 29 | GlLedgerRelationshipsAutomaticPostFlag | AUTOMATIC_POST_FLAG | — | ✅ |
| 30 | GlLedgerRelationshipsCreatedBy | CREATED_BY | — | ✅ |
| 31 | GlLedgerRelationshipsCreationDate | CREATION_DATE | — | ✅ |
| 32 | GlLedgerRelationshipsDisableConversionDate | DISABLE_CONVERSION_DATE | — | ✅ |
| 33 | GlLedgerRelationshipsGlJeConversionSetId | GL_JE_CONVERSION_SET_ID | — | ✅ |
| 34 | GlLedgerRelationshipsInheritCreationUserFlag | INHERIT_CREATION_USER_FLAG | — | ✅ |
| 35 | GlLedgerRelationshipsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | GlLedgerRelationshipsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 37 | GlLedgerRelationshipsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 38 | GlLedgerRelationshipsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 39 | GlLedgerRelationshipsOrgId | ORG_ID | — | ✅ |
| 40 | GlLedgerRelationshipsOwnerEquityXlationRuleCode | OE_XLATION_RULE_CODE | — | ✅ |
| 41 | GlLedgerRelationshipsPrimaryLedgerId | PRIMARY_LEDGER_ID | — | ✅ |
| 42 | GlLedgerRelationshipsRelationshipEnabledFlag | RELATIONSHIP_ENABLED_FLAG | — | ✅ |
| 43 | GlLedgerRelationshipsRelationshipId | RELATIONSHIP_ID | 🔑 | ✅ |
| 44 | GlLedgerRelationshipsRelationshipTypeCode | RELATIONSHIP_TYPE_CODE | — | ✅ |
| 45 | GlLedgerRelationshipsRevExpXlationRuleCode | REV_EXP_XLATION_RULE_CODE | — | ✅ |
| 46 | GlLedgerRelationshipsSlCoaMappingId | SL_COA_MAPPING_ID | — | ✅ |
| 47 | GlLedgerRelationshipsSlaLedgerId | SLA_LEDGER_ID | — | ✅ |
| 48 | GlLedgerRelationshipsSourceLedgerId | SOURCE_LEDGER_ID | — | ✅ |
| 49 | GlLedgerRelationshipsStatusCode | STATUS_CODE | — | ✅ |
| 50 | GlLedgerRelationshipsTargetCurrencyCode | TARGET_CURRENCY_CODE | — | ✅ |
| 51 | GlLedgerRelationshipsTargetLedgerCategoryCode | TARGET_LEDGER_CATEGORY_CODE | — | ✅ |
| 52 | GlLedgerRelationshipsTargetLedgerId | TARGET_LEDGER_ID | — | ✅ |
| 53 | GlLedgerRelationshipsTargetLedgerName | TARGET_LEDGER_NAME | — | ✅ |
| 54 | GlLedgerRelationshipsTargetLedgerShortName | TARGET_LEDGER_SHORT_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
