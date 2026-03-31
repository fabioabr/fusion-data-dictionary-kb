---
id: DOC-HCM-235
doc_type: system-doc
title: "HRT_CONTENT_TYPES_B — Tipos de Conteudo de Perfil — Base"
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
  - content-types
  - configuracao
  - talent
aliases:
  - HRT_CONTENT_TYPES_B
  - hrt_content_types_b
  - hrt-content-types-b
  - content-types-base
  - tipos-conteudo-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_CONTENT_TYPES_B

## 📌 Visao Geral

Tabela base que define os **tipos de conteudo** disponiveis para perfis de talento — competencias, habilidades, certificacoes, idiomas, educacao, honrarias, membros de associacoes, etc.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Definir quais tipos de conteudo estao disponiveis no tenant.
- **Estruturacao:** Cada tipo define quais campos dos itens sao utilizados e como.
- **Matching de perfis:** Tipos determinam quais dimensoes sao comparaveis entre perfis.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTENT_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do tipo de conteudo | — | 🟢 100% |
| 2 | CONTENT_TYPE_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo unico do tipo (e.g., COMPETENCY, SKILL) | — | 🟢 100% |
| 3 | ITEM_TYPE | VARCHAR2(30) | NULL | Classificacao | Classificacao do tipo de item | — | 🟡 80% |
| 4 | SUBSCRIBER_CODE | VARCHAR2(30) | NULL | Classificacao | Codigo do modulo consumidor | — | 🟡 75% |
| 5 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio de vigencia | — | 🟢 95% |
| 6 | DATE_TO | DATE | NULL | Data | Data de fim de vigencia | — | 🟢 95% |
| 7 | RATING_MODEL_ID | NUMBER(18) | NULL | FK | Modelo de rating padrao para este tipo | [[hrt_rating_models_b]] | 🟡 80% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_rating_models_b]] — via `RATING_MODEL_ID` (modelo de rating padrao)

### Tabelas-filha (FK de saida)
- [[hrt_content_types_tl]] — via `CONTENT_TYPE_ID` (traducoes do tipo de conteudo)
- [[hrt_content_items_b]] — via `CONTENT_TYPE_ID` (itens deste tipo)
- [[hrt_profile_items]] — via `CONTENT_TYPE_ID` (itens de perfil deste tipo)

---

## 📎 Uso Tipico

### Tipos de conteudo ativos
```sql
SELECT ct.CONTENT_TYPE_ID, ct.CONTENT_TYPE_CODE,
       ct.DATE_FROM, ct.DATE_TO
FROM   HRT_CONTENT_TYPES_B ct
WHERE  SYSDATE BETWEEN ct.DATE_FROM AND NVL(ct.DATE_TO, SYSDATE);
```

---

## 🔒 Observacoes

- Sufixo `_B` indica tabela base — traducoes em [[hrt_content_types_tl]].
- Tipos padrao Oracle incluem: COMPETENCY, CERTIFICATION, DEGREE, LANGUAGE, MEMBERSHIP, HONOR, SKILL.
- Novos tipos podem ser configurados por implementacao.

---

## 📚 Referencias

- [Oracle Docs — HRT_CONTENT_TYPES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtcontenttypesb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[advancementreadinesspvo|AdvancementReadinessPVO]] (HCM · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | FreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |
| MODULE_ID | ModuleId | — |

### [[advancementreadinesspvo_viewall|AdvancementReadinessPVO_Viewall]] (HCM · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | FreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |
| MODULE_ID | ModuleId | — |

### [[calibratedoverallcompetenciespvo|CalibratedOverallCompetenciesPVO]] (HCM · BICC: 3/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTypeBPEO1BusinessGroupId | — |
| BUSINESS_GROUP_ID | CTypeBPEOBusinessGroupId | ✅ |
| CONTENT_TYPE_ID | CTypeBPEO1ContentTypeId | — |
| CONTENT_TYPE_ID | CTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | CTypeBPEO1ContextName | — |
| CONTEXT_NAME | CTypeBPEOContextName | — |
| CREATED_BY | CTypeBPEOCreatedBy | — |
| CREATION_DATE | CTypeBPEOCreationDate | — |
| FREE_FORM_FLAG | CTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | CTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CTypeBPEOLastUpdatedBy | — |
| MODULE_ID | CTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | CTypeBPEOObjectVersionNumber | — |

### [[calibratedoverallgoalpvo|CalibratedOverallGoalPVO]] (HCM · BICC: 3/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTypeBPEO1BusinessGroupId | — |
| BUSINESS_GROUP_ID | CTypeBPEOBusinessGroupId | ✅ |
| CONTENT_TYPE_ID | CTypeBPEO1ContentTypeId | — |
| CONTENT_TYPE_ID | CTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | CTypeBPEO1ContextName | — |
| CONTEXT_NAME | CTypeBPEOContextName | — |
| CREATED_BY | CTypeBPEOCreatedBy | — |
| CREATION_DATE | CTypeBPEOCreationDate | — |
| FREE_FORM_FLAG | CTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | CTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CTypeBPEOLastUpdatedBy | — |
| MODULE_ID | CTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | CTypeBPEOObjectVersionNumber | — |

### [[calibratedperformancepvo|CalibratedPerformancePVO]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | CTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | CTypeBPEOContextName | — |
| CREATED_BY | CTypeBPEOCreatedBy | — |
| CREATION_DATE | CTypeBPEOCreationDate | — |
| FREE_FORM_FLAG | CTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | CTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CTypeBPEOLastUpdatedBy | — |
| MODULE_ID | CTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | CTypeBPEOObjectVersionNumber | — |

### [[calibratedperformancepvo_viewall|CalibratedPerformancePVO_Viewall]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | CTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | CTypeBPEOContextName | — |
| CREATED_BY | CTypeBPEOCreatedBy | — |
| CREATION_DATE | CTypeBPEOCreationDate | — |
| FREE_FORM_FLAG | CTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | CTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CTypeBPEOLastUpdatedBy | — |
| MODULE_ID | CTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | CTypeBPEOObjectVersionNumber | — |

### [[calibratedpotentialpvo|CalibratedPotentialPVO]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | CTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | CTypeBPEOContextName | — |
| CREATED_BY | CTypeBPEOCreatedBy | — |
| CREATION_DATE | CTypeBPEOCreationDate | — |
| FREE_FORM_FLAG | CTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | CTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CTypeBPEOLastUpdatedBy | — |
| MODULE_ID | CTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | CTypeBPEOObjectVersionNumber | — |

### [[calibratedpotentialpvo_viewall|CalibratedPotentialPVO_Viewall]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | CTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | CTypeBPEOContextName | — |
| CREATED_BY | CTypeBPEOCreatedBy | — |
| CREATION_DATE | CTypeBPEOCreationDate | — |
| FREE_FORM_FLAG | CTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | CTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CTypeBPEOLastUpdatedBy | — |
| MODULE_ID | CTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | CTypeBPEOObjectVersionNumber | — |

### [[calibratedriskpvo|CalibratedRiskPVO]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | CTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | CTypeBPEOContextName | — |
| CREATED_BY | CTypeBPEOCreatedBy | — |
| CREATION_DATE | CTypeBPEOCreationDate | — |
| FREE_FORM_FLAG | CTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | CTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CTypeBPEOLastUpdatedBy | — |
| MODULE_ID | CTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | CTypeBPEOObjectVersionNumber | — |

### [[calibratedriskpvo_viewall|CalibratedRiskPVO_Viewall]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | CTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | CTypeBPEOContextName | — |
| CREATED_BY | CTypeBPEOCreatedBy | — |
| CREATION_DATE | CTypeBPEOCreationDate | — |
| FREE_FORM_FLAG | CTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | CTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CTypeBPEOLastUpdatedBy | — |
| MODULE_ID | CTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | CTypeBPEOObjectVersionNumber | — |

### [[calibratedtalentscorepvo|CalibratedTalentScorePVO]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | CTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | CTypeBPEOContextName | — |
| CREATED_BY | CTypeBPEOCreatedBy | — |
| CREATION_DATE | CTypeBPEOCreationDate | — |
| FREE_FORM_FLAG | CTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | CTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CTypeBPEOLastUpdatedBy | — |
| MODULE_ID | CTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | CTypeBPEOObjectVersionNumber | — |

### [[calibratedtalentscorepvo_viewall|CalibratedTalentScorePVO_Viewall]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | CTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | CTypeBPEOContextName | — |
| CREATED_BY | CTypeBPEOCreatedBy | — |
| CREATION_DATE | CTypeBPEOCreationDate | — |
| FREE_FORM_FLAG | CTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | CTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CTypeBPEOLastUpdatedBy | — |
| MODULE_ID | CTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | CTypeBPEOObjectVersionNumber | — |

### [[careerpreferencepvo|CareerPreferencePVO]] (HCM · BICC: 3/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | ✅ |
| CONTENT_TYPE_ID | CTTLContentTypeId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | CTTLContextName | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | FreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[certificationcontentitempvo|CertificationContentItemPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTEXT_NAME | ContextName | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[certificationpvo|CertificationPVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CT_BusinessGroupId1 | — |
| CONTENT_TYPE_ID | CT_ContentTypeId | — |
| CONTEXT_NAME | CT_ContextName | — |
| FREE_FORM_FLAG | CT_FreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[competencycontentitempvo|CompetencyContentItemPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTEXT_NAME | ContextName | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[competencycontentitemratingpvo|CompetencyContentItemRatingPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTEXT_NAME | ContextName | — |
| LAST_UPDATE_DATE | ContentTypeBPEOForProfileTpSLastUpdateDate | ✅ |

### [[competencypvo|CompetencyPVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroup | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId1 | — |
| CONTEXT_NAME | ContentTypeBPEOContextName1 | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[contenttypepvo|ContentTypePVO]] (HCM · BICC: 10/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | ✅ |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | ContentTypeBPEOContextName | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| FREE_FORM_FLAG | FreeFormFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |

### [[criticalityprofileitempvo|CriticalityProfileItemPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| CONTEXT_NAME | ContextName | — |
| FREE_FORM_FLAG | CTBPEOFreeFormFlag | — |
| FREE_FORM_FLAG | ContentTypeBPEOFreeFormFlag | — |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[customcontentprofilepvo|CustomContentProfilePVO]] (HCM · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| CONTEXT_NAME | ContextName | — |
| FREE_FORM_FLAG | CTBPEOFreeFormFlag | — |
| FREE_FORM_FLAG | ContentTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[customcontentprofilepvo_viewall|CustomContentProfilePVO_Viewall]] (HCM · BICC: 3/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | ✅ |
| CONTEXT_NAME | ContextName | — |
| FREE_FORM_FLAG | CTBPEOFreeFormFlag | — |
| FREE_FORM_FLAG | ContentTypeBPEOFreeFormFlag | ✅ |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[degreecontentitempvo|DegreeContentItemPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTEXT_NAME | ContextName | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[degreepvo|DegreePVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId4 | — |
| CONTENT_TYPE_ID | ContentTypeId1 | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[genericprofilepvo|GenericProfilePVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| CONTEXT_NAME | ContextName | — |
| FREE_FORM_FLAG | CTBPEOFreeFormFlag | — |
| FREE_FORM_FLAG | ContentTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | — |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[honorcontentitempvo|HonorContentItemPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTEXT_NAME | ContextName | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[honorpvo|HonorPVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTBusinessGroupId | — |
| CONTENT_TYPE_ID | CTContentTypeId | ✅ |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTEXT_NAME | CTContextName1 | — |
| FREE_FORM_FLAG | CTFreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[impactratinglevelpvo|ImpactRatingLevelPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTEXT_NAME | ContextName | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[languagecontentitempvo|LanguageContentItemPVO]] (HCM · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | ✅ |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | FreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[languagepvo|LanguagePVO]] (HCM · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | ✅ |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTENT_TYPE_ID | ContentTypeId | ✅ |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| CONTEXT_NAME | ContextName | — |
| FREE_FORM_FLAG | FreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[membershipcontentitempvo|MembershipContentItemPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTEXT_NAME | ContextName | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[membershippvo|MembershipPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTBusinessGroupId1 | — |
| CONTENT_TYPE_ID | CTContentTypeId | — |
| CONTEXT_NAME | CTContextName1 | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[modelprofileitempvo|ModelProfileItemPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | CTBPEOContentTypeId | — |
| CONTEXT_NAME | CTBPEOContextName | — |
| FREE_FORM_FLAG | CTBPEOFreeFormFlag | — |

### [[nboxdimensionpvo|NBoxDimensionPVO]] (HCM · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | ✅ |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| CREATED_BY | ContentTypeBPEOCreatedBy | — |
| CREATION_DATE | ContentTypeBPEOCreationDate | — |
| FREE_FORM_FLAG | ContentTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ContentTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ContentTypeBPEOLastUpdatedBy | — |
| MODULE_ID | ContentTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | ContentTypeBPEOObjectVersionNumber | — |

### [[performancepotentialboxsequencepvo|PerformancePotentialBoxSequencePVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | ContentTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[performancepotentialboxsequencepvo_viewall|PerformancePotentialBoxSequencePVO_Viewall]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | ContentTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[personprofileitempvo|PersonProfileItemPVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | CTBPEOContentTypeId | — |
| CONTEXT_NAME | CTBPEOContextName | — |
| FREE_FORM_FLAG | CTBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[personprofileperformanceratingpvo|PersonProfilePerformanceRatingPVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | ContentTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[planreadinesspvo|PlanReadinessPVO]] (HCM · BICC: 5/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | ✅ |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | ✅ |
| FREE_FORM_FLAG | FreeFormFlag | ✅ |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | — |
| MODULE_ID | ContentTypeBPEOModuleId | — |
| MODULE_ID | ModuleId | ✅ |

### [[potentialpvo|PotentialPVO]] (HCM · BICC: 6/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTBusinessGroupId | — |
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | ✅ |
| CONTENT_TYPE_ID | CTContentTypeId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | CTContextName | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | ✅ |
| FREE_FORM_FLAG | FreeFormFlag | ✅ |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | ✅ |

### [[potentialpvo_viewall|PotentialPVO_Viewall]] (HCM · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTBusinessGroupId | — |
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | CTContentTypeId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | CTContextName | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | FreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[potentialratinglevelpvo|PotentialRatingLevelPVO]] (HCM · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | ✅ |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | FreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[previousemploymentprofilepvo|PreviousEmploymentProfilePVO]] (HCM · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | — |
| CONTEXT_NAME | CTBPContentTypeContextName | ✅ |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | ContentTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[previousemploymentpvo|PreviousEmploymentPVO]] (HCM · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| CONTEXT_NAME | ContextName | — |
| FREE_FORM_FLAG | CTBPEOFreeFormFlag | — |
| FREE_FORM_FLAG | ContentTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[readingratinglevelpvo|ReadingRatingLevelPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | FreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[riskpvo|RiskPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[riskpvo_viewall|RiskPVO_Viewall]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[riskratinglevelpvo|RiskRatingLevelPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTEXT_NAME | ContextName | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |

### [[speakingratinglevelpvo|SpeakingRatingLevelPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | FreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[specialprojectpvo|SpecialProjectPVO]] (HCM · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | CTContentTypeId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | CTContextName1 | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | CTFreeFormFlag | — |
| FREE_FORM_FLAG | ContentTypeBPEOFreeFormFlag | — |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[talentscoreboxsequencepvo|TalentScoreBoxSequencePVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | ContentTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | — |

### [[talentscoreboxsequencepvo_viewall|TalentScoreBoxSequencePVO_Viewall]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | ✅ |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | ContentTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | — |

### [[talentscorepvo|TalentScorePVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTBusinessGroupId | — |
| BUSINESS_GROUP_ID | CtBusinessGroupId2 | ✅ |
| CONTENT_TYPE_ID | CtContentTypeId1 | ✅ |
| CONTEXT_NAME | CtContextName | — |
| CREATED_BY | CtCreatedBy2 | — |
| CREATION_DATE | CtCreationDate2 | — |
| FREE_FORM_FLAG | CTFreeFormFlag | — |
| LAST_UPDATE_DATE | CtLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | CtLastUpdateLogin2 | — |
| LAST_UPDATED_BY | CtLastUpdatedBy2 | — |
| MODULE_ID | CtModuleId | — |
| OBJECT_VERSION_NUMBER | CtObjectVersionNumber2 | — |

### [[technicalpostpvo|TechnicalPostPVO]] (HCM · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| CONTEXT_NAME | ContextName | — |
| FREE_FORM_FLAG | CTBPEOFreeFormFlag | — |
| FREE_FORM_FLAG | ContentTypeBPEOFreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |

### [[workrequirementdatecheckpvo|WorkRequirementDateCheckPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTEXT_NAME | CTContextName | — |
| CONTEXT_NAME | ContextName | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | — |

### [[workrequirementpvo|WorkRequirementPVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTEXT_NAME | CTContextName | — |
| CONTEXT_NAME | ContextName | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[writingratinglevelpvo|WritingRatingLevelPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeBPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ContentTypeBPEOContentTypeId | — |
| CONTEXT_NAME | ContentTypeBPEOContextName | — |
| FREE_FORM_FLAG | FreeFormFlag | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ContentTypeBPEOModuleId | — |
