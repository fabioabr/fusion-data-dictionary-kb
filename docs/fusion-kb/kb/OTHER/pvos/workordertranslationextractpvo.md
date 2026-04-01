---
id: DOC-OTHER-PVO-WorkOrderTranslationExtractPVO
doc_type: system-doc
title: "WorkOrderTranslationExtractPVO — PVO Cross-Module"
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
  - WorkOrderTranslationExtractPVO
  - workordertranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkOrderTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Order Translation Extract. Acessa as tabelas: WIE_WORK_ORDERS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WieBiccExtractAM.WorkOrderTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wie_work_orders_tl|WIE_WORK_ORDERS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[wie_work_orders_tl|WIE_WORK_ORDERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | WorkOrderTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WorkOrderTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | WorkOrderTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | WorkOrderTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | WorkOrderTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | WorkOrderTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | WorkOrderTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 9 | WorkOrderTLPEOWorkOrderDescription | WORK_ORDER_DESCRIPTION | — | ✅ |
| 10 | WorkOrderTLPEOWorkOrderId | WORK_ORDER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
