---
id: DOC-HCM-451
doc_type: system-doc
title: "IRC_CAMP_AUDIENCE — Publico-Alvo de Campanhas de Recrutamento"
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
  - campaign-audience
  - irc-recruiting
aliases:
  - IRC_CAMP_AUDIENCE
  - irc_camp_audience
  - camp-audience
  - camp-audience-hcm
  - irc-camp-audience
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAMP_AUDIENCE

## Visao Geral

Armazena os **publicos-alvo** associados a campanhas de recrutamento (Recruiting Campaigns). Cada registro vincula uma campanha a um grupo demografico ou segmento de candidatos.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Segmentacao de campanhas:** Define quais grupos de candidatos sao alvo de cada campanha.
- **Analise de alcance:** Permite avaliar se a campanha atingiu o publico desejado.
- **Marketing de recrutamento:** Base para estrategias de atracao de talentos.
- **Metricas de eficacia:** Correlacao entre publico-alvo e candidatos atraidos.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAMP_AUDIENCE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do registro | — | 🟢 90% |
| 2 | CAMPAIGN_ID | NUMBER(18) | NOT NULL | FK | Referencia a campanha de recrutamento | IRC_CAMPAIGNS_B | 🟢 90% |
| 3 | AUDIENCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de publico-alvo | — | 🟡 70% |
| 4 | AUDIENCE_VALUE | VARCHAR2(240) | NULL | Dados | Valor ou descricao do segmento | — | 🟡 65% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 9 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da ultima sessao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_campaigns_b]] — via `CAMPAIGN_ID` (campanha-pai)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Publicos-alvo de uma campanha
```sql
SELECT ca.CAMP_AUDIENCE_ID, ca.AUDIENCE_TYPE, ca.AUDIENCE_VALUE
FROM   IRC_CAMP_AUDIENCE ca
WHERE  ca.CAMPAIGN_ID = :p_campaign_id;
```

### Filtros comuns
- `CAMPAIGN_ID = :id` — Filtrar por campanha
- `AUDIENCE_TYPE = :tipo` — Filtrar por tipo de publico
---

## Observacoes

- Tabela associativa entre campanhas e segmentos de publico-alvo.
- Usada em conjunto com IRC_CAMP_GOALS_B para avaliar metas por publico.
---

## Referencias

- [Oracle Docs -- IRC_CAMP_AUDIENCE](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccampaudience.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
