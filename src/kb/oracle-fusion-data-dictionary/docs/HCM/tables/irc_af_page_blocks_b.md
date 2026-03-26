---
id: DOC-HCM-430
doc_type: system-doc
title: "IRC_AF_PAGE_BLOCKS_B — Blocos por Pagina de Fluxo de Candidatura (Base)"
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
  - base
aliases:
  - IRC_AF_PAGE_BLOCKS_B
  - irc_af_page_blocks_b
  - irc-af-page-blocks-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_AF_PAGE_BLOCKS_B

## 📌 Visao Geral

Tabela base que armazena a **associacao entre paginas e blocos** dos fluxos de candidatura (Apply Flows) do modulo Recruiting (IRC). Define quais blocos aparecem em cada pagina.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base) — contem os dados primarios sem traducoes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Composicao de paginas:** define quais blocos compoem cada pagina do fluxo.
- **Ordenacao:** controla a sequencia de blocos dentro de cada pagina.
- **Personalizacao:** permite configurar diferentes composicoes de pagina.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAGE_BLOCK_ID | NUMBER(18) | NOT NULL | PK | Identificador da associacao | — | 🟡 70% |
| 2 | PAGE_ID | NUMBER(18) | NOT NULL | FK | Pagina associada | IRC_AF_PAGES_B | 🟡 70% |
| 3 | BLOCK_ID | NUMBER(18) | NOT NULL | FK | Bloco associado | IRC_AF_BLOCKS_B | 🟡 70% |
| 4 | DISPLAY_SEQUENCE | NUMBER | NULL | Controle | Ordem do bloco na pagina | — | 🟡 60% |
| 5 | REQUIRED_FLAG | VARCHAR2(1) | NULL | Controle | Bloco obrigatorio na pagina | — | 🟡 55% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo/inativo | — | 🟡 60% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_af_pages_b]] — via `PAGE_ID` (pagina do bloco no fluxo de candidatura)
- [[irc_af_blocks_b]] — via `BLOCK_ID` (bloco de conteudo na pagina de candidatura)

### Tabelas-filha (FK de saida)
- [[irc_af_page_blocks_tl]] — via `PAGE_BLOCK_ID` (traducoes do bloco de pagina)

---

## 📎 Uso Tipico

### Blocos de uma pagina de candidatura
```sql
SELECT pb.BLOCK_ID, pb.DISPLAY_SEQUENCE, pb.REQUIRED_FLAG
FROM   IRC_AF_PAGE_BLOCKS_B pb
WHERE  pb.PAGE_ID = :p_page_id
  AND  pb.ENABLED_FLAG = 'Y'
ORDER BY pb.DISPLAY_SEQUENCE;
```

### Filtros comuns
- `PAGE_ID = :p_page_id — Por pagina`
- `ENABLED_FLAG = 'Y' — Associacoes ativas`

---

## 🔒 Observacoes

- Tabela de associacao N:N entre paginas e blocos.
- Tabela base (_B) — traducoes em IRC_AF_PAGE_BLOCKS_TL.
- Permite reutilizar o mesmo bloco em multiplas paginas.

---

## 📚 Referencias

- [Oracle Docs — IRC_AF_PAGE_BLOCKS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircafpageblocksb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
