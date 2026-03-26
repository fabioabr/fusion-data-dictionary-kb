---
id: DOC-HCM-517
doc_type: system-doc
title: "IRC_PROCESSES_B — Processos Seletivos (Base)"
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
  - processes
  - irc-recruiting
aliases:
  - IRC_PROCESSES_B
  - irc_processes_b
  - processes-b
  - processes-b-hcm
  - irc-processes-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_PROCESSES_B

## Visao Geral

Configuracao dos **processos seletivos**. Tabela base (`_B`) com fluxo completo de selecao.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Definicao de processos:** Fluxo de selecao.
- **Padronizacao:** Processos reutilizaveis.
- **Governanca:** Controle centralizado de workflows.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROCESS_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | PROCESS_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do processo | — | 🟡 85% |
| 3 | PROCESS_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 80% |
| 4 | PROCESS_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de processo | — | 🟡 70% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Processos ativos
```sql
SELECT p.PROCESS_CODE, p.PROCESS_TYPE
FROM   IRC_PROCESSES_B p WHERE p.PROCESS_STATUS = 'ACTIVE';
```

### Filtros comuns
- `PROCESS_STATUS = 'ACTIVE'` — Ativos
---

## Observacoes

- Tabela base (_B).
- Cada processo define uma sequencia de fases.
---

## Referencias

- [Oracle Docs -- IRC_PROCESSES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircprocessesb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
