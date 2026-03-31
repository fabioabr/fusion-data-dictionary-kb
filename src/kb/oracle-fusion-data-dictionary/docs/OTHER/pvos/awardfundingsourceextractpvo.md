---
id: DOC-OTHER-PVO-AwardFundingSourceExtractPVO
doc_type: system-doc
title: "AwardFundingSourceExtractPVO — PVO Cross-Module"
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
  - AwardFundingSourceExtractPVO
  - awardfundingsourceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardFundingSourceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Funding Source Extract. Acessa as tabelas: GMS_AWARD_FUNDING_SOURCES_B.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardFundingSourceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_funding_sources_b|GMS_AWARD_FUNDING_SOURCES_B]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[gms_award_funding_sources_b|GMS_AWARD_FUNDING_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardFundingSrcBaseApprovalDate | APPROVAL_DATE | — | ✅ |
| 2 | AwardFundingSrcBaseApprovalPersonId | APPROVAL_PERSON_ID | — | ✅ |
| 3 | AwardFundingSrcBaseAwardId | AWARD_ID | — | ✅ |
| 4 | AwardFundingSrcBaseCreatedBy | CREATED_BY | — | ✅ |
| 5 | AwardFundingSrcBaseCreationDate | CREATION_DATE | — | ✅ |
| 6 | AwardFundingSrcBaseFundingSourceId | FUNDING_SOURCE_ID | — | ✅ |
| 7 | AwardFundingSrcBaseId | ID | 🔑 | ✅ |
| 8 | AwardFundingSrcBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | AwardFundingSrcBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | AwardFundingSrcBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | AwardFundingSrcBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | AwardFundingSrcBaseRequiredBySponsor | REQUIRED_BY_SPONSOR | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
