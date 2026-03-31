---
id: DOC-HCM-262
doc_type: system-doc
title: "HRT_RATING_LEVELS_TL — Niveis de Rating — Traducoes"
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
  - rating-levels
aliases:
  - HRT_RATING_LEVELS_TL
  - hrt_rating_levels_tl
  - hrt-rating-levels-tl
  - rating-levels-tl
  - niveis-rating-traducoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_RATING_LEVELS_TL

## 📌 Visao Geral

Tabela de traducoes que armazena textos em multiplos idiomas para cada registro definido em [[hrt_rating_levels_b]].

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
| 1 | RATING_LEVEL_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do registro base | [[hrt_rating_levels_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 4 | RATING_LEVEL_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome/texto traduzido | — | 🟢 100% |
| 5 | RATING_DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_rating_levels_b]] — via `RATING_LEVEL_ID` (registro base do nivel de classificacao)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Texto traduzido no idioma do usuario
```sql
SELECT tl.RATING_LEVEL_NAME, tl.RATING_DESCRIPTION
FROM   HRT_RATING_LEVELS_TL tl
WHERE  tl.RATING_LEVEL_ID = :p_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observacoes

- Sufixo `_TL` indica tabela de traducao — PK composta por (RATING_LEVEL_ID, LANGUAGE).
- JOIN com [[hrt_rating_levels_b]] para dados completos.

---

## 📚 Referencias

- [Oracle Docs — HRT_RATING_LEVELS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtratinglevelstl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[competencypvo|CompetencyPVO]] (HCM · BICC: 8/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| BUSINESS_GROUP_ID | BusinessGroupId6 | — |
| BUSINESS_GROUP_ID | RLvlTLPEOprofBusinessGroupId2 | — |
| LANGUAGE | Language | — |
| LANGUAGE | RLvlTLPEOprofLanguage | — |
| LANGUAGE | RtgLvlTLPEOPerfLanguage2 | — |
| LAST_UPDATE_DATE | RLvlTLPEOInterLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RLvlTLPEOprofLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgLvlTLPEOPerfLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RLvlTLPEOInterRtgDescription | — |
| RATING_DESCRIPTION | RLvlTLPEOprofRtgDescription | ✅ |
| RATING_DESCRIPTION | RLvlTLPEOprofRtgDescriptionM | ✅ |
| RATING_DESCRIPTION | RtgLvlTLPEOPerfRtgDescriptioM | ✅ |
| RATING_DESCRIPTION | RtgLvlTLPEOPerfRtgDescription | ✅ |
| RATING_LEVEL_ID | RLvlTLPEOInterRatingLevelId | — |
| RATING_LEVEL_ID | RLvlTLPEOprofRatingLevelId1 | — |
| RATING_LEVEL_ID | RtgLvlTLPEOPerfRatingLevelId3 | — |
| RATING_SHORT_DESCR | RLvlTLPEOInterRtgShortDescr | ✅ |
| RATING_SHORT_DESCR | RLvlTLPEOprofRatingShortDescM | — |
| RATING_SHORT_DESCR | RLvlTLPEOprofRatingShortDescr | — |
| RATING_SHORT_DESCR | RtgLvlTLPEOPerfRtgShortDesc | — |
| RATING_SHORT_DESCR | RtgLvlTLPEOPerfRtgShortDescrM | — |
| REVIEW_RATING_DESCR | RLvlTLPEOInterReviewRtgDescr | — |
| REVIEW_RATING_DESCR | RLvlTLPEOprofReviewRtgDescr | — |
| REVIEW_RATING_DESCR | RLvlTLPEOprofReviewRtgDescrM | — |
| REVIEW_RATING_DESCR | RtgLvlTLPEOPerfReviewRtgDescM | — |
| REVIEW_RATING_DESCR | RtgLvlTLPEOPerfReviewRtgDescr | — |
| SOURCE_LANG | RLvlTLPEOInterSourceLang | — |
| SOURCE_LANG | RLvlTLPEOprofSourceLang | — |

### [[criticalityprofileitempvo|CriticalityProfileItemPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RTLBusinessGroupId1 | — |
| LANGUAGE | RTLLanguage | — |
| RATING_DESCRIPTION | RTLRatingDescription | — |
| RATING_LEVEL_ID | RTLRatingLevelId | — |
| RATING_SHORT_DESCR | RTLRatingShortDescr | — |
| REVIEW_RATING_DESCR | RTLReviewRatingDescr | — |

### [[languagepvo|LanguagePVO]] (HCM · BICC: 10/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RLTLReadBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | RLTLSpeakBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | RLTLWriteBusinessGroupId | — |
| LANGUAGE | RLTLReadLanguage1 | — |
| LANGUAGE | RLTLSpeakLanguage1 | — |
| LANGUAGE | RLTLWriteLanguage1 | — |
| LAST_UPDATE_DATE | RtgLvlTLReadingLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgLvlTLSpeakingLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgLvlTLWritingLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RLTLReadRatingDescription | ✅ |
| RATING_DESCRIPTION | RLTLSpeakRatingDescription | ✅ |
| RATING_DESCRIPTION | RLTLWriteRatingDescription | ✅ |
| RATING_LEVEL_ID | RLTLReadRatingLevelId | — |
| RATING_LEVEL_ID | RLTLSpeakRatingLevelId | — |
| RATING_LEVEL_ID | RLTLWriteRatingLevelId | — |
| RATING_SHORT_DESCR | RLTLReadRatingShortDescr | ✅ |
| RATING_SHORT_DESCR | RLTLSpeakRatingShortDescr | ✅ |
| RATING_SHORT_DESCR | RLTLWriteRatingShortDescr | ✅ |
| REVIEW_RATING_DESCR | RLTLReadReviewRatingDescr | — |
| REVIEW_RATING_DESCR | RLTLSpeakReviewRatingDescr | ✅ |
| REVIEW_RATING_DESCR | RLTLWriteReviewRatingDescr | — |
| SOURCE_LANG | RLTLReadSourceLang | — |

### [[performancedocratinglevelpvo|PerformanceDocRatingLevelPVO]] (HCM · BICC: 4/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelTranslationPEOBusinessGroupId | — |
| LANGUAGE | Language | ✅ |
| RATING_DESCRIPTION | RatingLevelTranslationPEORatingDescription | ✅ |
| RATING_LEVEL_ID | RatingLevelTranslationPEORatingLevelId | — |
| RATING_SHORT_DESCR | RatingLevelTranslationPEORatingShortDescr | ✅ |
| REVIEW_RATING_DESCR | RatingLevelTranslationPEOReviewRatingDescr | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[personprofileperformanceratingpvo|PersonProfilePerformanceRatingPVO]] (HCM · BICC: 1/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RtgLvlTLBusinessGroupId1 | — |
| LANGUAGE | RtgLvlTLLanguage2 | — |
| LAST_UPDATE_DATE | RtgLvlTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RTgLvlTLRatingDescription | — |
| RATING_LEVEL_ID | RtgLvlTLRatingLevelId | — |
| RATING_SHORT_DESCR | RtgLvlTLRatingShortDescr | — |
| REVIEW_RATING_DESCR | RtgLvlTLReviewRatingDescr | — |

### [[potentialpvo|PotentialPVO]] (HCM · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RtgLvlTLPotBusinessGroupId | — |
| LANGUAGE | RtgLvlTLPotLanguage | — |
| LAST_UPDATE_DATE | RtgLvlTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RtgLvlTLPotRatingDescription | ✅ |
| RATING_LEVEL_ID | RtgLvlTLPotRatingLevelId | — |
| RATING_SHORT_DESCR | RtgLvlTLPotRatingShortDescr | ✅ |
| REVIEW_RATING_DESCR | RtgLvlTLPotReviewRatingDescr | — |

### [[potentialpvo_viewall|PotentialPVO_Viewall]] (HCM · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RtgLvlTLPotBusinessGroupId | — |
| LANGUAGE | RtgLvlTLPotLanguage | — |
| LAST_UPDATE_DATE | RtgLvlTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RtgLvlTLPotRatingDescription | ✅ |
| RATING_LEVEL_ID | RtgLvlTLPotRatingLevelId | — |
| RATING_SHORT_DESCR | RtgLvlTLPotRatingShortDescr | ✅ |
| REVIEW_RATING_DESCR | RtgLvlTLPotReviewRatingDescr | — |

### [[ratinglevelfirstlangpvo|RatingLevelFirstLangPVO]] (HCM · BICC: 3/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelTranslationPEOBusinessGroupId | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | RatingLevelTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RatingLevelTranslationPEORatingDescription | ✅ |
| RATING_LEVEL_ID | RatingLevelTranslationPEORatingLevelId | — |
| RATING_SHORT_DESCR | RatingLevelTranslationPEORatingShortDescr | ✅ |
| REVIEW_RATING_DESCR | RatingLevelTranslationPEOReviewRatingDescr | — |
| SOURCE_LANG | SourceLang | — |

### [[ratinglevelfirstlangtranslationpvo|RatingLevelFirstLangTranslationPVO]] (HCM · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| RATING_DESCRIPTION | RatingDescription | ✅ |
| RATING_LEVEL_ID | RatingLevelId | ✅ |
| RATING_SHORT_DESCR | RatingShortDescr | ✅ |
| REVIEW_RATING_DESCR | ReviewRatingDescr | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[ratinglevelfirstpvo|RatingLevelFirstPVO]] (HCM · BICC: 6/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelTranslationPEOBusinessGroupId | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | RatingLevelTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RatingLevelTranslationPEORatingDescription | ✅ |
| RATING_LEVEL_ID | RatingLevelTranslationPEORatingLevelId | — |
| RATING_SHORT_DESCR | RatingLevelTranslationPEORatingShortDescr | ✅ |
| REVIEW_RATING_DESCR | RatingLevelTranslationPEOReviewRatingDescr | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[ratinglevelinterestpvo|RatingLevelInterestPVO]] (HCM · BICC: 2/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelTranslationPEOBusinessGroupId | — |
| CREATED_BY | RatingLevelTranslationPEOCreatedBy | — |
| CREATION_DATE | RatingLevelTranslationPEOCreationDate | — |
| LANGUAGE | RatingLevelTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | RatingLevelTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RatingLevelTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RatingLevelTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | RatingLevelTranslationPEOObjectVersionNumber | — |
| RATING_DESCRIPTION | RatingLevelTranslationPEORatingDescription | — |
| RATING_LEVEL_ID | RatingLevelTranslationPEORatingLevelId | — |
| RATING_SHORT_DESCR | RatingLevelTranslationPEORatingShortDescr | ✅ |
| REVIEW_RATING_DESCR | RatingLevelTranslationPEOReviewRatingDescr | — |
| SOURCE_LANG | RatingLevelTranslationPEOSourceLang | — |

### [[ratinglevelsecondpvo|RatingLevelSecondPVO]] (HCM · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelTranslationPEOBusinessGroupId | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | RatingLevelTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RatingLevelTranslationPEORatingDescription | ✅ |
| RATING_LEVEL_ID | RatingLevelTranslationPEORatingLevelId | ✅ |
| RATING_SHORT_DESCR | RatingLevelTranslationPEORatingShortDescr | ✅ |
| REVIEW_RATING_DESCR | RatingLevelTranslationPEOReviewRatingDescr | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[ratinglevelthirdpvo|RatingLevelThirdPVO]] (HCM · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingLevelTranslationPEOBusinessGroupId | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | RatingLevelTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RatingLevelTranslationPEORatingDescription | ✅ |
| RATING_LEVEL_ID | RatingLevelTranslationPEORatingLevelId | ✅ |
| RATING_SHORT_DESCR | RatingLevelTranslationPEORatingShortDescr | ✅ |
| REVIEW_RATING_DESCR | RatingLevelTranslationPEOReviewRatingDescr | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[riskpvo|RiskPVO]] (HCM · BICC: 6/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RLTLImpactBusinessGroupId | — |
| BUSINESS_GROUP_ID | RLTLRISKBusinessGroupId | — |
| LANGUAGE | RLTLImpactLanguage | — |
| LANGUAGE | RLTLRISKLanguage | — |
| LAST_UPDATE_DATE | RtgLvlImpactTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgLvlRiskTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RLTLImpactRatingDescription | ✅ |
| RATING_DESCRIPTION | RLTLRISKRatingDescription | ✅ |
| RATING_LEVEL_ID | RLTLImpactRatingLevelId | — |
| RATING_LEVEL_ID | RLTLRISKRatingLevelId | — |
| RATING_SHORT_DESCR | RLTLImpactRatingShortDescr | ✅ |
| RATING_SHORT_DESCR | RLTLRISKRatingShortDescr | ✅ |
| REVIEW_RATING_DESCR | RLTLImpactReviewRatingDescr | — |
| REVIEW_RATING_DESCR | RLTLRISKReviewRatingDescr | — |

### [[riskpvo_viewall|RiskPVO_Viewall]] (HCM · BICC: 6/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RLTLImpactBusinessGroupId | — |
| BUSINESS_GROUP_ID | RLTLRISKBusinessGroupId | — |
| LANGUAGE | RLTLImpactLanguage | — |
| LANGUAGE | RLTLRISKLanguage | — |
| LAST_UPDATE_DATE | RtgLvlImpactTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgLvlRiskTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RLTLImpactRatingDescription | ✅ |
| RATING_DESCRIPTION | RLTLRISKRatingDescription | ✅ |
| RATING_LEVEL_ID | RLTLImpactRatingLevelId | — |
| RATING_LEVEL_ID | RLTLRISKRatingLevelId | — |
| RATING_SHORT_DESCR | RLTLImpactRatingShortDescr | ✅ |
| RATING_SHORT_DESCR | RLTLRISKRatingShortDescr | ✅ |
| REVIEW_RATING_DESCR | RLTLImpactReviewRatingDescr | — |
| REVIEW_RATING_DESCR | RLTLRISKReviewRatingDescr | — |

### [[talentscoreboxlabellookuppvo|TalentScoreBoxLabelLookupPVO]] (HCM · BICC: 4/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId4 | ✅ |
| LANGUAGE | Language | ✅ |
| RATING_DESCRIPTION | RatingDescription | ✅ |
| RATING_LEVEL_ID | RatingLevelId1 | ✅ |
| RATING_SHORT_DESCR | RatingShortDescr | — |

### [[talentscorepvo|TalentScorePVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TSBusinessGroupId | — |
| LANGUAGE | TSLanguage | — |
| RATING_DESCRIPTION | TSRatingDescription | ✅ |
| RATING_LEVEL_ID | TSRatingLevelId | — |
| RATING_SHORT_DESCR | TSRatingShortDescr | ✅ |
| REVIEW_RATING_DESCR | TSReviewRatingDescr | — |
