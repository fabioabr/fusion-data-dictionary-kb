---
id: DOC-HCM-426
doc_type: system-doc
title: "IRC_AF_BLOCKS_B — Blocos de Fluxo de Candidatura (Base)"
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
  - bloco-candidatura
  - base
aliases:
  - IRC_AF_BLOCKS_B
  - irc_af_blocks_b
  - irc-af-blocks-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_AF_BLOCKS_B

## 📌 Visao Geral

Tabela base que armazena as **definicoes de blocos** (blocks) dos fluxos de candidatura (Apply Flows) do modulo Recruiting (IRC). Cada bloco representa uma secao do formulario de candidatura.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base) — contem os dados primarios sem traducoes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao de formularios:** define blocos/secoes do formulario de candidatura.
- **Experiencia do candidato:** controla quais informacoes sao solicitadas.
- **Personalizacao:** permite diferentes formularios por tipo de vaga.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BLOCK_ID | NUMBER(18) | NOT NULL | PK | Identificador do bloco | — | 🟡 70% |
| 2 | BLOCK_CODE | VARCHAR2(80) | NOT NULL | Identificacao | Codigo do bloco | — | 🟡 65% |
| 3 | BLOCK_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do bloco | — | 🟡 60% |
| 4 | DISPLAY_SEQUENCE | NUMBER | NULL | Controle | Ordem de exibicao | — | 🟡 60% |
| 5 | REQUIRED_FLAG | VARCHAR2(1) | NULL | Controle | Bloco obrigatorio | — | 🟡 55% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo/inativo | — | 🟡 60% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saida)
- [[irc_af_blocks_tl]] — via `BLOCK_ID` (traducoes do bloco de candidatura)
- [[irc_af_page_blocks_b]] — via `BLOCK_ID` (associacao com paginas)

---

## 📎 Uso Tipico

### Listar blocos ativos de candidatura
```sql
SELECT b.BLOCK_ID, b.BLOCK_CODE, b.BLOCK_TYPE,
       b.DISPLAY_SEQUENCE, b.REQUIRED_FLAG
FROM   IRC_AF_BLOCKS_B b
WHERE  b.ENABLED_FLAG = 'Y'
ORDER BY b.DISPLAY_SEQUENCE;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y' — Blocos ativos`
- `BLOCK_TYPE = :p_type — Por tipo de bloco`

---

## 🔒 Observacoes

- Tabela base (_B) — traducoes em IRC_AF_BLOCKS_TL.
- Blocos definem secoes do formulario de candidatura (ex.: dados pessoais, experiencia, educacao).
- Parte do framework de Apply Flows do modulo Recruiting.

---

## 📚 Referencias

- [Oracle Docs — IRC_AF_BLOCKS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircafblocksb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
