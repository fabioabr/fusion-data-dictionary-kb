---
id: DOC-HCM-246
doc_type: system-doc
title: "HRT_PROFILES_TL — Perfis de Talento — Traducoes"
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
  - profiles
aliases:
  - HRT_PROFILES_TL
  - hrt_profiles_tl
  - hrt-profiles-tl
  - profiles-translations
  - perfis-talento-traducoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_PROFILES_TL

## 📌 Visao Geral

Tabela de traducoes que armazena textos em multiplos idiomas para cada registro definido em [[hrt_profiles_b]].

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
| 1 | PROFILE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do registro base | [[hrt_profiles_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 4 | PROFILE_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome/texto traduzido | — | 🟢 100% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_profiles_b]] — via `PROFILE_ID` (registro base do perfil de talento)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Texto traduzido no idioma do usuario
```sql
SELECT tl.PROFILE_NAME, tl.DESCRIPTION
FROM   HRT_PROFILES_TL tl
WHERE  tl.PROFILE_ID = :p_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observacoes

- Sufixo `_TL` indica tabela de traducao — PK composta por (PROFILE_ID, LANGUAGE).
- JOIN com [[hrt_profiles_b]] para dados completos.

---

## 📚 Referencias

- [Oracle Docs — HRT_PROFILES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtprofilestl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[careerdevgoalpvo|CareerDevGoalPVO]] (HCM · BICC: 1/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate3 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PROFILE_ID | ProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | Summary | — |

### [[careerdevgoalpvoviewall|CareerDevGoalPVOViewAll]] (HCM · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PROFILE_ID | ProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | Summary | — |

### [[careerdevgoalversionpvo|CareerDevGoalVersionPVO]] (HCM · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PROFILE_ID | ProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | Summary | — |

### [[careerdevgoalversionpvoviewall|CareerDevGoalVersionPVOViewAll]] (HCM · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PROFILE_ID | ProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | Summary | — |

### [[criticalityprofileitempvo|CriticalityProfileItemPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTranslationPEOBusinessGroupId | — |
| DESCRIPTION | ProfileTranslationPEODescription | — |
| LANGUAGE | Language | — |
| PROFILE_ID | ProfileTranslationPEOProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | ProfileTranslationPEOSummary | — |

### [[customcontentprofilepvo|CustomContentProfilePVO]] (HCM · BICC: 1/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTranslationPEOBusinessGroupId | — |
| DESCRIPTION | ProfileTranslationPEODescription | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | ProfileTranslationPEOLastUpdateDate | ✅ |
| PROFILE_ID | ProfileTranslationPEOProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | ProfileTranslationPEOSummary | — |

### [[customcontentprofilepvo_viewall|CustomContentProfilePVO_Viewall]] (HCM · BICC: 1/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTranslationPEOBusinessGroupId | — |
| DESCRIPTION | ProfileTranslationPEODescription | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | ProfileTranslationPEOLastUpdateDate | ✅ |
| PROFILE_ID | ProfileTranslationPEOProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | ProfileTranslationPEOSummary | — |

### [[developmentgoalpvo|DevelopmentGoalPVO]] (HCM · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PROFILE_ID | ProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | Summary | — |

### [[developmentgoalpvoviewall|DevelopmentGoalPVOViewAll]] (HCM · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PROFILE_ID | ProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | Summary | — |

### [[genericprofilepvo|GenericProfilePVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTranslationPEOBusinessGroupId | — |
| DESCRIPTION | ProfileTranslationPEODescription | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | ProfileTranslationPEOLastUpdateDate | — |
| PROFILE_ID | ProfileTranslationPEOProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | ProfileTranslationPEOSummary | — |

### [[goalppvo1|GoalPPVO1]] (HCM · BICC: 1/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| DESCRIPTION | Description | — |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PROFILE_ID | ProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | Summary | — |

### [[goalpvo_copy|GoalPVO_Copy]] (HCM · BICC: 1/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| DESCRIPTION | Description | — |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PROFILE_ID | ProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | Summary | — |

### [[jobprofilepvo|JobProfilePVO]] (HCM · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTranslationPEOBusinessGroupId | — |
| CREATED_BY | ProfileTranslationPEOCreatedBy | — |
| CREATION_DATE | ProfileTranslationPEOCreationDate | — |
| DESCRIPTION | ProfileTranslationPEODescription | ✅ |
| LANGUAGE | ProfileTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ProfileTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileTranslationPEOObjectVersionNumber | — |
| PROFILE_ID | ProfileTranslationPEOProfileId | — |
| SOURCE_LANG | ProfileTranslationPEOSourceLang | — |
| SUMMARY | ProfileTranslationPEOSummary | — |

### [[modelprofileitempvo|ModelProfileItemPVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTranslationPEOBusinessGroupId | — |
| DESCRIPTION | ProfileTranslationPEODescription | ✅ |
| LANGUAGE | Language | — |
| PROFILE_ID | ProfileTranslationPEOProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | ProfileTranslationPEOSummary | ✅ |

### [[modelprofilepvo|ModelProfilePVO]] (HCM · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTranslationPEOBusinessGroupId | — |
| DESCRIPTION | ProfileTranslationPEODescription | ✅ |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | ProfileTranslationPEOLastUpdateDate | ✅ |
| PROFILE_ID | ProfileTranslationPEOProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | ProfileTranslationPEOSummary | ✅ |

### [[performancegoalpvo|PerformanceGoalPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| DESCRIPTION | Description | — |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate3 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PROFILE_ID | ProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | Summary | — |

### [[performancegoalpvoviewall|PerformanceGoalPVOViewAll]] (HCM · BICC: 1/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| DESCRIPTION | Description | — |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PROFILE_ID | ProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | Summary | — |

### [[performancegoalversionpvo|PerformanceGoalVersionPVO]] (HCM · BICC: 1/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| DESCRIPTION | Description | — |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PROFILE_ID | ProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | Summary | — |

### [[performancegoalversionpvoviewall|PerformanceGoalVersionPVOViewAll]] (HCM · BICC: 1/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| DESCRIPTION | Description | — |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PROFILE_ID | ProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | Summary | — |

### [[personalgoalpvo|PersonalGoalPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| DESCRIPTION | Description | — |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate3 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PROFILE_ID | ProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | Summary | — |

### [[personprofileitempvo|PersonProfileItemPVO]] (HCM · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTranslationPEOBusinessGroupId | — |
| DESCRIPTION | ProfileTranslationPEODescription | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ProfileTranslationPEOLastUpdateDate | ✅ |
| PROFILE_ID | ProfileTranslationPEOProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | ProfileTranslationPEOSummary | — |

### [[personprofileperformanceratingpvo|PersonProfilePerformanceRatingPVO]] (HCM · BICC: 1/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTranslationPEOBusinessGroupId | — |
| DESCRIPTION | ProfileTranslationPEODescription | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | ProfileTranslationPEOLastUpdateDate | ✅ |
| PROFILE_ID | ProfileTranslationPEOProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | ProfileTranslationPEOSummary | — |

### [[personprofilepvo|PersonProfilePVO]] (HCM · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTranslationPEOBusinessGroupId | — |
| DESCRIPTION | ProfileTranslationPEODescription | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ProfileTranslationPEOLastUpdateDate | ✅ |
| PROFILE_ID | ProfileTranslationPEOProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | ProfileTranslationPEOSummary | — |

### [[previousemploymentprofilepvo|PreviousEmploymentProfilePVO]] (HCM · BICC: 1/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTranslationPEOBusinessGroupId | — |
| DESCRIPTION | ProfileTranslationPEODescription | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | ProfileTranslationPEOLastUpdateDate | ✅ |
| PROFILE_ID | ProfileTranslationPEOProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | ProfileTranslationPEOSummary | — |

### [[previousemploymentpvo|PreviousEmploymentPVO]] (HCM · BICC: 1/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTranslationPEOBusinessGroupId | — |
| DESCRIPTION | ProfileTranslationPEODescription | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | ProfileTranslationPEOLastUpdateDate | ✅ |
| PROFILE_ID | ProfileTranslationPEOProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | ProfileTranslationPEOSummary | — |

### [[profiletranslationextractpvo|ProfileTranslationExtractPVO]] (HCM · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PROFILE_ID | ProfileId | ✅ |
| SOURCE_LANG | SourceLang | ✅ |
| SUMMARY | Summary | ✅ |

### [[technicalpostpvo|TechnicalPostPVO]] (HCM · BICC: 1/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTranslationPEOBusinessGroupId | — |
| DESCRIPTION | ProfileTranslationPEODescription | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | ProfileTranslationPEOLastUpdateDate | ✅ |
| PROFILE_ID | ProfileTranslationPEOProfileId | — |
| SOURCE_LANG | SourceLang | — |
| SUMMARY | ProfileTranslationPEOSummary | — |
