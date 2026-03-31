---
id: DOC-HCM-516
doc_type: system-doc
title: "IRC_POOLMEM_LAST_INTERACTION_V — Ultima Interacao de Membro de Pool (View)"
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
  - pool-member-interaction
  - irc-recruiting
aliases:
  - IRC_POOLMEM_LAST_INTERACTION_V
  - irc_poolmem_last_interaction_v
  - poolmem-last-interaction-v
  - poolmem-last-hcm
  - irc-poolmem-last-interaction-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_POOLMEM_LAST_INTERACTION_V

## Visao Geral

**View** com ultima interacao de cada membro de pool de talentos.

> [!note] Sufixo _V
> O sufixo `_V` indica **view** — objeto de consulta que consolida dados de multiplas tabelas. Pode ter restricoes em operacoes DML.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Monitoramento:** Ultima interacao por membro.
- **Reengajamento:** Membros inativos.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POOL_MEMBER_ID | NUMBER(18) | NOT NULL | FK | Membro do pool | IRC_CAND_POOL_MEMBERS | 🟢 85% |
| 2 | LAST_INTERACTION_DATE | TIMESTAMP | NULL | Dados | Data/hora | — | 🟢 85% |
| 3 | LAST_INTERACTION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo | — | 🟡 75% |
| 4 | DAYS_SINCE_INTERACTION | NUMBER | NULL | Calculado | Dias desde ultima interacao | — | 🟡 65% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_cand_pool_members]] — via `POOL_MEMBER_ID` (membro do pool da ultima interacao)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Membros inativos
```sql
SELECT pm.POOL_MEMBER_ID, pm.DAYS_SINCE_INTERACTION
FROM   IRC_POOLMEM_LAST_INTERACTION_V pm
WHERE  pm.DAYS_SINCE_INTERACTION > 60;
```

### Filtros comuns
- `DAYS_SINCE_INTERACTION > 60` — Inativos
---

## Observacoes

- View (_V) — consulta rapida.
---

## Referencias

- [Oracle Docs -- IRC_POOLMEM_LAST_INTERACTION_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircpoolmemlastinteractionv.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[candidatepoolmemberpvo|CandidatePoolMemberPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INTERACTION_DATE | CandPoolMemLastInteractionPEOInteractionDate | — |
| INTERACTION_ID | CandPoolMemLastInteractionPEOInteractionId | — |
