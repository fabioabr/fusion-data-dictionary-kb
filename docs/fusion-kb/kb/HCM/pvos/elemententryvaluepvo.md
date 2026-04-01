---
id: DOC-HCM-PVO-ElementEntryValuePVO
doc_type: system-doc
title: "ElementEntryValuePVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ElementEntryValuePVO
  - elemententryvaluepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ElementEntryValuePVO

## 📌 Visão Geral

Disponibiliza valores de lançamentos de elementos de folha para análise. Permite rastrear valores históricos de proventos e descontos por colaborador.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmElementSetupAM.ElementEntryValuePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 5 | 36% |

---

## 🔗 Tabelas Relacionadas

- [[pay_element_entry_values_f|PAY_ELEMENT_ENTRY_VALUES_F]] — 14 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[pay_element_entry_values_f|PAY_ELEMENT_ENTRY_VALUES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ElementEntryValueId | ELEMENT_ENTRY_VALUE_ID | 🔑 | ✅ |
| 2 | ElementEntryValuePEOCreatedBy | CREATED_BY | — | — |
| 3 | ElementEntryValuePEOCreationDate | CREATION_DATE | — | — |
| 4 | ElementEntryValuePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 5 | ElementEntryValuePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | ElementEntryValuePEOElementEntryId | ELEMENT_ENTRY_ID | — | — |
| 7 | ElementEntryValuePEOEntryUsageId | ENTRY_USAGE_ID | — | — |
| 8 | ElementEntryValuePEOInputValueId | INPUT_VALUE_ID | — | — |
| 9 | ElementEntryValuePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ElementEntryValuePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ElementEntryValuePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ElementEntryValuePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | ElementEntryValuePEOScreenEntryValue | SCREEN_ENTRY_VALUE | — | ✅ |
| 14 | EnterpriseId | ENTERPRISE_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
