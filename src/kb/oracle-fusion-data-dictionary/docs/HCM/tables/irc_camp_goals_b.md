---
id: DOC-HCM-453
doc_type: system-doc
title: "IRC_CAMP_GOALS_B — Metas de Campanhas de Recrutamento (Base)"
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
  - campaign-goals
  - irc-recruiting
aliases:
  - IRC_CAMP_GOALS_B
  - irc_camp_goals_b
  - camp-goals-b
  - camp-goals-hcm
  - irc-camp-goals-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAMP_GOALS_B

## Visao Geral

Armazena as **metas** definidas para campanhas de recrutamento. Tabela base (`_B`) com valores quantitativos e configuracoes.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Definicao de metas:** Objetivos mensuraveis para campanhas.
- **Acompanhamento:** Base para comparar metas vs. realizadas.
- **Relatorios de performance:** Dashboards de metas de recruiting.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAMP_GOAL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da meta | — | 🟢 90% |
| 2 | CAMPAIGN_ID | NUMBER(18) | NOT NULL | FK | Referencia a campanha | IRC_CAMPAIGNS_B | 🟢 90% |
| 3 | GOAL_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de meta | — | 🟡 70% |
| 4 | TARGET_VALUE | NUMBER | NULL | Dados | Valor-alvo | — | 🟡 70% |
| 5 | ACTUAL_VALUE | NUMBER | NULL | Dados | Valor realizado | — | 🟡 65% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_campaigns_b]] — via `CAMPAIGN_ID`

### Tabelas-filha (FK de saida)
- [[irc_camp_goals_tl]] — via `CAMP_GOAL_ID` (traducoes da meta de campanha)
- [[irc_camp_goal_resp_b]] — via `CAMP_GOAL_ID` (traducoes da meta de campanha)

---

## Uso Tipico

### Metas e progresso por campanha
```sql
SELECT cg.GOAL_TYPE, cg.TARGET_VALUE, cg.ACTUAL_VALUE,
       ROUND(cg.ACTUAL_VALUE/NULLIF(cg.TARGET_VALUE,0)*100,1) AS pct
FROM   IRC_CAMP_GOALS_B cg
WHERE  cg.CAMPAIGN_ID = :p_campaign_id;
```

### Filtros comuns
- `CAMPAIGN_ID = :id` — Filtrar por campanha
---

## Observacoes

- Tabela base (_B) — traducoes em IRC_CAMP_GOALS_TL.
- Valores permitem calculo direto de % atingido.
---

## Referencias

- [Oracle Docs -- IRC_CAMP_GOALS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccampgoalsb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
