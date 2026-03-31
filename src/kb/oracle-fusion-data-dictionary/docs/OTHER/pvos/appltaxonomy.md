---
id: DOC-OTHER-PVO-ApplTaxonomy
doc_type: system-doc
title: "ApplTaxonomy — PVO Cross-Module"
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
  - ApplTaxonomy
  - appltaxonomy
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ApplTaxonomy

## 📌 Visão Geral

View Object para extração BICC de dados de Appl Taxonomy. Acessa as tabelas: FND_APPL_TAXONOMY_VL.

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.ApplTaxonomy`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 12 | 75% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_appl_taxonomy_vl|FND_APPL_TAXONOMY_VL]] — 16 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[fnd_appl_taxonomy_vl|FND_APPL_TAXONOMY_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AlternativeId | ALTERNATIVE_ID | — | — |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | IsSeedDataAllowed | IS_SEED_DATA_ALLOWED | — | — |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ModuleId | MODULE_ID | 🔑 | ✅ |
| 10 | ModuleKey | MODULE_KEY | — | ✅ |
| 11 | ModuleName | MODULE_NAME | — | ✅ |
| 12 | ModuleType | MODULE_TYPE | — | ✅ |
| 13 | ProductCode | PRODUCT_CODE | — | ✅ |
| 14 | ProductLine | PRODUCT_LINE | — | — |
| 15 | UsageType | USAGE_TYPE | — | ✅ |
| 16 | UserModuleName | USER_MODULE_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
