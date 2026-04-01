---
id: DOC-OTHER-PVO-WarrantyContractMeterExtractPVO
doc_type: system-doc
title: "WarrantyContractMeterExtractPVO — PVO Cross-Module"
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
  - WarrantyContractMeterExtractPVO
  - warrantycontractmeterextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WarrantyContractMeterExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Warranty Contract Meter Extract. Acessa as tabelas: CSE_W_CONTRACT_METERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.WarrantyContractMeterExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_w_contract_meters|CSE_W_CONTRACT_METERS]] — 17 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[cse_w_contract_meters|CSE_W_CONTRACT_METERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | CalculatedDueDate | CALCULATED_DUE_DATE | — | ✅ |
| 3 | ContractId | CONTRACT_ID | — | ✅ |
| 4 | ContractMeterId | CONTRACT_METER_ID | 🔑 | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 8 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | MeterEndValue | METER_END_VALUE | — | ✅ |
| 13 | MeterId | METER_ID | — | ✅ |
| 14 | MeterIntervalValue | METER_INTERVAL_VALUE | — | ✅ |
| 15 | MeterStartValue | METER_START_VALUE | — | ✅ |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | RequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
