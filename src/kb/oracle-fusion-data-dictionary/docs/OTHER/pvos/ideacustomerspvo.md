---
id: DOC-OTHER-PVO-IdeaCustomersPVO
doc_type: system-doc
title: "IdeaCustomersPVO — PVO Cross-Module"
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
  - IdeaCustomersPVO
  - ideacustomerspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IdeaCustomersPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Idea Customers. Acessa as tabelas: ACN_CUSTOMER_VL.

**Caminho:** `FscmTopModelAM.IdeasAnalyticsAM.IdeaCustomersPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 1 | 8 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[acn_customer_vl|ACN_CUSTOMER_VL]] — 8 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[acn_customer_vl|ACN_CUSTOMER_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IdeaCustomerCreatedBy | CREATED_BY | — | ✅ |
| 2 | IdeaCustomerCreationDate | CREATION_DATE | — | ✅ |
| 3 | IdeaCustomerCustomerId | CUSTOMER_ID | 🔑 | ✅ |
| 4 | IdeaCustomerLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | IdeaCustomerLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | IdeaCustomerLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | IdeaCustomerName | NAME | — | ✅ |
| 8 | IdeaCustomerObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
