---
id: DOC-OTHER-PVO-ContractRiskP
doc_type: system-doc
title: "ContractRiskP — PVO Cross-Module"
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
  - ContractRiskP
  - contractriskp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractRiskP

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Risk P. Acessa as tabelas: OKC_CONTRACT_RISKS, OKC_RISK_EVENTS_VL.

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractRiskP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 2 | 2 | 27 | 96% |

---

## 🔗 Tabelas Relacionadas

- [[okc_contract_risks|OKC_CONTRACT_RISKS]] — 16 atributos (2 PKs, 16 BICC)
- [[okc_risk_events_vl|OKC_RISK_EVENTS_VL]] — 12 atributos (11 BICC)

---

## ⚙️ Atributos

### [[okc_contract_risks|OKC_CONTRACT_RISKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChrId | CHR_ID | — | ✅ |
| 2 | Comments | COMMENTS | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | Id | ID | 🔑 | ✅ |
| 6 | ImpactCode | IMPACT_CODE | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | MajorVersion | MAJOR_VERSION | 🔑 | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | OccurrenceDate | OCCURRENCE_DATE | — | ✅ |
| 13 | ProbabilityCode | PROBABILITY_CODE | — | ✅ |
| 14 | RiskEventId1 | RISK_EVENT_ID | — | ✅ |
| 15 | RiskOccurredFlag | RISK_OCCURRED_FLAG | — | ✅ |
| 16 | VersionType | VERSION_TYPE | — | ✅ |

### [[okc_risk_events_vl|OKC_RISK_EVENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy1 | CREATED_BY | — | ✅ |
| 2 | CreationDate1 | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | EndDate | END_DATE | — | ✅ |
| 5 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 8 | Name | NAME | — | ✅ |
| 9 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | RiskEventId | RISK_EVENT_ID | — | ✅ |
| 11 | RowId1 | ROW_ID | — | — |
| 12 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
