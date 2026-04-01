---
id: DOC-HCM-432
doc_type: system-doc
title: "IRC_AF_SECTIONS_B — Secoes de Fluxo de Candidatura (Base)"
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
  - secao-candidatura
  - base
aliases:
  - IRC_AF_SECTIONS_B
  - irc_af_sections_b
  - irc-af-sections-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_AF_SECTIONS_B

## 📌 Visao Geral

Tabela base que armazena as **definicoes de secoes** dos fluxos de candidatura (Apply Flows) do modulo Recruiting (IRC). Secoes sao subdivisoes dentro de blocos.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base) — contem os dados primarios sem traducoes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Granularidade de formulario:** subdivide blocos em secoes menores.
- **Organizacao visual:** agrupa campos relacionados dentro de um bloco.
- **Personalizacao:** permite configurar secoes por tipo de vaga.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SECTION_ID | NUMBER(18) | NOT NULL | PK | Identificador da secao | — | 🟡 70% |
| 2 | SECTION_CODE | VARCHAR2(80) | NOT NULL | Identificacao | Codigo da secao | — | 🟡 65% |
| 3 | BLOCK_ID | NUMBER(18) | NOT NULL | FK | Bloco pai | IRC_AF_BLOCKS_B | 🟡 65% |
| 4 | SECTION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo da secao | — | 🟡 60% |
| 5 | DISPLAY_SEQUENCE | NUMBER | NULL | Controle | Ordem de exibicao | — | 🟡 60% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo/inativo | — | 🟡 60% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_af_blocks_b]] — via `BLOCK_ID` (bloco da secao no fluxo de candidatura)

### Tabelas-filha (FK de saida)
- [[irc_af_sections_tl]] — via `SECTION_ID` (traducoes da secao de candidatura)

---

## 📎 Uso Tipico

### Secoes de um bloco de candidatura
```sql
SELECT s.SECTION_ID, s.SECTION_CODE, s.SECTION_TYPE,
       s.DISPLAY_SEQUENCE
FROM   IRC_AF_SECTIONS_B s
WHERE  s.BLOCK_ID = :p_block_id
  AND  s.ENABLED_FLAG = 'Y'
ORDER BY s.DISPLAY_SEQUENCE;
```

### Filtros comuns
- `BLOCK_ID = :p_block_id — Por bloco`
- `ENABLED_FLAG = 'Y' — Secoes ativas`

---

## 🔒 Observacoes

- Tabela base (_B) — traducoes em IRC_AF_SECTIONS_TL.
- Secoes sao subdivisoes de blocos no formulario de candidatura.
- Parte do framework hierarquico: Flow > Page > Block > Section.

---

## 📚 Referencias

- [Oracle Docs — IRC_AF_SECTIONS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircafsectionsb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[applyflowsectionpagepvo|ApplyFlowSectionPagePVO]] (HCM · BICC: 3/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AF_VERSION_ID | AfVersionId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| SECTION_ID | SectionId | ✅ |
| SECTION_SEQ_NUM | SectionSeqNum | ✅ |
