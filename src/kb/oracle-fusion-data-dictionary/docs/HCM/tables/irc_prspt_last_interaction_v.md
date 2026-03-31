---
id: DOC-HCM-520
doc_type: system-doc
title: "IRC_PRSPT_LAST_INTERACTION_V — Ultima Interacao de Prospecto (View)"
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
  - prospect-interaction
  - irc-recruiting
aliases:
  - IRC_PRSPT_LAST_INTERACTION_V
  - irc_prspt_last_interaction_v
  - prspt-last-interaction-v
  - prspt-last-hcm
  - irc-prspt-last-interaction-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_PRSPT_LAST_INTERACTION_V

## Visao Geral

**View** com ultima interacao de cada prospecto.

> [!note] Sufixo _V
> O sufixo `_V` indica **view** — objeto de consulta que consolida dados de multiplas tabelas. Pode ter restricoes em operacoes DML.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Monitoramento:** Ultima interacao com prospectos.
- **Reengajamento:** Prospectos sem contato recente.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROSPECT_ID | NUMBER(18) | NOT NULL | FK | Prospecto | IRC_PROSPECTS | 🟢 85% |
| 2 | LAST_INTERACTION_DATE | TIMESTAMP | NULL | Dados | Data/hora | — | 🟢 85% |
| 3 | LAST_INTERACTION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo | — | 🟡 75% |
| 4 | DAYS_SINCE_INTERACTION | NUMBER | NULL | Calculado | Dias desde ultima interacao | — | 🟡 65% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_prospects]] — via `PROSPECT_ID` (prospecto da ultima interacao)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Prospectos inativos
```sql
SELECT pli.PROSPECT_ID, pli.DAYS_SINCE_INTERACTION
FROM   IRC_PRSPT_LAST_INTERACTION_V pli
WHERE  pli.DAYS_SINCE_INTERACTION > 30;
```

### Filtros comuns
- `DAYS_SINCE_INTERACTION > 30` — Inativos
---

## Observacoes

- View (_V) — consulta rapida.
---

## Referencias

- [Oracle Docs -- IRC_PRSPT_LAST_INTERACTION_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircprsptlastinteractionv.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[prospectspvo|ProspectsPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INTERACTION_DATE | ProspectLastInteractionPEOInteractionDate | — |
| INTERACTION_ID | ProspectLastInteractionPEOInteractionId | — |

### [[prospectsviewallpvo|ProspectsViewAllPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INTERACTION_DATE | ProspectLastInteractionPEOInteractionDate | — |
| INTERACTION_ID | ProspectLastInteractionPEOInteractionId | — |
