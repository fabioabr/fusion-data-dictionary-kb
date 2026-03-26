---
id: DOC-HCM-431
doc_type: system-doc
title: "IRC_AF_PAGE_BLOCKS_TL — Traducoes de Blocos por Pagina de Candidatura"
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
  - irc
  - apply-flow
  - pagina-bloco
  - traducao
aliases:
  - IRC_AF_PAGE_BLOCKS_TL
  - irc_af_page_blocks_tl
  - irc-af-page-blocks-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_AF_PAGE_BLOCKS_TL

## 📌 Visao Geral

Tabela de traducoes que armazena os **textos traduzidos** das associacoes entre paginas e blocos dos fluxos de candidatura do modulo Recruiting (IRC).

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducoes** (Translation) — armazena textos em multiplos idiomas.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao:** textos de blocos por pagina em multiplos idiomas.
- **Experiencia multilingual:** candidatos veem conteudo no seu idioma.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAGE_BLOCK_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da associacao | IRC_AF_PAGE_BLOCKS_B | 🟡 70% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 85% |
| 4 | BLOCK_TITLE | VARCHAR2(240) | NULL | Identificacao | Titulo traduzido do bloco na pagina | — | 🟡 60% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟡 55% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_af_page_blocks_b]] — via `PAGE_BLOCK_ID` (registro base do bloco de pagina)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Traducoes de blocos por pagina
```sql
SELECT tl.LANGUAGE, tl.BLOCK_TITLE, tl.DESCRIPTION
FROM   IRC_AF_PAGE_BLOCKS_TL tl
WHERE  tl.PAGE_BLOCK_ID = :p_pb_id;
```

### Filtros comuns
- `PAGE_BLOCK_ID = :p_pb_id — Por associacao`
- `LANGUAGE = USERENV('LANG') — Idioma da sessao`

---

## 🔒 Observacoes

- Tabela de traducoes (_TL) — join com _B para dados completos.
- Chave composta: PAGE_BLOCK_ID + LANGUAGE.

---

## 📚 Referencias

- [Oracle Docs — IRC_AF_PAGE_BLOCKS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircafpageblockstl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
