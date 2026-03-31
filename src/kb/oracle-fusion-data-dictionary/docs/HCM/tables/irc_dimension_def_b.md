---
id: DOC-HCM-482
doc_type: system-doc
title: "IRC_DIMENSION_DEF_B — Definicoes de Dimensoes (Base)"
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
  - dimension-def
  - irc-recruiting
aliases:
  - IRC_DIMENSION_DEF_B
  - irc_dimension_def_b
  - dimension-def-b
  - dimension-def-hcm
  - irc-dimension-def-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_DIMENSION_DEF_B

## Visao Geral

**Definicoes de dimensoes** para analytics de recrutamento. Tabela base (`_B`).

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Analytics:** Dimensoes configuraveis para analise multidimensional.
- **Flexibilidade:** Dimensoes customizadas para relatorios.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DIMENSION_DEF_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | DIMENSION_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo da dimensao | — | 🟡 80% |
| 3 | DIMENSION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de dimensao | — | 🟡 70% |
| 4 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Dimensoes ativas
```sql
SELECT dd.DIMENSION_CODE, dd.DIMENSION_TYPE
FROM   IRC_DIMENSION_DEF_B dd WHERE dd.STATUS = 'ACTIVE';
```

### Filtros comuns
- `STATUS = 'ACTIVE'` — Ativas
---

## Observacoes

- Tabela base (_B) — traducoes em IRC_DIMENSION_DEF_TL.
---

## Referencias

- [Oracle Docs -- IRC_DIMENSION_DEF_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircdimensiondefb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[sourcedimensionpvo|SourceDimensionPVO]] (HCM · BICC: 7/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DIMENSION_ID | DimensionId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MODULE_ID | ModuleId | — |
| PRIORITY | Priority | — |
| SEED_DATA_SOURCE | SeedDataSource | — |
| SEQUENCE | Sequence | — |
| SOURCE_MEDIUM | SourceMedium | ✅ |
| SOURCE_MEDIUM_URL_VALUE | SourceMediumUrlValue | — |
| SOURCE_URL_VALUE | SourceUrlValue | — |
| URL_HEADER_REGEX | UrlHeaderRegex | — |

### [[sourcetrackingviewallpvo|SourceTrackingViewAllPVO]] (HCM · BICC: 6/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | SourceDimensionBPEOCreatedBy | ✅ |
| CREATION_DATE | SourceDimensionBPEOCreationDate | ✅ |
| DIMENSION_ID | ParentSourceDimensionBPEODimensionId | — |
| DIMENSION_ID | SourceDimensionBPEODimensionId | — |
| LAST_UPDATE_DATE | SourceDimensionBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SourceDimensionBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | SourceDimensionBPEOLastUpdatedBy | ✅ |
| MODULE_ID | SourceDimensionBPEOModuleId | — |
| PRIORITY | SourceDimensionBPEOPriority | — |
| SEED_DATA_SOURCE | SourceDimensionBPEOSeedDataSource | — |
| SEQUENCE | SourceDimensionBPEOSequence | — |
| SOURCE_MEDIUM | SourceDimensionBPEOSourceMedium | ✅ |
| SOURCE_MEDIUM_URL_VALUE | SourceDimensionBPEOSourceMediumUrlValue | — |
| SOURCE_URL_VALUE | SourceDimensionBPEOSourceUrlValue | — |
| URL_HEADER_REGEX | SourceDimensionBPEOUrlHeaderRegex | — |
