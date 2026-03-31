---
id: DOC-HCM-412
doc_type: system-doc
title: "HXT_SETUP_OPTION_VALS — Valores de Opcoes de Configuracao HXT"
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
  - setup
  - configuracao
  - opcoes
aliases:
  - HXT_SETUP_OPTION_VALS
  - hxt_setup_option_vals
  - hxt-setup-option-vals
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_SETUP_OPTION_VALS

## 📌 Visao Geral

Armazena os **valores das opcoes de configuracao** do modulo Time & Labor (HXT). Cada registro contem um par opcao-valor que parametriza o comportamento do modulo.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Parametrizacao:** define valores de configuracao do modulo Time & Labor.
- **Personalizacao:** permite ajustar comportamento sem customizacao de codigo.
- **Administracao:** gerencia opcoes de setup de forma centralizada.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | OPTION_VAL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do valor | — | 🟡 70% |
| 2 | PROFILE_ID | NUMBER(18) | NOT NULL | FK | Perfil de configuracao | HXT_SETUP_PROFILES_B | 🟡 70% |
| 3 | OPTION_CODE | VARCHAR2(80) | NOT NULL | Identificacao | Codigo da opcao | — | 🟡 65% |
| 4 | OPTION_VALUE | VARCHAR2(240) | NULL | Dados | Valor da opcao | — | 🟡 65% |
| 5 | OPTION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo da opcao | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hxt_setup_profiles_b]] — via `PROFILE_ID` (perfil de configuracao da opcao de ponto)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Valores de configuracao de um perfil
```sql
SELECT v.OPTION_CODE, v.OPTION_VALUE, v.OPTION_TYPE
FROM   HXT_SETUP_OPTION_VALS v
WHERE  v.PROFILE_ID = :p_profile_id;
```

### Filtros comuns
- `PROFILE_ID = :p_profile_id — Por perfil de setup`
- `OPTION_CODE = :p_code — Por opcao especifica`

---

## 🔒 Observacoes

- Contem parametros de configuracao do modulo HXT.
- Alteracoes podem impactar o comportamento global do Time & Labor.
- Validar valores permitidos na documentacao Oracle.

---

## 📚 Referencias

- [Oracle Docs — HXT_SETUP_OPTION_VALS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxtsetupoptionvals.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[labordemandpvo|LaborDemandPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| SETUP_OPTION_VAL_ID | SetupOptionValId | — |

### [[setupprofileasgpvo|SetupProfileAsgPVO]] (GL · BICC: 147/475)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CorePrflValueDPEOCreatedBy | — |
| CREATED_BY | HtsPrflValueDPEOCreatedBy | — |
| CREATED_BY | MgrPrflValueDPEOCreatedBy | — |
| CREATED_BY | TcdPrflValueDPEOCreatedBy | — |
| CREATED_BY | WkrPrflValueDPEOCreatedBy | — |
| CREATION_DATE | CorePrflValueDPEOCreationDate | — |
| CREATION_DATE | HtsPrflValueDPEOCreationDate | — |
| CREATION_DATE | MgrPrflValueDPEOCreationDate | — |
| CREATION_DATE | TcdPrflValueDPEOCreationDate | — |
| CREATION_DATE | WkrPrflValueDPEOCreationDate | — |
| EFFECTIVE_END_DATE | CorePrflValueDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | HtsPrflValueDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | MgrPrflValueDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | TcdPrflValueDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | WkrPrflValueDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | CorePrflValueDPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | HtsPrflValueDPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | MgrPrflValueDPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | TcdPrflValueDPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | WkrPrflValueDPEOEffectiveStartDate | ✅ |
| ENTERPRISE_ID | CorePrflValueDPEOEnterpriseId | — |
| ENTERPRISE_ID | HtsPrflValueDPEOEnterpriseId | — |
| ENTERPRISE_ID | MgrPrflValueDPEOEnterpriseId | — |
| ENTERPRISE_ID | TcdPrflValueDPEOEnterpriseId | — |
| ENTERPRISE_ID | WkrPrflValueDPEOEnterpriseId | — |
| LAST_UPDATE_DATE | CorePrflValueDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | HtsPrflValueDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | MgrPrflValueDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TcdPrflValueDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | WkrPrflValueDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CorePrflValueDPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | HtsPrflValueDPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | MgrPrflValueDPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TcdPrflValueDPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | WkrPrflValueDPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CorePrflValueDPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | HtsPrflValueDPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | MgrPrflValueDPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | TcdPrflValueDPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | WkrPrflValueDPEOLastUpdatedBy | — |
| MODULE_ID | CorePrflValueDPEOModuleId | — |
| MODULE_ID | HtsPrflValueDPEOModuleId | — |
| MODULE_ID | MgrPrflValueDPEOModuleId | — |
| MODULE_ID | TcdPrflValueDPEOModuleId | — |
| MODULE_ID | WkrPrflValueDPEOModuleId | — |
| OBJECT_VERSION_NUMBER | CorePrflValueDPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | HtsPrflValueDPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | MgrPrflValueDPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TcdPrflValueDPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | WkrPrflValueDPEOObjectVersionNumber | — |
| SEED_DATA_SOURCE | CorePrflValueDPEOSeedDataSource | — |
| SEED_DATA_SOURCE | HtsPrflValueDPEOSeedDataSource | — |
| SEED_DATA_SOURCE | MgrPrflValueDPEOSeedDataSource | — |
| SEED_DATA_SOURCE | TcdPrflValueDPEOSeedDataSource | — |
| SEED_DATA_SOURCE | WkrPrflValueDPEOSeedDataSource | — |
| SETUP_OPTION_VAL_CD | CorePrflValueDPEOSetupOptionValCd | ✅ |
| SETUP_OPTION_VAL_CD | HtsPrflValueDPEOSetupOptionValCd | ✅ |
| SETUP_OPTION_VAL_CD | MgrPrflValueDPEOSetupOptionValCd | ✅ |
| SETUP_OPTION_VAL_CD | TcdPrflValueDPEOSetupOptionValCd | ✅ |
| SETUP_OPTION_VAL_CD | WkrPrflValueDPEOSetupOptionValCd | ✅ |
| SETUP_OPTION_VAL_ID | CorePrflValueDPEOSetupOptionValId | ✅ |
| SETUP_OPTION_VAL_ID | HtsPrflValueDPEOSetupOptionValId | ✅ |
| SETUP_OPTION_VAL_ID | MgrPrflValueDPEOSetupOptionValId | ✅ |
| SETUP_OPTION_VAL_ID | TcdPrflValueDPEOSetupOptionValId | ✅ |
| SETUP_OPTION_VAL_ID | WkrPrflValueDPEOSetupOptionValId | ✅ |
| SETUP_PROFILE_ID | CorePrflValueDPEOSetupProfileId | — |
| SETUP_PROFILE_ID | HtsPrflValueDPEOSetupProfileId | — |
| SETUP_PROFILE_ID | MgrPrflValueDPEOSetupProfileId | — |
| SETUP_PROFILE_ID | TcdPrflValueDPEOSetupProfileId | — |
| SETUP_PROFILE_ID | WkrPrflValueDPEOSetupProfileId | — |
| SGUID | CorePrflValueDPEOSguid | — |
| SGUID | HtsPrflValueDPEOSguid | — |
| SGUID | MgrPrflValueDPEOSguid | — |
| SGUID | TcdPrflValueDPEOSguid | — |
| SGUID | WkrPrflValueDPEOSguid | — |
| TYPE | CorePrflValueDPEOType | — |
| TYPE | HtsPrflValueDPEOType | — |
| TYPE | MgrPrflValueDPEOType | — |
| TYPE | TcdPrflValueDPEOType | — |
| TYPE | WkrPrflValueDPEOType | — |
| VALUE1 | CorePrflValueDPEOValue1 | — |
| VALUE1 | HtsPrflValueDPEOValue1 | — |
| VALUE1 | MgrPrflValueDPEOValue1 | ✅ |
| VALUE1 | TcdPrflValueDPEOValue1 | — |
| VALUE1 | WkrPrflValueDPEOValue1 | ✅ |
| VALUE10 | CorePrflValueDPEOValue10 | — |
| VALUE10 | HtsPrflValueDPEOValue10 | — |
| VALUE10 | MgrPrflValueDPEOValue10 | ✅ |
| VALUE10 | TcdPrflValueDPEOValue10 | ✅ |
| VALUE10 | WkrPrflValueDPEOValue10 | ✅ |
| VALUE11 | CorePrflValueDPEOValue11 | — |
| VALUE11 | HtsPrflValueDPEOValue11 | ✅ |
| VALUE11 | MgrPrflValueDPEOValue11 | ✅ |
| VALUE11 | TcdPrflValueDPEOValue11 | — |
| VALUE11 | WkrPrflValueDPEOValue11 | ✅ |
| VALUE12 | CorePrflValueDPEOValue12 | — |
| VALUE12 | HtsPrflValueDPEOValue12 | ✅ |
| VALUE12 | MgrPrflValueDPEOValue12 | ✅ |
| VALUE12 | TcdPrflValueDPEOValue12 | — |
| VALUE12 | WkrPrflValueDPEOValue12 | ✅ |
| VALUE13 | CorePrflValueDPEOValue13 | — |
| VALUE13 | HtsPrflValueDPEOValue13 | — |
| VALUE13 | MgrPrflValueDPEOValue13 | ✅ |
| VALUE13 | TcdPrflValueDPEOValue13 | — |
| VALUE13 | WkrPrflValueDPEOValue13 | ✅ |
| VALUE14 | CorePrflValueDPEOValue14 | — |
| VALUE14 | HtsPrflValueDPEOValue14 | ✅ |
| VALUE14 | MgrPrflValueDPEOValue14 | ✅ |
| VALUE14 | TcdPrflValueDPEOValue14 | — |
| VALUE14 | WkrPrflValueDPEOValue14 | ✅ |
| VALUE15 | CorePrflValueDPEOValue15 | — |
| VALUE15 | HtsPrflValueDPEOValue15 | ✅ |
| VALUE15 | MgrPrflValueDPEOValue15 | — |
| VALUE15 | TcdPrflValueDPEOValue15 | — |
| VALUE15 | WkrPrflValueDPEOValue15 | — |
| VALUE16 | CorePrflValueDPEOValue16 | — |
| VALUE16 | HtsPrflValueDPEOValue16 | ✅ |
| VALUE16 | MgrPrflValueDPEOValue16 | ✅ |
| VALUE16 | TcdPrflValueDPEOValue16 | — |
| VALUE16 | WkrPrflValueDPEOValue16 | ✅ |
| VALUE17 | CorePrflValueDPEOValue17 | — |
| VALUE17 | HtsPrflValueDPEOValue17 | ✅ |
| VALUE17 | MgrPrflValueDPEOValue17 | ✅ |
| VALUE17 | TcdPrflValueDPEOValue17 | — |
| VALUE17 | WkrPrflValueDPEOValue17 | ✅ |
| VALUE18 | CorePrflValueDPEOValue18 | — |
| VALUE18 | HtsPrflValueDPEOValue18 | — |
| VALUE18 | MgrPrflValueDPEOValue18 | ✅ |
| VALUE18 | TcdPrflValueDPEOValue18 | — |
| VALUE18 | WkrPrflValueDPEOValue18 | ✅ |
| VALUE19 | CorePrflValueDPEOValue19 | — |
| VALUE19 | HtsPrflValueDPEOValue19 | — |
| VALUE19 | MgrPrflValueDPEOValue19 | ✅ |
| VALUE19 | TcdPrflValueDPEOValue19 | — |
| VALUE19 | WkrPrflValueDPEOValue19 | ✅ |
| VALUE2 | CorePrflValueDPEOValue2 | — |
| VALUE2 | HtsPrflValueDPEOValue2 | — |
| VALUE2 | MgrPrflValueDPEOValue2 | ✅ |
| VALUE2 | TcdPrflValueDPEOValue2 | — |
| VALUE2 | WkrPrflValueDPEOValue2 | ✅ |
| VALUE20 | CorePrflValueDPEOValue20 | — |
| VALUE20 | HtsPrflValueDPEOValue20 | — |
| VALUE20 | MgrPrflValueDPEOValue20 | ✅ |
| VALUE20 | TcdPrflValueDPEOValue20 | — |
| VALUE20 | WkrPrflValueDPEOValue20 | ✅ |
| VALUE21 | CorePrflValueDPEOValue21 | — |
| VALUE21 | HtsPrflValueDPEOValue21 | — |
| VALUE21 | MgrPrflValueDPEOValue21 | — |
| VALUE21 | TcdPrflValueDPEOValue21 | — |
| VALUE21 | WkrPrflValueDPEOValue21 | — |
| VALUE22 | CorePrflValueDPEOValue22 | — |
| VALUE22 | HtsPrflValueDPEOValue22 | — |
| VALUE22 | MgrPrflValueDPEOValue22 | — |
| VALUE22 | TcdPrflValueDPEOValue22 | — |
| VALUE22 | WkrPrflValueDPEOValue22 | — |
| VALUE23 | CorePrflValueDPEOValue23 | — |
| VALUE23 | HtsPrflValueDPEOValue23 | — |
| VALUE23 | MgrPrflValueDPEOValue23 | — |
| VALUE23 | TcdPrflValueDPEOValue23 | — |
| VALUE23 | WkrPrflValueDPEOValue23 | — |
| VALUE24 | CorePrflValueDPEOValue24 | — |
| VALUE24 | HtsPrflValueDPEOValue24 | — |
| VALUE24 | MgrPrflValueDPEOValue24 | — |
| VALUE24 | TcdPrflValueDPEOValue24 | — |
| VALUE24 | WkrPrflValueDPEOValue24 | — |
| VALUE25 | CorePrflValueDPEOValue25 | — |
| VALUE25 | HtsPrflValueDPEOValue25 | — |
| VALUE25 | MgrPrflValueDPEOValue25 | — |
| VALUE25 | TcdPrflValueDPEOValue25 | — |
| VALUE25 | WkrPrflValueDPEOValue25 | — |
| VALUE26 | CorePrflValueDPEOValue26 | — |
| VALUE26 | HtsPrflValueDPEOValue26 | — |
| VALUE26 | MgrPrflValueDPEOValue26 | — |
| VALUE26 | TcdPrflValueDPEOValue26 | — |
| VALUE26 | WkrPrflValueDPEOValue26 | — |
| VALUE27 | CorePrflValueDPEOValue27 | — |
| VALUE27 | HtsPrflValueDPEOValue27 | — |
| VALUE27 | MgrPrflValueDPEOValue27 | — |
| VALUE27 | TcdPrflValueDPEOValue27 | — |
| VALUE27 | WkrPrflValueDPEOValue27 | — |
| VALUE28 | CorePrflValueDPEOValue28 | — |
| VALUE28 | HtsPrflValueDPEOValue28 | — |
| VALUE28 | MgrPrflValueDPEOValue28 | — |
| VALUE28 | TcdPrflValueDPEOValue28 | — |
| VALUE28 | WkrPrflValueDPEOValue28 | — |
| VALUE29 | CorePrflValueDPEOValue29 | — |
| VALUE29 | HtsPrflValueDPEOValue29 | — |
| VALUE29 | MgrPrflValueDPEOValue29 | — |
| VALUE29 | TcdPrflValueDPEOValue29 | — |
| VALUE29 | WkrPrflValueDPEOValue29 | — |
| VALUE3 | CorePrflValueDPEOValue3 | — |
| VALUE3 | HtsPrflValueDPEOValue3 | — |
| VALUE3 | MgrPrflValueDPEOValue3 | — |
| VALUE3 | TcdPrflValueDPEOValue3 | — |
| VALUE3 | WkrPrflValueDPEOValue3 | — |
| VALUE30 | CorePrflValueDPEOValue30 | ✅ |
| VALUE30 | HtsPrflValueDPEOValue30 | — |
| VALUE30 | MgrPrflValueDPEOValue30 | ✅ |
| VALUE30 | TcdPrflValueDPEOValue30 | ✅ |
| VALUE30 | WkrPrflValueDPEOValue30 | ✅ |
| VALUE31 | CorePrflValueDPEOValue31 | ✅ |
| VALUE31 | HtsPrflValueDPEOValue31 | — |
| VALUE31 | MgrPrflValueDPEOValue31 | — |
| VALUE31 | TcdPrflValueDPEOValue31 | ✅ |
| VALUE31 | WkrPrflValueDPEOValue31 | — |
| VALUE32 | CorePrflValueDPEOValue32 | ✅ |
| VALUE32 | HtsPrflValueDPEOValue32 | — |
| VALUE32 | MgrPrflValueDPEOValue32 | ✅ |
| VALUE32 | TcdPrflValueDPEOValue32 | ✅ |
| VALUE32 | WkrPrflValueDPEOValue32 | ✅ |
| VALUE33 | CorePrflValueDPEOValue33 | ✅ |
| VALUE33 | HtsPrflValueDPEOValue33 | — |
| VALUE33 | MgrPrflValueDPEOValue33 | ✅ |
| VALUE33 | TcdPrflValueDPEOValue33 | ✅ |
| VALUE33 | WkrPrflValueDPEOValue33 | ✅ |
| VALUE34 | CorePrflValueDPEOValue34 | ✅ |
| VALUE34 | HtsPrflValueDPEOValue34 | — |
| VALUE34 | MgrPrflValueDPEOValue34 | ✅ |
| VALUE34 | TcdPrflValueDPEOValue34 | — |
| VALUE34 | WkrPrflValueDPEOValue34 | ✅ |
| VALUE35 | CorePrflValueDPEOValue35 | — |
| VALUE35 | HtsPrflValueDPEOValue35 | — |
| VALUE35 | MgrPrflValueDPEOValue35 | ✅ |
| VALUE35 | TcdPrflValueDPEOValue35 | — |
| VALUE35 | WkrPrflValueDPEOValue35 | ✅ |
| VALUE36 | CorePrflValueDPEOValue36 | — |
| VALUE36 | HtsPrflValueDPEOValue36 | — |
| VALUE36 | MgrPrflValueDPEOValue36 | — |
| VALUE36 | TcdPrflValueDPEOValue36 | — |
| VALUE36 | WkrPrflValueDPEOValue36 | — |
| VALUE37 | CorePrflValueDPEOValue37 | — |
| VALUE37 | HtsPrflValueDPEOValue37 | — |
| VALUE37 | MgrPrflValueDPEOValue37 | — |
| VALUE37 | TcdPrflValueDPEOValue37 | — |
| VALUE37 | WkrPrflValueDPEOValue37 | — |
| VALUE38 | CorePrflValueDPEOValue38 | — |
| VALUE38 | HtsPrflValueDPEOValue38 | — |
| VALUE38 | MgrPrflValueDPEOValue38 | ✅ |
| VALUE38 | TcdPrflValueDPEOValue38 | — |
| VALUE38 | WkrPrflValueDPEOValue38 | ✅ |
| VALUE39 | CorePrflValueDPEOValue39 | — |
| VALUE39 | HtsPrflValueDPEOValue39 | — |
| VALUE39 | MgrPrflValueDPEOValue39 | ✅ |
| VALUE39 | TcdPrflValueDPEOValue39 | — |
| VALUE39 | WkrPrflValueDPEOValue39 | ✅ |
| VALUE4 | CorePrflValueDPEOValue4 | — |
| VALUE4 | HtsPrflValueDPEOValue4 | — |
| VALUE4 | MgrPrflValueDPEOValue4 | ✅ |
| VALUE4 | TcdPrflValueDPEOValue4 | — |
| VALUE4 | WkrPrflValueDPEOValue4 | ✅ |
| VALUE40 | CorePrflValueDPEOValue40 | — |
| VALUE40 | HtsPrflValueDPEOValue40 | — |
| VALUE40 | MgrPrflValueDPEOValue40 | ✅ |
| VALUE40 | TcdPrflValueDPEOValue40 | — |
| VALUE40 | WkrPrflValueDPEOValue40 | ✅ |
| VALUE41 | CorePrflValueDPEOValue41 | — |
| VALUE41 | HtsPrflValueDPEOValue41 | — |
| VALUE41 | MgrPrflValueDPEOValue41 | ✅ |
| VALUE41 | TcdPrflValueDPEOValue41 | — |
| VALUE41 | WkrPrflValueDPEOValue41 | ✅ |
| VALUE42 | CorePrflValueDPEOValue42 | — |
| VALUE42 | HtsPrflValueDPEOValue42 | — |
| VALUE42 | MgrPrflValueDPEOValue42 | ✅ |
| VALUE42 | TcdPrflValueDPEOValue42 | — |
| VALUE42 | WkrPrflValueDPEOValue42 | ✅ |
| VALUE43 | CorePrflValueDPEOValue43 | — |
| VALUE43 | HtsPrflValueDPEOValue43 | — |
| VALUE43 | MgrPrflValueDPEOValue43 | ✅ |
| VALUE43 | TcdPrflValueDPEOValue43 | — |
| VALUE43 | WkrPrflValueDPEOValue43 | ✅ |
| VALUE44 | CorePrflValueDPEOValue44 | — |
| VALUE44 | HtsPrflValueDPEOValue44 | — |
| VALUE44 | MgrPrflValueDPEOValue44 | ✅ |
| VALUE44 | TcdPrflValueDPEOValue44 | — |
| VALUE44 | WkrPrflValueDPEOValue44 | ✅ |
| VALUE45 | CorePrflValueDPEOValue45 | — |
| VALUE45 | HtsPrflValueDPEOValue45 | — |
| VALUE45 | MgrPrflValueDPEOValue45 | ✅ |
| VALUE45 | TcdPrflValueDPEOValue45 | — |
| VALUE45 | WkrPrflValueDPEOValue45 | ✅ |
| VALUE46 | CorePrflValueDPEOValue46 | — |
| VALUE46 | HtsPrflValueDPEOValue46 | — |
| VALUE46 | MgrPrflValueDPEOValue46 | ✅ |
| VALUE46 | TcdPrflValueDPEOValue46 | — |
| VALUE46 | WkrPrflValueDPEOValue46 | ✅ |
| VALUE47 | CorePrflValueDPEOValue47 | — |
| VALUE47 | HtsPrflValueDPEOValue47 | — |
| VALUE47 | MgrPrflValueDPEOValue47 | ✅ |
| VALUE47 | TcdPrflValueDPEOValue47 | — |
| VALUE47 | WkrPrflValueDPEOValue47 | ✅ |
| VALUE48 | CorePrflValueDPEOValue48 | — |
| VALUE48 | HtsPrflValueDPEOValue48 | — |
| VALUE48 | MgrPrflValueDPEOValue48 | — |
| VALUE48 | TcdPrflValueDPEOValue48 | — |
| VALUE48 | WkrPrflValueDPEOValue48 | — |
| VALUE49 | CorePrflValueDPEOValue49 | — |
| VALUE49 | HtsPrflValueDPEOValue49 | — |
| VALUE49 | MgrPrflValueDPEOValue49 | — |
| VALUE49 | TcdPrflValueDPEOValue49 | — |
| VALUE49 | WkrPrflValueDPEOValue49 | — |
| VALUE5 | CorePrflValueDPEOValue5 | — |
| VALUE5 | HtsPrflValueDPEOValue5 | — |
| VALUE5 | MgrPrflValueDPEOValue5 | ✅ |
| VALUE5 | TcdPrflValueDPEOValue5 | — |
| VALUE5 | WkrPrflValueDPEOValue5 | ✅ |
| VALUE50 | CorePrflValueDPEOValue50 | — |
| VALUE50 | HtsPrflValueDPEOValue50 | ✅ |
| VALUE50 | MgrPrflValueDPEOValue50 | ✅ |
| VALUE50 | TcdPrflValueDPEOValue50 | — |
| VALUE50 | WkrPrflValueDPEOValue50 | ✅ |
| VALUE51 | CorePrflValueDPEOValue51 | — |
| VALUE51 | HtsPrflValueDPEOValue51 | ✅ |
| VALUE51 | MgrPrflValueDPEOValue51 | ✅ |
| VALUE51 | TcdPrflValueDPEOValue51 | — |
| VALUE51 | WkrPrflValueDPEOValue51 | ✅ |
| VALUE52 | CorePrflValueDPEOValue52 | — |
| VALUE52 | HtsPrflValueDPEOValue52 | ✅ |
| VALUE52 | MgrPrflValueDPEOValue52 | ✅ |
| VALUE52 | TcdPrflValueDPEOValue52 | — |
| VALUE52 | WkrPrflValueDPEOValue52 | ✅ |
| VALUE53 | CorePrflValueDPEOValue53 | — |
| VALUE53 | HtsPrflValueDPEOValue53 | ✅ |
| VALUE53 | MgrPrflValueDPEOValue53 | ✅ |
| VALUE53 | TcdPrflValueDPEOValue53 | — |
| VALUE53 | WkrPrflValueDPEOValue53 | ✅ |
| VALUE54 | CorePrflValueDPEOValue54 | — |
| VALUE54 | HtsPrflValueDPEOValue54 | ✅ |
| VALUE54 | MgrPrflValueDPEOValue54 | ✅ |
| VALUE54 | TcdPrflValueDPEOValue54 | — |
| VALUE54 | WkrPrflValueDPEOValue54 | ✅ |
| VALUE55 | CorePrflValueDPEOValue55 | — |
| VALUE55 | HtsPrflValueDPEOValue55 | ✅ |
| VALUE55 | MgrPrflValueDPEOValue55 | ✅ |
| VALUE55 | TcdPrflValueDPEOValue55 | — |
| VALUE55 | WkrPrflValueDPEOValue55 | ✅ |
| VALUE56 | CorePrflValueDPEOValue56 | — |
| VALUE56 | HtsPrflValueDPEOValue56 | — |
| VALUE56 | MgrPrflValueDPEOValue56 | ✅ |
| VALUE56 | TcdPrflValueDPEOValue56 | — |
| VALUE56 | WkrPrflValueDPEOValue56 | ✅ |
| VALUE57 | CorePrflValueDPEOValue57 | — |
| VALUE57 | HtsPrflValueDPEOValue57 | — |
| VALUE57 | MgrPrflValueDPEOValue57 | ✅ |
| VALUE57 | TcdPrflValueDPEOValue57 | — |
| VALUE57 | WkrPrflValueDPEOValue57 | ✅ |
| VALUE58 | CorePrflValueDPEOValue58 | — |
| VALUE58 | HtsPrflValueDPEOValue58 | — |
| VALUE58 | MgrPrflValueDPEOValue58 | ✅ |
| VALUE58 | TcdPrflValueDPEOValue58 | — |
| VALUE58 | WkrPrflValueDPEOValue58 | ✅ |
| VALUE59 | CorePrflValueDPEOValue59 | — |
| VALUE59 | HtsPrflValueDPEOValue59 | — |
| VALUE59 | MgrPrflValueDPEOValue59 | ✅ |
| VALUE59 | TcdPrflValueDPEOValue59 | — |
| VALUE59 | WkrPrflValueDPEOValue59 | ✅ |
| VALUE6 | CorePrflValueDPEOValue6 | — |
| VALUE6 | HtsPrflValueDPEOValue6 | — |
| VALUE6 | MgrPrflValueDPEOValue6 | ✅ |
| VALUE6 | TcdPrflValueDPEOValue6 | — |
| VALUE6 | WkrPrflValueDPEOValue6 | ✅ |
| VALUE60 | CorePrflValueDPEOValue60 | — |
| VALUE60 | HtsPrflValueDPEOValue60 | — |
| VALUE60 | MgrPrflValueDPEOValue60 | — |
| VALUE60 | TcdPrflValueDPEOValue60 | — |
| VALUE60 | WkrPrflValueDPEOValue60 | — |
| VALUE61 | CorePrflValueDPEOValue61 | — |
| VALUE61 | HtsPrflValueDPEOValue61 | — |
| VALUE61 | MgrPrflValueDPEOValue61 | — |
| VALUE61 | TcdPrflValueDPEOValue61 | — |
| VALUE61 | WkrPrflValueDPEOValue61 | — |
| VALUE62 | CorePrflValueDPEOValue62 | — |
| VALUE62 | HtsPrflValueDPEOValue62 | — |
| VALUE62 | MgrPrflValueDPEOValue62 | ✅ |
| VALUE62 | TcdPrflValueDPEOValue62 | — |
| VALUE62 | WkrPrflValueDPEOValue62 | ✅ |
| VALUE63 | CorePrflValueDPEOValue63 | — |
| VALUE63 | HtsPrflValueDPEOValue63 | — |
| VALUE63 | MgrPrflValueDPEOValue63 | ✅ |
| VALUE63 | TcdPrflValueDPEOValue63 | — |
| VALUE63 | WkrPrflValueDPEOValue63 | ✅ |
| VALUE64 | CorePrflValueDPEOValue64 | — |
| VALUE64 | HtsPrflValueDPEOValue64 | — |
| VALUE64 | MgrPrflValueDPEOValue64 | ✅ |
| VALUE64 | TcdPrflValueDPEOValue64 | — |
| VALUE64 | WkrPrflValueDPEOValue64 | ✅ |
| VALUE65 | CorePrflValueDPEOValue65 | — |
| VALUE65 | HtsPrflValueDPEOValue65 | — |
| VALUE65 | MgrPrflValueDPEOValue65 | ✅ |
| VALUE65 | TcdPrflValueDPEOValue65 | — |
| VALUE65 | WkrPrflValueDPEOValue65 | ✅ |
| VALUE66 | CorePrflValueDPEOValue66 | — |
| VALUE66 | HtsPrflValueDPEOValue66 | — |
| VALUE66 | MgrPrflValueDPEOValue66 | ✅ |
| VALUE66 | TcdPrflValueDPEOValue66 | — |
| VALUE66 | WkrPrflValueDPEOValue66 | ✅ |
| VALUE67 | CorePrflValueDPEOValue67 | — |
| VALUE67 | HtsPrflValueDPEOValue67 | — |
| VALUE67 | MgrPrflValueDPEOValue67 | ✅ |
| VALUE67 | TcdPrflValueDPEOValue67 | — |
| VALUE67 | WkrPrflValueDPEOValue67 | ✅ |
| VALUE68 | CorePrflValueDPEOValue68 | — |
| VALUE68 | HtsPrflValueDPEOValue68 | — |
| VALUE68 | MgrPrflValueDPEOValue68 | ✅ |
| VALUE68 | TcdPrflValueDPEOValue68 | — |
| VALUE68 | WkrPrflValueDPEOValue68 | ✅ |
| VALUE69 | CorePrflValueDPEOValue69 | — |
| VALUE69 | HtsPrflValueDPEOValue69 | — |
| VALUE69 | MgrPrflValueDPEOValue69 | ✅ |
| VALUE69 | TcdPrflValueDPEOValue69 | — |
| VALUE69 | WkrPrflValueDPEOValue69 | ✅ |
| VALUE7 | CorePrflValueDPEOValue7 | — |
| VALUE7 | HtsPrflValueDPEOValue7 | — |
| VALUE7 | MgrPrflValueDPEOValue7 | ✅ |
| VALUE7 | TcdPrflValueDPEOValue7 | — |
| VALUE7 | WkrPrflValueDPEOValue7 | ✅ |
| VALUE70 | CorePrflValueDPEOValue70 | — |
| VALUE70 | HtsPrflValueDPEOValue70 | — |
| VALUE70 | MgrPrflValueDPEOValue70 | — |
| VALUE70 | TcdPrflValueDPEOValue70 | — |
| VALUE70 | WkrPrflValueDPEOValue70 | — |
| VALUE71 | CorePrflValueDPEOValue71 | — |
| VALUE71 | HtsPrflValueDPEOValue71 | — |
| VALUE71 | MgrPrflValueDPEOValue71 | — |
| VALUE71 | TcdPrflValueDPEOValue71 | — |
| VALUE71 | WkrPrflValueDPEOValue71 | — |
| VALUE72 | CorePrflValueDPEOValue72 | — |
| VALUE72 | HtsPrflValueDPEOValue72 | — |
| VALUE72 | MgrPrflValueDPEOValue72 | — |
| VALUE72 | TcdPrflValueDPEOValue72 | — |
| VALUE72 | WkrPrflValueDPEOValue72 | — |
| VALUE73 | CorePrflValueDPEOValue73 | — |
| VALUE73 | HtsPrflValueDPEOValue73 | — |
| VALUE73 | MgrPrflValueDPEOValue73 | — |
| VALUE73 | TcdPrflValueDPEOValue73 | — |
| VALUE73 | WkrPrflValueDPEOValue73 | — |
| VALUE74 | CorePrflValueDPEOValue74 | — |
| VALUE74 | HtsPrflValueDPEOValue74 | — |
| VALUE74 | MgrPrflValueDPEOValue74 | — |
| VALUE74 | TcdPrflValueDPEOValue74 | — |
| VALUE74 | WkrPrflValueDPEOValue74 | — |
| VALUE75 | CorePrflValueDPEOValue75 | — |
| VALUE75 | HtsPrflValueDPEOValue75 | — |
| VALUE75 | MgrPrflValueDPEOValue75 | — |
| VALUE75 | TcdPrflValueDPEOValue75 | — |
| VALUE75 | WkrPrflValueDPEOValue75 | — |
| VALUE76 | CorePrflValueDPEOValue76 | — |
| VALUE76 | HtsPrflValueDPEOValue76 | — |
| VALUE76 | MgrPrflValueDPEOValue76 | — |
| VALUE76 | TcdPrflValueDPEOValue76 | — |
| VALUE76 | WkrPrflValueDPEOValue76 | — |
| VALUE77 | CorePrflValueDPEOValue77 | — |
| VALUE77 | HtsPrflValueDPEOValue77 | — |
| VALUE77 | MgrPrflValueDPEOValue77 | — |
| VALUE77 | TcdPrflValueDPEOValue77 | — |
| VALUE77 | WkrPrflValueDPEOValue77 | — |
| VALUE78 | CorePrflValueDPEOValue78 | — |
| VALUE78 | HtsPrflValueDPEOValue78 | — |
| VALUE78 | MgrPrflValueDPEOValue78 | — |
| VALUE78 | TcdPrflValueDPEOValue78 | — |
| VALUE78 | WkrPrflValueDPEOValue78 | — |
| VALUE79 | CorePrflValueDPEOValue79 | — |
| VALUE79 | HtsPrflValueDPEOValue79 | — |
| VALUE79 | MgrPrflValueDPEOValue79 | — |
| VALUE79 | TcdPrflValueDPEOValue79 | — |
| VALUE79 | WkrPrflValueDPEOValue79 | — |
| VALUE8 | CorePrflValueDPEOValue8 | — |
| VALUE8 | HtsPrflValueDPEOValue8 | — |
| VALUE8 | MgrPrflValueDPEOValue8 | ✅ |
| VALUE8 | TcdPrflValueDPEOValue8 | — |
| VALUE8 | WkrPrflValueDPEOValue8 | ✅ |
| VALUE9 | CorePrflValueDPEOValue9 | — |
| VALUE9 | HtsPrflValueDPEOValue9 | — |
| VALUE9 | MgrPrflValueDPEOValue9 | — |
| VALUE9 | TcdPrflValueDPEOValue9 | — |
| VALUE9 | WkrPrflValueDPEOValue9 | — |

### [[setupprofilepvo|SetupProfilePVO]] (GL · BICC: 147/475)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CorePrflValueDPEOCreatedBy | — |
| CREATED_BY | HtsPrflValueDPEOCreatedBy | — |
| CREATED_BY | MgrPrflValueDPEOCreatedBy | — |
| CREATED_BY | TcdPrflValueDPEOCreatedBy | — |
| CREATED_BY | WkrPrflValueDPEOCreatedBy | — |
| CREATION_DATE | CorePrflValueDPEOCreationDate | — |
| CREATION_DATE | HtsPrflValueDPEOCreationDate | — |
| CREATION_DATE | MgrPrflValueDPEOCreationDate | — |
| CREATION_DATE | TcdPrflValueDPEOCreationDate | — |
| CREATION_DATE | WkrPrflValueDPEOCreationDate | — |
| EFFECTIVE_END_DATE | CorePrflValueDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | HtsPrflValueDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | MgrPrflValueDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | TcdPrflValueDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | WkrPrflValueDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | CorePrflValueDPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | HtsPrflValueDPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | MgrPrflValueDPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | TcdPrflValueDPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | WkrPrflValueDPEOEffectiveStartDate | ✅ |
| ENTERPRISE_ID | CorePrflValueDPEOEnterpriseId | — |
| ENTERPRISE_ID | HtsPrflValueDPEOEnterpriseId | — |
| ENTERPRISE_ID | MgrPrflValueDPEOEnterpriseId | — |
| ENTERPRISE_ID | TcdPrflValueDPEOEnterpriseId | — |
| ENTERPRISE_ID | WkrPrflValueDPEOEnterpriseId | — |
| LAST_UPDATE_DATE | CorePrflValueDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | HtsPrflValueDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | MgrPrflValueDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TcdPrflValueDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | WkrPrflValueDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CorePrflValueDPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | HtsPrflValueDPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | MgrPrflValueDPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TcdPrflValueDPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | WkrPrflValueDPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CorePrflValueDPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | HtsPrflValueDPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | MgrPrflValueDPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | TcdPrflValueDPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | WkrPrflValueDPEOLastUpdatedBy | — |
| MODULE_ID | CorePrflValueDPEOModuleId | — |
| MODULE_ID | HtsPrflValueDPEOModuleId | — |
| MODULE_ID | MgrPrflValueDPEOModuleId | — |
| MODULE_ID | TcdPrflValueDPEOModuleId | — |
| MODULE_ID | WkrPrflValueDPEOModuleId | — |
| OBJECT_VERSION_NUMBER | CorePrflValueDPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | HtsPrflValueDPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | MgrPrflValueDPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TcdPrflValueDPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | WkrPrflValueDPEOObjectVersionNumber | — |
| SEED_DATA_SOURCE | CorePrflValueDPEOSeedDataSource | — |
| SEED_DATA_SOURCE | HtsPrflValueDPEOSeedDataSource | — |
| SEED_DATA_SOURCE | MgrPrflValueDPEOSeedDataSource | — |
| SEED_DATA_SOURCE | TcdPrflValueDPEOSeedDataSource | — |
| SEED_DATA_SOURCE | WkrPrflValueDPEOSeedDataSource | — |
| SETUP_OPTION_VAL_CD | CorePrflValueDPEOSetupOptionValCd | ✅ |
| SETUP_OPTION_VAL_CD | HtsPrflValueDPEOSetupOptionValCd | ✅ |
| SETUP_OPTION_VAL_CD | MgrPrflValueDPEOSetupOptionValCd | ✅ |
| SETUP_OPTION_VAL_CD | TcdPrflValueDPEOSetupOptionValCd | ✅ |
| SETUP_OPTION_VAL_CD | WkrPrflValueDPEOSetupOptionValCd | ✅ |
| SETUP_OPTION_VAL_ID | CorePrflValueDPEOSetupOptionValId | ✅ |
| SETUP_OPTION_VAL_ID | HtsPrflValueDPEOSetupOptionValId | ✅ |
| SETUP_OPTION_VAL_ID | MgrPrflValueDPEOSetupOptionValId | ✅ |
| SETUP_OPTION_VAL_ID | TcdPrflValueDPEOSetupOptionValId | ✅ |
| SETUP_OPTION_VAL_ID | WkrPrflValueDPEOSetupOptionValId | ✅ |
| SETUP_PROFILE_ID | CorePrflValueDPEOSetupProfileId | — |
| SETUP_PROFILE_ID | HtsPrflValueDPEOSetupProfileId | — |
| SETUP_PROFILE_ID | MgrPrflValueDPEOSetupProfileId | — |
| SETUP_PROFILE_ID | TcdPrflValueDPEOSetupProfileId | — |
| SETUP_PROFILE_ID | WkrPrflValueDPEOSetupProfileId | — |
| SGUID | CorePrflValueDPEOSguid | — |
| SGUID | HtsPrflValueDPEOSguid | — |
| SGUID | MgrPrflValueDPEOSguid | — |
| SGUID | TcdPrflValueDPEOSguid | — |
| SGUID | WkrPrflValueDPEOSguid | — |
| TYPE | CorePrflValueDPEOType | — |
| TYPE | HtsPrflValueDPEOType | — |
| TYPE | MgrPrflValueDPEOType | — |
| TYPE | TcdPrflValueDPEOType | — |
| TYPE | WkrPrflValueDPEOType | — |
| VALUE1 | CorePrflValueDPEOValue1 | — |
| VALUE1 | HtsPrflValueDPEOValue1 | — |
| VALUE1 | MgrPrflValueDPEOValue1 | ✅ |
| VALUE1 | TcdPrflValueDPEOValue1 | — |
| VALUE1 | WkrPrflValueDPEOValue1 | ✅ |
| VALUE10 | CorePrflValueDPEOValue10 | — |
| VALUE10 | HtsPrflValueDPEOValue10 | — |
| VALUE10 | MgrPrflValueDPEOValue10 | ✅ |
| VALUE10 | TcdPrflValueDPEOValue10 | ✅ |
| VALUE10 | WkrPrflValueDPEOValue10 | ✅ |
| VALUE11 | CorePrflValueDPEOValue11 | — |
| VALUE11 | HtsPrflValueDPEOValue11 | ✅ |
| VALUE11 | MgrPrflValueDPEOValue11 | ✅ |
| VALUE11 | TcdPrflValueDPEOValue11 | — |
| VALUE11 | WkrPrflValueDPEOValue11 | ✅ |
| VALUE12 | CorePrflValueDPEOValue12 | — |
| VALUE12 | HtsPrflValueDPEOValue12 | ✅ |
| VALUE12 | MgrPrflValueDPEOValue12 | ✅ |
| VALUE12 | TcdPrflValueDPEOValue12 | — |
| VALUE12 | WkrPrflValueDPEOValue12 | ✅ |
| VALUE13 | CorePrflValueDPEOValue13 | — |
| VALUE13 | HtsPrflValueDPEOValue13 | — |
| VALUE13 | MgrPrflValueDPEOValue13 | ✅ |
| VALUE13 | TcdPrflValueDPEOValue13 | — |
| VALUE13 | WkrPrflValueDPEOValue13 | ✅ |
| VALUE14 | CorePrflValueDPEOValue14 | — |
| VALUE14 | HtsPrflValueDPEOValue14 | ✅ |
| VALUE14 | MgrPrflValueDPEOValue14 | ✅ |
| VALUE14 | TcdPrflValueDPEOValue14 | — |
| VALUE14 | WkrPrflValueDPEOValue14 | ✅ |
| VALUE15 | CorePrflValueDPEOValue15 | — |
| VALUE15 | HtsPrflValueDPEOValue15 | ✅ |
| VALUE15 | MgrPrflValueDPEOValue15 | — |
| VALUE15 | TcdPrflValueDPEOValue15 | — |
| VALUE15 | WkrPrflValueDPEOValue15 | — |
| VALUE16 | CorePrflValueDPEOValue16 | — |
| VALUE16 | HtsPrflValueDPEOValue16 | ✅ |
| VALUE16 | MgrPrflValueDPEOValue16 | ✅ |
| VALUE16 | TcdPrflValueDPEOValue16 | — |
| VALUE16 | WkrPrflValueDPEOValue16 | ✅ |
| VALUE17 | CorePrflValueDPEOValue17 | — |
| VALUE17 | HtsPrflValueDPEOValue17 | ✅ |
| VALUE17 | MgrPrflValueDPEOValue17 | ✅ |
| VALUE17 | TcdPrflValueDPEOValue17 | — |
| VALUE17 | WkrPrflValueDPEOValue17 | ✅ |
| VALUE18 | CorePrflValueDPEOValue18 | — |
| VALUE18 | HtsPrflValueDPEOValue18 | — |
| VALUE18 | MgrPrflValueDPEOValue18 | ✅ |
| VALUE18 | TcdPrflValueDPEOValue18 | — |
| VALUE18 | WkrPrflValueDPEOValue18 | ✅ |
| VALUE19 | CorePrflValueDPEOValue19 | — |
| VALUE19 | HtsPrflValueDPEOValue19 | — |
| VALUE19 | MgrPrflValueDPEOValue19 | ✅ |
| VALUE19 | TcdPrflValueDPEOValue19 | — |
| VALUE19 | WkrPrflValueDPEOValue19 | ✅ |
| VALUE2 | CorePrflValueDPEOValue2 | — |
| VALUE2 | HtsPrflValueDPEOValue2 | — |
| VALUE2 | MgrPrflValueDPEOValue2 | ✅ |
| VALUE2 | TcdPrflValueDPEOValue2 | — |
| VALUE2 | WkrPrflValueDPEOValue2 | ✅ |
| VALUE20 | CorePrflValueDPEOValue20 | — |
| VALUE20 | HtsPrflValueDPEOValue20 | — |
| VALUE20 | MgrPrflValueDPEOValue20 | ✅ |
| VALUE20 | TcdPrflValueDPEOValue20 | — |
| VALUE20 | WkrPrflValueDPEOValue20 | ✅ |
| VALUE21 | CorePrflValueDPEOValue21 | — |
| VALUE21 | HtsPrflValueDPEOValue21 | — |
| VALUE21 | MgrPrflValueDPEOValue21 | — |
| VALUE21 | TcdPrflValueDPEOValue21 | — |
| VALUE21 | WkrPrflValueDPEOValue21 | — |
| VALUE22 | CorePrflValueDPEOValue22 | — |
| VALUE22 | HtsPrflValueDPEOValue22 | — |
| VALUE22 | MgrPrflValueDPEOValue22 | — |
| VALUE22 | TcdPrflValueDPEOValue22 | — |
| VALUE22 | WkrPrflValueDPEOValue22 | — |
| VALUE23 | CorePrflValueDPEOValue23 | — |
| VALUE23 | HtsPrflValueDPEOValue23 | — |
| VALUE23 | MgrPrflValueDPEOValue23 | — |
| VALUE23 | TcdPrflValueDPEOValue23 | — |
| VALUE23 | WkrPrflValueDPEOValue23 | — |
| VALUE24 | CorePrflValueDPEOValue24 | — |
| VALUE24 | HtsPrflValueDPEOValue24 | — |
| VALUE24 | MgrPrflValueDPEOValue24 | — |
| VALUE24 | TcdPrflValueDPEOValue24 | — |
| VALUE24 | WkrPrflValueDPEOValue24 | — |
| VALUE25 | CorePrflValueDPEOValue25 | — |
| VALUE25 | HtsPrflValueDPEOValue25 | — |
| VALUE25 | MgrPrflValueDPEOValue25 | — |
| VALUE25 | TcdPrflValueDPEOValue25 | — |
| VALUE25 | WkrPrflValueDPEOValue25 | — |
| VALUE26 | CorePrflValueDPEOValue26 | — |
| VALUE26 | HtsPrflValueDPEOValue26 | — |
| VALUE26 | MgrPrflValueDPEOValue26 | — |
| VALUE26 | TcdPrflValueDPEOValue26 | — |
| VALUE26 | WkrPrflValueDPEOValue26 | — |
| VALUE27 | CorePrflValueDPEOValue27 | — |
| VALUE27 | HtsPrflValueDPEOValue27 | — |
| VALUE27 | MgrPrflValueDPEOValue27 | — |
| VALUE27 | TcdPrflValueDPEOValue27 | — |
| VALUE27 | WkrPrflValueDPEOValue27 | — |
| VALUE28 | CorePrflValueDPEOValue28 | — |
| VALUE28 | HtsPrflValueDPEOValue28 | — |
| VALUE28 | MgrPrflValueDPEOValue28 | — |
| VALUE28 | TcdPrflValueDPEOValue28 | — |
| VALUE28 | WkrPrflValueDPEOValue28 | — |
| VALUE29 | CorePrflValueDPEOValue29 | — |
| VALUE29 | HtsPrflValueDPEOValue29 | — |
| VALUE29 | MgrPrflValueDPEOValue29 | — |
| VALUE29 | TcdPrflValueDPEOValue29 | — |
| VALUE29 | WkrPrflValueDPEOValue29 | — |
| VALUE3 | CorePrflValueDPEOValue3 | — |
| VALUE3 | HtsPrflValueDPEOValue3 | — |
| VALUE3 | MgrPrflValueDPEOValue3 | — |
| VALUE3 | TcdPrflValueDPEOValue3 | — |
| VALUE3 | WkrPrflValueDPEOValue3 | — |
| VALUE30 | CorePrflValueDPEOValue30 | ✅ |
| VALUE30 | HtsPrflValueDPEOValue30 | — |
| VALUE30 | MgrPrflValueDPEOValue30 | ✅ |
| VALUE30 | TcdPrflValueDPEOValue30 | ✅ |
| VALUE30 | WkrPrflValueDPEOValue30 | ✅ |
| VALUE31 | CorePrflValueDPEOValue31 | ✅ |
| VALUE31 | HtsPrflValueDPEOValue31 | — |
| VALUE31 | MgrPrflValueDPEOValue31 | — |
| VALUE31 | TcdPrflValueDPEOValue31 | ✅ |
| VALUE31 | WkrPrflValueDPEOValue31 | — |
| VALUE32 | CorePrflValueDPEOValue32 | ✅ |
| VALUE32 | HtsPrflValueDPEOValue32 | — |
| VALUE32 | MgrPrflValueDPEOValue32 | ✅ |
| VALUE32 | TcdPrflValueDPEOValue32 | ✅ |
| VALUE32 | WkrPrflValueDPEOValue32 | ✅ |
| VALUE33 | CorePrflValueDPEOValue33 | ✅ |
| VALUE33 | HtsPrflValueDPEOValue33 | — |
| VALUE33 | MgrPrflValueDPEOValue33 | ✅ |
| VALUE33 | TcdPrflValueDPEOValue33 | ✅ |
| VALUE33 | WkrPrflValueDPEOValue33 | ✅ |
| VALUE34 | CorePrflValueDPEOValue34 | ✅ |
| VALUE34 | HtsPrflValueDPEOValue34 | — |
| VALUE34 | MgrPrflValueDPEOValue34 | ✅ |
| VALUE34 | TcdPrflValueDPEOValue34 | — |
| VALUE34 | WkrPrflValueDPEOValue34 | ✅ |
| VALUE35 | CorePrflValueDPEOValue35 | — |
| VALUE35 | HtsPrflValueDPEOValue35 | — |
| VALUE35 | MgrPrflValueDPEOValue35 | ✅ |
| VALUE35 | TcdPrflValueDPEOValue35 | — |
| VALUE35 | WkrPrflValueDPEOValue35 | ✅ |
| VALUE36 | CorePrflValueDPEOValue36 | — |
| VALUE36 | HtsPrflValueDPEOValue36 | — |
| VALUE36 | MgrPrflValueDPEOValue36 | — |
| VALUE36 | TcdPrflValueDPEOValue36 | — |
| VALUE36 | WkrPrflValueDPEOValue36 | — |
| VALUE37 | CorePrflValueDPEOValue37 | — |
| VALUE37 | HtsPrflValueDPEOValue37 | — |
| VALUE37 | MgrPrflValueDPEOValue37 | — |
| VALUE37 | TcdPrflValueDPEOValue37 | — |
| VALUE37 | WkrPrflValueDPEOValue37 | — |
| VALUE38 | CorePrflValueDPEOValue38 | — |
| VALUE38 | HtsPrflValueDPEOValue38 | — |
| VALUE38 | MgrPrflValueDPEOValue38 | ✅ |
| VALUE38 | TcdPrflValueDPEOValue38 | — |
| VALUE38 | WkrPrflValueDPEOValue38 | ✅ |
| VALUE39 | CorePrflValueDPEOValue39 | — |
| VALUE39 | HtsPrflValueDPEOValue39 | — |
| VALUE39 | MgrPrflValueDPEOValue39 | ✅ |
| VALUE39 | TcdPrflValueDPEOValue39 | — |
| VALUE39 | WkrPrflValueDPEOValue39 | ✅ |
| VALUE4 | CorePrflValueDPEOValue4 | — |
| VALUE4 | HtsPrflValueDPEOValue4 | — |
| VALUE4 | MgrPrflValueDPEOValue4 | ✅ |
| VALUE4 | TcdPrflValueDPEOValue4 | — |
| VALUE4 | WkrPrflValueDPEOValue4 | ✅ |
| VALUE40 | CorePrflValueDPEOValue40 | — |
| VALUE40 | HtsPrflValueDPEOValue40 | — |
| VALUE40 | MgrPrflValueDPEOValue40 | ✅ |
| VALUE40 | TcdPrflValueDPEOValue40 | — |
| VALUE40 | WkrPrflValueDPEOValue40 | ✅ |
| VALUE41 | CorePrflValueDPEOValue41 | — |
| VALUE41 | HtsPrflValueDPEOValue41 | — |
| VALUE41 | MgrPrflValueDPEOValue41 | ✅ |
| VALUE41 | TcdPrflValueDPEOValue41 | — |
| VALUE41 | WkrPrflValueDPEOValue41 | ✅ |
| VALUE42 | CorePrflValueDPEOValue42 | — |
| VALUE42 | HtsPrflValueDPEOValue42 | — |
| VALUE42 | MgrPrflValueDPEOValue42 | ✅ |
| VALUE42 | TcdPrflValueDPEOValue42 | — |
| VALUE42 | WkrPrflValueDPEOValue42 | ✅ |
| VALUE43 | CorePrflValueDPEOValue43 | — |
| VALUE43 | HtsPrflValueDPEOValue43 | — |
| VALUE43 | MgrPrflValueDPEOValue43 | ✅ |
| VALUE43 | TcdPrflValueDPEOValue43 | — |
| VALUE43 | WkrPrflValueDPEOValue43 | ✅ |
| VALUE44 | CorePrflValueDPEOValue44 | — |
| VALUE44 | HtsPrflValueDPEOValue44 | — |
| VALUE44 | MgrPrflValueDPEOValue44 | ✅ |
| VALUE44 | TcdPrflValueDPEOValue44 | — |
| VALUE44 | WkrPrflValueDPEOValue44 | ✅ |
| VALUE45 | CorePrflValueDPEOValue45 | — |
| VALUE45 | HtsPrflValueDPEOValue45 | — |
| VALUE45 | MgrPrflValueDPEOValue45 | ✅ |
| VALUE45 | TcdPrflValueDPEOValue45 | — |
| VALUE45 | WkrPrflValueDPEOValue45 | ✅ |
| VALUE46 | CorePrflValueDPEOValue46 | — |
| VALUE46 | HtsPrflValueDPEOValue46 | — |
| VALUE46 | MgrPrflValueDPEOValue46 | ✅ |
| VALUE46 | TcdPrflValueDPEOValue46 | — |
| VALUE46 | WkrPrflValueDPEOValue46 | ✅ |
| VALUE47 | CorePrflValueDPEOValue47 | — |
| VALUE47 | HtsPrflValueDPEOValue47 | — |
| VALUE47 | MgrPrflValueDPEOValue47 | ✅ |
| VALUE47 | TcdPrflValueDPEOValue47 | — |
| VALUE47 | WkrPrflValueDPEOValue47 | ✅ |
| VALUE48 | CorePrflValueDPEOValue48 | — |
| VALUE48 | HtsPrflValueDPEOValue48 | — |
| VALUE48 | MgrPrflValueDPEOValue48 | — |
| VALUE48 | TcdPrflValueDPEOValue48 | — |
| VALUE48 | WkrPrflValueDPEOValue48 | — |
| VALUE49 | CorePrflValueDPEOValue49 | — |
| VALUE49 | HtsPrflValueDPEOValue49 | — |
| VALUE49 | MgrPrflValueDPEOValue49 | — |
| VALUE49 | TcdPrflValueDPEOValue49 | — |
| VALUE49 | WkrPrflValueDPEOValue49 | — |
| VALUE5 | CorePrflValueDPEOValue5 | — |
| VALUE5 | HtsPrflValueDPEOValue5 | — |
| VALUE5 | MgrPrflValueDPEOValue5 | ✅ |
| VALUE5 | TcdPrflValueDPEOValue5 | — |
| VALUE5 | WkrPrflValueDPEOValue5 | ✅ |
| VALUE50 | CorePrflValueDPEOValue50 | — |
| VALUE50 | HtsPrflValueDPEOValue50 | ✅ |
| VALUE50 | MgrPrflValueDPEOValue50 | ✅ |
| VALUE50 | TcdPrflValueDPEOValue50 | — |
| VALUE50 | WkrPrflValueDPEOValue50 | ✅ |
| VALUE51 | CorePrflValueDPEOValue51 | — |
| VALUE51 | HtsPrflValueDPEOValue51 | ✅ |
| VALUE51 | MgrPrflValueDPEOValue51 | ✅ |
| VALUE51 | TcdPrflValueDPEOValue51 | — |
| VALUE51 | WkrPrflValueDPEOValue51 | ✅ |
| VALUE52 | CorePrflValueDPEOValue52 | — |
| VALUE52 | HtsPrflValueDPEOValue52 | ✅ |
| VALUE52 | MgrPrflValueDPEOValue52 | ✅ |
| VALUE52 | TcdPrflValueDPEOValue52 | — |
| VALUE52 | WkrPrflValueDPEOValue52 | ✅ |
| VALUE53 | CorePrflValueDPEOValue53 | — |
| VALUE53 | HtsPrflValueDPEOValue53 | ✅ |
| VALUE53 | MgrPrflValueDPEOValue53 | ✅ |
| VALUE53 | TcdPrflValueDPEOValue53 | — |
| VALUE53 | WkrPrflValueDPEOValue53 | ✅ |
| VALUE54 | CorePrflValueDPEOValue54 | — |
| VALUE54 | HtsPrflValueDPEOValue54 | ✅ |
| VALUE54 | MgrPrflValueDPEOValue54 | ✅ |
| VALUE54 | TcdPrflValueDPEOValue54 | — |
| VALUE54 | WkrPrflValueDPEOValue54 | ✅ |
| VALUE55 | CorePrflValueDPEOValue55 | — |
| VALUE55 | HtsPrflValueDPEOValue55 | ✅ |
| VALUE55 | MgrPrflValueDPEOValue55 | ✅ |
| VALUE55 | TcdPrflValueDPEOValue55 | — |
| VALUE55 | WkrPrflValueDPEOValue55 | ✅ |
| VALUE56 | CorePrflValueDPEOValue56 | — |
| VALUE56 | HtsPrflValueDPEOValue56 | — |
| VALUE56 | MgrPrflValueDPEOValue56 | ✅ |
| VALUE56 | TcdPrflValueDPEOValue56 | — |
| VALUE56 | WkrPrflValueDPEOValue56 | ✅ |
| VALUE57 | CorePrflValueDPEOValue57 | — |
| VALUE57 | HtsPrflValueDPEOValue57 | — |
| VALUE57 | MgrPrflValueDPEOValue57 | ✅ |
| VALUE57 | TcdPrflValueDPEOValue57 | — |
| VALUE57 | WkrPrflValueDPEOValue57 | ✅ |
| VALUE58 | CorePrflValueDPEOValue58 | — |
| VALUE58 | HtsPrflValueDPEOValue58 | — |
| VALUE58 | MgrPrflValueDPEOValue58 | ✅ |
| VALUE58 | TcdPrflValueDPEOValue58 | — |
| VALUE58 | WkrPrflValueDPEOValue58 | ✅ |
| VALUE59 | CorePrflValueDPEOValue59 | — |
| VALUE59 | HtsPrflValueDPEOValue59 | — |
| VALUE59 | MgrPrflValueDPEOValue59 | ✅ |
| VALUE59 | TcdPrflValueDPEOValue59 | — |
| VALUE59 | WkrPrflValueDPEOValue59 | ✅ |
| VALUE6 | CorePrflValueDPEOValue6 | — |
| VALUE6 | HtsPrflValueDPEOValue6 | — |
| VALUE6 | MgrPrflValueDPEOValue6 | ✅ |
| VALUE6 | TcdPrflValueDPEOValue6 | — |
| VALUE6 | WkrPrflValueDPEOValue6 | ✅ |
| VALUE60 | CorePrflValueDPEOValue60 | — |
| VALUE60 | HtsPrflValueDPEOValue60 | — |
| VALUE60 | MgrPrflValueDPEOValue60 | — |
| VALUE60 | TcdPrflValueDPEOValue60 | — |
| VALUE60 | WkrPrflValueDPEOValue60 | — |
| VALUE61 | CorePrflValueDPEOValue61 | — |
| VALUE61 | HtsPrflValueDPEOValue61 | — |
| VALUE61 | MgrPrflValueDPEOValue61 | — |
| VALUE61 | TcdPrflValueDPEOValue61 | — |
| VALUE61 | WkrPrflValueDPEOValue61 | — |
| VALUE62 | CorePrflValueDPEOValue62 | — |
| VALUE62 | HtsPrflValueDPEOValue62 | — |
| VALUE62 | MgrPrflValueDPEOValue62 | ✅ |
| VALUE62 | TcdPrflValueDPEOValue62 | — |
| VALUE62 | WkrPrflValueDPEOValue62 | ✅ |
| VALUE63 | CorePrflValueDPEOValue63 | — |
| VALUE63 | HtsPrflValueDPEOValue63 | — |
| VALUE63 | MgrPrflValueDPEOValue63 | ✅ |
| VALUE63 | TcdPrflValueDPEOValue63 | — |
| VALUE63 | WkrPrflValueDPEOValue63 | ✅ |
| VALUE64 | CorePrflValueDPEOValue64 | — |
| VALUE64 | HtsPrflValueDPEOValue64 | — |
| VALUE64 | MgrPrflValueDPEOValue64 | ✅ |
| VALUE64 | TcdPrflValueDPEOValue64 | — |
| VALUE64 | WkrPrflValueDPEOValue64 | ✅ |
| VALUE65 | CorePrflValueDPEOValue65 | — |
| VALUE65 | HtsPrflValueDPEOValue65 | — |
| VALUE65 | MgrPrflValueDPEOValue65 | ✅ |
| VALUE65 | TcdPrflValueDPEOValue65 | — |
| VALUE65 | WkrPrflValueDPEOValue65 | ✅ |
| VALUE66 | CorePrflValueDPEOValue66 | — |
| VALUE66 | HtsPrflValueDPEOValue66 | — |
| VALUE66 | MgrPrflValueDPEOValue66 | ✅ |
| VALUE66 | TcdPrflValueDPEOValue66 | — |
| VALUE66 | WkrPrflValueDPEOValue66 | ✅ |
| VALUE67 | CorePrflValueDPEOValue67 | — |
| VALUE67 | HtsPrflValueDPEOValue67 | — |
| VALUE67 | MgrPrflValueDPEOValue67 | ✅ |
| VALUE67 | TcdPrflValueDPEOValue67 | — |
| VALUE67 | WkrPrflValueDPEOValue67 | ✅ |
| VALUE68 | CorePrflValueDPEOValue68 | — |
| VALUE68 | HtsPrflValueDPEOValue68 | — |
| VALUE68 | MgrPrflValueDPEOValue68 | ✅ |
| VALUE68 | TcdPrflValueDPEOValue68 | — |
| VALUE68 | WkrPrflValueDPEOValue68 | ✅ |
| VALUE69 | CorePrflValueDPEOValue69 | — |
| VALUE69 | HtsPrflValueDPEOValue69 | — |
| VALUE69 | MgrPrflValueDPEOValue69 | ✅ |
| VALUE69 | TcdPrflValueDPEOValue69 | — |
| VALUE69 | WkrPrflValueDPEOValue69 | ✅ |
| VALUE7 | CorePrflValueDPEOValue7 | — |
| VALUE7 | HtsPrflValueDPEOValue7 | — |
| VALUE7 | MgrPrflValueDPEOValue7 | ✅ |
| VALUE7 | TcdPrflValueDPEOValue7 | — |
| VALUE7 | WkrPrflValueDPEOValue7 | ✅ |
| VALUE70 | CorePrflValueDPEOValue70 | — |
| VALUE70 | HtsPrflValueDPEOValue70 | — |
| VALUE70 | MgrPrflValueDPEOValue70 | — |
| VALUE70 | TcdPrflValueDPEOValue70 | — |
| VALUE70 | WkrPrflValueDPEOValue70 | — |
| VALUE71 | CorePrflValueDPEOValue71 | — |
| VALUE71 | HtsPrflValueDPEOalue71 | — |
| VALUE71 | MgrPrflValueDPEOValue71 | — |
| VALUE71 | TcdPrflValueDPEOValue71 | — |
| VALUE71 | WkrPrflValueDPEOValue71 | — |
| VALUE72 | CorePrflValueDPEOValue72 | — |
| VALUE72 | HtsPrflValueDPEOValue72 | — |
| VALUE72 | MgrPrflValueDPEOValue72 | — |
| VALUE72 | TcdPrflValueDPEOValue72 | — |
| VALUE72 | WkrPrflValueDPEOValue72 | — |
| VALUE73 | CorePrflValueDPEOValue73 | — |
| VALUE73 | HtsPrflValueDPEOValue73 | — |
| VALUE73 | MgrPrflValueDPEOValue73 | — |
| VALUE73 | TcdPrflValueDPEOValue73 | — |
| VALUE73 | WkrPrflValueDPEOValue73 | — |
| VALUE74 | CorePrflValueDPEOValue74 | — |
| VALUE74 | HtsPrflValueDPEOValue74 | — |
| VALUE74 | MgrPrflValueDPEOValue74 | — |
| VALUE74 | TcdPrflValueDPEOValue74 | — |
| VALUE74 | WkrPrflValueDPEOValue74 | — |
| VALUE75 | CorePrflValueDPEOValue75 | — |
| VALUE75 | HtsPrflValueDPEOValue75 | — |
| VALUE75 | MgrPrflValueDPEOValue75 | — |
| VALUE75 | TcdPrflValueDPEOValue75 | — |
| VALUE75 | WkrPrflValueDPEOValue75 | — |
| VALUE76 | CorePrflValueDPEOValue76 | — |
| VALUE76 | HtsPrflValueDPEOValue76 | — |
| VALUE76 | MgrPrflValueDPEOValue76 | — |
| VALUE76 | TcdPrflValueDPEOValue76 | — |
| VALUE76 | WkrPrflValueDPEOValue76 | — |
| VALUE77 | CorePrflValueDPEOValue77 | — |
| VALUE77 | HtsPrflValueDPEOValue77 | — |
| VALUE77 | MgrPrflValueDPEOValue77 | — |
| VALUE77 | TcdPrflValueDPEOValue77 | — |
| VALUE77 | WkrPrflValueDPEOValue77 | — |
| VALUE78 | CorePrflValueDPEOValue78 | — |
| VALUE78 | HtsPrflValueDPEOValue78 | — |
| VALUE78 | MgrPrflValueDPEOValue78 | — |
| VALUE78 | TcdPrflValueDPEOValue78 | — |
| VALUE78 | WkrPrflValueDPEOValue78 | — |
| VALUE79 | CorePrflValueDPEOValue79 | — |
| VALUE79 | HtsPrflValueDPEOValue79 | — |
| VALUE79 | MgrPrflValueDPEOValue79 | — |
| VALUE79 | TcdPrflValueDPEOValue79 | — |
| VALUE79 | WkrPrflValueDPEOValue79 | — |
| VALUE8 | CorePrflValueDPEOValue8 | — |
| VALUE8 | HtsPrflValueDPEOValue8 | — |
| VALUE8 | MgrPrflValueDPEOValue8 | ✅ |
| VALUE8 | TcdPrflValueDPEOValue8 | — |
| VALUE8 | WkrPrflValueDPEOValue8 | ✅ |
| VALUE9 | CorePrflValueDPEOValue9 | — |
| VALUE9 | HtsPrflValueDPEOValue9 | — |
| VALUE9 | MgrPrflValueDPEOValue9 | — |
| VALUE9 | TcdPrflValueDPEOValue9 | — |
| VALUE9 | WkrPrflValueDPEOValue9 | — |
