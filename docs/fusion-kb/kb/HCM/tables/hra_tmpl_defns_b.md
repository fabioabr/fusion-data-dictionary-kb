---
id: DOC-HCM-115
doc_type: system-doc
title: "HRA_TMPL_DEFNS_B — Definições de Templates de Avaliação (Base)"
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
  - templates
  - template-definitions
  - hra
aliases:
  - HRA_TMPL_DEFNS_B
  - hra_tmpl_defns_b
  - hra-tmpl-defns-b
  - DOC-HCM-115
  - definições-de-templates-de-avaliação-(base)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_TMPL_DEFNS_B

## 📌 Visão Geral

Armazena as **definições base dos templates** de avaliação de performance. Templates são modelos que combinam seções, papéis, etapas e regras para estruturar o processo de avaliação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estrutura de avaliação:** Template master que define o processo completo.
- **Composição de seções:** Quais seções compõem o template.
- **Workflow:** Definição de etapas e papéis do processo.
- **Reutilização:** Templates são reutilizados em múltiplos ciclos.
- **Base para tradução:** Complementada por `HRA_TMPL_DEFNS_TL`.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TMPL_DEFN_ID | NUMBER(18) | NOT NULL | PK | Identificador único do template | — | 🟢 90% |
| 2 | TMPL_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código do template | — | 🟡 80% |
| 3 | TMPL_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (ANNUAL_REVIEW, MID_YEAR, PROBATION, 360) | — | 🟡 80% |
| 4 | STATUS_CODE | VARCHAR2(30) | NULL | Status | Status (ACTIVE, INACTIVE, DRAFT) | — | 🟡 80% |
| 5 | EFFECTIVE_START_DATE | DATE | NULL | Data | Inicio de vigencia | — | 🟡 80% |
| 6 | EFFECTIVE_END_DATE | DATE | NULL | Data | Fim de vigencia | — | 🟡 80% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versão do objeto | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuario que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhum relacionamento de entrada identificado até o momento.

### Tabelas-filha (FK de saída)
- [[hra_tmpl_defns_tl]] — via `TMPL_DEFN_ID` (traducoes multilingue do registro)
- [[hra_evaluations]] — via `TMPL_DEFN_ID` (avaliações que usam este template)

---

## 📎 Uso Típico

### Templates ativos
```sql
SELECT td.TMPL_DEFN_ID, td.TMPL_CODE, td.TMPL_TYPE, td.STATUS_CODE
FROM   HRA_TMPL_DEFNS_B td
WHERE  td.STATUS_CODE = 'ACTIVE';
```

### Templates por tipo
```sql
SELECT td.TMPL_TYPE, COUNT(*) AS qtd
FROM   HRA_TMPL_DEFNS_B td
GROUP BY td.TMPL_TYPE;
```

---

## 🔒 Observações

- Tabela _B (base) contém dados independentes de idioma.
- O `TMPL_TYPE` categoriza: ANNUAL_REVIEW, MID_YEAR, PROBATION, 360_FEEDBACK.
- Templates ACTIVE são utilizados para criação de novos documentos de avaliação.
- O `OBJECT_VERSION_NUMBER` controla concorrência otimista.

---

## 🔗 PVOs Relacionados

### [[eligibilityresultpvo|EligibilityResultPVO]] (HCM · BICC: 3/87)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | TemplateDefnBPEOAttribute1 | — |
| ATTRIBUTE10 | TemplateDefnBPEOAttribute10 | — |
| ATTRIBUTE11 | TemplateDefnBPEOAttribute11 | — |
| ATTRIBUTE12 | TemplateDefnBPEOAttribute12 | — |
| ATTRIBUTE13 | TemplateDefnBPEOAttribute13 | — |
| ATTRIBUTE14 | TemplateDefnBPEOAttribute14 | — |
| ATTRIBUTE15 | TemplateDefnBPEOAttribute15 | — |
| ATTRIBUTE16 | TemplateDefnBPEOAttribute16 | — |
| ATTRIBUTE17 | TemplateDefnBPEOAttribute17 | — |
| ATTRIBUTE18 | TemplateDefnBPEOAttribute18 | — |
| ATTRIBUTE19 | TemplateDefnBPEOAttribute19 | — |
| ATTRIBUTE2 | TemplateDefnBPEOAttribute2 | — |
| ATTRIBUTE20 | TemplateDefnBPEOAttribute20 | — |
| ATTRIBUTE21 | TemplateDefnBPEOAttribute21 | — |
| ATTRIBUTE22 | TemplateDefnBPEOAttribute22 | — |
| ATTRIBUTE23 | TemplateDefnBPEOAttribute23 | — |
| ATTRIBUTE24 | TemplateDefnBPEOAttribute24 | — |
| ATTRIBUTE25 | TemplateDefnBPEOAttribute25 | — |
| ATTRIBUTE26 | TemplateDefnBPEOAttribute26 | — |
| ATTRIBUTE27 | TemplateDefnBPEOAttribute27 | — |
| ATTRIBUTE28 | TemplateDefnBPEOAttribute28 | — |
| ATTRIBUTE29 | TemplateDefnBPEOAttribute29 | — |
| ATTRIBUTE3 | TemplateDefnBPEOAttribute3 | — |
| ATTRIBUTE30 | TemplateDefnBPEOAttribute30 | — |
| ATTRIBUTE4 | TemplateDefnBPEOAttribute4 | — |
| ATTRIBUTE5 | TemplateDefnBPEOAttribute5 | — |
| ATTRIBUTE6 | TemplateDefnBPEOAttribute6 | — |
| ATTRIBUTE7 | TemplateDefnBPEOAttribute7 | — |
| ATTRIBUTE8 | TemplateDefnBPEOAttribute8 | — |
| ATTRIBUTE9 | TemplateDefnBPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | TemplateDefnBPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | TemplateDefnBPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | TemplateDefnBPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | TemplateDefnBPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | TemplateDefnBPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | TemplateDefnBPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | TemplateDefnBPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | TemplateDefnBPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | TemplateDefnBPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | TemplateDefnBPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | TemplateDefnBPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | TemplateDefnBPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | TemplateDefnBPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | TemplateDefnBPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | TemplateDefnBPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | TemplateDefnBPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | TemplateDefnBPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | TemplateDefnBPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | TemplateDefnBPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | TemplateDefnBPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | TemplateDefnBPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | TemplateDefnBPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | TemplateDefnBPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | TemplateDefnBPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | TemplateDefnBPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | TemplateDefnBPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | TemplateDefnBPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | TemplateDefnBPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | TemplateDefnBPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | TemplateDefnBPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | TemplateDefnBPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | TemplateDefnBPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | TemplateDefnBPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | TemplateDefnBPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | TemplateDefnBPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | TemplateDefnBPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | TemplateDefnBPEOBusinessGroupId | ✅ |
| CALCULATE_RATINGS_FLAG | TemplateDefnBPEOCalculateRatingsFlag | — |
| CREATED_BY | TemplateDefnBPEOCreatedBy | — |
| CREATION_DATE | TemplateDefnBPEOCreationDate | — |
| DATE_FROM | TemplateDefnBPEODateFrom | — |
| DATE_TO | TemplateDefnBPEODateTo | — |
| DECIMAL_PLACES | TemplateDefnBPEODecimalPlaces | — |
| DOC_TYPE_ID | TemplateDefnBPEODocTypeId | — |
| LAST_UPDATE_DATE | TemplateDefnBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplateDefnBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplateDefnBPEOLastUpdatedBy | — |
| MAPPING_METHOD_CODE | TemplateDefnBPEOMappingMethodCode | — |
| OBJECT_VERSION_NUMBER | TemplateDefnBPEOObjectVersionNumber | — |
| PROCESS_FLOW_ID | TemplateDefnBPEOProcessFlowId | — |
| ROUNDING_RULE_CODE | TemplateDefnBPEORoundingRuleCode | — |
| SELECT_MGR_ALLOWED_FLAG | TemplateDefnBPEOSelectMgrAllowedFlag | — |
| SET_ID | TemplateDefnBPEOSetId | — |
| SHOW_PARTICIPANT_NAMES | TemplateDefnBPEOShowParticipantNames | — |
| STAR_RATING_ENABLED_FLAG | TemplateDefnBPEOStarRatingEnabledFlag | — |
| STATUS_CODE | TemplateDefnBPEOStatusCode | — |
| TEMPLATE_DEFN_ID | TemplateDefnBPEOTemplateDefnId | ✅ |

### [[eligibilityresultsdetailspvo|EligibilityResultsDetailsPVO]] (HCM · BICC: 3/87)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | TemplateDefnBPEOAttribute1 | — |
| ATTRIBUTE10 | TemplateDefnBPEOAttribute10 | — |
| ATTRIBUTE11 | TemplateDefnBPEOAttribute11 | — |
| ATTRIBUTE12 | TemplateDefnBPEOAttribute12 | — |
| ATTRIBUTE13 | TemplateDefnBPEOAttribute13 | — |
| ATTRIBUTE14 | TemplateDefnBPEOAttribute14 | — |
| ATTRIBUTE15 | TemplateDefnBPEOAttribute15 | — |
| ATTRIBUTE16 | TemplateDefnBPEOAttribute16 | — |
| ATTRIBUTE17 | TemplateDefnBPEOAttribute17 | — |
| ATTRIBUTE18 | TemplateDefnBPEOAttribute18 | — |
| ATTRIBUTE19 | TemplateDefnBPEOAttribute19 | — |
| ATTRIBUTE2 | TemplateDefnBPEOAttribute2 | — |
| ATTRIBUTE20 | TemplateDefnBPEOAttribute20 | — |
| ATTRIBUTE21 | TemplateDefnBPEOAttribute21 | — |
| ATTRIBUTE22 | TemplateDefnBPEOAttribute22 | — |
| ATTRIBUTE23 | TemplateDefnBPEOAttribute23 | — |
| ATTRIBUTE24 | TemplateDefnBPEOAttribute24 | — |
| ATTRIBUTE25 | TemplateDefnBPEOAttribute25 | — |
| ATTRIBUTE26 | TemplateDefnBPEOAttribute26 | — |
| ATTRIBUTE27 | TemplateDefnBPEOAttribute27 | — |
| ATTRIBUTE28 | TemplateDefnBPEOAttribute28 | — |
| ATTRIBUTE29 | TemplateDefnBPEOAttribute29 | — |
| ATTRIBUTE3 | TemplateDefnBPEOAttribute3 | — |
| ATTRIBUTE30 | TemplateDefnBPEOAttribute30 | — |
| ATTRIBUTE4 | TemplateDefnBPEOAttribute4 | — |
| ATTRIBUTE5 | TemplateDefnBPEOAttribute5 | — |
| ATTRIBUTE6 | TemplateDefnBPEOAttribute6 | — |
| ATTRIBUTE7 | TemplateDefnBPEOAttribute7 | — |
| ATTRIBUTE8 | TemplateDefnBPEOAttribute8 | — |
| ATTRIBUTE9 | TemplateDefnBPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | TemplateDefnBPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | TemplateDefnBPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | TemplateDefnBPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | TemplateDefnBPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | TemplateDefnBPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | TemplateDefnBPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | TemplateDefnBPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | TemplateDefnBPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | TemplateDefnBPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | TemplateDefnBPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | TemplateDefnBPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | TemplateDefnBPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | TemplateDefnBPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | TemplateDefnBPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | TemplateDefnBPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | TemplateDefnBPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | TemplateDefnBPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | TemplateDefnBPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | TemplateDefnBPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | TemplateDefnBPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | TemplateDefnBPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | TemplateDefnBPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | TemplateDefnBPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | TemplateDefnBPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | TemplateDefnBPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | TemplateDefnBPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | TemplateDefnBPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | TemplateDefnBPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | TemplateDefnBPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | TemplateDefnBPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | TemplateDefnBPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | TemplateDefnBPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | TemplateDefnBPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | TemplateDefnBPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | TemplateDefnBPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | TemplateDefnBPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | TemplateDefnBPEOBusinessGroupId | ✅ |
| CALCULATE_RATINGS_FLAG | TemplateDefnBPEOCalculateRatingsFlag | — |
| CREATED_BY | TemplateDefnBPEOCreatedBy | — |
| CREATION_DATE | TemplateDefnBPEOCreationDate | — |
| DATE_FROM | TemplateDefnBPEODateFrom | — |
| DATE_TO | TemplateDefnBPEODateTo | — |
| DECIMAL_PLACES | TemplateDefnBPEODecimalPlaces | — |
| DOC_TYPE_ID | TemplateDefnBPEODocTypeId | — |
| LAST_UPDATE_DATE | TemplateDefnBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplateDefnBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplateDefnBPEOLastUpdatedBy | — |
| MAPPING_METHOD_CODE | TemplateDefnBPEOMappingMethodCode | — |
| OBJECT_VERSION_NUMBER | TemplateDefnBPEOObjectVersionNumber | — |
| PROCESS_FLOW_ID | TemplateDefnBPEOProcessFlowId | — |
| ROUNDING_RULE_CODE | TemplateDefnBPEORoundingRuleCode | — |
| SELECT_MGR_ALLOWED_FLAG | TemplateDefnBPEOSelectMgrAllowedFlag | — |
| SET_ID | TemplateDefnBPEOSetId | — |
| SHOW_PARTICIPANT_NAMES | TemplateDefnBPEOShowParticipantNames | — |
| STAR_RATING_ENABLED_FLAG | TemplateDefnBPEOStarRatingEnabledFlag | — |
| STATUS_CODE | TemplateDefnBPEOStatusCode | — |
| TEMPLATE_DEFN_ID | TemplateDefnBPEOTemplateDefnId | ✅ |

### [[managerperformanceoverallratingpvo|ManagerPerformanceOverallRatingPVO]] (HCM · BICC: 2/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplateDefnBPEOBusinessGroupId | — |
| CALCULATE_RATINGS_FLAG | TemplateDefnBPEOCalculateRatingsFlag | — |
| DATE_FROM | TemplateDefnBPEODateFrom | — |
| DATE_TO | TemplateDefnBPEODateTo | — |
| DECIMAL_PLACES | TemplateDefnBPEODecimalPlaces | — |
| DOC_TYPE_ID | TemplateDefnBPEODocTypeId | ✅ |
| MAPPING_METHOD_CODE | TemplateDefnBPEOMappingMethodCode | — |
| PROCESS_FLOW_ID | TemplateDefnBPEOProcessFlowId | — |
| ROUNDING_RULE_CODE | TemplateDefnBPEORoundingRuleCode | — |
| SELECT_MGR_ALLOWED_FLAG | TemplateDefnBPEOSelectMgrAllowedFlag | — |
| SET_ID | TemplateDefnBPEOSetId | — |
| SHOW_PARTICIPANT_NAMES | TemplateDefnBPEOShowParticipantNames | — |
| STAR_RATING_ENABLED_FLAG | TemplateDefnBPEOStarRatingEnabledFlag | — |
| STATUS_CODE | TemplateDefnBPEOStatusCode | — |
| TEMPLATE_DEFN_ID | TemplateDefnBPEOTemplateDefnId | ✅ |

### [[performancedocumentspvo|PerformanceDocumentsPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplateDefnBPEOBusinessGroupId | — |
| CALCULATE_RATINGS_FLAG | TemplateDefnBPEOCalculateRatingsFlag | — |
| DATE_FROM | TemplateDefnBPEODateFrom | — |
| DATE_TO | TemplateDefnBPEODateTo | — |
| DECIMAL_PLACES | TemplateDefnBPEODecimalPlaces | — |
| DOC_TYPE_ID | TemplateDefnBPEODocTypeId | — |
| LAST_UPDATE_DATE | TemplateDefnBPEOLastUpdateDate | — |
| MAPPING_METHOD_CODE | TemplateDefnBPEOMappingMethodCode | — |
| PROCESS_FLOW_ID | TemplateDefnBPEOProcessFlowId | — |
| ROUNDING_RULE_CODE | TemplateDefnBPEORoundingRuleCode | — |
| SELECT_MGR_ALLOWED_FLAG | TemplateDefnBPEOSelectMgrAllowedFlag | — |
| SET_ID | TemplateDefnBPEOSetId | — |
| SHOW_PARTICIPANT_NAMES | TemplateDefnBPEOShowParticipantNames | — |
| STAR_RATING_ENABLED_FLAG | TemplateDefnBPEOStarRatingEnabledFlag | — |
| STATUS_CODE | TemplateDefnBPEOStatusCode | — |
| TEMPLATE_DEFN_ID | TemplateDefnBPEOTemplateDefnId | — |

### [[performancedocumentstatuspvo|PerformanceDocumentStatusPVO]] (HCM · BICC: 3/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplateDefnBPEOBusinessGroupId | ✅ |
| CALCULATE_RATINGS_FLAG | TemplateDefnBPEOCalculateRatingsFlag | — |
| DATE_FROM | TemplateDefnBPEODateFrom | — |
| DATE_TO | TemplateDefnBPEODateTo | — |
| DECIMAL_PLACES | TemplateDefnBPEODecimalPlaces | — |
| DOC_TYPE_ID | TemplateDefnBPEODocTypeId | — |
| LAST_UPDATE_DATE | TemplateDefnBPEOLastUpdateDate | ✅ |
| MAPPING_METHOD_CODE | TemplateDefnBPEOMappingMethodCode | — |
| PROCESS_FLOW_ID | TemplateDefnBPEOProcessFlowId | — |
| ROUNDING_RULE_CODE | TemplateDefnBPEORoundingRuleCode | — |
| SELECT_MGR_ALLOWED_FLAG | TemplateDefnBPEOSelectMgrAllowedFlag | — |
| SET_ID | TemplateDefnBPEOSetId | — |
| SHOW_PARTICIPANT_NAMES | TemplateDefnBPEOShowParticipantNames | — |
| STAR_RATING_ENABLED_FLAG | TemplateDefnBPEOStarRatingEnabledFlag | — |
| STATUS_CODE | TemplateDefnBPEOStatusCode | — |
| TEMPLATE_DEFN_ID | TemplateDefnBPEOTemplateDefnId | ✅ |

### [[performanceitemratingpvo|PerformanceItemRatingPVO]] (HCM · BICC: 1/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplateDefnBPEOBusinessGroupId | — |
| CALCULATE_RATINGS_FLAG | TemplateDefnBPEOCalculateRatingsFlag | — |
| DATE_FROM | TemplateDefnBPEODateFrom | — |
| DATE_TO | TemplateDefnBPEODateTo | — |
| DECIMAL_PLACES | TemplateDefnBPEODecimalPlaces | — |
| DOC_TYPE_ID | TemplateDefnBPEODocTypeId | — |
| LAST_UPDATE_DATE | TemplateDefnBPEOLastUpdateDate | ✅ |
| MAPPING_METHOD_CODE | TemplateDefnBPEOMappingMethodCode | — |
| PROCESS_FLOW_ID | TemplateDefnBPEOProcessFlowId | — |
| ROUNDING_RULE_CODE | TemplateDefnBPEORoundingRuleCode | — |
| SELECT_MGR_ALLOWED_FLAG | TemplateDefnBPEOSelectMgrAllowedFlag | — |
| SET_ID | TemplateDefnBPEOSetId | — |
| SHOW_PARTICIPANT_NAMES | TemplateDefnBPEOShowParticipantNames | — |
| STAR_RATING_ENABLED_FLAG | TemplateDefnBPEOStarRatingEnabledFlag | — |
| STATUS_CODE | TemplateDefnBPEOStatusCode | — |
| TEMPLATE_DEFN_ID | TemplateDefnBPEOTemplateDefnId | — |

### [[performanceoverallratingpvo|PerformanceOverallRatingPVO]] (HCM · BICC: 1/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplateDefnBPEOBusinessGroupId | — |
| CALCULATE_RATINGS_FLAG | TemplateDefnBPEOCalculateRatingsFlag | — |
| DATE_FROM | TemplateDefnBPEODateFrom | — |
| DATE_TO | TemplateDefnBPEODateTo | — |
| DECIMAL_PLACES | TemplateDefnBPEODecimalPlaces | — |
| DOC_TYPE_ID | TemplateDefnBPEODocTypeId | — |
| LAST_UPDATE_DATE | TemplateDefnBPEOLastUpdateDate | ✅ |
| MAPPING_METHOD_CODE | TemplateDefnBPEOMappingMethodCode | — |
| PROCESS_FLOW_ID | TemplateDefnBPEOProcessFlowId | — |
| ROUNDING_RULE_CODE | TemplateDefnBPEORoundingRuleCode | — |
| SELECT_MGR_ALLOWED_FLAG | TemplateDefnBPEOSelectMgrAllowedFlag | — |
| SET_ID | TemplateDefnBPEOSetId | — |
| SHOW_PARTICIPANT_NAMES | TemplateDefnBPEOShowParticipantNames | — |
| STAR_RATING_ENABLED_FLAG | TemplateDefnBPEOStarRatingEnabledFlag | — |
| STATUS_CODE | TemplateDefnBPEOStatusCode | — |
| TEMPLATE_DEFN_ID | TemplateDefnBPEOTemplateDefnId | — |

### [[performancesectionratingpvo|PerformanceSectionRatingPVO]] (HCM · BICC: 1/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplateDefnBPEOBusinessGroupId4 | — |
| CALCULATE_RATINGS_FLAG | TemplateDefnBPEOCalculateRatingsFlag | — |
| DATE_FROM | TemplateDefnBPEODateFrom | — |
| DATE_TO | TemplateDefnBPEODateTo | — |
| DECIMAL_PLACES | TemplateDefnBPEODecimalPlaces | — |
| DOC_TYPE_ID | TemplateDefnBPEODocTypeId | — |
| LAST_UPDATE_DATE | TemplateDefnBPEOLastUpdateDate | ✅ |
| MAPPING_METHOD_CODE | TemplateDefnBPEOMappingMethodCode | — |
| PROCESS_FLOW_ID | TemplateDefnBPEOProcessFlowId | — |
| ROUNDING_RULE_CODE | TemplateDefnBPEORoundingRuleCode | — |
| SELECT_MGR_ALLOWED_FLAG | TemplateDefnBPEOSelectMgrAllowedFlag | — |
| SET_ID | TemplateDefnBPEOSetId | — |
| SHOW_PARTICIPANT_NAMES | TemplateDefnBPEOShowParticipantNames | — |
| STAR_RATING_ENABLED_FLAG | TemplateDefnBPEOStarRatingEnabledFlag | — |
| STATUS_CODE | TemplateDefnBPEOStatusCode | — |
| TEMPLATE_DEFN_ID | TemplateDefnBPEOTemplateDefnId | — |

### [[performancesubtaskstatuspvo|PerformanceSubTaskStatusPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplateDefnBPEOBusinessGroupId | — |
| CALCULATE_RATINGS_FLAG | TemplateDefnBPEOCalculateRatingsFlag | — |
| DATE_FROM | TemplateDefnBPEODateFrom | — |
| DATE_TO | TemplateDefnBPEODateTo | — |
| DECIMAL_PLACES | TemplateDefnBPEODecimalPlaces | — |
| DOC_TYPE_ID | TemplateDefnBPEODocTypeId | — |
| MAPPING_METHOD_CODE | TemplateDefnBPEOMappingMethodCode | — |
| PROCESS_FLOW_ID | TemplateDefnBPEOProcessFlowId | — |
| ROUNDING_RULE_CODE | TemplateDefnBPEORoundingRuleCode | — |
| SELECT_MGR_ALLOWED_FLAG | TemplateDefnBPEOSelectMgrAllowedFlag | — |
| SET_ID | TemplateDefnBPEOSetId | — |
| SHOW_PARTICIPANT_NAMES | TemplateDefnBPEOShowParticipantNames | — |
| STAR_RATING_ENABLED_FLAG | TemplateDefnBPEOStarRatingEnabledFlag | — |
| STATUS_CODE | TemplateDefnBPEOStatusCode | — |
| TEMPLATE_DEFN_ID | TemplateDefnBPEOTemplateDefnId | — |

### [[performancetaskstatuspvo|PerformanceTaskStatusPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplateDefnBPEOBusinessGroupId | — |
| CALCULATE_RATINGS_FLAG | TemplateDefnBPEOCalculateRatingsFlag | — |
| DATE_FROM | TemplateDefnBPEODateFrom | — |
| DATE_TO | TemplateDefnBPEODateTo | — |
| DECIMAL_PLACES | TemplateDefnBPEODecimalPlaces | — |
| DOC_TYPE_ID | TemplateDefnBPEODocTypeId | — |
| MAPPING_METHOD_CODE | TemplateDefnBPEOMappingMethodCode | — |
| PROCESS_FLOW_ID | TemplateDefnBPEOProcessFlowId | — |
| ROUNDING_RULE_CODE | TemplateDefnBPEORoundingRuleCode | — |
| SELECT_MGR_ALLOWED_FLAG | TemplateDefnBPEOSelectMgrAllowedFlag | — |
| SET_ID | TemplateDefnBPEOSetId | — |
| SHOW_PARTICIPANT_NAMES | TemplateDefnBPEOShowParticipantNames | — |
| STAR_RATING_ENABLED_FLAG | TemplateDefnBPEOStarRatingEnabledFlag | — |
| STATUS_CODE | TemplateDefnBPEOStatusCode | — |
| TEMPLATE_DEFN_ID | TemplateDefnBPEOTemplateDefnId | — |

### [[proficiencyitemratingpvo|ProficiencyItemRatingPVO]] (HCM · BICC: 1/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplateDefnBPEOBusinessGroupId | — |
| CALCULATE_RATINGS_FLAG | TemplateDefnBPEOCalculateRatingsFlag | — |
| DATE_FROM | TemplateDefnBPEODateFrom | — |
| DATE_TO | TemplateDefnBPEODateTo | — |
| DECIMAL_PLACES | TemplateDefnBPEODecimalPlaces | — |
| DOC_TYPE_ID | TemplateDefnBPEODocTypeId | — |
| LAST_UPDATE_DATE | TemplateDefnBPEOLastUpdateDate | ✅ |
| MAPPING_METHOD_CODE | TemplateDefnBPEOMappingMethodCode | — |
| PROCESS_FLOW_ID | TemplateDefnBPEOProcessFlowId | — |
| ROUNDING_RULE_CODE | TemplateDefnBPEORoundingRuleCode | — |
| SELECT_MGR_ALLOWED_FLAG | TemplateDefnBPEOSelectMgrAllowedFlag | — |
| SET_ID | TemplateDefnBPEOSetId | — |
| SHOW_PARTICIPANT_NAMES | TemplateDefnBPEOShowParticipantNames | — |
| STAR_RATING_ENABLED_FLAG | TemplateDefnBPEOStarRatingEnabledFlag | — |
| STATUS_CODE | TemplateDefnBPEOStatusCode | — |
| TEMPLATE_DEFN_ID | TemplateDefnBPEOTemplateDefnId | — |

### [[templatedefnpvo|TemplateDefnPVO]] (HCM · BICC: 23/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CALCULATE_RATINGS_FLAG | TemplateDefnBPEOCalculateRatingsFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_FROM | TemplateDefnBPEODateFrom | ✅ |
| DATE_TO | TemplateDefnBPEODateTo | ✅ |
| DECIMAL_PLACES | TemplateDefnBPEODecimalPlaces | — |
| DOC_TYPE_ID | TemplateDefnBPEODocTypeId | ✅ |
| KUDOS_REGION_FLAG | TemplateDefnBPEOKudosRegionFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MAPPING_METHOD_CODE | TemplateDefnBPEOMappingMethodCode | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PROCESS_FLOW_ID | TemplateDefnBPEOProcessFlowId | — |
| ROUNDING_RULE_CODE | TemplateDefnBPEORoundingRuleCode | ✅ |
| SELECT_MGR_ALLOWED_FLAG | TemplateDefnBPEOSelectMgrAllowedFlag | ✅ |
| SET_ID | TemplateDefnBPEOSetId | — |
| SET_ROLE_MINIMUMS_FLAG | TemplateDefnBPEOSetRoleMinimumsFlag | ✅ |
| SHOW_CHECK_IN_REGION_FLAG | TemplateDefnBPEOShowCheckInRegionFlag | ✅ |
| SHOW_FEEDBACK_REQ_REGION_FLAG | TemplateDefnBPEOShowFeedbackReqRegionFlag | ✅ |
| SHOW_PARTICIPANT_NAMES | TemplateDefnBPEOShowParticipantNames | ✅ |
| STAR_RATING_ENABLED_FLAG | TemplateDefnBPEOStarRatingEnabledFlag | ✅ |
| STATUS_CODE | TemplateDefnBPEOStatusCode | ✅ |
| TEMPLATE_DEFN_ID | TemplateDefnId | ✅ |
| TEMPLATE_TYPE_CODE | TemplateTypeCode | ✅ |
| TOTAL_MIN_PARTICIPANTS | TemplateDefnBPEOTotalMinParticipants | ✅ |

---

## 📚 Referências

- [Oracle Docs — HRA_TMPL_DEFNS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hratmpldefnsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
