---
id: DOC-OTHER-PVO-FosSystemOptionsExtractPVO
doc_type: system-doc
title: "FosSystemOptionsExtractPVO — PVO Cross-Module"
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
  - FosSystemOptionsExtractPVO
  - fossystemoptionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosSystemOptionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos System Options Extract. Acessa as tabelas: FOS_SYSTEM_OPTIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosSystemOptionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_system_options|FOS_SYSTEM_OPTIONS]] — 18 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[fos_system_options|FOS_SYSTEM_OPTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SystemOptionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | SystemOptionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | SystemOptionsPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 4 | SystemOptionsPEOIgnoreBillOnlyFlag | IGNORE_BILL_ONLY_FLAG | — | ✅ |
| 5 | SystemOptionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SystemOptionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | SystemOptionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | SystemOptionsPEOMultiFtrFlag | MULTI_FTR_FLAG | — | ✅ |
| 9 | SystemOptionsPEONativeSystemCode | NATIVE_SYSTEM_CODE | — | ✅ |
| 10 | SystemOptionsPEONativeSystemId | NATIVE_SYSTEM_ID | — | ✅ |
| 11 | SystemOptionsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | SystemOptionsPEOPartyTaxRegnOverrideFlag | PARTY_TAX_REGN_OVERRIDE_FLAG | — | ✅ |
| 13 | SystemOptionsPEOPayloadSize | PAYLOAD_SIZE | — | ✅ |
| 14 | SystemOptionsPEOProcessRmaAsUnrefFlag | PROCESS_RMA_AS_UNREF_FLAG | — | ✅ |
| 15 | SystemOptionsPEOServiceItemId | SERVICE_ITEM_ID | — | ✅ |
| 16 | SystemOptionsPEOSystemOptionId | SYSTEM_OPTION_ID | 🔑 | ✅ |
| 17 | SystemOptionsPEOTraTaxFlag | TRA_TAX_FLAG | — | ✅ |
| 18 | SystemOptionsPEOValidationOrganizationId | VALIDATION_ORGANIZATION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
