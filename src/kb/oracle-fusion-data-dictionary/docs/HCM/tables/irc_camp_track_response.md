---
id: DOC-HCM-458
doc_type: system-doc
title: "IRC_CAMP_TRACK_RESPONSE — Rastreamento de Respostas de Campanhas"
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
  - campaign-tracking
  - irc-recruiting
aliases:
  - IRC_CAMP_TRACK_RESPONSE
  - irc_camp_track_response
  - camp-track-response
  - camp-track-hcm
  - irc-camp-track-response
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAMP_TRACK_RESPONSE

## Visao Geral

Registra o **rastreamento de respostas** a campanhas de recrutamento. Captura interacoes de candidatos com campanhas.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Rastreamento de engajamento:** Respostas e interacoes de candidatos.
- **Metricas de marketing:** Taxa de resposta por campanha.
- **Analise de canal:** Quais canais geram mais respostas.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TRACK_RESPONSE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | CAMPAIGN_ID | NUMBER(18) | NOT NULL | FK | Referencia a campanha | IRC_CAMPAIGNS_B | 🟢 90% |
| 3 | RESPONSE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de resposta | — | 🟡 70% |
| 4 | RESPONSE_DATE | TIMESTAMP | NULL | Dados | Data/hora da resposta | — | 🟡 75% |
| 5 | SOURCE_MEDIUM | VARCHAR2(240) | NULL | Dados | Canal de origem | — | 🟡 65% |
| 6 | CANDIDATE_ID | NUMBER(18) | NULL | FK | Candidato (se identificado) | IRC_CANDIDATES | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_campaigns_b]] — via `CAMPAIGN_ID`
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato rastreado na campanha)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Respostas por tipo
```sql
SELECT ctr.RESPONSE_TYPE, COUNT(*) AS total
FROM   IRC_CAMP_TRACK_RESPONSE ctr
WHERE  ctr.CAMPAIGN_ID = :p_campaign_id
GROUP BY ctr.RESPONSE_TYPE;
```

### Filtros comuns
- `CAMPAIGN_ID = :id` — Por campanha
---

## Observacoes

- CANDIDATE_ID pode ser nulo para interacoes anonimas.
- SOURCE_MEDIUM permite analise por canal.
---

## Referencias

- [Oracle Docs -- IRC_CAMP_TRACK_RESPONSE](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccamptrackresponse.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
