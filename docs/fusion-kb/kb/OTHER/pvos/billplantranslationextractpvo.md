---
id: DOC-OTHER-PVO-BillPlanTranslationExtractPVO
doc_type: system-doc
title: "BillPlanTranslationExtractPVO — PVO Cross-Module"
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
  - BillPlanTranslationExtractPVO
  - billplantranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillPlanTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bill Plan Translation Extract. Acessa as tabelas: PJB_BILL_PLANS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.BillPlanTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 3 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_bill_plans_tl|PJB_BILL_PLANS_TL]] — 14 atributos (3 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[pjb_bill_plans_tl|PJB_BILL_PLANS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillPlanTranslationPEOBillPlanDesc | BILL_PLAN_DESC | — | ✅ |
| 2 | BillPlanTranslationPEOBillPlanId | BILL_PLAN_ID | 🔑 | ✅ |
| 3 | BillPlanTranslationPEOBillPlanName | BILL_PLAN_NAME | — | ✅ |
| 4 | BillPlanTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | BillPlanTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | BillPlanTranslationPEOInvoiceComment | INVOICE_COMMENT | — | ✅ |
| 7 | BillPlanTranslationPEOInvoiceInstructions | INVOICE_INSTRUCTIONS | — | ✅ |
| 8 | BillPlanTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 9 | BillPlanTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | BillPlanTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | BillPlanTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | BillPlanTranslationPEOMajorVersion | MAJOR_VERSION | 🔑 | ✅ |
| 13 | BillPlanTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | BillPlanTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
