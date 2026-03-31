---
id: DOC-HCM-248
doc_type: system-doc
title: "HRT_PROFILE_RELATIONS — Relacionamentos entre Perfis"
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
  - profile-relations
  - talent
  - matching
aliases:
  - HRT_PROFILE_RELATIONS
  - hrt_profile_relations
  - hrt-profile-relations
  - profile-relations
  - relacionamentos-perfil
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_PROFILE_RELATIONS

## 📌 Visao Geral

Armazena os **relacionamentos entre perfis de talento** — permite vincular perfis de pessoa a perfis de posicao, job ou modelo para fins de matching e gap analysis.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Matching:** Vincular perfil de pessoa ao perfil de posicao ocupada.
- **Gap analysis:** Identificar diferencas entre competencias.
- **Sucessao:** Vincular candidatos a posicoes em planos de sucessao.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROFILE_RELATION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do relacionamento | — | 🟢 95% |
| 2 | PROFILE_ID | NUMBER(18) | NOT NULL | FK | Perfil de origem | [[hrt_profiles_b]] | 🟢 95% |
| 3 | RELATED_PROFILE_ID | NUMBER(18) | NOT NULL | FK | Perfil relacionado | [[hrt_profiles_b]] | 🟢 95% |
| 4 | RELATION_TYPE | VARCHAR2(30) | NOT NULL | Classificacao | Tipo de relacionamento | — | 🟡 80% |
| 5 | DATE_FROM | DATE | NULL | Data | Data de inicio | — | 🟢 85% |
| 6 | DATE_TO | DATE | NULL | Data | Data de fim | — | 🟢 85% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_profiles_b]] — via `PROFILE_ID` (perfil de origem da relacao)
- [[hrt_profiles_b]] — via `RELATED_PROFILE_ID` (perfil relacionado na associacao)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Relacionamentos de um perfil
```sql
SELECT pr.RELATED_PROFILE_ID, pr.RELATION_TYPE
FROM   HRT_PROFILE_RELATIONS pr
WHERE  pr.PROFILE_ID = :p_profile_id;
```

---

## 🔒 Observacoes

- Relacionamento e direcional — PROFILE_ID e a origem.
- RELATION_TYPE define a natureza do vinculo.

---

## 📚 Referencias

- [Oracle Docs — HRT_PROFILE_RELATIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtprofilerelations.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[goaltargetoutcomeprofilespvo|GoalTargetOutcomeProfilesPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_ID | ProfileRelationPEOObjectId | — |
| PROFILE_RELATION_ID | ProfileRelationPEOProfileRelationId | — |
| RELATION_ID | ProfileRelationPEORelationId | — |

### [[jobprofilepvo|JobProfilePVO]] (HCM · BICC: 2/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileRelationPEOBusinessGroupId | — |
| CREATED_BY | ProfileRelationPEOCreatedBy | — |
| CREATION_DATE | ProfileRelationPEOCreationDate | — |
| LAST_UPDATE_DATE | ProfileRelationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileRelationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileRelationPEOLastUpdatedBy | — |
| OBJECT_EFF_END_DATE | ProfileRelationPEOObjectEffEndDate | — |
| OBJECT_EFF_START_DATE | ProfileRelationPEOObjectEffStartDate | — |
| OBJECT_ID | ProfileRelationPEOObjectId | ✅ |
| OBJECT_VERSION_NUMBER | ProfileRelationPEOObjectVersionNumber | — |
| PROFILE_ID | ProfileRelationPEOProfileId | — |
| PROFILE_RELATION_ID | ProfileRelationPEOProfileRelationId | — |
| RELATION_ID | ProfileRelationPEORelationId | — |

### [[modelprofileitempvo|ModelProfileItemPVO]] (HCM · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileRelationPEOBusinessGroupId | — |
| OBJECT_EFF_END_DATE | ProfileRelationPEOObjectEffEndDate | — |
| OBJECT_EFF_START_DATE | ProfileRelationPEOObjectEffStartDate | — |
| OBJECT_ID | ProfileRelationPEOObjectId | ✅ |
| PROFILE_ID | ProfileRelationPEOProfileId | — |
| PROFILE_RELATION_ID | ProfileRelationPEOProfileRelationId | ✅ |
| RELATION_ID | ProfileRelationPEORelationId | ✅ |

### [[modelprofilepvo|ModelProfilePVO]] (HCM · BICC: 8/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileRelationPEOBusinessGroupId | ✅ |
| LAST_UPDATE_DATE | ProfileRelationPEOLastUpdateDate | ✅ |
| OBJECT_EFF_END_DATE | ProfileRelationPEOObjectEffEndDate | ✅ |
| OBJECT_EFF_START_DATE | ProfileRelationPEOObjectEffStartDate | ✅ |
| OBJECT_ID | ProfileRelationPEOObjectId | ✅ |
| PROFILE_ID | ProfileRelationPEOProfileId | ✅ |
| PROFILE_RELATION_ID | ProfileRelationPEOProfileRelationId | ✅ |
| RELATION_ID | ProfileRelationPEORelationId | ✅ |

### [[profilerelationpvo|ProfileRelationPVO]] (HCM · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_EFF_END_DATE | ObjectEffEndDate | ✅ |
| OBJECT_EFF_START_DATE | ObjectEffStartDate | ✅ |
| OBJECT_ID | ObjectId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PROFILE_ID | ProfileId | ✅ |
| PROFILE_RELATION_ID | ProfileRelationId | ✅ |
| RELATION_ID | RelationId | ✅ |
