---
id: DOC-OTHER-PVO-RiskControlXrefPVO
doc_type: system-doc
title: "RiskControlXrefPVO — PVO Cross-Module"
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
  - RiskControlXrefPVO
  - riskcontrolxrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RiskControlXrefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Risk Control Xref. Acessa as tabelas: GTG_RISK_CONTROL_XREF.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.RiskControlXrefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 4 | 1 | 2 | 2 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[gtg_risk_control_xref|GTG_RISK_CONTROL_XREF]] — 4 atributos (2 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[gtg_risk_control_xref|GTG_RISK_CONTROL_XREF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskControlXrefPEOControlEffectiveSequence | CONTROL_EFFECTIVE_SEQUENCE | — | — |
| 2 | RiskControlXrefPEOControlId | CONTROL_ID | 🔑 | ✅ |
| 3 | RiskControlXrefPEORiskEffectiveSequence | RISK_EFFECTIVE_SEQUENCE | — | — |
| 4 | RiskControlXrefPEORiskId | RISK_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
