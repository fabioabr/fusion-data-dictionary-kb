---
id: DOC-AP-PVO-AgingPeriodLinePVO
doc_type: system-doc
title: "AgingPeriodLinePVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - AgingPeriodLinePVO
  - agingperiodlinepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AgingPeriodLinePVO

## 📌 Visão Geral

Extrai as configurações de períodos de aging (envelhecimento) de contas a pagar, incluindo faixas de dias de atraso, sequência de períodos e cabeçalhos de relatório. Essencial para análise de aging de fornecedores, monitoramento de inadimplência e gestão do ciclo de pagamento.

**Caminho:** `FscmTopModelAM.FinApInvSetupAgingPeriodsPublicModelAM.AgingPeriodLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 1 | 13 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[ap_aging_periods|AP_AGING_PERIODS]] — 10 atributos (3 BICC)
- [[ap_aging_period_lines|AP_AGING_PERIOD_LINES]] — 15 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[ap_aging_periods|AP_AGING_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgingHeaderAgingPeriodId | AGING_PERIOD_ID | — | — |
| 2 | AgingHeaderCreatedBy | CREATED_BY | — | — |
| 3 | AgingHeaderCreationDate | CREATION_DATE | — | — |
| 4 | AgingHeaderDescription | DESCRIPTION | — | — |
| 5 | AgingHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AgingHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | AgingHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | AgingHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | AgingHeaderPeriodName | PERIOD_NAME | — | ✅ |
| 10 | AgingHeaderStatus | STATUS | — | ✅ |

### [[ap_aging_period_lines|AP_AGING_PERIOD_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgingLinesAgingPeriodId | AGING_PERIOD_ID | — | — |
| 2 | AgingLinesCreatedBy | CREATED_BY | — | ✅ |
| 3 | AgingLinesCreationDate | CREATION_DATE | — | ✅ |
| 4 | AgingLinesDaysStart | DAYS_START | — | ✅ |
| 5 | AgingLinesDaysTo | DAYS_TO | — | ✅ |
| 6 | AgingLinesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AgingLinesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AgingLinesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AgingLinesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | AgingLinesPeriodSequenceNum | PERIOD_SEQUENCE_NUM | — | ✅ |
| 11 | AgingLinesReportHeading1 | REPORT_HEADING1 | — | ✅ |
| 12 | AgingLinesReportHeading2 | REPORT_HEADING2 | — | ✅ |
| 13 | AgingLinesReportHeading3 | REPORT_HEADING3 | — | — |
| 14 | AgingLinesType | TYPE | — | — |
| 15 | AgingPeriodLineId | AGING_PERIOD_LINE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
