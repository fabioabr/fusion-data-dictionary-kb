---
id: DOC-AR-PVO-MemoLinePVO
doc_type: system-doc
title: "MemoLinePVO — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - MemoLinePVO
  - memolinepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MemoLinePVO

## 📌 Visão Geral

Extrai as linhas de memorando (memo lines) configuradas para uso em notas de débito e crédito, com descrição, classificação fiscal e valores padrão. Padroniza os itens recorrentes utilizados em ajustes e cobranças avulsas.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.MemoLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 49 | 5 | 3 | 18 | 37% |

---

## 🔗 Tabelas Relacionadas

- [[ar_memo_lines_all_b|AR_MEMO_LINES_ALL_B]] — 20 atributos (9 BICC)
- [[ar_memo_lines_all_tl|AR_MEMO_LINES_ALL_TL]] — 12 atributos (3 PKs, 6 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos (2 BICC)
- [[per_users|PER_USERS]] — 4 atributos
- [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]] — 5 atributos (1 BICC)

---

## ⚙️ Atributos

### [[ar_memo_lines_all_b|AR_MEMO_LINES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MemoLineBaseAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 2 | MemoLineBaseCreatedBy1 | CREATED_BY | — | ✅ |
| 3 | MemoLineBaseCreationDate | CREATION_DATE | — | ✅ |
| 4 | MemoLineBaseDescription | DESCRIPTION | — | — |
| 5 | MemoLineBaseEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 6 | MemoLineBaseEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | MemoLineBaseInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 8 | MemoLineBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | MemoLineBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | MemoLineBaseLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 11 | MemoLineBaseLineType | LINE_TYPE | — | ✅ |
| 12 | MemoLineBaseMemoLineId | MEMO_LINE_ID | — | — |
| 13 | MemoLineBaseMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 14 | MemoLineBaseName | NAME | — | — |
| 15 | MemoLineBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | MemoLineBaseSetId | SET_ID | — | — |
| 17 | MemoLineBaseTaxCode | TAX_CODE | — | — |
| 18 | MemoLineBaseTaxProductCategory | TAX_PRODUCT_CATEGORY | — | — |
| 19 | MemoLineBaseUnitStdPrice | UNIT_STD_PRICE | — | ✅ |
| 20 | MemoLineBaseUomCode | UOM_CODE | — | — |

### [[ar_memo_lines_all_tl|AR_MEMO_LINES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MemoLineId | MEMO_LINE_ID | 🔑 | ✅ |
| 2 | MemoLineTranslationCreatedBy | CREATED_BY | — | — |
| 3 | MemoLineTranslationCreationDate | CREATION_DATE | — | — |
| 4 | MemoLineTranslationDescription | DESCRIPTION | — | ✅ |
| 5 | MemoLineTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | MemoLineTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | MemoLineTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | MemoLineTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | MemoLineTranslationName | NAME | — | ✅ |
| 10 | MemoLineTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | MemoLineTranslationSourceLang | SOURCE_LANG | — | — |
| 12 | SetId | SET_ID | 🔑 | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MemoLineBaseCreatedBy | DISPLAY_NAME | — | ✅ |
| 2 | MemoLineBaseLastUpdatedBy | DISPLAY_NAME | — | ✅ |
| 3 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByUserId | USER_ID | — | — |
| 3 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | UserUpdatedByUserId | USER_ID | — | — |

### [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductCategoriesClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | ProductCategoriesClassificationId | CLASSIFICATION_ID | — | — |
| 3 | ProductCategoriesClassificationName | CLASSIFICATION_NAME | — | ✅ |
| 4 | ProductCategoriesConcatLeafName | CONCAT_LEAF_NAME | — | — |
| 5 | ProductCategoriesCountryCode | COUNTRY_CODE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
