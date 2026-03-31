---
id: DOC-HCM-109
doc_type: system-doc
title: "FND_APPL_TAXONOMY_VL — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - FND_APPL_TAXONOMY_VL
  - fnd_appl_taxonomy_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_APPL_TAXONOMY_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALTERNATIVE_ID | — | — | — | — | — | — |
| 2 | CREATED_BY | — | — | — | — | — | — |
| 3 | CREATION_DATE | — | — | — | — | — | — |
| 4 | DESCRIPTION | — | — | — | — | — | — |
| 5 | IS_SEED_DATA_ALLOWED | — | — | — | — | — | — |
| 6 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 7 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 8 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 9 | MODULE_ID | — | — | — | — | — | — |
| 10 | MODULE_KEY | — | — | — | — | — | — |
| 11 | MODULE_NAME | — | — | — | — | — | — |
| 12 | MODULE_TYPE | — | — | — | — | — | — |
| 13 | PRODUCT_CODE | — | — | — | — | — | — |
| 14 | PRODUCT_LINE | — | — | — | — | — | — |
| 15 | USAGE_TYPE | — | — | — | — | — | — |
| 16 | USER_MODULE_NAME | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[appltaxonomy|ApplTaxonomy]] (OTHER · BICC: 12/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATIVE_ID | AlternativeId | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| IS_SEED_DATA_ALLOWED | IsSeedDataAllowed | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MODULE_ID | ModuleId | ✅ |
| MODULE_KEY | ModuleKey | ✅ |
| MODULE_NAME | ModuleName | ✅ |
| MODULE_TYPE | ModuleType | ✅ |
| PRODUCT_CODE | ProductCode | ✅ |
| PRODUCT_LINE | ProductLine | — |
| USAGE_TYPE | UsageType | ✅ |
| USER_MODULE_NAME | UserModuleName | — |

### [[documenttypespvo|DocumentTypesPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| MODULE_ID | ApplTaxonomyPEOModuleId | — |
| MODULE_NAME | ApplTaxonomyPEOModuleName | — |
