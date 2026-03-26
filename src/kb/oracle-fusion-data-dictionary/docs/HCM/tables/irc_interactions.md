---
id: DOC-HCM-496
doc_type: system-doc
title: "IRC_INTERACTIONS — Interacoes de Recrutamento"
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
  - interactions
  - irc-recruiting
aliases:
  - IRC_INTERACTIONS
  - irc_interactions
  - irc-interactions
  - irc_interactions-oracle
  - irc_interactions-oracle
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_INTERACTIONS

## Visao Geral

Todas as **interacoes** entre organizacao e candidatos/prospects.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Historico:** Registro completo de contatos.
- **Engajamento:** Metricas de frequencia.
- **SLA:** Tempo entre interacoes.
- **Compliance:** Rastreabilidade.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INTERACTION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | INTERACTION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo (email, phone, meeting) | — | 🟡 80% |
| 3 | INTERACTION_DATE | TIMESTAMP | NULL | Dados | Data/hora | — | 🟢 85% |
| 4 | CANDIDATE_ID | NUMBER(18) | NULL | FK | Candidato | IRC_CANDIDATES | 🟢 85% |
| 5 | PERFORMER_ID | NUMBER(18) | NULL | FK | Executor | PER_ALL_PEOPLE_F | 🟡 80% |
| 6 | SUBJECT | VARCHAR2(240) | NULL | Dados | Assunto | — | 🟡 70% |
| 7 | NOTES | VARCHAR2(4000) | NULL | Dados | Notas | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato da interacao de recrutamento)
- [[per_all_people_f]] — via `PERFORMER_ID` (pessoa que realizou a interacao)

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Interacoes recentes
```sql
SELECT i.INTERACTION_TYPE, i.INTERACTION_DATE, i.SUBJECT
FROM   IRC_INTERACTIONS i
WHERE  i.CANDIDATE_ID = :p_id ORDER BY i.INTERACTION_DATE DESC;
```

### Filtros comuns
- `CANDIDATE_ID = :id` — Por candidato
---

## Observacoes

- Alto volume — indexar por CANDIDATE_ID.
- Base para views de ultima interacao.
---

## Referencias

- [Oracle Docs -- IRC_INTERACTIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircinteractions.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
