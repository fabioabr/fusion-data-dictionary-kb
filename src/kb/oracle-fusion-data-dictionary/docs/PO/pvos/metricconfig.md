---
id: DOC-PO-PVO-MetricConfig
doc_type: system-doc
title: "MetricConfig — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - MetricConfig
  - metricconfig
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MetricConfig

## 📌 Visão Geral

Extrai configurações de métricas e KPIs de procurement, incluindo nome, fórmula, unidade e thresholds. Suporta a definição e governança de indicadores de desempenho de compras.

**Caminho:** `FscmTopModelAM.PortfolioAnalyticsAM.MetricConfig`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 2 | 3 | 6 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[ace_metric_config_b|ACE_METRIC_CONFIG_B]] — 16 atributos (1 PKs, 3 BICC)
- [[ace_metric_config_tl|ACE_METRIC_CONFIG_TL]] — 12 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[ace_metric_config_b|ACE_METRIC_CONFIG_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MetricConfigColumnName | COLUMN_NAME | — | ✅ |
| 2 | MetricConfigCreatedBy | CREATED_BY | — | — |
| 3 | MetricConfigCreationDate | CREATION_DATE | — | — |
| 4 | MetricConfigDataType | DATA_TYPE | — | — |
| 5 | MetricConfigDefaultSelected | DEFAULT_SELECTED | — | — |
| 6 | MetricConfigIsEnabled | IS_ENABLED | — | — |
| 7 | MetricConfigIsSystem | IS_SYSTEM | — | — |
| 8 | MetricConfigLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | MetricConfigLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | MetricConfigLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | MetricConfigMaxValue | MAX_VALUE | — | — |
| 12 | MetricConfigMetricConfigId | METRIC_CONFIG_ID | 🔑 | ✅ |
| 13 | MetricConfigMetricType | METRIC_TYPE | — | — |
| 14 | MetricConfigMinValue | MIN_VALUE | — | — |
| 15 | MetricConfigObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | MetricConfigTableName | TABLE_NAME | — | — |

### [[ace_metric_config_tl|ACE_METRIC_CONFIG_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MetricConfigTLCreatedBy | CREATED_BY | — | — |
| 2 | MetricConfigTLCreationDate | CREATION_DATE | — | — |
| 3 | MetricConfigTLDescription | DESCRIPTION | — | — |
| 4 | MetricConfigTLDisplayLabel | DISPLAY_LABEL | — | — |
| 5 | MetricConfigTLErrorMessage | ERROR_MESSAGE | — | — |
| 6 | MetricConfigTLLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | MetricConfigTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | MetricConfigTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | MetricConfigTLLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | MetricConfigTLMetricConfigId | METRIC_CONFIG_ID | 🔑 | ✅ |
| 11 | MetricConfigTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | MetricConfigTLSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
