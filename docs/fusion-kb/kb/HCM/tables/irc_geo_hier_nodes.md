---
id: DOC-HCM-487
doc_type: system-doc
title: "IRC_GEO_HIER_NODES — Nos de Hierarquias Geograficas"
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
  - geo-nodes
  - irc-recruiting
aliases:
  - IRC_GEO_HIER_NODES
  - irc_geo_hier_nodes
  - geo-hier-nodes
  - geo-hier-hcm
  - irc-geo-hier-nodes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_GEO_HIER_NODES

## Visao Geral

**Nos** das hierarquias geograficas. Cada registro e um nivel na arvore (pais, estado, cidade).

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Estrutura hierarquica:** Arvore de nos geograficos.
- **Navegacao:** Drill-down geografico.
- **Mapeamento:** Localizacoes fisicas na hierarquia.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GEO_HIER_NODE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | GEO_HIERARCHY_ID | NUMBER(18) | NOT NULL | FK | Hierarquia | IRC_GEO_HIERARCHIES | 🟢 85% |
| 3 | PARENT_NODE_ID | NUMBER(18) | NULL | FK | No pai (NULL=raiz) | IRC_GEO_HIER_NODES | 🟡 80% |
| 4 | NODE_NAME | VARCHAR2(240) | NULL | Dados | Nome do no | — | 🟡 80% |
| 5 | NODE_LEVEL | NUMBER | NULL | Dados | Nivel (1=raiz) | — | 🟡 75% |
| 6 | GEOGRAPHY_CODE | VARCHAR2(30) | NULL | Identificacao | Codigo geografico | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_geo_hierarchies]] — via `GEO_HIERARCHY_ID` (hierarquia geografica do no)
- [[irc_geo_hier_nodes]] — via `PARENT_NODE_ID` (auto-referencia)

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Nos raiz de uma hierarquia
```sql
SELECT ghn.NODE_NAME, ghn.GEOGRAPHY_CODE, ghn.NODE_LEVEL
FROM   IRC_GEO_HIER_NODES ghn
WHERE  ghn.GEO_HIERARCHY_ID = :p_id AND ghn.PARENT_NODE_ID IS NULL;
```

### Filtros comuns
- `PARENT_NODE_ID IS NULL` — Nos raiz
---

## Observacoes

- Auto-referenciada — PARENT_NODE_ID aponta para mesma tabela.
- NODE_LEVEL facilita consultas sem recursao.
---

## Referencias

- [Oracle Docs -- IRC_GEO_HIER_NODES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircgeohiernodes.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[geographyhiringpvo|GeographyHiringPVO]] (HCM · BICC: 9/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | GeographyNodePEOCreatedBy | ✅ |
| CREATION_DATE | GeographyNodePEOCreationDate | ✅ |
| GEOGRAPHY_ID | GeographyNodePEOGeographyId | ✅ |
| GEOGRAPHY_NODE_ID | GeographyNodeId | ✅ |
| HIERARCHY_ID | GeographyNodePEOHierarchyId | ✅ |
| LAST_UPDATE_DATE | GeographyNodePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GeographyNodePEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GeographyNodePEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | GeographyNodePEOObjectVersionNumber | — |
| PARENT_GEO_NODE_ID | GeographyNodePEOParentGeoNodeId | ✅ |
