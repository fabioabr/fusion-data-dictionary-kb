---
id: DOC-HCM-131
doc_type: system-doc
title: "HMO_MODEL_PLANS_TL — Planos de Modelo Organizacional (Tradução)"
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
  - workforce-modeling
  - modelo-organizacional
  - traducao
  - hmo
aliases:
  - HMO_MODEL_PLANS_TL
  - hmo_model_plans_tl
  - hmo-model-plans-tl
  - DOC-HCM-131
  - planos-de-modelo-organizacional-(tradução)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HMO_MODEL_PLANS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes e descrições dos planos de modelo organizacional. Tabela _TL que complementa `HMO_MODEL_PLANS_B`.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Multilinguismo:** Nomes de planos de modelo em múltiplos idiomas.
- **Interface localizada:** Exibição traduzida na UI.
- **Relatórios:** Nomes traduzidos em relatórios.
- **Integração:** Base para views _VL.
- **Governança:** Controle de traduções.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MODEL_PLAN_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do plano | [[hmo_model_plans_b]] | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 95% |
| 4 | MODEL_PLAN_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome do plano no idioma | — | 🟡 80% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição no idioma | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hmo_model_plans_b]] — via `MODEL_PLAN_ID` (registro base do cadastro)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Nome do plano em português
```sql
SELECT tl.MODEL_PLAN_NAME, tl.DESCRIPTION
FROM   HMO_MODEL_PLANS_TL tl
WHERE  tl.MODEL_PLAN_ID = :p_plan_id
  AND  tl.LANGUAGE = 'PTBR';
```

### Planos com tradução
```sql
SELECT b.MODEL_PLAN_CODE, tl.MODEL_PLAN_NAME
FROM   HMO_MODEL_PLANS_B b
JOIN   HMO_MODEL_PLANS_TL tl ON b.MODEL_PLAN_ID = tl.MODEL_PLAN_ID
WHERE  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Chave primária composta: `MODEL_PLAN_ID` + `LANGUAGE`.
- Padrão Oracle _TL: um registro por idioma instalado.
- O `SOURCE_LANG` indica o idioma original.
- Para consultas na UI, utilizar views _VL.

---

## 🔗 PVOs Relacionados

### [[modelplanpvo|ModelPlanPVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ModelPlanTranslationPEOCreatedBy | — |
| CREATION_DATE | ModelPlanTranslationPEOCreationDate | — |
| DESCRIPTION | ModelPlanTranslationPEODescription | ✅ |
| ENTERPRISE_ID | ModelPlanTranslationPEOEnterpriseId | — |
| LANGUAGE | ModelPlanTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ModelPlanTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ModelPlanTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ModelPlanTranslationPEOLastUpdatedBy | — |
| MODEL_PLAN_ID | ModelPlanTranslationPEOModelPlanId | — |
| MODEL_PLAN_NAME | ModelPlanTranslationPEOModelPlanName | ✅ |
| OBJECT_VERSION_NUMBER | ModelPlanTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | ModelPlanTranslationPEOSourceLang | — |

### [[modelplanpvoviewall|ModelPlanPVOViewAll]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ModelPlanTranslationPEOCreatedBy | — |
| CREATION_DATE | ModelPlanTranslationPEOCreationDate | — |
| DESCRIPTION | ModelPlanTranslationPEODescription | ✅ |
| ENTERPRISE_ID | ModelPlanTranslationPEOEnterpriseId | — |
| LANGUAGE | ModelPlanTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ModelPlanTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ModelPlanTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ModelPlanTranslationPEOLastUpdatedBy | — |
| MODEL_PLAN_ID | ModelPlanTranslationPEOModelPlanId | — |
| MODEL_PLAN_NAME | ModelPlanTranslationPEOModelPlanName | ✅ |
| OBJECT_VERSION_NUMBER | ModelPlanTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | ModelPlanTranslationPEOSourceLang | — |

---

## 📚 Referências

- [Oracle Docs — HMO_MODEL_PLANS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hmomodelplanstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
