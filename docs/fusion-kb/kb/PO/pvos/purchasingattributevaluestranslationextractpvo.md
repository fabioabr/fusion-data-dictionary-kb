---
id: DOC-PO-PVO-PurchasingAttributeValuesTranslationExtractPVO
doc_type: system-doc
title: "PurchasingAttributeValuesTranslationExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PurchasingAttributeValuesTranslationExtractPVO
  - purchasingattributevaluestranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingAttributeValuesTranslationExtractPVO

## 📌 Visão Geral

Extrai traduções dos valores de atributos flexíveis de compras para múltiplos idiomas. Garante que campos customizados sejam exibidos corretamente em todas as localidades.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingAttributeValuesTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[po_attribute_values_tlp|PO_ATTRIBUTE_VALUES_TLP]] — 21 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[po_attribute_values_tlp|PO_ATTRIBUTE_VALUES_TLP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Alias | ALIAS | — | ✅ |
| 2 | AttributeValuesTlpId | ATTRIBUTE_VALUES_TLP_ID | 🔑 | ✅ |
| 3 | Comments | COMMENTS | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | Description | DESCRIPTION | — | ✅ |
| 7 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 8 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 9 | Language | LANGUAGE | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | LastUpdatedProgram | LAST_UPDATED_PROGRAM | — | ✅ |
| 14 | LongDescription | LONG_DESCRIPTION | — | ✅ |
| 15 | Manufacturer | MANUFACTURER | — | ✅ |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 18 | PoLineId | PO_LINE_ID | — | ✅ |
| 19 | PrcBuId | PRC_BU_ID | — | ✅ |
| 20 | RebuildSearchIndexFlag | REBUILD_SEARCH_INDEX_FLAG | — | ✅ |
| 21 | RequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
