---
id: DOC-HCM-462
doc_type: system-doc
title: "IRC_CAND_LAST_INTERACTION_V — Ultima Interacao do Candidato (View)"
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
  - candidate-interaction
  - irc-recruiting
aliases:
  - IRC_CAND_LAST_INTERACTION_V
  - irc_cand_last_interaction_v
  - cand-last-interaction-v
  - cand-last-hcm
  - irc-cand-last-interaction-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAND_LAST_INTERACTION_V

## Visao Geral

**View** que apresenta a **ultima interacao** de cada candidato. Consolida IRC_INTERACTIONS.

> [!note] Sufixo _V
> O sufixo `_V` indica **view** — objeto de consulta que consolida dados de multiplas tabelas. Pode ter restricoes em operacoes DML.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Monitoramento:** Candidatos sem interacao recente.
- **Alertas de inatividade:** Base para reengajamento.
- **Dashboard:** Ultimo contato com cada candidato.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CANDIDATE_ID | NUMBER(18) | NOT NULL | FK | Candidato | IRC_CANDIDATES | 🟢 90% |
| 2 | LAST_INTERACTION_ID | NUMBER(18) | NULL | FK | Ultima interacao | IRC_INTERACTIONS | 🟡 75% |
| 3 | LAST_INTERACTION_DATE | TIMESTAMP | NULL | Dados | Data/hora | — | 🟢 85% |
| 4 | LAST_INTERACTION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo | — | 🟡 75% |
| 5 | DAYS_SINCE_INTERACTION | NUMBER | NULL | Calculado | Dias desde ultima interacao | — | 🟡 65% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato da ultima interacao)
- [[irc_interactions]] — via `LAST_INTERACTION_ID` (ultima interacao registrada do candidato)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Candidatos inativos ha 30+ dias
```sql
SELECT cli.CANDIDATE_ID, cli.LAST_INTERACTION_DATE,
       cli.DAYS_SINCE_INTERACTION
FROM   IRC_CAND_LAST_INTERACTION_V cli
WHERE  cli.DAYS_SINCE_INTERACTION > 30;
```

### Filtros comuns
- `DAYS_SINCE_INTERACTION > 30` — Inativos
---

## Observacoes

- View (_V) — consulta rapida.
- Util para SLA de resposta.
---

## Referencias

- [Oracle Docs -- IRC_CAND_LAST_INTERACTION_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccandlastinteractionv.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
