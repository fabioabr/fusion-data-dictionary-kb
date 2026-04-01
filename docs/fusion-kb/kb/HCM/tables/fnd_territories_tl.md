---
id: DOC-HCM-140
doc_type: system-doc
title: "FND_TERRITORIES_TL — (título a preencher)"
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
  - FND_TERRITORIES_TL
  - fnd_territories_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_TERRITORIES_TL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | DESCRIPTION | — | — | — | — | — | — |
| 4 | LANGUAGE | — | — | — | — | — | — |
| 5 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 6 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 7 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 8 | SOURCE_LANG | — | — | — | — | — | — |
| 9 | TERRITORY_CODE | — | — | — | — | — | — |
| 10 | TERRITORY_SHORT_NAME | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[legislationpvo|LegislationPVO]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | LegislationTranslationPEOCreatedBy | — |
| CREATION_DATE | LegislationTranslationPEOCreationDate | — |
| DESCRIPTION | LegislationTranslationPEODescription | ✅ |
| LANGUAGE | LegislationTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LegislationTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LegislationTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LegislationTranslationPEOLastUpdatedBy | — |
| SOURCE_LANG | LegislationTranslationPEOSourceLang | — |
| TERRITORY_CODE | LegislationTranslationPEOTerritoryCode | — |
| TERRITORY_SHORT_NAME | LegislationTranslationPEOTerritoryShortName | ✅ |

### [[territoriespvo|TerritoriesPVO]] (HCM · BICC: 4/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | ✅ |
| SOURCE_LANG | SourceLang | ✅ |
| TERRITORY_CODE | TerritoryCode1 | — |
| TERRITORY_SHORT_NAME | TerritoryShortName | ✅ |

### [[territoriestlpvo|TerritoriesTLPVO]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DESCRIPTION | Description | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| SOURCE_LANG | SourceLang | — |
| TERRITORY_CODE | TerritoryCode | ✅ |
| TERRITORY_SHORT_NAME | TerritoryShortName | ✅ |
