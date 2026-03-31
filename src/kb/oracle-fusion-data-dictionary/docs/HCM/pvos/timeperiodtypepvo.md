---
id: DOC-HCM-PVO-TimePeriodTypePVO
doc_type: system-doc
title: "TimePeriodTypePVO — PVO Human Capital Management"
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
  - TimePeriodTypePVO
  - timeperiodtypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimePeriodTypePVO

## 📌 Visão Geral

Extrai tipos de período de tempo com frequência anual e classificação. Define categorias de periodicidade (mensal, semanal, quinzenal) para processamento de payroll.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayCoreAM.TimePeriodTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 2 | 3 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[pay_time_period_types|PAY_TIME_PERIOD_TYPES]] — 16 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[pay_time_period_types|PAY_TIME_PERIOD_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NumberPerFiscalYear | NUMBER_PER_FISCAL_YEAR | 🔑 | ✅ |
| 2 | PeriodType | PERIOD_TYPE | 🔑 | ✅ |
| 3 | TimePeriodTypePEOCreatedBy | CREATED_BY | — | — |
| 4 | TimePeriodTypePEOCreationDate | CREATION_DATE | — | — |
| 5 | TimePeriodTypePEODescription | DESCRIPTION | — | — |
| 6 | TimePeriodTypePEODisplayPeriodType | DISPLAY_PERIOD_TYPE | — | — |
| 7 | TimePeriodTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | TimePeriodTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | TimePeriodTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | TimePeriodTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | TimePeriodTypePEOProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 12 | TimePeriodTypePEOProgramId | PROGRAM_ID | — | — |
| 13 | TimePeriodTypePEOProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 14 | TimePeriodTypePEORequestId | REQUEST_ID | — | — |
| 15 | TimePeriodTypePEOSystemFlag | SYSTEM_FLAG | — | — |
| 16 | TimePeriodTypePEOYearTypeInName | YEAR_TYPE_IN_NAME | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
