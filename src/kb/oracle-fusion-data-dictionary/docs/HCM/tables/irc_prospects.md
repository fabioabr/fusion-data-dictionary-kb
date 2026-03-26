---
id: DOC-HCM-519
doc_type: system-doc
title: "IRC_PROSPECTS — Prospectos de Recrutamento"
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
  - prospects
  - irc-recruiting
aliases:
  - IRC_PROSPECTS
  - irc_prospects
  - irc-prospects
  - irc_prospects-oracle
  - irc_prospects-oracle
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_PROSPECTS

## Visao Geral

**Prospectos** — contatos que ainda nao se candidataram formalmente mas foram identificados como potenciais.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Pipeline de talentos:** Contatos pre-candidatura.
- **Sourcing:** Candidatos identificados proativamente.
- **Engajamento:** Campanhas de atracao.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROSPECT_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | CANDIDATE_ID | NUMBER(18) | NULL | FK | Candidato (se convertido) | IRC_CANDIDATES | 🟡 80% |
| 3 | PROSPECT_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 75% |
| 4 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Origem | — | 🟡 70% |
| 5 | REQUISITION_ID | NUMBER(18) | NULL | FK | Requisicao de interesse | IRC_REQUISITIONS_B | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato registrado como prospecto)
- [[irc_requisitions_b]] — via `REQUISITION_ID` (requisicao do prospecto)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Prospectos ativos
```sql
SELECT p.PROSPECT_ID, p.PROSPECT_STATUS, p.SOURCE_TYPE
FROM   IRC_PROSPECTS p WHERE p.PROSPECT_STATUS = 'ACTIVE';
```

### Filtros comuns
- `PROSPECT_STATUS = 'ACTIVE'` — Ativos
---

## Observacoes

- Diferem de candidatos — sem candidatura formal.
- CANDIDATE_ID preenchido quando se torna candidato.
---

## Referencias

- [Oracle Docs -- IRC_PROSPECTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircprospects.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
