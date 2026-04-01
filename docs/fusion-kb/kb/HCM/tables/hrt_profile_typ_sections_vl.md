---
id: DOC-HCM-255
doc_type: system-doc
title: "HRT_PROFILE_TYP_SECTIONS_VL — Secoes de Tipo de Perfil (View Linguistica)"
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
  - profile-type-sections
  - configuracao
  - talent
aliases:
  - HRT_PROFILE_TYP_SECTIONS_VL
  - hrt_profile_typ_sections_vl
  - hrt-profile-typ-sections-vl
  - profile-typ-sections-vl
  - secoes-tipo-perfil-vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_PROFILE_TYP_SECTIONS_VL

## 📌 Visao Geral

View linguistica que combina dados base e traducoes das **secoes de tipo de perfil**. Cada secao representa uma categoria de conteudo dentro de um tipo de perfil.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Definir quais secoes compoem cada tipo de perfil.
- **Estruturacao:** Organizar os itens de perfil em categorias.
- **Exibicao:** Apresentar secoes com nomes traduzidos em UIs.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROFILE_TYPE_SECTION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da secao | — | 🟢 95% |
| 2 | PROFILE_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de perfil | [[hrt_profile_types_b]] | 🟢 95% |
| 3 | CONTENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de conteudo da secao | [[hrt_content_types_b]] | 🟢 95% |
| 4 | SECTION_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome da secao (traduzido) | — | 🟢 95% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao da secao | — | 🟢 90% |
| 6 | SECTION_SEQUENCE | NUMBER | NULL | Dados | Ordem de exibicao da secao | — | 🟡 80% |
| 7 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio de vigencia | — | 🟢 90% |
| 8 | DATE_TO | DATE | NULL | Data | Data de fim de vigencia | — | 🟢 90% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_profile_types_b]] — via `PROFILE_TYPE_ID` (tipo de perfil da secao)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo da secao de perfil)

### Tabelas-filha (FK de saida)
- [[hrt_profile_tp_sc_prp_b]] — via `PROFILE_TYPE_SECTION_ID` (propriedades da secao do tipo de perfil)

---

## 📎 Uso Tipico

### Secoes de um tipo de perfil
```sql
SELECT pts.SECTION_NAME, pts.CONTENT_TYPE_ID, pts.SECTION_SEQUENCE
FROM   HRT_PROFILE_TYP_SECTIONS_VL pts
WHERE  pts.PROFILE_TYPE_ID = :p_profile_type_id
ORDER BY pts.SECTION_SEQUENCE;
```

---

## 🔒 Observacoes

- Sufixo `_VL` indica View Linguistica.
- Cada secao vincula um tipo de conteudo a um tipo de perfil.

---

## 📚 Referencias

- [Oracle Docs — HRT_PROFILE_TYP_SECTIONS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtprofiletypsectionsvl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[advancementreadinesspvo|AdvancementReadinessPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | PTSSectionId | — |

### [[advancementreadinesspvo_viewall|AdvancementReadinessPVO_Viewall]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | PTSSectionId | — |

### [[careerpreferencepvo|CareerPreferencePVO]] (HCM · BICC: 3/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | SectionId | ✅ |

### [[certificationpvo|CertificationPVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| BUSINESS_GROUP_ID | PTS_BusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | CT_SectionId1 | — |
| SECTION_ID | PT_SectionId1 | — |

### [[competencycontentitemratingpvo|CompetencyContentItemRatingPVO]] (HCM · BICC: 2/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_REQUIRED_FLAG | ApprovalRequiredFlag | — |
| BUSINESS_GROUP_ID | ProfileTypeSectionPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ProfileTypeSectionPEOContentTypeId | — |
| CONTENT_TYPE_RELATION_ID | ProfileTypeSectionPEOContentTypeRelationId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTypeSectionPEOModuleId | — |
| PARENT_SECTION_ID | ProfileTypeSectionPEOParentSectionId | — |
| PROFILE_TYPE_ID | ProfileTypeSectionPEOProfileTypeId | — |
| QUALIFIER_SET_ID1 | QualifierSetId1 | — |
| QUALIFIER_SET_ID2 | QualifierSetId2 | — |
| SECTION_CONTEXT | ProfileTypeSectionPEOSectionContext | — |
| SECTION_ID | ProfileTypeSectionPEOSectionId | ✅ |
| SECTION_ITEM_REQD_FLAG | SectionItemReqdFlag | — |

### [[competencypvo|CompetencyPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | SectionId1 | — |

### [[criticalityprofileitempvo|CriticalityProfileItemPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTS_BusinessGroupId1 | — |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | PTSSectionId | — |

### [[customcontentprofilepvo|CustomContentProfilePVO]] (HCM · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId | — |
| CREATED_BY | PTSCreatedBy1 | — |
| CREATION_DATE | PTSCreationDate1 | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_CONTEXT | SectionContext | — |
| SECTION_ID | PTSSectionId1 | ✅ |

### [[customcontentprofilepvo_viewall|CustomContentProfilePVO_Viewall]] (HCM · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId | — |
| CREATED_BY | PTSCreatedBy1 | — |
| CREATION_DATE | PTSCreationDate1 | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_CONTEXT | SectionContext | — |
| SECTION_ID | PTSSectionId1 | ✅ |

### [[degreepvo|DegreePVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | SectionId1 | — |

### [[genericprofilepvo|GenericProfilePVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId | — |
| CREATED_BY | PTSCreatedBy1 | — |
| CREATION_DATE | PTSCreationDate1 | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | — |
| NAME | ProfileTypeSectionPEOName | — |
| SECTION_CONTEXT | SectionContext | — |
| SECTION_ID | PTSSectionId1 | — |

### [[honorpvo|HonorPVO]] (HCM · BICC: 2/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTPEOBusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| QUALIFIER_SET_ID1 | QualifierSetId1 | — |
| QUALIFIER_SET_ID2 | QualifierSetId2 | — |
| SECTION_CONTEXT | SectionContext | — |
| SECTION_ID | PTPEOSectionId1 | — |
| SECTION_ITEM_REQD_FLAG | PTPEOSectionItemReqdFlag | — |

### [[impactratinglevelpvo|ImpactRatingLevelPVO]] (HCM · BICC: 2/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_REQUIRED_FLAG | ApprovalRequiredFlag | — |
| BUSINESS_GROUP_ID | ProfileTypeSectionPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ProfileTypeSectionPEOContentTypeId | — |
| CONTENT_TYPE_RELATION_ID | ProfileTypeSectionPEOContentTypeRelationId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTypeSectionPEOModuleId | — |
| PARENT_SECTION_ID | ProfileTypeSectionPEOParentSectionId | — |
| PROFILE_TYPE_ID | ProfileTypeSectionPEOProfileTypeId | — |
| QUALIFIER_SET_ID1 | QualifierSetId1 | — |
| QUALIFIER_SET_ID2 | QualifierSetId2 | — |
| SECTION_CONTEXT | ProfileTypeSectionPEOSectionContext | — |
| SECTION_ID | ProfileTypeSectionPEOSectionId | ✅ |
| SECTION_ITEM_REQD_FLAG | SectionItemReqdFlag | — |

### [[languagepvo|LanguagePVO]] (HCM · BICC: 3/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | SectionId | ✅ |

### [[membershippvo|MembershipPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | SectionId1 | — |

### [[modelprofileitempvo|ModelProfileItemPVO]] (HCM · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_REQUIRED_FLAG | ApprovalRequiredFlag | — |
| BUSINESS_GROUP_ID | PTSBusinessGroupId | — |
| CREATED_BY | PTSCreatedBy1 | — |
| CREATION_DATE | PTSCreationDate1 | — |
| LAST_UPDATE_DATE | PTSLastUpdateDate1 | ✅ |
| LAST_UPDATED_BY | PTSLastUpdatedBy1 | — |
| NAME | ProfileTypeSectionPEOName | — |
| PARENT_SECTION_ID | ParentSectionId | — |
| PROFILE_TYPE_ID | PTSProfileTypeId | — |
| SECTION_CONTEXT | PTSSectionContext | — |
| SECTION_ID | SectionId1 | — |

### [[performancedocsectionpvo|PerformanceDocSectionPVO]] (HCM · BICC: 2/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_REQUIRED_FLAG | ProfileTypeSectionPEOApprovalRequiredFlag | — |
| BUSINESS_GROUP_ID | ProfileTypeSectionPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ProfileTypeSectionPEOContentTypeId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| PROFILE_TYPE_ID | ProfileTypeSectionPEOProfileTypeId | — |
| SECTION_ID | ProfileTypeSectionPEOSectionId | — |
| SECTION_ITEM_REQD_FLAG | ProfileTypeSectionPEOSectionItemReqdFlag | — |

### [[personprofileitempvo|PersonProfileItemPVO]] (HCM · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_REQUIRED_FLAG | ApprovalRequiredFlag | — |
| BUSINESS_GROUP_ID | PTSBusinessGroupId | — |
| CREATED_BY | PTSCreatedBy1 | — |
| CREATION_DATE | PTSCreationDate1 | — |
| LAST_UPDATE_DATE | PTSLastUpdateDate1 | ✅ |
| LAST_UPDATED_BY | PTSLastUpdatedBy1 | — |
| NAME | ProfileTypeSectionPEOName | — |
| PARENT_SECTION_ID | ParentSectionId | — |
| PROFILE_TYPE_ID | PTSProfileTypeId | — |
| SECTION_CONTEXT | PTSSectionContext | — |
| SECTION_ID | SectionId1 | — |

### [[personprofileperformanceratingpvo|PersonProfilePerformanceRatingPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId1 | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | PTSSectionId1 | — |

### [[planreadinesspvo|PlanReadinessPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | — |
| NAME | ProfileTypeSectionPEOName | — |
| SECTION_ID | PTSSectionId | — |

### [[potentialpvo|PotentialPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | PTSSectionId1 | — |

### [[potentialpvo_viewall|PotentialPVO_Viewall]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | PTSSectionId1 | — |

### [[potentialratinglevelpvo|PotentialRatingLevelPVO]] (HCM · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_REQUIRED_FLAG | ApprovalRequiredFlag | — |
| BUSINESS_GROUP_ID | ProfileTypeSectionPEOBusinessGroupId | ✅ |
| CONTENT_TYPE_ID | ProfileTypeSectionPEOContentTypeId | — |
| CONTENT_TYPE_RELATION_ID | ProfileTypeSectionPEOContentTypeRelationId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTypeSectionPEOModuleId | — |
| PARENT_SECTION_ID | ProfileTypeSectionPEOParentSectionId | — |
| PROFILE_TYPE_ID | ProfileTypeSectionPEOProfileTypeId | — |
| QUALIFIER_SET_ID1 | QualifierSetId1 | — |
| QUALIFIER_SET_ID2 | QualifierSetId2 | — |
| SECTION_CONTEXT | ProfileTypeSectionPEOSectionContext | — |
| SECTION_ID | ProfileTypeSectionPEOSectionId | ✅ |
| SECTION_ITEM_REQD_FLAG | SectionItemReqdFlag | — |

### [[previousemploymentprofilepvo|PreviousEmploymentProfilePVO]] (HCM · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| PARENT_SECTION_ID | PTSParentSectionId | — |
| QUALIFIER_SET_ID1 | PTSQualifierSetId1 | — |
| QUALIFIER_SET_ID2 | PTSQualifierSetId2 | — |
| SECTION_ID | PTS_SectionId1 | — |

### [[previousemploymentpvo|PreviousEmploymentPVO]] (HCM · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId | — |
| CREATED_BY | PTSCreatedBy1 | — |
| CREATION_DATE | PTSCreationDate1 | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_CONTEXT | SectionContext | — |
| SECTION_ID | PTSSectionId1 | — |

### [[profiletypesectionpvo|ProfileTypeSectionPVO]] (HCM · BICC: 4/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_REQUIRED_FLAG | ApprovalRequiredFlag | — |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CONTENT_TYPE_RELATION_ID | ContentTypeRelationId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DESCRIPTION | SectionDescription | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MODULE_ID | ModuleId | — |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PARENT_SECTION_ID | ParentSectionId | — |
| PROFILE_TYPE_ID | ProfileTypeId | — |
| QUALIFIER_SET_ID1 | QualifierSetId1 | — |
| QUALIFIER_SET_ID2 | QualifierSetId2 | — |
| SECTION_CONTEXT | SectionContext | — |
| SECTION_ID | SectionId | ✅ |
| SECTION_ITEM_REQD_FLAG | SectionItemReqdFlag | — |

### [[projrolequalificationspvo|ProjRoleQualificationsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | ProfileTypeSectionPEOName | — |

### [[readingratinglevelpvo|ReadingRatingLevelPVO]] (HCM · BICC: 1/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_REQUIRED_FLAG | ApprovalRequiredFlag | — |
| BUSINESS_GROUP_ID | ProfileTypeSectionPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ProfileTypeSectionPEOContentTypeId | — |
| CONTENT_TYPE_RELATION_ID | ProfileTypeSectionPEOContentTypeRelationId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTypeSectionPEOModuleId | — |
| PARENT_SECTION_ID | ProfileTypeSectionPEOParentSectionId | — |
| PROFILE_TYPE_ID | ProfileTypeSectionPEOProfileTypeId | — |
| QUALIFIER_SET_ID1 | QualifierSetId1 | — |
| QUALIFIER_SET_ID2 | QualifierSetId2 | — |
| SECTION_CONTEXT | ProfileTypeSectionPEOSectionContext | — |
| SECTION_ID | ProfileTypeSectionPEOSectionId | — |
| SECTION_ITEM_REQD_FLAG | SectionItemReqdFlag | — |

### [[resourcequalificationpvo|ResourceQualificationPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | ProfileTypeSectionPEOName | — |

### [[resourcerequestdetailspvo|ResourceRequestDetailsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | ProfileTypeSectionPEOName | — |

### [[riskpvo|RiskPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSPEOBusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | PTSectionPEOSectionId1 | — |

### [[riskpvo_viewall|RiskPVO_Viewall]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSPEOBusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | PTSectionPEOSectionId1 | — |

### [[riskratinglevelpvo|RiskRatingLevelPVO]] (HCM · BICC: 2/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_REQUIRED_FLAG | ApprovalRequiredFlag | — |
| BUSINESS_GROUP_ID | ProfileTypeSectionPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ProfileTypeSectionPEOContentTypeId | — |
| CONTENT_TYPE_RELATION_ID | ProfileTypeSectionPEOContentTypeRelationId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTypeSectionPEOModuleId | — |
| PARENT_SECTION_ID | ProfileTypeSectionPEOParentSectionId | — |
| PROFILE_TYPE_ID | ProfileTypeSectionPEOProfileTypeId | — |
| QUALIFIER_SET_ID1 | QualifierSetId1 | — |
| QUALIFIER_SET_ID2 | QualifierSetId2 | — |
| SECTION_CONTEXT | ProfileTypeSectionPEOSectionContext | — |
| SECTION_ID | ProfileTypeSectionPEOSectionId | ✅ |
| SECTION_ITEM_REQD_FLAG | SectionItemReqdFlag | — |

### [[speakingratinglevelpvo|SpeakingRatingLevelPVO]] (HCM · BICC: 1/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_REQUIRED_FLAG | ApprovalRequiredFlag | — |
| BUSINESS_GROUP_ID | ProfileTypeSectionPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ProfileTypeSectionPEOContentTypeId | — |
| CONTENT_TYPE_RELATION_ID | ProfileTypeSectionPEOContentTypeRelationId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTypeSectionPEOModuleId | — |
| PARENT_SECTION_ID | ProfileTypeSectionPEOParentSectionId | — |
| PROFILE_TYPE_ID | ProfileTypeSectionPEOProfileTypeId | — |
| QUALIFIER_SET_ID1 | QualifierSetId1 | — |
| QUALIFIER_SET_ID2 | QualifierSetId2 | — |
| SECTION_CONTEXT | ProfileTypeSectionPEOSectionContext | — |
| SECTION_ID | ProfileTypeSectionPEOSectionId | — |
| SECTION_ITEM_REQD_FLAG | SectionItemReqdFlag | — |

### [[specialprojectpvo|SpecialProjectPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | SectionId1 | — |

### [[talentscorepvo|TalentScorePVO]] (HCM · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId | — |
| NAME | ProfileTypeSectionPEOName | ✅ |
| PARENT_SECTION_ID | ParentSectionId | — |
| QUALIFIER_SET_ID1 | QualifierSetId1 | — |
| QUALIFIER_SET_ID2 | QualifierSetId2 | — |
| SECTION_CONTEXT | SectionContext | — |
| SECTION_ID | PTSSectionId1 | — |
| SECTION_ITEM_REQD_FLAG | PTSSectionItemReqdFlag | — |

### [[technicalpostpvo|TechnicalPostPVO]] (HCM · BICC: 1/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId | — |
| CREATED_BY | PTSCreatedBy1 | — |
| CREATION_DATE | PTSCreationDate1 | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | — |
| SECTION_CONTEXT | SectionContext | — |
| SECTION_ID | PTSSectionId1 | — |

### [[workrequirementdatecheckpvo|WorkRequirementDateCheckPVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId1 | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | — |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | PTSSectionId | ✅ |
| SECTION_ITEM_REQD_FLAG | PTSSectionItemReqdFlag | — |

### [[workrequirementpvo|WorkRequirementPVO]] (HCM · BICC: 3/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PTSBusinessGroupId1 | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| NAME | ProfileTypeSectionPEOName | ✅ |
| SECTION_ID | PTSSectionId | ✅ |
| SECTION_ITEM_REQD_FLAG | PTSSectionItemReqdFlag | — |

### [[writingratinglevelpvo|WritingRatingLevelPVO]] (HCM · BICC: 1/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_REQUIRED_FLAG | ApprovalRequiredFlag | — |
| BUSINESS_GROUP_ID | ProfileTypeSectionPEOBusinessGroupId | — |
| CONTENT_TYPE_ID | ProfileTypeSectionPEOContentTypeId | — |
| CONTENT_TYPE_RELATION_ID | ProfileTypeSectionPEOContentTypeRelationId | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTypeSectionPEOModuleId | — |
| PARENT_SECTION_ID | ProfileTypeSectionPEOParentSectionId | — |
| PROFILE_TYPE_ID | ProfileTypeSectionPEOProfileTypeId | — |
| QUALIFIER_SET_ID1 | QualifierSetId1 | — |
| QUALIFIER_SET_ID2 | QualifierSetId2 | — |
| SECTION_CONTEXT | ProfileTypeSectionPEOSectionContext | — |
| SECTION_ID | ProfileTypeSectionPEOSectionId | — |
| SECTION_ITEM_REQD_FLAG | SectionItemReqdFlag | — |
