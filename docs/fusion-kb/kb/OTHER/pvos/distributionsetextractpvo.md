---
id: DOC-OTHER-PVO-DistributionSetExtractPVO
doc_type: system-doc
title: "DistributionSetExtractPVO — PVO Cross-Module"
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
  - DistributionSetExtractPVO
  - distributionsetextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DistributionSetExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Distribution Set Extract. Acessa as tabelas: AR_DISTRIBUTION_SETS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.DistributionSetExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ar_distribution_sets_all|AR_DISTRIBUTION_SETS_ALL]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[ar_distribution_sets_all|AR_DISTRIBUTION_SETS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArDistributionSetCreatedBy | CREATED_BY | — | ✅ |
| 2 | ArDistributionSetCreationDate | CREATION_DATE | — | ✅ |
| 3 | ArDistributionSetDescription | DESCRIPTION | — | ✅ |
| 4 | ArDistributionSetDistributionSetId | DISTRIBUTION_SET_ID | 🔑 | ✅ |
| 5 | ArDistributionSetDistributionSetName | DISTRIBUTION_SET_NAME | — | ✅ |
| 6 | ArDistributionSetLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ArDistributionSetLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ArDistributionSetLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ArDistributionSetObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ArDistributionSetOrgId | ORG_ID | — | ✅ |
| 11 | ArDistributionSetStatus | STATUS | — | ✅ |
| 12 | ArDistributionSetTotalPercentDistribution | TOTAL_PERCENT_DISTRIBUTION | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
