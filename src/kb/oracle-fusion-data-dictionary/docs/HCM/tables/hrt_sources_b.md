---
id: DOC-HCM-269
doc_type: system-doc
title: "HRT_SOURCES_B — Fontes de Conteudo — Base"
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
  - sources
  - configuracao
  - integracao
aliases:
  - HRT_SOURCES_B
  - hrt_sources_b
  - hrt-sources-b
  - sources-base
  - fontes-conteudo-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_SOURCES_B

## 📌 Visao Geral

Tabela base que define as **fontes** (sources) de itens de conteudo de perfil — provedores externos de competencias, certificacoes e habilidades.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Integracao:** Registrar provedores de dados de competencias.
- **Rastreabilidade:** Identificar a origem de itens importados.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SOURCE_ID | NUMBER(18) | NOT NULL | PK | Identificador da fonte | — | 🟢 95% |
| 2 | SOURCE_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo da fonte | — | 🟢 90% |
| 3 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo da fonte (EXTERNAL, INTERNAL) | — | 🟡 80% |
| 4 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio | — | 🟢 90% |
| 5 | DATE_TO | DATE | NULL | Data | Data de fim | — | 🟢 90% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- [[hrt_sources_tl]] — via `SOURCE_ID` (traducoes da fonte de conteudo)
- [[hrt_content_source_rlats]] — via `SOURCE_ID` (traducoes da fonte de conteudo)

---

## 📎 Uso Tipico

### Fontes ativas
```sql
SELECT s.SOURCE_ID, s.SOURCE_CODE, s.SOURCE_TYPE
FROM   HRT_SOURCES_B s
WHERE  SYSDATE BETWEEN s.DATE_FROM AND NVL(s.DATE_TO, SYSDATE);
```

---

## 🔒 Observacoes

- Sufixo `_B` — traducoes em [[hrt_sources_tl]].

---

## 📚 Referencias

- [Oracle Docs — HRT_SOURCES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtsourcesb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
