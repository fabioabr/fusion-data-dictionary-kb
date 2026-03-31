---
id: DOC-OTHER-PVO-OrderTotalExtractPVO
doc_type: system-doc
title: "OrderTotalExtractPVO — PVO Cross-Module"
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
  - OrderTotalExtractPVO
  - ordertotalextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrderTotalExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Order Total Extract. Acessa as tabelas: DOO_ORDER_TOTALS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.OrderTotalExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_order_totals|DOO_ORDER_TOTALS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[doo_order_totals|DOO_ORDER_TOTALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrderTotalCreatedBy | CREATED_BY | — | ✅ |
| 2 | OrderTotalCreationDate | CREATION_DATE | — | ✅ |
| 3 | OrderTotalCurrencyCode | CURRENCY_CODE | — | ✅ |
| 4 | OrderTotalDisplayName | DISPLAY_NAME | — | ✅ |
| 5 | OrderTotalEstimatedFlag | ESTIMATED_FLAG | — | ✅ |
| 6 | OrderTotalHeaderId | HEADER_ID | — | ✅ |
| 7 | OrderTotalId | ORDER_TOTAL_ID | 🔑 | ✅ |
| 8 | OrderTotalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | OrderTotalLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | OrderTotalLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | OrderTotalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | OrderTotalPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 13 | OrderTotalTotalAmount | TOTAL_AMOUNT | — | ✅ |
| 14 | OrderTotalTotalCode | TOTAL_CODE | — | ✅ |
| 15 | OrderTotalTotalGroup | TOTAL_GROUP | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
