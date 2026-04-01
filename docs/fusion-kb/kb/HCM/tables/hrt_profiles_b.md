---
id: DOC-HCM-245
doc_type: system-doc
title: "HRT_PROFILES_B — Perfis de Talento — Base"
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
  - profiles
  - talent
  - competencias
aliases:
  - HRT_PROFILES_B
  - hrt_profiles_b
  - hrt-profiles-b
  - profiles-base
  - perfis-talento-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_PROFILES_B

## 📌 Visao Geral

Tabela base que armazena os **perfis de talento** — cada perfil representa o conjunto de competencias, habilidades, experiencias e qualificacoes de uma pessoa ou posicao. E a entidade central do modulo Talent Profile.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Talent Management:** Registrar competencias e qualificacoes de colaboradores.
- **Matching:** Comparar perfis de pessoa vs. perfis de posicao (gap analysis).
- **Sucessao:** Base para identificar candidatos qualificados para posicoes criticas.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROFILE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do perfil | — | 🟢 100% |
| 2 | PROFILE_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de perfil | [[hrt_profile_types_b]] | 🟢 100% |
| 3 | PROFILE_USAGE_CODE | VARCHAR2(30) | NOT NULL | Classificacao | Uso do perfil (PERSON, POSITION, JOB, MODEL) | — | 🟢 95% |
| 4 | PROFILE_STATUS_CODE | VARCHAR2(30) | NULL | Classificacao | Status do perfil (ACTIVE, INACTIVE) | — | 🟡 80% |
| 5 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa associada (se perfil de pessoa) | [[per_all_people_f]] | 🟢 95% |
| 6 | POSITION_ID | NUMBER(18) | NULL | FK | Posicao associada (se perfil de posicao) | [[hr_all_positions_f]] | 🟢 90% |
| 7 | JOB_ID | NUMBER(18) | NULL | FK | Job associado (se perfil de job) | — | 🟡 80% |
| 8 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio de vigencia | — | 🟢 95% |
| 9 | DATE_TO | DATE | NULL | Data | Data de fim de vigencia | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_profile_types_b]] — via `PROFILE_TYPE_ID` (tipo de perfil de talento)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa titular do perfil de talento)
- [[hr_all_positions_f]] — via `POSITION_ID` (posicao associada ao perfil de talento)

### Tabelas-filha (FK de saida)
- [[hrt_profiles_tl]] — via `PROFILE_ID` (traducoes do perfil de talento)
- [[hrt_profile_items]] — via `PROFILE_ID` (itens do perfil)
- [[hrt_profile_relations]] — via `PROFILE_ID` (relacionamentos)

---

## 📎 Uso Tipico

### Perfis ativos de pessoas
```sql
SELECT p.PROFILE_ID, p.PERSON_ID, p.PROFILE_STATUS_CODE
FROM   HRT_PROFILES_B p
WHERE  p.PROFILE_USAGE_CODE = 'PERSON'
  AND  p.PROFILE_STATUS_CODE = 'ACTIVE';
```

---

## 🔒 Observacoes

- Sufixo `_B` indica tabela base — traducoes em [[hrt_profiles_tl]].
- PROFILE_USAGE_CODE define se e perfil de PERSON, POSITION, JOB ou MODEL.
- Apenas um dos campos PERSON_ID, POSITION_ID, JOB_ID e preenchido conforme o uso.

---

## 📚 Referencias

- [Oracle Docs — HRT_PROFILES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtprofilesb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[advancementreadinesspvo|AdvancementReadinessPVO]] (HCM · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | — |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[advancementreadinesspvo_viewall|AdvancementReadinessPVO_Viewall]] (HCM · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | — |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[calibratedoverallcompetenciespvo|CalibratedOverallCompetenciesPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[calibratedoverallgoalpvo|CalibratedOverallGoalPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[calibratedperformancepvo|CalibratedPerformancePVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[calibratedperformancepvo_viewall|CalibratedPerformancePVO_Viewall]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[calibratedpotentialpvo|CalibratedPotentialPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[calibratedpotentialpvo_viewall|CalibratedPotentialPVO_Viewall]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[calibratedriskpvo|CalibratedRiskPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[calibratedriskpvo_viewall|CalibratedRiskPVO_Viewall]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[calibratedtalentscorepvo|CalibratedTalentScorePVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[calibratedtalentscorepvo_viewall|CalibratedTalentScorePVO_Viewall]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[competenciescalbratingpvo|CompetenciesCalbRatingPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[competenciescalbratingpvo_viewall|CompetenciesCalbRatingPVO_ViewAll]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[criticalityprofileitempvo|CriticalityProfileItemPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[customcontentprofilepvo|CustomContentProfilePVO]] (HCM · BICC: 7/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | ✅ |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[customcontentprofilepvo_viewall|CustomContentProfilePVO_Viewall]] (HCM · BICC: 7/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | ✅ |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[genericprofilepvo|GenericProfilePVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[goalscalibratingpvo|GoalsCalibRatingPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[goalscalibratingpvo_viewall|GoalsCalibRatingPVO_ViewAll]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[goaltargetoutcomeprofilespvo|GoalTargetOutcomeProfilesPVO]] (HCM · BICC: 1/1)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PROFILE_ID | ProfileId | ✅ |

### [[impactoflosscalibratingpvo|ImpactOfLossCalibRatingPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[impactoflosscalibratingpvo_viewall|ImpactOfLossCalibRatingPVO_ViewAll]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[jobprofilepvo|JobProfilePVO]] (HCM · BICC: 2/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |
| REVIEW_REQD_FLAG | ProfileBPEOReviewRequiredFlag | — |

### [[meetingfactpvo|MeetingFactPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | OwnerPersonId | — |
| PARTY_ID | PartyId | — |
| PERSON_ID | PersonId | — |
| PROFILE_CODE | ProfileCode | — |
| PROFILE_ID | ProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileUsageCode | — |

### [[modelprofileitempvo|ModelProfileItemPVO]] (HCM · BICC: 12/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | ✅ |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | ✅ |
| PROFILE_CODE | ProfileBPEOProfileCode | ✅ |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | ✅ |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | ✅ |
| REVIEW_REQD_FLAG | ProfileBPEOReviewReqdFlag | — |

### [[modelprofilepvo|ModelProfilePVO]] (HCM · BICC: 14/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | ✅ |
| PARTY_ID | ProfileBPEOPartyId | ✅ |
| PERSON_ID | ProfileBPEOPersonId | ✅ |
| PROFILE_CODE | ProfileBPEOProfileCode | ✅ |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | ✅ |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | ✅ |
| REVIEW_REQD_FLAG | ProfileBPEOReviewRequiredFlag | — |

### [[nboxdimensionpvo|NBoxDimensionPVO]] (HCM · BICC: 3/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | ✅ |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[performancecalibratedratingvo|PerformanceCalibratedRatingVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[performancecalibratedratingvo_viewall|PerformanceCalibratedRatingVO_ViewAll]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[performancepotentialboxsequencepvo|PerformancePotentialBoxSequencePVO]] (HCM · BICC: 4/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | ✅ |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[performancepotentialboxsequencepvo_viewall|PerformancePotentialBoxSequencePVO_Viewall]] (HCM · BICC: 4/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | ✅ |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[personprofileitempvo|PersonProfileItemPVO]] (HCM · BICC: 7/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | ✅ |
| PERSON_ID | ProfileBPEOPersonId | ✅ |
| PROFILE_CODE | ProfileBPEOProfileCode | ✅ |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | ✅ |

### [[personprofileperformanceratingpvo|PersonProfilePerformanceRatingPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[personprofilepvo|PersonProfilePVO]] (HCM · BICC: 14/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | ✅ |
| PARTY_ID | ProfileBPEOPartyId | ✅ |
| PERSON_ID | ProfileBPEOPersonId | ✅ |
| PROFILE_CODE | ProfileBPEOProfileCode | ✅ |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | ✅ |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | ✅ |

### [[planreadinesspvo|PlanReadinessPVO]] (HCM · BICC: 8/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | ✅ |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | ✅ |
| PARTY_ID | ProfileBPEOPartyId | ✅ |
| PERSON_ID | ProfileBPEOPersonId | ✅ |
| PROFILE_CODE | ProfileBPEOProfileCode | ✅ |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | ✅ |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | ✅ |

### [[potentialcalibratedratingvo|PotentialCalibratedRatingVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[potentialcalibratedratingvo_viewall|PotentialCalibratedRatingVO_ViewAll]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[potentialpvo|PotentialPVO]] (HCM · BICC: 9/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | ✅ |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | ✅ |
| PARTY_ID | ProfileBPEOPartyId | ✅ |
| PERSON_ID | ProfileBPEOPersonId | ✅ |
| PROFILE_CODE | ProfileBPEOProfileCode | ✅ |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | ✅ |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | ✅ |

### [[potentialpvo_viewall|PotentialPVO_Viewall]] (HCM · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | — |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[previousemploymentprofilepvo|PreviousEmploymentProfilePVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[previousemploymentpvo|PreviousEmploymentPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[riskoflosscalibratingpvo|RiskOfLossCalibRatingPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[riskoflosscalibratingpvo_viewall|RiskOfLossCalibRatingPVO_ViewAll]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[riskpvo|RiskPVO]] (HCM · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | — |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[riskpvo_viewall|RiskPVO_Viewall]] (HCM · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | — |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[talentscoreboxsequencepvo|TalentScoreBoxSequencePVO]] (HCM · BICC: 4/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | ✅ |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[talentscoreboxsequencepvo_viewall|TalentScoreBoxSequencePVO_Viewall]] (HCM · BICC: 4/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | ✅ |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[talentscorecalibratingpvo|TalentScoreCalibRatingPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[talentscorecalibratingpvo_viewall|TalentScoreCalibRatingPVO_ViewAll]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | ProfileBPEOCreatedBy | — |
| CREATION_DATE | ProfileBPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileBPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |

### [[talentscorepvo|TalentScorePVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PrfBusinessGroupId | — |
| CREATED_BY | PrfCreatedBy | — |
| CREATION_DATE | PrfCreationDate | — |
| LAST_UPDATE_DATE | PrfLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PrfLastUpdateLogin | — |
| LAST_UPDATED_BY | PrfLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PrfObjectVersionNumber | — |
| OWNER_PERSON_ID | PrfOwnerPersonId | — |
| PARTY_ID | PrfPartyId | — |
| PERSON_ID | PrfPersonId | — |
| PROFILE_CODE | PrfProfileCode | — |
| PROFILE_ID | PrfProfileId | ✅ |
| PROFILE_TYPE_ID | PrfProfileTypeId | — |
| PROFILE_USAGE_CODE | PrfProfileUsageCode | — |

### [[technicalpostpvo|TechnicalPostPVO]] (HCM · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileBPEOBusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNER_PERSON_ID | ProfileBPEOOwnerPersonId | — |
| PARTY_ID | ProfileBPEOPartyId | — |
| PERSON_ID | ProfileBPEOPersonId | — |
| PROFILE_CODE | ProfileBPEOProfileCode | — |
| PROFILE_ID | ProfileBPEOProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileBPEOProfileUsageCode | — |
