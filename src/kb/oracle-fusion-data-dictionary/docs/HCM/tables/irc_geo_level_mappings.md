---
id: DOC-HCM-488
doc_type: system-doc
title: "IRC_GEO_LEVEL_MAPPINGS — Mapeamentos de Niveis Geograficos"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - geo-level-mappings
  - irc-recruiting
aliases:
  - IRC_GEO_LEVEL_MAPPINGS
  - irc_geo_level_mappings
  - geo-level-mappings
  - geo-level-hcm
  - irc-geo-level-mappings
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_GEO_LEVEL_MAPPINGS

## Visao Geral

**Mapeamentos** entre niveis geograficos e definicoes. Define semantica de cada nivel.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Semantica de cada nivel hierarquico.
- **Flexibilidade:** Profundidades diferentes por pais.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GEO_LEVEL_MAPPING_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | GEO_HIERARCHY_ID | NUMBER(18) | NOT NULL | FK | Hierarquia | IRC_GEO_HIERARCHIES | 🟡 80% |
| 3 | LEVEL_NUMBER | NUMBER | NOT NULL | Dados | Numero do nivel | — | 🟡 80% |
| 4 | LEVEL_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de nivel | — | 🟡 75% |
| 5 | LEVEL_NAME | VARCHAR2(240) | NULL | Dados | Nome do nivel | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_geo_hierarchies]] — via `GEO_HIERARCHY_ID` (hierarquia geografica do mapeamento de nivel)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Mapeamento de niveis
```sql
SELECT glm.LEVEL_NUMBER, glm.LEVEL_TYPE, glm.LEVEL_NAME
FROM   IRC_GEO_LEVEL_MAPPINGS glm
WHERE  glm.GEO_HIERARCHY_ID = :p_id ORDER BY glm.LEVEL_NUMBER;
```

### Filtros comuns
- `GEO_HIERARCHY_ID = :id` — Por hierarquia
---

## Observacoes

- Define semantica de cada nivel.
---

## Referencias

- [Oracle Docs -- IRC_GEO_LEVEL_MAPPINGS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircgeolevelmappings.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[geolevelmappingpvo|GeoLevelMappingPVO]] (HCM · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COUNTRY_CODE | GeoLevelMappingPEOCountryCode | ✅ |
| CREATED_BY | GeoLevelMappingPEOCreatedBy | — |
| CREATION_DATE | GeoLevelMappingPEOCreationDate | — |
| GEO_LEVEL2_COLUMN_NAME | GeoLevelMappingPEOGeoLevel2ColumnName | — |
| GEO_LEVEL3_COLUMN_NAME | GeoLevelMappingPEOGeoLevel3ColumnName | — |
| GEO_MAPPING_ID | GeoMappingId | ✅ |
| LAST_UPDATE_DATE | GeoLevelMappingPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GeoLevelMappingPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GeoLevelMappingPEOLastUpdatedBy | — |
| MODULE_ID | GeoLevelMappingPEOModuleId | — |
| OBJECT_STATUS | GeoLevelMappingPEOObjectStatus | — |
| OBJECT_VERSION_NUMBER | GeoLevelMappingPEOObjectVersionNumber | — |
| SEED_DATA_SOURCE | GeoLevelMappingPEOSeedDataSource | — |
