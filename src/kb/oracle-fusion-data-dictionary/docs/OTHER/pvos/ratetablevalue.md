---
id: DOC-OTHER-PVO-RateTableValue
doc_type: system-doc
title: "RateTableValue — PVO Cross-Module"
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
  - RateTableValue
  - ratetablevalue
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RateTableValue

## 📌 Visão Geral

View Object para extração BICC de dados de Rate Table Value. Acessa as tabelas: CN_RATE_TABLE_VALUES_ALL.

**Caminho:** `FscmTopModelAM.RateTableAM.RateTableValue`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cn_rate_table_values_all|CN_RATE_TABLE_VALUES_ALL]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[cn_rate_table_values_all|CN_RATE_TABLE_VALUES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CommissionValue | COMMISSION_VALUE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | OrgId | ORG_ID | — | ✅ |
| 9 | ParentRateTableValueId | PARENT_RATE_TABLE_VALUE_ID | — | ✅ |
| 10 | RateSequence | RATE_SEQUENCE | — | ✅ |
| 11 | RateTableId | RATE_TABLE_ID | — | ✅ |
| 12 | RateTableValueId | RATE_TABLE_VALUE_ID | 🔑 | ✅ |
| 13 | SrpFormRateTableId | SRP_FORM_RATE_TABLE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
