---
id: DOC-HCM-263
doc_type: system-doc
title: "HRT_RATING_MODELS_B — Modelos de Rating — Base"
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
  - rating-models
  - configuracao
  - talent
aliases:
  - HRT_RATING_MODELS_B
  - hrt_rating_models_b
  - hrt-rating-models-b
  - rating-models-base
  - modelos-rating-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_RATING_MODELS_B

## 📌 Visao Geral

Tabela base que define os **modelos de rating** — cada modelo representa uma escala de avaliacao (e.g., 1-5 estrelas, Exceeds/Meets/Below). Modelos sao associados a tipos de conteudo e processos de avaliacao.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Criar escalas de avaliacao reutilizaveis.
- **Performance Management:** Associar modelos a objetivos e competencias.
- **Talent Review:** Definir escalas para potencial, risco e impacto de perda.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RATING_MODEL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do modelo | — | 🟢 100% |
| 2 | RATING_MODEL_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do modelo | — | 🟢 95% |
| 3 | RATING_CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria de rating | [[hrt_rating_categories_b]] | 🟢 90% |
| 4 | MIN_VALUE | NUMBER | NULL | Dados | Valor minimo da escala | — | 🟢 85% |
| 5 | MAX_VALUE | NUMBER | NULL | Dados | Valor maximo da escala | — | 🟢 85% |
| 6 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio | — | 🟢 95% |
| 7 | DATE_TO | DATE | NULL | Data | Data de fim | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_rating_categories_b]] — via `RATING_CATEGORY_ID` (categoria do modelo de classificacao)

### Tabelas-filha (FK de saida)
- [[hrt_rating_models_tl]] — via `RATING_MODEL_ID` (traducoes do modelo de classificacao)
- [[hrt_rating_levels_b]] — via `RATING_MODEL_ID` (traducoes do modelo de classificacao)
- [[hrt_rating_distributions]] — via `RATING_MODEL_ID` (traducoes do modelo de classificacao)

---

## 📎 Uso Tipico

### Modelos de rating ativos
```sql
SELECT rm.RATING_MODEL_ID, rm.RATING_MODEL_CODE,
       rm.MIN_VALUE, rm.MAX_VALUE
FROM   HRT_RATING_MODELS_B rm
WHERE  SYSDATE BETWEEN rm.DATE_FROM AND NVL(rm.DATE_TO, SYSDATE);
```

---

## 🔒 Observacoes

- Sufixo `_B` — traducoes em [[hrt_rating_models_tl]].
- MIN_VALUE e MAX_VALUE definem a faixa numerica da escala.
- Modelos sao reutilizaveis — mesmo modelo pode ser usado em multiplos tipos de conteudo.

---

## 📚 Referencias

- [Oracle Docs — HRT_RATING_MODELS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtratingmodelsb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
