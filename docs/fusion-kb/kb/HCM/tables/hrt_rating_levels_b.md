---
id: DOC-HCM-261
doc_type: system-doc
title: "HRT_RATING_LEVELS_B — Niveis de Rating — Base"
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
  - rating-levels
  - configuracao
  - talent
aliases:
  - HRT_RATING_LEVELS_B
  - hrt_rating_levels_b
  - hrt-rating-levels-b
  - rating-levels-base
  - niveis-rating-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_RATING_LEVELS_B

## 📌 Visao Geral

Tabela base que define os **niveis de rating** dentro de cada modelo — como "Exceeds Expectations", "Meets Expectations". Cada nivel tem valor numerico e sequencia.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Avaliacao:** Definir os niveis disponiveis para avaliacao.
- **Configuracao:** Cada modelo possui seus proprios niveis.
- **Analytics:** Base para analise de distribuicao de avaliacoes.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RATING_LEVEL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do nivel | — | 🟢 100% |
| 2 | RATING_MODEL_ID | NUMBER(18) | NOT NULL | FK | Modelo de rating | [[hrt_rating_models_b]] | 🟢 100% |
| 3 | STEP_VALUE | NUMBER | NOT NULL | Dados | Valor numerico do nivel | — | 🟢 95% |
| 4 | FROM_VALUE | NUMBER | NULL | Dados | Valor inferior da faixa | — | 🟡 80% |
| 5 | TO_VALUE | NUMBER | NULL | Dados | Valor superior da faixa | — | 🟡 80% |
| 6 | SEQUENCE | NUMBER | NULL | Dados | Ordem de exibicao | — | 🟢 90% |
| 7 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio | — | 🟢 95% |
| 8 | DATE_TO | DATE | NULL | Data | Data de fim | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_rating_models_b]] — via `RATING_MODEL_ID` (modelo de classificacao do nivel)

### Tabelas-filha (FK de saida)
- [[hrt_rating_levels_tl]] — via `RATING_LEVEL_ID` (traducoes do nivel de classificacao)
- [[hrt_profile_items]] — via `RATING_LEVEL_ID` (traducoes do nivel de classificacao)

---

## 📎 Uso Tipico

### Niveis de um modelo
```sql
SELECT rl.RATING_LEVEL_ID, rl.STEP_VALUE, rl.SEQUENCE
FROM   HRT_RATING_LEVELS_B rl
WHERE  rl.RATING_MODEL_ID = :p_rating_model_id
ORDER BY rl.SEQUENCE;
```

---

## 🔒 Observacoes

- Sufixo `_B` — traducoes em [[hrt_rating_levels_tl]].
- STEP_VALUE e o valor numerico; SEQUENCE define a ordem de exibicao.

---

## 📚 Referencias

- [Oracle Docs — HRT_RATING_LEVELS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtratinglevelsb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[competencycontentitemratingpvo|CompetencyContentItemRatingPVO]] (HCM · BICC: 4/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | ✅ |
| CAREER_STR_DEV | CareerStrDev | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | FromPoints | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | — |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | RatingLevelBPEONumericRating | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | — |
| REVIEW_POINTS | ReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | ToPoints | — |

### [[competencypvo|CompetencyPVO]] (HCM · BICC: 6/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId5 | — |
| BUSINESS_GROUP_ID | RLvlBPEOInterestBusinessGroup | — |
| BUSINESS_GROUP_ID | RLvlBPEOProfBusinessGroupId1 | — |
| CAREER_STR_DEV | RLvlBPEOInterestCareerStrDev | — |
| CAREER_STR_DEV | RLvlBPEOPerfRtgCareerStrDev | — |
| DATE_FROM | RLvlBPEOInterestDateFrom | — |
| DATE_FROM | RLvlBPEOPerfRtgDateFrom | — |
| DATE_FROM | RLvlBPEOProfDateFrom | — |
| DATE_TO | RLvlBPEOInterestDateTo | — |
| DATE_TO | RLvlBPEOPerfRtgDateTo | — |
| DATE_TO | RLvlBPEOProfDateTo | — |
| FROM_POINTS | RLvlBPEOInterestFromPoints | — |
| FROM_POINTS | RLvlBPEOPerfRtgFromPoints | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_DATE | RLvlBPEOPerfRtgLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RLvlBPEOProfLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| MAX_RATING_DISTRIBUTION | RLvlBPEOInterestMaxRtgDistri | — |
| MAX_RATING_DISTRIBUTION | RLvlBPEOPerfRtgMaxRtgDistribu | — |
| MAX_RATING_DISTRIBUTION | RLvlBPEOProfMaxRtgDistributio | — |
| MIN_RATING_DISTRIBUTION | RLvlBPEOInterestMinRtgDistri | — |
| MIN_RATING_DISTRIBUTION | RLvlBPEOPerfRtgMinRtgDistribu | — |
| MIN_RATING_DISTRIBUTION | RLvlBPEOProfMinRtgDistributio | — |
| MODULE_ID | RLvlBPEOInterestModuleId | — |
| MODULE_ID | RLvlBPEOPerfRtgModuleId | — |
| NUMERIC_RATING | RLvlBPEOInterestNumericRating | — |
| NUMERIC_RATING | RLvlBPEOPerfRtgNumericRating | — |
| NUMERIC_RATING | RLvlBPEOProfNumericRating | — |
| RATING_LEVEL_CODE | RLvlBPEOInterestRLCode | ✅ |
| RATING_LEVEL_CODE | RLvlBPEOPerfRtgLevelCode | ✅ |
| RATING_LEVEL_CODE | RLvlBPEOProfRatingLevelCode | ✅ |
| RATING_LEVEL_ID | RLvlBPEOInterestRatingLevelId | — |
| RATING_LEVEL_ID | RLvlBPEOPerfRtgRatingLevelId2 | — |
| RATING_LEVEL_ID | RLvlBPEOProfRatingLevelId | — |
| RATING_MODEL_ID | RLvlBPEOPerfRtgRatingModelId3 | — |
| RATING_MODEL_ID | RLvlBPEOProfRatingMdlId | — |
| REVIEW_POINTS | RLvlBPEOInterestReviewPoints | — |
| REVIEW_POINTS | RLvlBPEOPerfRtgReviewPoints | — |
| REVIEW_POINTS | RLvlBPEOProfReviewPoints | — |
| STAR_RATING | RLvlBPEOInterestStarRating | — |
| STAR_RATING | RLvlBPEOPerfRtgStarRating | — |
| STAR_RATING | RLvlBPEOProfStarRating | — |
| TO_POINTS | RLvlBPEOInterestToPoints | — |
| TO_POINTS | RLvlBPEOPerfRtgToPoints | — |
| TO_POINTS | RLvlBPEOProfToPoints | — |

### [[contentitemvaluepvo|ContentItemValuePVO]] (HCM · BICC: 13/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | RatingLevelBPEOAttributeCategory | ✅ |
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | — |
| CAREER_STR_DEV | RatingLevelBPEOCareerStrDev | ✅ |
| CREATED_BY | RatingLevelBPEOCreatedBy | — |
| CREATION_DATE | RatingLevelBPEOCreationDate | — |
| DATE_FROM | RatingLevelBPEODateFrom | ✅ |
| DATE_TO | RatingLevelBPEODateTo | ✅ |
| FROM_POINTS | RatingLevelBPEOFromPoints | ✅ |
| LAST_UPDATE_DATE | RatingLevelBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RatingLevelBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RatingLevelBPEOLastUpdatedBy | — |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | ✅ |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | ✅ |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | RatingLevelBPEONumericRating | ✅ |
| OBJECT_VERSION_NUMBER | RatingLevelBPEOObjectVersionNumber | — |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | — |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | — |
| REVIEW_POINTS | RatingLevelBPEOReviewPoints | ✅ |
| STAR_RATING | RatingLevelBPEOStarRating | ✅ |
| TO_POINTS | RatingLevelBPEOToPoints | ✅ |

### [[criticalityprofileitempvo|CriticalityProfileItemPVO]] (HCM · BICC: 1/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RtgLvlBusinessGroupId1 | — |
| CAREER_STR_DEV | RtgLvlCareerStrDev | — |
| DATE_FROM | RtgLvlDateFrom1 | — |
| DATE_TO | RtgLvlDateTo1 | — |
| FROM_POINTS | RtgLvlFromPoints | — |
| LAST_UPDATE_DATE | RtgLvlLastUpdateDate1 | ✅ |
| MAX_RATING_DISTRIBUTION | RtgLvlMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RtgLvlMinRatingDistribution | — |
| NUMERIC_RATING | RtgLvlNumericRating | — |
| RATING_LEVEL_CODE | RtgLvlRatingLevelCode | — |
| RATING_LEVEL_ID | RtgLvlRatingLevelId | — |
| RATING_MODEL_ID | RtgLvlRatingModelId | — |
| REVIEW_POINTS | ReviewPoints | — |
| STAR_RATING | RtgLvlStarRating | — |
| TO_POINTS | RtgLvlToPoints | — |

### [[goaltargetoutcomeprofilespvo|GoalTargetOutcomeProfilesPVO]] (HCM · BICC: 11/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId2 | — |
| CAREER_STR_DEV | RatingLevelBPEOCareerStrDev | ✅ |
| DATE_FROM | RatingLevelBPEODateFrom1 | ✅ |
| DATE_TO | RatingLevelBPEODateTo1 | ✅ |
| FROM_POINTS | RatingLevelBPEOFromPoints | ✅ |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | ✅ |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | ✅ |
| NUMERIC_RATING | RatingLevelBPEONumericRating | ✅ |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | — |
| RATING_LEVEL_ID | RatingLevelId | — |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId4 | — |
| REVIEW_POINTS | RatingLevelBPEOReviewPoints | ✅ |
| STAR_RATING | RatingLevelBPEOStarRating | ✅ |
| TO_POINTS | RatingLevelBPEOToPoints | ✅ |

### [[impactratinglevelpvo|ImpactRatingLevelPVO]] (HCM · BICC: 4/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | ✅ |
| CAREER_STR_DEV | CareerStrDev | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | FromPoints | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | — |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | NumericRating | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | — |
| REVIEW_POINTS | ReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | ToPoints | — |

### [[languagepvo|LanguagePVO]] (HCM · BICC: 6/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RLReadingBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | RLSpeakBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | RLWriteBusinessGroupId3 | — |
| CAREER_STR_DEV | RLReadingCareerStrDev | — |
| CAREER_STR_DEV | RLSpeakCareerStrDev | — |
| CAREER_STR_DEV | RLWriteCareerStrDev | — |
| DATE_FROM | RLReadingDateFrom | — |
| DATE_FROM | RLSpeakDateFrom | — |
| DATE_FROM | RLWriteDateFrom | — |
| DATE_TO | RLReadingDateTo | — |
| DATE_TO | RLSpeakDateTo | — |
| DATE_TO | RLWriteDateTo | — |
| FROM_POINTS | RLReadingFromPoints | — |
| FROM_POINTS | RLSpeakFromPoints | — |
| FROM_POINTS | RLWriteFromPoints | — |
| LAST_UPDATE_DATE | RtgLvlReadingLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgLvlSpeakingLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgLvlWritingLastUpdateDate | ✅ |
| MAX_RATING_DISTRIBUTION | RLReadMaxRatingDistribution | — |
| MAX_RATING_DISTRIBUTION | RLSpeakMaxRatingDistribution | — |
| MAX_RATING_DISTRIBUTION | RLWriteMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RLReadMinRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RLSpeakMinRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RLWriteMinRatingDistribution | — |
| NUMERIC_RATING | RLReadingNumericRating | — |
| NUMERIC_RATING | RLSpeakNumericRating | — |
| NUMERIC_RATING | RLWriteNumericRating | — |
| RATING_LEVEL_CODE | RLReadingRatingLevelCode | ✅ |
| RATING_LEVEL_CODE | RLSpeakRatingLevelCode | ✅ |
| RATING_LEVEL_CODE | RLWriteRatingLevelCode | ✅ |
| RATING_LEVEL_ID | RLReadingRatingLevelId | — |
| RATING_LEVEL_ID | RLSpeakRatingLevelId | — |
| RATING_LEVEL_ID | RLWriteRatingLevelId | — |
| REVIEW_POINTS | RLReadingReviewPoints | — |
| REVIEW_POINTS | RLSpeakReviewPoints | — |
| REVIEW_POINTS | RLWriteReviewPoints | — |
| STAR_RATING | RLReadingStarRating | — |
| STAR_RATING | RLSpeakStarRating | — |
| STAR_RATING | RLWriteStarRating | — |
| TO_POINTS | RLReadingToPoints | — |
| TO_POINTS | RLSpeakToPoints | — |
| TO_POINTS | RLWriteToPoints | — |

### [[managerperformanceoverallratingpvo|ManagerPerformanceOverallRatingPVO]] (HCM · BICC: 3/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | — |
| CAREER_STR_DEV | RatingLevelBPEOCareerStrDev | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | RatingLevelBPEOFromPoints | — |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | — |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | RatingLevelBPEONumericRating | — |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | ✅ |
| REVIEW_POINTS | RatingLevelBPEOReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | RatingLevelBPEOToPoints | — |

### [[performancedocratingdistributionpvo|PerformanceDocRatingDistributionPVO]] (HCM · BICC: 2/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | — |
| CAREER_STR_DEV | RatingLevelBPEOCareerStrDev | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | RatingLevelBPEOFromPoints | — |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | ✅ |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | ✅ |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | RatingLevelBPEONumericRating | — |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | — |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | — |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | — |
| REVIEW_POINTS | RatingLevelBPEOReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | RatingLevelBPEOToPoints | — |

### [[performancedocratinglevelpvo|PerformanceDocRatingLevelPVO]] (HCM · BICC: 10/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | — |
| CAREER_STR_DEV | RatingLevelBPEOCareerStrDev | ✅ |
| DATE_FROM | RatingLevelBPEODateFrom | ✅ |
| DATE_TO | RatingLevelBPEODateTo | ✅ |
| FROM_POINTS | RatingLevelBPEOFromPoints | — |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | ✅ |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | ✅ |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | RatingLevelBPEONumericRating | ✅ |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | ✅ |
| REVIEW_POINTS | RatingLevelBPEOReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | ✅ |
| TO_POINTS | RatingLevelBPEOToPoints | — |

### [[performanceitemratingpvo|PerformanceItemRatingPVO]] (HCM · BICC: 3/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | — |
| CAREER_STR_DEV | RatingLevelBPEOCareerStrDev | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | RatingLevelBPEOFromPoints | — |
| LAST_UPDATE_DATE | RatingLevelBPEOLastUpdateDate | ✅ |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | — |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | RatingLevelBPEONumericRating | ✅ |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | — |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | — |
| REVIEW_POINTS | RatingLevelBPEOReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | RatingLevelBPEOToPoints | — |

### [[performanceoverallratingpvo|PerformanceOverallRatingPVO]] (HCM · BICC: 5/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | ✅ |
| CAREER_STR_DEV | RatingLevelBPEOCareerStrDev | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | RatingLevelBPEOFromPoints | — |
| LAST_UPDATE_DATE | RatingLevelBPEOLastUpdateDate | ✅ |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | — |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | RatingLevelBPEONumericRating | ✅ |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | — |
| REVIEW_POINTS | RatingLevelBPEOReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | RatingLevelBPEOToPoints | — |

### [[performancesectionratingpvo|PerformanceSectionRatingPVO]] (HCM · BICC: 3/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId5 | — |
| CAREER_STR_DEV | RatingLevelBPEOCareerStrDev | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | RatingLevelBPEOFromPoints | — |
| LAST_UPDATE_DATE | RatingLevelBPEOLastUpdateDate | ✅ |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | — |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | RatingLevelBPEONumericRating | ✅ |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | — |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | — |
| REVIEW_POINTS | RatingLevelBPEOReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | RatingLevelBPEOToPoints | — |

### [[personprofileperformanceratingpvo|PersonProfilePerformanceRatingPVO]] (HCM · BICC: 1/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RtgLvlBusinessGroupId1 | — |
| CAREER_STR_DEV | RtgLvlCareerStrDev | — |
| CREATED_BY | RtgLvlCreatedBy1 | — |
| CREATION_DATE | RtgLvlCreationDate1 | — |
| DATE_FROM | RtgLvlDateFrom | — |
| DATE_TO | RtgLvlDateTo | — |
| FROM_POINTS | RtgLvlFromPoints | — |
| LAST_UPDATE_DATE | RtgLvlLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | RtgLvlLastUpdateLogin1 | — |
| LAST_UPDATED_BY | RtgLvlLastUpdatedBy1 | — |
| MAX_RATING_DISTRIBUTION | RtgLvlMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RtgLvlMinRatingDistribution | — |
| MODULE_ID | RtgLvlModuleId | — |
| NUMERIC_RATING | RtgLvlNumericRating | — |
| OBJECT_VERSION_NUMBER | RtgLvlObjectVersionNumber1 | — |
| RATING_LEVEL_CODE | RtgLvlRatingLevelCode | — |
| RATING_LEVEL_ID | RtgLvlRatingLevelId | — |
| REVIEW_POINTS | RtgLvlReviewPoints | — |
| STAR_RATING | RtgLvlStarRating | — |
| TO_POINTS | RtgLvlToPoints | — |

### [[potentialpvo|PotentialPVO]] (HCM · BICC: 3/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RtgLvlPotBusinessGroupId | — |
| CAREER_STR_DEV | RtgLvlPotCareerStrDev | — |
| DATE_FROM | RtgLvlPotDateFrom | — |
| DATE_TO | RtgLvlPotDateTo | — |
| FROM_POINTS | RtgLvlPotFromPoints | — |
| LAST_UPDATE_DATE | RatingLevelBPEOLastUpdateDate | ✅ |
| MAX_RATING_DISTRIBUTION | RtgLvlPotMaxRatingDistrib | — |
| MIN_RATING_DISTRIBUTION | RtgLvlPotMinRatingDistrib | — |
| NUMERIC_RATING | ItemDecimal1 | ✅ |
| NUMERIC_RATING | RtgLvlPotNumericRating | — |
| RATING_LEVEL_CODE | RtgLvlPotRatingLevelCode | ✅ |
| RATING_LEVEL_ID | RtgLvlPotRatingLevelId | — |
| REVIEW_POINTS | RtgLvlPotReviewPoints | — |
| STAR_RATING | RtgLvlPotStarRating | — |
| TO_POINTS | RtgLvlPotToPoints | — |

### [[potentialpvo_viewall|PotentialPVO_Viewall]] (HCM · BICC: 3/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RtgLvlPotBusinessGroupId | — |
| CAREER_STR_DEV | RtgLvlPotCareerStrDev | — |
| DATE_FROM | RtgLvlPotDateFrom | — |
| DATE_TO | RtgLvlPotDateTo | — |
| FROM_POINTS | RtgLvlPotFromPoints | — |
| LAST_UPDATE_DATE | RatingLevelBPEOLastUpdateDate | ✅ |
| MAX_RATING_DISTRIBUTION | RtgLvlPotMaxRatingDistrib | — |
| MIN_RATING_DISTRIBUTION | RtgLvlPotMinRatingDistrib | — |
| NUMERIC_RATING | ItemDecimal1 | ✅ |
| NUMERIC_RATING | RtgLvlPotNumericRating | — |
| RATING_LEVEL_CODE | RtgLvlPotRatingLevelCode | ✅ |
| RATING_LEVEL_ID | RtgLvlPotRatingLevelId | — |
| REVIEW_POINTS | RtgLvlPotReviewPoints | — |
| STAR_RATING | RtgLvlPotStarRating | — |
| TO_POINTS | RtgLvlPotToPoints | — |

### [[potentialratinglevelpvo|PotentialRatingLevelPVO]] (HCM · BICC: 4/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | ✅ |
| CAREER_STR_DEV | CareerStrDev | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | FromPoints | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | — |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | NumericRating | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | — |
| REVIEW_POINTS | ReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | ToPoints | — |

### [[proficiencyitemratingpvo|ProficiencyItemRatingPVO]] (HCM · BICC: 3/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | — |
| CAREER_STR_DEV | RatingLevelBPEOCareerStrDev | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | RatingLevelBPEOFromPoints | — |
| LAST_UPDATE_DATE | RatingLevelBPEOLastUpdateDate | ✅ |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | — |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | RatingLevelBPEONumericRating | ✅ |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | — |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | — |
| REVIEW_POINTS | RatingLevelBPEOReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | RatingLevelBPEOToPoints | — |

### [[ratinglevelfirstlangpvo|RatingLevelFirstLangPVO]] (HCM · BICC: 5/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | ✅ |
| CAREER_STR_DEV | RatingLevelBPEOCareerStrDev | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | RatingLevelBPEOFromPoints | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | — |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | RatingLevelBPEONumericRating | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | — |
| REVIEW_POINTS | RatingLevelBPEOReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | RatingLevelBPEOToPoints | — |

### [[ratinglevelfirstpvo|RatingLevelFirstPVO]] (HCM · BICC: 20/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | ✅ |
| CAREER_STR_DEV | RatingLevelBPEOCareerStrDev | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_FROM | RatingLevelBPEODateFrom | ✅ |
| DATE_TO | RatingLevelBPEODateTo | ✅ |
| FROM_POINTS | RatingLevelBPEOFromPoints | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | ✅ |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | ✅ |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | RatingLevelBPEONumericRating | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | ✅ |
| REVIEW_POINTS | RatingLevelBPEOReviewPoints | ✅ |
| STAR_RATING | RatingLevelBPEOStarRating | ✅ |
| TO_POINTS | RatingLevelBPEOToPoints | ✅ |

### [[ratinglevelinterestpvo|RatingLevelInterestPVO]] (HCM · BICC: 4/87)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | RatingLevelBPEOAttribute1 | — |
| ATTRIBUTE10 | RatingLevelBPEOAttribute10 | — |
| ATTRIBUTE11 | RatingLevelBPEOAttribute11 | — |
| ATTRIBUTE12 | RatingLevelBPEOAttribute12 | — |
| ATTRIBUTE13 | RatingLevelBPEOAttribute13 | — |
| ATTRIBUTE14 | RatingLevelBPEOAttribute14 | — |
| ATTRIBUTE15 | RatingLevelBPEOAttribute15 | — |
| ATTRIBUTE16 | RatingLevelBPEOAttribute16 | — |
| ATTRIBUTE17 | RatingLevelBPEOAttribute17 | — |
| ATTRIBUTE18 | RatingLevelBPEOAttribute18 | — |
| ATTRIBUTE19 | RatingLevelBPEOAttribute19 | — |
| ATTRIBUTE2 | RatingLevelBPEOAttribute2 | — |
| ATTRIBUTE20 | RatingLevelBPEOAttribute20 | — |
| ATTRIBUTE21 | RatingLevelBPEOAttribute21 | — |
| ATTRIBUTE22 | RatingLevelBPEOAttribute22 | — |
| ATTRIBUTE23 | RatingLevelBPEOAttribute23 | — |
| ATTRIBUTE24 | RatingLevelBPEOAttribute24 | — |
| ATTRIBUTE25 | RatingLevelBPEOAttribute25 | — |
| ATTRIBUTE26 | RatingLevelBPEOAttribute26 | — |
| ATTRIBUTE27 | RatingLevelBPEOAttribute27 | — |
| ATTRIBUTE28 | RatingLevelBPEOAttribute28 | — |
| ATTRIBUTE29 | RatingLevelBPEOAttribute29 | — |
| ATTRIBUTE3 | RatingLevelBPEOAttribute3 | — |
| ATTRIBUTE30 | RatingLevelBPEOAttribute30 | — |
| ATTRIBUTE4 | RatingLevelBPEOAttribute4 | — |
| ATTRIBUTE5 | RatingLevelBPEOAttribute5 | — |
| ATTRIBUTE6 | RatingLevelBPEOAttribute6 | — |
| ATTRIBUTE7 | RatingLevelBPEOAttribute7 | — |
| ATTRIBUTE8 | RatingLevelBPEOAttribute8 | — |
| ATTRIBUTE9 | RatingLevelBPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | RatingLevelBPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | RatingLevelBPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | RatingLevelBPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | RatingLevelBPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | RatingLevelBPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | RatingLevelBPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | RatingLevelBPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | RatingLevelBPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | RatingLevelBPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | RatingLevelBPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | RatingLevelBPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | RatingLevelBPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | RatingLevelBPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | RatingLevelBPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | RatingLevelBPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | RatingLevelBPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | RatingLevelBPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | RatingLevelBPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | RatingLevelBPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | RatingLevelBPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | RatingLevelBPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | RatingLevelBPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | RatingLevelBPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | RatingLevelBPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | RatingLevelBPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | RatingLevelBPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | RatingLevelBPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | RatingLevelBPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | RatingLevelBPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | RatingLevelBPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | RatingLevelBPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | RatingLevelBPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | RatingLevelBPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | RatingLevelBPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | RatingLevelBPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | RatingLevelBPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | ✅ |
| CAREER_STR_DEV | RatingLevelBPEOCareerStrDev | — |
| CREATED_BY | RatingLevelBPEOCreatedBy | — |
| CREATION_DATE | RatingLevelBPEOCreationDate | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | RatingLevelBPEOFromPoints | — |
| LAST_UPDATE_DATE | RatingLevelBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RatingLevelBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RatingLevelBPEOLastUpdatedBy | — |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | — |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | RatingLevelBPEONumericRating | — |
| OBJECT_VERSION_NUMBER | RatingLevelBPEOObjectVersionNumber | — |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | — |
| REVIEW_POINTS | RatingLevelBPEOReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | RatingLevelBPEOToPoints | — |

### [[ratinglevelsecondpvo|RatingLevelSecondPVO]] (HCM · BICC: 21/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | ✅ |
| CAREER_STR_DEV | RatingLevelBPEOCareerStrDev | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_FROM | RatingLevelBPEODateFrom | ✅ |
| DATE_TO | RatingLevelBPEODateTo | ✅ |
| FROM_POINTS | RatingLevelBPEOFromPoints | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | ✅ |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | ✅ |
| MODULE_ID | RatingLevelBPEOModuleId | ✅ |
| NUMERIC_RATING | RatingLevelBPEONumericRating | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | ✅ |
| REVIEW_POINTS | RatingLevelBPEOReviewPoints | ✅ |
| STAR_RATING | RatingLevelBPEOStarRating | ✅ |
| TO_POINTS | RatingLevelBPEOToPoints | ✅ |

### [[ratinglevelthirdpvo|RatingLevelThirdPVO]] (HCM · BICC: 21/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | ✅ |
| CAREER_STR_DEV | RatingLevelBPEOCareerStrDev | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_FROM | RatingLevelBPEODateFrom | ✅ |
| DATE_TO | RatingLevelBPEODateTo | ✅ |
| FROM_POINTS | RatingLevelBPEOFromPoints | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | ✅ |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | ✅ |
| MODULE_ID | RatingLevelBPEOModuleId | ✅ |
| NUMERIC_RATING | RatingLevelBPEONumericRating | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | ✅ |
| REVIEW_POINTS | RatingLevelBPEOReviewPoints | ✅ |
| STAR_RATING | RatingLevelBPEOStarRating | ✅ |
| TO_POINTS | RatingLevelBPEOToPoints | ✅ |

### [[readingratinglevelpvo|ReadingRatingLevelPVO]] (HCM · BICC: 5/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | ✅ |
| CAREER_STR_DEV | CareerStrDev | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | FromPoints | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | — |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | NumericRating | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | ✅ |
| REVIEW_POINTS | ReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | ToPoints | — |

### [[riskpvo|RiskPVO]] (HCM · BICC: 4/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RLIMPACTBusinessGroupId | — |
| BUSINESS_GROUP_ID | RLRISKBusinessGroupId | — |
| CAREER_STR_DEV | RLIMPACTCareerStrDev | — |
| DATE_FROM | RLIMPACTDateFrom | — |
| DATE_FROM | RLRISKDateFrom | — |
| DATE_TO | RLIMPACTDateTo | — |
| DATE_TO | RLRISKDateTo | — |
| FROM_POINTS | RLIMPACTFromPoints | — |
| FROM_POINTS | RLRISKFromPoints | — |
| LAST_UPDATE_DATE | RatingLevelImpactBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RatingLevelRiskBPEOLastUpdateDate | ✅ |
| MAX_RATING_DISTRIBUTION | RLIMPACTMaxRatingDistrib | — |
| MAX_RATING_DISTRIBUTION | RLRISKMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RLIMPACTMinRatingDistrib | — |
| MIN_RATING_DISTRIBUTION | RLRISKMinRatingDistribution | — |
| NUMERIC_RATING | RLIMPACTNumericRating | — |
| RATING_LEVEL_CODE | RLIMPACTRatingLevelCode | ✅ |
| RATING_LEVEL_CODE | RLRISKRatingLevelCode | ✅ |
| RATING_LEVEL_ID | RLIMPACTRatingLevelId | — |
| RATING_LEVEL_ID | RLRISKRatingLevelId | — |
| RATING_MODEL_ID | RLRISKRatingModelId | — |
| REVIEW_POINTS | RLIMPACTReviewPoints | — |
| REVIEW_POINTS | RLRISKReviewPoints | — |
| STAR_RATING | RLIMPACTStarRating | — |
| STAR_RATING | RLRISKStarRating | — |
| TO_POINTS | RLIMPACTToPoints | — |
| TO_POINTS | RLRISKToPoints | — |

### [[riskpvo_viewall|RiskPVO_Viewall]] (HCM · BICC: 4/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RLIMPACTBusinessGroupId | — |
| BUSINESS_GROUP_ID | RLRISKBusinessGroupId | — |
| CAREER_STR_DEV | RLIMPACTCareerStrDev | — |
| DATE_FROM | RLIMPACTDateFrom | — |
| DATE_FROM | RLRISKDateFrom | — |
| DATE_TO | RLIMPACTDateTo | — |
| DATE_TO | RLRISKDateTo | — |
| FROM_POINTS | RLIMPACTFromPoints | — |
| FROM_POINTS | RLRISKFromPoints | — |
| LAST_UPDATE_DATE | RatingLevelImpactBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RatingLevelRiskBPEOLastUpdateDate | ✅ |
| MAX_RATING_DISTRIBUTION | RLIMPACTMaxRatingDistrib | — |
| MAX_RATING_DISTRIBUTION | RLRISKMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RLIMPACTMinRatingDistrib | — |
| MIN_RATING_DISTRIBUTION | RLRISKMinRatingDistribution | — |
| NUMERIC_RATING | RLIMPACTNumericRating | — |
| RATING_LEVEL_CODE | RLIMPACTRatingLevelCode | ✅ |
| RATING_LEVEL_CODE | RLRISKRatingLevelCode | ✅ |
| RATING_LEVEL_ID | RLIMPACTRatingLevelId | — |
| RATING_LEVEL_ID | RLRISKRatingLevelId | — |
| RATING_MODEL_ID | RLRISKRatingModelId | — |
| REVIEW_POINTS | RLIMPACTReviewPoints | — |
| REVIEW_POINTS | RLRISKReviewPoints | — |
| STAR_RATING | RLIMPACTStarRating | — |
| STAR_RATING | RLRISKStarRating | — |
| TO_POINTS | RLIMPACTToPoints | — |
| TO_POINTS | RLRISKToPoints | — |

### [[riskratinglevelpvo|RiskRatingLevelPVO]] (HCM · BICC: 4/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | ✅ |
| CAREER_STR_DEV | CareerStrDev | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | FromPoints | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | — |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | NumericRating | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | — |
| REVIEW_POINTS | ReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | ToPoints | — |

### [[speakingratinglevelpvo|SpeakingRatingLevelPVO]] (HCM · BICC: 5/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | ✅ |
| CAREER_STR_DEV | CareerStrDev | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | FromPoints | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | — |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | NumericRating | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | ✅ |
| REVIEW_POINTS | ReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | ToPoints | — |

### [[talentscoreboxlabellookuppvo|TalentScoreBoxLabelLookupPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId5 | — |
| NUMERIC_RATING | NumericRating | — |
| RATING_LEVEL_CODE | RatingLevelCode | — |
| RATING_LEVEL_ID | RatingLevelId2 | — |

### [[talentscorepvo|TalentScorePVO]] (HCM · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RtgLvlBusinessGroupId | — |
| CAREER_STR_DEV | RtgLvlCareerStrDev | — |
| DATE_FROM | RtgLvlDateFrom | — |
| DATE_TO | RtgLvlDateTo | — |
| NUMERIC_RATING | RatingLevelBPEONumericRatin | ✅ |
| RATING_LEVEL_CODE | RtgLvlRatingLevelCode | ✅ |
| RATING_LEVEL_ID | RtgLvlRatingLevelId | — |
| STAR_RATING | RtgLvlStarRating | — |
| TO_POINTS | RtgLvlToPoints | — |

### [[writingratinglevelpvo|WritingRatingLevelPVO]] (HCM · BICC: 5/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelBPEOBusinessGroupId | ✅ |
| CAREER_STR_DEV | CareerStrDev | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | RatingLevelBPEODateFrom | — |
| DATE_TO | RatingLevelBPEODateTo | — |
| FROM_POINTS | FromPoints | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MAX_RATING_DISTRIBUTION | RatingLevelBPEOMaxRatingDistribution | — |
| MIN_RATING_DISTRIBUTION | RatingLevelBPEOMinRatingDistribution | — |
| MODULE_ID | RatingLevelBPEOModuleId | — |
| NUMERIC_RATING | NumericRating | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_LEVEL_CODE | RatingLevelBPEORatingLevelCode | ✅ |
| RATING_LEVEL_ID | RatingLevelBPEORatingLevelId | ✅ |
| RATING_MODEL_ID | RatingLevelBPEORatingModelId | ✅ |
| REVIEW_POINTS | ReviewPoints | — |
| STAR_RATING | RatingLevelBPEOStarRating | — |
| TO_POINTS | ToPoints | — |
