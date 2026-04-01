---
id: DOC-HCM-113
doc_type: system-doc
title: "HRA_SECTION_DEFNS_B — Definições de Seções de Avaliação (Base)"
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
  - performance-management
  - seções
  - section-definitions
  - hra
aliases:
  - HRA_SECTION_DEFNS_B
  - hra_section_defns_b
  - hra-section-defns-b
  - DOC-HCM-113
  - definições-de-seções-de-avaliação-(base)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_SECTION_DEFNS_B

## 📌 Visão Geral

Armazena as **definições base das seções** que compõem documentos/templates de avaliação de performance. Cada seção agrupa critérios de avaliação (ex: Competências, Objetivos, Desenvolvimento).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estrutura de avaliação:** Definição de seções dos documentos de performance.
- **Agrupamento de critérios:** Organização lógica dos itens avaliados.
- **Pesos por seção:** Configuracao de peso de cada seção no resultado final.
- **Templates:** Seções são reutilizadas em múltiplos templates.
- **Base para tradução:** Complementada por `HRA_SECTION_DEFNS_TL`.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SECTION_DEFN_ID | NUMBER(18) | NOT NULL | PK | Identificador único da seção | — | 🟢 90% |
| 2 | SECTION_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código da seção | — | 🟡 80% |
| 3 | SECTION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (COMPETENCY, GOAL, DEVELOPMENT, OVERALL) | — | 🟡 80% |
| 4 | WEIGHT | NUMBER | NULL | Cálculo | Peso da seção no resultado total (%) | — | 🟡 75% |
| 5 | STATUS_CODE | VARCHAR2(30) | NULL | Status | Status (ACTIVE, INACTIVE) | — | 🟡 80% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versão do objeto | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuario que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhum relacionamento de entrada identificado até o momento.

### Tabelas-filha (FK de saída)
- [[hra_section_defns_tl]] — via `SECTION_DEFN_ID` (traducoes multilingue do registro)
- [[hra_eval_sections]] — via `SECTION_DEFN_ID` (seções em avaliações)

---

## 📎 Uso Típico

### Seções ativas
```sql
SELECT sd.SECTION_DEFN_ID, sd.SECTION_CODE, sd.SECTION_TYPE, sd.WEIGHT
FROM   HRA_SECTION_DEFNS_B sd
WHERE  sd.STATUS_CODE = 'ACTIVE';
```

### Seções por tipo
```sql
SELECT sd.SECTION_TYPE, COUNT(*) AS qtd
FROM   HRA_SECTION_DEFNS_B sd
GROUP BY sd.SECTION_TYPE;
```

---

## 🔒 Observações

- Tabela _B (base) contém dados independentes de idioma.
- O `SECTION_TYPE` categoriza: COMPETENCY, GOAL, DEVELOPMENT, OVERALL, FEEDBACK.
- O `WEIGHT` define o percentual de contribuição da seção no score final.
- Seções são blocos reutilizáveis montados em templates de avaliação.

---

## 🔗 PVOs Relacionados

### [[performancedocsectionpvo|PerformanceDocSectionPVO]] (HCM · BICC: 5/114)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_ITEMS_CONFIRM_CRIT_FLAG | SectionDefnBPEOAddItemsConfirmCritFlag | — |
| ATTRIBUTE1 | SectionDefnBPEOAttribute1 | — |
| ATTRIBUTE10 | SectionDefnBPEOAttribute10 | — |
| ATTRIBUTE11 | SectionDefnBPEOAttribute11 | — |
| ATTRIBUTE12 | SectionDefnBPEOAttribute12 | — |
| ATTRIBUTE13 | SectionDefnBPEOAttribute13 | — |
| ATTRIBUTE14 | SectionDefnBPEOAttribute14 | — |
| ATTRIBUTE15 | SectionDefnBPEOAttribute15 | — |
| ATTRIBUTE16 | SectionDefnBPEOAttribute16 | — |
| ATTRIBUTE17 | SectionDefnBPEOAttribute17 | — |
| ATTRIBUTE18 | SectionDefnBPEOAttribute18 | — |
| ATTRIBUTE19 | SectionDefnBPEOAttribute19 | — |
| ATTRIBUTE2 | SectionDefnBPEOAttribute2 | — |
| ATTRIBUTE20 | SectionDefnBPEOAttribute20 | — |
| ATTRIBUTE21 | SectionDefnBPEOAttribute21 | — |
| ATTRIBUTE22 | SectionDefnBPEOAttribute22 | — |
| ATTRIBUTE23 | SectionDefnBPEOAttribute23 | — |
| ATTRIBUTE24 | SectionDefnBPEOAttribute24 | — |
| ATTRIBUTE25 | SectionDefnBPEOAttribute25 | — |
| ATTRIBUTE26 | SectionDefnBPEOAttribute26 | — |
| ATTRIBUTE27 | SectionDefnBPEOAttribute27 | — |
| ATTRIBUTE28 | SectionDefnBPEOAttribute28 | — |
| ATTRIBUTE29 | SectionDefnBPEOAttribute29 | — |
| ATTRIBUTE3 | SectionDefnBPEOAttribute3 | — |
| ATTRIBUTE30 | SectionDefnBPEOAttribute30 | — |
| ATTRIBUTE4 | SectionDefnBPEOAttribute4 | — |
| ATTRIBUTE5 | SectionDefnBPEOAttribute5 | — |
| ATTRIBUTE6 | SectionDefnBPEOAttribute6 | — |
| ATTRIBUTE7 | SectionDefnBPEOAttribute7 | — |
| ATTRIBUTE8 | SectionDefnBPEOAttribute8 | — |
| ATTRIBUTE9 | SectionDefnBPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | SectionDefnBPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | SectionDefnBPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | SectionDefnBPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | SectionDefnBPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | SectionDefnBPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | SectionDefnBPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | SectionDefnBPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | SectionDefnBPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | SectionDefnBPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | SectionDefnBPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | SectionDefnBPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | SectionDefnBPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | SectionDefnBPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | SectionDefnBPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | SectionDefnBPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | SectionDefnBPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | SectionDefnBPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | SectionDefnBPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | SectionDefnBPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | SectionDefnBPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | SectionDefnBPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | SectionDefnBPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | SectionDefnBPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | SectionDefnBPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | SectionDefnBPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | SectionDefnBPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | SectionDefnBPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | SectionDefnBPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | SectionDefnBPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | SectionDefnBPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | SectionDefnBPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | SectionDefnBPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | ASectionDefnBPEOttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | SectionDefnBPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | SectionDefnBPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | SectionDefnBPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | SectionDefnBPEOBusinessGroupId | ✅ |
| CALCULATION_RULE_CODE | SectionDefnBPEOCalculationRuleCode | — |
| CONTENT_PROFILE_FLAG | SectionDefnBPEOContentProfileFlag | — |
| CONTENT_TYPE_ID | SectionDefnBPEOContentTypeId | — |
| CREATED_BY | SectionDefnBPEOCreatedBy | — |
| CREATION_DATE | SectionDefnBPEOCreationDate | — |
| DATE_FROM | SectionDefnBPEODateFrom | — |
| DATE_TO | SectionDefnBPEODateTo | — |
| ENABLE_ITEMS_FLAG | SectionDefnBPEOEnableItemsFlag | — |
| FAST_FORMULA_ID | SectionDefnBPEOFastFormulaId | — |
| FREE_FORM_ALLOWED_FLAG | SectionDefnBPEOFreeFormAllowedFlag | — |
| ITEM_CALCULATION_CODE | SectionDefnBPEOItemCalculationCode | — |
| LAST_UPDATE_DATE | SectionDefnBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SectionDefnBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SectionDefnBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | SectionDefnBPEOObjectVersionNumber | — |
| PERF_RATING_MODEL_ID | SectionDefnBPEOPerfRatingModelId | ✅ |
| PROFILE_ID | SectionDefnBPEOProfileId | — |
| PROFILE_TYPE_ID | SectionDefnBPEOProfileTypeId | — |
| RATE_ITEM_FLAG | SectionDefnBPEORateItemFlag | — |
| RATE_SECTION_FLAG | SectionDefnBPEORateSectionFlag | — |
| RATING_TYPE_CODE | SectionDefnBPEORatingTypeCode | — |
| SECTION_DEF_ID | SectionDefId | ✅ |
| SECTION_MIN_WEIGHT | SectionDefnBPEOSectionMinWeight | — |
| SECTION_RATING_MODEL_ID | SectionDefnBPEOSectionRatingModelId | ✅ |
| SECTION_TYPE_CODE | SectionDefnBPEOSectionTypeCode | — |
| SECTION_WEIGHT | SectionDefnBPEOSectionWeight | — |
| SHOW_CRITICAL | SectionDefnBPEOShowCritical | — |
| SHOW_DESCRIPTION | SectionDefnBPEOShowDescription | — |
| SHOW_DUE_DATE | SectionDefnBPEOShowDueDate | — |
| SHOW_MANDATORY | SectionDefnBPEOShowMandatory | — |
| SHOW_MEASUREMENT | SectionDefnBPEOShowMeasurement | — |
| SHOW_OWNED_BY | SectionDefnBPEOShowOwnedBy | — |
| SHOW_PERCENT_COMPLETE | SectionDefnBPEOShowPercentComplete | — |
| SHOW_REMINDER_DATE | SectionDefnBPEOShowReminderDate | — |
| SHOW_SECTION_MIN_WEIGHT | SectionDefnBPEOShowSectionMinWeight | — |
| SHOW_SECTION_WEIGHT | SectionDefnBPEOShowSectionWeight | — |
| SHOW_STATUS | SectionDefnBPEOShowStatus | — |
| SHOW_TARGET_PERF_RTG | SectionDefnBPEOShowTargetPerfRtg | — |
| SHOW_TARGET_PROF_LEVEL | SectionDefnBPEOShowTargetProfLevel | — |
| STATUS_CODE | SectionDefnBPEOStatusCode | — |
| USE_PROFILE_FLAG | SectionDefnBPEOUseProfileFlag | — |
| USE_SECRTG_FOR_PERFRTG_FLAG | SectionDefnBPEOUseSecrtgForPerfrtgFlag | — |
| USE_SPEC_CONTENT_ITEM_FLAG | SectionDefnBPEOUseSpecContentItemFlag | — |
| USE_SPEC_PROFILE_FLAG | SectionDefnBPEOUseSpecProfileFlag | — |
| USE_WORKER_GOALS_FLAG | SectionDefnBPEOUseWorkerGoalsFlag | — |
| WEIGHT_SECTION_FLAG | SectionDefnBPEOWeightSectionFlag | — |

### [[sectiontypepvo|SectionTypePVO]] (HCM · BICC: 4/114)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_ITEMS_CONFIRM_CRIT_FLAG | AddItemsConfirmCritFlag | — |
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CALCULATION_RULE_CODE | CalculationRuleCode | — |
| CONTENT_PROFILE_FLAG | ContentProfileFlag | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| ENABLE_ITEMS_FLAG | EnableItemsFlag | — |
| FAST_FORMULA_ID | FastFormulaId | — |
| FREE_FORM_ALLOWED_FLAG | FreeFormAllowedFlag | — |
| ITEM_CALCULATION_CODE | ItemCalculationCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERF_RATING_MODEL_ID | PerfRatingModelId | — |
| PROFILE_ID | ProfileId | — |
| PROFILE_TYPE_ID | ProfileTypeId | — |
| RATE_ITEM_FLAG | RateItemFlag | — |
| RATE_SECTION_FLAG | RateSectionFlag | — |
| RATING_TYPE_CODE | RatingTypeCode | — |
| SECTION_DEF_ID | SectionDefId | ✅ |
| SECTION_MIN_WEIGHT | SectionMinWeight | — |
| SECTION_RATING_MODEL_ID | SectionRatingModelId | — |
| SECTION_TYPE_CODE | SectionTypeCode | ✅ |
| SECTION_WEIGHT | SectionWeight | — |
| SHOW_CRITICAL | ShowCritical | — |
| SHOW_DESCRIPTION | ShowDescription | — |
| SHOW_DUE_DATE | ShowDueDate | — |
| SHOW_MANDATORY | ShowMandatory | — |
| SHOW_MEASUREMENT | ShowMeasurement | — |
| SHOW_OWNED_BY | ShowOwnedBy | — |
| SHOW_PERCENT_COMPLETE | ShowPercentComplete | — |
| SHOW_REMINDER_DATE | ShowReminderDate | — |
| SHOW_SECTION_MIN_WEIGHT | ShowSectionMinWeight | — |
| SHOW_SECTION_WEIGHT | ShowSectionWeight | — |
| SHOW_STATUS | ShowStatus | — |
| SHOW_TARGET_PERF_RTG | ShowTargetPerfRtg | — |
| SHOW_TARGET_PROF_LEVEL | ShowTargetProfLevel | — |
| STATUS_CODE | StatusCode | — |
| USE_PROFILE_FLAG | UseProfileFlag | — |
| USE_SECRTG_FOR_PERFRTG_FLAG | UseSecrtgForPerfrtgFlag | — |
| USE_SPEC_CONTENT_ITEM_FLAG | UseSpecContentItemFlag | — |
| USE_SPEC_PROFILE_FLAG | UseSpecProfileFlag | — |
| USE_WORKER_GOALS_FLAG | UseWorkerGoalsFlag | — |
| WEIGHT_SECTION_FLAG | WeightSectionFlag | — |

---

## 📚 Referências

- [Oracle Docs — HRA_SECTION_DEFNS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrasectiondefnsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
