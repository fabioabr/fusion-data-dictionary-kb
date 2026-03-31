---
id: DOC-OTHER-PVO-AwardFundAllocationExtractPVO
doc_type: system-doc
title: "AwardFundAllocationExtractPVO — PVO Cross-Module"
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
  - AwardFundAllocationExtractPVO
  - awardfundallocationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardFundAllocationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Fund Allocation Extract. Acessa as tabelas: GMS_AWARD_FUND_ALLOCATIONS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardFundAllocationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_fund_allocations|GMS_AWARD_FUND_ALLOCATIONS]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[gms_award_fund_allocations|GMS_AWARD_FUND_ALLOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardFundAllocationPEOAwardId | AWARD_ID | — | ✅ |
| 2 | AwardFundAllocationPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | AwardFundAllocationPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | AwardFundAllocationPEOFundingAmount | FUNDING_AMOUNT | — | ✅ |
| 5 | AwardFundAllocationPEOFundingDate | FUNDING_DATE | — | ✅ |
| 6 | AwardFundAllocationPEOFundingId | FUNDING_ID | — | ✅ |
| 7 | AwardFundAllocationPEOId | ID | 🔑 | ✅ |
| 8 | AwardFundAllocationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | AwardFundAllocationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | AwardFundAllocationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | AwardFundAllocationPEOLcFundingAmount | LC_FUNDING_AMOUNT | — | ✅ |
| 12 | AwardFundAllocationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | AwardFundAllocationPEOProjectId | PROJECT_ID | — | ✅ |
| 14 | AwardFundAllocationPEOTaskId | TASK_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
