---
id: DOC-OTHER-PVO-RiskProcessXrefPVO
doc_type: system-doc
title: "RiskProcessXrefPVO — PVO Cross-Module"
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
  - RiskProcessXrefPVO
  - riskprocessxrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RiskProcessXrefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Risk Process Xref. Acessa as tabelas: GRC_PROC_RISK_XREF, GTG_RISK_CONTROL_XREF.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.RiskProcessXrefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 2 | 2 | 3 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[grc_proc_risk_xref|GRC_PROC_RISK_XREF]] — 10 atributos (2 PKs, 3 BICC)
- [[gtg_risk_control_xref|GTG_RISK_CONTROL_XREF]] — 4 atributos

---

## ⚙️ Atributos

### [[grc_proc_risk_xref|GRC_PROC_RISK_XREF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessRiskXrefPEOCreatedBy | CREATED_BY | — | — |
| 2 | ProcessRiskXrefPEOCreationDate | CREATION_DATE | — | — |
| 3 | ProcessRiskXrefPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 4 | ProcessRiskXrefPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProcessRiskXrefPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ProcessRiskXrefPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ProcessRiskXrefPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ProcessRiskXrefPEOProcessId | PROCESS_ID | 🔑 | ✅ |
| 9 | ProcessRiskXrefPEORevisionDate | REVISION_DATE | — | — |
| 10 | ProcessRiskXrefPEORiskId | RISK_ID | 🔑 | ✅ |

### [[gtg_risk_control_xref|GTG_RISK_CONTROL_XREF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskControlXrefPEOControlEffectiveSequence | CONTROL_EFFECTIVE_SEQUENCE | — | — |
| 2 | RiskControlXrefPEOControlId | CONTROL_ID | — | — |
| 3 | RiskControlXrefPEORiskEffectiveSequence | RISK_EFFECTIVE_SEQUENCE | — | — |
| 4 | RiskControlXrefPEORiskId | RISK_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
