---
id: DOC-HCM-486
doc_type: system-doc
title: "IRC_GEO_HIERARCHIES — Hierarquias Geograficas"
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
  - geo-hierarchies
  - irc-recruiting
aliases:
  - IRC_GEO_HIERARCHIES
  - irc_geo_hierarchies
  - geo-hierarchies
  - geo-hierarchies-hcm
  - irc-geo-hierarchies
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_GEO_HIERARCHIES

## Visao Geral

**Hierarquias geograficas** para organizar localizacoes no recrutamento.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Organizacao geografica:** Estrutura hierarquica de localizacoes.
- **Filtros por regiao:** Base para filtros geograficos.
- **Analise regional:** Relatorios por regiao.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GEO_HIERARCHY_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | HIERARCHY_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo | — | 🟡 80% |
| 3 | HIERARCHY_NAME | VARCHAR2(240) | NULL | Dados | Nome da hierarquia | — | 🟡 80% |
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

### Hierarquias ativas
```sql
SELECT gh.HIERARCHY_CODE, gh.HIERARCHY_NAME
FROM   IRC_GEO_HIERARCHIES gh WHERE gh.STATUS = 'ACTIVE';
```

### Filtros comuns
- `STATUS = 'ACTIVE'` — Ativas
---

## Observacoes

- Nos definidos em IRC_GEO_HIER_NODES.
---

## Referencias

- [Oracle Docs -- IRC_GEO_HIERARCHIES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircgeohierarchies.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
