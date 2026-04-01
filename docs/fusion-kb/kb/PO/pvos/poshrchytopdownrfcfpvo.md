---
id: DOC-PO-PVO-PosHrchyTopDownRFCFPVO
doc_type: system-doc
title: "PosHrchyTopDownRFCFPVO — PVO Purchasing"
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
  - PosHrchyTopDownRFCFPVO
  - poshrchytopdownrfcfpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PosHrchyTopDownRFCFPVO

## 📌 Visão Geral

Extrai a hierarquia organizacional top-down de posições, com cadeia completa de reporte. Suporta validação de fluxos de aprovação, delegação de autoridade e análise de span of control em procurement.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PositionAM.PosHrchyTopDownRFCFPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 4 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_pos_hrchy_topdown_rf_cf_v|PER_POS_HRCHY_TOPDOWN_RF_CF_V]] — 20 atributos (4 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[per_pos_hrchy_topdown_rf_cf_v|PER_POS_HRCHY_TOPDOWN_RF_CF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChildLevel | CHILD_LEVEL | — | ✅ |
| 2 | ChildPosId1 | CHILD_POS_ID1 | — | ✅ |
| 3 | ChildPosId10 | CHILD_POS_ID10 | — | ✅ |
| 4 | ChildPosId11 | CHILD_POS_ID11 | — | ✅ |
| 5 | ChildPosId12 | CHILD_POS_ID12 | — | ✅ |
| 6 | ChildPosId13 | CHILD_POS_ID13 | — | ✅ |
| 7 | ChildPosId14 | CHILD_POS_ID14 | — | ✅ |
| 8 | ChildPosId15 | CHILD_POS_ID15 | — | ✅ |
| 9 | ChildPosId2 | CHILD_POS_ID2 | — | ✅ |
| 10 | ChildPosId3 | CHILD_POS_ID3 | — | ✅ |
| 11 | ChildPosId4 | CHILD_POS_ID4 | — | ✅ |
| 12 | ChildPosId5 | CHILD_POS_ID5 | — | ✅ |
| 13 | ChildPosId6 | CHILD_POS_ID6 | — | ✅ |
| 14 | ChildPosId7 | CHILD_POS_ID7 | — | ✅ |
| 15 | ChildPosId8 | CHILD_POS_ID8 | — | ✅ |
| 16 | ChildPosId9 | CHILD_POS_ID9 | — | ✅ |
| 17 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 18 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 19 | NonnullChildPosId15 | NONNULL_CHILD_POS_ID15 | 🔑 | ✅ |
| 20 | PositionId | POSITION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
