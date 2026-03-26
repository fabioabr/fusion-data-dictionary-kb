---
id: DOC-HCM-502
doc_type: system-doc
title: "IRC_LC_ACTIONS_TL — Acoes do Ciclo de Vida (Traducoes)"
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
  - lc-actions-tl
  - irc-recruiting
aliases:
  - IRC_LC_ACTIONS_TL
  - irc_lc_actions_tl
  - lc-actions-tl
  - lc-actions-hcm
  - irc-lc-actions-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_LC_ACTIONS_TL

## Visao Geral

Traducoes das **acoes do ciclo de vida** do candidato.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducao** (Translation) — armazena textos multilingues associados a tabela `_B` correspondente. Chave composta pelo ID base + LANGUAGE.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao:** Nomes de acoes traduzidos.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LC_ACTION_ID | NUMBER(18) | NOT NULL | PK/FK | Acao | — | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 90% |
| 4 | ACTION_NAME | VARCHAR2(240) | NULL | Dados | Nome traduzido | — | 🟡 80% |
| 5 | ACTION_DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Acoes em portugues
```sql
SELECT tl.ACTION_NAME FROM IRC_LC_ACTIONS_TL tl WHERE tl.LANGUAGE = 'PT';
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Portugues
---

## Observacoes

- Chave composta: LC_ACTION_ID + LANGUAGE.
---

## Referencias

- [Oracle Docs -- IRC_LC_ACTIONS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irclcactionstl.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
