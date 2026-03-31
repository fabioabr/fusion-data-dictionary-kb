---
id: DOC-HCM-258
doc_type: system-doc
title: "HRT_RATING_CATEGORIES_B — Categorias de Rating — Base"
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
  - rating-categories
  - configuracao
  - talent
aliases:
  - HRT_RATING_CATEGORIES_B
  - hrt_rating_categories_b
  - hrt-rating-categories-b
  - rating-categories-base
  - categorias-rating-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_RATING_CATEGORIES_B

## 📌 Visao Geral

Tabela base que define as **categorias de rating** usadas no talent management. Categorias agrupam modelos de rating por funcao (desempenho, potencial, risco, proficiencia).

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Organizar modelos de rating em categorias funcionais.
- **Classificacao:** Distinguir ratings de desempenho, potencial, risco, etc.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RATING_CATEGORY_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da categoria | — | 🟢 95% |
| 2 | RATING_CATEGORY_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo da categoria (e.g., PERFORMANCE, POTENTIAL) | — | 🟢 90% |
| 3 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio | — | 🟢 90% |
| 4 | DATE_TO | DATE | NULL | Data | Data de fim | — | 🟢 90% |
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
- [[hrt_rating_categories_tl]] — via `RATING_CATEGORY_ID` (traducoes da categoria de classificacao)
- [[hrt_rating_models_b]] — via `RATING_CATEGORY_ID` (traducoes da categoria de classificacao)

---

## 📎 Uso Tipico

### Categorias ativas
```sql
SELECT rc.RATING_CATEGORY_ID, rc.RATING_CATEGORY_CODE
FROM   HRT_RATING_CATEGORIES_B rc
WHERE  SYSDATE BETWEEN rc.DATE_FROM AND NVL(rc.DATE_TO, SYSDATE);
```

---

## 🔒 Observacoes

- Sufixo `_B` — traducoes em [[hrt_rating_categories_tl]].
- Categorias padrao: PERFORMANCE, POTENTIAL, RISK_OF_LOSS, IMPACT_OF_LOSS, PROFICIENCY.

---

## 📚 Referencias

- [Oracle Docs — HRT_RATING_CATEGORIES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtratingcategoriesb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[personprofileperformanceratingpvo|PersonProfilePerformanceRatingPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PerfRtgCatBusinessGroupId2 | — |
| CATEGORY_ID | PerfRtgCatCategoryId | — |
| LAST_UPDATE_DATE | RatingCategoriesBPEOLastUpdateDate | ✅ |
| LOWER_BOUNDARY | PerfRtgCatLowerBoundary | — |
| RATING_MODEL_ID | PerfRtgCatRatingModelId1 | — |
| UPPER_BOUNDARY | PerfRtgCatUpperBoundary | — |

### [[ratingcategoriesfirstpvo|RatingCategoriesFirstPVO]] (HCM · BICC: 5/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingCategoriesBPEOBusinessGroupId | ✅ |
| CATEGORY_ID | RatingCategoriesBPEOCategoryId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LOWER_BOUNDARY | RatingCategoriesBPEOLowerBoundary | ✅ |
| MODULE_ID | RatingCategoriesBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_MODEL_ID | RatingCategoriesBPEORatingModelId | — |
| UPPER_BOUNDARY | RatingCategoriesBPEOUpperBoundary | ✅ |
