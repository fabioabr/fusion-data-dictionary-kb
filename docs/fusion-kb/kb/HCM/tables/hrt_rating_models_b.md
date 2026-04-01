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

---

## 🔗 PVOs Relacionados

### [[competencypvo|CompetencyPVO]] (HCM · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| BUSINESS_GROUP_ID | RMdlBPEOProfBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | RMdllBPEOPerfBusinessGroupId7 | — |
| DATE_FROM | RMdlBPEOProfDateFrom | — |
| DATE_TO | RMdlBPEOProfDateTo | — |
| LAST_UPDATE_DATE | RMdlBPEOInterestLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RMdlBPEOProfLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RMdllBPEOPerfLastUpdateDate | ✅ |
| RATING_MODEL_CODE | RMdlBPEOProfRatingModelCode | — |
| RATING_MODEL_CODE | RMdllBPEOPerfRatingModelCode | — |
| RATING_MODEL_ID | RMdlBPEOProfRatingModelId1 | — |
| RATING_MODEL_ID | RMdllBPEOPerfRatingModelId4 | — |
| RATING_MODEL_ID | RatingModelId | — |

### [[criticalityprofileitempvo|CriticalityProfileItemPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RMBusinessGroupId1 | — |
| DATE_FROM | RMDateFrom1 | — |
| DATE_TO | RMDateTo1 | — |
| DISTRIBUTION_THRESHOLD | RMDistributionThreshold | — |
| DISTRIBUTION_THRESHOLD | RMDistributionThreshold1 | — |
| RATING_MODEL_CODE | RMRatingModelCode | — |
| RATING_MODEL_ID | RMRatingModelId | — |

### [[languagepvo|LanguagePVO]] (HCM · BICC: 6/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RMReadBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | RMSpeakBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | RMWriteBusinessGroupId3 | — |
| DATE_FROM | RMReadDateFrom | — |
| DATE_FROM | RMSpeakDateFrom | — |
| DATE_FROM | RMWriteDateFrom | — |
| DATE_TO | RMReadDateTo | — |
| DATE_TO | RMWriteDateTo | — |
| LAST_UPDATE_DATE | RtgMdlReadingBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgMdlSpeakingLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgMdlWritingLastUpdateDate | ✅ |
| OBJECT_VERSION_NUMBER | RMReadObjectVersionNumber1 | — |
| RATING_MODEL_CODE | RMReadRatingModelCode | ✅ |
| RATING_MODEL_CODE | RMSpeakRatingModelCode | ✅ |
| RATING_MODEL_CODE | RMWriteRatingModelCode | ✅ |
| RATING_MODEL_ID | RMReadRatingModelId | — |
| RATING_MODEL_ID | RMSpeakRatingModelId | — |
| RATING_MODEL_ID | RMWriteRatingModelId | — |

### [[personprofileperformanceratingpvo|PersonProfilePerformanceRatingPVO]] (HCM · BICC: 1/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PerfRtgBusinessGroupId1 | — |
| DATE_FROM | PerfRtgDateFrom | — |
| DATE_TO | PerfRtgDateTo | — |
| LAST_UPDATE_DATE | RatingModelBPEOLastUpdateDate | ✅ |
| MODULE_ID | PerfRtgModuleId | — |
| RATING_MODEL_CODE | PerfRtgRatingModelCode | — |
| RATING_MODEL_ID | PerfRtgRatingModelId | — |

### [[potentialpvo|PotentialPVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RtgMdlBusinessGroupId | — |
| DATE_FROM | RtgMdlDateFrom | — |
| DATE_TO | RtgMdlDateTo | — |
| LAST_UPDATE_DATE | RatingModelBPEOLastUpdateDate | ✅ |
| RATING_MODEL_CODE | RtgMdlRatingModelCode | ✅ |
| RATING_MODEL_ID | RtgMdlRatingModelId | — |

### [[potentialpvo_viewall|PotentialPVO_Viewall]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RtgMdlBusinessGroupId | — |
| DATE_FROM | RtgMdlDateFrom | — |
| DATE_TO | RtgMdlDateTo | — |
| LAST_UPDATE_DATE | RatingModelBPEOLastUpdateDate | ✅ |
| RATING_MODEL_CODE | RtgMdlRatingModelCode | ✅ |
| RATING_MODEL_ID | RtgMdlRatingModelId | — |

### [[ratinglevelinterestpvo|RatingLevelInterestPVO]] (HCM · BICC: 3/79)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | RatingModelBPEOAttribute1 | — |
| ATTRIBUTE10 | RatingModelBPEOAttribute10 | — |
| ATTRIBUTE11 | RatingModelBPEOAttribute11 | — |
| ATTRIBUTE12 | RatingModelBPEOAttribute12 | — |
| ATTRIBUTE13 | RatingModelBPEOAttribute13 | — |
| ATTRIBUTE14 | RatingModelBPEOAttribute14 | — |
| ATTRIBUTE15 | RatingModelBPEOAttribute15 | — |
| ATTRIBUTE16 | RatingModelBPEOAttribute16 | — |
| ATTRIBUTE17 | RatingModelBPEOAttribute17 | — |
| ATTRIBUTE18 | RatingModelBPEOAttribute18 | — |
| ATTRIBUTE19 | RatingModelBPEOAttribute19 | — |
| ATTRIBUTE2 | RatingModelBPEOAttribute2 | — |
| ATTRIBUTE20 | RatingModelBPEOAttribute20 | — |
| ATTRIBUTE21 | RatingModelBPEOAttribute21 | — |
| ATTRIBUTE22 | RatingModelBPEOAttribute22 | — |
| ATTRIBUTE23 | RatingModelBPEOAttribute23 | — |
| ATTRIBUTE24 | RatingModelBPEOAttribute24 | — |
| ATTRIBUTE25 | RatingModelBPEOAttribute25 | — |
| ATTRIBUTE26 | RatingModelBPEOAttribute26 | — |
| ATTRIBUTE27 | RatingModelBPEOAttribute27 | — |
| ATTRIBUTE28 | RatingModelBPEOAttribute28 | — |
| ATTRIBUTE29 | RatingModelBPEOAttribute29 | — |
| ATTRIBUTE3 | RatingModelBPEOAttribute3 | — |
| ATTRIBUTE30 | RatingModelBPEOAttribute30 | — |
| ATTRIBUTE4 | RatingModelBPEOAttribute4 | — |
| ATTRIBUTE5 | RatingModelBPEOAttribute5 | — |
| ATTRIBUTE6 | RatingModelBPEOAttribute6 | — |
| ATTRIBUTE7 | RatingModelBPEOAttribute7 | — |
| ATTRIBUTE8 | RatingModelBPEOAttribute8 | — |
| ATTRIBUTE9 | RatingModelBPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | RatingModelBPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | RatingModelBPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | RatingModelBPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | RatingModelBPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | RatingModelBPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | RatingModelBPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | RatingModelBPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | RatingModelBPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | RatingModelBPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | RatingModelBPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | RatingModelBPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | RatingModelBPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | RatingModelBPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | RatingModelBPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | RatingModelBPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | RatingModelBPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | RatingModelBPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | RatingModelBPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | RatingModelBPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | RatingModelBPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | RatingModelBPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | RatingModelBPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | RatingModelBPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | RatingModelBPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | RatingModelBPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | RatingModelBPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | RatingModelBPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | RatingModelBPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | RatingModelBPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | RatingModelBPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | RatingModelBPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | RatingModelBPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | RatingModelBPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | RatingModelBPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | RatingModelBPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | RatingModelBPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | RatingModelBPEOBusinessGroupId | ✅ |
| CREATED_BY | RatingModelBPEOCreatedBy | — |
| CREATION_DATE | RatingModelBPEOCreationDate | — |
| DATE_FROM | RatingModelBPEODateFrom | — |
| DATE_TO | RatingModelBPEODateTo | — |
| DISTRIBUTION_THRESHOLD | RatingModelBPEODistributionThreshold | — |
| LAST_UPDATE_DATE | RatingModelBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RatingModelBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RatingModelBPEOLastUpdatedBy | — |
| MODULE_ID | RatingModelBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | RatingModelBPEOObjectVersionNumber | — |
| RATING_MODEL_CODE | RatingModelBPEORatingModelCode | — |
| RATING_MODEL_ID | RatingModelBPEORatingModelId | ✅ |

### [[ratingmodelfirstlangpvo|RatingModelFirstLangPVO]] (HCM · BICC: 4/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingModelBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | RatingModelBPEODateFrom | — |
| DATE_TO | RatingModelBPEODateTo | — |
| DISTRIBUTION_THRESHOLD | RatingModelBPEODistributionThreshold | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MODULE_ID | RatingModelBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_MODEL_CODE | RatingModelBPEORatingModelCode | ✅ |
| RATING_MODEL_ID | RatingModelBPEORatingModelId | ✅ |

### [[ratingmodelfirstpvo|RatingModelFirstPVO]] (HCM · BICC: 12/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingModelBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_FROM | RatingModelBPEODateFrom | ✅ |
| DATE_TO | RatingModelBPEODateTo | ✅ |
| DISTRIBUTION_THRESHOLD | RatingModelBPEODistributionThreshold | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MODULE_ID | RatingModelBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| RATING_MODEL_CODE | RatingModelBPEORatingModelCode | ✅ |
| RATING_MODEL_ID | RatingModelBPEORatingModelId | ✅ |

### [[ratingmodelsecondpvo|RatingModelSecondPVO]] (HCM · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingModelBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | RatingModelBPEODateFrom | — |
| DATE_TO | RatingModelBPEODateTo | — |
| DISTRIBUTION_THRESHOLD | RatingModelBPEODistributionThreshold | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MODULE_ID | RatingModelBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_MODEL_CODE | RatingModelBPEORatingModelCode | — |
| RATING_MODEL_ID | RatingModelBPEORatingModelId | ✅ |

### [[ratingmodelthirdpvo|RatingModelThirdPVO]] (HCM · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RatingModelBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | RatingModelBPEODateFrom | — |
| DATE_TO | RatingModelBPEODateTo | — |
| DISTRIBUTION_THRESHOLD | RatingModelBPEODistributionThreshold | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MODULE_ID | RatingModelBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_MODEL_CODE | RatingModelBPEORatingModelCode | — |
| RATING_MODEL_ID | RatingModelBPEORatingModelId | ✅ |

### [[riskpvo|RiskPVO]] (HCM · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RMdlImpactBusinessGroupId | — |
| BUSINESS_GROUP_ID | RiskRtgMdlBusinessGroupId | — |
| DATE_FROM | RMdlImpactDateFrom | — |
| DATE_FROM | RiskRtgMdlDateFrom | — |
| DATE_TO | RMdlImpactDateTo | — |
| DATE_TO | RiskRtgMdlDateTo | — |
| LAST_UPDATE_DATE | RtgMdlImpactBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgMdlRiskBPEOLastUpdateDate | ✅ |
| RATING_MODEL_CODE | RMdlImpactRatingModelCode | ✅ |
| RATING_MODEL_CODE | RMdlRiskRatingModelCode | ✅ |
| RATING_MODEL_ID | RMdlImpactRatingModelId | — |
| RATING_MODEL_ID | RiskRtgMdlRatingModelId | — |

### [[riskpvo_viewall|RiskPVO_Viewall]] (HCM · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RMdlImpactBusinessGroupId | — |
| BUSINESS_GROUP_ID | RiskRtgMdlBusinessGroupId | — |
| DATE_FROM | RMdlImpactDateFrom | — |
| DATE_FROM | RiskRtgMdlDateFrom | — |
| DATE_TO | RMdlImpactDateTo | — |
| DATE_TO | RiskRtgMdlDateTo | — |
| LAST_UPDATE_DATE | RtgMdlImpactBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RtgMdlRiskBPEOLastUpdateDate | ✅ |
| RATING_MODEL_CODE | RMdlImpactRatingModelCode | ✅ |
| RATING_MODEL_CODE | RMdlRiskRatingModelCode | ✅ |
| RATING_MODEL_ID | RMdlImpactRatingModelId | — |
| RATING_MODEL_ID | RiskRtgMdlRatingModelId | — |

### [[talentscorepvo|TalentScorePVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RMdlBusinessGroupId | — |
| DATE_FROM | RMdlDateFrom | — |
| DATE_TO | RMdlDateTo | — |
| MODULE_ID | RMdlModuleId | — |
| RATING_MODEL_CODE | RMdlRatingModelCode | ✅ |
| RATING_MODEL_ID | RMdlRatingModelId | — |
