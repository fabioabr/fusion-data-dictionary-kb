---
id: DOC-OTHER-PVO-ElementEntryValue
doc_type: system-doc
title: "ElementEntryValue — PVO Cross-Module"
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
  - ElementEntryValue
  - elemententryvalue
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ElementEntryValue

## 📌 Visão Geral

View Object para extração BICC de dados de Element Entry Value. Acessa as tabelas: PAY_ELEMENT_ENTRY_VALUES_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmElementSetupAM.ElementEntryValue`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 3 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pay_element_entry_values_f|PAY_ELEMENT_ENTRY_VALUES_F]] — 13 atributos (3 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[pay_element_entry_values_f|PAY_ELEMENT_ENTRY_VALUES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | ElementEntryValueDPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ElementEntryValueDPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ElementEntryValueDPEOElementEntryId | ELEMENT_ENTRY_ID | — | ✅ |
| 6 | ElementEntryValueDPEOEntryUsageId | ENTRY_USAGE_ID | — | ✅ |
| 7 | ElementEntryValueDPEOInputValueId | INPUT_VALUE_ID | — | ✅ |
| 8 | ElementEntryValueDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ElementEntryValueDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | ElementEntryValueDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ElementEntryValueDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ElementEntryValueDPEOScreenEntryValue | SCREEN_ENTRY_VALUE | — | ✅ |
| 13 | ElementEntryValueId | ELEMENT_ENTRY_VALUE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
