---
id: DOC-HCM-PVO-PayrollActionTypePVO
doc_type: system-doc
title: "PayrollActionTypePVO — PVO Human Capital Management"
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
  - PayrollActionTypePVO
  - payrollactiontypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PayrollActionTypePVO

## 📌 Visão Geral

Extrai tipos de ações de folha de pagamento a partir de lookups HCM. Fornece a taxonomia de operações disponíveis no processamento de payroll (cálculo, reversão, etc.).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBatchProcessCoreAM.PayrollActionTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 2 | 13 | 93% |

---

## 🔗 Tabelas Relacionadas

- [[hcm_lookups|HCM_LOOKUPS]] — 14 atributos (2 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[hcm_lookups|HCM_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | DisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 5 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 11 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 12 | Meaning | MEANING | — | ✅ |
| 13 | StartDateActive | START_DATE_ACTIVE | — | ✅ |
| 14 | Tag | TAG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
