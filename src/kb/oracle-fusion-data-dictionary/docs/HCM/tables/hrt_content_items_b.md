---
id: DOC-HCM-232
doc_type: system-doc
title: "HRT_CONTENT_ITEMS_B — Itens de Conteudo de Perfil — Base"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - content-items
  - competencias
  - talent
aliases:
  - HRT_CONTENT_ITEMS_B
  - hrt_content_items_b
  - hrt-content-items-b
  - content-items-base
  - itens-conteudo-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_CONTENT_ITEMS_B

## 📌 Visao Geral

Tabela base que armazena os **itens de conteudo** disponiveis para associacao a perfis de talento — competencias, habilidades, certificacoes, graus academicos, idiomas e outros conteudos configuraveis.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Catalogo de conteudos:** Repositorio centralizado de competencias, habilidades e qualificacoes.
- **Perfis de talento:** Itens associaveis a perfis de pessoa ou cargo via HRT_PROFILE_ITEMS.
- **Matching:** Base para comparacao de perfis (gap analysis) em talent management.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTENT_ITEM_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do item de conteudo | — | 🟢 100% |
| 2 | CONTENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de conteudo ao qual pertence | [[hrt_content_types_b]] | 🟢 100% |
| 3 | ITEM_KEY | VARCHAR2(30) | NULL | Identificacao | Chave natural do item | — | 🟢 90% |
| 4 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio de vigencia | — | 🟢 95% |
| 5 | DATE_TO | DATE | NULL | Data | Data de fim de vigencia | — | 🟢 95% |
| 6 | ITEM_TEXT_240 | VARCHAR2(240) | NULL | Dados | Texto livre associado ao item | — | 🟡 75% |
| 7 | ITEM_NUMBER_1 | NUMBER | NULL | Dados | Valor numerico generico 1 | — | 🟡 70% |
| 8 | ITEM_DATE_1 | DATE | NULL | Dados | Data generica 1 | — | 🟡 70% |
| 9 | COUNTRY_ID | NUMBER(18) | NULL | FK | Pais associado ao item | — | 🟡 70% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo)

### Tabelas-filha (FK de saida)
- [[hrt_content_items_tl]] — via `CONTENT_ITEM_ID` (traducoes do item de conteudo)
- [[hrt_profile_items]] — via `CONTENT_ITEM_ID` (itens associados a perfis)

---

## 📎 Uso Tipico

### Itens de conteudo por tipo
```sql
SELECT ci.CONTENT_ITEM_ID, ci.CONTENT_TYPE_ID,
       ci.DATE_FROM, ci.DATE_TO
FROM   HRT_CONTENT_ITEMS_B ci
WHERE  ci.CONTENT_TYPE_ID = :p_content_type_id
  AND  SYSDATE BETWEEN ci.DATE_FROM AND NVL(ci.DATE_TO, SYSDATE);
```

---

## 🔒 Observacoes

- Sufixo `_B` indica tabela base (sem traducao) — textos traduzidos ficam em [[hrt_content_items_tl]].
- Campos genericos (ITEM_TEXT_240, ITEM_NUMBER_1, ITEM_DATE_1) sao usados conforme configuracao do content type.
- O `OBJECT_VERSION_NUMBER` implementa controle de concorrencia otimista.

---

## 📚 Referencias

- [Oracle Docs — HRT_CONTENT_ITEMS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtcontentitemsb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
