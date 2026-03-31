---
id: DOC-HCM-456
doc_type: system-doc
title: "IRC_CAMP_GOAL_RESP_TL — Responsaveis por Metas (Traducoes)"
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
  - goal-resp-tl
  - irc-recruiting
aliases:
  - IRC_CAMP_GOAL_RESP_TL
  - irc_camp_goal_resp_tl
  - camp-goal-resp-tl
  - camp-goal-hcm
  - irc-camp-goal-resp-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAMP_GOAL_RESP_TL

## Visao Geral

Armazena as **traducoes** dos registros de responsaveis por metas de campanha. Tabela `_TL`.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducao** (Translation) — armazena textos multilingues associados a tabela `_B` correspondente. Chave composta pelo ID base + LANGUAGE.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao:** Textos de responsabilidades em multiplos idiomas.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAMP_GOAL_RESP_ID | NUMBER(18) | NOT NULL | PK/FK | Referencia ao responsavel | IRC_CAMP_GOAL_RESP_B | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 90% |
| 4 | RESPONSIBILITY_NAME | VARCHAR2(240) | NULL | Dados | Nome traduzido | — | 🟡 70% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_camp_goal_resp_b]] — via `CAMP_GOAL_RESP_ID` (registro base do responsavel pela meta)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Responsabilidades em portugues
```sql
SELECT tl.RESPONSIBILITY_NAME, b.PERSON_ID
FROM   IRC_CAMP_GOAL_RESP_B b
JOIN   IRC_CAMP_GOAL_RESP_TL tl ON tl.CAMP_GOAL_RESP_ID = b.CAMP_GOAL_RESP_ID
WHERE  tl.LANGUAGE = 'PT';
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Portugues
---

## Observacoes

- Chave composta: CAMP_GOAL_RESP_ID + LANGUAGE.
---

## Referencias

- [Oracle Docs -- IRC_CAMP_GOAL_RESP_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccampgoalresptl.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[campgoalpvo|CampGoalPVO]] (HCM · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CampGoalRespTranslationPEOCreatedBy2 | — |
| CREATION_DATE | CampGoalRespTranslationPEOCreationDate2 | — |
| GOAL_RESPONSE_ID | CampGoalRespTranslationPEOGoalResponseId1 | — |
| LANGUAGE | CampGoalRespTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | CampGoalRespTranslationPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | CampGoalRespTranslationPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | CampGoalRespTranslationPEOLastUpdatedBy2 | — |
| OBJECT_VERSION_NUMBER | CampGoalRespTranslationPEOObjectVersionNumber2 | — |
| RESPONSE_LABEL | CampGoalRespTranslationPEOResponseLabel | ✅ |
| SOURCE_LANG | CampGoalRespTranslationPEOSourceLang | — |
