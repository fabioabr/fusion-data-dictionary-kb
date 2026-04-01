---
id: DOC-HCM-416
doc_type: system-doc
title: "HXT_SETUP_PROFILE_ASGS — Atribuicoes de Perfis de Configuracao HXT"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - time-labor
  - hxt
  - setup-profile-assignment
  - atribuicao-perfil
aliases:
  - HXT_SETUP_PROFILE_ASGS
  - hxt_setup_profile_asgs
  - hxt-setup-profile-asgs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_SETUP_PROFILE_ASGS

## 📌 Visao Geral

Armazena as **atribuicoes de perfis de configuracao** do modulo Time & Labor (HXT) a organizacoes, locais ou grupos especificos.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Atribuicao de perfis:** vincula perfis de setup a contextos organizacionais.
- **Configuracao por organizacao:** permite diferentes setups por unidade de negocio.
- **Hierarquia:** suporta heranca de configuracao na hierarquia organizacional.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROFILE_ASG_ID | NUMBER(18) | NOT NULL | PK | Identificador da atribuicao | — | 🟡 70% |
| 2 | PROFILE_ID | NUMBER(18) | NOT NULL | FK | Perfil de configuracao | HXT_SETUP_PROFILES_B | 🟡 70% |
| 3 | ORGANIZATION_ID | NUMBER(18) | NULL | FK | Organizacao atribuida | HR_ALL_ORGANIZATION_UNITS | 🟡 65% |
| 4 | LOCATION_ID | NUMBER(18) | NULL | FK | Local atribuido | — | 🟡 55% |
| 5 | ASSIGNMENT_SCOPE | VARCHAR2(30) | NULL | Classificacao | Escopo da atribuicao | — | 🟡 60% |
| 6 | EFFECTIVE_START_DATE | DATE | NULL | Vigencia | Inicio da vigencia | — | 🟡 60% |
| 7 | EFFECTIVE_END_DATE | DATE | NULL | Vigencia | Fim da vigencia | — | 🟡 60% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hxt_setup_profiles_b]] — via `PROFILE_ID` (perfil de configuracao da atribuicao)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Atribuicoes de perfil por organizacao
```sql
SELECT a.PROFILE_ASG_ID, a.PROFILE_ID, a.ORGANIZATION_ID,
       a.ASSIGNMENT_SCOPE
FROM   HXT_SETUP_PROFILE_ASGS a
WHERE  a.ORGANIZATION_ID = :p_org_id;
```

### Filtros comuns
- `ORGANIZATION_ID = :p_org_id — Por organizacao`
- `PROFILE_ID = :p_profile_id — Por perfil`

---

## 🔒 Observacoes

- Vincula perfis de setup HXT a contextos organizacionais.
- Permite configuracoes diferentes de Time & Labor por organizacao/local.

---

## 📚 Referencias

- [Oracle Docs — HXT_SETUP_PROFILE_ASGS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxtsetupprofileasgs.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[labordemandpvo|LaborDemandPVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGN_TO | AssignTo | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| OBJECT_ID | ObjectId | — |
| SETUP_PROFILE_ASG_ID | SetupProfileAsgId | ✅ |

### [[setupprofileasgpvo|SetupProfileAsgPVO]] (GL · BICC: 11/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGN_TO | SetupProfileAsgPEOAssignTo | ✅ |
| CREATED_BY | SetupProfileAsgPEOCreatedBy | ✅ |
| CREATION_DATE | SetupProfileAsgPEOCreationDate | ✅ |
| DATE_FROM | SetupProfileAsgPEODateFrom | ✅ |
| DATE_TO | SetupProfileAsgPEODateTo | ✅ |
| ENTERPRISE_ID | SetupProfileAsgPEOEnterpriseId | — |
| LAST_UPDATE_DATE | SetupProfileAsgPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SetupProfileAsgPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | SetupProfileAsgPEOLastUpdatedBy | ✅ |
| MODULE_ID | SetupProfileAsgPEOModuleId | — |
| OBJECT_ID | SetupProfileAsgPEOObjectId | ✅ |
| OBJECT_VERSION_NUMBER | SetupProfileAsgPEOObjectVersionNumber | — |
| SEED_DATA_SOURCE | SetupProfileAsgPEOSeedDataSource | — |
| SETUP_PROFILE_ASG_CD | SetupProfileAsgPEOSetupProfileAsgCd | ✅ |
| SETUP_PROFILE_ASG_ID | SetupProfileAsgPEOSetupProfileAsgId | ✅ |
| SETUP_PROFILE_ID | SetupProfileAsgPEOSetupProfileId | — |
| SGUID | SetupProfileAsgPEOSguid | — |
