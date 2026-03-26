---
id: DOC-HCM-455
doc_type: system-doc
title: "IRC_CAMP_GOAL_RESP_B — Responsaveis por Metas de Campanha (Base)"
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
  - goal-responsibility
  - irc-recruiting
aliases:
  - IRC_CAMP_GOAL_RESP_B
  - irc_camp_goal_resp_b
  - camp-goal-resp-b
  - camp-goal-hcm
  - irc-camp-goal-resp-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAMP_GOAL_RESP_B

## Visao Geral

Armazena os **responsaveis** atribuidos a cada meta de campanha. Tabela base (`_B`) vinculando pessoas a metas.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Accountability:** Define quem e responsavel por cada meta.
- **Gestao de performance:** Avaliacao de contribuicao individual.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAMP_GOAL_RESP_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | CAMP_GOAL_ID | NUMBER(18) | NOT NULL | FK | Referencia a meta | IRC_CAMP_GOALS_B | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa responsavel | PER_ALL_PEOPLE_F | 🟡 75% |
| 4 | RESPONSIBILITY_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de responsabilidade | — | 🟡 65% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_camp_goals_b]] — via `CAMP_GOAL_ID` (meta de campanha do responsavel)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa responsavel pela meta de campanha)

### Tabelas-filha (FK de saida)
- [[irc_camp_goal_resp_tl]] — via `CAMP_GOAL_RESP_ID` (traducoes do responsavel pela meta)

---

## Uso Tipico

### Responsaveis por metas de uma campanha
```sql
SELECT gr.PERSON_ID, gr.RESPONSIBILITY_TYPE, g.GOAL_TYPE
FROM   IRC_CAMP_GOAL_RESP_B gr
JOIN   IRC_CAMP_GOALS_B g ON g.CAMP_GOAL_ID = gr.CAMP_GOAL_ID
WHERE  g.CAMPAIGN_ID = :p_campaign_id;
```

### Filtros comuns
- `CAMP_GOAL_ID = :id` — Por meta
- `PERSON_ID = :id` — Por responsavel
---

## Observacoes

- Tabela base (_B).
- Vincula pessoas a metas de campanha.
---

## Referencias

- [Oracle Docs -- IRC_CAMP_GOAL_RESP_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccampgoalrespb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
