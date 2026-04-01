---
id: DOC-HCM-PVO-TerritoriesTLPVO
doc_type: system-doc
title: "TerritoriesTLPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - TerritoriesTLPVO
  - territoriestlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TerritoriesTLPVO

## 📌 Visão Geral

Disponibiliza traduções de nomes de territórios com nomes abreviados. Suporta localização multilíngue de referências geográficas no Oracle Fusion.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AnalyticsServiceAM.TerritoriesTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 4 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_territories_tl|FND_TERRITORIES_TL]] — 10 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[fnd_territories_tl|FND_TERRITORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | Description | DESCRIPTION | — | — |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | SourceLang | SOURCE_LANG | — | — |
| 9 | TerritoryCode | TERRITORY_CODE | 🔑 | ✅ |
| 10 | TerritoryShortName | TERRITORY_SHORT_NAME | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
