---
id: DOC-HCM-236
doc_type: system-doc
title: "HRT_CONTENT_TYPES_TL — Tipos de Conteudo de Perfil — Traducoes"
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
  - content-types
aliases:
  - HRT_CONTENT_TYPES_TL
  - hrt_content_types_tl
  - hrt-content-types-tl
  - content-types-translations
  - tipos-conteudo-traducoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_CONTENT_TYPES_TL

## 📌 Visao Geral

Tabela de traducoes que armazena textos em multiplos idiomas para cada registro definido em [[hrt_content_types_b]].

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
| 1 | CONTENT_TYPE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do registro base | [[hrt_content_types_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 4 | CONTENT_TYPE_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome/texto traduzido | — | 🟢 100% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (registro base do tipo de conteudo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Texto traduzido no idioma do usuario
```sql
SELECT tl.CONTENT_TYPE_NAME, tl.DESCRIPTION
FROM   HRT_CONTENT_TYPES_TL tl
WHERE  tl.CONTENT_TYPE_ID = :p_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observacoes

- Sufixo `_TL` indica tabela de traducao — PK composta por (CONTENT_TYPE_ID, LANGUAGE).
- JOIN com [[hrt_content_types_b]] para dados completos.

---

## 📚 Referencias

- [Oracle Docs — HRT_CONTENT_TYPES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtcontenttypestl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[advancementreadinesspvo|AdvancementReadinessPVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTTLBusinessGroupId | — |
| CONTENT_TYPE_ID | CTTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTTLContentTypeName | — |
| LANGUAGE | CTTLLanguage | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[advancementreadinesspvo_viewall|AdvancementReadinessPVO_Viewall]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTTLBusinessGroupId | — |
| CONTENT_TYPE_ID | CTTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTTLContentTypeName | — |
| LANGUAGE | CTTLLanguage | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[careerpreferencepvo|CareerPreferencePVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTTLBusinessGroupId2 | — |
| CONTENT_DESCRIPTION | CTTLContentDescription | — |
| CONTENT_TYPE_ID | CTTLContentTypeId1 | — |
| CONTENT_TYPE_NAME | CTTLContentTypeName | ✅ |
| LANGUAGE | CTTLLanguage1 | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[certificationpvo|CertificationPVO]] (HCM · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CT_TL_BusinessGroupId1 | — |
| CONTENT_DESCRIPTION | CT_TL_ContentDescription | — |
| CONTENT_TYPE_ID | CT_TL_ContentTypeId | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTENT_TYPE_NAME | CT_TL_ContentTypeName | ✅ |
| LANGUAGE | CT_TL_Language1 | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[competencypvo|CompetencyPVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CntTypeTLPEOBusinessGroupId3 | — |
| CONTENT_DESCRIPTION | CntTypeTLPEOContentDescrip | — |
| CONTENT_TYPE_ID | CntTypeTLPEOContentTypeId2 | — |
| CONTENT_TYPE_NAME | CntTypeTLPEOContentTypeName | ✅ |
| LANGUAGE | CntTypeTLPEOLanguage2 | — |
| LAST_UPDATE_DATE | CntTypeTLPEOLastUpdateDate | ✅ |

### [[contenttypepvo|ContentTypePVO]] (HCM · BICC: 6/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentTypeTranslationPEOBusinessGroupId | — |
| CONTENT_DESCRIPTION | ContentTypeTranslationPEOContentDescription | ✅ |
| CONTENT_TYPE_ID | ContentTypeTranslationPEOContentTypeId | ✅ |
| CONTENT_TYPE_NAME | ContentTypeTranslationPEOContentTypeName | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[contenttypetranslationextractpvo|ContentTypeTranslationExtractPVO]] (HCM · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CONTENT_DESCRIPTION | ContentDescription | ✅ |
| CONTENT_TYPE_ID | ContentTypeId | ✅ |
| CONTENT_TYPE_NAME | ContentTypeName | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[criticalityprofileitempvo|CriticalityProfileItemPVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTLBusinessGroupId | — |
| BUSINESS_GROUP_ID | CTTLBusinessGroupId1 | — |
| CONTENT_DESCRIPTION | CTTLContentDescription | ✅ |
| CONTENT_TYPE_ID | CTLContentTypeId | — |
| CONTENT_TYPE_ID | ContentTypeId2 | — |
| CONTENT_TYPE_NAME | CTLContentTypeName | — |
| CONTENT_TYPE_NAME | CTTLContentTypeName | ✅ |
| CREATED_BY | CTTLCreatedBy1 | — |
| LANGUAGE | CTLLanguage1 | — |
| LANGUAGE | CTTLLanguage | — |
| LAST_UPDATE_DATE | CTTLLastUpdateDate1 | ✅ |
| LAST_UPDATED_BY | CTTLLastUpdatedBy1 | — |

### [[customcontentprofilepvo|CustomContentProfilePVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTLBusinessGroupId | — |
| CONTENT_DESCRIPTION | CTTLContentDescription | — |
| CONTENT_TYPE_ID | CTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTLContentTypeName | — |
| LANGUAGE | CTLLanguage1 | — |
| LAST_UPDATE_DATE | CntTypeTLPEOLastUpdateDate | ✅ |

### [[customcontentprofilepvo_viewall|CustomContentProfilePVO_Viewall]] (HCM · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTLBusinessGroupId | — |
| CONTENT_DESCRIPTION | CTTLContentDescription | ✅ |
| CONTENT_TYPE_ID | CTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTLContentTypeName | ✅ |
| LANGUAGE | CTLLanguage1 | — |
| LAST_UPDATE_DATE | CntTypeTLPEOLastUpdateDate | ✅ |

### [[degreepvo|DegreePVO]] (HCM · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CONTENT_DESCRIPTION | ContentDescription | — |
| CONTENT_TYPE_ID | ContentTypeId | ✅ |
| CONTENT_TYPE_NAME | ContentTypeName | ✅ |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[genericprofilepvo|GenericProfilePVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTLBusinessGroupId | — |
| CONTENT_DESCRIPTION | CTTLContentDescription | — |
| CONTENT_TYPE_ID | CTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTLContentTypeName | — |
| LANGUAGE | CTLLanguage1 | — |
| LAST_UPDATE_DATE | CntTypeTLPEOLastUpdateDate | — |

### [[honorpvo|HonorPVO]] (HCM · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| BUSINESS_GROUP_ID | CTLBusinessGroupId | — |
| CONTENT_DESCRIPTION | CTLContentDescription | — |
| CONTENT_TYPE_ID | CTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTLContentTypeName | ✅ |
| LANGUAGE | CTLLanguage1 | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[languagepvo|LanguagePVO]] (HCM · BICC: 3/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| CONTENT_TYPE_ID | ContentTypeId1 | — |
| CONTENT_TYPE_NAME | ContentTypeName | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[membershippvo|MembershipPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CONTENT_DESCRIPTION | ContentDescription | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTENT_TYPE_NAME | ContentTypeName | — |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[modelprofileitempvo|ModelProfileItemPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTTLBusinessGroupId | — |
| CONTENT_DESCRIPTION | CTTLContentDescription | — |
| CONTENT_TYPE_ID | CTTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTTLContentTypeName | — |
| LANGUAGE | CTTLLanguage1 | — |

### [[personprofileitempvo|PersonProfileItemPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTTLBusinessGroupId | — |
| CONTENT_DESCRIPTION | CTTLContentDescription | — |
| CONTENT_TYPE_ID | CTTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTTLContentTypeName | — |
| LANGUAGE | CTTLLanguage1 | — |
| LAST_UPDATE_DATE | CntTypeTLPEOLastUpdateDate | ✅ |

### [[personprofileperformanceratingpvo|PersonProfilePerformanceRatingPVO]] (HCM · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CONTENT_DESCRIPTION | ContentDescription | ✅ |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTENT_TYPE_NAME | ContentTypeName | ✅ |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[planreadinesspvo|PlanReadinessPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTTLBusinessGroupId | — |
| CONTENT_TYPE_ID | CTTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTTLContentTypeName | — |
| LANGUAGE | CTTLLanguage | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | — |

### [[potentialpvo|PotentialPVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTLBusinessGroupId | — |
| CONTENT_DESCRIPTION | CTLContentDescription | — |
| CONTENT_TYPE_ID | CTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTLContentTypeName | ✅ |
| LANGUAGE | CTLLanguage | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[potentialpvo_viewall|PotentialPVO_Viewall]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTLBusinessGroupId | — |
| CONTENT_DESCRIPTION | CTLContentDescription | — |
| CONTENT_TYPE_ID | CTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTLContentTypeName | ✅ |
| LANGUAGE | CTLLanguage | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[previousemploymentprofilepvo|PreviousEmploymentProfilePVO]] (HCM · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TLBusinessGroupId | — |
| CONTENT_DESCRIPTION | CTTLContentDescription | ✅ |
| CONTENT_TYPE_ID | CTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTTLContentTypeName | ✅ |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[previousemploymentpvo|PreviousEmploymentPVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTLBusinessGroupId | — |
| CONTENT_DESCRIPTION | CTTLContentDescription | ✅ |
| CONTENT_TYPE_ID | CTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTLContentTypeName | — |
| LANGUAGE | CTLLanguage1 | — |
| LAST_UPDATE_DATE | CntTypeTLPEOLastUpdateDate | ✅ |

### [[riskpvo|RiskPVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTTLBusinessGroupId | — |
| CONTENT_DESCRIPTION | CTTLContentDescription | — |
| CONTENT_TYPE_ID | CTTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTTLContentTypeName | ✅ |
| LANGUAGE | CTTLLanguage | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[riskpvo_viewall|RiskPVO_Viewall]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTTLBusinessGroupId | — |
| CONTENT_DESCRIPTION | CTTLContentDescription | — |
| CONTENT_TYPE_ID | CTTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTTLContentTypeName | ✅ |
| LANGUAGE | CTTLLanguage | — |
| LAST_UPDATE_DATE | ContentTypeTranslationPEOLastUpdateDate | ✅ |

### [[specialprojectpvo|SpecialProjectPVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTTLBusinessGroupId2 | — |
| CONTENT_DESCRIPTION | CTTLContentDescription | — |
| CONTENT_TYPE_ID | CTTLContentTypeId1 | — |
| CONTENT_TYPE_NAME | CTTLContentTypeName | ✅ |
| LANGUAGE | CTTLLanguage | — |

### [[talentscorepvo|TalentScorePVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTBusinessGroupId1 | — |
| CONTENT_DESCRIPTION | CTTLContentDescription | — |
| CONTENT_TYPE_ID | CTTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTTLContentTypeName | — |
| LANGUAGE | CTLanguage | — |

### [[technicalpostpvo|TechnicalPostPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTLBusinessGroupId | — |
| CONTENT_DESCRIPTION | CTTLContentDescription | — |
| CONTENT_TYPE_ID | CTLContentTypeId | — |
| CONTENT_TYPE_NAME | CTLContentTypeName | — |
| LANGUAGE | CTLLanguage1 | — |
| LAST_UPDATE_DATE | CntTypeTLPEOLastUpdateDate | ✅ |

### [[workrequirementdatecheckpvo|WorkRequirementDateCheckPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTTLBusinessGroupId1 | — |
| CONTENT_TYPE_ID | CT_ContentTypeId1 | — |
| CONTENT_TYPE_NAME | ContentTypeName | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | — |

### [[workrequirementpvo|WorkRequirementPVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTTLBusinessGroupId1 | — |
| CONTENT_TYPE_ID | CT_ContentTypeId1 | — |
| CONTENT_TYPE_NAME | ContentTypeName | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | ContentTypeBPEOLastUpdateDate | ✅ |
