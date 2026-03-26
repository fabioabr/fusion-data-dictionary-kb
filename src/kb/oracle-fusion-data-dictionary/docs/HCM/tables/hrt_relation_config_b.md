---
id: DOC-HCM-265
doc_type: system-doc
title: "HRT_RELATION_CONFIG_B — Configuracao de Relacionamentos de Perfil — Base"
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
  - relation-config
  - configuracao
  - talent
aliases:
  - HRT_RELATION_CONFIG_B
  - hrt_relation_config_b
  - hrt-relation-config-b
  - relation-config-base
  - configuracao-relacionamentos-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_RELATION_CONFIG_B

## 📌 Visao Geral

Tabela base que armazena a **configuracao de relacionamentos** entre perfis de talento. Define regras e parametros para os tipos de relacionamento permitidos.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Definir regras de relacionamento entre perfis.
- **Governanca:** Controlar tipos de relacionamento validos.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RELATION_CONFIG_ID | NUMBER(18) | NOT NULL | PK | Identificador da configuracao | — | 🟢 90% |
| 2 | RELATION_TYPE | VARCHAR2(30) | NOT NULL | Classificacao | Tipo de relacionamento | — | 🟡 85% |
| 3 | SOURCE_USAGE_CODE | VARCHAR2(30) | NULL | Classificacao | Uso do perfil de origem | — | 🟡 80% |
| 4 | TARGET_USAGE_CODE | VARCHAR2(30) | NULL | Classificacao | Uso do perfil de destino | — | 🟡 80% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- [[hrt_relation_config_tl]] — via `RELATION_CONFIG_ID` (traducoes da configuracao de relacao)

---

## 📎 Uso Tipico

### Configuracoes de relacionamento
```sql
SELECT rc.RELATION_TYPE, rc.SOURCE_USAGE_CODE, rc.TARGET_USAGE_CODE
FROM   HRT_RELATION_CONFIG_B rc;
```

---

## 🔒 Observacoes

- Sufixo `_B` — traducoes em [[hrt_relation_config_tl]].
- Define quais combinacoes de perfil podem ser relacionadas.

---

## 📚 Referencias

- [Oracle Docs — HRT_RELATION_CONFIG_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtrelationconfigb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
