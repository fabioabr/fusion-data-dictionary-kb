---
id: DOC-HCM-519
doc_type: system-doc
title: "IBY_PAYMENT_METHODS_TL — (título a preencher)"
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
  - IBY_PAYMENT_METHODS_TL
  - iby_payment_methods_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# IBY_PAYMENT_METHODS_TL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | DESCRIPTION | — | — | — | — | — | — |
| 4 | LANGUAGE | — | — | — | — | — | — |
| 5 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 6 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 7 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 8 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 9 | PAYMENT_METHOD_CODE | — | — | — | — | — | — |
| 10 | PAYMENT_METHOD_NAME | — | — | — | — | — | — |
| 11 | SOURCE_LANG | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | PaymentMethodLanguage | — |
| PAYMENT_METHOD_CODE | PaymentMethodCode | ✅ |
| PAYMENT_METHOD_NAME | PaymentMethodName | ✅ |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | PaymentMethodLanguage | — |
| PAYMENT_METHOD_CODE | PaymentMethodCode | ✅ |
| PAYMENT_METHOD_NAME | PaymentMethodName | ✅ |

### [[paymentmethodtranslationpvo|PaymentMethodTranslationPVO]] (OTHER · BICC: 9/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PaymentMthdBaseCreatedBy | ✅ |
| CREATION_DATE | PaymentMthdBaseCreationDate | ✅ |
| DESCRIPTION | PaymentMthdBaseDescription | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | PaymentMthdBaseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentMthdBaseLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentMthdBaseLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PaymentMthdBaseObjectVersionNumber | — |
| PAYMENT_METHOD_CODE | PaymentMethodCode | ✅ |
| PAYMENT_METHOD_NAME | PaymentMthdBasePaymentMethodName | ✅ |
| SOURCE_LANG | PaymentMthdBaseSourceLang | ✅ |
