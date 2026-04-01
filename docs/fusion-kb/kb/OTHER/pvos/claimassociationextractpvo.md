---
id: DOC-OTHER-PVO-ClaimAssociationExtractPVO
doc_type: system-doc
title: "ClaimAssociationExtractPVO — PVO Cross-Module"
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
  - ClaimAssociationExtractPVO
  - claimassociationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClaimAssociationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Claim Association Extract. Acessa as tabelas: CJM_CLAIM_ASSOCIATIONS_ALL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ClaimAssociationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_claim_associations_all|CJM_CLAIM_ASSOCIATIONS_ALL]] — 21 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[cjm_claim_associations_all|CJM_CLAIM_ASSOCIATIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssociationAcctdAmount | ASSOCIATION_ACCTD_AMOUNT | — | ✅ |
| 2 | AssociationAmount | ASSOCIATION_AMOUNT | — | ✅ |
| 3 | AssociationCurrencyCode | ASSOCIATION_CURRENCY_CODE | — | ✅ |
| 4 | AssociationId | ASSOCIATION_ID | 🔑 | ✅ |
| 5 | AssociationNumber | ASSOCIATION_NUMBER | — | ✅ |
| 6 | AssociationTrxAmount | ASSOCIATION_TRX_AMOUNT | — | ✅ |
| 7 | AssociationTrxCurrCode | ASSOCIATION_TRX_CURR_CODE | — | ✅ |
| 8 | AssociationTypeCode | ASSOCIATION_TYPE_CODE | — | ✅ |
| 9 | BuId | BU_ID | — | ✅ |
| 10 | ClaimId | CLAIM_ID | — | ✅ |
| 11 | ClaimLineId | CLAIM_LINE_ID | — | ✅ |
| 12 | CreatedBy | CREATED_BY | — | ✅ |
| 13 | CreationDate | CREATION_DATE | — | ✅ |
| 14 | ItemId | ITEM_ID | — | ✅ |
| 15 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 16 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 20 | ProgramHeaderId | PROGRAM_HEADER_ID | — | ✅ |
| 21 | RequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
