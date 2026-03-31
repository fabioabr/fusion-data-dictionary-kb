---
id: DOC-HCM-152
doc_type: system-doc
title: "HRA_TMPL_PERIODS_TL — Traduções de Períodos de Template"
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
  - translation
aliases:
  - HRA_TMPL_PERIODS_TL
  - hra_tmpl_periods_tl
  - traduções-de-períodos-de-template
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_TMPL_PERIODS_TL

## 📌 Visão Geral

Tabela de **traduções** dos períodos de templates de aprovação. Padrão Oracle MLS com sufixo `_TL`.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização:** Traduções de nomes de períodos em múltiplos idiomas.
- **Interface multilíngue:** Exibição no idioma do usuário.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TMPL_PERIOD_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do período | [[hra_tmpl_periods_b]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 4 | NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hra_tmpl_periods_b]] — via `TMPL_PERIOD_ID` (registro base do cadastro)

---

## 📎 Uso Típico

### Períodos traduzidos
```sql
SELECT b.TMPL_PERIOD_ID, tl.NAME, tl.DESCRIPTION
FROM   HRA_TMPL_PERIODS_B b
JOIN   HRA_TMPL_PERIODS_TL tl ON tl.TMPL_PERIOD_ID = b.TMPL_PERIOD_ID
WHERE  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Chave primária composta: `TMPL_PERIOD_ID` + `LANGUAGE`.
- Padrão MLS Oracle.

---

## 🔗 PVOs Relacionados

### [[performancedocumentdetailspvo|PerformanceDocumentDetailsPVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| CREATED_BY | CreatedBy2 | — |
| CREATION_DATE | CreationDate2 | — |
| CUSTOMARY_NAME | CustomaryName | ✅ |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin2 | — |
| LAST_UPDATED_BY | LastUpdatedBy2 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| SHORT_NAME | ShortName | ✅ |
| SOURCE_LANG | SourceLang | — |
| TMPL_PERIOD_ID | TmplPeriodId2 | — |

### [[templateperiodevaluationpvo|TemplatePeriodEvaluationPVO]] (HCM · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplatePeriodTlPEOBusinessGroupId2 | — |
| CREATED_BY | TemplatePeriodTlPEOCreatedBy2 | — |
| CREATION_DATE | TemplatePeriodTlPEOCreationDate2 | — |
| CUSTOMARY_NAME | TemplatePeriodTLPEOCustomaryName | ✅ |
| LANGUAGE | TemplatePeriodTlPEOLanguage | ✅ |
| LAST_UPDATE_DATE | TemplatePeriodTlPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | TemplatePeriodTlPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | TemplatePeriodTlPEOLastUpdatedBy2 | — |
| OBJECT_VERSION_NUMBER | TemplatePeriodTlPEOObjectVersionNumber2 | — |
| SHORT_NAME | TemplatePeriodTlPEOShortName | ✅ |
| SOURCE_LANG | TemplatePeriodTlPEOSourceLang | — |
| TMPL_PERIOD_ID | TemplatePeriodTlPEOTmplPeriodId2 | — |

### [[templateperiodpvo|TemplatePeriodPVO]] (HCM · BICC: 4/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplatePeriodTranslationPEOBusinessGroupId | — |
| CUSTOMARY_NAME | TemplatePeriodTranslationPEOCustomaryName | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | TemplatePeriodTranslationPEOLastUpdateDate | ✅ |
| SHORT_NAME | TemplatePeriodTranslationPEOShortName | ✅ |
| SOURCE_LANG | SourceLang | — |
| TMPL_PERIOD_ID | TemplatePeriodTranslationPEOTmplPeriodId | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
