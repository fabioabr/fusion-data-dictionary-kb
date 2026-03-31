---
id: DOC-OTHER-PVO-FosPrimaryTradeRelationExtractPVO
doc_type: system-doc
title: "FosPrimaryTradeRelationExtractPVO — PVO Cross-Module"
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
  - FosPrimaryTradeRelationExtractPVO
  - fosprimarytraderelationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosPrimaryTradeRelationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Primary Trade Relation Extract. Acessa as tabelas: FOS_AGREEMENT_PTR_F.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosPrimaryTradeRelationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 45 | 1 | 3 | 45 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_agreement_ptr_f|FOS_AGREEMENT_PTR_F]] — 45 atributos (3 PKs, 45 BICC)

---

## ⚙️ Atributos

### [[fos_agreement_ptr_f|FOS_AGREEMENT_PTR_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrimaryTradeRelationPEOAgreementId | AGREEMENT_ID | — | ✅ |
| 2 | PrimaryTradeRelationPEOAgreementPtrId | AGREEMENT_PTR_ID | 🔑 | ✅ |
| 3 | PrimaryTradeRelationPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 4 | PrimaryTradeRelationPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 5 | PrimaryTradeRelationPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 6 | PrimaryTradeRelationPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 7 | PrimaryTradeRelationPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 8 | PrimaryTradeRelationPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 9 | PrimaryTradeRelationPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 10 | PrimaryTradeRelationPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 11 | PrimaryTradeRelationPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 12 | PrimaryTradeRelationPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 13 | PrimaryTradeRelationPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 14 | PrimaryTradeRelationPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 15 | PrimaryTradeRelationPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 16 | PrimaryTradeRelationPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 17 | PrimaryTradeRelationPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 18 | PrimaryTradeRelationPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 19 | PrimaryTradeRelationPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 20 | PrimaryTradeRelationPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 21 | PrimaryTradeRelationPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 22 | PrimaryTradeRelationPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 23 | PrimaryTradeRelationPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 24 | PrimaryTradeRelationPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 25 | PrimaryTradeRelationPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 26 | PrimaryTradeRelationPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 27 | PrimaryTradeRelationPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 28 | PrimaryTradeRelationPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 29 | PrimaryTradeRelationPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 30 | PrimaryTradeRelationPEOCreatedBy | CREATED_BY | — | ✅ |
| 31 | PrimaryTradeRelationPEOCreationDate | CREATION_DATE | — | ✅ |
| 32 | PrimaryTradeRelationPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 33 | PrimaryTradeRelationPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 34 | PrimaryTradeRelationPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 35 | PrimaryTradeRelationPEOFromBuId | FROM_BU_ID | — | ✅ |
| 36 | PrimaryTradeRelationPEOFromLeId | FROM_LE_ID | — | ✅ |
| 37 | PrimaryTradeRelationPEOFromTradeOrganizationId | FROM_TRADE_ORGANIZATION_ID | — | ✅ |
| 38 | PrimaryTradeRelationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | PrimaryTradeRelationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 40 | PrimaryTradeRelationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 41 | PrimaryTradeRelationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 42 | PrimaryTradeRelationPEOPtrNumber | PTR_NUMBER | — | ✅ |
| 43 | PrimaryTradeRelationPEOToBuId | TO_BU_ID | — | ✅ |
| 44 | PrimaryTradeRelationPEOToLeId | TO_LE_ID | — | ✅ |
| 45 | PrimaryTradeRelationPEOToTradeOrganizationId | TO_TRADE_ORGANIZATION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
