---
id: DOC-HCM-454
doc_type: system-doc
title: "IRC_CAMP_GOALS_TL — Metas de Campanhas (Traducoes)"
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
  - campaign-goals-tl
  - irc-recruiting
aliases:
  - IRC_CAMP_GOALS_TL
  - irc_camp_goals_tl
  - camp-goals-tl
  - camp-goals-hcm
  - irc-camp-goals-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAMP_GOALS_TL

## Visao Geral

Armazena as **traducoes** das metas de campanhas. Tabela `_TL` com textos multilingues associados a IRC_CAMP_GOALS_B.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducao** (Translation) — armazena textos multilingues associados a tabela `_B` correspondente. Chave composta pelo ID base + LANGUAGE.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao:** Nomes e descricoes de metas em multiplos idiomas.
- **Suporte multilingue:** Essencial para organizacoes multinacionais.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAMP_GOAL_ID | NUMBER(18) | NOT NULL | PK/FK | Referencia a meta base | IRC_CAMP_GOALS_B | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 90% |
| 4 | GOAL_NAME | VARCHAR2(240) | NULL | Dados | Nome traduzido da meta | — | 🟡 75% |
| 5 | GOAL_DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_camp_goals_b]] — via `CAMP_GOAL_ID` (registro base da meta de campanha)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Metas com traducao em portugues
```sql
SELECT b.CAMP_GOAL_ID, tl.GOAL_NAME, tl.GOAL_DESCRIPTION
FROM   IRC_CAMP_GOALS_B b
JOIN   IRC_CAMP_GOALS_TL tl ON tl.CAMP_GOAL_ID = b.CAMP_GOAL_ID
WHERE  tl.LANGUAGE = 'PT';
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Portugues
---

## Observacoes

- Chave composta: CAMP_GOAL_ID + LANGUAGE.
- JOIN com IRC_CAMP_GOALS_B para dados completos.
---

## Referencias

- [Oracle Docs -- IRC_CAMP_GOALS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccampgoalstl.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
