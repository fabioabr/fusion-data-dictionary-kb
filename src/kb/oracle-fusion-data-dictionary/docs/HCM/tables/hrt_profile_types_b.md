---
id: DOC-HCM-251
doc_type: system-doc
title: "HRT_PROFILE_TYPES_B — Tipos de Perfil de Talento — Base"
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
  - profile-types
  - configuracao
  - talent
aliases:
  - HRT_PROFILE_TYPES_B
  - hrt_profile_types_b
  - hrt-profile-types-b
  - profile-types-base
  - tipos-perfil-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_PROFILE_TYPES_B

## 📌 Visao Geral

Tabela base que define os **tipos de perfil** disponiveis — pessoa, posicao, job, modelo. Cada tipo determina a estrutura e secoes que compoem os perfis.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Definir quais tipos de perfil existem no sistema.
- **Estruturacao:** Cada tipo define suas secoes de conteudo.
- **Governanca:** Controlar quais secoes estao disponiveis para cada tipo de perfil.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROFILE_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do tipo de perfil | — | 🟢 100% |
| 2 | PROFILE_TYPE_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do tipo (e.g., PERSON, POSITION) | — | 🟢 100% |
| 3 | PROFILE_USAGE_CODE | VARCHAR2(30) | NOT NULL | Classificacao | Uso do tipo de perfil | — | 🟢 95% |
| 4 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio de vigencia | — | 🟢 95% |
| 5 | DATE_TO | DATE | NULL | Data | Data de fim de vigencia | — | 🟢 95% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- [[hrt_profile_types_tl]] — via `PROFILE_TYPE_ID` (traducoes do tipo de perfil)
- [[hrt_profiles_b]] — via `PROFILE_TYPE_ID` (traducoes do tipo de perfil)
- [[hrt_profile_type_rels]] — via `PROFILE_TYPE_ID` (traducoes do tipo de perfil)
- [[hrt_profile_typ_sections_vl]] — via `PROFILE_TYPE_ID` (traducoes do tipo de perfil)

---

## 📎 Uso Tipico

### Tipos de perfil ativos
```sql
SELECT pt.PROFILE_TYPE_ID, pt.PROFILE_TYPE_CODE
FROM   HRT_PROFILE_TYPES_B pt
WHERE  SYSDATE BETWEEN pt.DATE_FROM AND NVL(pt.DATE_TO, SYSDATE);
```

---

## 🔒 Observacoes

- Sufixo `_B` — traducoes em [[hrt_profile_types_tl]].
- Tipos padrao Oracle: PERSON, POSITION, JOB, WORKFORCE_STRUCTURE, MODEL.

---

## 📚 Referencias

- [Oracle Docs — HRT_PROFILE_TYPES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtprofiletypesb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[meetingfactpvo|MeetingFactPVO]] (HCM · BICC: 1/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTypeBPEOBusinessGroupId | — |
| CREATED_BY | ProfileTypeBPEOCreatedBy | — |
| CREATION_DATE | ProfileTypeBPEOCreationDate | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| LAST_UPDATE_DATE | ProfileTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileTypeBPEOLastUpdatedBy | — |
| MODULE_ID | ModuleId | — |
| OBJECT_VERSION_NUMBER | ProfileTypeBPEOObjectVersionNumber | — |
| PID_APPROVAL_FLAG | PidApprovalFlag | — |
| PROFILE_STATUS_CODE | ProfileTypeBPEOProfileStatusCode | — |
| PROFILE_TYPE_CODE | ProfileTypeCode | — |
| PROFILE_TYPE_ID | ProfileTypeBPEOProfileTypeId | — |
| PROFILE_USAGE_CODE | ProfileTypeBPEOProfileUsageCode | — |

### [[modelprofileitempvo|ModelProfileItemPVO]] (HCM · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTypeBPEOBusinessGroupId | — |
| DATE_FROM | ProfileTypeBPEODateFrom | — |
| DATE_TO | ProfileTypeBPEODateTo | — |
| MODULE_ID | ProfileTypeBPEOModuleId | — |
| PID_APPROVAL_FLAG | ProfileTypeBPEOPidApprovalFlag | ✅ |
| PROFILE_STATUS_CODE | ProfileTypeBPEOProfileStatusCode | ✅ |
| PROFILE_TYPE_CODE | ProfileTypeBPEOProfileTypeCode | ✅ |
| PROFILE_TYPE_ID | ProfileTypeBPEOProfileTypeId | ✅ |
| PROFILE_USAGE_CODE | ProfileTypeBPEOProfileUsageCode | — |

### [[modelprofilepvo|ModelProfilePVO]] (HCM · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTypeBPEOBusinessGroupId | ✅ |
| DATE_FROM | ProfileTypeBPEODateFrom | ✅ |
| DATE_TO | ProfileTypeBPEODateTo | ✅ |
| LAST_UPDATE_DATE | ProfileTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTypeBPEOModuleId | ✅ |
| PID_APPROVAL_FLAG | ProfileTypeBPEOPidApprovalFlag | ✅ |
| PROFILE_STATUS_CODE | ProfileTypeBPEOProfileStatusCode | ✅ |
| PROFILE_TYPE_CODE | ProfileTypeBPEOProfileTypeCode | ✅ |
| PROFILE_TYPE_ID | ProfileTypeBPEOProfileTypeId | ✅ |
| PROFILE_USAGE_CODE | ProfileTypeBPEOProfileUsageCode | ✅ |

### [[personprofileitempvo|PersonProfileItemPVO]] (HCM · BICC: 3/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTypeBPEOBusinessGroupId | — |
| DATE_FROM | ProfileTypeBPEODateFrom | — |
| DATE_TO | ProfileTypeBPEODateTo | — |
| LAST_UPDATE_DATE | ProfileTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTypeBPEOModuleId | — |
| PID_APPROVAL_FLAG | ProfileTypeBPEOPidApprovalFlag | ✅ |
| PROFILE_STATUS_CODE | ProfileTypeBPEOProfileStatusCode | — |
| PROFILE_TYPE_CODE | ProfileTypeBPEOProfileTypeCode | — |
| PROFILE_TYPE_ID | ProfileTypeBPEOProfileTypeId | ✅ |
| PROFILE_USAGE_CODE | ProfileTypeBPEOProfileUsageCode | — |

### [[personprofilepvo|PersonProfilePVO]] (HCM · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTypeBPEOBusinessGroupId | ✅ |
| DATE_FROM | ProfileTypeBPEODateFrom | ✅ |
| DATE_TO | ProfileTypeBPEODateTo | ✅ |
| LAST_UPDATE_DATE | ProfileTypeBPEOLastUpdateDate | ✅ |
| MODULE_ID | ProfileTypeBPEOModuleId | ✅ |
| PID_APPROVAL_FLAG | ProfileTypeBPEOPidApprovalFlag | ✅ |
| PROFILE_STATUS_CODE | ProfileTypeBPEOProfileStatusCode | ✅ |
| PROFILE_TYPE_CODE | ProfileTypeBPEOProfileTypeCode | ✅ |
| PROFILE_TYPE_ID | ProfileTypeBPEOProfileTypeId | ✅ |
| PROFILE_USAGE_CODE | ProfileTypeBPEOProfileUsageCode | ✅ |

### [[profiletypepvo|ProfileTypePVO]] (HCM · BICC: 12/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileTypeBPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_FROM | ProfileTypeBPEODateFrom | ✅ |
| DATE_TO | ProfileTypeBPEODateTo | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MODULE_ID | ProfileTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PID_APPROVAL_FLAG | ProfileTypeBPEOPidApprovalFlag | ✅ |
| PROFILE_STATUS_CODE | ProfileTypeBPEOProfileStatusCode | ✅ |
| PROFILE_TYPE_CODE | ProfileTypeBPEOProfileTypeCode | ✅ |
| PROFILE_TYPE_ID | ProfileTypeBPEOProfileTypeId | ✅ |
| PROFILE_USAGE_CODE | ProfileTypeBPEOProfileUsageCode | ✅ |
