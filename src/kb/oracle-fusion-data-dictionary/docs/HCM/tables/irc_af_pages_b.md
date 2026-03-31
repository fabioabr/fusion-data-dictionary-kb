---
id: DOC-HCM-428
doc_type: system-doc
title: "IRC_AF_PAGES_B — Paginas de Fluxo de Candidatura (Base)"
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
  - base
aliases:
  - IRC_AF_PAGES_B
  - irc_af_pages_b
  - irc-af-pages-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_AF_PAGES_B

## 📌 Visao Geral

Tabela base que armazena as **definicoes de paginas** dos fluxos de candidatura (Apply Flows) do modulo Recruiting (IRC). Cada pagina representa uma etapa do processo de candidatura online.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base) — contem os dados primarios sem traducoes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao de fluxo:** define as paginas/etapas do processo de candidatura.
- **Experiencia do candidato:** controla a navegacao no formulario de candidatura.
- **Personalizacao:** permite diferentes fluxos por tipo de vaga ou site de carreiras.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador da pagina | — | 🟡 70% |
| 2 | PAGE_CODE | VARCHAR2(80) | NOT NULL | Identificacao | Codigo da pagina | — | 🟡 65% |
| 3 | PAGE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo da pagina | — | 🟡 60% |
| 4 | DISPLAY_SEQUENCE | NUMBER | NULL | Controle | Ordem de exibicao | — | 🟡 60% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo/inativo | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saida)
- [[irc_af_pages_tl]] — via `PAGE_ID` (traducoes da pagina de candidatura)
- [[irc_af_page_blocks_b]] — via `PAGE_ID` (blocos da pagina)

---

## 📎 Uso Tipico

### Listar paginas do fluxo de candidatura
```sql
SELECT p.PAGE_ID, p.PAGE_CODE, p.PAGE_TYPE,
       p.DISPLAY_SEQUENCE
FROM   IRC_AF_PAGES_B p
WHERE  p.ENABLED_FLAG = 'Y'
ORDER BY p.DISPLAY_SEQUENCE;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y' — Paginas ativas`
- `PAGE_TYPE = :p_type — Por tipo`

---

## 🔒 Observacoes

- Tabela base (_B) — traducoes em IRC_AF_PAGES_TL.
- Paginas definem as etapas que o candidato percorre durante a candidatura.
- Cada pagina contem um ou mais blocos (IRC_AF_PAGE_BLOCKS_B).

---

## 📚 Referencias

- [Oracle Docs — IRC_AF_PAGES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircafpagesb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[applyflowsectionpagepvo|ApplyFlowSectionPagePVO]] (HCM · BICC: 1/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ApplyFlowPageBPEOCreatedBy | — |
| CREATION_DATE | ApplyFlowPageBPEOCreationDate | — |
| LAST_UPDATE_DATE | ApplyFlowPageBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ApplyFlowPageBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ApplyFlowPageBPEOLastUpdatedBy | — |
| PAGE_ID | PageId | — |
| PAGE_SEQ_NUM | ApplyFlowPageBPEOPageSeqNum | — |
