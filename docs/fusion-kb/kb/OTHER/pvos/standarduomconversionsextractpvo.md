---
id: DOC-OTHER-PVO-StandardUOMConversionsExtractPVO
doc_type: system-doc
title: "StandardUOMConversionsExtractPVO — PVO Cross-Module"
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
  - StandardUOMConversionsExtractPVO
  - standarduomconversionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StandardUOMConversionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Standard UOMConversions Extract. Acessa as tabelas: RCS_UOM_STD_CONVERSIONS_V.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.StandardUOMConversionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[rcs_uom_std_conversions_v|RCS_UOM_STD_CONVERSIONS_V]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[rcs_uom_std_conversions_v|RCS_UOM_STD_CONVERSIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConversionRate | CONVERSION_RATE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PrimaryUomCode | PRIMARY_UOM_CODE | 🔑 | ✅ |
| 9 | TransactionUomCode | TRANSACTION_UOM_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
