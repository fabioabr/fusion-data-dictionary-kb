---
id: DOC-HCM-259
doc_type: system-doc
title: "HRT_RATING_CATEGORIES_TL — Categorias de Rating — Traducoes"
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
  - traducoes
  - nls
  - rating-categories
aliases:
  - HRT_RATING_CATEGORIES_TL
  - hrt_rating_categories_tl
  - hrt-rating-categories-tl
  - rating-categories-tl
  - categorias-rating-traducoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_RATING_CATEGORIES_TL

## 📌 Visao Geral

Tabela de traducoes que armazena textos em multiplos idiomas para cada registro definido em [[hrt_rating_categories_b]].

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Multi-idioma:** Nomes e descricoes traduzidos para multiplos idiomas.
- **Exibicao:** Textos traduzidos para interfaces de usuario e relatorios.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RATING_CATEGORY_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do registro base | [[hrt_rating_categories_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 4 | RATING_CATEGORY_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome/texto traduzido | — | 🟢 100% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_rating_categories_b]] — via `RATING_CATEGORY_ID` (registro base da categoria de classificacao)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Texto traduzido no idioma do usuario
```sql
SELECT tl.RATING_CATEGORY_NAME, tl.DESCRIPTION
FROM   HRT_RATING_CATEGORIES_TL tl
WHERE  tl.RATING_CATEGORY_ID = :p_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observacoes

- Sufixo `_TL` indica tabela de traducao — PK composta por (RATING_CATEGORY_ID, LANGUAGE).
- JOIN com [[hrt_rating_categories_b]] para dados completos.

---

## 📚 Referencias

- [Oracle Docs — HRT_RATING_CATEGORIES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtratingcategoriestl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[personprofileperformanceratingpvo|PersonProfilePerformanceRatingPVO]] (HCM · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PerfRtgBusinessGroupId2 | — |
| CATEGORY_DESCRIPTION | PerfRtgCategoryDescription | — |
| CATEGORY_ID | PerfRtgCategoryId | — |
| CATEGORY_NAME | PerfRtgCategoryName | — |
| LANGUAGE | PerfRtgLanguage3 | — |
| LAST_UPDATE_DATE | RtgCategoriesTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgCategoriesTransltionPEOLastUpdateDate | ✅ |

### [[ratingcategoriesfirstpvo|RatingCategoriesFirstPVO]] (HCM · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingCategoriesTranslationPEOBusinessGroupId | — |
| CATEGORY_DESCRIPTION | RatingCategoriesTranslationPEOCategoryDescription | ✅ |
| CATEGORY_ID | RatingCategoriesTranslationPEOCategoryId | — |
| CATEGORY_NAME | RatingCategoriesTranslationPEOCategoryName | ✅ |
| LANGUAGE | RatingCategoriesTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | RatingCategoriesTranslationPLastUpdateDate | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[ratingcategoriesfirsttranslationpvo|RatingCategoriesFirstTranslationPVO]] (HCM · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CATEGORY_DESCRIPTION | CategoryDescription | ✅ |
| CATEGORY_ID | CategoryId | ✅ |
| CATEGORY_NAME | CategoryName | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| SOURCE_LANG | SourceLang | ✅ |
