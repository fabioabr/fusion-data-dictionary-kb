---
id: DOC-HCM-514
doc_type: system-doc
title: "IRC_PHASES_B — Fases do Processo Seletivo (Base)"
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
  - process-phases
  - irc-recruiting
aliases:
  - IRC_PHASES_B
  - irc_phases_b
  - phases-b
  - phases-b-hcm
  - irc-phases-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_PHASES_B

## Visao Geral

**Fases** dos processos seletivos. Tabela base (`_B`) com etapas de transicao de candidatos.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Estrutura do processo:** Etapas do fluxo seletivo.
- **Governanca:** Sequencia de fases.
- **Funil:** Analise de conversao por fase.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PHASE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | PHASE_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo da fase | — | 🟡 85% |
| 3 | PHASE_ORDER | NUMBER | NULL | Dados | Ordem sequencial | — | 🟡 80% |
| 4 | PROCESS_ID | NUMBER(18) | NULL | FK | Processo | IRC_PROCESSES_B | 🟡 80% |
| 5 | PHASE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de fase | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_processes_b]] — via `PROCESS_ID` (processo seletivo da fase)

### Tabelas-filha (FK de saida)
- [[irc_candidates]] — via `CURRENT_PHASE_ID` (candidatos nesta fase do processo)
- [[irc_lc_history]] — via `FROM_PHASE_ID` / `TO_PHASE_ID` (historicos de transicao desta fase)

---

## Uso Tipico

### Fases em ordem
```sql
SELECT p.PHASE_CODE, p.PHASE_ORDER, p.PHASE_TYPE
FROM   IRC_PHASES_B p WHERE p.PROCESS_ID = :p_id
ORDER BY p.PHASE_ORDER;
```

### Filtros comuns
- `PROCESS_ID = :id` — Por processo
---

## Observacoes

- Tabela base (_B).
- PHASE_ORDER define a sequencia.
---

## Referencias

- [Oracle Docs -- IRC_PHASES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircphasesb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
