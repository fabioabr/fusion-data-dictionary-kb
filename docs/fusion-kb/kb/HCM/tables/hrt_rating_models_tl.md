---
id: DOC-HCM-264
doc_type: system-doc
title: "HRT_RATING_MODELS_TL — Modelos de Rating — Traducoes"
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
  - rating-models
aliases:
  - HRT_RATING_MODELS_TL
  - hrt_rating_models_tl
  - hrt-rating-models-tl
  - rating-models-tl
  - modelos-rating-traducoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_RATING_MODELS_TL

## 📌 Visao Geral

Tabela de traducoes que armazena textos em multiplos idiomas para cada registro definido em [[hrt_rating_models_b]].

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
| 1 | RATING_MODEL_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do registro base | [[hrt_rating_models_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 4 | RATING_MODEL_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome/texto traduzido | — | 🟢 100% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_rating_models_b]] — via `RATING_MODEL_ID` (registro base do modelo de classificacao)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Texto traduzido no idioma do usuario
```sql
SELECT tl.RATING_MODEL_NAME, tl.DESCRIPTION
FROM   HRT_RATING_MODELS_TL tl
WHERE  tl.RATING_MODEL_ID = :p_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observacoes

- Sufixo `_TL` indica tabela de traducao — PK composta por (RATING_MODEL_ID, LANGUAGE).
- JOIN com [[hrt_rating_models_b]] para dados completos.

---

## 📚 Referencias

- [Oracle Docs — HRT_RATING_MODELS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtratingmodelstl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[competencypvo|CompetencyPVO]] (HCM · BICC: 7/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId4 | — |
| BUSINESS_GROUP_ID | BusinessGroupId8 | — |
| BUSINESS_GROUP_ID | RMdlTLPEOInterBusinessGroupId | — |
| LANGUAGE | Language1 | — |
| LANGUAGE | Language3 | — |
| LANGUAGE | RMdlTLBPEOProfLanguage1 | — |
| LAST_UPDATE_DATE | RMdlTLBPEOProfLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RMdlTLPEOInterLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RMdlTLPEOPerfLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RMdlTLBPEOProfRtgDescription | — |
| RATING_DESCRIPTION | RMdlTLPEOInterRtgDescription | — |
| RATING_DESCRIPTION | RMdlTLPEOPerfRtgDescription | — |
| RATING_MODEL_ID | RMdlTLBPEOProfRatingModelId2 | — |
| RATING_MODEL_ID | RMdlTLPEOInterRatingModelId | — |
| RATING_MODEL_ID | RMdlTLPEOPerfRatingModelId5 | — |
| RATING_NAME | RMdlTLBPEOProfRatingNameM | ✅ |
| RATING_NAME | RMdlTLBPEOProfRtgName | ✅ |
| RATING_NAME | RMdlTLPEOInterRatingName | — |
| RATING_NAME | RMdlTLPEOPerfRatingName1 | ✅ |
| RATING_NAME | RMdlTLPEOPerfRatingName1M | ✅ |
| SOURCE_LANG | RMdlTLPEOInterSourceLang | — |

### [[criticalityprofileitempvo|CriticalityProfileItemPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RMTLBusinessGroupId1 | — |
| LANGUAGE | RMTLLanguage | — |
| RATING_DESCRIPTION | RMTLRatingDescription | — |
| RATING_MODEL_ID | RMTLRatingModelId | — |
| RATING_NAME | RMTLRatingName | — |

### [[languagepvo|LanguagePVO]] (HCM · BICC: 6/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RMTLReadBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | RMTLSpeakBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | RMTLWriteBusinessGroupId3 | — |
| LANGUAGE | RMTLReadLanguage1 | — |
| LANGUAGE | RMTLSpeakLanguage1 | — |
| LANGUAGE | RMTLWriteLanguage1 | — |
| LAST_UPDATE_DATE | RtgMdlTLReadingLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgMdlTLSpeakingLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgMdlTLWritingLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RMTLReadRatingDescription | — |
| RATING_DESCRIPTION | RMTLSpeakRatingDescription | — |
| RATING_DESCRIPTION | RMTLWriteRatingDescription | — |
| RATING_MODEL_ID | RMTLReadRatingModelId | — |
| RATING_MODEL_ID | RMTLSpeakRatingModelId | — |
| RATING_MODEL_ID | RMTLWriteRatingModelId | — |
| RATING_NAME | RMTLReadRatingName | ✅ |
| RATING_NAME | RMTLSpeakRatingName | ✅ |
| RATING_NAME | RMTLWriteRatingName | ✅ |
| SOURCE_LANG | RMTLReadSourceLang | — |

### [[personprofileperformanceratingpvo|PersonProfilePerformanceRatingPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| LANGUAGE | Language2 | — |
| LAST_UPDATE_DATE | RtgMdlTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RatingDescription | — |
| RATING_MODEL_ID | RatingModelId | — |
| RATING_NAME | RatingName | — |

### [[potentialpvo|PotentialPVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RMTLPotBusinessGroupId | — |
| LANGUAGE | RMTLPotLanguage | — |
| LAST_UPDATE_DATE | RtgMdlTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RMTLPotRatingDescription | — |
| RATING_MODEL_ID | RMTLPotRatingModelId | — |
| RATING_NAME | RMdlTLPotRatingName | ✅ |

### [[potentialpvo_viewall|PotentialPVO_Viewall]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RMTLPotBusinessGroupId | — |
| LANGUAGE | RMTLPotLanguage | — |
| LAST_UPDATE_DATE | RtgMdlTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RMTLPotRatingDescription | — |
| RATING_MODEL_ID | RMTLPotRatingModelId | — |
| RATING_NAME | RMdlTLPotRatingName | ✅ |

### [[ratingmodelfirstlangpvo|RatingModelFirstLangPVO]] (HCM · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingModelTranslationPEOBusinessGroupId | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | RatingModelTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RatingModelTranslationPEORatingDescription | ✅ |
| RATING_MODEL_ID | RatingModelTranslationPEORatingModelId | — |
| RATING_NAME | RatingModelTranslationPEORatingName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[ratingmodelfirstlangtranslationpvo|RatingModelFirstLangTranslationPVO]] (HCM · BICC: 12/12)

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
| RATING_MODEL_ID | RatingModelId | ✅ |
| RATING_NAME | RatingName | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[ratingmodelfirstpvo|RatingModelFirstPVO]] (HCM · BICC: 4/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingModelTranslationPEOBusinessGroupId | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | RatingModelTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RatingModelTranslationPEORatingDescription | ✅ |
| RATING_MODEL_ID | RatingModelTranslationPEORatingModelId | — |
| RATING_NAME | RatingModelTranslationPEORatingName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[ratingmodelsecondpvo|RatingModelSecondPVO]] (HCM · BICC: 4/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingModelTranslationPEOBusinessGroupId | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | RatingModelTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RatingModelTranslationPEORatingDescription | ✅ |
| RATING_MODEL_ID | RatingModelTranslationPEORatingModelId | — |
| RATING_NAME | RatingModelTranslationPEORatingName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[ratingmodelthirdpvo|RatingModelThirdPVO]] (HCM · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingModelTranslationPEOBusinessGroupId | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | RatingModelTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RatingModelTranslationPEORatingDescription | — |
| RATING_MODEL_ID | RatingModelTranslationPEORatingModelId | — |
| RATING_NAME | RatingModelTranslationPEORatingName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[riskpvo|RiskPVO]] (HCM · BICC: 4/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RtgMdlRiskBusinessGroupId | — |
| BUSINESS_GROUP_ID | RtgMdlTLImpactBusinessGroupId | — |
| LANGUAGE | RtgMdlRiskLanguage | — |
| LANGUAGE | RtgMdlTLImpactLanguage | — |
| LAST_UPDATE_DATE | RtgMdlImpactTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgMdlRiskTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RtgMdlTLImpactRatingDescrip | — |
| RATING_MODEL_ID | RtgMdlRiskRatingModelId | — |
| RATING_MODEL_ID | RtgMdlTLImpactRatingModelId | — |
| RATING_NAME | RtgMdlTLImpactRatingName | ✅ |
| RATING_NAME | RtgMdlTLRiskRatingName | ✅ |

### [[riskpvo_viewall|RiskPVO_Viewall]] (HCM · BICC: 4/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RtgMdlRiskBusinessGroupId | — |
| BUSINESS_GROUP_ID | RtgMdlTLImpactBusinessGroupId | — |
| LANGUAGE | RtgMdlRiskLanguage | — |
| LANGUAGE | RtgMdlTLImpactLanguage | — |
| LAST_UPDATE_DATE | RtgMdlImpactTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgMdlRiskTranslationPEOLastUpdateDate | ✅ |
| RATING_DESCRIPTION | RtgMdlTLImpactRatingDescrip | — |
| RATING_MODEL_ID | RtgMdlRiskRatingModelId | — |
| RATING_MODEL_ID | RtgMdlTLImpactRatingModelId | — |
| RATING_NAME | RtgMdlTLImpactRatingName | ✅ |
| RATING_NAME | RtgMdlTLRiskRatingName | ✅ |

### [[talentscorepvo|TalentScorePVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RMTLBusinessGroupId | — |
| LANGUAGE | RMTLLanguage | — |
| RATING_DESCRIPTION | RMTLRatingDescription | ✅ |
| RATING_MODEL_ID | RMTLRatingModelId | — |
| RATING_NAME | RMTLRatingName | ✅ |
