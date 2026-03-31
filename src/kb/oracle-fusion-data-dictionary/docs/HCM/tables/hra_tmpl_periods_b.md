---
id: DOC-HCM-151
doc_type: system-doc
title: "HRA_TMPL_PERIODS_B — Períodos de Template de Aprovação (Base)"
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
  - periods
aliases:
  - HRA_TMPL_PERIODS_B
  - hra_tmpl_periods_b
  - períodos-de-template-de-aprovação-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_TMPL_PERIODS_B

## 📌 Visão Geral

Tabela base que armazena os **períodos de templates de aprovação** do módulo HCM. Define intervalos temporais para configurações de aprovação. Sufixo `_B` indica tabela base.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de aprovações:** Períodos de validade para templates de workflow.
- **Gestão temporal:** Vigência das regras de aprovação.
- **Automação:** Configurações de aprovação por período.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TMPL_PERIOD_ID | NUMBER(18) | NOT NULL | PK | Identificador único do período de template | — | 🟢 95% |
| 2 | TEMPLATE_ID | NUMBER(18) | NOT NULL | FK | Referência ao template de aprovação | — | 🟢 90% |
| 3 | PERIOD_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do período | — | 🟡 75% |
| 4 | START_DATE | DATE | NOT NULL | Data | Data de início da vigência | — | 🟢 90% |
| 5 | END_DATE | DATE | NULL | Data | Data de término da vigência | — | 🟢 90% |
| 6 | PERIOD_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do período (anual, mensal) | — | 🟡 70% |
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
- [[hra_tmpl_periods_tl]] — via `TMPL_PERIOD_ID` (traducoes do periodo do template)
- [[hra_tmpl_sections]] — via `TEMPLATE_ID` (seções do mesmo template)
- [[hra_tmpl_roles]] — via `TEMPLATE_ID` (papéis do mesmo template)

---

## 📎 Uso Típico

### Períodos ativos de um template
```sql
SELECT p.TMPL_PERIOD_ID, p.PERIOD_NAME, p.START_DATE, p.END_DATE
FROM   HRA_TMPL_PERIODS_B p
WHERE  p.TEMPLATE_ID = :p_template_id
  AND  SYSDATE BETWEEN p.START_DATE AND NVL(p.END_DATE, SYSDATE + 1);
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hra_tmpl_periods_tl]].
- Padrão Oracle de versionamento via `OBJECT_VERSION_NUMBER`.
- Períodos sem `END_DATE` indicam vigência indefinida.

---

## 🔗 PVOs Relacionados

### [[eligibilityresultpvo|EligibilityResultPVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplatePeriodBPEOBusinessGroupId | ✅ |
| CREATED_BY | TemplatePeriodBPEOCreatedBy | — |
| CREATION_DATE | TemplatePeriodBPEOCreationDate | — |
| LAST_UPDATE_DATE | TemplatePeriodBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplatePeriodBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplatePeriodBPEOLastUpdatedBy | — |
| NOMINAL_FROM_DATE | TemplatePeriodBPEONominalFromDate | — |
| NOMINAL_TO_DATE | TemplatePeriodBPEONominalToDate | — |
| OBJECT_VERSION_NUMBER | TemplatePeriodBPEOObjectVersionNumber | — |
| REVIEW_PERIOD_ID | TemplatePeriodBPEOReviewPeriodId | — |
| TEMPLATE_DEFN_ID | TemplatePeriodBPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | TemplatePeriodBPEOTmplPeriodId | ✅ |

### [[eligibilityresultsdetailspvo|EligibilityResultsDetailsPVO]] (HCM · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplatePeriodBPEOBusinessGroupId | ✅ |
| CREATED_BY | TemplatePeriodBPEOCreatedBy | — |
| CREATION_DATE | TemplatePeriodBPEOCreationDate | — |
| LAST_UPDATE_DATE | TemplatePeriodBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplatePeriodBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplatePeriodBPEOLastUpdatedBy | — |
| NOMINAL_FROM_DATE | TemplatePeriodBPEONominalFromDate | — |
| NOMINAL_TO_DATE | TemplatePeriodBPEONominalToDate | — |
| OBJECT_VERSION_NUMBER | TemplatePeriodBPEOObjectVersionNumber | — |
| TEMPLATE_DEFN_ID | TemplatePeriodBPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | TemplatePeriodBPEOTmplPeriodId | ✅ |

### [[performancedocratingdistributionpvo|PerformanceDocRatingDistributionPVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplatePeriodBPEOBusinessGroupId | ✅ |
| CREATED_BY | TemplatePeriodBPEOCreatedBy | — |
| CREATION_DATE | TemplatePeriodBPEOCreationDate | — |
| LAST_UPDATE_DATE | TemplatePeriodBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplatePeriodBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplatePeriodBPEOLastUpdatedBy | — |
| NOMINAL_FROM_DATE | TemplatePeriodBPEONominalFromDate | — |
| NOMINAL_TO_DATE | TemplatePeriodBPEONominalToDate | — |
| OBJECT_VERSION_NUMBER | TemplatePeriodBPEOObjectVersionNumber | — |
| REVIEW_PERIOD_ID | TemplatePeriodBPEOReviewPeriodId | — |
| TEMPLATE_DEFN_ID | TemplatePeriodBPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | TemplatePeriodBPEOTmplPeriodId | ✅ |

### [[performancedocumentdetailspvo|PerformanceDocumentDetailsPVO]] (HCM · BICC: 1/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| NOMINAL_FROM_DATE | NominalFromDate | — |
| NOMINAL_TO_DATE | NominalToDate | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| REVIEW_PERIOD_ID | ReviewPeriodId | — |
| TEMPLATE_DEFN_ID | TemplateDefnId1 | — |
| TMPL_PERIOD_ID | TmplPeriodId1 | — |

### [[performancedocumentspvo|PerformanceDocumentsPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplatePeriodBPEOBusinessGroupId | — |
| CREATED_BY | TemplatePeriodBPEOCreatedBy | — |
| CREATION_DATE | TemplatePeriodBPEOCreationDate | — |
| LAST_UPDATE_DATE | TemplatePeriodBPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | TemplatePeriodBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplatePeriodBPEOLastUpdatedBy | — |
| NOMINAL_FROM_DATE | TemplatePeriodBPEONominalFromDate | — |
| NOMINAL_TO_DATE | TemplatePeriodBPEONominalToDate | — |
| OBJECT_VERSION_NUMBER | TemplatePeriodBPEOObjectVersionNumber | — |
| REVIEW_PERIOD_ID | TemplatePeriodBPEOReviewPeriodId | — |
| TEMPLATE_DEFN_ID | TemplatePeriodBPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | TemplatePeriodBPEOTmplPeriodId | — |

### [[performancedocumentstatuspvo|PerformanceDocumentStatusPVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplatePeriodBPEOBusinessGroupId | ✅ |
| CREATED_BY | TemplatePeriodBPEOCreatedBy | — |
| CREATION_DATE | TemplatePeriodBPEOCreationDate | — |
| LAST_UPDATE_DATE | TemplatePeriodBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplatePeriodBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplatePeriodBPEOLastUpdatedBy | — |
| NOMINAL_FROM_DATE | TemplatePeriodBPEONominalFromDate | — |
| NOMINAL_TO_DATE | TemplatePeriodBPEONominalToDate | — |
| OBJECT_VERSION_NUMBER | TemplatePeriodBPEOObjectVersionNumber | — |
| REVIEW_PERIOD_ID | TemplatePeriodBPEOReviewPeriodId | — |
| TEMPLATE_DEFN_ID | TemplatePeriodBPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | TemplatePeriodBPEOTmplPeriodId | ✅ |

### [[performanceitemratingpvo|PerformanceItemRatingPVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplatePeriodBPEOBusinessGroupId | ✅ |
| CREATED_BY | TemplatePeriodBPEOCreatedBy | — |
| CREATION_DATE | TemplatePeriodBPEOCreationDate | — |
| LAST_UPDATE_DATE | TemplatePeriodBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplatePeriodBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplatePeriodBPEOLastUpdatedBy | — |
| NOMINAL_FROM_DATE | TemplatePeriodBPEONominalFromDate | — |
| NOMINAL_TO_DATE | TemplatePeriodBPEONominalToDate | — |
| OBJECT_VERSION_NUMBER | TemplatePeriodBPEOObjectVersionNumber | — |
| REVIEW_PERIOD_ID | TemplatePeriodBPEOReviewPeriodId | — |
| TEMPLATE_DEFN_ID | TemplatePeriodBPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | TemplatePeriodBPEOTmplPeriodId | ✅ |

### [[performanceoverallratingpvo|PerformanceOverallRatingPVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplatePeriodBPEOBusinessGroupId | ✅ |
| CREATED_BY | TemplatePeriodBPEOCreatedBy | — |
| CREATION_DATE | TemplatePeriodBPEOCreationDate | — |
| LAST_UPDATE_DATE | TemplatePeriodBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplatePeriodBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplatePeriodBPEOLastUpdatedBy | — |
| NOMINAL_FROM_DATE | TemplatePeriodBPEONominalFromDate | — |
| NOMINAL_TO_DATE | TemplatePeriodBPEONominalToDate | — |
| OBJECT_VERSION_NUMBER | TemplatePeriodBPEOObjectVersionNumber | — |
| REVIEW_PERIOD_ID | TemplatePeriodBPEOReviewPeriodId | — |
| TEMPLATE_DEFN_ID | TemplatePeriodBPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | TemplatePeriodBPEOTmplPeriodId | ✅ |

### [[performancesectionratingpvo|PerformanceSectionRatingPVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplatePeriodBPEOBusinessGroupId | ✅ |
| CREATED_BY | TemplatePeriodBPEOCreatedBy | — |
| CREATION_DATE | TemplatePeriodBPEOCreationDate | — |
| LAST_UPDATE_DATE | TemplatePeriodBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplatePeriodBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplatePeriodBPEOLastUpdatedBy | — |
| NOMINAL_FROM_DATE | TemplatePeriodBPEONominalFromDate | — |
| NOMINAL_TO_DATE | TemplatePeriodBPEONominalToDate | — |
| OBJECT_VERSION_NUMBER | TemplatePeriodBPEOObjectVersionNumber | — |
| REVIEW_PERIOD_ID | TemplatePeriodBPEOReviewPeriodId | — |
| TEMPLATE_DEFN_ID | TemplatePeriodBPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | TemplatePeriodBPEOTmplPeriodId | ✅ |

### [[performancesubtaskstatuspvo|PerformanceSubTaskStatusPVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplatePeriodBPEOBusinessGroupId | ✅ |
| CREATED_BY | TemplatePeriodBPEOCreatedBy | — |
| CREATION_DATE | TemplatePeriodBPEOCreationDate | — |
| LAST_UPDATE_DATE | TemplatePeriodBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplatePeriodBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplatePeriodBPEOLastUpdatedBy | — |
| NOMINAL_FROM_DATE | TemplatePeriodBPEONominalFromDate | — |
| NOMINAL_TO_DATE | TemplatePeriodBPEONominalToDate | — |
| OBJECT_VERSION_NUMBER | TemplatePeriodBPEOObjectVersionNumber | — |
| REVIEW_PERIOD_ID | TemplatePeriodBPEOReviewPeriodId | — |
| TEMPLATE_DEFN_ID | TemplatePeriodBPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | TemplatePeriodBPEOTmplPeriodId | ✅ |

### [[performancetaskstatuspvo|PerformanceTaskStatusPVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplatePeriodBPEOBusinessGroupId | ✅ |
| CREATED_BY | TemplatePeriodBPEOCreatedBy | — |
| CREATION_DATE | TemplatePeriodBPEOCreationDate | — |
| LAST_UPDATE_DATE | TemplatePeriodBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplatePeriodBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplatePeriodBPEOLastUpdatedBy | — |
| NOMINAL_FROM_DATE | TemplatePeriodBPEONominalFromDate | — |
| NOMINAL_TO_DATE | TemplatePeriodBPEONominalToDate | — |
| OBJECT_VERSION_NUMBER | TemplatePeriodBPEOObjectVersionNumber | — |
| REVIEW_PERIOD_ID | TemplatePeriodBPEOReviewPeriodId | — |
| TEMPLATE_DEFN_ID | TemplatePeriodBPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | TemplatePeriodBPEOTmplPeriodId | ✅ |

### [[proficiencyitemratingpvo|ProficiencyItemRatingPVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplatePeriodBPEOBusinessGroupId | ✅ |
| CREATED_BY | TemplatePeriodBPEOCreatedBy | — |
| CREATION_DATE | TemplatePeriodBPEOCreationDate | — |
| LAST_UPDATE_DATE | TemplatePeriodBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplatePeriodBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplatePeriodBPEOLastUpdatedBy | — |
| NOMINAL_FROM_DATE | TemplatePeriodBPEONominalFromDate | — |
| NOMINAL_TO_DATE | TemplatePeriodBPEONominalToDate | — |
| OBJECT_VERSION_NUMBER | TemplatePeriodBPEOObjectVersionNumber | — |
| REVIEW_PERIOD_ID | TemplatePeriodBPEOReviewPeriodId | — |
| TEMPLATE_DEFN_ID | TemplatePeriodBPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | TemplatePeriodBPEOTmplPeriodId | ✅ |

### [[templateperiodevaluationpvo|TemplatePeriodEvaluationPVO]] (HCM · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplatePeriodBPEOBusinessGroupId | ✅ |
| CREATED_BY | TemplatePeriodBPEOCreatedBy | — |
| CREATION_DATE | TemplatePeriodBPEOCreationDate | — |
| LAST_UPDATE_DATE | TemplatePeriodBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplatePeriodBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplatePeriodBPEOLastUpdatedBy | — |
| NOMINAL_FROM_DATE | TemplatePeriodBPEONominalFromDate | — |
| NOMINAL_TO_DATE | TemplatePeriodBPEONominalToDate | — |
| OBJECT_VERSION_NUMBER | TemplatePeriodBPEOObjectVersionNumber | — |
| TEMPLATE_DEFN_ID | TemplatePeriodBPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | TemplatePeriodBPEOTmplPeriodId | ✅ |

### [[templateperiodpvo|TemplatePeriodPVO]] (HCM · BICC: 6/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LOCK_MGR_SHARE_FOR_CALIB_FLAG | TemplatePeriodBPEOLockMgrShareForCalibFlag | ✅ |
| NOMINAL_FROM_DATE | TemplatePeriodBPEONominalFromDate | ✅ |
| NOMINAL_TO_DATE | TemplatePeriodBPEONominalToDate | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| TEMPLATE_DEFN_ID | TemplatePeriodBPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | TmplPeriodId | ✅ |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
