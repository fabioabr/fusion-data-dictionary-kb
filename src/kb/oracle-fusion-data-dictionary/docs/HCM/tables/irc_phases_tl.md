---
id: DOC-HCM-515
doc_type: system-doc
title: "IRC_PHASES_TL — Fases do Processo (Traducoes)"
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
  - phases-tl
  - irc-recruiting
aliases:
  - IRC_PHASES_TL
  - irc_phases_tl
  - phases-tl
  - phases-tl-hcm
  - irc-phases-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_PHASES_TL

## Visao Geral

Traducoes das fases. Tabela `_TL`.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducao** (Translation) — armazena textos multilingues associados a tabela `_B` correspondente. Chave composta pelo ID base + LANGUAGE.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao:** Nomes de fases traduzidos.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PHASE_ID | NUMBER(18) | NOT NULL | PK/FK | Fase base | IRC_PHASES_B | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 90% |
| 4 | PHASE_NAME | VARCHAR2(240) | NULL | Dados | Nome traduzido | — | 🟡 80% |
| 5 | PHASE_DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_phases_b]] — via `PHASE_ID` (registro base da fase do processo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Fases em portugues
```sql
SELECT tl.PHASE_NAME FROM IRC_PHASES_TL tl WHERE tl.LANGUAGE = 'PT';
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Portugues
---

## Observacoes

- Chave composta: PHASE_ID + LANGUAGE.
---

## Referencias

- [Oracle Docs -- IRC_PHASES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircphasestl.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
