---
id: DOC-AR-PVO-DistributionRulePVO
doc_type: system-doc
title: "DistributionRulePVO — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - DistributionRulePVO
  - distributionrulepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DistributionRulePVO

## 📌 Visão Geral

Extrai as regras de distribuição de receita (revenue scheduling rules), que definem como a receita é reconhecida ao longo do tempo. Essencial para conformidade com normas de reconhecimento de receita e planejamento de fluxo de caixa.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.DistributionRulePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 3 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[ra_rules|RA_RULES]] — 16 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[ra_rules|RA_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalendarId | CALENDAR_ID | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | DeferredRevenueFlag | DEFERRED_REVENUE_FLAG | — | — |
| 5 | Description | DESCRIPTION | — | — |
| 6 | Frequency | FREQUENCY | — | — |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | Name | NAME | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | Occurrences | OCCURRENCES | — | — |
| 13 | RuleId | RULE_ID | 🔑 | ✅ |
| 14 | SetId | SET_ID | — | — |
| 15 | Status | STATUS | — | — |
| 16 | Type | TYPE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
