---
id: DOC-HCM-505
doc_type: system-doc
title: "IRC_LC_HISTORY — Historico do Ciclo de Vida"
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
  - lifecycle-history
  - irc-recruiting
aliases:
  - IRC_LC_HISTORY
  - irc_lc_history
  - lc-history
  - lc-history-hcm
  - irc-lc-history
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_LC_HISTORY

## Visao Geral

**Historico completo** de transicoes no ciclo de vida do candidato.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Auditoria:** Todas as transicoes registradas.
- **Timeline:** Jornada do candidato no processo.
- **Metricas:** Time-to-fill, time-in-phase.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LC_HISTORY_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | CANDIDATE_ID | NUMBER(18) | NULL | FK | Candidato | IRC_CANDIDATES | 🟢 85% |
| 3 | REQUISITION_ID | NUMBER(18) | NULL | FK | Requisicao | IRC_REQUISITIONS_B | 🟡 80% |
| 4 | FROM_PHASE_ID | NUMBER(18) | NULL | FK | Fase de origem | IRC_PHASES_B | 🟡 75% |
| 5 | TO_PHASE_ID | NUMBER(18) | NULL | FK | Fase de destino | IRC_PHASES_B | 🟡 75% |
| 6 | ACTION_ID | NUMBER(18) | NULL | FK | Acao executada | — | 🟡 70% |
| 7 | TRANSITION_DATE | TIMESTAMP | NULL | Dados | Data/hora | — | 🟢 85% |
| 8 | PERFORMED_BY | NUMBER(18) | NULL | FK | Executor | PER_ALL_PEOPLE_F | 🟡 75% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato no historico do ciclo de vida)
- [[irc_requisitions_b]] — via `REQUISITION_ID` (requisicao no historico do ciclo de vida)
- [[irc_phases_b]] — via `FROM_PHASE_ID` / `TO_PHASE_ID` (fase de origem na transicao do candidato)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Transicoes de um candidato
```sql
SELECT lch.FROM_PHASE_ID, lch.TO_PHASE_ID, lch.TRANSITION_DATE
FROM   IRC_LC_HISTORY lch
WHERE  lch.CANDIDATE_ID = :p_cand_id AND lch.REQUISITION_ID = :p_req_id
ORDER BY lch.TRANSITION_DATE;
```

### Filtros comuns
- `CANDIDATE_ID = :id` — Por candidato
---

## Observacoes

- Alto volume — essencial para metricas.
- Tabela append-only.
---

## Referencias

- [Oracle Docs -- IRC_LC_HISTORY](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irclchistory.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
