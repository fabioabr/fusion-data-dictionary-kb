---
id: DOC-OTHER-PVO-BillingMethodTLExtractPVO
doc_type: system-doc
title: "BillingMethodTLExtractPVO — PVO Cross-Module"
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
  - BillingMethodTLExtractPVO
  - billingmethodtlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillingMethodTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Billing Method TLExtract. Acessa as tabelas: PJB_BILLING_METHODS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.BillingMethodTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_billing_methods_tl|PJB_BILLING_METHODS_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjb_billing_methods_tl|PJB_BILLING_METHODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillingMethodTLPEOBillMethodDesc | BILL_METHOD_DESC | — | ✅ |
| 2 | BillingMethodTLPEOBillMethodId | BILL_METHOD_ID | 🔑 | ✅ |
| 3 | BillingMethodTLPEOBillMethodName | BILL_METHOD_NAME | — | ✅ |
| 4 | BillingMethodTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | BillingMethodTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | BillingMethodTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | BillingMethodTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | BillingMethodTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | BillingMethodTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | BillingMethodTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | BillingMethodTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | BillingMethodTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
