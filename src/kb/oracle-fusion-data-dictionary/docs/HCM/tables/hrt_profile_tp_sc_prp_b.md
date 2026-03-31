---
id: DOC-HCM-249
doc_type: system-doc
title: "HRT_PROFILE_TP_SC_PRP_B — Propriedades de Secoes de Tipo de Perfil — Base"
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
  - profile-type-section-properties
  - configuracao
aliases:
  - HRT_PROFILE_TP_SC_PRP_B
  - hrt_profile_tp_sc_prp_b
  - hrt-profile-tp-sc-prp-b
  - profile-tp-sc-prp-base
  - propriedades-secao-tipo-perfil
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_PROFILE_TP_SC_PRP_B

## 📌 Visao Geral

Tabela base que armazena as **propriedades das secoes de tipos de perfil**. Define configuracoes especificas de cada secao dentro de um tipo de perfil.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Definir propriedades de secoes de perfil.
- **Estruturacao:** Controlar comportamento de cada secao de conteudo.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROFILE_TP_SC_PRP_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da propriedade | — | 🟢 90% |
| 2 | PROFILE_TYPE_SECTION_ID | NUMBER(18) | NOT NULL | FK | Secao do tipo de perfil | [[hrt_profile_typ_sections_vl]] | 🟢 90% |
| 3 | PROPERTY_CODE | VARCHAR2(30) | NOT NULL | Classificacao | Codigo da propriedade | — | 🟢 85% |
| 4 | PROPERTY_VALUE | VARCHAR2(240) | NULL | Dados | Valor da propriedade | — | 🟢 85% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_profile_typ_sections_vl]] — via `PROFILE_TYPE_SECTION_ID` (secao do tipo de perfil da propriedade)

### Tabelas-filha (FK de saida)
- [[hrt_profile_tp_sc_prp_tl]] — via `PROFILE_TP_SC_PRP_ID` (traducoes da propriedade de secao)

---

## 📎 Uso Tipico

### Propriedades de uma secao
```sql
SELECT p.PROPERTY_CODE, p.PROPERTY_VALUE
FROM   HRT_PROFILE_TP_SC_PRP_B p
WHERE  p.PROFILE_TYPE_SECTION_ID = :p_section_id;
```

---

## 🔒 Observacoes

- Sufixo `_B` indica tabela base.
- Propriedades controlam comportamento de UI e validacoes de perfil.

---

## 📚 Referencias

- [Oracle Docs — HRT_PROFILE_TP_SC_PRP_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtprofiletpscprpb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[competencycontentitemratingpvo|CompetencyContentItemRatingPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTpScPrpBPEOBusinessGroupId | — |
| COLUMN_NAME | ProfileTpScPrpBPEOColumnName | — |
| DEFAULT_VALUE | ProfileTpScPrpBPEODefaultValue | — |
| DISPLAY_FLAG | DisplayFlag | — |
| FIELD_NAME | FieldName | — |
| LAST_UPDATE_DATE | ProfileTpScPrpBPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTpScPrpBPEOModuleId | — |
| PROPERTY_SOURCE | PropertySource | — |
| REQUIRED_FLAG | RequiredFlag | — |
| SEARCH_FLAG | SearchFlag | — |
| SECTION_ID | ProfileTpScPrpBPEOSectionId | — |
| SECTION_PROP_ID | ProfileTpScPrpBPEOSectionPropId | ✅ |
| VALUE_SET_NAME | ValueSetName | — |
| VIEW_ATTRB_NAME | ViewAttrbName | — |

### [[impactratinglevelpvo|ImpactRatingLevelPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTpScPrpBPEOBusinessGroupId | — |
| COLUMN_NAME | ProfileTpScPrpBPEOColumnName | — |
| DEFAULT_VALUE | ProfileTpScPrpBPEODefaultValue | — |
| DISPLAY_FLAG | DisplayFlag | — |
| FIELD_NAME | FieldName | — |
| LAST_UPDATE_DATE | ProfileTpScPrpBPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTpScPrpBPEOModuleId | — |
| PROPERTY_SOURCE | PropertySource | — |
| REQUIRED_FLAG | RequiredFlag | — |
| SEARCH_FLAG | SearchFlag | — |
| SECTION_ID | ProfileTpScPrpBPEOSectionId | — |
| SECTION_PROP_ID | ProfileTpScPrpBPEOSectionPropId | ✅ |
| VALUE_SET_NAME | ValueSetName | — |
| VIEW_ATTRB_NAME | ViewAttrbName | — |

### [[potentialratinglevelpvo|PotentialRatingLevelPVO]] (HCM · BICC: 3/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTpScPrpBPEOBusinessGroupId | ✅ |
| COLUMN_NAME | ProfileTpScPrpBPEOColumnName | — |
| DEFAULT_VALUE | ProfileTpScPrpBPEODefaultValue | — |
| DISPLAY_FLAG | DisplayFlag | — |
| FIELD_NAME | FieldName | — |
| LAST_UPDATE_DATE | ProfileTpScPrpBPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTpScPrpBPEOModuleId | — |
| PROPERTY_SOURCE | PropertySource | — |
| REQUIRED_FLAG | RequiredFlag | — |
| SEARCH_FLAG | SearchFlag | — |
| SECTION_ID | ProfileTpScPrpBPEOSectionId | — |
| SECTION_PROP_ID | ProfileTpScPrpBPEOSectionPropId | ✅ |
| VALUE_SET_NAME | ValueSetName | — |
| VIEW_ATTRB_NAME | ViewAttrbName | — |

### [[profiletypesectionpropertypvo|ProfileTypeSectionPropertyPVO]] (HCM · BICC: 3/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTypeSectionPropertyBPEOBusinessGroupId | ✅ |
| COLUMN_NAME | ProfileTypeSectionPropertyBPEOColumnName | — |
| CREATED_BY | ProfileTypeSectionPropertyBPEOCreatedBy | — |
| CREATION_DATE | ProfileTypeSectionPropertyBPEOCreationDate | — |
| DEFAULT_VALUE | ProfileTypeSectionPropertyBPEODefaultValue | — |
| DISPLAY_FLAG | ProfileTypeSectionPropertyBPEODisplayFlag | — |
| FIELD_NAME | ProfileTypeSectionPropertyBPEOFieldName | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPropertyBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileTypeSectionPropertyBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileTypeSectionPropertyBPEOLastUpdatedBy | — |
| MODULE_ID | ProfileTypeSectionPropertyBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | ProfileTypeSectionPropertyBPEOObjectVersionNumber | — |
| PROPERTY_SOURCE | ProfileTypeSectionPropertyBPEOPropertySource | — |
| REQUIRED_FLAG | ProfileTypeSectionPropertyBPEORequiredFlag | — |
| SEARCH_FLAG | ProfileTypeSectionPropertyBPEOSearchFlag | — |
| SECTION_ID | ProfileTypeSectionPropertyBPEOSectionId | — |
| SECTION_PROP_ID | ProfileTypeSectionPropertyBPEOSectionPropId | ✅ |
| VALUE_SET_NAME | ProfileTypeSectionPropertyBPEOValueSetName | — |
| VIEW_ATTRB_NAME | ProfileTypeSectionPropertyBPEOViewAttrbName | — |

### [[readingratinglevelpvo|ReadingRatingLevelPVO]] (HCM · BICC: 1/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTpScPrpBPEOBusinessGroupId | — |
| COLUMN_NAME | ProfileTpScPrpBPEOColumnName | — |
| DEFAULT_VALUE | ProfileTpScPrpBPEODefaultValue | — |
| DISPLAY_FLAG | DisplayFlag | — |
| FIELD_NAME | FieldName | — |
| LAST_UPDATE_DATE | ProfileTpScPrpBPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTpScPrpBPEOModuleId | — |
| PROPERTY_SOURCE | PropertySource | — |
| REQUIRED_FLAG | RequiredFlag | — |
| SEARCH_FLAG | SearchFlag | — |
| SECTION_ID | ProfileTpScPrpBPEOSectionId | — |
| SECTION_PROP_ID | ProfileTpScPrpBPEOSectionPropId | — |
| VALUE_SET_NAME | ValueSetName | — |
| VIEW_ATTRB_NAME | ViewAttrbName | — |

### [[riskratinglevelpvo|RiskRatingLevelPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTpScPrpBPEOBusinessGroupId | — |
| COLUMN_NAME | ProfileTpScPrpBPEOColumnName | — |
| DEFAULT_VALUE | ProfileTpScPrpBPEODefaultValue | — |
| DISPLAY_FLAG | DisplayFlag | — |
| FIELD_NAME | FieldName | — |
| LAST_UPDATE_DATE | ProfileTpScPrpBPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTpScPrpBPEOModuleId | — |
| PROPERTY_SOURCE | PropertySource | — |
| REQUIRED_FLAG | RequiredFlag | — |
| SEARCH_FLAG | SearchFlag | — |
| SECTION_ID | ProfileTpScPrpBPEOSectionId | — |
| SECTION_PROP_ID | ProfileTpScPrpBPEOSectionPropId | ✅ |
| VALUE_SET_NAME | ValueSetName | — |
| VIEW_ATTRB_NAME | ViewAttrbName | — |

### [[speakingratinglevelpvo|SpeakingRatingLevelPVO]] (HCM · BICC: 1/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTpScPrpBPEOBusinessGroupId | — |
| COLUMN_NAME | ProfileTpScPrpBPEOColumnName | — |
| DEFAULT_VALUE | ProfileTpScPrpBPEODefaultValue | — |
| DISPLAY_FLAG | DisplayFlag | — |
| FIELD_NAME | FieldName | — |
| LAST_UPDATE_DATE | ProfileTpScPrpBPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTpScPrpBPEOModuleId | — |
| PROPERTY_SOURCE | PropertySource | — |
| REQUIRED_FLAG | RequiredFlag | — |
| SEARCH_FLAG | SearchFlag | — |
| SECTION_ID | ProfileTpScPrpBPEOSectionId | — |
| SECTION_PROP_ID | ProfileTpScPrpBPEOSectionPropId | — |
| VALUE_SET_NAME | ValueSetName | — |
| VIEW_ATTRB_NAME | ViewAttrbName | — |

### [[writingratinglevelpvo|WritingRatingLevelPVO]] (HCM · BICC: 1/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTpScPrpBPEOBusinessGroupId | — |
| COLUMN_NAME | ProfileTpScPrpBPEOColumnName | — |
| DEFAULT_VALUE | ProfileTpScPrpBPEODefaultValue | — |
| DISPLAY_FLAG | DisplayFlag | — |
| FIELD_NAME | FieldName | — |
| LAST_UPDATE_DATE | ProfileTpScPrpBPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTpScPrpBPEOModuleId | — |
| PROPERTY_SOURCE | PropertySource | — |
| REQUIRED_FLAG | RequiredFlag | — |
| SEARCH_FLAG | SearchFlag | — |
| SECTION_ID | ProfileTpScPrpBPEOSectionId | — |
| SECTION_PROP_ID | ProfileTpScPrpBPEOSectionPropId | — |
| VALUE_SET_NAME | ValueSetName | — |
| VIEW_ATTRB_NAME | ViewAttrbName | — |
