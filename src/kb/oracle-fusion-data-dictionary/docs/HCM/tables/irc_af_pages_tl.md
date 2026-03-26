---
id: DOC-HCM-429
doc_type: system-doc
title: "IRC_AF_PAGES_TL — Traducoes de Paginas de Fluxo de Candidatura"
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
  - pagina-candidatura
  - traducao
aliases:
  - IRC_AF_PAGES_TL
  - irc_af_pages_tl
  - irc-af-pages-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_AF_PAGES_TL

## 📌 Visao Geral

Tabela de traducoes que armazena os **textos traduzidos** das paginas de fluxo de candidatura do modulo Recruiting (IRC) em multiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducoes** (Translation) — armazena textos em multiplos idiomas.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao:** titulos de paginas em multiplos idiomas.
- **Experiencia multilingual:** candidatos navegam paginas no seu idioma.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAGE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da pagina | IRC_AF_PAGES_B | 🟡 70% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 85% |
| 4 | PAGE_TITLE | VARCHAR2(240) | NOT NULL | Identificacao | Titulo traduzido da pagina | — | 🟡 65% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_af_pages_b]] — via `PAGE_ID` (registro base da pagina de candidatura)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Traducoes de uma pagina de candidatura
```sql
SELECT tl.LANGUAGE, tl.PAGE_TITLE, tl.DESCRIPTION
FROM   IRC_AF_PAGES_TL tl
WHERE  tl.PAGE_ID = :p_page_id;
```

### Filtros comuns
- `PAGE_ID = :p_page_id — Por pagina`
- `LANGUAGE = USERENV('LANG') — Idioma da sessao`

---

## 🔒 Observacoes

- Tabela de traducoes (_TL) — join com _B para dados completos.
- Chave composta: PAGE_ID + LANGUAGE.

---

## 📚 Referencias

- [Oracle Docs — IRC_AF_PAGES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircafpagestl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
