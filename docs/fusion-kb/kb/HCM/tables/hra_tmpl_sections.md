---
id: DOC-HCM-154
doc_type: system-doc
title: "HRA_TMPL_SECTIONS — Seções de Templates de Aprovação"
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
  - approval-template
  - sections
aliases:
  - HRA_TMPL_SECTIONS
  - hra_tmpl_sections
  - seções-de-templates-de-aprovação
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_TMPL_SECTIONS

## 📌 Visão Geral

Armazena as **seções de templates de aprovação**. Cada seção define um bloco de conteúdo dentro de um template, permitindo fluxos estruturados por etapas lógicas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estruturação:** Seções lógicas dentro de templates.
- **Configuração modular:** Regras distintas por seção.
- **Visibilidade:** Controle de informações por etapa.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TMPL_SECTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da seção | — | 🟢 95% |
| 2 | TEMPLATE_ID | NUMBER(18) | NOT NULL | FK | Template de aprovação | — | 🟢 90% |
| 3 | SECTION_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome da seção | — | 🟡 75% |
| 4 | SECTION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da seção | — | 🟡 70% |
| 5 | DISPLAY_SEQUENCE | NUMBER | NULL | Ordenação | Ordem de exibição | — | 🟡 75% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativa (Y/N) | — | 🟡 70% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Template de aprovação — via `TEMPLATE_ID`

### Tabelas relacionadas

---

## 📎 Uso Típico

### Seções ativas de um template
```sql
SELECT s.TMPL_SECTION_ID, s.SECTION_NAME, s.DISPLAY_SEQUENCE
FROM   HRA_TMPL_SECTIONS s
WHERE  s.TEMPLATE_ID = :p_template_id
  AND  NVL(s.ENABLED_FLAG, 'Y') = 'Y'
ORDER BY s.DISPLAY_SEQUENCE;
```

---

## 🔒 Observações

- Seções desabilitadas (`ENABLED_FLAG = 'N'`) não são apresentadas ao aprovador.

---

## 🔗 PVOs Relacionados

### [[performancedocratinglevelpvo|PerformanceDocRatingLevelPVO]] (HCM · BICC: 3/50)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_ITEMS_CONFIRM_CRIT_FLAG | TemplateSectionPEOAddItemsConfirmCritFlag | — |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CALCULATION_RULE_CODE | TemplateSectionPEOCalculationRuleCode | — |
| CONTENT_PROFILE_FLAG | TemplateSectionPEOContentProfileFlag | — |
| CONTENT_TYPE_ID | TemplateSectionPEOContentTypeId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DESCRIPTION | TemplateSectionPEODescription | — |
| ENABLE_ITEMS_FLAG | TemplateSectionPEOEnableItemsFlag | — |
| FAST_FORMULA_ID | TemplateSectionPEOFastFormulaId | — |
| FREE_FORM_ALLOWED_FLAG | TemplateSectionPEOFreeFormAllowedFlag | — |
| ITEM_CALCULATION_CODE | TemplateSectionPEOItemCalculationCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERF_RATING_MODEL_ID | TemplateSectionPEOPerfRatingModelId | — |
| PROFILE_ID | TemplateSectionPEOProfileId | — |
| PROFILE_TYPE_ID | TemplateSectionPEOProfileTypeId | — |
| RATE_ITEM_FLAG | TemplateSectionPEORateItemFlag | — |
| RATE_SECTION_FLAG | TemplateSectionPEORateSectionFlag | — |
| RATING_TYPE_CODE | TemplateSectionPEORatingTypeCode | — |
| REFERENCE_SECTION_ID | ReferenceSectionId | — |
| SECTION_DEF_ID | TemplateSectionPEOSectionDefId | — |
| SECTION_ID | SectionId | ✅ |
| SECTION_MIN_WEIGHT | TemplateSectionPEOSectionMinWeight | — |
| SECTION_RATING_MODEL_ID | TemplateSectionPEOSectionRatingModelId | — |
| SECTION_TYPE_CODE | TemplateSectionPEOSectionTypeCode | — |
| SECTION_WEIGHT | TemplateSectionPEOSectionWeight | — |
| SEQUENCE_NUMBER | TemplateSectionPEOSequenceNumber | — |
| SHOW_CRITICAL | TemplateSectionPEOShowCritical | — |
| SHOW_DESCRIPTION | TemplateSectionPEOShowDescription | — |
| SHOW_DUE_DATE | TemplateSectionPEOShowDueDate | — |
| SHOW_MANDATORY | TemplateSectionPEOShowMandatory | — |
| SHOW_MEASUREMENT | TemplateSectionPEOShowMeasurement | — |
| SHOW_OWNED_BY | TemplateSectionPEOShowOwnedBy | — |
| SHOW_PERCENT_COMPLETE | TemplateSectionPEOShowPercentComplete | — |
| SHOW_REMINDER_DATE | TemplateSectionPEOShowReminderDate | — |
| SHOW_SECTION_MIN_WEIGHT | TemplateSectionPEOShowSectionMinWeight | — |
| SHOW_SECTION_WEIGHT | TemplateSectionPEOShowSectionWeight | — |
| SHOW_STATUS | TemplateSectionPEOShowStatus | — |
| SHOW_TARGET_PERF_RTG | TemplateSectionPEOShowTargetPerfRtg | — |
| SHOW_TARGET_PROF_LEVEL | TemplateSectionPEOShowTargetProfLevel | — |
| TEMPLATE_DEFN_ID | TemplateSectionPEOTemplateDefnId | — |
| USE_PROFILE_FLAG | TemplateSectionPEOUseProfileFlag | — |
| USE_SECRTG_FOR_PERFRTG_FLAG | TemplateSectionPEOUseSecrtgForPerfrtgFlag | — |
| USE_SPEC_CONTENT_ITEM_FLAG | TemplateSectionPEOUseSpecContentItemFlag | — |
| USE_SPEC_PROFILE_FLAG | TemplateSectionPEOUseSpecProfileFlag | — |
| USE_WORKER_GOALS_FLAG | TemplateSectionPEOUseWorkerGoalsFlag | — |
| WEIGHT_SECTION_FLAG | TemplateSectionPEOWeightSectionFlag | — |

### [[performancedocsectionpvo|PerformanceDocSectionPVO]] (HCM · BICC: 37/117)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_ITEMS_CONFIRM_CRIT_FLAG | TemplateSectionPEOAddItemsConfirmCritFlag | ✅ |
| ATTRIBUTE1 | TemplateSectionPEOAttribute1 | — |
| ATTRIBUTE10 | TemplateSectionPEOAttribute10 | — |
| ATTRIBUTE11 | TemplateSectionPEOAttribute11 | — |
| ATTRIBUTE12 | TemplateSectionPEOAttribute12 | — |
| ATTRIBUTE13 | TemplateSectionPEOAttribute13 | — |
| ATTRIBUTE14 | TemplateSectionPEOAttribute14 | — |
| ATTRIBUTE15 | TemplateSectionPEOAttribute15 | — |
| ATTRIBUTE16 | TemplateSectionPEOAttribute16 | — |
| ATTRIBUTE17 | TemplateSectionPEOAttribute17 | — |
| ATTRIBUTE18 | TemplateSectionPEOAttribute18 | — |
| ATTRIBUTE19 | TemplateSectionPEOAttribute19 | — |
| ATTRIBUTE2 | TemplateSectionPEOAttribute2 | — |
| ATTRIBUTE20 | TemplateSectionPEOAttribute20 | — |
| ATTRIBUTE21 | TemplateSectionPEOAttribute21 | — |
| ATTRIBUTE22 | TemplateSectionPEOAttribute22 | — |
| ATTRIBUTE23 | TemplateSectionPEOAttribute23 | — |
| ATTRIBUTE24 | TemplateSectionPEOAttribute24 | — |
| ATTRIBUTE25 | TemplateSectionPEOAttribute25 | — |
| ATTRIBUTE26 | TemplateSectionPEOAttribute26 | — |
| ATTRIBUTE27 | TemplateSectionPEOAttribute27 | — |
| ATTRIBUTE28 | TemplateSectionPEOAttribute28 | — |
| ATTRIBUTE29 | TemplateSectionPEOAttribute29 | — |
| ATTRIBUTE3 | TemplateSectionPEOAttribute3 | — |
| ATTRIBUTE30 | TemplateSectionPEOAttribute30 | — |
| ATTRIBUTE4 | TemplateSectionPEOAttribute4 | — |
| ATTRIBUTE5 | TemplateSectionPEOAttribute5 | — |
| ATTRIBUTE6 | TemplateSectionPEOAttribute6 | — |
| ATTRIBUTE7 | TemplateSectionPEOAttribute7 | — |
| ATTRIBUTE8 | TemplateSectionPEOAttribute8 | — |
| ATTRIBUTE9 | TemplateSectionPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | TemplateSectionPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | TemplateSectionPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | TemplateSectionPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | TemplateSectionPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | TemplateSectionPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | TemplateSectionPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | TemplateSectionPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | TemplateSectionPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | TemplateSectionPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | TemplateSectionPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | TemplateSectionPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | TemplateSectionPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | TemplateSectionPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | TemplateSectionPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | TemplateSectionPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | TemplateSectionPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | TemplateSectionPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | TemplateSectionPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | TemplateSectionPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | TemplateSectionPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | TemplateSectionPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | TemplateSectionPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | TemplateSectionPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | TemplateSectionPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | TemplateSectionPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | TemplateSectionPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | TemplateSectionPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | TemplateSectionPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | TemplateSectionPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | TemplateSectionPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | TemplateSectionPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | TemplateSectionPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | TemplateSectionPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | TemplateSectionPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | TemplateSectionPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | TemplateSectionPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CALCULATION_RULE_CODE | TemplateSectionPEOCalculationRuleCode | ✅ |
| CONTENT_PROFILE_FLAG | TemplateSectionPEOContentProfileFlag | ✅ |
| CONTENT_TYPE_ID | TemplateSectionPEOContentTypeId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DESCRIPTION | TemplateSectionPEODescription | ✅ |
| ENABLE_ITEM_COMMENTS_FLAG | TemplateSectionPEOEnableItemCommentsFlag | ✅ |
| ENABLE_ITEMS_FLAG | TemplateSectionPEOEnableItemsFlag | ✅ |
| FAST_FORMULA_ID | TemplateSectionPEOFastFormulaId | — |
| FREE_FORM_ALLOWED_FLAG | TemplateSectionPEOFreeFormAllowedFlag | ✅ |
| ITEM_CALCULATION_CODE | TemplateSectionPEOItemCalculationCode | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERF_RATING_MODEL_ID | TemplateSectionPEOPerfRatingModelId | — |
| PROFILE_ID | TemplateSectionPEOProfileId | — |
| PROFILE_TYPE_ID | TemplateSectionPEOProfileTypeId | — |
| RATE_ITEM_FLAG | TemplateSectionPEORateItemFlag | ✅ |
| RATE_SECTION_FLAG | TemplateSectionPEORateSectionFlag | ✅ |
| RATING_TYPE_CODE | TemplateSectionPEORatingTypeCode | ✅ |
| REFERENCE_SECTION_ID | ReferenceSectionId | — |
| SECTION_DEF_ID | TemplateSectionPEOSectionDefId | — |
| SECTION_ID | SectionId | ✅ |
| SECTION_MIN_WEIGHT | TemplateSectionPEOSectionMinWeight | ✅ |
| SECTION_RATING_MODEL_ID | TemplateSectionPEOSectionRatingModelId | — |
| SECTION_TYPE_CODE | TemplateSectionPEOSectionTypeCode | ✅ |
| SECTION_WEIGHT | TemplateSectionPEOSectionWeight | ✅ |
| SEQUENCE_NUMBER | TemplateSectionPEOSequenceNumber | ✅ |
| SHOW_CRITICAL | TemplateSectionPEOShowCritical | ✅ |
| SHOW_DESCRIPTION | TemplateSectionPEOShowDescription | ✅ |
| SHOW_DUE_DATE | TemplateSectionPEOShowDueDate | ✅ |
| SHOW_MANDATORY | TemplateSectionPEOShowMandatory | ✅ |
| SHOW_MEASUREMENT | TemplateSectionPEOShowMeasurement | ✅ |
| SHOW_OWNED_BY | TemplateSectionPEOShowOwnedBy | ✅ |
| SHOW_PERCENT_COMPLETE | TemplateSectionPEOShowPercentComplete | ✅ |
| SHOW_REMINDER_DATE | TemplateSectionPEOShowReminderDate | ✅ |
| SHOW_SECTION_MIN_WEIGHT | TemplateSectionPEOShowSectionMinWeight | ✅ |
| SHOW_SECTION_WEIGHT | TemplateSectionPEOShowSectionWeight | ✅ |
| SHOW_STATUS | TemplateSectionPEOShowStatus | ✅ |
| SHOW_TARGET_PERF_RTG | TemplateSectionPEOShowTargetPerfRtg | ✅ |
| SHOW_TARGET_PROF_LEVEL | TemplateSectionPEOShowTargetProfLevel | ✅ |
| TEMPLATE_DEFN_ID | TemplateSectionPEOTemplateDefnId | — |
| USE_PROFILE_FLAG | TemplateSectionPEOUseProfileFlag | ✅ |
| USE_SECRTG_FOR_PERFRTG_FLAG | TemplateSectionPEOUseSecrtgForPerfrtgFlag | ✅ |
| USE_SPEC_CONTENT_ITEM_FLAG | TemplateSectionPEOUseSpecContentItemFlag | ✅ |
| USE_SPEC_PROFILE_FLAG | TemplateSectionPEOUseSpecProfileFlag | ✅ |
| USE_WORKER_GOALS_FLAG | TemplateSectionPEOUseWorkerGoalsFlag | ✅ |
| WEIGHT_SECTION_FLAG | TemplateSectionPEOWeightSectionFlag | ✅ |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
