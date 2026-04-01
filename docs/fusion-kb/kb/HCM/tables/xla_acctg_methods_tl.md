---
id: DOC-HCM-867
doc_type: system-doc
title: "XLA_ACCTG_METHODS_TL — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - XLA_ACCTG_METHODS_TL
  - xla_acctg_methods_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# XLA_ACCTG_METHODS_TL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCOUNTING_METHOD_CODE | — | — | — | — | — | — |
| 2 | ACCOUNTING_METHOD_TYPE_CODE | — | — | — | — | — | — |
| 3 | CREATED_BY | — | — | — | — | — | — |
| 4 | CREATION_DATE | — | — | — | — | — | — |
| 5 | DESCRIPTION | — | — | — | — | — | — |
| 6 | LANGUAGE | — | — | — | — | — | — |
| 7 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 8 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 9 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 10 | NAME | — | — | — | — | — | — |
| 11 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 12 | SOURCE_LANG | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[accountingmethodextractpvo|AccountingMethodExtractPVO]] (OTHER · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_METHOD_CODE | AcctgMethodTranslationAccountingMethodCode1 | ✅ |
| ACCOUNTING_METHOD_TYPE_CODE | AcctgMethodTranslationAccountingMethodTypeCode1 | ✅ |
| CREATED_BY | AcctgMethodTranslationCreatedBy1 | ✅ |
| CREATION_DATE | AcctgMethodTranslationCreationDate1 | ✅ |
| DESCRIPTION | AcctgMethodTranslationDescription | ✅ |
| LANGUAGE | AcctgMethodTranslationLanguage | ✅ |
| LAST_UPDATE_DATE | AcctgMethodTranslationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AcctgMethodTranslationLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AcctgMethodTranslationLastUpdatedBy | ✅ |
| NAME | AcctgMethodTranslationName | ✅ |
| SOURCE_LANG | AcctgMethodTranslationSourceLang | ✅ |

### [[accountingmethodtlextractpvo|AccountingMethodTLExtractPVO]] (OTHER · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_METHOD_CODE | AcctgMethodTranslationAccountingMethodCode | ✅ |
| ACCOUNTING_METHOD_TYPE_CODE | AcctgMethodTranslationAccountingMethodTypeCode | ✅ |
| CREATED_BY | AcctgMethodTranslationCreatedBy | ✅ |
| CREATION_DATE | AcctgMethodTranslationCreationDate | ✅ |
| DESCRIPTION | AcctgMethodTranslationDescription | ✅ |
| LANGUAGE | AcctgMethodTranslationLanguage | ✅ |
| LAST_UPDATE_DATE | AcctgMethodTranslationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AcctgMethodTranslationLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AcctgMethodTranslationLastUpdatedBy | ✅ |
| NAME | AcctgMethodTranslationName | ✅ |
| OBJECT_VERSION_NUMBER | AcctgMethodTranslationObjectVersionNumber | ✅ |
| SOURCE_LANG | AcctgMethodTranslationSourceLang | ✅ |

### [[acctgmethodpvo|AcctgMethodPVO]] (OTHER · BICC: 7/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_METHOD_CODE | AcctgMethodTranslationAccountingMethodCode | ✅ |
| ACCOUNTING_METHOD_TYPE_CODE | AcctgMethodTranslationAccountingMethodTypeCode | ✅ |
| CREATED_BY | AcctgMethodTranslationCreatedBy | — |
| CREATION_DATE | AcctgMethodTranslationCreationDate | — |
| DESCRIPTION | AcctgMethodTranslationDescription | ✅ |
| LANGUAGE | AcctgMethodTranslationLanguage | ✅ |
| LAST_UPDATE_DATE | AcctgMethodTranslationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AcctgMethodTranslationLastUpdateLogin | — |
| LAST_UPDATED_BY | AcctgMethodTranslationLastUpdatedBy | — |
| NAME | AcctgMethodTranslationName | ✅ |
| OBJECT_VERSION_NUMBER | AcctgMethodTranslationObjectVersionNumber | — |
| SOURCE_LANG | AcctgMethodTranslationSourceLang | ✅ |

### [[ledgerextractpvo|LedgerExtractPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_METHOD_CODE | AcctgMethodTLAccountingMethodCode | — |
| ACCOUNTING_METHOD_TYPE_CODE | AcctgMethodTLAccountingMethodTypeCode | — |
| DESCRIPTION | AcctgMethodTLDescription | — |
| LANGUAGE | AcctgMethodTLLanguage | — |
| NAME | AcctgMethodTLName | — |

### [[ledgerpvo|LedgerPVO]] (GL · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_METHOD_CODE | AcctgMethodTransAcctngMethodCode | — |
| ACCOUNTING_METHOD_TYPE_CODE | AcctgMethodTransAcctngMethodTypeCode | — |
| DESCRIPTION | AcctgMethodDescription | ✅ |
| LANGUAGE | AcctgMethodTransLanguage | — |
| NAME | AcctgMethodName | ✅ |
