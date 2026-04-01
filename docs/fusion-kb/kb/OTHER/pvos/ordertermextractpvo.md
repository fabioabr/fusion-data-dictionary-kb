---
id: DOC-OTHER-PVO-OrderTermExtractPVO
doc_type: system-doc
title: "OrderTermExtractPVO — PVO Cross-Module"
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
  - OrderTermExtractPVO
  - ordertermextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrderTermExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Order Term Extract. Acessa as tabelas: DOO_ORDER_TERMS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.OrderTermExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_order_terms|DOO_ORDER_TERMS]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[doo_order_terms|DOO_ORDER_TERMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrderTermCreatedBy | CREATED_BY | — | ✅ |
| 2 | OrderTermCreationDate | CREATION_DATE | — | ✅ |
| 3 | OrderTermDeltaType | DELTA_TYPE | — | ✅ |
| 4 | OrderTermHeaderId | HEADER_ID | — | ✅ |
| 5 | OrderTermId | ORDER_TERM_ID | 🔑 | ✅ |
| 6 | OrderTermLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | OrderTermLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | OrderTermLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | OrderTermModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 10 | OrderTermObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | OrderTermParentEntityCode | PARENT_ENTITY_CODE | — | ✅ |
| 12 | OrderTermParentEntityId | PARENT_ENTITY_ID | — | ✅ |
| 13 | OrderTermReferenceOrderTermId | REFERENCE_ORDER_TERM_ID | — | ✅ |
| 14 | OrderTermSourceOrderTermId | SOURCE_ORDER_TERM_ID | — | ✅ |
| 15 | OrderTermTermApplicationMethod | TERM_APPLICATION_METHOD | — | ✅ |
| 16 | OrderTermTermApplicationValuePct | TERM_APPLICATION_VALUE_PCT | — | ✅ |
| 17 | OrderTermTermDuration | TERM_DURATION | — | ✅ |
| 18 | OrderTermTermEndDate | TERM_END_DATE | — | ✅ |
| 19 | OrderTermTermPeriod | TERM_PERIOD | — | ✅ |
| 20 | OrderTermTermStartDate | TERM_START_DATE | — | ✅ |
| 21 | OrderTermTermSubtypeCode | TERM_SUBTYPE_CODE | — | ✅ |
| 22 | OrderTermTermTypeCode | TERM_TYPE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
