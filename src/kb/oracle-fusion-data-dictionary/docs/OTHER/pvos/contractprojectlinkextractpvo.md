---
id: DOC-OTHER-PVO-ContractProjectLinkExtractPVO
doc_type: system-doc
title: "ContractProjectLinkExtractPVO — PVO Cross-Module"
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
  - ContractProjectLinkExtractPVO
  - contractprojectlinkextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractProjectLinkExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Project Link Extract. Acessa as tabelas: PJB_CNTRCT_PROJ_LINKS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.ContractProjectLinkExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 2 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_cntrct_proj_links|PJB_CNTRCT_PROJ_LINKS]] — 21 atributos (2 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[pjb_cntrct_proj_links|PJB_CNTRCT_PROJ_LINKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractProjectLinkPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | ContractProjectLinkPEOBillableContractLineId | BILLABLE_CONTRACT_LINE_ID | — | ✅ |
| 3 | ContractProjectLinkPEOBillingTypeCode | BILLING_TYPE_CODE | — | ✅ |
| 4 | ContractProjectLinkPEOContractId | CONTRACT_ID | — | ✅ |
| 5 | ContractProjectLinkPEOContractLineId | CONTRACT_LINE_ID | — | ✅ |
| 6 | ContractProjectLinkPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | ContractProjectLinkPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | ContractProjectLinkPEOExternalKey1 | EXTERNAL_KEY1 | — | ✅ |
| 9 | ContractProjectLinkPEOExternalKey2 | EXTERNAL_KEY2 | — | ✅ |
| 10 | ContractProjectLinkPEOFundingAmount | FUNDING_AMOUNT | — | ✅ |
| 11 | ContractProjectLinkPEOLastRevRecogDate | LAST_REV_RECOG_DATE | — | ✅ |
| 12 | ContractProjectLinkPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | ContractProjectLinkPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | ContractProjectLinkPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ContractProjectLinkPEOLinkId | LINK_ID | 🔑 | ✅ |
| 16 | ContractProjectLinkPEOMajorVersion | MAJOR_VERSION | 🔑 | ✅ |
| 17 | ContractProjectLinkPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | ContractProjectLinkPEOPercentComplete | PERCENT_COMPLETE | — | ✅ |
| 19 | ContractProjectLinkPEOProjElementId | PROJ_ELEMENT_ID | — | ✅ |
| 20 | ContractProjectLinkPEOProjectId | PROJECT_ID | — | ✅ |
| 21 | ContractProjectLinkPEOVersionType | VERSION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
