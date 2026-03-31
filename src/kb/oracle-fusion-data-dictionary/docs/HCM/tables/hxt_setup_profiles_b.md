---
id: DOC-HCM-413
doc_type: system-doc
title: "HXT_SETUP_PROFILES_B — Perfis de Configuracao HXT (Base)"
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
  - setup-profile
  - perfil-configuracao
  - base
aliases:
  - HXT_SETUP_PROFILES_B
  - hxt_setup_profiles_b
  - hxt-setup-profiles-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_SETUP_PROFILES_B

## 📌 Visao Geral

Tabela base que armazena os **perfis de configuracao** do modulo Time & Labor (HXT). Cada perfil agrupa um conjunto de opcoes de setup.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base) — contem os dados primarios sem traducoes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Agrupamento de configuracoes:** organiza opcoes de setup em perfis.
- **Atribuicao por contexto:** permite diferentes configuracoes por organizacao ou grupo.
- **Administracao centralizada:** gerencia perfis de setup do HXT.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROFILE_ID | NUMBER(18) | NOT NULL | PK | Identificador do perfil | — | 🟡 70% |
| 2 | PROFILE_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do perfil | — | 🟡 70% |
| 3 | PROFILE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do perfil | — | 🟡 60% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Indicador ativo/inativo | — | 🟡 65% |
| 5 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificacao | Codigo da legislacao | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saida)
- [[hxt_setup_profiles_tl]] — via `PROFILE_ID` (traducoes do perfil de configuracao de ponto)
- [[hxt_setup_option_vals]] — via `PROFILE_ID` (valores de opcoes)
- [[hxt_setup_profile_asgs]] — via `PROFILE_ID` (atribuicoes do perfil de configuracao)

---

## 📎 Uso Tipico

### Listar perfis de configuracao ativos
```sql
SELECT p.PROFILE_ID, p.PROFILE_CODE, p.PROFILE_TYPE
FROM   HXT_SETUP_PROFILES_B p
WHERE  p.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y' — Perfis ativos`
- `LEGISLATION_CODE = 'BR' — Legislacao brasileira`

---

## 🔒 Observacoes

- Tabela base (_B) — traducoes em HXT_SETUP_PROFILES_TL.
- Perfis controlam o comportamento do modulo Time & Labor.
- Cada perfil pode ter multiplas opcoes de configuracao associadas.

---

## 📚 Referencias

- [Oracle Docs — HXT_SETUP_PROFILES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxtsetupprofilesb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[setupprofileasgpvo|SetupProfileAsgPVO]] (GL · BICC: 9/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | SetupProfileBPEOCreatedBy | ✅ |
| CREATION_DATE | SetupProfileBPEOCreationDate | ✅ |
| ENTERPRISE_ID | SetupProfileBPEOEnterpriseId | — |
| LAST_UPDATE_DATE | SetupProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SetupProfileBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | SetupProfileBPEOLastUpdatedBy | ✅ |
| MODULE_ID | SetupProfileBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | SetupProfileBPEOObjectVersionNumber | — |
| PRECEDENCE | SetupProfileBPEOPrecedence | ✅ |
| PRODUCT_AREA | SetupProfileBPEOProductArea | ✅ |
| SETUP_PROFILE_CD | SetupProfileBPEOSetupProfileCd | ✅ |
| SETUP_PROFILE_ID | SetupProfileBPEOSetupProfileId | ✅ |

### [[setupprofilepvo|SetupProfilePVO]] (GL · BICC: 9/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | SetupProfileBPEOCreatedBy | ✅ |
| CREATION_DATE | SetupProfileBPEOCreationDate | ✅ |
| ENTERPRISE_ID | SetupProfileBPEOEnterpriseId | — |
| LAST_UPDATE_DATE | SetupProfileBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SetupProfileBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | SetupProfileBPEOLastUpdatedBy | ✅ |
| MODULE_ID | SetupProfileBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | SetupProfileBPEOObjectVersionNumber | — |
| PRECEDENCE | SetupProfileBPEOPrecedence | ✅ |
| PRODUCT_AREA | SetupProfileBPEOProductArea | ✅ |
| SETUP_PROFILE_CD | SetupProfileBPEOSetupProfileCd | ✅ |
| SETUP_PROFILE_ID | SetupProfileBPEOSetupProfileId | ✅ |
