---
id: DOC-HCM-235
doc_type: system-doc
title: "HRT_CONTENT_TYPES_B — Tipos de Conteudo de Perfil — Base"
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
  - content-types
  - configuracao
  - talent
aliases:
  - HRT_CONTENT_TYPES_B
  - hrt_content_types_b
  - hrt-content-types-b
  - content-types-base
  - tipos-conteudo-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_CONTENT_TYPES_B

## 📌 Visao Geral

Tabela base que define os **tipos de conteudo** disponiveis para perfis de talento — competencias, habilidades, certificacoes, idiomas, educacao, honrarias, membros de associacoes, etc.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Definir quais tipos de conteudo estao disponiveis no tenant.
- **Estruturacao:** Cada tipo define quais campos dos itens sao utilizados e como.
- **Matching de perfis:** Tipos determinam quais dimensoes sao comparaveis entre perfis.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTENT_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do tipo de conteudo | — | 🟢 100% |
| 2 | CONTENT_TYPE_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo unico do tipo (e.g., COMPETENCY, SKILL) | — | 🟢 100% |
| 3 | ITEM_TYPE | VARCHAR2(30) | NULL | Classificacao | Classificacao do tipo de item | — | 🟡 80% |
| 4 | SUBSCRIBER_CODE | VARCHAR2(30) | NULL | Classificacao | Codigo do modulo consumidor | — | 🟡 75% |
| 5 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio de vigencia | — | 🟢 95% |
| 6 | DATE_TO | DATE | NULL | Data | Data de fim de vigencia | — | 🟢 95% |
| 7 | RATING_MODEL_ID | NUMBER(18) | NULL | FK | Modelo de rating padrao para este tipo | [[hrt_rating_models_b]] | 🟡 80% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_rating_models_b]] — via `RATING_MODEL_ID` (modelo de rating padrao)

### Tabelas-filha (FK de saida)
- [[hrt_content_types_tl]] — via `CONTENT_TYPE_ID` (traducoes do tipo de conteudo)
- [[hrt_content_items_b]] — via `CONTENT_TYPE_ID` (itens deste tipo)
- [[hrt_profile_items]] — via `CONTENT_TYPE_ID` (itens de perfil deste tipo)

---

## 📎 Uso Tipico

### Tipos de conteudo ativos
```sql
SELECT ct.CONTENT_TYPE_ID, ct.CONTENT_TYPE_CODE,
       ct.DATE_FROM, ct.DATE_TO
FROM   HRT_CONTENT_TYPES_B ct
WHERE  SYSDATE BETWEEN ct.DATE_FROM AND NVL(ct.DATE_TO, SYSDATE);
```

---

## 🔒 Observacoes

- Sufixo `_B` indica tabela base — traducoes em [[hrt_content_types_tl]].
- Tipos padrao Oracle incluem: COMPETENCY, CERTIFICATION, DEGREE, LANGUAGE, MEMBERSHIP, HONOR, SKILL.
- Novos tipos podem ser configurados por implementacao.

---

## 📚 Referencias

- [Oracle Docs — HRT_CONTENT_TYPES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtcontenttypesb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
