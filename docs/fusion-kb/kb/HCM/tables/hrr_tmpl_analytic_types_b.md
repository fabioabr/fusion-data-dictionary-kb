---
id: DOC-HCM-210
doc_type: system-doc
title: "HRR_TMPL_ANALYTIC_TYPES_B — Tipos Analíticos de Template (Base)"
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
  - talent-review
  - analytics
aliases:
  - HRR_TMPL_ANALYTIC_TYPES_B
  - hrr_tmpl_analytic_types_b
  - tipos-analíticos-de-template-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRR_TMPL_ANALYTIC_TYPES_B

## 📌 Visão Geral

Tabela base dos **tipos analíticos** de templates de Talent Review (9-Box, etc.).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração:** Tipos de análise (9-Box, Performance Grid).
- **Dimensões analíticas:** Eixos e categorizações.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ANALYTIC_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | TEMPLATE_ID | NUMBER(18) | NOT NULL | FK | Template de dashboard | [[hrr_dashboard_tmpls_b]] | 🟢 85% |
| 3 | ANALYTIC_TYPE_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código do tipo | — | 🟡 80% |
| 4 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 9 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrr_dashboard_tmpls_b]] — via `TEMPLATE_ID` (template do tipo analitico de talent review)

### Tabelas-filha

### Tabelas relacionadas

---

## 📎 Uso Típico

### Tipos analíticos
```sql
SELECT at_.ANALYTIC_TYPE_ID, at_.ANALYTIC_TYPE_CODE
FROM   HRR_TMPL_ANALYTIC_TYPES_B at_
WHERE  at_.TEMPLATE_ID = :p_id;
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrr_tmpl_analytic_types_tl]].

---

## 🔗 PVOs Relacionados

### [[boxlabellookuppvo|BoxLabelLookupPVO]] (HCM · BICC: 1/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANALYTIC_TYPE_CODE | AnalyticTypeCode | — |
| ANALYTIC_TYPE_ID | AnalyticTypeId | — |
| ANALYTIC_VIEW_MODE | AnalyticViewMode | — |
| BUSINESS_GROUP_ID | TmplAnalyticTypeBPEOBusinessGroupId | — |
| COLOR_SCHEME_CODE | ColorSchemeCode | — |
| CREATED_BY | TmplAnalyticTypeBPEOCreatedBy | — |
| CREATION_DATE | TmplAnalyticTypeBPEOCreationDate | — |
| DASHBOARD_TMPL_ID | TmplAnalyticTypeBPEODashboardTmplId | — |
| HORIZONTAL_AXIS_CODE | HorizontalAxisCode | — |
| LAST_UPDATE_DATE | TmplAnalyticTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TmplAnalyticTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TmplAnalyticTypeBPEOLastUpdatedBy | — |
| MODULE_ID | TmplAnalyticTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | TmplAnalyticTypeBPEOObjectVersionNumber | — |
| SUBMIT_BOX_ASGNMNT_FLAG | SubmitBoxAsgnmntFlag | — |
| VERTICAL_AXIS_CODE | VerticalAxisCode | — |

### [[nboxdimensionpvo|NBoxDimensionPVO]] (HCM · BICC: 3/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANALYTIC_TYPE_CODE | TemplateAnalyticTypeBPEOAnalyticTypeCode | — |
| ANALYTIC_TYPE_ID | TemplateAnalyticTypeBPEOAnalyticTypeId | ✅ |
| ANALYTIC_VIEW_MODE | TemplateAnalyticTypeBPEOAnalyticViewMode | — |
| BUSINESS_GROUP_ID | TemplateAnalyticTypeBPEOBusinessGroupId | ✅ |
| COLOR_SCHEME_CODE | TemplateAnalyticTypeBPEOColorSchemeCode | — |
| CREATED_BY | TemplateAnalyticTypeBPEOCreatedBy | — |
| CREATION_DATE | TemplateAnalyticTypeBPEOCreationDate | — |
| DASHBOARD_TMPL_ID | TemplateAnalyticTypeBPEODashboardTmplId | — |
| DEFAULT_VIEW_FLAG | TemplateAnalyticTypeBPEODefaultViewFlag | — |
| HORIZONTAL_AXIS_CODE | TemplateAnalyticTypeBPEOHorizontalAxisCode | — |
| LAST_UPDATE_DATE | TemplateAnalyticTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplateAnalyticTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TemplateAnalyticTypeBPEOLastUpdatedBy | — |
| METRIC_CODE | TemplateAnalyticTypeBPEOMetricCode | — |
| MODULE_ID | TemplateAnalyticTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | TemplateAnalyticTypeBPEOObjectVersionNumber | — |
| SUBMIT_BOX_ASGNMNT_FLAG | TemplateAnalyticTypeBPEOSubmitBoxAsgnmntFlag | — |
| VERTICAL_AXIS_CODE | TemplateAnalyticTypeBPEOVerticalAxisCode | — |
| VIEW_COLUMN_COUNT | TemplateAnalyticTypeBPEOViewColumnCount | — |
| VIEW_ROW_COUNT | TemplateAnalyticTypeBPEOViewRowCount | — |

### [[nboxlabelpvo|NBoxLabelPVO]] (HCM · BICC: 1/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANALYTIC_TYPE_CODE | AnalyticTypeCode | — |
| ANALYTIC_TYPE_ID | AnalyticTypeId | — |
| ANALYTIC_VIEW_MODE | AnalyticViewMode | — |
| BUSINESS_GROUP_ID | TmplAnalyticTypeBPEOBusinessGroupId | — |
| COLOR_SCHEME_CODE | ColorSchemeCode | — |
| CREATED_BY | TmplAnalyticTypeBPEOCreatedBy | — |
| CREATION_DATE | TmplAnalyticTypeBPEOCreationDate | — |
| DASHBOARD_TMPL_ID | TmplAnalyticTypeBPEODashboardTmplId | — |
| HORIZONTAL_AXIS_CODE | HorizontalAxisCode | — |
| LAST_UPDATE_DATE | TmplAnalyticTypeBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TmplAnalyticTypeBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TmplAnalyticTypeBPEOLastUpdatedBy | — |
| MODULE_ID | TmplAnalyticTypeBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | TmplAnalyticTypeBPEOObjectVersionNumber | — |
| SUBMIT_BOX_ASGNMNT_FLAG | SubmitBoxAsgnmntFlag | — |
| VERTICAL_AXIS_CODE | VerticalAxisCode | — |

### [[performancepotentialboxsequencepvo|PerformancePotentialBoxSequencePVO]] (HCM · BICC: 2/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANALYTIC_TYPE_ID | TemplateAnalyticTypeBPEOAnalyticTypeId | ✅ |
| ANALYTIC_VIEW_MODE | TemplateAnalyticTypeBPEOAnalyticViewMode | — |
| BUSINESS_GROUP_ID | TemplateAnalyticTypeBPEOBusinessGroupId | — |
| HORIZONTAL_AXIS_CODE | TemplateAnalyticTypeBPEOHorizontalAxisCode | — |
| LAST_UPDATE_DATE | TemplateAnalyticTypeBPEOLastUpdateDate | ✅ |
| METRIC_CODE | TemplateAnalyticTypeBPEOMetricCode | — |
| SUBMIT_BOX_ASGNMNT_FLAG | TemplateAnalyticTypeBPEOSubmitBoxAsgnmntFlag | — |
| VERTICAL_AXIS_CODE | TemplateAnalyticTypeBPEOVerticalAxisCode | — |

### [[performancepotentialboxsequencepvo_viewall|PerformancePotentialBoxSequencePVO_Viewall]] (HCM · BICC: 2/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANALYTIC_TYPE_ID | TemplateAnalyticTypeBPEOAnalyticTypeId | ✅ |
| ANALYTIC_VIEW_MODE | TemplateAnalyticTypeBPEOAnalyticViewMode | — |
| BUSINESS_GROUP_ID | TemplateAnalyticTypeBPEOBusinessGroupId | — |
| HORIZONTAL_AXIS_CODE | TemplateAnalyticTypeBPEOHorizontalAxisCode | — |
| LAST_UPDATE_DATE | TemplateAnalyticTypeBPEOLastUpdateDate | ✅ |
| METRIC_CODE | TemplateAnalyticTypeBPEOMetricCode | — |
| SUBMIT_BOX_ASGNMNT_FLAG | TemplateAnalyticTypeBPEOSubmitBoxAsgnmntFlag | — |
| VERTICAL_AXIS_CODE | TemplateAnalyticTypeBPEOVerticalAxisCode | — |

### [[talentscoreboxlabellookuppvo|TalentScoreBoxLabelLookupPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANALYTIC_TYPE_CODE | AnalyticTypeCode | — |
| ANALYTIC_TYPE_ID | AnalyticTypeId | — |
| ANALYTIC_VIEW_MODE | AnalyticViewMode | — |
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| METRIC_CODE | MetricCode | — |
| SUBMIT_BOX_ASGNMNT_FLAG | SubmitBoxAsgnmntFlag | — |

### [[talentscoreboxsequencepvo|TalentScoreBoxSequencePVO]] (HCM · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANALYTIC_TYPE_ID | TemplateAnalyticTypeBPEOAnalyticTypeId | ✅ |
| ANALYTIC_VIEW_MODE | TemplateAnalyticTypeBPEOAnalyticViewMode | — |
| BUSINESS_GROUP_ID | TemplateAnalyticTypeBPEOBusinessGroupId | — |
| HORIZONTAL_AXIS_CODE | TemplateAnalyticTypeBPEOHorizontalAxisCode | — |
| LAST_UPDATE_DATE | TemplateAnalyticTypeBPEOLastUpdateDate | — |
| METRIC_CODE | TemplateAnalyticTypeBPEOMetricCode | — |
| SUBMIT_BOX_ASGNMNT_FLAG | TemplateAnalyticTypeBPEOSubmitBoxAsgnmntFlag | — |
| VERTICAL_AXIS_CODE | TemplateAnalyticTypeBPEOVerticalAxisCode | — |

### [[talentscoreboxsequencepvo_viewall|TalentScoreBoxSequencePVO_Viewall]] (HCM · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANALYTIC_TYPE_ID | TemplateAnalyticTypeBPEOAnalyticTypeId | ✅ |
| ANALYTIC_VIEW_MODE | TemplateAnalyticTypeBPEOAnalyticViewMode | — |
| BUSINESS_GROUP_ID | TemplateAnalyticTypeBPEOBusinessGroupId | — |
| HORIZONTAL_AXIS_CODE | TemplateAnalyticTypeBPEOHorizontalAxisCode | — |
| LAST_UPDATE_DATE | TemplateAnalyticTypeBPEOLastUpdateDate | — |
| METRIC_CODE | TemplateAnalyticTypeBPEOMetricCode | — |
| SUBMIT_BOX_ASGNMNT_FLAG | TemplateAnalyticTypeBPEOSubmitBoxAsgnmntFlag | — |
| VERTICAL_AXIS_CODE | TemplateAnalyticTypeBPEOVerticalAxisCode | — |

### [[templateanalytictypepvo|TemplateAnalyticTypePVO]] (HCM · BICC: 20/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANALYTIC_TYPE_CODE | AnalyticTypeCode | ✅ |
| ANALYTIC_TYPE_ID | AnalyticTypeId | ✅ |
| ANALYTIC_VIEW_MODE | AnalyticViewMode | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| COLOR_SCHEME_CODE | ColorSchemeCode | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DASHBOARD_TMPL_ID | DashboardTmplId | ✅ |
| DEFAULT_VIEW_FLAG | DefaultViewFlag | ✅ |
| HORIZONTAL_AXIS_CODE | HorizontalAxisCode | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| METRIC_CODE | MetricCode | ✅ |
| MODULE_ID | ModuleId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| SUBMIT_BOX_ASGNMNT_FLAG | SubmitBoxAsgnmntFlag | ✅ |
| VERTICAL_AXIS_CODE | VerticalAxisCode | ✅ |
| VIEW_COLUMN_COUNT | ViewColumnCount | ✅ |
| VIEW_ROW_COUNT | ViewRowCount | ✅ |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
