---
id: DOC-HCM-461
doc_type: system-doc
title: "IRC_CANDIDATE_SEARCH_TRACKING — Rastreamento de Buscas de Candidatos"
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
  - search-tracking
  - irc-recruiting
aliases:
  - IRC_CANDIDATE_SEARCH_TRACKING
  - irc_candidate_search_tracking
  - candidate-search-tracking
  - candidate-search-hcm
  - irc-candidate-search-tracking
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CANDIDATE_SEARCH_TRACKING

## Visao Geral

Registra o **historico de buscas** realizadas por recrutadores no banco de candidatos.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Analytics de busca:** Criterios mais usados pelos recrutadores.
- **Otimizacao de perfis:** Gaps entre buscas e perfis disponiveis.
- **Auditoria:** Rastreabilidade de acessos.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SEARCH_TRACKING_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | SEARCHER_PERSON_ID | NUMBER(18) | NULL | FK | Recrutador | PER_ALL_PEOPLE_F | 🟡 75% |
| 3 | SEARCH_CRITERIA | VARCHAR2(4000) | NULL | Dados | Criterios de busca | — | 🟡 70% |
| 4 | SEARCH_DATE | TIMESTAMP | NULL | Dados | Data/hora da busca | — | 🟡 75% |
| 5 | RESULTS_COUNT | NUMBER | NULL | Dados | Numero de resultados | — | 🟡 65% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `SEARCHER_PERSON_ID` (recrutador que realizou a busca)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Buscas recentes
```sql
SELECT st.SEARCH_CRITERIA, st.SEARCH_DATE, st.RESULTS_COUNT
FROM   IRC_CANDIDATE_SEARCH_TRACKING st
WHERE  st.SEARCHER_PERSON_ID = :p_person_id
ORDER BY st.SEARCH_DATE DESC;
```

### Filtros comuns
- `SEARCHER_PERSON_ID = :id` — Por recrutador
---

## Observacoes

- Alto volume potencial.
- Util para identificar tendencias.
---

## Referencias

- [Oracle Docs -- IRC_CANDIDATE_SEARCH_TRACKING](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccandidatesearchtracking.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
