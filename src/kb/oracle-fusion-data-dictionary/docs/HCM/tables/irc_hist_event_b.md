---
id: DOC-HCM-489
doc_type: system-doc
title: "IRC_HIST_EVENT_B — Eventos Historicos (Base)"
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
  - historical-events
  - irc-recruiting
aliases:
  - IRC_HIST_EVENT_B
  - irc_hist_event_b
  - hist-event-b
  - hist-event-hcm
  - irc-hist-event-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_HIST_EVENT_B

## Visao Geral

**Eventos historicos** do recrutamento. Tabela base (`_B`) com marcos e acontecimentos.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Auditoria:** Registro completo de eventos.
- **Timeline:** Linha do tempo de processos.
- **Compliance:** Evidencia de acoes realizadas.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | HIST_EVENT_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | EVENT_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de evento | — | 🟡 75% |
| 3 | EVENT_DATE | TIMESTAMP | NULL | Dados | Data/hora | — | 🟡 80% |
| 4 | CONTEXT_TYPE | VARCHAR2(30) | NULL | Classificacao | Contexto | — | 🟡 70% |
| 5 | CONTEXT_ID | NUMBER(18) | NULL | FK | ID do contexto | — | 🟡 70% |
| 6 | PERFORMER_ID | NUMBER(18) | NULL | FK | Executor | PER_ALL_PEOPLE_F | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERFORMER_ID` (pessoa que executou o evento historico)

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Eventos de uma requisicao
```sql
SELECT he.EVENT_TYPE, he.EVENT_DATE
FROM   IRC_HIST_EVENT_B he
WHERE  he.CONTEXT_TYPE = 'REQUISITION' AND he.CONTEXT_ID = :p_id
ORDER BY he.EVENT_DATE DESC;
```

### Filtros comuns
- `CONTEXT_TYPE = :tipo` — Por contexto
---

## Observacoes

- Tabela base (_B).
- Alto volume — considerar particionamento.
---

## Referencias

- [Oracle Docs -- IRC_HIST_EVENT_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irchisteventb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
